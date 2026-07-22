# Proof

The pairing map `P` has two output coordinates, so its rank `s` lies in
`{0,1,2}` and rank-nullity gives `dim K=r-s`. Since every row lies in
`W^perp`, membership in `K` is exactly augmented orthogonality. Pairing the
selected-error equation at slope `gamma_i` with `lambda_i` gives `(OQ2)`.

If `s=0`, there is nothing further to prove.

Suppose `s=1`, and write `im P=<v>` for a nonzero `v=(v_0,v_1)`. A row
outside `K` has image `alpha_i v`, `alpha_i!=0`, so `(OQ2)` forces

```text
v_0+gamma_i v_1=0.                                  (1)
```

There is at most one affine root. There must be at least one row outside
`K`, because the active rows span `L` and `P` is nonzero. Hence `v_1!=0`,
the root is an active slope, and exactly one active row lies outside `K`.

The other `t-1` coefficient-slope columns lie in `K tensor F^2`, of
dimension `2(r-1)`. They form a proper subset of the projective circuit and
are therefore independent. Thus

```text
t-1<=2(r-1),
```

which gives the upper bound in `(OQ3)`; the lower bound is the general
circuit bound.

Finally suppose `s=2`. Choose quotient coordinates identifying `P` with the
identity map from `L/K` to `F^2`. Equation `(OQ2)` says that the quotient
coefficient of row `i` is either zero or spans the one-dimensional
orthogonal complement of `(1,gamma_i)`. It therefore has the unique form
`(OQ4)` for a scalar `tau_i`. Appending its slope multiple gives `(OQ5)`.
Those four coordinates are linear combinations of

```text
1,       gamma_i,       gamma_i^2,
```

so their span has dimension at most three. Distinct nonzero quotient
directions are slope-distinct. This proves all three classes.

The construction is intrinsic: `K` is the kernel of the canonical pairing
map, while changes of bases only change quotient coordinates. It classifies
interaction but supplies no count of the augmented-orthogonal lifts. QED.
