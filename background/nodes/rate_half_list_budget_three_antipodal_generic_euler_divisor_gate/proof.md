# Proof

The centered generic norm expansion is

```text
F=U^4+e_2U^2V^2+e_3UV^3+e_4V^4=U^4+V^2K.            (1)
```

Since `DF=Y^d-1`, putting `S=DV^2K` gives

```text
DU^4=Y^d-1-S.                                        (2)
```

Multiply the definition of `T` by `U^3` and add `d`:

```text
P=dDU^4-Y(DU^4)'+d.                                  (3)
```

Substitute `(2)`. The Euler expression of `Y^d-1` vanishes, leaving

```text
P=YS'-dS
 =V(2YDV'K+YV(D'K+DK')-dDVK).                       (4)
```

This proves `V|P` without assuming that `V` is squarefree. The quotient
pencil has `gcd(U,V)=1`. Also `P` is congruent to the nonzero scalar `d`
modulo `U`, so `gcd(P,U)=1`. If `V` shared a factor with `T`, that factor
would divide both terms of `P=TU^3+d`, hence the nonzero scalar `d`.
Therefore `gcd(V,TU)=1`, proving `(GED4)--(GED5)`.

On the generic floor, `deg T=1` and `U` is monic of degree `r`; the
characteristic exceeds `d>3r+1`, so the leading term does not cancel and
`deg P=3r+1`. Substitution of `r=2^37-1` and `v=2^36-2` gives

```text
3r+1=6*2^36-2,       (3r+1)-v=5*2^36,
```

which is `(GED6)`. The canonical-span converse shows that the primary and
secondary gaps determine the normalized `U,V`, so `(GED5)` is a deterministic
necessary test on the four deleted roots. QED.
