---
layout: post
title: "Fix: ticket DUPLICATE spostati in Closed & Resolved (PR #1207)"
date: 2024-09-16 10:29:39 +0200
categories: [django-helpdesk, open-source]
tags: [django, helpdesk, contribuzione]
author: buoncri
---

Contributo a [django-helpdesk/django-helpdesk](https://github.com/django-helpdesk/django-helpdesk) — **Pull Request #1207**.

- **Link GitHub:** [PR #1207 — DUPLICATE_STATUS Tickets moved to closed & resolved ones](https://github.com/django-helpdesk/django-helpdesk/pull/1207)
- **Stato:** Merged il 2024-09-16 (fix per Issue #1205)
- **Riferimenti:** Fix #1205

## Sommario

I ticket con stato `DUPLICATE` restavano nella sezione "Open Tickets assigned to you" in dashboard anche dopo la risoluzione del ticket principale, mentre quest'ultimo veniva correttamente spostato in "Closed & resolved Tickets".

## Dettagli tecnici

La PR correla l'handle del `DUPLICATE_STATUS` al flusso di chiusura/risoluzione, spostando i duplicati nel riquadro dei ticket chiusi/risolti anziché lasciarli tra gli aperti. Body originale minimale: *"Issue #1205"*.

File coinvolti: vista dashboard e query di filtraggio per status `duplicate` / `closed`.

## Impatto

La dashboard mostra ora solo ticket realmente aperti in "Open Tickets assigned to you", migliorando la priorità percepita e riducendo il rumore per l'assegnatario.
