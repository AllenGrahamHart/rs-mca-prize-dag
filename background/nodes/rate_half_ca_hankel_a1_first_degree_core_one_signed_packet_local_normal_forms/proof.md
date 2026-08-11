# Proof

Let

```text
C_tot=sum_gamma deg R_gamma
```

be the total excess-recurrence degree. For each parameter fibre, let
`t_gamma` count the distinct roots of `R_gamma` outside the squarefree
minimal locator. The omission identity is

```text
O=sum_gamma(deg R_gamma-t_gamma),
t:=sum_gamma t_gamma=C_tot-O.                         (1)
```

The regular-rank budget gives `C_tot<=Delta`. Every distinguished incidence
uses at least one excess copy, and every ordinary incidence uses at least
two. Hence

```text
C_tot>=d_*+2I_0=Delta-(u-I_0).                        (2)
```

For `(1,1,1,4)`, the right side of `(2)` is `Delta`, while
`O=Delta-1`. Therefore

```text
C_tot=Delta,       t=1.                               (3)
```

For `(2,0,1,5)` and `(2,0,2,6)`, one has `O=Delta`; consequently

```text
C_tot=Delta,       t=0.                               (4)
```

We next spend these exact budgets. At any supported incidence write `b` for
the indicator that the point belongs to the squarefree minimal locator and
`r>=1` for its multiplicity in the excess factor. Its horizontal
intersection multiplicity is

```text
m=b+r.                                                (5)
```

At an ordinary incidence the residual scalar is a unit, so the cancelled
cube identity gives `m=3k`. Thus the least possibility is `b=1,r=2,m=3`
and `k=1`; if `b=0`, at least three excess copies are required.

In packet `(1,1,1,4)`, equality in `(2)` leaves no unspent excess degree.
The ordinary incidence is therefore `b=1,r=2`. Every distinguished
incidence has `r=1`, and `(3)` says exactly one of them has `b=0`. Denote
that reduced point by `A`.

In packet `(2,0,2,6)`, equality again leaves no unspent degree, while
`t=0`. Both ordinary incidences are `b=1,r=2`, and every distinguished
incidence is `b=1,r=1`.

Packet `(2,0,1,5)` has exactly one excess degree beyond the minimum in
`(2)`, and `t=0`. The ordinary incidence must have `b=1`. Raising its
excess multiplicity from two to three would give `m=4`, contrary to
`3|m`. Placing the spare copy at any other point off the distinguished row
would give `b=r=1` and again `m=2`, contrary to the ordinary cube identity.
Hence the spare copy occurs at a unique distinguished incidence `A`. At
that point `b=1,r=2`; every other distinguished incidence has `b=r=1`.

It remains to read the vertical fibre. Let `n` be the positive vertical
intersection multiplicity and `k` the contact multiplicity at a
distinguished incidence. Since the residual scalar has a simple zero at
the distinguished domain point, the local identity is

```text
3k=m+n.                                               (6)
```

The official integer `e` is divisible by three.

For `(1,1,1,4)`, the divisor of horizontal multiplicities on `R_*` is
`2R_*-A`. Thus `n` is `2 mod 3` at `A`, `1 mod 3` at the other
distinguished points, and `0 mod 3` at unsupported vertical points. Since
`deg R_*=e-4`, the complete degree-`e` vertical divisor has the unique
divisor form

```text
V_*=R_*+A+3B,       deg B=1.                          (7)
```

Adding the horizontal and vertical multiplicity divisors in `(6)` gives
`3R_*+3B`; hence the contact divisor on this fibre is `R_*+B`.

For `(2,0,1,5)`, the horizontal divisor on `R_*` is `2R_*+A` and
`deg R_*=e-5`. The same congruence and degree calculation gives

```text
V_*=R_*+2A+3B,      deg B=1,                          (8)
```

and `(6)` gives contact divisor `R_*+A+B` on this fibre.

For `(2,0,2,6)`, the horizontal divisor is `2R_*` and
`deg R_*=e-6`. Therefore

```text
V_*=R_*+3B,         deg B=2,                          (9)
```

and the contact divisor on this fibre is `R_*+B`.

The ordinary-incidence calculation above gives contact multiplicity one at
each point of `R_0`. Comparing `(7)`--`(9)` with

```text
div(s_F)=R_*+R_0+E_u
```

uses all `u` residual contact degrees on the distinguished fibre. Hence
`E_1=B`, `E_2=A+B`, and `E_2=B` in the three cases. Substitution into
`O_C(rho+2,-e-1)=O_C(Z_c-R_0-E_u)`, with
`Z_c=V_*-R_*`, proves `(SLN2)`--`(SLN4)`. QED.
