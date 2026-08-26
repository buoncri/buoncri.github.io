---
layout: home
---

<div style="text-align: center; margin: 2rem 0 2.5rem 0;">
  <img src="https://avatars.githubusercontent.com/u/3062441?v=4" alt="Luca Buoncristiani" width="150" height="150" style="border-radius: 50%; max-width: 150px; height: auto; border: 3px solid #e8e8e8; box-shadow: 0 2px 8px rgba(0,0,0,0.1);" loading="lazy" onerror="this.onerror=null;this.src='/images/profile.jpg';" />
  <h2 style="margin: 1rem 0 0.3rem 0;">Luca Buoncristiani</h2>
  <p style="margin: 0; color: #666; font-size: 1.05em;">
    Sviluppatore Open Source &bull; Consorzio di Bonifica<br />
    Appassionato di Django, Python e soluzioni per la PA
  </p>
  <p style="margin: 0.8rem 0 0 0;">
    <a href="https://github.com/buoncri" target="_blank" rel="noopener">GitHub @buoncri</a>
    &bull;
    <a href="mailto:luca.buoncristiani@bonificaumbra.it">Contatti</a>
    &bull;
    <a href="#contributi">Contributi django-helpdesk</a>
  </p>
</div>

Benvenuta, forma di vita basata sul carbonio ...

Questo spazio è un semplice raccoglitore di appunti, esperimenti e soluzioni Open Source su cui mi trovo a lavorare. Nessuna pretesa, ma spero che qualche spunto possa tornare utile.

Lunga vita e prosperità 🖖

Benvenuto nel mio spazio personale: qui condivido idee ed esperienze su soluzioni software Open Source per Consorzi di Bonifica e contributi alla community Django. Dai un'occhiata ai [miei contributi a django-helpdesk](#contributi-a-django-helpdesk) qui sotto — 13 tra PR e issue per rendere il ticketing più solido e accessibile.

---

## Contributi a django-helpdesk {#contributi-a-django-helpdesk}

Raccolta dei miei contributi al progetto open-source [django-helpdesk/django-helpdesk](https://github.com/django-helpdesk/django-helpdesk) — helpdesk/ticketing system per Django. Ogni voce rimanda a un post dedicato con dettagli tecnici e link a GitHub.

### 2026

- [Fix: badge color per status/priority con stable id (PR #1371)]({% post_url 2026-08-06-fix-badge-color-stable-id %}) — colori ancorati a ID stabile, nuove settings `HELPDESK_TICKET_STATUS_CSS_CLASSES`.
- [Feat: tutte le colonne ordinabili nel filtro sorting (PR #1370)]({% post_url 2026-08-05-expose-sortable-columns-ticket-list %}) — estende dropdown con `id`, `last_followup`, `due_date` e altri + fix annotation.
- [Issue: Sorting dropdown per Last Followup e altre colonne (Issue #1369)]({% post_url 2026-08-05-sorting-dropdown-last-followup %}) — richiesta feature che ha portato alla PR #1370.
- [Issue: Ticket riaperti usano template email errati (Issue #1367)]({% post_url 2026-08-04-reopened-tickets-email-templates %}) — bug aperto: fallback a `updated_*` per `REOPENED_STATUS`.
- [Fix: rendering status ticket senza traduzioni (PR #1362)]({% post_url 2026-07-31-fix-ticket-status-rendering-translations %}) — risolve #1361.
- [Issue: Badge grigi con locale non-inglese (Issue #1361)]({% post_url 2026-07-30-status-badge-colors-non-english-locales %}) — badge status/priority grigi con `LANGUAGE_CODE=it`.
- [Fix: template email submitter sempre su updated (PR #1358)]({% post_url 2026-07-29-fix-submitter-email-template-status %}) — `template_prefix` basato sullo stato reale.
- [Docs: email settings per OAuth (PR #1352)]({% post_url 2026-07-24-docs-email-settings-oauth %}) — documentazione OAuth/IMAP e debug.
- [Docs: feature on-hold per escalation (PR #1340)]({% post_url 2026-05-08-document-on-hold-feature %}) — documenta la funzionalità di sospensione ticket.

### 2024

- [Issue: refactor label FOLLOW_UP in settings (Issue #1220)]({% post_url 2024-12-04-refactor-followup-label-settings %}) — allineare `FOLLOW_UP` vs `FOLLOWUP`.
- [Fix: ticket DUPLICATE spostati in closed & resolved (PR #1207)]({% post_url 2024-09-16-duplicate-status-closed-resolved %}) — risolve #1205.
- [Issue: dashboard e stato Duplicate nei ticket aperti (Issue #1205)]({% post_url 2024-09-12-dashboard-duplicate-status-open-tickets %}) — duplicate resta in "open tickets assigned to you".
- [Chore: aggiornamento upgrade.rst (PR #1203)]({% post_url 2024-09-06-update-upgrade-rst %}) — rimozione `bootstrap5form`, note upgrade 0.3 → 0.4.

> Tutti i post sono taggati `django-helpdesk` e `open-source` — li trovi anche nella lista automatica qui sotto generata dal tema Minima.
