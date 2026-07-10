# The per-power Lam–Leung step for the deep-regime exactness theorem
# (discharges the write-up flag on satellite f2_deep_regime_exactness;
#  cycle 114, 2026-07-10)

CLAIM (the step the satellite flagged): for n = 2^s and T a subset of
Z/n (exponents of mu_n), if the cyclotomic integers M_i(T) =
sum_{e in T} zeta_n^{ie} vanish for ALL i <= j with j in {2, 3},
then T is a union of mu_4-cosets (mod-4 exponent classes) — i.e.
exactly the struct census. Consequently any non-struct T has some
M_i(T) != 0 (i <= j), which is what the norm/divisor argument needs.

PROOF (two Lam–Leung applications + one direct computation).

Step 1 (i = 1). M_1(T) = 0 is a vanishing 0/1-sum of n-th roots of
unity with n a 2-power. By Lam–Leung (prime-power case; for p = 2:
every vanishing N-combination of 2^s-th roots of unity is an
N-combination of antipodal pairs {zeta^e, zeta^{e + n/2}}), a 0/1
coefficient vector vanishes iff T is a disjoint union of antipodal
pairs {e, e + n/2}.

Step 2 (i = 2). Assume Step 1's conclusion; write T as a union of
pairs with representatives e_1, ..., e_r (mod n/2). Each pair
contributes zeta_n^{2e} + zeta_n^{2e + n} = 2 zeta_n^{2e}, so
  M_2(T) = 2 sum_t zeta_{n/2}^{e_t}   (as (n/2)-th roots, e_t mod n/2,
                                        each with coefficient 2;
                                        representatives are DISTINCT
                                        mod n/2 by disjointness).
M_2(T) = 0 is thus a vanishing 0/1-sum (after dividing by 2) of
(n/2)-th roots of unity, n/2 again a 2-power. Lam–Leung again: the
representatives form antipodal pairs mod n/2, i.e. pairs
{e, e + n/4} mod n/2. Pulling back: T is a union of quadruples
{e, e + n/4, e + n/2, e + 3n/4} = mu_4-cosets. This proves the
claim for j = 2.

Step 3 (i = 3 adds nothing). On a mu_4-coset {e + k n/4 : k = 0..3},
  M_3 = zeta_n^{3e} sum_k zeta_n^{3k n/4} = zeta_n^{3e} sum_k i^{3k}
      = 0,
since 3 is coprime to 4 so i^{3k} runs over all 4th roots of unity.
Hence M_3 vanishes automatically on every mu_4-coset union: the
j = 3 condition set has the SAME struct as j = 2 — which is exactly
the banked observation struct(j=2) = struct(j=3) = 2^{n/4}
(satellites 20/22) and the (113,16,j=3) autopsy's classification.
QED.

REMARKS. (a) The same induction extends to larger j: M_1 = ... =
M_j = 0 with j < 2^{v+1} forces mu_{2^{ceil(log2(j+1))}}-coset...
more precisely each further power-of-2 threshold crossed by j adds
one more descent; for the campaign's j <= 3 only two descents are
ever needed, as proved above. (b) Lam–Leung for prime-power order
is classical (Lam & Leung, J. Algebra 224 (2000); for p = 2 it is
also elementary: pair off zeta^e with -zeta^e = zeta^{e + n/2}).
(c) This note makes satellite f2_deep_regime_exactness's proof
chain complete at full rigor for j <= 3; the theorem's regime
caveat (deep regime only, not official rows) is unchanged.
