---
layout: post
title: "Sorting dropdown su /tickets/ per Last Followup e altre colonne ordinabili (Issue #1369)"
date: 2026-08-05 09:23:37 +0200
categories: [django-helpdesk, open-source]
tags: [django, helpdesk, contribuzione]
author: buoncri
---

Contributo a [django-helpdesk/django-helpdesk](https://github.com/django-helpdesk/django-helpdesk) — **Issue #1369**.

- **Link GitHub:** [Issue #1369 — Sorting dropdown on /tickets/ by "Last Followup" (and other sortable columns)](https://github.com/django-helpdesk/django-helpdesk/issues/1369)
- **Stato:** Closed (enhancement, risolta da PR #1370)
- **Riferimenti:** Implementata in PR #1370

## Sommario

Ho aperto questa feature request per segnalare il disallineamento tra il dropdown Sorting (sei campi: Created, Title, Queue, Status, Priority, Owner) e i campi già accettati da `ALLOWED_SORTS` e `DATATABLES_ORDER_COLUMN_CHOICES` (`id`, `due_date`, `submitter_email`, `last_followup`, `kbitem`). In particolare `last_followup` non era utilizzabile perché l'ordinamento avveniva prima dell'annotation in `Query.__run__()`.

## Dettagli tecnici

La issue propone:

1. Aggiungere `last_followup`, `id`, `due_date`, `submitter_email`, `kbitem` al dropdown (`kbitem` condizionato a `HELPDESK_KB_ENABLED`).
2. Aggiungere `id`, `due_date`, `submitter_email` a `ALLOWED_SORTS`.
3. Rendere `last_followup` ordinabile estraendo la `Subquery` in helper e applicando l'annotation **prima** di `order_by()` (incluso `-last_followup`), riusando l'helper in `get_datatables_context()`.

Contesto d'uso citato: manteniamo una vista custom che elenca i ticket per ultimo follow-up per monitorare l'attività live; l'ordinamento nativo in `/tickets/` permetterebbe di sostituirla con una saved query.

## Impatto

La proposta è stata accolta e implementata integralmente nella PR #1370, chiudendo il gap UI/backend senza impattare il flusso saved query.
