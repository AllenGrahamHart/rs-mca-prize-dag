# Proof

Reconstruct the six systems in `(KBM3-1)` with the pinned generic `5 x 5`
source solver. Reduce modulo `p` and sequentially saturate each four-equation
ideal by its eleven reconstruction factors and by `b,c,d,c-d`. Five ideals
become unit. Independent ideals `<I,1-yL>`, with `L` the complete product of
fifteen factors, give the same five unit classifications and retain only
`M03-OB-RL`.

The surviving complete-chart ideal is zero-dimensional. Exact lex conversion
gives `(KBM3-2)`, with basis SHA-256

```text
3322ad7d8d8efb28dc60a861306faad5f382ebc0c275efa879b86932d38605fa.
```

Factoring the `c`-eliminant gives `(KBM3-3)`. Sage's factorization over `F_p`
certifies two distinct irreducible degree-two factors, each with multiplicity
one. The linear `b` relation and `d=-1` then give exactly four direct points
over `F_(p^2)`. Since `2` divides `6`, all four lie in the deployed field.

The restricted inversion theorem is exact for q-slices and localizers, but
not for full quotient identities. We therefore use it only to enumerate the
literal companion chart. Direct substitution into `(KBM3-2)` verifies

```text
c -> 1/c  and  b(c) -> 1/b(c).                  (KBM3-5)
```

For each of the four roots, the quotient replay separately reconstructs the
`OB` point with target root `r=1/b` and the `OI` point with target root `r=b`.
This gives eight literal records. Each fresh finite-field reconstruction
verifies both endpoint quadratics, the q-slice identity, and all fifteen
localizers.

It remains to apply a necessary full quotient identity. With `w=1/c` and
`d=-1`, the source data give

```text
P_J=(T-2)(T-1/2)(T-b)(T-b^-1)(T-c)(T-d),
K_5=(W-w)(W-z)(W-z^-1)(W-r)(W-d^-1),
chi_Omega=(W-r^-1)(W-d).
```

The colored quotient compiler forces `(KBM3-4)` for every actual packet.
Direct projective coefficient comparison gives `299` nonzero mismatches at
each of the eight literal points. Thus every point fails the first necessary
quotient norm; the second quotient identity is not needed. This proves the
complete affine `M03` direct block empty. QED.
