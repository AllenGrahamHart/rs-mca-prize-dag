# Proof

Notation as in `statement.md`: `RS_k` on `n` distinct points `x_i` of
`F_q`, `A = k + h`, `C_S` the shortened dual on `S`,
`G_z(W) = {(c, zc) : c in W}` with `G_{(0:1)}(W) = {(0, c) : c in W}`.

## Lemma L1 (MDS shortening)

`dim C_S = |S| - k` for `|S| >= k`, and
`dim (C_S ^ C_T) = max(0, |S ^ T| - k)`.

*Proof.* The evaluation-restriction map `F_q^S -> Hom(RS_k, F_q)`,
`c -> (f -> sum_{i in S} c_i f(x_i))`, has full rank `k` when
`|S| >= k` (Vandermonde on any `k` points of `S`), so its kernel `C_S`
has dimension `|S| - k`. A vector in `C_S ^ C_T` is supported in
`S ^ T` and orthogonal to `RS_k`, so `C_S ^ C_T = C_{S ^ T}`, of
dimension `|S ^ T| - k` when `|S ^ T| >= k`; if `|S ^ T| < k`, any
such vector is supported on `< k` points and orthogonality to `RS_k`
(which is `k`-wise independent, MDS) forces it to vanish. QED

*(Basis used by the verifier: `c^(t)_i = lam^S_i x_i^t`, `i in S`,
`t = 0..|S|-k-1`, with `lam^S_i = prod_{j in S, j != i} (x_i-x_j)^{-1}`
— the classical duality of generalized RS codes.)*

## Lemma 0 (fibre identity — graded-band-ledger pilot THEOREM 2)

If live slopes `z_1 != z_2` (both in `F_q` here; the `(0:1)` case is
symmetric with the roles of `u` and `v` exchanged) have
`|S_{z_1} ^ S_{z_2}| >= k`, then the forced codeword pair `P = (f,g)`
satisfies `S_{z_1} ^ S_{z_2} = Z_P` exactly.

*Proof.* Two-slope forcing on the core: on `S_{z_1} ^ S_{z_2}` (size
`>= k`) both `u + z_1 v = c_{z_1}` and `u + z_2 v = c_{z_2}` hold; the
`2 x 2` system with determinant `z_2 - z_1 != 0` inverts, so `u = f`,
`v = g` there with `f = (z_2 c_{z_1} - z_1 c_{z_2})/(z_2 - z_1)`,
`g = (c_{z_2} - c_{z_1})/(z_2 - z_1)`, both of degree `< k`, and
`c_{z_j} = f + z_j g` (degree-`< k` agreement on `>= k` points). Write
`e = u - f`, `e' = v - g`; then `S_{z_j} = Z_P u {i : e_i + z_j e'_i
= 0, i not in Z_P}`. If `i` lies in both supports off `Z_P`,
subtracting gives `(z_1 - z_2) e'_i = 0`, so `e'_i = 0`, then
`e_i = 0`, i.e. `i in Z_P` — contradiction. QED

*(Provenance: `notes/pilots_20260802/xr_graded_band_ledger/REPORT.md`
THEOREM 2, verified there at 0 violations across the whole battery;
re-verified here inside the realisation check. Minted inline because no
package of this wave carries it as a standalone claim — see
AUDIT_CHECKLIST flag B1.a.)*

## Claim 1 (exact per-datum cost `2h`)

Fix an admissible datum `(Z; z_1, S_1; z_2, S_2)`, `|Z| = k + d`,
`|S_j| = A = k + h`, `Z = S_1 ^ S_2`, `z_1 != z_2 in P^1(F_q)`.

**Step 1 — core rows are implied by ray rows.** For `c in C_Z`: since
`Z <= S_1` and `Z <= S_2`, `c in C_{S_1} ^ C_{S_2}` (L1), so both
`(c, z_1 c)` and `(c, z_2 c)` lie in the ray span; their difference is
`(0, (z_1 - z_2) c)`, giving `(0, c)`, then `(c, z_1 c) - z_1 (0, c) =
(c, 0)`. (If one slope is `(0:1)`, the rows `(0, c)` are present
directly and the same conclusion holds.) Hence
`C_Z x C_Z <= G_{z_1}(C_{S_1}) + G_{z_2}(C_{S_2})` and
`R(P) = G_{z_1}(C_{S_1}) + G_{z_2}(C_{S_2})`.

**Step 2 — the block-sum computation.** Suppose
`(c_1, z_1 c_1) + (c_2, z_2 c_2) = 0` with `c_j in C_{S_j}` (for
`(0:1)` read the corresponding column form; the argument is
identical). The first coordinate gives `c_2 = -c_1`, so `c_1` is
supported in `S_1 ^ S_2 = Z`, i.e. `c_1 in C_Z` (L1). The second
coordinate gives `(z_1 - z_2) c_1 = 0`, so `c_1 = 0`. The two ray
blocks are TRANSVERSE:

```text
dim R(P) = dim G_{z_1}(C_{S_1}) + dim G_{z_2}(C_{S_2}) = h + h = 2h,
```

using `dim G_z(C_S) = dim C_S = A - k = h` (L1). The bookkeeping form
`2d + (h-d) + (h-d)` is the same number split core-first. Independence
of `d` is manifest. QED (1)

## Claim 2 (free-slope codimension `2h - 2`)

Each prescribed slope pair gives a kernel of codimension exactly `2h`
(Claim 1). Two DISTINCT slope pairs `{z_1, z_2} != {z_1', z_2'}` have
distinct kernels: say `z_1' not in {z_1, z_2}`. Any `(u,v)` in both
kernels satisfies `(C1')`, i.e. `<c, u> + z_1' <c, v> = 0` for
`c in C_{S_1}`, as well as `(C1)`; subtracting,
`(z_1 - z_1') <c, v> = 0`, so `<c, v> = <c, u> = 0` for all
`c in C_{S_1}` — `h` fresh independent conditions relative to either
single kernel wherever `h >= 1`, so the joint rank strictly exceeds
`2h`. The union over the `~q^2/2` slope pairs of codimension-`2h`
subspaces, parametrized by the 2-dimensional slope choice, therefore
has codimension `2h - 2` (each kernel contributes a slice; no slice
contains another). The verifier witnesses both halves exactly: every
prescribed pair at the tiny shape has rank `2h`, and merged systems of
distinct pairs have rank `> 2h`. QED (2)

## Claim 3 (design ceiling, per-ray accounting of record)

`RS_k x RS_k` lies in the kernel of every condition row: for
`f, g in RS_k`, `<c, f> = 0` for `c in C_S` by definition of the dual,
and every row is of the form `(c, zc)`, `(c, 0)`, or `(0, c)` with
`c in C_S` for some `S`. A received pair realising the family
NON-degenerately means `(u,v) not in RS_k x RS_k` solves all rows, so
the kernel strictly contains `RS_k x RS_k`:
`2n - rank >= 2k + 1`, i.e.

```text
rank <= 2(n-k) - 1.
```

**Per-ray form.** By Claim 1 Step 1 the family row space equals the sum
of its ray blocks `G_{z_a}(C_{S_a})`, `a = 1..V` (core rows implied
whenever the core is carried by two rays of the family — the definition
of a two-slope family), so `rank <= sum_a dim C_{S_a} = V h` and
realisability forces `V h - dim Rel <= 2(n-k) - 1` with
`Rel = {(c_a) : sum_a c_a = 0, sum_a z_a c_a = 0}` the relation space.
A datum IS an unordered pair of rays sharing a core, so `M <= C(V,2)`.

**Per-datum form.** For a prescribed-slope family of `M` data with
total rank `2hM - delta` (Claim 1 gives `2h` per datum, `delta` the
family deficit): `2hM - delta <= 2(n-k) - 1` gives
`N_d = M <= (2(n-k)-1+delta)/(2h)`; with free slopes each datum's locus
has codimension `2h-2` (Claim 2) and the same argument gives
`/(2h-2)`. The deficit `delta` is NOT `0` in general — the sunflower
cycle has `delta = 2hM - Mh = Mh` (cost `h` per datum, the exact `2x`),
and `K_V` has `delta = 2h C(V,2) - Vh`. This is why the per-ray form is
the accounting of record (definitions item 11).

**Six-row arithmetic.** With `R = n - k` pinned at the six rows
(RowC `n = 1024`, `k = 256/128/64`, `h = 5/5/3`; prize `n = 2^41`,
`k = 2^39/2^38/2^37`, `h = 2^33+1/2^33+1/2^32+1`):
`floor((2R-1)/(2h))` = 153/179/319/191/223/479;
`floor((2R-1)/(2h-2))` = 191/223/479/191/223/479;
`floor((2R-1)/h)` = 307/358/639/383/447/959; and at the prize rows the
`d = 1` point budget `V* = floor((R+1)/(h-1)) = 192/224/480` gives
`C(V*,2) = 18336/24976/114960`. All recomputed as exact integers by the
verifier. QED (3)

## Honest scope

Claims 1-3 are interpolation/linear algebra, valid at every scale. What
is toy-verified only: end-to-end admissibility of realized data under
the full gate (the verifier realises one datum at `(16,4,4,97)` and
scans it exhaustively), and every empirical statement quoted from the
pilot record (rank measurements at 20 (shape, depth) points, 59/59
realisations, the K_V fixtures 104/104). The pilot's growth laws,
first-moment figures, and the sunflower's realized-law calibration
(`383/447/959`, ratio 1.00000 against `floor((2(n-k)-1)/(h-1))`) are
RECORDED context, not claims of this node.
