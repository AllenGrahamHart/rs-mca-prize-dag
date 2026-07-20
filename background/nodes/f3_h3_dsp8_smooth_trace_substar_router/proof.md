# Proof

## Nodal degree

For a product representation `{x,y}` of `t`, its sum and product are

```text
x+y=1+xy-t,       xy=r.
```

Thus `r` determines the monic quadratic with roots `{x,y}`. Distinct generic
vertices have distinct parameters `r`.

For vertices `r,s`, the primitive shift-pair adapter gives decorated cubics
whose common trace and product are

```text
sigma_0=1+r+s-t,       product=rs.                 (1)
```

After the unique cube-root normalization, the product becomes one. The trace
curve router says that the normalized cubic is nodal exactly when its trace
has cube `27`. Cubing before division by the normalizing scale gives exactly

```text
(1+r+s-t)^3=27rs.                                  (2)
```

For fixed `t,r`, the left side minus the right side is

```text
(s+1+r-t)^3-27rs,
```

a degree-three polynomial in `s` with leading coefficient one. It therefore
has at most three roots in the official field. Since the vertex parameter is
injective, every vertex has at most three nodal neighbors. Restricting to
signed-disjoint distance-six edges can only decrease that degree.

## Pareto substars

The proved joint-star/depth compiler supplies product stars of degrees

```text
E=10,11:  (5,3),
E=12,13:  (6,4),
E=14,15:  (7,5),
E=16:     (8,6),                                 (3)
```

where each pair is `(antipodal-free, antipodal)`. At any chosen center, at
most three leaves in `(3)` are nodal by the preceding argument. Deleting
those leaves proves `(SSR2)`. At `E=16`, this leaves at least five and three
smooth leaves at the same centers as the degree-eight and degree-six stars.

## Saturation

Lift the center target and root products to the dyadic cyclotomic ring. At
the degree-one prime selected by an actual official survivor, all lifted
target values reduce to the common finite target `t`. Therefore `Delta_i` in
`(SSR3)` reduces to the left side of `(SSR1)` for that edge. A selected smooth
edge makes this residue nonzero, so `Delta_i` is not in the row prime.

Let `J` be the product-star candidate ideal and
`Delta=product_i Delta_i`. The actual row prime contains `J` and avoids
`Delta`. If `a Delta^k` lies in `J`, primality then forces `a` into the row
prime. Hence the saturation

```text
J:Delta^infinity
```

is still contained in every actual survivor prime. Saturating by the selected
smooth discriminants is therefore completeness-preserving. It supplies no
bound on the saturated ideal's norm or prime support. QED.
