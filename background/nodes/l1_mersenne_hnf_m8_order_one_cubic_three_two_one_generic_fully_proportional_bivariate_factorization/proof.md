# Proof - L1 Mersenne HNF m=8 order-one cubic three-two-one generic fully-proportional bivariate factorization

Write

```text
P=p_0+p_1q,
p_0=40b(b^2-6b+27),       p_1=42(11b+15),

Q=q_0+q_1q,
q_0=480(b^2+27),          q_1=5544.                (1)
```

Collect powers of `q` in `F_N=6P^2-bPQ+2880b^2T_c`. The constant,
linear, and quadratic coefficients are respectively

```text
9600b^2(9-b^2)(b^2+27),
221760b^2(9-b^2),
1512(1575-247b^2).                                  (2)
```

Substituting `z=b^2` and dividing (2) by the official unit 24 proves
(FBF2)--(FBF3).

The dependency has `b*q!=0`, so `z!=0`. If `z=9`, the last two terms in
(FBF3) vanish while the first is

```text
63(1575-247*9)q^2=-63*648q^2!=0,                   (3)
```

proving (FBF4).

For the generic coefficient chart, direct calculation gives

```text
Disc_q(F_b)
 =9240^2z^2(9-z)^2
  -4*63*400(1575-247z)z(9-z)(z+27)

 =302400z(9-z)(-200z^2+4239z-14175),               (4)
```

which proves (FBF5). If the leading coefficient vanishes, then
`z=1575/247`; it is neither zero nor nine, so the linear coefficient is
nonzero. Solving (FBF3) gives (FBF6). All excluded integer primes are at
most 19 and hence are absent from the official characteristics. QED.
