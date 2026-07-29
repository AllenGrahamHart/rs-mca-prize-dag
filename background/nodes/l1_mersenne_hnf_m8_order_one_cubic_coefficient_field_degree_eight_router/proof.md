# Proof - L1 Mersenne HNF m=8 order-one cubic coefficient-field degree-eight router

Fix an official exponent `t` in (CFR1). Modulo `n=2^(t+3)`, direct
expansion gives

```text
p^2=(2^t-1)^2 = 1-2^(t+1) = 1-n/4 mod n,
p^4                         = 1-n/2 mod n,
p^8                         = 1 mod n.              (1)
```

The omitted square terms are divisible by `2^(t+3)` because `t>=13`.
Neither `p`, `p^2`, nor `p^4` is one modulo `n`. Since every proper divisor
of eight is `1`, `2`, or `4`, equation (1) proves (CFR2).

The roots of `X^n-1` over `F_p` lie in `F_(p^e)` precisely when
`n | p^e-1`. Thus (CFR2) says that its splitting field is `K=F_(p^8)`.
The Belyi shifted-value gate proves

```text
P(W)=(W+1/d)L(W) divides W^n-1.                     (2)
```

Hence the known root `-1/d` and all six roots of `L` lie in `K`. They are
nonzero, so `d in K`. Every monic factor of `L` selected by a color fiber
has a root set contained in `K`; its coefficients are elementary symmetric
functions of those roots and therefore also lie in `K`. In particular the
complementary cubic `G` has `g_1 in K`. Formula (CFR4) now proves (CFR5).

Finally, an irreducible polynomial of degree `e` over `F_p` has all its
roots in `F_(p^e)`, and one of those roots lies in `F_(p^8)` exactly when
`F_(p^e)` embeds in `F_(p^8)`. For finite fields this is equivalent to
`e | 8`. The possible degrees are exactly `1,2,4,8`, proving (CFR6) and the
packet classification rule. QED.
