# Proof

Reconstruct the six systems in `(KBM1-1)` with the pinned generic `5 x 5`
source solver. Reduce modulo `p` and sequentially saturate each four-equation
ideal by its eleven reconstruction factors and by `b,c,d,c-d`. Five ideals
become unit. Independent ideals `<I,1-yL>`, with `L` the complete product of
fifteen factors, give the same five unit classifications and retain only
`M01-A-RL`.

The surviving complete-chart ideal is zero-dimensional. Exact lex conversion
gives `(KBM1-2)`, with basis SHA-256

```text
340df1fa9c7cc15843f8d6043df5c70f27d8757c0e398ce620973ddcdc5cc1dd.
```

Here `c=1065353217=1/2` and `d=-1` in `F_p`. The first polynomial splits at
the two values in `(KBM1-3)`, so these are all direct q-slice points.

The literal inversion theorem is exact for q-slices and localizers, but not
for full quotient identities. We therefore use it only to enumerate the
companions and replay every companion directly. The eight records are

```text
M01-A:   b=1790190462, 87362733
M02-A:   b=1905873591, 683754230
M01-TA:  b=1790190462, 87362733
M02-TA:  b=1905873591, 683754230.
```

For `A`, use `c=1/2`; for `TA`, use `c=2`; in both cases `d=-1` and
`w=1/c`. Each fresh finite-field reconstruction verifies both endpoint
quadratics and all fifteen localizers.

It remains to apply a necessary full quotient identity. Let `r` be the
q-slice target root, namely `1/2` for `A` and `2` for `TA`. The source data
give

```text
P_J=(T-2)(T-1/2)(T-b)(T-b^-1)(T-c)(T-d),
K_5=(W-w)(W-z)(W-z^-1)(W-r)(W-d^-1),
chi_Omega=(W-r^-1)(W-d).
```

The colored quotient compiler forces `(KBM1-4)` for every actual packet.
After replaying the q-slice identity as a control, direct projective
coefficient comparison gives `299` nonzero mismatches at each of the eight
literal points. Thus every point fails the first necessary quotient norm;
the second quotient identity is not needed. This proves the block empty.
QED.
