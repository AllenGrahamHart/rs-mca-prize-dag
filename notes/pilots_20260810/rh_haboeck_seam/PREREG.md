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
