# TARGET 3C — THE PRIMITIVE-CENSUS FLOOR (mechanically extracted).
# Prove or falsify.

Extraction provenance: built mechanically from the live consumer
(extraction audit: notes/kernel_basis/TARGET_3C_EXTRACTION.md);
NOT guessed. Survived the full adversarial checklist (32/32, exact
arithmetic) before freezing: every known falsifier family provably
fails the hypotheses below (verification table in the audit).

## Setup

F a finite field of characteristic p, |F| < 2^256. D = mu_N <= F^x,
N = 2^s a power of two. B0 = F_p(D) the generated field, Q = |B0|.
t >= 1. An index i is P-FREE if p does not divide i;
t*_eff = #{p-free i <= t}. p_i(S) = sum_{x in S} x^i.

t-NULL: p_i(S) = 0 for every p-free i <= t (equivalent to all
i <= t; equivalent to vanishing reversed-locator coefficients at
p-free indices <= min(t, |S|) — the banked dictionary; the free
indices are p-multiples, p = char).

Scales: 2-power divisors M | N; M_0 = 2^{floor log2 t};
M_t = 2 M_0 (least 2-power > t).

PRIMITIVE: S contains no full coset y*mu_M for any M > t
(dressing strip), AND S is not a union of mu_M-cosets for any
2-power 2 <= M <= M_0 (lift strip).

GUARDED ROW: (G1) Q^{t*_eff} >= 2^N (generated-field p-free
sub-balance); (G2) Q^41 <= N^256 (the aspect guard — proved
necessary by explicit counterexample); (G3) N = 2^s,
2^13 <= N <= 2^41, |F| < 2^256.

CENSUS: C_b = #{S subset D : |S| = b, t-null, primitive}. Sets,
counted once. (Disjoint unions of primitive t-null blocks are
themselves census members — closure is internal; no family
weighting is required.)

## The conjecture

At every guarded row:

    2 * sum_{b = t+16}^{N/2 - 1} C_b  +  C_{N/2}  <=  N^3 / 2.

(At N = 2^41: <= 2^122; equivalently half-band <= 2^121.)

## PROVE OR FALSIFY.

Pre-registered falsifier form (immutable): exact primitive weighted
censuses exceeding N^3/2 at 3+ strictly increasing scales, every
row guarded (G1-G3 verified per row, t*_eff computed p-free, Q at
the generated field). Above-balance rows, aspect-violating rows,
and raw (non-primitive) counts do not qualify.

Why the known falsifier families cannot reach it (each verified by
exact computation — audit Part 3): the char-7 tensor family crosses
super-budget only where it violates G2 (aspect 6.42+ vs 6.244; the
aspect-valid scale is sub-budget); the char-3 eta-block family
fails G1 (t*_eff = 2) AND G2; M_0/multi-level zero-sum lifts are
excluded by the lift strip and are separately paid (banked
boundary-scale column, <= 64 per row above the QA.25 crossover);
dressing amplification is excluded by the dressing strip (a single
mid-band primitive extra generates ~2^126 dressings — the reason
the census must be primitive); complements are handled by the
two-sided weighted form; near-tails are separately PROVED
(< 2^122 two-sided at the rate-1/2 row, replayed exactly).

What this supplies if proved: with the banked paid ledger (empty
bands, struct, boundary column, near-tails, complementation — all
PROVED or exactly counted), the live consumer's requirement
(#{non-coset-union t-null blocks + trade families} <= N^3) follows
by the assembly arithmetic (audit Part 1, table). The residual this
bounds is exactly the moving-sector anti-concentration content
(growing-order Myerson) — the prize floor's sole named open input.

Known scope caveat (honest): the single verbatim prize-max
instantiation is BLOCKED-ON an official pin of q = p^k — the
admissible sliver is log2 Q in [255.9113, 256), width 0.089 bits
(upstream's own r2 note: 'the prize band is underdetermined').
The conjecture as stated quantifies over all guarded rows and does
not depend on the pin.
