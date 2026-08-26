---
layout: post
title: "Dashboard: ticket Duplicate restano tra gli Open Tickets assegnati (Issue #1205)"
date: 2024-09-12 12:08:16 +0200
categories: [django-helpdesk, open-source]
tags: [django, helpdesk, contribuzione]
author: buoncri
---

Contributo a [django-helpdesk/django-helpdesk](https://github.com/django-helpdesk/django-helpdesk) — **Issue #1205**.

- **Link GitHub:** [Issue #1205 — Dashboard, open tickets assigned to you and Duplicate status](https://github.com/django-helpdesk/django-helpdesk/issues/1205)
- **Stato:** Closed (bug, risolta da PR #1207)
- **Riferimenti:** Fix in PR #1207

## Sommario

Segnalazione: nella pagina Dashboard, nel riquadro "Open Tickets assigned to you", i ticket con stato `Duplicate` rimangono visibili anche dopo che il ticket principale è stato risolto e spostato correttamente in "Closed & resolved Tickets you used to work on".

## Dettagli tecnici

Passi per riprodurre:

1. Creare ticket uno
2. Creare ticket due
3. Unire (merge) i ticket e risolvere
4. Verificare l'errore in dashboard

Comportamento atteso: i ticket marcati come duplicate dovrebbero seguire il principale nello stesso riquadro dei risolti, o in un riquadro dedicato ai duplicati, così che "Open Tickets assigned to you" contenga solo ticket realmente aperti.

## Impatto

La issue ha motivato la PR #1207 che ha corretto il filtraggio per `DUPLICATE_STATUS` in dashboard.
