# Proof - L1 Mersenne HNF order-zero linear-color exclusion

Put `h=m-1`. The roots of `P_s` are distinct and nonzero because `P_s`
divides the squarefree polynomial `W^n-1`.

First suppose `E_s=epsilon` is constant. Put `t=s^p`. Frobenius sends each
root `a` to `a^p=epsilon/a`, so comparison of the monic root polynomials
gives

```text
P_t(W)=P_s(0)^(-1) W^h P_s(epsilon/W).               (1)
```

Since `s,t notin F_p`, the generalized binomial coefficients through degree
`h` are nonzero. Ratios of successive coefficients in `(1)` give, for
`1<=r<=h`,

```text
(t+r-1)/r=epsilon (h-r+1)/(s+h-r).                   (2)
```

After cross multiplication, the two quadratics in `r`

```text
-r^2+(s+h-t+1)r+(t-1)(s+h)
and
epsilon[-r^2+(h+1)r]                                (3)
```

agree at `r=1,2,3`. They are identical because `p>h+1`. Their quadratic
coefficients give `epsilon=1`, and their linear coefficients then give
`s=t`, contradicting `s notin F_p`. Thus `E_s` is nonconstant.

Now suppose for contradiction that

```text
E_s(W)=alpha W+beta,       alpha!=0.                 (4)
```

For every root `a` of `P_s`, equation `(LCE1)` gives

```text
E_s(a)^m=a^(m(p+1))=a^n=1.                          (5)
```

The linear map `E_s` is injective. It therefore sends the `h=m-1` roots of
`P_s` to `m-1` distinct members of `mu_m`. There is one missing color
`eta in mu_m`. Normalize

```text
x=beta/eta,       y=alpha/eta.                       (6)
```

Since `eta^m=1`, comparison of monic polynomials gives

```text
P_s(W)=y^(-h) ((yW+x)^m-1)/(yW+x-1)
      =y^(-h) sum_(j=0)^h (yW+x)^j.                 (7)
```

Let `C_r(x)` be `y^r` times the coefficient of `W^(h-r)` on the right of
`(7)`. The first three coefficients are

```text
C_1=1+hx,
C_2=1+(h-1)x+h(h-1)x^2/2,
C_3=1+(h-2)x+(h-1)(h-2)x^2/2
                 +h(h-1)(h-2)x^3/6.                (8)
```

The coefficient of `W^(h-r)` in `P_s` is
`binom(s+r-1,r)`. Hence

```text
C_1=sy,
2C_2=C_1(C_1+y),
6C_3=C_1(C_1+y)(C_1+2y).                            (9)
```

Write the last two equations as `E_2(x,y)=E_3(x,y)=0`. Direct expansion gives

```text
E_2=-hx^2-hxy-2x-y+1.                              (10)
```

Eliminating `y` from the two equations gives the exact resultant

```text
Res_y(E_2,E_3)=-2(h+1)x(x-1)(hx+1).                (11)
```

All denominators and the scalar in `(11)` are invertible on the official
rows because `p>h+1`. Thus `x` is `0`, `1`, or `-1/h`. The last value is
impossible: substituting it in `(10)` gives `(h+1)/h!=0`. If `x=0`, equation
`(10)` gives `y=1`, and then `(9)` gives `s=1`. If `x=1`, equation `(10)`
gives `y=-1`, and `(9)` gives `s=-(h+1)=-m`. Both values lie in `F_p`,
contrary to `(LCE1)`. Therefore `deg E_s` is at least two. QED.
