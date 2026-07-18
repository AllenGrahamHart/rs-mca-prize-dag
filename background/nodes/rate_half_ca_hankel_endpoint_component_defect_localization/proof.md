# Proof

All factorization and incidence notation is over the algebraic closure of the
constant field.  The preceding component-profile theorem proves that every
factor has positive bidegree and every specialization used below is nonzero.

## 1. Squarefreeness and generic split fibers

Let `c_gamma` be the rank loss at a supported slope.  The endpoint charge
gives

```text
sum_gamma c_gamma<=m-1.
```

There are therefore at least

```text
T-(m-1)=3m+2                                            (1)
```

supported slopes with `c_gamma=0`.  At each one, the specialized generator
`Q_gamma` has `rho` distinct roots in `D` and degree exactly `rho`.

If an irreducible factor occurred at least twice in `Q`, specialize at any
slope counted by `(1)`.  Since the degree of the product remains
`rho=sum_i r_i`, every factor retains its full `X`-degree.  The repeated
factor would make `Q_gamma` nonsquarefree, a contradiction.  Thus `Q` is
geometrically squarefree.  At every slope in `(1)`, each distinct factor
`Q_i(gamma;X)` has `r_i` distinct roots in `D`, and roots belonging to
different factors are disjoint.  This proves item 1.

The endpoint norm theorem gives at least

```text
3m+1-O>=2m+2                                             (2)
```

supported slopes that are generic-rank, completely split, and
parameter-transverse at every root.  Since the component root sets are
disjoint there, transversality of `Q` is equivalent to transversality of the
unique component through the point.  This proves item 3.

## 2. Exact row and column ledgers

The component incidence sets have union equal to the zero set of `Q` on
`D x Z`.  Hence

```text
sum_i I_i=I+E,       E>=0.                              (3)
```

The root bounds in the two directions give

```text
I_i<=T*r_i,       I_i<=N*e_i,
```

so every `D_i` and `C_i` in `(CDL1)` is nonnegative.  Summing them and using
`sum r_i=rho`, `sum e_i=m`, and `I=T*rho-O` gives

```text
sum_i D_i
 =T*rho-(I+E)
 =O-E,                                                  (4)

sum_i C_i
 =N*m-(I+E)
 =16m^2-((4m+1)(4m-1)-O+E)
 =1+O-E.                                                (5)
```

These are `(CDL2)`.  Nonnegativity in `(4)` also proves `E<=O`.

For an individual component,

```text
C_i-D_i=N*e_i-T*r_i.                                   (6)
```

Write `b=m-e_*`.  For the dominant component,

```text
N*e_*-T*(4e_*-1)
 =16m e_*-(4m+1)(4e_*-1)
 =4b+1.                                                 (7)
```

For a balanced residual component,

```text
T*(4e_i)-N*e_i=4e_i.                                   (8)
```

Equations `(6)`--`(8)` prove `(CDL3)`.  Summing `(8)` over all residual
components and using `(4)` yields

```text
4b<=sum_(i!=i_*)D_i<=O-E,
```

which is `(CDL4)` and specializes immediately to `(CDL5)`.

## 3. Saturated domain fibers

The endpoint saturation theorem gives at least

```text
N-(1+O)>=15m                                            (9)
```

domain points `x` for which `Q(U,V;x)` has exactly `m` distinct roots, all
in `Z`.  Every component specialization is a nonzero homogeneous form of
degree `e_i`.  Since their product has `m=sum e_i` distinct roots, each
`Q_i(U,V;x)` has exactly `e_i` distinct roots in `Z`, and different
components have disjoint root sets.  This proves item 2 and completes the
proof.  QED.
