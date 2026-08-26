---
layout: post
title: "Documentata la feature on-hold per prevenire escalation automatiche (PR #1340)"
date: 2026-05-08 08:09:06 +0200
categories: [django-helpdesk, open-source]
tags: [django, helpdesk, contribuzione]
author: buoncri
---

Contributo a [django-helpdesk/django-helpdesk](https://github.com/django-helpdesk/django-helpdesk) — **Pull Request #1340**.

- **Link GitHub:** [PR #1340 — Document 'on hold' feature for ticket escalations](https://github.com/django-helpdesk/django-helpdesk/pull/1340)
- **Stato:** Merged il 2026-05-08

## Sommario

Documentata la funzionalità "on hold" che permette di sospendere un ticket per prevenire escalation automatiche.

## Dettagli tecnici

- Aggiunte istruzioni in `docs/` su come mettere un ticket in stato di sospensione e sull'effetto sulle regole di escalation.
- Body originale: *"Added instructions for putting tickets on hold to prevent automatic escalations."*

## Impatto

Rende scopribile una feature esistente ma poco documentata, utile per gestire ticket in attesa di input esterno senza generare escalation spurie.
