---
layout: page
title: Contributi
permalink: /contrib/
---

Raccolta dei miei contributi pubblici su GitHub — PR, issue e discussioni a cui ho partecipato come autore. Repo principale: [github.com/buoncri](https://github.com/buoncri). Per il codice più recente vedi anche [tutti i repository](https://github.com/buoncri?tab=repositories).

> **Nota:** elenco raggruppato per repository, generato il **2026-08-31** via GitHub Search API (`search/issues?q=author:buoncri is:public`, 65 risultati totali — solo repository pubblici). I conteggi includono PR e issue. Sotto trovi dettaglio per i repo con più attività; i singoli contributi minori sono in coda in "Altri".

## Panoramica

| Repository | Contributi | Tipo |
|---|---|---|
| [django-helpdesk/django-helpdesk](https://github.com/django-helpdesk/django-helpdesk) | 13 | PR/issue esterni (dettaglio sotto) |
| [buoncri/iiot-irrigation-telecontrol](https://github.com/buoncri/iiot-irrigation-telecontrol) | 10 | PR — piattaforma IIoT telecontrollo |
| [waifung0207/ci_bootstrap_3](https://github.com/waifung0207/ci_bootstrap_3) | 9 | issue/PR (CodeIgniter, storico) |
| [kimai/kimai](https://github.com/kimai/kimai) | 5 | PR/issue — traduzioni it, calendario |
| [scoumbourdis/grocery-crud](https://github.com/scoumbourdis/grocery-crud) | 4 | PR/issue — traduzioni, fix |
| [buoncri/grocery-crud](https://github.com/buoncri/grocery-crud) | 2 | PR |
| [3liz/lizmap-web-client](https://github.com/3liz/lizmap-web-client) | 2 | issue |
| [nextcloud/maps](https://github.com/nextcloud/maps) | 2 | issue |
| [anvoz/CodeIgniter-Skeleton](https://github.com/anvoz/CodeIgniter-Skeleton) | 2 | issue |
| Altri (singoli) | 16 | 1 contributo ciascuno (vedi sotto) |

---

## django-helpdesk {#django-helpdesk}

Contributi al progetto open-source [django-helpdesk/django-helpdesk](https://github.com/django-helpdesk/django-helpdesk) — helpdesk/ticketing per Django. I miei contributi sono consultabili direttamente su GitHub — dettaglio storico rimosso, vedi link sotto (nessun post locale).

- [PR #1371 — fix: key status/priority badge color by stable id](https://github.com/django-helpdesk/django-helpdesk/pull/1371) — colori ancorati a ID stabile, nuove settings `HELPDESK_TICKET_STATUS_CSS_CLASSES`.
- [PR #1370 — feat: expose all sortable columns in ticket list sorting filter](https://github.com/django-helpdesk/django-helpdesk/pull/1370) — estende dropdown con `id`, `last_followup`, `due_date` e altri.
- [Issue #1369 — Sorting dropdown on /tickets/ by Last Followup](https://github.com/django-helpdesk/django-helpdesk/issues/1369) — richiesta feature che ha portato alla PR #1370.
- [Issue #1367 — Reopened tickets use updated email templates](https://github.com/django-helpdesk/django-helpdesk/issues/1367) — bug: fallback a `updated_*` per `REOPENED_STATUS`.
- [PR #1362 — Fix ticket status rendering without translations](https://github.com/django-helpdesk/django-helpdesk/pull/1362) — risolve #1361.
- [Issue #1361 — Status badge colors break on non-English locales](https://github.com/django-helpdesk/django-helpdesk/issues/1361) — badge grigi con `LANGUAGE_CODE=it`.
- [PR #1358 — Fix submitter email template always using updated](https://github.com/django-helpdesk/django-helpdesk/pull/1358) — `template_prefix` basato sullo stato reale.
- [PR #1352 — Docs, added email settings for oauth](https://github.com/django-helpdesk/django-helpdesk/pull/1352) — documentazione OAuth/IMAP e debug.
- [PR #1340 — Document on hold feature for ticket escalations](https://github.com/django-helpdesk/django-helpdesk/pull/1340) — documenta la funzionalità di sospensione ticket.
- [Issue #1220 — Trivial refactor in settings.py about followup label](https://github.com/django-helpdesk/django-helpdesk/issues/1220) — allineare `FOLLOW_UP` vs `FOLLOWUP`.
- [PR #1207 — DUPLICATE_STATUS Tickets moved to closed & resolved ones](https://github.com/django-helpdesk/django-helpdesk/pull/1207) — risolve #1205.
- [Issue #1205 — Dashboard, open tickets assigned to you and Duplicate status](https://github.com/django-helpdesk/django-helpdesk/issues/1205) — duplicate resta in open tickets.
- [PR #1203 — Update upgrade.rst](https://github.com/django-helpdesk/django-helpdesk/pull/1203) — rimozione `bootstrap5form`, note upgrade 0.3 → 0.4.

---

## Altri contributi pubblici

Per non creare centinaia di post, qui sotto trovi i contributi raggruppati per repository con conteggio e 3–5 voci recenti/più rilevanti (titolo + link + stato). Lista completa su GitHub: `https://github.com/search?q=author%3Abuoncri&type=issues`.

### [buoncri/iiot-irrigation-telecontrol](https://github.com/buoncri/iiot-irrigation-telecontrol) — 10

Piattaforma IIoT per telecontrollo impianti idrici (Docker Compose).

- `2026-08-28` [closed] [chore: sostituisci dockge con dockhand come stack manager](https://github.com/buoncri/iiot-irrigation-telecontrol/pull/10)
- `2026-03-18` [closed] [feat: aggiungi supporto per nuovi servizi multimediali in assistenza …](https://github.com/buoncri/iiot-irrigation-telecontrol/pull/9)
- `2026-03-18` [closed] [Debug](https://github.com/buoncri/iiot-irrigation-telecontrol/pull/8)
- `2026-03-18` [closed] [Debug](https://github.com/buoncri/iiot-irrigation-telecontrol/pull/7)
- `2026-03-16` [closed] [Speckle](https://github.com/buoncri/iiot-irrigation-telecontrol/pull/6)

### [waifung0207/ci_bootstrap_3](https://github.com/waifung0207/ci_bootstrap_3) — 9

Storico CodeIgniter — discussioni e PR 2015–2016.

- `2016-07-05` [closed] [On model db (Gcrud and Base_model)](https://github.com/waifung0207/ci_bootstrap_3/issues/75)
- `2016-05-27` [closed] [Report an interesting project to use with ci_bootstrap](https://github.com/waifung0207/ci_bootstrap_3/issues/68)
- `2015-12-04` [closed] [form_builder lib](https://github.com/waifung0207/ci_bootstrap_3/issues/32)
- `2015-11-20` [closed] [Update adminlte_helper.php](https://github.com/waifung0207/ci_bootstrap_3/pull/30)
- `2015-10-29` [closed] [Grocery_CRUD_MultiSearch](https://github.com/waifung0207/ci_bootstrap_3/issues/19)

### [kimai/kimai](https://github.com/kimai/kimai) — 5

Time-tracking open-source — contributi traduzioni italiane e issue calendario.

- `2020-08-27` [closed] [Update italian translations (1.10)](https://github.com/kimai/kimai/pull/1929)
- `2020-08-27` [closed] [Update italian translations](https://github.com/kimai/kimai/pull/1926)
- `2020-07-29` [closed] [Improve calendar view with last activities](https://github.com/kimai/kimai/issues/1852)
- `2020-03-10` [closed] [Italian translations update](https://github.com/kimai/kimai/pull/1538)
- `2020-02-04` [closed] [Missing italian translations files added.](https://github.com/kimai/kimai/pull/1437)

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
