# Proof

The element `3` generates `F_17^*`. Taking discrete logarithms of the four
supports in the dependency gives `(PCI2)`.

For an exponent `e`, evaluation of a degree-less-than-eight polynomial at
`zeta^e` is the row

```text
(1,zeta^e,...,zeta^(7e)).                               (1)
```

Insert `(1)` with the signs prescribed by the equal-value equations among the
words present at `e`. This gives the stated `28 x 24` matrix over
`Z[zeta]`, where `zeta^8=-1`. Exact elimination on the rows `(PCI3)` gives

```text
alpha=12582912 zeta^5-14680064 zeta^4+29360128 zeta^3
      -14680064 zeta^2+12582912 zeta,
```

which is the factorized expression in `(PCI4)`. The determinant of
multiplication by `alpha` on the integral basis
`1,zeta,...,zeta^7` is

```text
2^170 17^4.
```

The verifier reconstructs the matrix, performs elimination in
`Q[zeta]/(zeta^8+1)`, and computes this multiplication determinant with exact
integer arithmetic.

Let the same exponent pattern be realized over a field of odd characteristic
`p` with a primitive sixteenth root. If its intersection matrix is singular,
then the selected minor vanishes after reduction at the corresponding prime of
`Z[zeta_16]`. Therefore that prime divides `(alpha)`, and its rational
characteristic divides `|Norm(alpha)|`. Formula `(PCI4)` forces `p=17`.
The dependency directly computes rank `23` for the original `p=17`,
`zeta=3` realization.

Finally suppose `F` has characteristic `17`, cardinality `17^e`, and contains
an element of order `2^41`. Then `2^41` divides `17^e-1`. For odd `e`,
`v_2(17^e-1)=v_2(16)=4`. For even `e`, lifting the exponent gives

```text
v_2(17^e-1)
 =v_2(16)+v_2(18)+v_2(e)-1
 =4+v_2(e).
```

Hence `v_2(e)>=37`, so `e>=2^37`. This contradicts the official field cap,
since already `17^64>2^256` and `2^37>64`. Thus characteristic `17` is absent
at the prize-max row, proving the scoped transport exclusion. QED.
