# Proof

The source-row compiler gives, for the twelve distinct target labels
`alpha_i`,

```text
Res_T(A(T),H(T,X))
 = product_i H(alpha_i,X)
 = constant * B_source(X)^2.                      (1)
```

All divisors in (1) retain ramification multiplicity.

Consider first the quotient branch `W=0`, with local source coordinate
`u=X`.  A loop `{a,-a}` has product `-a^2`, so leading support and its
Vieta row give

```text
D(0)!=0,       E(0)=-a^2D(0).                     (2)
```

Substitute `T=a` and `T=-a` in `(KBPRM-1)`.  Their even parts start in
degree two by (2), while their linear terms are respectively
`aC(0)u` and `-aC(0)u`.  Since `aC(0)!=0`, both rows have exact order one.
For any other target label `t`, fixed-point-free target transport and
distinct signed target pairs give `t^2!=a^2`; hence

```text
H(t,0)=D(0)(t^2-a^2)!=0.                           (3)
```

The product on the left of (1) therefore has order exactly two.

The complete source fiber over a quotient branch is the ramified divisor
`2[u=0]`.  Thus `B_source` has order two there and the right side of (1)
has order four, contradiction.  At `W=infinity`, use the local coordinate
`u=1/X` and homogenize the bidegree-four source variable.  The local form
is again `(KBPRM-1)`, with the leading coefficients of `D,E,B_1`; the same
order-two versus order-four contradiction applies.

For any of the twelve complete fibers away from ramification, the positive
Vieta sum equation has nonzero source lift and `A_2`, so an antipodal star
forces `B_1=0`.  At ramification the local contradiction just proved makes
`B_1=0` necessary as well.  The parent proves that `B_1` is a nonzero
projective linear form, hence has one zero.  Distinct complete fibers have
distinct quotient labels, so at most one can be a loop.  This proves the
global form of `(KBPRM-4)`.

For completeness, apply it to the earlier common-loop census.  The parent
also proves that a two-loop packet uses at least one branch value and a
three-loop packet uses both branch values.  In a
two-loop packet with one ordinary loop, that ordinary loop consumes the
unique zero, so `B_1` is nonzero at the ramified loop.  With two ramified
loops, a linear form can vanish at at most one of them.  A three-loop packet
has one ordinary and both ramified loops, so `B_1` is nonzero at both
branches.  Every case contradicts the local result.  This proves
the two- and three-common-loop exclusions directly.  If there is one
common loop, the global cap forbids every outside loop; if there is no
common loop, at most one outside loop remains. QED.
