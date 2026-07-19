# H3 distance-six support-overlap payment

- **status:** PROVED
- **closure:** proof
- **consumer:** `f3_h3_mobius_excess_half`
- **dependencies:** `f3_h3_distance_four_fiber_degree_cap`,
  `f3_h3_antipodal_tail_distance_six_split`,
  `f3_h3_quotient_block_identity`

For a small generic representation `E={x,y}`, call the three distinct signed
half-basis atoms of

```text
v_E=+xy-x-y
```

its signed support. A distance-six edge is **disjoint** when both endpoints
are generic and their signed supports have disjoint underlying coordinates.
Every other distance-six edge is **overlapping**.

Inside any fixed nonzero product fiber:

1. there are at most six overlapping generic--generic distance-six edges;
2. if the fiber contains its unique antipodal representation, at most two
   distance-six edges are incident to it;
3. consequently the number `O_6(t)` of overlapping distance-six edges obeys

```text
O_6(t)<=6                 on an antipodal-free target,
O_6(t)<=8                 on an antipodal target.          (DSO1)
```

The generic overlap locus has two exact one-parameter covers. Up to endpoint
and internal root exchanges, every such edge is one of

```text
x=2u^2/(1+u^2),       y=-u,       v=-2u/(1+u^2),   (DSO2)
x=(1+y^2)/(2y^2),     u=xy,       v=-1/y.          (DSO3)
```

The corresponding target maps have degree three. This proves the constant
six in `(DSO1)` independently of the subgroup order.

For the `E=6` tail `P(t)>=25`, split the disjoint moment by target class:

```text
D_6,25^0=sum_(t antipodal-free) N_6^disj(t)R(t),
D_6,25^A=sum_(t antipodal)      N_6^disj(t)R(t),
Q_n=(n-1)(n-2).                                           (DSO4)
```

The exact quotient-mass ledger and `(DSO1)` give

```text
O_6,25^0+(17/10)O_6,25^A <=(68/5)Q_n.              (DSO5)
```

Consequently C36' follows from the disjoint-support estimate

```text
D_6,25^0+(17/10)D_6,25^A
 <=(750n^2-527Q_n)/20.                              (DSO6)
```

In particular, the simpler bound

```text
D_6,25^0+(17/10)D_6,25^A <=(223/20)n^2             (DSO7)
```

is sufficient. The remaining incidence has four free subgroup roots and two
membership tests, but now every retained distance-six edge has six disjoint
signed atoms. This theorem supplies no estimate for that disjoint incidence.
