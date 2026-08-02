# Proof

Throughout `n = 2^s >= 4`, `h = phi(n) = n/2`, `Phi_n(x) = x^h + 1`,
`Z[zeta_n] = Z[x]/(x^h+1)`, and `q` is an odd prime with `n | q - 1` and
`zeta in F_q^*` of exact order `n`. All coefficient vectors are supported in
the basis range `0 <= i < h`, so that `alpha = sum_i a_i zeta_n^i` with
`a_i in Z` and `alpha = 0` iff all `a_i = 0` (the `zeta_n^i`, `i < h`, are a
`Z`-basis of `Z[x]/(x^h+1)`).

## Claim 1 (LN0: splitting)

**The `h` roots.** `zeta` has exact order `n = 2h`, so `zeta^h = -1` (it is a
square root of `1` different from `1`). For `j` odd,
`(zeta^j)^h = (zeta^h)^j = (-1)^j = -1`, so each `zeta^j` is a root of
`x^h + 1` in `F_q`. They are pairwise distinct: `zeta^j = zeta^{j'}` forces
`j == j' (mod n)`, and the `h` odd residues mod `n` are distinct. A monic
degree-`h` polynomial with `h` distinct roots splits:

```text
x^h + 1 = prod_{j odd mod n} (x - zeta^j)   in F_q[x].          (LN0-1)
```

**The primes.** Reducing `Z[zeta_n] = Z[x]/(x^h+1)` mod `q` and applying the
Chinese Remainder Theorem to `(LN0-1)` (the factors are pairwise coprime,
being distinct monic linear polynomials),

```text
Z[zeta_n]/(q) = F_q[x]/(x^h+1) ~ prod_{j odd mod n} F_q,        (LN0-2)
```

the `j`-th projection being `pi_j : Z[zeta_n] -> F_q`, `zeta_n -> zeta^j`.
Each `pi_j` is a surjective ring map onto a field, so `p_j := ker(pi_j)` is a
maximal ideal with residue field `F_q`, i.e. of absolute norm `q`; `(LN0-2)`
is a product of `h` DISTINCT such ideals, so `q` is unramified and
`(q) = prod_{j odd} p_j` with exactly `h = [Q(zeta_n):Q]` factors. (`Z[zeta_n]`
is the full ring of integers of `Q(zeta_n)` — classical for cyclotomic fields —
but nothing below needs that: every argument uses only `(LN0-1)`/`(LN0-2)` and
the `q`-adic factorization of Claim 4.)

**Galois.** For `a in (Z/n)^*` let `sigma_a(zeta_n) = zeta_n^a`. Then
`pi_j(sigma_a(zeta_n)) = zeta^{ja} = pi_{ja}(zeta_n)`, so `pi_j o sigma_a = pi_{ja}`
and `sigma_a^{-1}(p_j) = p_{ja}`. The map `(a, j) -> ja` on odd residues mod `n`
is simply transitive — for fixed odd `j, j'` the congruence `a j == j' (mod n)`
has the unique odd solution `a = j' j^{-1}` — so `Gal` permutes `{p_j}` simply
transitively. QED (1).

*Ramification caveat.* Distinctness of the `h` factors in `(LN0-1)` is exactly
"`q` is unramified", which here comes free from `q` odd and `n` a power of two
(the only ramified prime of `Q(zeta_{2^s})` is `2`). Residue degree `1` — hence
norm exactly `q` per prime, which is what makes Claim 3 read `q^o` — is exactly
`n | q - 1`. Both hypotheses are used; neither is decorative.

## Claim 4 (LN3: evaluation form) — proved first, it is the engine

**(a) The reduction identity.** `Norm(alpha)` is the determinant of
multiplication by `alpha` on the free `Z`-module `Z[zeta_n]`; determinants
commute with the ring map `Z -> F_q`, so `Norm(alpha) mod q` is the
determinant of multiplication by `alpha mod q` on `F_q[x]/(x^h+1)`. Under the
isomorphism `(LN0-2)` that operator is DIAGONAL with entries `alpha(zeta^j)`,
`j` odd. Hence

```text
Norm(alpha) == prod_{j odd mod n} alpha(zeta^j)   (mod q),      (LN3-1)
```

and `q | Norm(alpha)` iff some factor vanishes, i.e. iff `m(alpha) >= 1`.

**(b) The valuation bound.** Work in `Z_q` (the `q`-adic integers). By
`(LN0-1)` the reduction of `x^h + 1` has `h` simple roots in `F_q`, so by
Hensel's lemma each lifts uniquely: there are `r_j in Z_q` with
`r_j == zeta^j (mod q)` and

```text
x^h + 1 = prod_{j odd mod n} (x - r_j)   in Z_q[x].             (LN3-2)
```

`Norm(alpha) = prod_j alpha(r_j)` (the resultant/norm formula is a polynomial
identity in the coefficients, so it may be read in `Z_q`). For each
`j in Z(alpha)` we have `alpha(r_j) == alpha(zeta^j) == 0 (mod q)`, i.e.
`q | alpha(r_j)` in `Z_q`. Multiplying the `m(alpha)` such factors,

```text
v_q(Norm(alpha)) >= m(alpha).                                    (LN3-3)
```

QED (4).

## Claim 2 (LN1: forward gate)

Let `G subset [0,h)`, `eps in {+-1}^G`, `alpha = sum_{i in G} eps_i zeta_n^i`,
and suppose `alpha(zeta) = 0` in `F_q`.

*Nonvanishing.* The `zeta_n^i`, `0 <= i < h`, are a `Z`-basis, and the
coefficients `eps_i` are `+-1 != 0`, so `alpha != 0` in `Z[zeta_n]`. `Q(zeta_n)`
is a field, so multiplication by `alpha` is invertible and
`Norm(alpha) != 0`. (Equivalently: `x^h+1 = Phi_n` is irreducible over `Q` and
`deg alpha < h`, so no `alpha(zeta_n^j)` vanishes.)

*Divisibility.* `1` is an odd residue, so `1 in Z(alpha)` and `m(alpha) >= 1`;
by `(LN3-1)` (or `(LN3-3)`), `q | Norm(alpha)`. QED (2).

*Structural restatement.* `alpha(zeta) = 0` says exactly `alpha in p_1`, hence
`p_1 | (alpha)` and `q = N(p_1)` divides `|Norm(alpha)| = N((alpha))`.

*Why the basis range is load-bearing.* If `G` is allowed to meet an opposite
pair `{i, i+h}` then the formal signed sum need not be a nonzero element:
`zeta_n^{i+h} = -zeta_n^i`, so e.g. `zeta_n^0 + zeta_n^h = 0`, whose
"evaluations" all vanish and whose norm is `0`. The conclusion
"`q | Norm(alpha) != 0`" then carries no arithmetic information. This is the
banked C1 reduced-signed-support ("no opposite pairs") clause; in the DLI tower
the junction-`j` index range is `0 <= i < h_{j+1} = phi(h_j)`, so the
hypothesis holds by construction, and it is THE clause that a future seam edit
folding cells onto opposite pairs would break.

## Claim 3 (LN2: `o`-fold upgrade)

Let `U` be a set of `o` odd residues mod `n` and suppose `alpha(zeta^u) = 0`
for every `u in U`, with `alpha != 0` supported in `[0,h)`. Then
`U subset Z(alpha)`, so `m(alpha) >= o`, and `(LN3-3)` gives

```text
v_q(Norm(alpha)) >= o,   i.e.   q^o | Norm(alpha),   Norm(alpha) != 0.
```

QED (3).

*Second, independent proof (the ideal-theoretic one, which is where "simple
transitivity" is the operative fact).* `alpha(zeta^u) = 0` says
`alpha in ker(pi_u) = p_u`. By Claim 1 the ideals `p_u`, `u in U`, are
**pairwise distinct** maximal ideals — this is precisely simple transitivity of
the Galois action, `p_u = sigma_u^{-1}(p_1)` with `u -> sigma_u` injective.
Distinct maximal ideals are comaximal, so
`prod_{u in U} p_u = intersection_{u in U} p_u` contains `(alpha)`, hence
divides it, hence `N(prod_u p_u) = q^o` divides `|Norm(alpha)|`.

*Official instantiation.* At junction `j` the block is
`U_j = {odd u : u * 2^j <= t}` acting on the order-`h_j` root, `|U_j| = L_j`,
and the skew element `delta = sum_{i < h_{j+1}} d_i zeta_{h_j}^i` is supported
in the basis range `[0, phi(h_j))`. So every nonzero junction-`j` skew solution
satisfies `q^{L_j} | Norm(delta) != 0`. QED.

## Remark (what the three claims are for)

`(LN3-1)` turns a norm-divisibility measurement into `h` modular evaluations
(the form used by every scan in the provenance pilot, cross-checked against
fraction-free Bareiss determinants and `sympy.resultant`). Claims 2-3 supply
the LOWER bound `q^{L_j} <= Norm` in the junction router; the matching UPPER
bound `Norm <= E^{phi(h_j)/2}` is proved separately in
`dli_norm_gate_energy_ceiling`, and the two together are the router that kills
states (`dli_official_support_forcing`).
