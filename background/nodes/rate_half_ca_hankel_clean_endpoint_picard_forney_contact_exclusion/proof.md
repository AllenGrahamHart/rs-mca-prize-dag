# Proof

Put `u=X^(-1)` on the chart around `X=infinity`, and write

```text
q^vee(z;u)=u^rho Q(z;u^(-1)).                         (1)
```

The canonical numerator is

```text
N(z;u)=[q^vee(z;u)sum_(i=0)^(rho-1)y_i(z)u^i]_(<rho),
u^(rho-1)P(z;u^(-1))=N(z;u).                         (2)
```

Use instead the available moment polynomial

```text
Y(z;u)=sum_(i=0)^(2rho+1)y_i(z)u^i.                  (3)
```

For `rho<=k<=2rho+1`, the coefficient of `u^k` in `q^vee Y` is

```text
sum_(j=0)^rho q_j(z)y_(k-rho+j)(z).                  (4)
```

These are precisely the `rho+2` rows of the full rectangular Hankel kernel
equation `M(z)q(z)=0`. The coefficients below degree `rho` are exactly `N`.
It follows that there is a polynomial `R(z;u)` such that

```text
q^vee(z;u)Y(z;u)=N(z;u)+u^(2rho+2)R(z;u).            (5)
```

In the coordinate ring of `C` on this chart, `q^vee=0`. Equations `(2)` and
`(5)` therefore give

```text
u^(rho-1)P(z;u^(-1))=-u^(2rho+2)R(z;u).              (6)
```

Thus the restriction of the homogenized Forney section is divisible by the
`(2rho+2)`nd power of the local equation of `H_X`. This is `(PFC2)`.
The normalized resultant theorem says

```text
Res_X(Q,P)=c a^(2rho+2)Delta!=0,
```

so `P` does not vanish identically on the integral curve. Dividing its
section by the canonical section cutting out `(2rho+2)H_X` gives a nonzero
section of

```text
O_C(rho-1,m+1) tensor O_C(-(2rho+2),0)
 =O_C(-rho-3,m+1)=L_F.                               (7)
```

Its degree is

```text
deg L_F=(-rho-3)m+(m+1)rho=rho-3m=m-1.               (8)
```

The two-axis Picard theorem gives `(PFC4)` and its canonical nonzero point
section. Since `C` is integral, the fourth tensor power of the section in
`(7)` times the point section is nonzero. The parameter identities
`rho=4m-1`, `N=16m`, and `T=4m+1` give

```text
4(-rho-3)+N=-8,       4(m+1)-T=3,                    (9)
```

so this product lies in `H^0(C,O_C(-8,3))`.

It remains to compute that space. Since `C` is the integral Cartier divisor
of bidegree `(rho,m)` in `P^1_X x P^1_z`, restriction gives

```text
0 -> O(-rho-8,3-m) -> O(-8,3) -> O_C(-8,3) -> 0.    (10)
```

The middle surface has no global sections. For `m>3`, the Kunneth formula
also gives

```text
H^1(O(-rho-8,3-m))=0:                                (11)
```

the first summand contains `H^0(P^1,O(3-m))=0`, while the second contains
`H^0(P^1,O(-rho-8))=0`. The long exact sequence of `(10)` proves `(PFC6)`.
This contradicts the nonzero tensor-product section and excludes the clean
endpoint. QED.
