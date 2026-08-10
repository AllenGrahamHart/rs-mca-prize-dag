# FABLE_AUDIT — rh_type2_stratum (round 31)

Coordinator: Fable. Date: 2026-08-10. Pilot: Opus (~34 min, 48 tool
uses, 12 interpreter invocations, all ramguard; one MemoryError
under tiny disclosed and fixed by closed form, two documented
RAMGUARD_TIMEOUT extensions). REPORT.md persisted verbatim by the
coordinator (harness refused the pilot's write).

## Verdict

**BANKED — the largest single cap movement of the campaign:
residual (ii)'s 5.04e22 shrinks to 1,236,950,581,231 (40,722,652,881x
= 10.61 decimal orders), leaving a residual factor of EXACTLY 9/4
and ONE named missing inequality. The mechanism is (OV) — for every
pair of distinct supported slopes, w* <= |S_gamma u S_gamma'| — an
inequality banked in apolar's round-28 report and never summed over
pairs. Summed and fed through the incidence identity + the SAT4
convexity minimum it yields (NEWCAP): under (SAT1)-(SAT4) with
T = rho+2, w* <= 7m-1 asymptotically — the SAME 7m-1 apolar
computed as the location of the AVERAGE configuration, now
re-derived as an UPPER BOUND on w*. Since CAP(m,a) is increasing in
a, the stratum cap re-evaluates at a = 7m-1 with spend floor m+2
instead of 3: cap 9m-17. Bonus theorems: a = 8m-2 is VACUOUS for
all m >= 2 (w* = 2rho forces the disjointness R4 refutes), and
m = 1 is STRUCTURALLY DISJOINT from residual (ii) (p is pinned to
3 and wt(kappa) >= R+1 forces j = 0 — a proof, not a measurement).
Neither budget closes: the honest frontier is (FR), the max-vs-mean
upgrade |S_gamma ^ W| <= ~2m against ALL of W at once, with an
in-repo no-go precedent (the l1_fpc5 distance-only no-go) flagged
as possibly transporting — if it does, 9/4 is this route's ceiling
and the next instrument must be algebraic (the (GNF) f_gamma
polynomials or the Hankel pencil).**

## Coordinator verifications (mine)

| what | result |
|---|---|
| (OV) -> (NEWCAP) algebra | HAND-VERIFIED end to end: the pairwise union bound, the C(T,2) sum, the incidence identity sum_x C(d_x,2), the convexity minimum Lmin(O), the O-monotonicity slope (T-1)-(m-1) = 3m+1 > 0 with T = 4m+1 |
| the exact ledger at m = 2^37 | INDEPENDENTLY RE-DERIVED, all five numbers exact: banked cap 50371909150701174915072; a_max = 7m-1 = 962072674303; sharpened cap 1236950581231; AO1/2^39 = 2.25 - 2.7e-11; shrink 40722652881x |
| d4_verdict.py + d2_transport.py replays | both green, outputs match the results files |
| the four port anchors | all verbatim (apolar REPORT :57 the union bound, :63 the 7m-1 mean, :78 R4; crossing statement :477 the 5.04e22, :207 the ~7m-1 location) |
| the "~39-order" correction | CONFIRMED AGAINST MY OWN BRIEF: the true gap was 11 decimal / 36 binary orders; my "39 orders" conflated 2^39 with decimal orders — my error, banked |

## Audit judgements

- **The result is a direction-reversal, not new arithmetic — and
  that is its strength.** Every ingredient was banked; apolar read
  7m-1 as where the average sits and concluded "does not move
  either budget"; the pilot read the same number as a ceiling via
  the every-pair quantifier. CATCH-24A subtraction is exemplary:
  four ports declared, contribution scoped to the direction.
- **The self-falsification (MISS 2) is the round's process
  exhibit**: the pilot's own D1.6 "integer-feasibility certificate"
  (published in its results file) claimed no counting argument
  could close the a = 8m-2 face; adding (OV) killed the
  certificate — and the failure mode IS the theorem. The stale
  conclusion is flagged in-file, not edited (round-29 precedent).
- **Honest conditionality**: (NEWCAP) is conditional on (SAT3)
  T = rho+2; falsifier F1 (a realizable T = rho+2 configuration
  with w* > 7m-1) is LIVE and unexercised — the census never
  reached T > 3, declared as zero-power. (EQ)'s converse is
  sampled (121/121), not proved. Both carried into the addendum.
- **MISS 3 honestly priced**: no replay-identity evidence this
  round (own decoder, not the banked census machinery); the one
  reproduction check is the exact 5.04e22 re-evaluation. My own
  independent re-derivation of the ledger (above) substantially
  covers this gap for the headline numbers.
- The 906 firings of the w*-minimality counter (planting a third
  slope drops true w* below 2rho) are the empirical shadow of (OV)
  — good convergent evidence.

## Corrections applied

- critical/nodes/rate_half_band_crossing_location/statement.md —
  round-31 type-2 addendum: (OV)/(NEWCAP)/the sharpened ledger, the
  9/4 residual + (FR), the vacuity of a = 8m-2, the m = 1
  structural disjointness, supersession notes on the banked
  5.04e22 and "2/3 window" figures, and the coordinator's own
  "~39-order" brief-line correction. No status flips.

## Follow-ups filed (not executed)

- (FR) is the round-32 anchor for residual (ii): the max-vs-mean
  upgrade of the overlap statement against all of W. Check FIRST
  whether the l1_fpc5 distance-only no-go transports — if yes, go
  algebraic ((GNF) f_gamma or the Hankel pencil) without spending a
  round on combinatorial retries.
- Falsifier F1 needs a targeted T > 3 construction (MODE B extends;
  the census's T = 3 wall is a sampler limit, not a fact).
- Mint candidates: (NEWCAP) + the vacuity lemma + the m = 1
  disjointness lemma as a package; (GNF) as a port note into the
  ca_hankel lane.
- Cross-pilot: (OV) is the same object the rh_overlap_cap pilot is
  attacking from the T5 side — reconcile at round close.
