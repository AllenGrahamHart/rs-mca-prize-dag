# Proof - exceptional-E singular-affine router

Write the coefficients from (FQR1) and (FEQ1) as

```text
a_2=63A,       a_1=9240z(9-z),
a_0=400z(9-z)(z+27),

e_2=-720b,     e_1=240z-1902b-630,
e_0=-40b(z-6b+27).                                 (1)
```

Expanding `S_0=a_2e_0-e_2a_0`, factoring `360b`, and expanding the remaining
quadratic in `z` gives `S_0=360bE_0`. Expanding
`S_1=a_2e_1-e_2a_1` and factoring `126` gives `S_1=126E_1`. This proves
(FSA1)--(FSA3).

For (FSA4), use

```text
C=-7A+800z(9-z).
```

The terms containing `z(9-z)` cancel in `(z+27)E_1-66bE_0`. After using
`b^2=z`, the residue is

```text
A(120z^2+153z-8505-489b(z+27))
=-3A(163b(z+27)-40z^2-51z+2835),
```

which is `-3AR`.

Assume first that `S_1=S_0=0` on the declared chart. Since `b`, `126`, and
`360` are units, (FSA3) gives `E_0=E_1=0`. Since `A!=0`, (FSA4) gives
`R=0`. If `z+27=0`, this would force `N(-27)=24948=0`, but `24948` is
nonzero modulo every official prime. Thus

```text
b=N/(163(z+27)).                                    (2)
```

The square relation `b^2=z` now gives `H=0`, while substituting `(2)` into
`E_0=0` and multiplying by `163(z+27)` gives `K=0`.

Conversely, suppose `H=K=0`, retain `A!=0`, and reconstruct `b` by `(2)`.
The same `N(-27)` check makes this reconstruction legal. The equation `H=0`
gives `b^2=z`, and `K=0` gives `E_0=0`. Now (FSA4), together with `R=0`,
gives `(z+27)E_1=0`, so `E_1=0`. Equation (FSA3) recovers
`S_1=S_0=0`. This proves (FSA6).

The square in `N^2` gives leading coefficient `40^2=1600` for `H`. The
degree-four term of `K` comes only from `163(z+27)^2C`, and has coefficient
`-163*800=-130400`. Neither coefficient vanishes at an official prime.
Finally (FEQ3) reads `a_2E_G=e_2F_b` on `S_1=S_0=0`; hence (FSA7) recovers
`E_G=0` because `a_2!=0`. All equations not used in this coefficient
reduction remain retained. QED.
