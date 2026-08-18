# Proof

The group `H` is cyclic of even order `N`, so `-1` belongs to `H` and the
square subgroup `H^2` has index two.

For the antipodal map, `x=-x` would imply `x=0`, impossible in `H`. Hence all
`N` elements form `N/2` two-cycles. The orbit of `x` has locator

```text
(X-x)(X+x)=X^2-x^2.
```

As `x` ranges over `H`, `x^2` ranges over `H^2` with two preimages. Thus the
orbits are exactly the fibers of `X^2-y`, one for each `y in H^2`. This is the
degree-two cyclic power-map construction in the quotient-periodic fence.

Now fix `kappa in H`. The map `iota(x)=kappa/x` is an involution of `H`. Its
fixed points satisfy `x^2=kappa`. There are no such points when `kappa` is a
nonsquare in `H`, and exactly two when it is a square. Removing fixed points,
the remaining elements form respectively

```text
N/2       or       (N-2)/2
```

two-cycles. One orbit `{x,kappa/x}` has locator

```text
(X-x)(X-kappa/x)=X^2-(x+kappa/x)X+kappa.            (1)
```

These are members of the pencil `u+gamma v` with

```text
u=X^2+kappa,       v=X,       gamma=-(x+kappa/x).
```

If two nonfixed orbits have the same sum, their common product `kappa` and
common sum determine the same monic quadratic `(1)`, hence the same unordered
root pair. Distinct orbits therefore give distinct slopes and disjoint split
squarefree locators. For nonsquare `kappa` this is exactly the degree-two
dihedral construction; the same calculation supplies its square-`kappa`
boundary after the two repeated-root fibers are deleted.

At `N=2097152`, the smaller count is

```text
(N-2)/2=1048575,
1048575-4370=1044205.
```

Both quotient classes therefore survive every local cap below 4370. The
quadratic router and reciprocal-affine elimination leave only general shifted
inversion as a pointwise-cap candidate. Identification is not a chronology or
factor-owner payment, so the quotient classes remain explicit. QED.
