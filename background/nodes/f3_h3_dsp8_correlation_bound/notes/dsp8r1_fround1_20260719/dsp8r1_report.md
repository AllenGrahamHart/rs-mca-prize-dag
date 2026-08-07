# DSP8 F-round 1 — report

- Predicate: `f3_h3_dsp8_correlation_bound` — at every official row
  (n = 2^s, 13 <= s <= 41, p = 1 mod n, n^2 <= p <= 6^{n/4}):
  10 J_25^0 + 17 J_25^A <= 892 n^2, J = 8D (DSP7), retained targets
  t != 1 with P(t) >= 25, disjoint distance-six split-pencil x line-fiber
  correlation (DSP4/DSO4 definitions, reused exactly; constants 892,
  weights 10/17, normalization J=8D, cutoff 25 all pinned, none touched).
- Round: pre-registered F-round 1, instantiated in dsp8r1_falsifiers.md
  BEFORE any computation. Census: dsp8r1_census_modal.py. Full shard
  ledger + Modal app ids + coverage table: dsp8r1_results.md. Catches:
  dsp8r1_findings.md.

## VERDICT: SURVIVED (vacuously at the pinned cutoff in the measured scope)

No kill line fired. 48,544 rows measured exactly across nine 2-power
scales (32..8192, the last one OFFICIAL); not one row possessed a single
retained target (t != 1 with P(t) >= 25), so LHS = 0 <= 892n^2 with
infinite relative margin everywhere, including at the richest official
row known to the project.

## Kill-line outcomes

- KILL-1 (exact row with 10J_25^0 + 17J_25^A > 892n^2): NOT FIRED.
  Worst LHS/(892n^2) per scale = 0 exactly, at all nine scales.
- KILL-2 (monotone rho_max trend extrapolating past 1 at official
  aspect): NOT FIRED — rho_max(n) is identically zero; there is no
  monotone increase to extrapolate. The only nonzero signal anywhere is
  the sub-cutoff diagnostic ratio_19 (a pre-named NOT-kill), which
  DECREASES with n where nonzero: 9.5e-6 (2048) -> 2.4e-6 (4096) ->
  1.2e-7 (8192 official).

## Controls (all green; round valid)

- PC-1 router-fixture totals: exact MATCH (195/18/200), locally and on
  the Modal image.
- PC-2 banked wave-5 boundary-row constants at OFFICIAL row
  (8192, 67657729): exact MATCH (maxP=20, two rich targets, R=1 each,
  X18=4, X35=0).
- PC-3 DSP2/DSP3/DSP4/antipodal-class identities: PASS on all 408 fibers
  of (32,1153) and asserted on every rich fiber measured anywhere.
- Dual implementation: numpy-vs-pure FULL P-counter + row-field match on
  the three analogue rich rows (1.6M-6.6M targets each) and on three
  control rows.
- MC-1 (+1-edge census mutation): TRIPPED (required).
- MC-2 (kill-detector at RHS const -1): TRIPPED on all rows (required).

## Evidence weight (honest scope)

What this round DOES establish:

1. Exhaustive corridor closure at n=32: every one of the 7,937
   official-shape rows in the ENTIRE corridor [1024, 6^8] has
   max P = 10 < 25 — DSP8 is an (enumerated) fact at that scale.
2. Deep exhaustive low-p windows at n = 64..4096 (p <= 1e7-2.1e7, i.e.
   the dense end where richness concentrates) plus high-p samples at
   ~1e11 (all maxP = 2): 40,602 further rows, all vacuous.
3. At the official scale n=8192 (in-corridor, kill lines apply
   directly): the first five official primes, including the richest
   known row, have J_25 = 0.
4. The richness frontier maxP saturates at 20 across three consecutive
   scales (2048, 4096, 8192) — 5 below the cutoff — and every observed
   near-rich row has the same twin structure: exactly two antipodal-free
   targets with P = 20, 10 generic members, N_6^disj in {44,45}.

What this round does NOT establish (stated plainly):

- The bound was never STRESSED at its own cutoff: J_25 = 0 everywhere
  measured, so survival is vacuous survival — evidence that retained
  targets are extremely rare at analogue and boundary-official aspect,
  not evidence about the size of the correlation when they exist.
- Officially the corridor reaches p ~ 6^{n/4} at n up to 2^41; rich
  primes (if any) at official aspect with P >= 25 would come from the
  collision-norm accident set, which this round did not attempt to
  construct (that is the fixed-order reserve route's machinery).
- No claim about t = 1, no claim about sub-cutoff moments, no promotion
  of any node.

Net: DSP8's F-round-1 wall stands, with the important structural caveat
that its non-vacuous regime remains unobserved — the predicate has not
yet been tested where it has content. Evidence weight: MODERATE for
"official rows with P >= 25 are extraordinarily rare"; WEAK-only for the
inequality's tightness in the non-vacuous regime.

## Round-2 design (pre-commitments for the next falsification round)

1. **Engineered rich-prime hunt (the real round-2)**: use the wave-12/13
   collision-norm ideal machinery (rich primes divide members of the
   finite low-distance collision-norm set; norm <= 6^{n/4}, and the
   coupled-ideal sieve norms <= 6^{n/4}/4) to CONSTRUCT candidate primes
   with P(t) >= 25 at orders 2048-16384, rather than scanning for them.
   Kill lines unchanged. If construction provably fails below P = 25 at
   those orders, that itself is a route-strengthening fact worth a node.
2. **Twin-fiber structure probe**: all four observed near-rich rows have
   the twin (P=20, antipodal-free, all-disjoint) shape, and the DSO1
   overlap payment is INACTIVE there (N_6^disj = C(10,2)). Pose and test
   a "P <= 20 at official aspect" satellite (it would close DSP8
   vacuously); its falsifier is any official-analogue row with
   P(t) >= 21, t != 1 — cheap to scan for and sharply defined.
3. **Antipodal-class starvation check**: every rich fiber observed is
   antipodal-free (class A never fired above P = 6-ish). The 17/10
   weight asymmetry is untested; round-2 should record the antipodal
   class's maximum P per row to see whether J^A can EVER be nonzero at
   cutoff 25.
4. Keep the 892n^2 / 10:17 / J=8D pins frozen; keep the dual
   implementation + PC-1/PC-2 controls as the standing harness (they are
   now demonstrated to trip).

## Reproduction

- Pre-registration: dsp8r1_falsifiers.md (same directory).
- All commands + Modal app ids: dsp8r1_results.md shard ledger.
- Census: dsp8r1_census_modal.py; control replay:
  `tools/ramguard tiny -- python3 <scratchpad>/dsp8r1_census_modal.py control expect=195,18,200`
  from the prize repo root; any row exactly reproducible via
  `... --args "replay n=<n> p=<p>"` (Modal) — all identity assertions
  (DSP2/3/4, antipodal two-form) run on every rich fiber.
