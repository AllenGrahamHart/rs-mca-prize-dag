# Budget-three fiber-two c=2 one-antipodal minimum-support collision branch compiler

- **status:** PROVED
- **closure:** proof
- **consumer:** `rate_half_list_adjacent_crossing`
- **dependencies:**
  `rate_half_list_budget_three_fiber_two_cycle_c2_one_antipodal_minimum_support_barycentric_collision_router`,
  `rate_half_list_budget_three_fiber_two_cycle_c2_torsion_field_router`

Retain the exact one-pair minimum-support packet from `(BCR1)--(BCR5)` and
write `z=z_t`.  Define

```text
L(y,z)=y(z+12)-2z+8,
Q(y,z)=[y(z+12)-16]^2-64z.                           (BCB1)
```

The normalized completion curve has the exact factorization

```text
32z(z-36)^2-(3y-4)^2(3y+2)(z+12)^3
 =-27L(y,z)Q(y,z).                                   (BCB2)
```

Consequently every retained packet lies on one of only two branches:

```text
L branch: y(z+12)=2z-8,
Q branch: [y(z+12)-16]^2=64z.                        (BCB3)
```

The branches meet only at

```text
(y,z)=(0,4),       (y,z)=(4/3,36).                   (BCB3')
```

A disjoint implementation may assign both intersections to `L` and define
the second shard by `Q=0,L!=0`.

Here `z!=-12`.  Since the selected normalized denominator roots `1,t` are
base-field squares, choose `rho` in the base field with `rho^2=t` and put

```text
x=rho+rho^(-1),       z=x^2,       rho^(2N)=1.       (BCB4)
```

Changing `rho` to `-rho` changes only the sign of `x`.  Thus `(BCB3)` is
equivalently

```text
L branch: y(x^2+12)=2x^2-8,
Q branch: y(x^2+12)=16+epsilon 8x, epsilon in {+1,-1},
```

where the two signs on the `Q` branch are the same square-root orbit.  In
the selected ratio coordinate these become

```text
L: y(t^2+14t+1)=2(t-1)^2,
Q: [y(t^2+14t+1)-16t]^2=64t(1+t)^2.                 (BCB5)
```

There is also one exact split test.  Put

```text
kappa=-2alpha/(z+12).                                (BCB6)
```

On the retained separable one-pair normal form, both outer quadratics split
over the base field if and only if `kappa` is a nonzero square.  In
particular every complete candidate satisfies this square-class gate.  If
the selected denominator pair is the unique antipodal pair, then `z=0`, the
`L` branch is inseparable, and necessarily

```text
y=4/3,       s^2=4alpha/3,
12gamma=11alpha^2,       27beta^2=64alpha^3,
J=0,       -alpha/6 is a square.                     (BCB7)
```

In this shard `-2` is also a base-field square.

This compiler replaces the cubic invariant equation and two outer
discriminant tests by a two-branch union and one square class.  It does not
exclude either branch, evaluate the official coefficient gaps, or classify
larger barycentric support.
