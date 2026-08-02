# C1 doubling-orbit pilot (2026-08-02)

> **Headline: the doubling dynamic is exactly right and exactly
> uninformative.** All identities of `dli_c1_doubling_coboundary_identity`
> survive 13,501 exact rows; but the excess X is UNCORRELATED with the
> doubling-cycle structure (Spearman <= 0.11) and strongly correlated
> with short-relation structure (-0.55). The lane that closes the
> analogue is a RESULTANT ROUTER ON THE RELATION SIDE, built and
> closed-loop verified here: it COMPLETELY PROVES the analogue target at
> 2N=8 and 2N=16. Pilot by an Opus 5 subagent; audited by Fable
> (FABLE_AUDIT.md). Coverage: 13,501 primes at 2N=32 (q to 3e6); 54,071
> rows at 2N=8; 27,055 at 2N=16; 300 at 2N=64.

## Structure theorem (exact, simplifying)

Q = F_q^*/H is cyclic and doubling is TRANSLATION by the class of 2:
every cycle has the SAME length r = ord_q(2)/gcd(ord_q(2), 2N), with
M/r cycles (cosets of <2,H>). There is no cycle-length spectrum to
exploit. Verified explicitly on 170 rows.

## Bankable corollary of DB-2 (the AM-GM floor)

Cycle products = 1 give per-cycle mean >= 1, hence avg_C A >= 1 and

    X >= (q-1)/(q 2^N),   equality iff A == 1.

Verified 13,501/13,501; equality exactly at the r=1 rows (q = 257,
65537; plus 641 at 2N=64). This is the ONLY quantitative consequence of
the doubling dynamic in the data — and it is a LOWER bound.

## Hypothesis verdicts

- H-A (excess ~ cycle structure): NO. X vs r: +0.108; vs n_cycles:
  +0.007; vs v2(q-1): +0.019; vs MIN RELATION WEIGHT: -0.553. Rows
  where Q is a single cycle (maximal mixing) are indistinguishable.
- H-B (small r => flat): NO except r=1 exactly. q=274177 (r=4,
  q | 2^64+1) has avg A = 79,055 — ABOVE typical. The finite router
  q | 2^(2N r)-1 buys only the Fermat rows.
- H-C/K4: PATTERN PRESENT, NOT TRIGGERED. q=70529: X = 2.2353 (max in
  hard regime), min weight 7 (no relation of weight <= 6), no short
  cycle (r=551) — the K4 shape at the ledger's wired cut. But the
  excess has a bounded owner set (15 orbits, weights 7-9; certificate
  Res(f, x^16+1) = 70529 exactly, independently re-verified). Across
  13,090 hard rows, unowned excess beyond weight 9 never exceeds 0.131.
  **The owner budget must run to weight ~9-10; the wired weight-3/4
  exclusions control none of the excess in this regime.**

## THE FINDING: the relation-side resultant router

q carries a weight-w relation iff q | Res(f, x^N+1) for some ternary f
of weight w — a q-INDEPENDENT integer norm. Complete finite theorems
(closed-loop verified against the independent MITM sweep):

- **2N=8: max|Norm| = 9 over ALL ternary f** (re-verified by Fable) =>
  NO admissible prime has any relation => X = 1 - 2^4/q < 1 < 4
  UNCONDITIONALLY. (54,071 rows confirm.)
- **2N=16: max|Norm| = 2401 = 7^4** => exactly eleven primes <= 881
  carry relations; every larger q has X = 1 - 2^8/q exactly. Analogue
  target proved unconditionally (27,055 rows; max X = 0.999915).
- 2N=32 per-weight: weight <= 4 bound 38416 = 14^4; weight <= 5 bound
  279841 = 23^4 — explaining the shrinking excess tail exactly. The
  norm ladder 9, 7^4, 14^4, 23^4 suggests a c_w^(N/4)-shaped law.
- 7 of 8 high-excess primes ARE the norms of low-weight ternary
  cyclotomic integers on the nose.

## Cautions

- **Mutation control: never instantiate the analogue at non-power-of-two
  order** (odd prime factor p gives a universal weight-p relation for
  every q; measured median X jumps to 1.55/2.24 at 2N=12/24).
- **The analogue lab certifies the mechanism, not the constant 4**: the
  size-independent p90 excess GROWS with N (0.931 -> 0.929 -> 1.154 at
  N = 4, 8, 16); max X in the hard regime is 2.357 (margin 1.643).
  2N=32 is the largest order whose hard regime is reachable.
- sd(log A) is universal at 4*pi/sqrt(3) = 7.2552 (independent-factor
  value); a Gaussian moment model is wrong by 7 orders — the moment is
  set by the hard ceiling and near-independence; concentration is at
  the COSET level (top 1% of cosets carry 85-95% of the mass), not the
  cycle level. Clean framing: X = (true moment)/(independent model),
  and X <= 4 says "within a factor 4 of independence."

## Retargeted sequencing (adopted)

1. Bound max|Res(f, x^N+1)| over ternary weight-w f (the c_w^(N/4)
   conjecture) — exact, q-free, the audit's surviving discipline on the
   RELATION side.
2. Bound the NUMBER of relation orbits n_w in the active band (these
   are the ledger's A_j terms).
3. Only then the exponential-moment theorem, framed as
   moment/independent-model <= 4 — not as cycle dynamics.

(Scripts: orbit_spectrum.py, analyse.py, structure_checks.py,
cycle_spectrum.py, order64_sweep.py, scaling_transfer.py,
relation_certificates.py, low_weight_router.py; 16 result JSONs.)
