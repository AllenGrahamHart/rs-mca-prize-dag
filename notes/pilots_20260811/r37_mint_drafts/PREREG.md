# PREREG — r37_mint_drafts (round 37)

Coordinator brief. Constraints: CONSTRAINTS.md in this dir (binding).
AUDIT-AND-DRAFT: this pilot DRAFTS node packages in its own
directory; the coordinator line-audits and wires them. You never
touch dag/, critical/, background/ or tools/.

## Anchors (read these two FIRST, then register the drafting plan)

1. `critical/nodes/rate_half_band_crossing_location/statement.md`
   — read ONLY the addenda sections from "## Round-34 layer-A
   addendum" to the end (bounded windows; this file is >4600
   lines — grep for "## Round-3" headers first and window each).
2. `background/nodes/rate_half_layer_a_saturation_count_route_fence/statement.md`
   — the FORMAT EXEMPLAR (a recent, well-formed background node:
   statement header block, display math, scope section; its
   node.json and verify.py live beside it — read those too as
   part of this anchor).

## Mandate

THE MINT WAVE, DRAFTED. Rounds 34-36 banked ~30 mint-queue items
as addenda on the crossing node; none is yet a first-class node.
Draft the TOP TEN as complete node packages in YOUR OWN directory
(one subdirectory each: statement.md + node.json + verify.py +
where applicable proof.md), ready for coordinator line-audit and
wiring. Every verify.py must RUN (under ramguard, from repo root)
and PASS before you include it. Statements must carry exact
sourcing (which round/bank, which addendum section) and honest
status (PROVED only where the addendum says
coordinator-audited/hand-verified with replays; POSED/TARGET
otherwise — when in doubt, the weaker status).

## The ten packages (priority order; draft in this order)

1. **statement_u** — Statement U + the exact-value consequence
   B_ca^far(k+2^34) = r+1; the T_fib/T_sym/T_rand decomposition;
   U-sym's razor kill; U-rand open. Status: TARGET (the statement)
   with PROVED components clearly separated. verify.py: the razor
   integers + the fibre-cap pigeonhole arithmetic.
2. **l2_par_parametrization** — the (PAR) rational parametrization
   + (RES) gcd criterion + the determinantal form (round-36 bank
   2; coordinator hand-verified — PROVED). verify.py: verify the
   three identities symbolically over two small fields on random
   draws, plus one certified T = 2 witness replay.
3. **l2_nonempty_theorem** — the round-35 R-L2 witness theorem
   (12 objects, 5 fields; the D-B criterion; 11m-4 vs the dead
   +4 reading). PROVED (witness-checkable). verify.py: re-verify
   the published q=97 witness from scratch.
4. **hr_dictionary_common_support** — h_r = rho + deg(e_1/e_0);
   common support forced; LB1 unique-and-forced at h_r = rho+1;
   the p*(d) law with its named failures. PROVED components +
   POSED law. verify.py: the dictionary at 2 shapes x 2 fields.
5. **negation_closure_excess_fence** — the T = 95 mechanism
   (even-locator collapse, count C(m-1, r/2-1), the control, the
   razor kill 2^33-1); cross-pointer to the e22 locator algebra.
   PROVED (measured + counted exactly). verify.py: reproduce the
   count at one (n, q) cell.
6. **la_eq_and_geometry_counterexamples** — (LA-EQ) + the H1 and
   H1+H2 nullity-1 families (closed form) + the generalized fence
   Z^m - X^{2m} + the (RIC3)/row-surplus cross-pointers (round-36
   bank 1). verify.py: one H1+H2 exhibit + one generalized-fence
   cell.
7. **share3_luroth_template** — (SHARE3-m): the Lüroth pullback
   identification, the waste law 3(m-1) mod k, the corrected
   demand D(k,k') + D_max(m) = 4m-8, the constant-norm existence
   mechanism, the one-coincidence scope table (round-36 bank 4;
   flag the compliance censure in provenance). Mixed
   PROVED/POSED. verify.py: the demand arithmetic + one
   constant-norm pencil existence check at q=193.
8. **outm_identity_degm** — (OUT-m) in the corrected form + the
   aggregate identity sum eps~ = sum def(x)*t_x + (DEG-m) with
   its budget + the completion-level record (rounds 34-36).
   POSED (inherits). verify.py: the identity on the banked m=3
   witness.
9. **type2_ledger_scope_fence** — the (C2)-vacuity-by-sign law,
   the 62r/63 threshold, "vacuous by sign before vacuous by
   counting" (round-35 bank 2). PROVED (arithmetic). verify.py:
   the sign arithmetic at razor + one small cell.
10. **sat3_ledger_corrections** — the realizability-ledger record:
    the automorphism quotient (round 34), the (ERC2)-forced dim
    18 (round 36), the stacked +8..+10, the double re-pose to
    m <= 1; and the C(16m,4m-1) first-moment gate with its m=1
    16=16 double calibration. HEURISTIC/RECORD status. verify.py:
    the excess arithmetic at m = 1..4 + the gate at m=1.

## Deliverables

**D1 — the ten packages**, drafted in priority order (if time
runs short, fewer COMPLETE packages beat ten partial ones — a
package without a passing verify.py does not count). **D2 — a
MANIFEST.md** in your dir: per package, the source addenda
(file:line), the status you assigned and why, what you could NOT
verify and left flagged, and the suggested wiring (consumers /
evidence edges — suggestions only). **D3 — a DISCREPANCY
section**: anything in the addenda that resisted precise
statement (contradictions, ambiguous scoping, missing constants)
— finding these is as valuable as the drafts. **D4 — VERDICT**:
package count completed, misses first, compliance.

## Blind priors to register

Expected packages completed (a number of 10); P(at least one
addendum contains a discrepancy that blocks a draft); P(all
verify.py drafts pass on first run) — plus your MISS-2 guard and
zero-power declarations (a draft is not a wired node; statuses
are proposals).

## Pilot registrations (r37_mint_drafts, filed after the two anchors, before any other read/grep/ls/interpreter)

**Read state at filing.** Anchor 2 read whole (statement.md,
node.json, verify.py — 89/30/85 lines). Anchor 1 read in four
bounded windows covering L3186-3870, L3868-3967, L4270-4645
(the Round-34/35/36 bank addenda + the three ROUND CLOSE
sections). DISCLOSED GAP: L3967-4269 (Cycles 146-157, Codex
cycle addenda) NOT yet read at filing time; I will window it
only if a draft demands it, and will report the read as
partial either way.

**Point predictions.**
- Expected packages COMPLETE (statement.md + node.json +
  passing verify.py, all four artifacts where proof.md
  applies): **7 of 10**. Distribution: P(>=5) = 0.85,
  P(>=7) = 0.55, P(10) = 0.15. A package with a verify.py
  that does not pass counts 0, per the brief.
- P(at least one addendum contains a discrepancy that BLOCKS a
  draft — i.e. forces me to ship the package at a weaker
  status or drop a named component): **0.80**. Prior reason:
  the round CLOSE sections themselves record eleven
  consecutive rounds of banked-text corrections
  (L4623 "AUDIT LEDGER (11th consecutive catching round)"),
  so the base rate of live contradictions in this corpus is
  high by the corpus's own accounting.
- P(ALL verify.py drafts pass on FIRST run): **0.12**. Per-file
  P(pass first run) ~ 0.75, and I intend to iterate until each
  passes; only the first-run figure is being predicted.
- P(at least one item I draft turns out to duplicate an
  existing in-repo node): **0.45** (the corpus has already
  self-caught two such: L3225-3233 the dichotomy was
  ALREADY-PROVED in-repo; L3838-3846 three D3 objects
  subtracted to PROVED nodes).

**MISS-2 GUARD (mean-vs-max), registered.** The named failure
mode I am guarding against is round-34 bank 4's MISS 2
(L3436-3439: a degenerate 1.4%-rate family briefly misread as
refuting a count) and its cousin at L3210-3214 ("Rout <= 3"
banked as a bound when the bank's own file recorded
maxRout = 4). GUARD: every numeric constant I transcribe into
a statement.md carries an explicit tag in the source line —
EXACT (closed form or hand-verified arithmetic),
MAX-OVER-SAMPLE (a measured ceiling, e.g. a DFS ceiling),
MEAN/RATE-OVER-SAMPLE (a hit rate), or RANGE-OVER-CELLS. No
MAX-OVER-SAMPLE or MEAN-OVER-SAMPLE quantity is written as a
universal bound in any statement or node.json "statement"
field, and no such quantity carries PROVED. Specifically
pre-flagged as sample-quantities, not theorems, before I draft
them: T = 95-98 (L4460-4461), the DFS ceilings 7/8/9
(L3703-3720), the 12/9/9 complete fibres (L3539-3541 analogue
at L4540), a* = 13 on 5 of 6 witnesses (L3583-3586). If a
verify.py of mine reproduces a max over a sample, its PASS
line says so in words.

**Zero-power declarations.**
1. A DRAFT IS NOT A WIRED NODE. Every status in every
   node.json I write is a PROPOSAL to the coordinator. I have
   zero authority to wire, and I write nothing outside
   notes/pilots_20260811/r37_mint_drafts/.
2. Zero power over the underlying mathematics. My verify.py
   files replay arithmetic, small-field algebra, and counting
   identities. They do NOT re-run the original searches
   (DFS censuses, five-field sweeps, 40000-draw ALLOC runs).
   A PASS is evidence that the STATEMENT I transcribed is
   self-consistent and matches the banked constants — not
   that the addendum's experiment was correct.
3. Zero power over q-uniformity and over the official row.
   Everything I compute runs at small primes (q <= ~1000) or
   in exact integer arithmetic on the razor constants. Nothing
   I check bears on q ~ 2^128 beyond exact-integer replay of
   already-banked razor numbers.
4. Zero power over novelty/duplication. I will grep the repo
   before any novelty language (CATCH-24A, hyphenated and
   infixed variants), but a negative grep is not a proof of
   absence; the coordinator's subtraction pass is the
   authority.
5. Zero power over (SAT3)-conditionality. Most m >= 2 content
   in items 1-10 is (SAT3)-conditional per L3263-3264 and
   L3866; I inherit that conditioning verbatim and do not
   discharge it.
6. Zero power over the compliance censure in item 7's source
   (L4572-4574, one bare-python3 breach in round-36 bank 4).
   I record it in provenance; I do not adjudicate it.
