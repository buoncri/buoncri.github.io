---
layout: post
title: "Fix: badge color per status e priority con stable id invece di label tradotta (PR #1371)"
date: 2026-08-06 10:10:37 +0200
categories: [django-helpdesk, open-source]
tags: [django, helpdesk, contribuzione]
author: buoncri
---
{% raw %}
Contributo a [django-helpdesk/django-helpdesk](https://github.com/django-helpdesk/django-helpdesk) — **Pull Request #1371**.

- **Link GitHub:** [PR #1371 — fix: key status/priority badge color by stable id, not localized label](https://github.com/django-helpdesk/django-helpdesk/pull/1371)
- **Stato:** Merged il 2026-08-07
- **Riferimenti:** Ref #1363

## Sommario

I colori dei badge per status e priorità nella lista ticket erano mappati sulla label visualizzata (tradotta tramite `{% translate %}`) e su una mappa hardcoded lato client. Con locale non-inglese o con label personalizzate dall'amministratore i badge cadevano in fallback grigio.

La PR sposta la logica a una singola source of truth lato server, chiave su **stable id** invece che su stringa tradotta.

## Dettagli tecnici

- Nuove settings `HELPDESK_TICKET_STATUS_CSS_CLASSES` e `HELPDESK_TICKET_PRIORITY_CSS_CLASSES`: dizionari con chiave l'id stabile di status/priorità e valore la classe CSS, con default che replica lo schema UI precedente.
- `Ticket.get_status_badge_class` / `get_priority_badge_class` leggono dalle settings; il legacy `get_priority_css_class` (usato per `row_class` e template non-datatables) è preservato per compatibilità API.
- `DatatablesTicketSerializer` espone `status_badge_class` e `priority_badge_class` per riga.
- `ticket_list.html` renderizza da `row.*_badge_class` con fallback `secondary`; rimossi `contextMaps` hardcoded e le chiavi `{% translate %}` lato JS, così gli status custom ottengono un colore solo modificando le settings.

> Body originale PR: *"The ticket list badge colors were keyed by the displayed status label (translated via {% translate %}), so they broke on non-English locales and when admins renamed/replaced status labels."*

## Impatto

Badge consistenti in tutte le lingue e per status custom, configurabili senza toccare il frontend. Risolve definitivamente la classe di bug segnalata in #1361/#1363.
{% endraw %}
