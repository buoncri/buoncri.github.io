---
layout: post
title: "Fix: template email submitter sempre su updated invece dello status reale (PR #1358)"
date: 2026-07-29 12:56:37 +0200
categories: [django-helpdesk, open-source]
tags: [django, helpdesk, contribuzione]
author: buoncri
---

Contributo a [django-helpdesk/django-helpdesk](https://github.com/django-helpdesk/django-helpdesk) — **Pull Request #1358**.

- **Link GitHub:** [PR #1358 — Fix submitter email template always using "updated" regardless of ticket status](https://github.com/django-helpdesk/django-helpdesk/pull/1358)
- **Stato:** Merged il 2026-07-29

## Sommario

Quando un ticket veniva risolto o chiuso, l'email al submitter mostrava un oggetto errato perché il nome del template era hardcoded a `updated_submitter`, indipendentemente dallo stato reale.

## Dettagli tecnici

Allineato il comportamento del submitter a quello già applicato per owner/cc: il nome del template ora usa la stessa logica `template_prefix` basata sullo stato (es. `resolved_`, `closed_`).

> Body originale: *"When a ticket is resolved or closed, the submitter email subject showed the wrong status because the template name was hardcoded to \"updated_submitter\". Use the same template_prefix logic already applied to owner/cc notifications."*

File coinvolto: `update_ticket.py` — dove `get_email_template_prefix()` determina il prefisso in base allo status.

## Impatto

Oggetto e corpo email al submitter ora riflettono correttamente lo stato (Resolved/Closed), migliorando chiarezza e coerenza della comunicazione.
