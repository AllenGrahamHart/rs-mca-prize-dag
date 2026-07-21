# Proof

Because the row has support `S_i`, its active-union numerator vanishes on
`Z_i` and its selected-block numerator vanishes on `T_i`. Therefore

```text
F_i=R_X Lambda_(Z_i),       P_i=R_A Lambda_(T_i).    (1)
```

The support size is `|S_i|=|X|-z_i=a+d+1-z_i`, so

```text
|T_i|=|A_i|-|S_i|=h-d-1+z_i,
```

which proves `(SE3)`. The degree bounds in `(SE2)` give

```text
deg R_X<=d-z_i,
deg R_A< h-|T_i|=d+1-z_i,
```

and hence both cofactors have degree at most `d-z_i`.

For `x in S_i`, factor the locator derivatives as

```text
Lambda'_X(x)=Lambda'_(S_i)(x)Lambda_(Z_i)(x),
Lambda'_(A_i)(x)=Lambda'_(S_i)(x)Lambda_(T_i)(x).   (2)
```

Substituting `(1)` and `(2)` into the two equal values in `(SE2)` gives

```text
R_X(x)/Lambda'_(S_i)(x)=R_A(x)/Lambda'_(S_i)(x).
```

Thus `R_X` and `R_A` agree on every point of `S_i`. Every active row has
weight at least `a+1`, while `d-z_i<=a-1`; therefore polynomial uniqueness
gives `R_X=R_A=:R_i`. This proves `(SE4)` and `(SE6)`. If `R_i` vanished on
`S_i`, that point would not be in the support, proving `(SE5)` and uniqueness.

For the converse, the degree assumptions give

```text
deg(R Lambda_Z)<=d<|X|-a,
deg(R Lambda_T)<=d-|Z|+h-d-1+|Z|=h-1.
```

Hence the two locator formulas are words of the dual degree-less-than-`a`
evaluation codes on `X` and `A`. The derivative factorization `(2)` cancels
the corresponding locator on `S`, giving `R/Lambda'_S` in both formulas.
Both numerators vanish off `S` in their respective domains, and root
avoidance makes the support exactly `S`. The two extended words are therefore
identical. QED.
