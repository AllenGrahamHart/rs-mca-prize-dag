# Proof

The extension locator is monic of degree `tau_i`, so Euclidean division gives
the unique decomposition `(AR2)`. Since

```text
Lambda'_(A_i)(x)=Lambda'_(S_i)(x)Lambda_(T_i)(x)
                                                     for x in S_i,
```

the `Lambda_(T_i)U` part of the parity sum vanishes on `T_i` and cancels its
locator on `S_i`. The remainder `V` contributes on all of `A_i`. This proves
`(AR3)`. The two polynomial spaces in `(AR2)` have dimensions

```text
h-tau_i=d+1-z_i       and       tau_i,
```

proving `(AR4)`.

The support-extension factorization gives the selected block numerator

```text
P_i=R_i Lambda_(T_i),       deg R_i<=d-z_i.
```

It is therefore one nonzero member of the first summand. Extend `R_i` to a
basis of the polynomials of degree below `d+1-z_i`; after removing that one
check, the two residual dimensions satisfy

```text
(d-z_i)+tau_i=h-1,
```

which is `(AR5)`.

The support-local functionals in `(AR3)` are the complete dual of the
degree-less-than-`a` evaluation code on `S_i`, because

```text
|S_i|-a=d+1-z_i.
```

They all vanish exactly when `-f_i|S_i` is the evaluation of a polynomial
`w_i` of degree below `a`. Since `|S_i|>=a+1`, that polynomial is unique.
This proves `(AR6)`.

Assume `(AR6)`. The original split-pencil error on slope `gamma_i` is

```text
f_i+w_i.
```

It already vanishes on `S_i`. Hence it vanishes on the completed block
`S_i union T_i` exactly when every point of `T_i` belongs to the external
zero set `(AR7)`. The forced extension size in `(AR1)` makes the completed
block have size `a+h`, proving `(AR8)` and its converse. Choosing `tau_i`
points from `E_i` gives `(AR9)`. QED.
