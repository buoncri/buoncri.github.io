#!/usr/bin/env python3
"""
Aggiorna contrib.md con i contributi pubblici di @buoncri via GitHub Search API.

- Query: author:buoncri is:public (solo repo pubblici)
- Raggruppa per repository_url, genera panoramica + dettaglio
- Preserva esattamente la sezione ## django-helpdesk dal file esistente
- Se il file rigenerato è identico, exit 0 senza scrivere
"""
from __future__ import annotations

import json
import os
import sys
import time
import urllib.error
import urllib.request
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
CONTRIB = ROOT / "contrib.md"
QUERY = "author:buoncri is:public"
API_URL = "https://api.github.com/search/issues"
PER_PAGE = 100
EXCLUDE_FROM_GROUPS = {"django-helpdesk/django-helpdesk"}

# front matter + intro statici (mantenuti identici all'esistente)
FRONT_MATTER = """---
layout: page
title: Contributi
permalink: /contrib/
---
"""

INTRO = (
    "Raccolta dei miei contributi pubblici su GitHub — PR, issue e discussioni "
    "a cui ho partecipato come autore. Repo principale: [github.com/buoncri]"
    "(https://github.com/buoncri). Per il codice più recente vedi anche "
    "[tutti i repository](https://github.com/buoncri?tab=repositories)."
)


def gh_request(url: str, token: str) -> tuple[dict, dict]:
    headers = {
        "Accept": "application/vnd.github+json",
        "X-GitHub-Api-Version": "2022-11-28",
        "User-Agent": "update-contrib-script",
    }
    if token:
        headers["Authorization"] = f"Bearer {token}"
    req = urllib.request.Request(url, headers=headers)
    try:
        with urllib.request.urlopen(req) as resp:
            data = json.loads(resp.read().decode())
            resp_headers = {k.lower(): v for k, v in resp.headers.items()}
            return data, resp_headers
    except urllib.error.HTTPError as e:
        body = e.read().decode(errors="replace") if hasattr(e, "read") else ""
        # Rate limit handling
        if e.code in (403, 429):
            reset = e.headers.get("X-RateLimit-Reset") or e.headers.get("x-ratelimit-reset")
            remaining = e.headers.get("X-RateLimit-Remaining") or e.headers.get("x-ratelimit-remaining")
            print(f"HTTP {e.code} rate limit? remaining={remaining} reset={reset} body={body[:500]}", file=sys.stderr)
            if reset:
                try:
                    wait = int(reset) - int(time.time()) + 5
                    if wait > 0 and wait < 600:
                        print(f"Rate limited, waiting {wait}s...", file=sys.stderr)
                        time.sleep(wait)
                        return gh_request(url, token)
                except ValueError:
                    pass
        print(f"HTTPError {e.code} for {url}: {body[:1000]}", file=sys.stderr)
        raise


def fetch_all(token: str) -> tuple[list[dict], int]:
    all_items: list[dict] = []
    total_count: int | None = None
    page = 1

    # Use token if available, otherwise try unauthenticated (rate limit 10/min)
    if not token:
        print("WARN: GITHUB_TOKEN non impostato, uso richiesta non autenticata (rate limit ridotto)", file=sys.stderr)

    while True:
        url = f"{API_URL}?q={urllib.parse.quote(QUERY)}&per_page={PER_PAGE}&page={page}"
        print(f"Fetching page {page}: {url}", file=sys.stderr)
        data, headers = gh_request(url, token)

        if total_count is None:
            total_count = int(data.get("total_count", 0))
            print(f"total_count={total_count} incomplete={data.get('incomplete_results')}", file=sys.stderr)

        items = data.get("items", [])
        all_items.extend(items)

        # Rate limit log
        remaining = headers.get("x-ratelimit-remaining")
        reset = headers.get("x-ratelimit-reset")
        if remaining is not None:
            print(f"  -> got {len(items)} items, remaining={remaining} reset={reset}", file=sys.stderr)

        if len(items) < PER_PAGE:
            break
        if len(all_items) >= (total_count or 0):
            break
        page += 1
        # Gentle pause to avoid secondary rate limits
        time.sleep(0.5)
        if page > 20:  # safety: 20*100 = 2000
            print("Stop pagination at page 20 (safety)", file=sys.stderr)
            break

    # GitHub Search API caps total_count at 1000, but our dataset is ~64
    return all_items, total_count or len(all_items)


def extract_repo_full(repository_url: str) -> str:
    # https://api.github.com/repos/owner/repo -> owner/repo
    prefix = "https://api.github.com/repos/"
    if repository_url.startswith(prefix):
        return repository_url[len(prefix):]
    # fallback: try html_url parsing
    return repository_url.rsplit("/", 2)[-2] + "/" + repository_url.rsplit("/", 1)[-1]


def group_by_repo(items: list[dict]) -> dict[str, list[dict]]:
    groups: dict[str, list[dict]] = defaultdict(list)
    for it in items:
        repo = extract_repo_full(it.get("repository_url", ""))
        if not repo or repo == "/":
            continue
        groups[repo].append(it)
    # sort each group's items by created_at desc
    for repo in groups:
        groups[repo].sort(key=lambda x: x.get("created_at", ""), reverse=True)
    return groups


REPO_TIPO = {
    "buoncri/iiot-irrigation-telecontrol": "PR — piattaforma IIoT telecontrollo",
    "waifung0207/ci_bootstrap_3": "issue/PR (CodeIgniter, storico)",
    "kimai/kimai": "PR/issue — traduzioni it, calendario",
    "scoumbourdis/grocery-crud": "PR/issue — traduzioni, fix",
}

REPO_DESC = {
    "buoncri/iiot-irrigation-telecontrol": "Piattaforma IIoT per telecontrollo impianti idrici (Docker Compose).",
    "waifung0207/ci_bootstrap_3": "Storico CodeIgniter — discussioni e PR 2015–2016.",
    "kimai/kimai": "Time-tracking open-source — contributi traduzioni italiane e issue calendario.",
}


def extract_django_section(text: str) -> str:
    start_marker = "## django-helpdesk"
    end_marker = "## Altri contributi pubblici"
    start = text.find(start_marker)
    end = text.find(end_marker)
    if start == -1:
        print("WARN: marker ## django-helpdesk non trovato, uso fallback vuoto", file=sys.stderr)
        return ""
    if end == -1:
        section = text[start:].rstrip()
    else:
        section = text[start:end].rstrip()
    # Rimuovi separatore finale "---" che precede "## Altri" (lo rigeneriamo noi)
    section = section.strip()
    # se finisce con "---", rimuovilo con eventuale whitespace
    if section.endswith("---"):
        section = section[: -len("---")].rstrip()
    return section.strip()


def tipo_for_group(items: list[dict]) -> str:
    has_pr = sum(1 for i in items if "pull_request" in i)
    if has_pr == len(items):
        return "PR"
    if has_pr == 0:
        return "issue"
    return "PR/issue"


def generate_contrib(groups: dict[str, list[dict]], total_count: int, date_str: str, existing_text: str) -> str:
    # Filter out django-helpdesk from dynamic groups (preservata staticamente)
    filtered = {k: v for k, v in groups.items() if k not in EXCLUDE_FROM_GROUPS}

    # Panoramica: sort by count desc, poi per data più recente desc, poi repo asc
    def latest_date(items: list[dict]) -> str:
        return max((it.get("created_at", "") for it in items), default="")

    # stable sort: repo asc -> date desc -> count desc
    sorted_repos = sorted(filtered.items(), key=lambda kv: kv[0].lower())
    sorted_repos = sorted(sorted_repos, key=lambda kv: latest_date(kv[1]), reverse=True)
    sorted_repos = sorted(sorted_repos, key=lambda kv: len(kv[1]), reverse=True)

    # Singles
    singles = [(k, v) for k, v in sorted_repos if len(v) == 1]
    multi = [(k, v) for k, v in sorted_repos if len(v) > 1]

    singles_count = len(singles)
    # Singles: sort by latest date desc (come in file esistente), poi repo asc
    def single_latest(kv):
        return max((it.get("created_at", "") for it in kv[1]), default="")

    singles_sorted = sorted(singles, key=lambda kv: kv[0].lower())
    singles_sorted = sorted(singles_sorted, key=lambda kv: single_latest(kv), reverse=True)

    django_section = extract_django_section(existing_text)
    if not django_section:
        # fallback hardcoded: keep minimal placeholder (should not happen)
        django_section = (
            "## django-helpdesk {#django-helpdesk}\n\n"
            "Contributi al progetto open-source [django-helpdesk/django-helpdesk]"
            "(https://github.com/django-helpdesk/django-helpdesk) — helpdesk/ticketing per Django.\n"
        )

    parts: list[str] = []
    parts.append(FRONT_MATTER)
    parts.append(INTRO)
    parts.append("")
    # Nota
    parts.append(
        f"> **Nota:** elenco raggruppato per repository, generato il **{date_str}** "
        f"via GitHub Search API (`search/issues?q=author:buoncri is:public`, "
        f"{total_count} risultati totali — solo repository pubblici). I conteggi includono PR e issue. "
        f'Sotto trovi dettaglio per i repo con più attività; i singoli contributi minori sono in coda in "Altri".'
    )
    parts.append("")
    parts.append("## Panoramica")
    parts.append("")
    parts.append("| Repository | Contributi | Tipo |")
    parts.append("|---|---|---|")
    # django-helpdesk fisso 13 (statico, non da API) — sempre primo in tabella
    parts.append("| [django-helpdesk/django-helpdesk](https://github.com/django-helpdesk/django-helpdesk) | 13 | PR/issue esterni (dettaglio sotto) |")
    for repo, items in sorted_repos:
        cnt = len(items)
        tipo = REPO_TIPO.get(repo, tipo_for_group(items))
        parts.append(f"| [{repo}](https://github.com/{repo}) | {cnt} | {tipo} |")
    if singles_count > 0:
        # Rimosso dai singoli già contati sopra? No, li abbiamo già messi come righe singole
        # Invece la tabella originale raggruppa i singoli in un'unica riga "Altri (singoli) | 16 | ..."
        # Per non duplicare, rimuoviamo le righe singole e sostituiamo con riga aggregata.
        # Quindi rifacciamo: rimuovi ultime singles_count righe e aggiungi aggregata.
        # Implementazione: togli le righe singole appena aggiunte
        if singles_count:
            # remove last singles_count entries
            parts = parts[: -singles_count]
            parts.append(f"| Altri (singoli) | {singles_count} | 1 contributo ciascuno (vedi sotto) |")
    parts.append("")
    parts.append("---")
    parts.append("")
    parts.append(django_section)
    parts.append("")
    parts.append("---")
    parts.append("")
    parts.append("## Altri contributi pubblici")
    parts.append("")
    parts.append(
        "Per non creare centinaia di post, qui sotto trovi i contributi raggruppati per repository "
        "con conteggio e 3–5 voci recenti/più rilevanti (titolo + link + stato). "
        "Lista completa su GitHub: `https://github.com/search?q=author%3Abuoncri&type=issues`."
    )
    parts.append("")

    if multi:
        for repo, items in multi:
            parts.append(f"### [{repo}](https://github.com/{repo}) — {len(items)}")
            parts.append("")
            if repo in REPO_DESC:
                parts.append(REPO_DESC[repo])
                parts.append("")
            # prendi 5 più recenti
            for it in items[:5]:
                created = it.get("created_at", "")[:10]
                state = it.get("state", "")
                title = (it.get("title") or "").replace("\n", " ").replace("|", "\\|").strip()
                # tronca titolo lunghissimo a 120 chars come nell'esistente
                if len(title) > 120:
                    title = title[:117] + "…"
                html_url = it.get("html_url", "")
                parts.append(f"- `{created}` [{state}] [{title}]({html_url})")
            parts.append("")
    else:
        parts.append("_Nessun repository con più di un contributo trovato._")
        parts.append("")

    parts.append("---")
    parts.append("")
    parts.append("### Altri — 1 contributo ciascuno")
    parts.append("")
    parts.append("Contributi singoli su repo diversi (link diretto):")
    parts.append("")
    if singles_sorted:
        for repo, _ in singles_sorted:
            if repo == "buoncri/django-helpdesk":
                parts.append(f"- [{repo}](https://github.com/{repo}) — fork personale (1)")
            else:
                parts.append(f"- [{repo}](https://github.com/{repo}) (1)")
    else:
        parts.append("- _Nessun contributo singolo._")
    parts.append("")
    parts.append(
        "> Per l'elenco completo e aggiornato: [github.com/buoncri?tab=repositories]"
        "(https://github.com/buoncri?tab=repositories) e ricerca GitHub "
        "[`author:buoncri`](https://github.com/search?q=author%3Abuoncri&type=issues)."
    )
    parts.append("")

    content = "\n".join(parts)
    # ensure ends with single newline
    if not content.endswith("\n"):
        content += "\n"
    return content


def main() -> int:
    token = os.environ.get("GITHUB_TOKEN", "").strip()
    date_str = datetime.now(timezone.utc).date().isoformat()

    if not CONTRIB.exists():
        print(f"ERRORE: {CONTRIB} non trovato", file=sys.stderr)
        return 1

    existing = CONTRIB.read_text(encoding="utf-8")

    try:
        items, total_count = fetch_all(token)
    except Exception as e:
        print(f"Fetch fallito: {e}", file=sys.stderr)
        return 1

    # Se API ritorna 0 (es. rate limit o query vuota), non sovrascrivere con file vuoto
    if total_count == 0 and not items:
        print("WARN: total_count 0, non aggiorno il file", file=sys.stderr)
        return 0

    groups = group_by_repo(items)

    # Usa total_count da API (64 attesi). Se filtered django escluso, il totale resta quello API.
    new_content = generate_contrib(groups, total_count, date_str, existing)

    if new_content == existing:
        print("Nessuna modifica a contrib.md (già aggiornato)")
        return 0

    # Mostra diff summary
    old_lines = existing.splitlines()
    new_lines = new_content.splitlines()
    print(f"Aggiornamento contrib.md: {len(old_lines)} -> {len(new_lines)} righe, total={total_count}", file=sys.stderr)

    CONTRIB.write_text(new_content, encoding="utf-8")
    print(f"Scritto {CONTRIB} con data {date_str} e {total_count} risultati")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
