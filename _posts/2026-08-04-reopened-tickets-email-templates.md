---
layout: post
title: "Reopened tickets usano template email updated e saltano la notifica al submitter (Issue #1367)"
date: 2026-08-04 13:44:01 +0200
categories: [django-helpdesk, open-source]
tags: [django, helpdesk, contribuzione]
author: buoncri
---

Contributo a [django-helpdesk/django-helpdesk](https://github.com/django-helpdesk/django-helpdesk) — **Issue #1367**.

- **Link GitHub:** [Issue #1367 — Reopened tickets use "updated" email templates and skip submitter notification](https://github.com/django-helpdesk/django-helpdesk/issues/1367)
- **Stato:** Open (bug)

## Sommario

I ticket riaperti usano i template generici `updated_*` — l'oggetto riporta "(Updated)" invece di "(Reopened)" — e con le impostazioni di default la riapertura senza commento non invia alcuna email al submitter.

## Dettagli tecnici

Causa radice:

- `get_email_template_prefix()` in `update_ticket.py` gestisce solo `RESOLVED` e `CLOSED`, facendo fallback a `"updated_"` per `REOPENED_STATUS`.
- Il fixture `emailtemplate.json` non contiene record `reopened_*` in alcuna locale.
- Il guard per la notifica al submitter controlla solo `(RESOLVED_STATUS, CLOSED_STATUS)`, quindi `REOPENED` viene silenziosamente ignorato.

Riproduzione:

1. Creare un ticket e chiuderlo.
2. Riaprirlo dalla vista staff (follow-up pubblico, senza commento).
3. Verificare la inbox del submitter: nessuna email, o oggetto "(Updated)" se `HELPDESK_NOTIFY_SUBMITTER_FOR_ALL_TICKET_CHANGES=True`.

Direzione proposta nella issue:

- Restituire `"reopened_"` da `get_email_template_prefix` per `REOPENED_STATUS`.
- Aggiungere fixture `reopened_*` (`reopened_cc`, `reopened_owner`, `reopened_submitter`) + migrazione.
- Includere `REOPENED_STATUS` tra gli stati che notificano il submitter anche senza commento.
- A lungo termine: mapping configurabile `status_id → template prefix` per supportare status custom (es. `HELPDESK_TICKET_FORKED_STATUS`).

## Impatto

Segnalazione ancora aperta che documenta un'inconsistenza nel flusso email di riapertura; la soluzione proposta allinea template, notifiche e fixture, migliorando la comunicazione verso l'utente finale.
