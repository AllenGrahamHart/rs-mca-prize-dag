# Proof

Notation as in `statement.md`. Inputs consumed: MC-1/MC-2 (window
classification + ceiling: `P_T` agrees with `u` EXACTLY on `H \ T`,
nothing agrees on `>= k+w+1` points) and MC-3 (family membership) from
`xr_band_key_lemma_pencil_mass`; the banked locator factorization
mechanism (`background/nodes/e22_tail_coset_locator_algebra`); the
banked k-packing
(`background/nodes/xr_mismatch_chart_nongeneric_joint_support_equivalence/proof.md:19-22`).

## Claim 1 (THEOREM 5: diagonal at exactly `w`)

`T` and `T'` are unions of `m` distinct `mu_M`-cosets out of `N`;
distinct unions share at most `m - 1` cosets, each of size `M`, so
`|T ^ T'| <= (m-1) M = r' - M`. Then

```text
|(H\T) ^ (H\T')| = n - |T u T'| = n - 2r' + |T ^ T'|
                 <= n - 2r' + r' - M = k + w - M <= k    (w <= M).
```

On the shift pencil the `v`-side member is `Q_T = P_T / X^j` (well
defined since `X^{M-1} | P_T`, `j <= M-1`; division by `x^j` is
pointwise invertible on `H`), which agrees with `v = u/X^j` exactly
where `P_T` agrees with `u`, i.e. exactly on `H \ T`. Hence the joint
agreement of the cross pair `(P_T, Q_{T'})`, `T != T'`, is contained in
`(H\T) ^ (H\T')`, of size `<= k` — not a band pair. The diagonal pair
`(P_T, Q_T)` has joint agreement exactly `H \ T`, size `k + w`, depth
exactly `w`. QED (1)

*(The exactness of the per-member agreement — no accidental extra
points — is MC-2's ceiling; without it "diagonal at exactly `w`" would
read "at least `w`".)*

## Claim 2 (BP(1): structured => `d` a power of two)

Let the core complement `T` (`|T| = r'`, excess/depth `d = w`) be a
union of `mu_M`-cosets with `M = 2^ceil(log2 d)`. Cosets have size
`M`, so `M | r'`; also `M | n` (`mu_M <= mu_n` needs `M | n`), hence
`M | n - r' = k + d`. At the six-row shape `k` is a power of two and
`M = 2^ceil(log2 d) < 2d <= 2(h-2) < k` (exact integer check in the
verifier for all six rows), so `M | k` (two powers of two, the smaller
divides the larger), and therefore `M | d`. Since
`M = 2^ceil(log2 d) >= d` and `M | d` with `d >= 1`, this forces
`M = d`: `d` is a power of two.

The choice `M = 2^ceil(log2 d)` is not free: it is the
STRUCTURED-FLOOR COMPLETENESS input (MC-4 of the list-bound-transfer
record; iterated Lam-Leung, char 0, `n` a power of two): the
structured solutions of the vanishing window `e_1 = ... = e_{d-1} = 0`
at excess `d` are EXACTLY the `mu_{2^ceil(log2 d)}`-coset unions. The
verifier checks this census empirically at `(n,k,w,M) = (16,8,2,2)`,
`q = 65537` (window census = coset-union family, exactly); char-`p`
accidental extras outside the six-row shape are recorded in the
adjudication REPORT (caveat 3), and BP(3) below does not need
completeness — it excludes every coset union directly.

**Six-row consequence.** `h` is odd at all six rows. Powers of two in
`[ceil(h/2), h]`: `h - 1 = 2^s` is one; any other `2^t` in the window
would satisfy `2^t >= ceil(h/2) = 2^{s-1} + 1 > 2^{s-1}` and
`2^t <= h = 2^s + 1`, so `2^t = 2^s = h - 1`. Unique. Hence the band
proper's upper window `[ceil(h/2), h-2]` contains no structured depth,
and excess `h` (odd `> 1`) is not a power of two. QED (2)

## Claim 3 (BP(3): parity exclusion of the whole band proper)

On the shift class `v = u/X^j`, for any family pair at depth `d` the
per-point direction is `zeta_P(i) = -x_i^j` (the unique `z` with
`(u_i - f(x_i)) + z (v_i - g(x_i)) = 0` off the core: substituting
`v = u/x^j` and `g = f/x^j` pointwise gives
`(u_i - f(x_i)) (1 + z x_i^{-j}) = 0`). The fibre of `zeta_P` over a
slope value is a `mu_g`-coset intersected with the off-core set,
`g = gcd(j, n)`, and the off-core set `T` is a union of `mu_M`-cosets
with `g | M`, so each nonempty fibre inside `T` has size exactly `g`.
A forced ray therefore has agreement `(k + d) + g`, and it is live
(`= A = k + h`) iff `g = h - d`; `g < h - d` gives no live slope;
`g > h - d` breaks the tangent gate.

At the six rows `n` is a power of two, so `g = gcd(j, n)` is a power
of two. `h` is odd. By BP(1) a populated structured depth `d` is a
power of two: for `d >= 2`, `d` is even, so `h - d` is odd and `> 1`
(as `d <= h - 2`), while `g` is a power of two — `g = h - d` is
impossible. For `d = 1`, `M = d = 1` and the shift range
`1 <= j <= M - 1` is empty — no shift class exists at all. Hence no
coset construction is productive at ANY `d in [1, h-2]`:
`N_d^{coset} = 0`. QED (3)

*(Where the two arguments overlap — even `d` in the upper window —
BP(3) is strictly stronger than the occupancy-v2 count: it excludes
every band-proper depth including the low powers of two `d <
ceil(h/2)`, where BP(1) alone leaves `L_P = 0` to be checked
separately. This is the merge direction the occupancy-v2 REPORT
itself endorses (its section 6).)*

## Claim 4 (BP(2): confinement trichotomy, shift class)

The computation of Claim 3 gives the trichotomy directly. In the live
case `g = h - d` the forced slope at a point `i` is `z = -x_i^j`, so
the forced slope set satisfies `Gamma subset {-x^j : x in H}`, a set
of size `n/g = n/(h-d)`. Exclusivity is automatic: `g | j` and
`j >= 1` give `j >= g = h - d`, while `j <= M - 1 = d - 1`, so
`h - d <= d - 1`, i.e. `2d >= h + 1 > h` — the live shift class only
exists at high band depth, where `xr_two_slope_deficit_dichotomy`
THEOREM 2(b) says no ray of agreement `<= A` carries two depth-`d`
cores. Each live slope therefore serves at most one depth-`d` family
pair and `N_d <= |Gamma| / 2 <= n / (2(h-d))` — linear in `n`. The
`h`-even
control (`n = 20, t = 6, d = 4, j = 2`: `g = 2 = h - d`) realizes
live slopes inside `{-x^2 : x in H}`; the official rows are protected
by PARITY (Claim 3), not by the mechanism being impossible. QED (4)

## Claim 5 (cascade-tier population; the load-bearing definition)

At the prize rows `w = M` must divide `n` (a power of two) and satisfy
`w <= h - 1` with the family joint at depth `w`; by Claim 2's window
count the unique power of two in `[ceil(h/2), h-1]` is `h - 1`, so the
astronomically populated MC configuration sits AT the cascade tier
(`C(N,m)/N` members, `N = n/(h-1)`, `m = r'/(h-1)`). Two depth-`(h-1)`
cores inside one agreement set of size `A` would intersect in
`>= 2(A-1) - A = k + h - 2 >= k` points, violating the k-packing —
so under the SELECTED-support reading each live slope serves at most
one cascade-tier pair, `Sum_P L_P <= |Gamma| <= n`, and
`N_{h-1} <= n/2`. Under "any exact-`A` ray" the same family counts
`C(N,m)/N = 2^130`-`2^197` — definitions item 8's load-bearing
non-example, restated here because this node is where it bites. QED (5)

## Honest scope

Toy-verified: the diagonal quantization scans (two shapes here, five
in the pilot record, exhaustive by interpolation); the BP(2)/BP(3)
fixture battery (fresh replication of `exp_band_proper.py`'s S1-S4 at
`q = 41`). Exact at every scale: Claims 1-3 and the six-row window and
parity arithmetic. Char-0 input: MC-4 completeness (BP(1)'s floor
half), machine-checked empirically at one shape. Unproved and NOT
claimed: general-`v` emptiness (BP(2) scope), the quotient-convention
question (P3 formal firing), and any occupancy bound.
