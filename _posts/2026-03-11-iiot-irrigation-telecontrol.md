---
layout: post
title: "Pubblicazione del repository IIoT Irrigation Telecontrol"
date: 2026-03-11 10:00:00 +0100
categories: iiot open-source docker irrigation bim
---

Oggi ho pubblicato sul mio profilo GitHub il progetto [**iiot-irrigation-telecontrol**](https://github.com/buoncri/iiot-irrigation-telecontrol). Si tratta di un repository di orchestrazione per una piattaforma IIoT pensata per il telecontrollo di impianti idrici e di irrigazione industriale, interamente basata su **Docker Compose**.

### Di cosa si tratta?
Il progetto nasce per centralizzare e gestire con ordine un'intera infrastruttura locale. Al suo interno sono definiti:
- **Stack applicativi**: configurazioni Docker di vari servizi tra cui *Homepage, Excalidash, Portainer, Dockge, PostgreSQL, Speckle, LibreNMS* e altri.
- **Utility di gestione**: strumenti per la gestione dell'infrastruttura (attraverso l'uso di Dockge e di script di automazione come stackctl.sh).
- **Dati persistenti**: un'organizzazione rigida per separare i dati runtime dai file versionati.

### Sicurezza e dati sensibili
In fase di preparazione al rilascio pubblico ho fatto una bella analisi del codice e... mi sono accorto che, per sbaglio, avevo lasciato all’interno del repository alcune informazioni sensibili! (era rimasta la chiave api di portainer :-D, niente di grave, ora l'ho tolta e non viene più salvata :-D)

In un tipico ecosistema Docker Compose ci si destreggia continuamente tra file .env, chiavi, token e volumi di database. Inizialmente, nella foga di sistemare tutto, qualche password e dato runtime era finito nei commit. Ho quindi provveduto a rivedere la struttura, separare nettamente le configurazioni sensibili e inserire le regole adeguate nel .gitignore in modo da garantire un rilascio pulito e sicuro. 

Lezione imparata: mai dare per scontato il contenuto di una directory `appdata/` o dei template `.env` prima di fare un bel `git push`.

Trovate il repository e le istruzioni dettagliate su come fare il bootstrap dell'infrastruttura su [GitHub](https://github.com/buoncri/iiot-irrigation-telecontrol).
