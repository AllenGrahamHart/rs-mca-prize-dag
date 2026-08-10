# PREREG — rh_haboeck_seam (round 32)

Coordinator brief, written before dispatch. The pilot appends its own
registrations BELOW the brief BEFORE any computation beyond the two
named anchors. AUDIT-AND-DRAFT: any surgery stays coordinator-gated.

## Anchors (read these two FIRST, then register blind priors)

1. `background/nodes/haboeck_quadratic_johnson_mca_import/statement.md`
2. `background/nodes/rate_half_haboeck_quadratic_johnson_safe_bracket/statement.md`

## Mandate

ADVERSARIAL. Wave 57 moved the razor bracket top for the first time
since round 27, via an EXTERNAL theorem import (Haboeck, IACR ePrint
2025/2110 Thm 2) specialized at the official row. The campaign's
record says newly-landed load-bearing text grows a catch within one
or two rounds (P0, T5's object slip, F1's stale reduction, the F4
e-axis). An external import that moves a critical bracket is the
highest-stakes text of the wave. YOUR JOB: break it, or certify it
to the campaign's standard. The verifiers pass — your target is
what verifiers cannot see: OBJECT IDENTITY and CONVENTION seams.

## Deliverables

**D1 — THE OBJECT IDENTITY (CATCH-24C, the prime suspect).**
Haboeck's E_m counts finite affine slopes z with an |A| >= (1-γ_m)n
support where (f_0 + z f_1)|_A is in C|_A BUT (f_0,f_1)|_A is NOT
in C^2|_A — the pair-unexplained slopes. Quote, file:line, the
EXACT definition of the B_mca numerator that
rate_half_band_crossing_location's crossing inequality consumes
(B_mca(a_RH) <= B* < B_mca(a_RH - 1)) — per received line? per
pair? counting which slopes, with or without the pair-explained
exclusion? Infinite slope included? Then check the safe-bracket
node's (RHJ3) claim "the full support-wise MCA numerator is safe at
a_m: B_mca(a_m) <= Q_m" — does E_m's count COVER B_mca's count, or
is there a class of B_mca-bad slopes that E_m excludes
(pair-explained slopes! the z where (f_0,f_1)|_A IS in C^2|_A —
are those bad for B_mca? do they exist above the unique-decoding
radius?). The round-31 T5 death was EXACTLY this shape (a cap
constant transported between two different objects). Both texts
quoted side by side; any daylight is the finding of the round.

**D2 — THE CONVENTION CORRECTION.** Cycle 41 says "the source
convention corrected to rho = (k-1)/n". Verify: what is Haboeck's
rho (degree bound d vs dimension k = d+1 — the import statement
says deg(p) <= d, dim d+1)? Is the official row's code deg < k
(dim k) or deg <= k (dim k+1)? An off-by-one in rho at n = 2^41
moves (RHJ2)'s a_m by ~sqrt scale — recompute a_9, a_94, a_95 from
scratch under BOTH conventions and compare with the banked
integers. Also audit the integerization directions in (RHJ1)-(RHJ2)
(floor on Q_m — safe direction? ceil on a_m — safe direction?) —
each rounding must be on the SAFE side of the inequality chain.

**D3 — THE LADDER ARITHMETIC + HOSTILE EXTENSION.** Re-derive the
full m-ladder (Q_m, a_m for m = 3..96) by exact integer arithmetic
from the import's (HJ1) alone, independently of the banked
verifier. Confirm: m=9 first improvement, m=95 cap, m=96
infeasible, the two razor thresholds. Then the e-axis check: the
import's field hypothesis (any F_q? the O6 rule says no future
far-CA upper bound may assume no-subfield — does Haboeck's proof
per the import's own audit notes carry a field restriction, and is
the widened pose's e in {1..6} covered?).

**D4 — SOURCE AUDIT, honestly scoped.** The import cites ePrint
2025/2110 Thm 2 with "statement and proof audit" claimed in-repo.
You have no network. Audit what IS in-repo: the import node's
proof.md (what does the audit actually check?), any vendored
fragment, the "excluded BCHKS25 refinement" boundary (is anything
downstream quietly using the linear refinement?). ZERO-POWER
declare what cannot be checked offline; name the outward
verification question for the coordinator if one is needed.

## Constraints (binding)

- COMPUTE LAW: never bare python3; ramguard tiny/local, repo root,
  literal `--`; RAMGUARD_TIMEOUT documented; stdlib only; no
  Modal/network/git.
- RAM DISCIPLINE: file-at-a-time; NEVER open dag.json; bounded
  windows on large statements.
- WRITE SCOPE: ONLY notes/pilots_20260810/rh_haboeck_seam/. No
  dag/, nodes/, tools/ edits. No git. Never touch prize-codex-*.
- QUARANTINE: never open notes/pilots_20260802/CAMPAIGN_LEDGER.md;
  never read siblings (rh_fr_algebraic, rh_farca_upper,
  rh_residuals_close); round-31 and earlier readable.
- BLIND PRIORS: after the two anchors only, append "## Pilot
  registrations" (P(at least one real seam), the seam class you
  expect (object/convention/rounding/field), P(the bracket numbers
  survive re-derivation)) BEFORE any further read.
- REPORT: REPORT.md (harness-refused fallback: return verbatim; in
  all cases ALSO return verbatim as final message); MISSES-FIRST;
  the full attack log with what-would-have-killed per attack;
  CATCH-24C both-sides quotes; CATCH-24A greps; zero-power
  declarations.

## Pilot registrations

Written after reading ONLY the two named anchors
(`haboeck_quadratic_johnson_mca_import/statement.md`,
`rate_half_haboeck_quadratic_johnson_safe_bracket/statement.md`)
and before opening any other file in the repo.

**R0 — disclosure of anchor-only work already done.** Reading the two
anchors, I carried out one pencil check with no further reads: HJ1's
`(ell_m^7/3)(rho n)^2` with `ell_m=(m+1/2)/sqrt(rho)` equals
`(2m+1)^7 n^{7/2} / (384 (k-1)^{3/2})` under `rho=(k-1)/n`, whose square
is exactly `N_m/D = (2m+1)^14 n^7 / (384^2 (k-1)^3)`; and
`(1-gamma_m)n = ((2m+1)/(2m))sqrt(n(k-1))` squares to RHJ2's
`(2m a)^2 >= (2m+1)^2 n(k-1)`. So the RHJ1/RHJ2 *algebraic forms* are
faithful transcriptions of HJ1 under the stated reindexing. This
raises my prior on the arithmetic lane and lowers it nowhere else; it
says nothing about object identity, which is untouched by it.

**R1 — P(at least one real seam in the wave-57 import chain) = 0.72.**
Base rate from the campaign's own record (P0, T5's object slip, F1's
stale reduction, F4's e-axis: newly-landed load-bearing text has grown
a catch within one or two rounds every time), discounted slightly
because the transcription algebra above already came out clean on
first contact, which is weak evidence of a careful author.

**R2 — seam class I expect, ranked.**
1. OBJECT (0.50 of my seam mass). Specifically the D1 shape: `E_m`
   carries an explicit exclusion — `(f_0,f_1)|_A not in C^2|_A` — and
   RHJ3 asserts a bound on "the full support-wise MCA numerator"
   `B_mca`. The word "full" is doing visible work in a sentence whose
   supporting theorem is explicitly *partial*. If `B_mca` counts every
   bad slope rather than only the pair-unexplained ones, RHJ3 is a
   bound on a subset masquerading as a bound on the whole, and the
   crossing inequality downstream consumes the wrong object. This is
   the round-31 T5 death re-run on a new pair of objects.
2. CONVENTION (0.25). The `d` vs `K` seam. The import states
   `deg(p)<=d`, `dim = d+1`, `rho=d/n` and then reindexes
   `d=K-1, rho=(K-1)/n`. That reindexing is internally right for
   `RS={deg<K}`; the exposure is whether the official row's `k=2^40`
   is a dimension or a degree bound downstream, i.e. whether the
   bracket should be using `(k-1)` or `k` in `D` and in `a_m`. Cycle
   41's note that "the source convention corrected to rho=(k-1)/n"
   tells me this seam was already touched once, which is exactly where
   a half-applied correction lives.
3. ROUNDING (0.15). floor on `Q_m` / ceil on `a_m`. My anchor-only
   read says both look safe-side (an integer count below a real bound
   may be floored; an integer agreement threshold above a real
   threshold must be ceiled), so I expect this to survive; the live
   risk is a *third* rounding somewhere downstream in the crossing
   inequality, or `sqrt` evaluated in floating point.
4. FIELD/e-AXIS (0.10). O6 forbids a no-subfield assumption; imports
   of coding-theoretic list-decoding theorems often carry a
   large-field or prime-field hypothesis that the import statement
   silently drops. The import statement as written says `F_q` with no
   restriction, which is either genuinely unrestricted or a dropped
   hypothesis — I cannot tell from the anchor.

**R3 — P(the banked bracket integers survive exact re-derivation from
HJ1 alone) = 0.86.** Elevated by R0. The residual 0.14 is mostly the
`(k-1)` vs `k` fork in R2.2 and the chance that `m=9 / m=95 / m=96`
boundary claims were computed with a floating-point `sqrt` near a tie.

**R4 — P(I return a "no seam" certification) = 0.30**, and I register
now that I will only return it after every attack in the brief has run
and been logged with its what-would-have-killed.

**R5 — pre-registered falsifiers for my own primary hypothesis (D1).**
I will call CATCH-24C *dead* (i.e. no object seam) if EITHER: (a) the
downstream definition of `B_mca`'s numerator itself carries the
pair-unexplained restriction, in matching words; OR (b) the chain
carries a separate, cited discharge of the pair-explained class (e.g.
a lemma that pair-explained slopes above the relevant radius are
empty or are absorbed elsewhere), and that discharge is not itself
assumed. I will call it *live* if `B_mca` is defined as an unrestricted
bad-slope count and no such discharge exists in the chain.
