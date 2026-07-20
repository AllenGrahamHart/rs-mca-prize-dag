# Proof

All four roots of `D_*` lie in `mu_N`, so `lambda=A^(-1)` is an allowed
common subgroup scaling. Dividing the roots by `A` gives `(C2N1)`. The
canonical-span covariance preserves the primary gap, secondary gap, span
identity, and split/Mobius verdict, while transforming the outer coefficients
as in `(C2N2)`. The invariant weights follow from

```text
I=alpha^2+12gamma,
J=72alpha gamma-27beta^2-2alpha^3.                  (1)
```

In particular,

```text
K_A(Z)=lambda^(12h)K_O(Z).                          (2)
```

The pair trace is unchanged by common scaling and equals

```text
(A+B)^2/(AB)=(1+t)^2/t.                            (3)
```

The joint pair-torsion selector proves that the original actual pair passes
precisely when its trace is a zero of `K_O` and `(A/B)^N=1`. Equations
`(2)` and `(3)` convert this criterion exactly to `(C2N4)`.

For the complementary pair let

```text
T_j=c^(2^j)+d^(2^j),       P_j=(cd)^(2^j).          (4)
```

The initial values are `S,P`, and squaring `(4)` gives the last two
recurrences in `(C2N5)`. The recurrence for `t_j` is immediate. Therefore
`t,c,d in mu_N` implies all three terminal equations.

Conversely, set `x=c^N` and `y=d^N`. The last two terminal equations give

```text
x+y=2,       xy=1.
```

Both are roots of `(Z-1)^2`, hence `x=y=1`; the first terminal equation gives
`t^N=1`. This proves `(C2N6)`.

The factors in `(C2N7)` respectively enforce nonzero selected and
complementary roots, distinct selected roots, neither complementary root
equal to one, neither complementary root equal to `t`, and distinct
complementary roots. The separate split and square conditions are inherited
from the cycle router.

If instead the same unordered selected pair is normalized at `B`, then its
new coordinates are

```text
A/B=t^(-1),       C/B=c/t,       D/B=d/t,
S'=S/t,       P'=P/t^2,
```

which proves `(C2N8)`; applying it twice is the identity. Every original
passing packet can therefore be normalized into the claimed chamber.
Conversely, normalized data satisfying all retained conditions already
describe an actual selected pair with its exact invariant coupling and
torsion conditions, so undoing the subgroup scaling recovers the original
packet. QED.
