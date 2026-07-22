# Proof

Assume first that `C_q` is MDS. Choose any information set and put a generator
in systematic form

```text
G=[I_e | B].                                         (1)
```

The MDS property says that `B` is invertible and every entry in `B` is
nonzero. Let `c_1,...,c_e` be the rows of `G`. The `e` squares

```text
c_i*c_i       (1<=i<=e)                              (2)
```

are independent because their first `e` coordinates are the standard basis.
The `e-1` products

```text
c_1*c_j       (2<=j<=e)                              (3)
```

vanish in those first coordinates. On the last `e` coordinates they are the
coordinatewise products of the nonzero first row of `B` with rows
`2,...,e`. Multiplication by that nonzero diagonal row is invertible, and
those `e-1` rows are independent because `B` is invertible. Hence the
products in `(2)--(3)` are `2e-1` independent elements of `U_q^2`.

The Forney-residue theorem gives the opposite bound
`dim U_q^2<=2e-1`, proving `(HMR1)`. Its codimension-one clause then makes
the Forney residue class unique up to scalar.

If the code is not MDS, some maximal minor `Delta_I` vanishes. The weighted
self-dual complementary-minor law is

```text
Delta_J^2 product_J beta=(-1)^e Delta_I^2 product_I beta.
```

All weights are nonzero, so `Delta_J=0` as well. This is `(HMR2)` and
completes the exhaustive router. QED.
