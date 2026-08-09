# PREREG — cancellation_recon (round 27)

Coordinator brief, written before dispatch. The pilot appends its own
registrations BELOW the brief BEFORE any computation.

## Mandate

Underneath the band-closure analytic half sits the campaign's oldest
wall: converting "counts are Poisson-ordinary everywhere probed" into
a PROVED lower bound is an anti-concentration statement — the
cancellation barrier both branches have historically hit. This round
has one specific new reason for hope: **THEOREM Z-FLOOR (banked
round 18, on the F2 lane) is a PROVED pointwise first-moment floor,
tight within 2x, that survived round 26's falsification event
untouched (0 violations over 292 cells while the ceiling above it
died).** Your job: a disciplined reconnaissance — can Z-FLOOR's proof
mechanism transport to band counts, and if not exactly, what is the
weakest usable BAND-AC lower bound and what would prove it?

## Deliverables

**D1 — THE NEED, STATED EXACTLY.** Read the three consumers'
contracts (adjacency_closing, list_adjacency_closing, mca_safe) and
extract what each actually needs from the band determination: which
direction (the anti-concentration direction = counts do NOT fall
below the model, i.e. the deficit side stays deficit), at what
tolerance, at which sigma. Name each bar per consumer (CATCH-24C).
The output is the exact target statement BAND-AC-LB that a proof
would have to deliver. Include the K5 witness-kernel framing
(WP5_RATEHALF_VERDICT.md) — the priced witness family covering
(R(lq), sigma*] is the constructive reading of the same need.

**D2 — THE Z-FLOOR TRANSPORT TEST.** Read THEOREM Z-FLOOR's proof
(f2_z1_mass_knife_edge lineage; the round-18 z1_ternary_mass
pilot's banked material) and extract its mechanism skeleton: what
makes the first-moment floor PROVABLE there (the structure that
yields pointwise tightness within 2x). Then map the band count into
the same shape: what plays the role of the mass, the normalizer,
the orbit structure? Registered verdict options: (a) TRANSPORTS
(state the transported theorem + verify at accessible band cells);
(b) transports PARTIALLY (a weaker floor — state it exactly and
what it buys against D1's bars); (c) STRUCTURAL MISMATCH (name the
exact clause that fails — that names the barrier sharply for the
first time). Also survey the OTHER proved in-repo floors for the
same test at lower priority: the k-local LP floors (round 22), the
E1 floors, THEOREM D / Z-3's transport law (which already moved
between lanes once — "DLI law transports, blind convergence").

**D3 — THE WEAKEST USABLE FLOOR, ATTACKED.** Whatever D2 yields,
state the weakest BAND-AC lower bound that still serves at least
one consumer bar from D1 (a partial floor serving one consumer is
a real result). Attack it falsification-first at accessible scales:
compute exact band-analogue minima across layouts (the round-19+
standard: registered grids, 2-power configs, matched controls) and
test whether the candidate floor is (i) true in vivo with margin
and (ii) tight enough to matter. The floor-campaign posture: pose
weakest-form, attack, harden or kill.

**D4 — THE BARRIER MAP (if D2 = mismatch and D3 dies).** Then the
deliverable is the sharpest statement of WHY: the exact structural
feature of band counts that blocks every in-repo floor mechanism —
with the failed transports as evidence. A named, evidenced barrier
is the honest prerequisite for deciding whether this half needs
genuinely new mathematics or an external instrument.

## Escape tests (before the main work)

- Replay Z-FLOOR at two banked cells (SCRATCH COPY of the round-24/25
  z machinery) — the floor holds and is within 2x where banked.
- Reproduce one banked band-analogue exact count from the
  window-law data before computing your own.

## Rules (binding)

- QUARANTINE: do not read notes/pilots_20260802/CAMPAIGN_LEDGER.md
  at or below line 4062; do not read the other round-27 pilot dirs
  (pincer_formalization, nonpoly_flank_census, staircase_extension).
  Pass this clause to any subagent verbatim.
- COMPUTE LAW: every interpreter run via
  `tools/ramguard tiny|local -- python3 ...` from the repo root —
  including file patching and JSON peeking. RAMGUARD_TIMEOUT
  documented per use.
- BANKED SCRIPTS FROM SCRATCH COPIES ONLY (the round-26 lesson).
- RAM DISCIPLINE: file-at-a-time reads; never open dag.json; no
  bulk loads; checkpoint long runs; background batches with results
  files for >10-min runs.
- DRAFT-ONLY: writes only in
  notes/pilots_20260809/cancellation_recon/; no dag/nodes/tools
  writes; no git; no Modal; stdlib only.
- Register predictions with numeric windows BEFORE computing;
  misses first. Name every measured functional (CATCH-19C).
  Own-repo grep gates every "no such floor exists" claim
  (CATCH-24A). The f2 calibration clause binds on anything touching
  the F2 lane's objects.
- Your final message IS the report. End with a compliance paragraph.

## Pilot registrations (appended by the pilot before any computation)
