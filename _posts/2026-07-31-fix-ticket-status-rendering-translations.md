---
layout: post
title: "Fix: rendering dello status ticket senza traduzioni (PR #1362)"
date: 2026-07-31 09:32:59 +0200
categories: [django-helpdesk, open-source]
tags: [django, helpdesk, contribuzione]
author: buoncri
---

Contributo a [django-helpdesk/django-helpdesk](https://github.com/django-helpdesk/django-helpdesk) — **Pull Request #1362**.

- **Link GitHub:** [PR #1362 — Fix ticket status rendering without translations](https://github.com/django-helpdesk/django-helpdesk/pull/1362)
- **Stato:** Merged il 2026-07-31
- **Riferimenti:** Resolve #1361

## Sommario

Correzione del rendering dello status ticket quando le traduzioni non sono disponibili o il locale non è inglese. La PR risolve il bug che lasciava i badge in grigio su `LANGUAGE_CODE=it` e altre lingue.

## Dettagli tecnici

Aggiornato il rendering dello status per usare la traduzione delle label di status in modo robusto, evitando che la mappatura colori dipenda da stringhe in inglese hardcoded. Questo è il fix intermedio che ha sbloccato il caso #1361 prima del refactor più strutturale della PR #1371 (mapping su stable id).

Body originale sintetico: *"Updated ticket status rendering to use translation for status labels. Resolve issue #1361."*

## Impatto

Ripristina il colore corretto dei badge di status anche senza traduzioni complete, garantendo coerenza visiva per installazioni localizzate.
