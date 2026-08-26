---
layout: page
title: Contributi
permalink: /contrib/
---

Raccolta dei miei contributi pubblici su GitHub — PR, issue e discussioni a cui ho partecipato come autore. Repo principale: [github.com/buoncri](https://github.com/buoncri). Per il codice più recente vedi anche [tutti i repository](https://github.com/buoncri?tab=repositories).

> **Nota:** elenco raggruppato per repository, generato il **2026-08-26** via GitHub Search API (`search/issues?q=author:buoncri`, 335 risultati totali). I conteggi includono PR e issue. Sotto trovi dettaglio per i repo con più attività; i singoli contributi minori sono in coda in "Altri".

## Panoramica

| Repository | Contributi | Tipo |
|---|---|---|
| [buoncri/portoneniu](https://github.com/buoncri/portoneniu) | 152 | PR/issue — gestionale Django interno (formazione, istituzione) |
| [buoncri/djangocbutemplate](https://github.com/buoncri/djangocbutemplate) | 114 | PR — template Django per pratiche Consorzio |
| [django-helpdesk/django-helpdesk](https://github.com/django-helpdesk/django-helpdesk) | 13 | PR/issue esterni (dettaglio sotto) |
| [buoncri/iiot-irrigation-telecontrol](https://github.com/buoncri/iiot-irrigation-telecontrol) | 9 | PR — piattaforma IIoT telecontrollo |
| [waifung0207/ci_bootstrap_3](https://github.com/waifung0207/ci_bootstrap_3) | 9 | issue/PR (CodeIgniter, storico) |
| [buoncri/intranet_cbu](https://github.com/buoncri/intranet_cbu) | 5 | PR/issue — intranet |
| [kimai/kimai](https://github.com/kimai/kimai) | 5 | PR/issue — traduzioni it, calendario |
| [scoumbourdis/grocery-crud](https://github.com/scoumbourdis/grocery-crud) | 4 | PR/issue — traduzioni, fix |
| [buoncri/grocery-crud](https://github.com/buoncri/grocery-crud) | 2 | PR |
| [3liz/lizmap-web-client](https://github.com/3liz/lizmap-web-client) | 2 | issue |
| [nextcloud/maps](https://github.com/nextcloud/maps) | 2 | issue |
| [anvoz/CodeIgniter-Skeleton](https://github.com/anvoz/CodeIgniter-Skeleton) | 2 | issue |
| Altri (singoli) | 16 | 1 contributo ciascuno (vedi sotto) |

---

## django-helpdesk {#django-helpdesk}

Contributi al progetto open-source [django-helpdesk/django-helpdesk](https://github.com/django-helpdesk/django-helpdesk) — helpdesk/ticketing per Django. Ogni voce rimanda a un post dedicato con dettagli tecnici e link a GitHub.

### 2026

- [Fix: badge color per status/priority con stable id (PR #1371)]({% post_url 2026-08-06-fix-badge-color-stable-id %}) — colori ancorati a ID stabile, nuove settings `HELPDESK_TICKET_STATUS_CSS_CLASSES`.
- [Feat: tutte le colonne ordinabili nel filtro sorting (PR #1370)]({% post_url 2026-08-05-expose-sortable-columns-ticket-list %}) — estende dropdown con `id`, `last_followup`, `due_date` e altri + fix annotation.
- [Issue: Sorting dropdown per Last Followup e altre colonne (Issue #1369)]({% post_url 2026-08-05-sorting-dropdown-last-followup %}) — richiesta feature che ha portato alla PR #1370.
- [Issue: Ticket riaperti usano template email errati (Issue #1367)]({% post_url 2026-08-04-reopened-tickets-email-templates %}) — bug aperto: fallback a `updated_*` per `REOPENED_STATUS`.
- [Fix: rendering status ticket senza traduzioni (PR #1362)]({% post_url 2026-07-31-fix-ticket-status-rendering-translations %}) — risolve #1361.
- [Issue: Badge grigi con locale non-inglese (Issue #1361)]({% post_url 2026-07-30-status-badge-colors-non-english-locales %}) — badge status/priority grigi con `LANGUAGE_CODE=it`.
- [Fix: template email submitter sempre su updated (PR #1358)]({% post_url 2026-07-29-fix-submitter-email-template-status %}) — `template_prefix` basato sullo stato reale.
- [Docs: email settings per OAuth (PR #1352)]({% post_url 2026-07-24-docs-email-settings-oauth %}) — documentazione OAuth/IMAP e debug.
- [Docs: feature on-hold per escalation (PR #1340)]({% post_url 2026-05-08-document-on-hold-feature %}) — documenta la funzionalità di sospensione ticket.

### 2024

- [Issue: refactor label FOLLOW_UP in settings (Issue #1220)]({% post_url 2024-12-04-refactor-followup-label-settings %}) — allineare `FOLLOW_UP` vs `FOLLOWUP`.
- [Fix: ticket DUPLICATE spostati in closed & resolved (PR #1207)]({% post_url 2024-09-16-duplicate-status-closed-resolved %}) — risolve #1205.
- [Issue: dashboard e stato Duplicate nei ticket aperti (Issue #1205)]({% post_url 2024-09-12-dashboard-duplicate-status-open-tickets %}) — duplicate resta in "open tickets assigned to you".
- [Chore: aggiornamento upgrade.rst (PR #1203)]({% post_url 2024-09-06-update-upgrade-rst %}) — rimozione `bootstrap5form`, note upgrade 0.3 → 0.4.

> Tutti i post sono taggati `django-helpdesk` e `open-source`.

---

## Altri contributi pubblici

Per non creare centinaia di post, qui sotto trovi i contributi raggruppati per repository con conteggio e 3–5 voci recenti/più rilevanti (titolo + link + stato). Lista completa su GitHub: `https://github.com/search?q=author%3Abuoncri&type=issues`.

### [buoncri/portoneniu](https://github.com/buoncri/portoneniu) — 152

Gestionale Django per Consorzio (formazione sicurezza sul lavoro, istituzione/uffici). Attività più intensa nel 2025–2026.

- `2026-08-26` [closed] [feat(formazione): configurable compliance windows and grouped email digest](https://github.com/buoncri/portoneniu/pull/152)
- `2026-08-26` [closed] [Refactor/formazione solo sicurezza su lavoro](https://github.com/buoncri/portoneniu/pull/151)
- `2026-08-26` [closed] [refactor(formazione): narrow app to workplace-safety-only training](https://github.com/buoncri/portoneniu/pull/150)
- `2026-08-25` [closed] [fix(formazione): FO validity window in compliance + route rename](https://github.com/buoncri/portoneniu/pull/149)
- `2026-08-21` [closed] [refactor(formazione): remove per-column text search from prevenzione report](https://github.com/buoncri/portoneniu/pull/148)

### [buoncri/djangocbutemplate](https://github.com/buoncri/djangocbutemplate) — 114

Template Django per pratiche espropri, integrazione QGIS/Lizmap e DataBridge.

- `2026-07-01` [closed] [New/ebingest](https://github.com/buoncri/djangocbutemplate/pull/114)
- `2026-06-30` [closed] [fix: auto-heal stale Pratica.nome_pratica fallback names on save](https://github.com/buoncri/djangocbutemplate/pull/113)
- `2026-06-30` [closed] [refactor(soggetto): enforce CF uniqueness, add model validation, extract TipoPersona](https://github.com/buoncri/djangocbutemplate/pull/112)
- `2026-06-30` [closed] [Issue/varie](https://github.com/buoncri/djangocbutemplate/pull/111)
- `2026-06-26` [closed] [Refactor/DS4 modelli base](https://github.com/buoncri/djangocbutemplate/pull/110)

### [buoncri/iiot-irrigation-telecontrol](https://github.com/buoncri/iiot-irrigation-telecontrol) — 9

Piattaforma IIoT per telecontrollo impianti idrici (Docker Compose).

- `2026-03-18` [closed] [feat: aggiungi supporto per nuovi servizi multimediali in assistenza …](https://github.com/buoncri/iiot-irrigation-telecontrol/pull/9)
- `2026-03-18` [closed] [Debug](https://github.com/buoncri/iiot-irrigation-telecontrol/pull/8)
- `2026-03-18` [closed] [Debug](https://github.com/buoncri/iiot-irrigation-telecontrol/pull/7)
- `2026-03-16` [closed] [Speckle](https://github.com/buoncri/iiot-irrigation-telecontrol/pull/6)
- `2026-03-14` [closed] [feat: aggiorna configurazione dei segnalibri e dei widget per miglior…](https://github.com/buoncri/iiot-irrigation-telecontrol/pull/5)

### [buoncri/intranet_cbu](https://github.com/buoncri/intranet_cbu) — 5

Intranet e pubblicazione Determine.

- `2025-06-06` [closed] [Sviluppo](https://github.com/buoncri/intranet_cbu/pull/5)
- `2025-03-20` [closed] [Buoncri/issue1](https://github.com/buoncri/intranet_cbu/pull/4)
- `2025-03-17` [closed] [Prima implementazione pubblicazione Determine](https://github.com/buoncri/intranet_cbu/pull/3)
- `2025-03-11` [closed] [Spostamento repository](https://github.com/buoncri/intranet_cbu/issues/2)
- `2025-03-11` [closed] [Aggiungere pubblicazione Determine dirigenziali su bonificaumbra.it](https://github.com/buoncri/intranet_cbu/issues/1)

### [kimai/kimai](https://github.com/kimai/kimai) — 5

Time-tracking open-source — contributi traduzioni italiane e issue calendario.

- `2020-08-27` [closed] [Update italian translations (1.10)](https://github.com/kimai/kimai/pull/1929)
- `2020-08-27` [closed] [Update italian translations](https://github.com/kimai/kimai/pull/1926)
- `2020-07-29` [closed] [Improve calendar view with last activities](https://github.com/kimai/kimai/issues/1852)
- `2020-03-10` [closed] [Italian translations update](https://github.com/kimai/kimai/pull/1538)
- `2020-02-04` [closed] [Missing italian translations files added.](https://github.com/kimai/kimai/pull/1437)

### [waifung0207/ci_bootstrap_3](https://github.com/waifung0207/ci_bootstrap_3) — 9

Storico CodeIgniter — discussioni e PR 2015–2016.

- `2016-07-05` [closed] [On model db (Gcrud and Base_model)](https://github.com/waifung0207/ci_bootstrap_3/issues/75)
- `2016-05-27` [closed] [Report an interesting project to use with ci_bootstrap](https://github.com/waifung0207/ci_bootstrap_3/issues/68)
- `2015-12-04` [closed] [form_builder lib](https://github.com/waifung0207/ci_bootstrap_3/issues/32)
- `2015-11-20` [closed] [Update adminlte_helper.php](https://github.com/waifung0207/ci_bootstrap_3/pull/30)
- `2015-10-29` [closed] [Grocery_CRUD_MultiSearch](https://github.com/waifung0207/ci_bootstrap_3/issues/19)

### [scoumbourdis/grocery-crud](https://github.com/scoumbourdis/grocery-crud) — 4

- `2016-12-05` [closed] [Updating image_moo](https://github.com/scoumbourdis/grocery-crud/issues/384)
- `2015-10-30` [closed] [1](https://github.com/scoumbourdis/grocery-crud/pull/333)
- `2015-09-14` [closed] [Update italian.php](https://github.com/scoumbourdis/grocery-crud/pull/328)
- `2015-03-13` [closed] [Update italian.php](https://github.com/scoumbourdis/grocery-crud/pull/307)

### [buoncri/grocery-crud](https://github.com/buoncri/grocery-crud) — 2

- `2020-04-30` [closed] [sync to core/master](https://github.com/buoncri/grocery-crud/pull/2)
- `2015-09-14` [closed] [Update italian.php](https://github.com/buoncri/grocery-crud/pull/1)

### [3liz/lizmap-web-client](https://github.com/3liz/lizmap-web-client) — 2

- `2019-10-29` [closed] [wrong print scale](https://github.com/3liz/lizmap-web-client/issues/1368)
- `2019-06-21` [closed] [Filter data with form errors](https://github.com/3liz/lizmap-web-client/issues/1270)

### [nextcloud/maps](https://github.com/nextcloud/maps) — 2

- `2019-09-03` [closed] [Personlized basemap](https://github.com/nextcloud/maps/issues/115)
- `2019-07-23` [closed] [How to regenerate oc_maps table](https://github.com/nextcloud/maps/issues/67)

### [anvoz/CodeIgniter-Skeleton](https://github.com/anvoz/CodeIgniter-Skeleton) — 2

- `2013-11-22` [closed] [integrating grocerycrud](https://github.com/anvoz/CodeIgniter-Skeleton/issues/3)
- `2013-11-14` [closed] [What do you think of adding another piece of software](https://github.com/anvoz/CodeIgniter-Skeleton/issues/2)

---

### Altri — 1 contributo ciascuno

Contributi singoli su repo diversi (link diretto):

- [buoncri/django-helpdesk](https://github.com/buoncri/django-helpdesk) — fork personale (1)
- [DjangoCRM/django-crm](https://github.com/DjangoCRM/django-crm) (1)
- [marcanuy/django-dynamic-breadcrumbs](https://github.com/marcanuy/django-dynamic-breadcrumbs) (1)
- [buoncri/kimai2](https://github.com/buoncri/kimai2) (1)
- [nnseva/django-leaflet-admin-list](https://github.com/nnseva/django-leaflet-admin-list) (1)
- [traccar/traccar](https://github.com/traccar/traccar) (1)
- [fastapi-admin/restful-admin](https://github.com/fastapi-admin/restful-admin) (1)
- [kevinpapst/AdminLTEBundle](https://github.com/kevinpapst/AdminLTEBundle) (1)
- [buoncri/traccar-api-php](https://github.com/buoncri/traccar-api-php) (1)
- [buoncri/snipe-it](https://github.com/buoncri/snipe-it) (1)
- [buoncri/Ignited-Datatables](https://github.com/buoncri/Ignited-Datatables) (1)
- [3liz/lizmap-documentation](https://github.com/3liz/lizmap-documentation) (1)
- [KIOS-Research/ImportPhotos](https://github.com/KIOS-Research/ImportPhotos) (1)
- [goFrendiAsgard/No-CMS](https://github.com/goFrendiAsgard/No-CMS) (1)
- [TuniLame/charisma-template-codeigniter](https://github.com/TuniLame/charisma-template-codeigniter) (1)
- [vesparny/codeigniter-html5boilerplate-twitter-bootstrap](https://github.com/vesparny/codeigniter-html5boilerplate-twitter-bootstrap) (1)

> Per l'elenco completo e aggiornato: [github.com/buoncri?tab=repositories](https://github.com/buoncri?tab=repositories) e ricerca GitHub [`author:buoncri`](https://github.com/search?q=author%3Abuoncri&type=issues).
