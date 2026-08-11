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
