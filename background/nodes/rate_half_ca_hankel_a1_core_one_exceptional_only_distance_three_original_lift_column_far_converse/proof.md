# Proof

Let `q_j(z)` be the coefficients of `Q`. If `p(z;X)=(X-s)Q(z;X)`, then for
every admissible row index,

```text
sum_j p_j(z)y_(i+j)
 =sum_j q_j(z)(y_(i+j+1)-s y_(i+j))
 =sum_j q_j(z)h_(i+j)=0.                              (1)
```

The final equality is the contracted Hankel converse. This proves the lift
and annihilation assertions. Splitness and degrees follow from the exact
internal/external fibers and the disjoint fixed core. Padding the exceptional
fiber proves closeness at all `4e+1` slopes.

It remains to prove column-farness. Suppose a squarefree degree-`rho=r+1`
domain locator `Lambda` annihilated both lifted endpoints.

If `Lambda(s)=0`, write

```text
Lambda=(X-s)L,       deg L=r.                         (2)
```

Contracting the lifted recurrences shows that `L` annihilates both
contracted endpoints. Hence it annihilates every contracted slope. At any
external slope, both `L` and `G_z` give source representations on at most
`r` points. Their union has at most `2r` points, inside the `2r+1`-column
Vandermonde independence range. The two representations must coincide, so
the root set of every external `G_z` is the fixed root set of `L`. This is
impossible because the external locators have union of size `6e+3>r`.

Now suppose `Lambda(s)!=0`. The lifted endpoint representation on the
`r+1` roots of `Lambda` contracts to a representation of each `h_ell` on
the same root set; multiplication of each source weight by `x-s` preserves
nonzero weights because the core is absent. Thus every contracted slope has
a representation on this fixed `(r+1)`-set `U`.

At an external slope it also has the nonzero `r`-point representation on
`G_z`. The union `U union G_z` has at most

```text
(r+1)+r=2r+1                                         (3)
```

points. The available moment columns through degree `2r` are independent on
every such set, so the representations coincide and `G_z` is a subset of
`U`. This would place the union of all external locators, of size `6e+3`,
inside the `r+1=2e+2` points of `U`, again impossible. This proves `(OLC4)`
for every lift scalar pair.

Finally `rho=r+1=2e+2`, and `(OLC5)` is equivalent to `2e-2>0`. The official
value of `e` is much larger than one. The preceding routers prove the reverse
reduction from any distance-three counterexample to the exact design, so the
claimed equivalence follows. QED.
