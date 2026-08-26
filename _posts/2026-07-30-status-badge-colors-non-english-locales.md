---
layout: post
title: "Status badge colors rotti su locale non-inglese nella ticket list (Issue #1361)"
date: 2026-07-30 09:31:48 +0200
categories: [django-helpdesk, open-source]
tags: [django, helpdesk, contribuzione]
author: buoncri
---

Contributo a [django-helpdesk/django-helpdesk](https://github.com/django-helpdesk/django-helpdesk) — **Issue #1361**.

- **Link GitHub:** [Issue #1361 — Status badge colors break on non-English locales in ticket list](https://github.com/django-helpdesk/django-helpdesk/issues/1361)
- **Stato:** Closed (bug, risolta da PR #1362 e successivamente da #1371)
- **Riferimenti:** Fix in PR #1362, refactor in PR #1371

## Sommario

Ho segnalato che i colori dei badge di status erano mappati su stringhe inglesi lato client (JS), quindi con qualsiasi locale diverso da `en` tutti i badge risultavano grigi.

## Dettagli tecnici

- **Riproduzione:** impostare `LANGUAGE_CODE = "it"` in settings, aprire la ticket list: tutti i badge status/priority appaiono grigi.
- Causa: mappa `contextMaps` hardcoded in JavaScript con chiavi in inglese; nessuna normalizzazione su id stabile né su traduzione.
- Contesto: Debian Sid, Firefox 140.13.

La issue include screenshot del problema e ha portato prima al fix puntuale #1362 e poi al refactor strutturale #1371 che àncora i colori a `HELPDESK_TICKET_STATUS_CSS_CLASSES` con chiave id stabile.

## Impatto

Segnalazione che ha evidenziato un difetto di internazionalizzazione critico per deployment non-inglesi, guidando due fix successivi.
