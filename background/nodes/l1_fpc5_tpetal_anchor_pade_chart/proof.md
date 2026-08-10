# Proof: general t-petal anchor Pade chart

The anchor is primitive and satisfies

```text
W==c_iF mod L_i
```

for every `i`. Hence `gcd(F,Lambda)=1`: any common factor of `F` and one
`L_i` would also divide `W`. In particular, the roots of `F` avoid the
petal roots. Primitivity also gives `gcd(F,W)=1`, so the inverse `I` in the
statement exists.

By the definition of `R_H`,

```text
G_H W+Lambda H==0 mod F.
```

Thus `B_H` in `(PC1)` is a polynomial. Since `deg R_H<d`, the locator
`G_H=F+R_H` is monic of degree `d`. Moreover,

```text
deg(G_H W+Lambda H)
 <=max(2d,deg Lambda+e-1)=2d,
```

so `deg B_H<=d`.

For every petal locator `L_i`,

```text
F(B_H-c_iG_H)
 =G_H(W-c_iF)+Lambda H
```

is divisible by `L_i`. Since `gcd(F,L_i)=1`, this proves
`L_i|(B_H-c_iG_H)`. Hence `(G_H,B_H)` belongs to the pair slice, and the
definition of `B_H` gives `(PC3)`.

Conversely, let `(G,B)` be any point of the complete monic chart with
coordinate `H`. Reducing

```text
FB-GW=Lambda H
```

modulo `F` gives `G==-Lambda H I mod F`. Both `G` and `F` are monic of
degree `d`, so `deg(G-F)<d`; therefore `G=G_H`. The displayed determinant
identity then forces `B=B_H`. This proves the inverse and uniqueness claims.

It remains to prove `(PC5)`. If `G_H(x)=0` and `F(x)!=0`, then `(PC3)` gives

```text
F(x)B_H(x)=Lambda(x)H(x).
```

Both `F(x)` and `Lambda(x)` are nonzero, proving the first equivalence.
If `F(x)=G_H(x)=0`, then `(PC3)` first gives `H(x)=0`. Differentiate it and
evaluate at `x`. The terms containing `F(x)`, `G_H(x)`, and `H(x)` vanish,
leaving

```text
F'(x)B_H(x)-G_H'(x)W(x)=Lambda(x)H'(x).
```

Squarefreeness gives `F'(x)!=0`, so `B_H(x)!=0` is equivalent to the second
inequality in `(PC5)`. Finally, for squarefree `G_H`, coprimality with `B_H`
is exactly nonvanishing of `B_H` at every root of `G_H`. QED.
