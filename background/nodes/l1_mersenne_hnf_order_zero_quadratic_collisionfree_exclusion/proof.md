# Proof - L1 Mersenne HNF order-zero quadratic collision-free exclusion

Write

```text
E_s(W)=A W^2+B W+C,       A!=0,       S=-B/A,
U=W(W-S).                                               (1)
```

Suppose, for contradiction, that `E_s` takes distinct values on the `h=m-1`
roots `a_1,...,a_h` of `P_s`. Those values are distinct members of `mu_m`,
so exactly one color is missing.

The other root in the quadratic fiber through `a_i` is `S-a_i`. By the
collision-free assumption it is not a root of `P_s`. Hence

```text
P_s(W)(-1)^h P_s(S-W)=H_(s,S)(U),                    (2)
```

where `H_(s,S)` is monic of degree `h` with distinct roots

```text
u_i=a_i(a_i-S).                                      (3)
```

The color is affine in this invariant:

```text
E_s(W)=A U+C.                                        (4)
```

Therefore `(4)` maps the roots of `H_(s,S)` bijectively to `mu_m` minus one
color.

We now compute only the first three coefficients of `H_(s,S)`. If `p_j` is
the `j`th power sum of the roots of `P_s`, Newton's identities and

```text
sum_(r=0)^(j-1) binom(s+r-1,r)=binom(s+j-1,j-1)
```

give

```text
p_j=-s,       1<=j<=h.                               (5)
```

For `z=1-S` and `r<=3`, expansion of `(a_i^2-Sa_i)^r` uses only
`p_j` with `j<=6<=h`, so

```text
sum_i u_i^r=-s z^r.                                  (6)
```

Applying Newton's identities once more, the coefficient of `U^(h-r)` in
`H_(s,S)` is

```text
d_r=binom(s+r-1,r) z^r,       r=1,2,3.              (7)
```

Normalize the missing color to one and write the affine color map in `(4)`
as `yU+x`. The punctured-cyclotomic identity is

```text
H_(s,S)(U)=y^(-h) sum_(j=0)^h (yU+x)^j.              (8)
```

Let `C_r(x)` be `y^r` times the coefficient of `U^(h-r)` on the right. If
`z!=0`, equations `(7)--(8)`, with `Y=yz`, give

```text
C_1=sY,
2C_2=C_1(C_1+Y),
6C_3=C_1(C_1+Y)(C_1+2Y).                             (9)
```

These are exactly the three-coefficient equations in the linear-color
dependency. Their exact resultant is

```text
-2(h+1)x(x-1)(hx+1).                                (10)
```

The three cases force `s=1`, `s=-m`, or an inconsistent second coefficient,
so each contradicts `s notin F_p`.

If `z=0`, equation `(7)` gives `d_1=d_2=0`. The first equation from `(8)`
forces `x=-1/h`, but then

```text
C_2(-1/h)=(h+1)/(2h)!=0,                            (11)
```

contradicting `d_2=0`. Thus the collision-free quadratic branch is empty.
QED.
