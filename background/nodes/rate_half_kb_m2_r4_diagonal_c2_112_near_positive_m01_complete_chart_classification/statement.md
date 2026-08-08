# KoalaBear near-positive M01 complete-chart and quotient exclusions

- **status:** PROVED
- **scope:** the six affine positive near-aligned `M01` direct q-slice
  representatives and their exact `M01/M02`, `A/TA` transport companions
  over characteristic `p=2130706433`
- **dependencies:** the direct residual registry, literal inversion transport,
  q-slice gate, and colored quotient compiler
- **consumer:** source-line literal-assignment coverage

Five cells in

```text
{M01-A,M01-OB} x {RX,RL,RM}                     (KBM1-1)
```

have unit complete-chart ideals after localization by their eleven recorded
reconstruction factors and `b,c,d,c-d`. Sequential saturation and independent
one-step Rabinowitsch ideals agree.

The sole nonunit cell is `M01-A-RL`. Its exact localized lex basis is

```text
b^2 + 253153238*b - 400825962,
c + 1065353216,
d + 1.                                           (KBM1-2)
```

The quadratic in `(KBM1-2)` splits over `F_p` at

```text
b=1790190462, 87362733.                          (KBM1-3)
```

Thus the direct chart has exactly two base-field points. Exact q-slice
transport gives eight literal points after including `M02` and the `TA`
target companion. Each literal point is replayed independently: all four
endpoint equations hold and all fifteen chart localizers are nonzero.

For each point reconstruct `H=U+XV`, put `G=U^2-WV^2`, and test the first
necessary normed colored-quotient identity

```text
Res_T(P_J,G) ~ K_5^4 chi_Omega^2.                (KBM1-4)
```

All eight points fail `(KBM1-4)`. Hence no literal point satisfies the full
colored quotient system. The complete `M01/M02` direct-orbit block is empty,
and the affine near-positive frontier decreases from `12` to `6`.

This theorem does not classify `M03`, projective-boundary, or negative-sign
branches.

## Falsifier

A further complete-chart point, a companion absent from the eight-point
replay, or a point satisfying `(KBM1-4)`.
