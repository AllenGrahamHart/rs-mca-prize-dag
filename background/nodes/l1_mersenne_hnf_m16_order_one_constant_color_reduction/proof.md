# Proof - L1 Mersenne HNF m=16 order-one constant-color reduction

Write `H=h-1=14` and

```text
L(W)=W^H+l_1W^(H-1)+l_2W^(H-2)+...+l_H.
```

The hypergeometric top coefficients and the differential equation at
`y=1` give

```text
l_1=H/d,
l_2=(H(H-1)+r*d)/(2d^2),
l_(H-1)/l_H=-H*d/(r-1),
l_(H-2)/l_H=H*d*(r+(h-2)d)/((r-1)(r-2)).            (1)
```

If every reduced root has color `epsilon`, then

```text
L^[p](W)=W^H L(epsilon/W)/L(0).                     (2)
```

The first coefficient in (2), using `d^p=zeta/d`, gives

```text
r=1-alpha,       alpha=epsilon*zeta.                 (3)
```

The value `alpha=1` gives `r=0`, contrary to `rho*c!=0`. If `alpha=-1`,
then `r=2`; the second derivative of the HNF differential equation at one
gives

```text
d=-2/(h-2)=-2/13.                                   (4)
```

This lies in `F_p`, so `zeta=d^(p+1)=d^2` belongs to
`F_p intersect mu_16={+1,-1}`. Equation (4) would make the characteristic
divide `165` or `173`, not `8191`.

Now take `alpha!=+1,-1`. Comparing the second coefficient in (2) and using
(1)--(3) gives, for general `H=h-1`,

```text
H(h-2)alpha*d=(alpha+1)zeta+2H alpha^2.             (5)
```

At `h=15`, this is (CCR3). It puts `d` in `F_(p^2)` because
`alpha,zeta in mu_16` and `p=-1 mod 16`. Its norm `zeta=d^(p+1)` is
therefore in `F_p intersect mu_16={+1,-1}`.

Rewrite (CCR3) as

```text
d=(28alpha+zeta*(1+alpha^(-1)))/182.                (6)
```

Taking the `F_(p^2)/F_p` norm and putting
`s=alpha+alpha^(-1)` yields

```text
28zeta*s^2+(1+28zeta)s+786-33180zeta=0.             (7)
```

Reducing (7) modulo `8191` gives the two equations in (CCR4). Finally the
sixteenth-root traces are `+/-2`, `0`, the roots of `S^2-2`, and the roots
of `S^4-4S^2+2`, proving (CCR5). Therefore the two gcds in (CCR6) cover
every possible constant-color packet. QED.
