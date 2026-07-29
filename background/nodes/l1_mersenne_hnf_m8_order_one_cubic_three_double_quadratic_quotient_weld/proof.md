# Proof - L1 Mersenne HNF m=8 order-one cubic three-double quadratic-quotient weld

Substitute `b=p+12` into `D_b=b^2+3Hb+3K`. The coefficient of `p` is

```text
24+3H=3x^2-q/2=a.
```

The constant term simplifies to

```text
144+36H+3K=-3q(d^2+3d+3)/4-q^2/8=-h,
```

proving (QQW2).

If `p^n=U_np+V_n` modulo (QQW2), then

```text
p^(n+1)=U_n(-ap+h)+V_np
       =(V_n-aU_n)p+hU_n,
```

which proves (QQW3) by induction. Every polynomial in `p` consequently has
a unique affine-linear remainder. Formula (AIF5) is polynomial in `p`
after clearing `2,3`, and each expression in (AIF6) is polynomial in `P,Q`;
this proves (QQW4).

For (QQW5), expand the first formula in (AIF5), use
`ell=x^2+q/6-2p/3` and `eta=-xp-q(d+2)/6`, and reduce `p^2,p^3` by (QQW2).
The terms involving `h` cancel from the constant coefficient, leaving
exactly `R_P,S_P`.

It remains to prove the weld. In the shifted variable `p`, equations (TLR5)
and (TLR7) are

```text
alpha p+delta=0,       A_6p+gamma=0.                (1)
```

Because `alpha!=0`, the first equation gives `p=-delta/alpha`. Substitution
in (QQW2), the second equation in (1), and (QQW4) gives respectively the
last three equations in (QQW7). The conic is unchanged.

Conversely, a solution of (QQW7) on `alpha!=0` reconstructs
`p=-delta/alpha`. The second, third, and fourth equations then recover
(QQW2), `M_6=0`, and the chosen color factor; (1) recovers `M_5=0`.
Thus (QQW7) is equivalent to the complete generic p-free core in that color
packet, not merely a projection of it. QED.
