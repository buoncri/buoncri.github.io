---
layout: post
title: "Refactor label FOLLOW_UP vs FOLLOWUP in settings (Issue #1220)"
date: 2024-12-04 11:35:04 +0200
categories: [django-helpdesk, open-source]
tags: [django, helpdesk, contribuzione]
author: buoncri
---

Contributo a [django-helpdesk/django-helpdesk](https://github.com/django-helpdesk/django-helpdesk) — **Issue #1220**.

- **Link GitHub:** [Issue #1220 — Trivial refactor in settings.py about followup label](https://github.com/django-helpdesk/django-helpdesk/issues/1220)
- **Stato:** Closed (enhancement)

## Sommario

Ho segnalato un'inconsistenza di naming in `settings.py`: i follow-up compaiono con due label diverse, `FOLLOW_UP` e `FOLLOWUP`.

## Dettagli tecnici

- Richiesta: rinominare una delle due label per avere coerenza nelle settings relative ai follow-up.
- Alternativa valutata: lasciare tutto com'è (impatto minimo, solo pulizia).
- File impattato: `src/helpdesk/settings.py` e relativi import.

## Impatto

Proposta di pulizia e coerenza del codebase, utile per nuovi contributor e per ridurre ambiguità nella configurazione.
