# Proof

Substitute the printed common values into the explicit involution formulas.
They give `(Gamma,Alpha,Beta)=(7,16,16)`, `Delta=-1`, and forced mate
`m=18`.  The `S1` signed products are

```text
ce, -cf, -de, df, -d^2, ef, -ef.
```

At `(d,e,f)=(15,7,18)` these and the five common products give exactly
`(KB41FW-2)`.  Direct reduction modulo 41 proves all twelve are distinct,
as are the representative squares.

Remove the forced value `-de=18`.  The Mobius action

```text
u |--> (16u+16)/(7u-16)
```

sends the residual products in the three pairs `(KB41FW-3)`, with every
denominator nonzero.  Equivalently, direct homogeneous substitution in the
sextic with coefficient vector `(KB41FW-4)` gives `H(M)=-H=Delta^3 H`.

For completeness, put `e=-m/d` and `f=sd`, multiply the monic residual
sextic by the nonzero scalar `d`, and enumerate all nonzero `(d,s)` in
`F_41^2`.  Testing all seven coefficient equations and both injectivity
guards leaves only `(15,34)`, which recovers `(KB41FW-1)`. QED.
