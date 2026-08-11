# Proof

At the boundary slack `(ADF2)`, the direct three-contact theorem gives a
nonzero section of

```text
O_C(d-3,ell-e+3-beta)=O_C(d-3,j).                     (1)
```

The restriction sequence is

```text
0 -> O(-3,j-e)
  -> O(d-3,j)
  -> O_C(d-3,j) -> 0.                                 (2)
```

Because `j<e`, both coordinates of the left bundle are negative. It has no
`H^0` or `H^1` by Kunneth. Hence restriction in `(2)` is an isomorphism on
global sections, proving the existence and uniqueness of the nonzero
ambient lift `A_j`.

Fix `x in D\S` and restrict the polynomial identity underlying `(ADF3)` to
that domain row. The factor `G(X)` vanishes at `x`, so in the parameter
polynomial ring

```text
q_x divides A_j(x;U,V)H(U,V).                         (3)
```

The form `H` is squarefree. Therefore, after writing

```text
q_x=g_xR_x,       H=g_xH_x,
```

one has `gcd(R_x,H_x)=1`: repeated supported roots of `q_x` remain in
`R_x`, while `H_x` contains no second copy. Euclid's lemma applied to `(3)`
gives `(ADF5)`.

The coefficient form `q_x` is nonzero and homogeneous of degree `e`. Since
`H` has one simple factor for every supported slope, `deg g_x` is exactly
the number `d_x` of distinct supported roots. Thus `deg R_x=c_x`.

If `c_x>j`, the degree-`j` form `A_j(x;U,V)` cannot contain `R_x` unless it
is zero. Consequently every one of its `j+1` coefficient polynomials in
`X` vanishes at `x`. Distinct heavy rows give distinct linear domain
factors, so their product `B_j` divides every coefficient and hence the
whole biform. Nonvanishing of `A_j` gives `deg B_j<=d-3`. Dividing by
`B_j` preserves `(ADF5)` on every row outside its root set and completes the
proof. QED.
