# A1-PROD: the production norm-sieve theorem (round S1, self-tennis, 2026-07-07)

**STATUS: PROVED** (elementary, self-contained below; every constant computed
by exact integer arithmetic in `a1_prod_norm_sieve_verifier.py`, ALL PASS;
table banked in `a1_prod_norm_sieve_table.json`). The density corollary
additionally uses the standard prime-count-in-APs input (AP), stated
explicitly. The theorem's LIMITS are computed exactly and stated at the end
— they are the round's structural discovery, not fine print.

## Setting

Level = (n′ = 2N a power of two, L ≥ 1). Admissible prime: q ≡ 1 (mod n′),
Q ≤ q < 2Q. Pinned embedding ω of ζ = ζ_{n′}; section x_y = ω^y, 0 ≤ y < N.
For d ∈ Z^N write D(t) = Σ_y d_y t^y ∈ Z[t]/(t^N + 1) ≅ Z[ζ]. The kernel
lattice is K_q = {d : D(ω^{2l−1}) ≡ 0 (mod q), l = 1..L}. The excess ledger
consumes, for the chosen coverage weight w_cov ≤ w*(q, L),

>  W_cov(q) = Σ over reduced ternary d ∈ K_q with L+1 ≤ w(d) ≤ w_cov of 2^−w(d).

(Weights < L+1 carry no kernel vectors — the proved Vandermonde floor.)

## Theorem (unconditional count form)

Let D_cap(w) = max{m ≥ 0 : Q^{Lm} ≤ w^N} and
TOTAL(w_cov) = Σ_{w=L+1}^{w_cov} C(N, w) · D_cap(w). Then for every T > 0:

>  #{q ∈ [Q, 2Q), q ≡ 1 (mod n′) : W_cov(q) ≥ T} ≤ TOTAL(w_cov) / T.

### Proof

**(F1) Kernel membership forces q^L | Norm(D).** Since q ≡ 1 (mod n′), q
splits completely in Q(ζ); the primes above q are P_a = ker(Z[ζ] → F_q,
ζ ↦ ω^a) for a ∈ (Z/n′)^×, pairwise distinct because ω has exact order n′.
The L kernel conditions say D ∈ P_{2l−1} for l = 1..L — L DISTINCT maximal
ideals (2l−1 are distinct units mod n′ for L ≤ N). Distinct maximal ideals
are coprime, so (D) ⊆ P_1 P_3 ··· P_{2L−1}, and taking ideal norms
(N(P_a) = q by complete splitting): q^L | |Norm(D)|.

**(F2) Norm size and nonvanishing.** t^N + 1 is irreducible over Q (n′ a
power of two), so Z[ζ] is a domain and any nonzero reduced ternary d (degree
< N, not all coefficients 0) has D ≠ 0, hence Norm(D) ≠ 0. Every archimedean
conjugate is a sum of w(d) roots of unity, so |Norm(D)| ≤ w^N.

**(F3) Per-element band cap.** If q_1 < ··· < q_m are distinct primes of the
band with d ∈ K_{q_i}, their prime-ideal sets are disjoint (different
residue characteristics), so q_1^L···q_m^L ≤ |Norm(D)| ≤ w^N, forcing
Q^{Lm} ≤ w^N, i.e. m ≤ D_cap(w).

**(F4) Weighted Markov.** Σ_{q ∈ band} W_cov(q) =
Σ_{d ternary, L+1 ≤ w ≤ w_cov} 2^−w · #{q : d ∈ K_q} ≤
Σ_w [C(N,w)·2^w] · 2^−w · D_cap(w) = TOTAL(w_cov). The count claim is
Markov's inequality. ∎

## Corollary (density form; uses input AP)

**(AP)** #{q ∈ [Q, 2Q) : q ≡ 1 (mod n′)} ≥ Q / (2·φ(n′)·ln 2Q) — the
standard prime-count-in-progressions lower bound, comfortably explicit in
our range (modulus n′ ≤ 2^14 ≪ any power saving; the factor 2 is a crude
safety margin).

Then the density of admissible q in the band with W_cov(q) ≥ T is at most
TOTAL(w_cov) · 2·φ(n′)·ln(2Q) / (T·Q).

## Exact production instantiation (Q = 2^255, N = 256L, T = 1)

Computed exactly (no floating logs on decision paths); X = achieved
exceptional-density exponent (density ≤ 2^−X). Full 34-level table in
`a1_prod_norm_sieve_table.json`; the shape:

| L | w*(L) (exact) | covered w_1 | fraction of window | X |
|---|---|---|---|---|
| 1 | 55 | **55 (FULL)** | 1.00 | **47.6** |
| 2 | 113 | 39 | 0.33 | 40.1 |
| 3 | 171 | 33 | 0.18 | 42.0 |
| 5 | 287 | 28 | 0.08 | 43.5 |
| 10 | 576 | 24 | 0.025 | 40.7 |
| 19 | 1096 | 21 | 0.002 | 40.6 |
| **20–34** | 1154–1963 | **none** | 0 | — |

Threshold trade-off is linear in the exponent: the same table at threshold
T = 2^−s has X(T) = X(1) − s. E.g. T = 2^−5 keeps X ≥ 35 everywhere covered
while capping each covered level's aggregate cost at log2(1 + r·2^−5) ≤
0.045 bits; the union over the 19 covered levels costs ≤ 0.86 bits of
aggregate against a combined exceptional density ≤ 19·2^−35 ≤ 2^−30.7.

**Correction to the pinned file:** the round-1 estimate w* ≈ 68L is wrong;
exact w*(L) ≈ 57.7L − 2 (L=1: 55, not 68). Nothing banked depended on the
estimate (w* only positions the ledger/tail split); recorded here and in the
round log.

## What the theorem does NOT cover (the discovery — the new zone-(b) residue)

The uncovered region is EXACTLY
{(L, w) : 2 ≤ L ≤ 19, w_1(L) < w ≤ w*(L)} ∪ {(L, w) : L ≥ 20, L+1 ≤ w ≤ w*(L)}.

The obstruction is fundamental to first-moment counting, not slack in the
argument: the weighted family size Σ_{w ≤ w_cov} C(N, w) must stay below the
number of primes in the band (≈ 2^237.5) for Markov to say anything, and at
L ≥ 20 even the MINIMAL window w = L+1 has C(256L, L+1) > 2^194. A second
moment does not help: pair incidences are capped by the same norm-capacity
argument and the family size enters squared. Within this tool class the wall
is real. Consequences:

1. Deep levels (L ≥ 20) retain only their conjectural status from zone (b) —
   but their LEDGER exposure is exponentially discounted (a level-L orbit
   costs ≤ 256L·2^−L; to cost one bit at L = 34 a single prime would need
   ≥ 2^25 independent minimal-weight orbits, a stack of ~2^25 simultaneous
   q^34-norm-divisibility events).
2. The analytic route (A2 / R-bound: per-λ log-sum with the one-bit margin)
   is now the ONLY known tool whose reach covers the entire uncovered zone —
   it subsumes middle bands, deep levels, and the tail at once. A2 is
   therefore promoted from co-equal leaf to THE load-bearing leaf.
3. Refutation guidance (both chairs): any attack on the covered zone must
   beat exact integer arithmetic (hopeless); attacks belong in the uncovered
   zone, specifically engineered deep-level multi-orbit stacks — priced
   above as multi-fold norm coincidences.

## Verifier

`a1_prod_norm_sieve_verifier.py` — ALL PASS: exact w*/w_1/X table; toy
instantiation (n′ = 64 band) dominates the observed census incidences;
per-element cap attack (exact resultant norms of all four round-7 B1
generators factored: each hits exactly one band prime, cap 4 never
approached); norm-divisibility replay of the B1 row.
