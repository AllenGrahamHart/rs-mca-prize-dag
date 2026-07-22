# Budget-three fiber-two c=2 one-antipodal reciprocal affine collapse

- **status:** PROVED
- **closure:** proof
- **consumer:** `rate_half_list_adjacent_crossing`
- **dependencies:**
  `rate_half_list_budget_three_fiber_two_cycle_c2_one_antipodal_degree_defect_global_gate_router`,
  `rate_half_list_budget_three_fiber_two_cycle_c2_torsion_field_router`

Retain a maximal-degree one-antipodal `c=2` collision packet for which the
selected denominator pair is the unique antipodal pair. Work in the
reciprocal quadratic-field chamber

```text
q=p^2,       N=2^40,       p=-1 mod N.                 (RAC1)
```

The global affine gate supplies

```text
a^2=-2,       y!=1,
u=A_a(y)=(a+2)y-(a+1),
v=B_a(y)=(a-1)y+(2-a),
y,u,v in mu_N.                                        (RAC2)
```

Then this three-affine-image intersection has only one possible point:

```text
y=(7+4a)/9,
u=r=(2a-1)/3,
v=-r,       y=-r^2.                                   (RAC3)
```

In particular, the packet necessarily satisfies the fixed-element torsion
test

```text
r^N=1.                                                (RAC4)
```

This test is prime-field scalar. Define

```text
R_0=-2/3,
R_(j+1)=R_j^2-2,       0<=j<40.                       (RAC5)
```

Then `(RAC4)` is equivalent to

```text
R_40=2 mod p.                                         (RAC6)
```

On the maximal budget-three row the complete reciprocal candidate ledger is

```text
3*2^128<=p^2<2^130,
p=k*2^40-1,
29058991<=k<=33554432.                                (RAC7)
```

Thus there are exactly `4,495,442` progression values before primality and
the forty-squaring test. This replaces the all-field `2^29` affine candidate
cap by one fixed torsion value per reciprocal official field.

A preregistered 16-shard exact screen evaluated `(RAC5)` at every progression
modulus in `(RAC7)`, including composites. It returned

```text
processed=expected=4,495,442,
coverage_exact=true,       all_complete=true,
hits=[].                                                (RAC8)
```

Every official reciprocal characteristic is among the tested non-factor-
three moduli. Therefore no maximal-degree selected-antipodal collision packet
exists in the reciprocal quadratic-field chamber.

The theorem does not reconstruct the scale `tau` or check source-product,
Euler, canonical, or gap conditions because the earlier torsion gate already
rejects the shard. It does not cover the fixed-field chambers,
degree-deficient packets, or a collision packet whose selected denominator
pair is not the antipodal pair.
