# Proof

For core one and scalar residual degree two, the exact heavy-incidence
identity is

```text
I_H+O=e-6.                                           (1)
```

Subtracting `(1)` from `2Delta=2e-4` gives

```text
u+v=e+2.                                             (2)
```

Because `v<=Delta=e-2`, equation `(2)` gives `u>=4`. If `u=4`, then

```text
v=Delta,       O=0,       I_H=Delta-u=e-6.           (3)
```

The omission identity is a sum of nonnegative terms
`deg R_gamma-t_gamma`. Hence `O=0` makes every specialized excess factor
squarefree and disjoint from the minimal locator. At an ordinary heavy
incidence the residual scalar is a unit, so the horizontal multiplicity
would be one, contrary to ordinary cube divisibility. Thus `I_0=0`.

Every distinguished incidence consumes one excess degree. Any additional
excess root would again lie off the residual-root rows and have horizontal
multiplicity one at a unit of the residual scalar, which is impossible.
Therefore

```text
C_tot=I_H=e-6,       w=Delta-C_tot=4,                (4)
```

proving `(QG43)`.

At least one root of the residual quadratic is heavy because `I_H>0`. If
the quadratic has a double root, it is the unique heavy root and carries
all `e-6` distinguished incidences. Its deficit is six.

At every such incidence the horizontal multiplicity is `m=1`. For a
double residual root the cancelled cube identity is

```text
3k=m+2n.                                             (5)
```

Thus the least positive vertical multiplicity is one. Unsupported vertical
roots have multiplicity divisible by three. Exact vertical degree gives

```text
V_*=R_*+3B,       deg B=2.                           (6)
```

Equation `(5)` then gives contact divisor `R_*+2B`, whose degree is
`e-6+4=Delta`; it is the complete divisor of `s_F`. Since the vertical
fibre has class `O_C(1,0)`, subtracting the contact divisor from it proves
the Picard identity in `(QG44)`.

The divisor `B` is a proper length-two subdivisor of the vertical fibre:
the nonempty reduced divisor `R_*` remains. Its two elementary-modification
directions lie in the nilpotent ideal of the fibre algebra and miss the
constant line. Starting from

```text
pi_*O_C=O direct_sum O(-d)^(e-1),       d=rho-1,      (7)
```

both modifications enter the negative block independently. This gives
`(QG45)`. The rational section `(X-x_*)/s_F` has divisor `B`, so it is the
unique section.

It remains to handle a squarefree residual. A single heavy simple root
would carry all `e-6` distinguished incidences. At each, the simple-root
cube identity with `m=1` forces vertical multiplicity at least two, giving
vertical degree at least `2(e-6)>e`, a contradiction. Hence both roots are
heavy.

Write `d_i=e-c_i` for their distinguished counts. Then

```text
d_1+d_2=e-6,       c_1+c_2=e+6.                      (8)
```

All distinguished roots are new, so the simple-row correction is

```text
q_i=c_i-d_i=2c_i-e.                                  (9)
```

It is a nonnegative multiple of three, and `(8)` gives

```text
q_1+q_2=12.                                          (10)
```

The official `e` is odd, so each `q_i=2c_i-e` is odd. The only unordered
pair of nonnegative odd multiples of three summing to twelve is `{3,9}`.
This proves `(QG46)`.

On a simple root row, `m=1` at every point of `R_i`, so the least vertical
multiplicity is two. Exact degree and `(9)` therefore give

```text
V_i=2R_i+3P_i,       deg P_i=q_i/3.                  (11)
```

The contact divisor there is `R_i+P_i`. Its total degree is

```text
(e-6)+(1+3)=e-2=Delta,                               (12)
```

so no other contact zero remains and `(QG47)` follows.

Finally, on each fibre

```text
V_i-(R_i+P_i)=R_i+2P_i.                              (13)
```

The two fibres have class `O_C(2,0)`. Comparing `(13)` with the contact
line bundle `O_C(-rho-1,e+1)` proves `(QG48)`. Its degree on the
bidegree-`(rho-1,e)` curve is

```text
(rho+3)e-(e+1)(rho-1)=4e-rho+1=e+2.                 (14)
```

QED.
