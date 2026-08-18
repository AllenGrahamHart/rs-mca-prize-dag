# Proof

The quadratic survivor router and product-energy ledger give all listed
alternatives and identify the shifted branch with

```text
(x+tau)(y+tau)=kappa
```

on `H^2`, with at least 4370 disjoint two-cycles.

Assume for contradiction that `lambda=1`, so `kappa=tau^2`. Put
`u=x^(-1),v=y^(-1)`. The official domain is a multiplicative subgroup, so
coordinatewise inversion is a bijection of `H^2` and maps disjoint pairs to
disjoint pairs. The product-energy ledger gives the transformed equation

```text
u+v=-1/tau.                                           (1)
```

The constant `c=-1/tau` is a nonzero base-field element. Equation `(1)` is
the graph of the affine reflection `u -> c-u`; each transformed pair is one
split squarefree fiber of its fixed normalized quadratic pencil.

The complete official affine-reflection census bounds every such fixed
nonzero pencil by 1154 nonfixed fibers, equivalently at most 2308 nonfixed
graph points. This contradicts 4370 fibers, with margin

```text
4370-1154=3216.
```

Therefore `lambda!=1`. Every other parent alternative is retained verbatim,
so the displayed route is exhaustive. QED.
