# PREREG — apolar_origin (round 28)

Coordinator brief, written before dispatch. The pilot appends its own
registrations BELOW the brief BEFORE any computation.

## Mandate

THE NAMED THEOREM TARGET of the RH-AC program
(rate_half_band_crossing_location, created in the band
decomposition). Round 27's staircase_extension diagnosed the
wave-10 residual budgets {2^39, 2^39+1} TO THE UNIT: the counting
layer's cap (ERC2) is exactly ONE SLOPE above the target at the
first live degree, the cap is ATTAINED by non-Hankel objects (9
collinear disjoint split cubics at N=28 with Hankel nullity 0 —
exact certificates banked at
notes/pilots_20260809/staircase_extension/d1_realizability*), and
the m=1 fence (rate_half_ca_hankel_strict_m1_corefree_five_slope_
route_fence, PROVED, explicit F_17 witness) proves NO
incidence/core-freeness/split-fiber/Hankel-equation argument closes
the endpoint uniformly. The truth evidence is prime-field clean
(the only scaled violation is a q=17 smallest-field artifact; and
rate_half_residual_prime_field_collapse (PROVED) forces the
residual onto prime fields q > 2^167). YOUR JOB: prove the two
budgets by adding the missing ingredient — the APOLAR ORIGIN of the
Hankel system, i.e. the fact that realizable far-CA configurations
arise from an apolarity/kernel structure the design-cap-attaining
configurations lack. The round-27 cyclotomic law is your model
result: "realizable exactly when it does not exceed the target" —
that law, proved uniformly, IS the theorem.

## Deliverables

**D1 — THE MECHANISM EXTRACTION.** From the banked material (the
m=1 fence's proof; the realizability certificates; the Hankel suite
nodes' proofs — read them, they state their own domains), extract
exactly WHAT distinguishes a realizable configuration from a
design-cap-attaining one. The round-27 data says: over-target
instances have Hankel nullity 0; at-or-below-target instances have
positive nullity. Register a candidate characterization (an exact
condition C on configurations such that realizable => C and C =>
count <= target) BEFORE attempting the proof.

**D2 — THE PROOF ATTEMPT (the main event).** Prove, for the two
residual strata (w10-H1: budget 2^39 = strict A=3, s=0, e in
[2^37, floor((2^39-1)/3)]; budget 2^39+1 = A=3 e >= 2^37+1 plus
A=1 rows): every REALIZABLE configuration satisfies T <= rho+1.
Routes to consider (register your order): (a) uniformize the
cyclotomic realizability law — show every cap-attaining family is
cyclotomic-type and inherits the law; (b) the apolarity route —
the Hankel system M_r(y_0+Zy_1)Q(Z)=0 has an apolar/annihilator
interpretation; show cap saturation forces nullity 0 by a rank
argument uniform in the scale; (c) the one-slope route — the
deficit is exactly 1, so a parity/involution argument that any
realizable T = rho+2 configuration contains a forbidden
sub-structure. PARTIAL RESULTS ARE BANKABLE: the theorem at one of
the two budgets, or on a sub-stratum (e.g. e = m sharp face only),
each has named payoff.

**D3 — VERIFICATION.** Machine-check whatever lands at every
accessible scale (the round-27 harness: d1_realizability.py,
d1_cyclotomic_threat.py, d3_scale_field_census.py — SCRATCH
COPIES). The theorem must reproduce: the q=17 violation (your
statement must EXCLUDE q=17 by an explicit hypothesis, not ignore
it), the prime-field cleanliness, and the nullity dichotomy.

**D4 — THE PAYOFF, PRICED EXACTLY.** If D2 lands: state the
corollary chain — the far-CA layer extends to r <= 2^39+1, (RQ4)
completes, the crossing formula a_RH = n - B + 1 becomes
unconditional on all 2^128 < q < 2^167 WITHOUT residual, AND the
bracket top a_RH <= 3n/4 extends from q >= 2^169 to all q > 2^167
(the round-27 D4 cross-link — re-derive it, do not trust it). If
D2 does not land: the sharpest statement of what the apolar route
still lacks, with the failed attempts as evidence.

## Escape tests (before the main work)

- Replay d1_realizability.py + d1_cyclotomic_threat.py (SCRATCH
  COPIES; coordinator got byte-identical).
- Reproduce the m=1 fence's F_17 witness from the node's own
  verifier.

## Rules (binding)

- QUARANTINE: do not read notes/pilots_20260802/CAMPAIGN_LEDGER.md
  at or below line 4302; do not read the other round-28 pilot dirs
  (ssparse_endpoints, maxscan_algorithm, mca_safe_rewire). Pass
  this clause to any subagent verbatim.
- COMPUTE LAW: every interpreter run via
  `tools/ramguard tiny|local -- python3 ...` from
  /home/u2470931/smooth-read-solomin/prize — including file
  patching and JSON peeking. RAMGUARD_TIMEOUT documented per use.
- BANKED SCRIPTS FROM SCRATCH COPIES ONLY.
- RAM DISCIPLINE: file-at-a-time reads; never open dag.json; no
  bulk loads; checkpoint long runs; background batches with
  results files for >10-min runs.
- DRAFT-ONLY: writes only in notes/pilots_20260810/apolar_origin/;
  no dag/nodes/tools writes; no git; no Modal; stdlib only.
- Register predictions with numeric windows BEFORE computing;
  misses first. Name every measured functional (CATCH-19C).
  Own-repo grep gates every "missing ingredient" claim (CATCH-24A)
  — four missing-theorem claims in a row were bookkeeping; check
  whether the apolar characterization already exists under another
  name before building it.
- Your final message IS the report. End with a compliance
  paragraph.

## Pilot registrations (appended by the pilot before any computation)
