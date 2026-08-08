# KoalaBear near-positive M03 complete-chart and quotient exclusions

- **status:** PROVED
- **scope:** the six affine positive near-aligned `M03` direct q-slice
  representatives and all literal companions of the surviving chart over
  characteristic `p=2130706433`
- **dependencies:** the direct residual registry, literal inversion transport,
  q-slice gate, and colored quotient compiler
- **consumer:** source-line literal-assignment coverage

Five cells in

```text
{M03-A,M03-OB} x {RX,RL,RM}                     (KBM3-1)
```

have unit complete-chart ideals after localization by their eleven recorded
reconstruction factors and `b,c,d,c-d`. Sequential saturation and independent
one-step Rabinowitsch ideals agree.

The sole nonunit cell is `M03-OB-RL`. Its exact localized lex basis is

```text
b + c^3 + 819502469*c^2 - 327800980*c + 819502469,
c^4 + 819502469*c^3 - 327800980*c^2 + 819502469*c + 1,
d + 1.                                           (KBM3-2)
```

The quartic in `(KBM3-2)` factors over `F_p` as

```text
(c^2 + 148474327*c + 1)(c^2 + 671028142*c + 1). (KBM3-3)
```

Both factors are irreducible quadratics. Hence the direct chart has exactly
four points over `F_(p^2)`, and all four occur over the deployed `F_(p^6)`.

The assignment is fixed by simultaneous inversion, which exchanges roots by
`c -> 1/c` and `b -> 1/b`; this is checked directly on `(KBM3-2)`. Full
quotient covariance is not assumed. Instead, all four `OB` points and all four
literal `OI` companions are reconstructed and replayed independently. Every
point satisfies both endpoint equations and all fifteen chart localizers.

For target root `r=1/b` on `OB` and `r=b` on `OI`, reconstruct `H=U+XV`, put
`G=U^2-WV^2`, and test the first necessary normed colored-quotient identity

```text
Res_T(P_J,G) ~ K_5^4 chi_Omega^2.                (KBM3-4)
```

All eight literal points fail `(KBM3-4)`. Thus the complete affine `M03`
direct block is empty, and the affine near-positive frontier decreases from
`6` to `0`.

This theorem does not classify near-positive projective-boundary or either
negative-sign branch.

## Falsifier

A further complete-chart point, failure of the inversion closure check, a
literal companion absent from the eight-point replay, or a point satisfying
`(KBM3-4)`.
