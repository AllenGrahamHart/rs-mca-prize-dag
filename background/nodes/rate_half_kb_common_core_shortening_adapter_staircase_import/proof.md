# Proof (line-audited rendering of upstream Theorem 2.1 + walls)

## The adapter

Let `C`, `c`, `G_C`, `a_0`, `a_1` be as in the statement, `c < k` (source
theorem in the non-affine case; in every machine replay here `c < k` is
checked directly).

**Divisibility.** On `C`, `h_i = r_0 + gamma_i r_1` (since `C` lies in
every maximal support) and `a_j = r_j` (interpolation). So
`h_i - a_0 - gamma_i a_1` vanishes on all roots of the squarefree
`G_C`, and the quotient `h'_i` is a polynomial with
`deg h'_i < k - c`. Likewise any degree-`<k` explainer `p_j` of `r_j`
on a support containing `C` has `G_C | (p_j - a_j)`.

**Maximal supports.** For `x` off `C`, `G_C(x) != 0`, and dividing the
pointwise identity by `G_C(x)` is an equivalence; hence the shortened
maximal support is exactly `S_hat_i minus C`, and the containment
transport `(p_0,p_1) = (a_0 + G_C p'_0, a_1 + G_C p'_1)` is a bijection
between explaining pairs on `T` (with `C subset T`) and shortened
explaining pairs on `T minus C`. Noncontainment is therefore preserved
in both directions.

**Witness through the core.** Size-`m` subsets of `S_hat_i` containing
`C` form a connected exchange graph. Adjacent subsets share `m-1 >= k`
points, so if both are pair-contained their explaining pairs agree on
`>= k` points and are identical; containment would then propagate to
the union — all of `S_hat_i` — contradicting the assumed actual
noncontained witness inside `S_hat_i`. Hence some size-`m` subset
through `C` is noncontained, and its image is a size-`(m-c)`
noncontained witness in the shortened row.

**Parameters.** `(n', k', m') = (n-c, k-c, m-c)` gives
`m'-k' = m-k`, `n'-k' = n-k`, `n'-m' = n-m`, i.e. `(R+s, s, d+s)` with
`s = k-c`; and `3m-k+3 = (3m'-k'+3) + 2c` since each deleted point
contributes two to the two-cover sum.

**Converse.** Given a shortened record and `c` fresh evaluation points,
choose any `a_0, a_1` of degree `< c` and lift by the inverse formulas;
all correspondences pull back, so the compatible shortened staircase
embeds into common-core records.

## The walls (all replayed exactly in `verify.py` / `verify_audit.py`)

1. `ceil(32(m-c)/(n-c)) >= 18` iff `32(m-c) > 17(n-c)` iff
   `61952 > 15c`, so the last surviving core is `c = 4130` (slack 2)
   and `c = 4131` overshoots by 13. At `c = k-1`:
   `ceil(32*67473/1048577) = 3`.
2. `B_cell(s) = min{C(R+s,d+s), C(R+s,s+1)}`: the `s+1` branch is the
   minimum at `s <= 3`; exact values `549756338176`,
   `192154133857304576` (under `B_*`), `50372197381489643749376`
   (over `B_*` by `50371922400761532354289`).
3. `J_s = floor(prod_{i=0..s} (R+i)/(d+i))`: exact rational product;
   `J_13 = 47876303026096432 < B_* < J_14 = 743896698428332665`.
4. `C(n,4131) > B_* C(m,4131)` by exact integer comparison;
   `ceil(C(n,4131)/C(m,4131))` has bit length 3765 and 1134 decimal
   digits. Staging is futile:
   `C(n,c1) C(n-c1,c2) / (C(m,c1) C(m-c1,c2)) = C(n,c)/C(m,c)`
   exactly (both sides equal `C(n,c) C(c,c1) / (C(m,c) C(c,c1))`).
