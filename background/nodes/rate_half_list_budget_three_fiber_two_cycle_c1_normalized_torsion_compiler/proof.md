# Proof

The four roots of `D_*` lie in `mu_N`, so
`lambda=A^(-1)` also lies in `mu_N`. The canonical-span covariance
therefore preserves the primary gap, secondary gap, span identity, and
split/Mobius verdict after replacing every denominator root by its product
with `lambda`. It gives `(C1N1)--(C1N2)`; the invariant exponents follow
directly from

```text
I=alpha^2+12gamma,
J=72alpha gamma-27beta^2-2alpha^3.                   (1)
```

Scaling the source square variables by `A^(-1)` sends its binary-quartic
invariants to

```text
I_1'=A^(-2)I_1,       J_1'=A^(-3)J_1.                (2)
```

Each lift-sign invariant equation
`I^3J_1^2-J^2I_1^3` is consequently multiplied by
`A^(-(12h+6))). The radical-free norm is the product of its two conjugate
lift-sign equations, so it is multiplied by
`A^(-(24h+12))`. Substitution of `A=1,B=b,D=d` in `(MTR6)` gives
exactly `(C1N3)`, proving `(C1N4)`.

For the torsion assertion, let

```text
T_j=b^(2^j)+d^(2^j),       P_j=(bd)^(2^j).            (3)
```

The initial values are `S,P`, and squaring `T_j` proves the two
recurrences in `(C1N5)`. The recurrence for `c_j` is immediate. Thus
`b^N=d^N=c^N=1` implies the three terminal equations.

Conversely, put `x=b^N` and `y=d^N`. The first two terminal equations
give

```text
x+y=2,       xy=1.
```

Hence `x,y` are both roots of `Z^2-2Z+1=(Z-1)^2), so
`x=y=1`. The third terminal equation gives `c^N=1`. This proves
`(C1N6)`.

The factors in `(C1N7)` respectively enforce nonzero pair product,
nonzero unused root, `c!=1`, neither pair root equal to one, `c` not a
pair root, and distinct pair roots. The separate split and square conditions
are inherited from the cycle router.

Every original passing packet can therefore be normalized as stated.
Conversely, normalized data satisfying all retained canonical conditions are
already a packet with repeated square `A=1`; the coefficient-resultant
dependency and its invariant-coupling dependency reconstruct the matching
and the cycle. QED.

