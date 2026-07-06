# S5: the Lam–Leung / Conway–Jones transport — resolved (empty at n′ = 2^s)
# (round S5, self-tennis, 2026-07-07; whiteboard round, no compute needed)

The last untried proof-approach family on the singular core (suggested in
DLI-CLOSE-4 as route (ii)): transport the characteristic-zero
classification of vanishing sums of roots of unity to F_q, splitting
mod-q vanishers into (structured = char-0 relations) + (accidents =
sieve-counted remainder).

## The resolution

**Lam–Leung (1995):** the weight of any vanishing sum of n-th roots of
unity in characteristic zero lies in the numerical semigroup
N·p₁ + ... + N·p_k over the primes p_i | n; **Conway–Jones (1976):** such
sums decompose into rational combinations of full p-coset sums.

For our rows n′ = 2^s is a POWER OF TWO: the only prime is 2, so every
char-0 vanishing sum of n′-th roots of unity is a combination of antipodal
pairs x + (−x). In REDUCED form (exponents 0 ≤ e < N with z^N = −1,
i.e. working in Z[ζ_{2N}] with the integral power basis) antipodal pairs
do not exist — reduction eliminates them identically. Hence:

>  **The structured side of the transport is EMPTY at n′ = 2^s: there are
>  NO characteristic-zero vanishers in reduced form** (equivalently:
>  z^N + 1 is irreducible, so Norm(D) ≠ 0 for reduced ternary D ≠ 0 —
>  which is exactly Fact F2 of the S1 sieve).

So the transport's dichotomy degenerates: EVERY mod-q vanisher is an
"accident" (a norm-divisibility event), and the transport returns us to
the S1 norm-sieve with nothing added. The classification route does not
open the sieve-uncovered zone; it is not a fifth tool, it is the second
half of the first tool. (This is also WHY the section hypotheses (S1)/(S2)
of the pinned setting were load-bearing: antipodal pairs and full cosets
are precisely the Lam–Leung structured sums, and the section was designed
to exclude them — the design already consumed this theory.)

## Bookkeeping

Approach families consumed at the singular core, with outcomes:
1. First-moment norm sieve (S1) — PARTIAL: covers {L=1 full; L≤19 partial}.
2. Second moment / pair sieve (S1) — same family-size wall.
3. Analytic / higher moments (S2) — transfers between alphabets only.
4. Transference, both directions (S3/S4) — ultra-top only.
5. Structure classification / Lam–Leung transport (S5) — EMPTY at n′=2^s.

Attack families absorbed at the core: norm-engineering (round 5);
boundary-volume population (round 7 B1); multiplier/additive clusters
(rounds 6–7); dual-geometric (S3). All priced or killed.

The goal file's freezing criterion (≥ 3 distinct proof approaches AND
≥ 3 distinct attack families, all resisting) is met with margin. The core
qualifies for IRREDUCIBLE-CORE freezing as a named conjecture.
