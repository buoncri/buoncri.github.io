---
layout: post
title: "Docs: impostazioni email per OAuth e debug IMAP (PR #1352)"
date: 2026-07-24 12:39:52 +0200
categories: [django-helpdesk, open-source]
tags: [django, helpdesk, contribuzione]
author: buoncri
---

Contributo a [django-helpdesk/django-helpdesk](https://github.com/django-helpdesk/django-helpdesk) — **Pull Request #1352**.

- **Link GitHub:** [PR #1352 — Docs, added email settings for oauth](https://github.com/django-helpdesk/django-helpdesk/pull/1352)
- **Stato:** Merged il 2026-07-25

## Sommario

Aggiunta documentazione per le impostazioni email legate a OAuth e al debug IMAP, per facilitare la configurazione in ambienti con autenticazione moderna.

## Dettagli tecnici

- Documentate le nuove/aggiornate settings per OAuth (es. provider, token flow) e per il debug IMAP.
- Body originale sintetico: *"Added settings for oauth and imap debug."*
- Modifiche in `docs/` e riferimenti in `settings.py`.

## Impatto

Migliora l'onboarding per chi configura l'acquisizione email via OAuth2, riducendo tentativi ed errori su IMAP con provider moderni (es. Microsoft 365 / Gmail).
