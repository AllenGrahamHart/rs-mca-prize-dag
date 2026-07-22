# Proof - L1 Mersenne next-to-maximal hypergeometric normal form

The dependency supplies

```text
G-lambda Y=((Y-r_0)(Y-z)/(2a))(hG-YG').               (1)
```

Substitute `Y=r_0y`, divide by `r_0^h`, and use the definitions in (HNF1).
This gives (HNF2). The normalization of the leading coefficients follows
from the monicity and depression of `G`.

## 1. Coefficient recurrence and the branch equation

The coefficient of `y^k` on the right of (HNF2) is

```text
(h-k+2)g_(k-2)-(1+c)(h-k+1)g_(k-1)+c(h-k)g_k.
```

Moving the last term to the left proves (HNF3). Since `h<p`, every integer
denominator in the top-down recurrence is invertible. The equations from
`k=h` through `k=2` therefore determine all lower coefficients down to
`g_0`; the `k=1` equation determines `ell` because `A!=0`. At `k=0` the
two absent negative-index terms leave exactly (HNF4).

The least exponent of `T=hG-YG'` is the least lower index `j` for which
`(h-j)g_j` is nonzero. The dependency already proves that this order is zero
or one. Hence the two cases are precisely `g_0!=0` and
`g_0=0,g_1!=0`. Equation (HNF4) gives `2A=ch` in the first case. Since
`theta=2a/(r_0z)=2A/c`, this also gives `theta=h`. In the second case the
top-down expression for `g_0` is a polynomial in `A,c`; its only divisions
are by nonzero elements of the prime field.

For the closed form, reverse the coefficients by putting `u_r=g_(h-r)`.
For `0<=r<=h-2`, recurrence (HNF3) is

```text
(r+2)u_(r+2)-(1+c)(r+1)u_(r+1)-(2A-cr)u_r=0.
```

The formal series `U=sum_(r>=0)u_r t^r`, initialized by `u_0=1,u_1=0`,
therefore obeys, through the required order,

```text
(1-t)(1-ct)U'=2AtU.
```

With `rho=2A/[c(c-1)]`, its unique unit-constant solution is

```text
U=(1-t)^(c rho)(1-ct)^(-rho).
```

This proves (HNF4a). In particular the order-one condition `g_0=0` is the
explicit coefficient equation (HNF7a), equivalent to the recurrence-defined
curve above.

## 2. The hypergeometric polynomial

Assume `ord_0(T)=0`. Write the dependency's shifted polynomial as

```text
P(W)=sum_(j=0)^h p_j W^j,       p_h=1.
```

Because `G` is depressed, affine translation gives

```text
p_(h-1)=h r_0/(z-r_0)=h/(c-1)=s.                     (2)
```

The dependency also gives

```text
W(W-1)P'-K=(hW+b)P.                                  (3)
```

Comparison of the coefficient of `W^h` in (3), using (2), gives
`b=-h-s`. For `1<=j<=h`, comparison of the coefficient of `W^j` gives

```text
(j-1-h)p_(j-1)-(j+b)p_j=0.                           (4)
```

Put `j=h-r+1`. Equation (4) becomes

```text
r p_(h-r)=(s+r-1)p_(h-r+1).
```

Induction from `p_h=1` proves (HNF5). The constant coefficient of (3) is
`-K=bp_0`, proving (HNF6).

The dependency proves `P|W^n-1`. It also proves that in this chamber
`c` cannot lie in `F_p`, because `theta=h` does. The fractional-linear
relation `s=h/(c-1)` then shows `s notin F_p`, proving (HNF7).

## 3. Torsion on the order-one curve

Assume `ord_0(T)=1`. Then zero is a split value and its root in the shifted
coordinate is

```text
x_0=(0-r_0)/(z-r_0)=-1/(c-1).
```

Every shifted split value lies in `mu_n` by the dependency. Since `n` is
even, `x_0^n=1` is equivalent to `(c-1)^n=1`, proving (HNF8). The remaining
cyclotomic divisibility and non-prime-field condition are exactly those of
the dependency. This proves the stated normal form without asserting that
either low-dimensional residue is empty.
