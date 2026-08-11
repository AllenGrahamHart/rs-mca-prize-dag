# Proof

In `(ZTP1)`, the packet theorem gives

```text
d_(x_*)=I_H=Delta=e-2,       O=Delta-2=e-4,           (1)
```

and there are no ordinary heavy incidences. Every one of the `Delta`
incidences at `x_*` consumes at least one excess-recurrence degree. Since
the total excess degree is at most `Delta`, equality holds throughout:

```text
sum_gamma c_gamma=Delta,
c_gamma=1 at each of the Delta incidences,             (2)
```

and no excess degree remains at another slope.

At such a slope the specialized factorization is

```text
Qbar_gamma=Q_min R_gamma,       R_gamma=X-x_*          (3)
```

up to scalar. If `x_*` is a root of `Q_min`, `(3)` has a double root and
contributes one omission. If not, it is a new simple domain root and
contributes no omission. Equation `(1)` therefore says that the first case
occurs at exactly `e-4` slopes and the second at exactly two, denoted
`alpha,beta`.

The local cancelled cube identity at `x_*` is

```text
s_F^3 G_L=P_Z(X-x_*).                                  (4)
```

At one of the first `e-4` points, the horizontal intersection multiplicity
is two. If `n` is the vertical intersection multiplicity there, `(4)`
gives `2+n` divisible by three, hence `n>=1` with equality only at one. At
`alpha,beta`, the horizontal multiplicity is one, so `1+n` is divisible by
three and `n>=2`, with equality only at two. These lower bounds already sum
to

```text
(e-4)*1+2*2=e.                                         (5)
```

The vertical fibre has total degree `e`. Thus all bounds in `(5)` are
equalities and there are no other points on that fibre. This proves the
factorization of `q_*` in `(ZTP3)`.

The core-one adjugate theorem gives a form `D` of degree `Delta`, with
`ord_gamma(D)>=c_gamma`. Equation `(2)` and the degree of `D` force simple
zeros at exactly the `Delta` incidence slopes. Hence `D` is their
squarefree locator, proving the first line of `(ZTP3)`.

The Forney numerator vanishes at every heavy incidence. Since `D` is
squarefree,

```text
D divides N_F(U,V;x_*).                                (6)
```

The numerator has parameter degree at most `e+1`, so the quotient in `(6)`
has degree at most three. It is nonzero. Indeed, if the specialization were
identically zero, the surface numerator would be divisible by `X-x_*`.
The cube identity makes `s_F` nonzero on every mixed component, while that
factor would put the full degree-`e` vertical fibre in its zero divisor.
This contradicts `deg div(s_F)=Delta=e-2`. This proves the first line of
`(ZTP4)`.

At every root of `P_ord`, the specialized `X`-root is double, so the first
`X`-derivative vanishes. At `alpha,beta` it is simple, so the derivative is
nonzero. Its parameter degree is at most `e`; division by the degree-`e-4`
form `P_ord` proves the second line of `(ZTP4)`.

Finally, `(4)` and the equalities in `(5)` give contact multiplicity one at
each of the `Delta` distinct points. These already exhaust the degree of the
contact line bundle, so its zero divisor is their reduced sum. The vertical
fibre contains those points once and contains one additional copy at each
of `P_alpha,P_beta`, proving `(ZTP5)`. Since the contact line bundle is
`O_C(-rho-1,e+1)` and the vertical fibre has class `O_C(1,0)`, `(ZTP6)`
follows by rearranging. Its degree is

```text
(rho+2)e-(e+1)(rho-1)=2                               (7)
```

using `rho=3e-1`. QED.
