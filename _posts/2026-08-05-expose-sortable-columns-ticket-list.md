---
layout: post
title: "Feat: tutte le colonne ordinabili nel filtro sorting della ticket list (PR #1370)"
date: 2026-08-05 10:17:14 +0200
categories: [django-helpdesk, open-source]
tags: [django, helpdesk, contribuzione]
author: buoncri
---

Contributo a [django-helpdesk/django-helpdesk](https://github.com/django-helpdesk/django-helpdesk) — **Pull Request #1370**.

- **Link GitHub:** [PR #1370 — feat: expose all sortable columns in ticket list sorting filter](https://github.com/django-helpdesk/django-helpdesk/pull/1370)
- **Stato:** Merged il 2026-08-05
- **Riferimenti:** Fix #1369

## Sommario

Il dropdown "Sorting" in `/tickets/` offriva solo sei campi, mentre `ALLOWED_SORTS` e `DATATABLES_ORDER_COLUMN_CHOICES` supportavano già `id`, `due_date`, `submitter_email`, `last_followup`, `kbitem`. `last_followup` essendo una annotation sollevava `FieldError` se usato come ordinamento.

La PR allinea UI e backend e rende ordinabile anche `last_followup`.

## Dettagli tecnici

- Aggiunti al dropdown `src/helpdesk/templates/helpdesk/filters/sorting.html`: `id`, `last_followup`, `due_date`, `submitter_email`, `kbitem` (quest'ultimo condizionato a `HELPDESK_KB_ENABLED`).
- `last_followup` è una `Subquery` sui `FollowUp`: estratta in helper riutilizzabile e annotata sul `queryset` **prima** di `order_by()` in `Query.__run__()` (in `src/helpdesk/query.py`), gestendo anche `-last_followup`.
- Stesso helper riutilizzato in `get_datatables_context()` per endpoint datatables e timeline.
- Aggiornati `ALLOWED_SORTS` in `src/helpdesk/views/staff.py` per i campi reali già validati da `_validate_sorting()`. Il flusso saved-query persiste già `sorting`, nessuna modifica necessaria.

## Impatto

Permette di sostituire viste custom (es. ordinamento per attività recente su `last_followup`) con una saved query standard su `/tickets/`, con coerenza tra UI, validazione e query layer.
