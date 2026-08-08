# KoalaBear near-positive F04 complete-chart exclusions

- **status:** PROVED
- **scope:** the six affine positive near-aligned `F04` q-slice orbit
  representatives over characteristic `p=2130706433`
- **dependencies:** the exact 30-cell residual registry and source-line
  q-slice gate
- **consumer:** source-line literal-assignment coverage

For every cell in

```text
{F04-A,F04-OB} x {RX,RL,RM},                    (KBF4-1)
```

let `I` be its four exact q-slice equations. Localize `I` by all twelve
reconstruction-generated nonmonomial factors and the inherited chart units

```text
b, c, d, c-d.                                  (KBF4-2)
```

Sequential exact saturation over `F_p[b,c,d]` gives the unit ideal in all
six cases. Independently, if `L` is the product of the sixteen factors in
`(KBF4-2)`, every one-step Rabinowitsch ideal

```text
<I, 1-yL> subset F_p[y,b,c,d]                   (KBF4-3)
```

has basis `[1]`. Hence all six cells are empty over the algebraic closure
and therefore over `F_(p^6)`. Through the already proved literal inversion
quotient, this closes the complete `F04/F05` direct-orbit block. The affine
near-positive frontier decreases from `24` to `18` representatives.

This theorem does not classify any `F06`, `M01`, or `M03` representative,
and does not cover projective-boundary or negative-sign branches.

## Falsifier

An admissible point satisfying one of the six systems with all sixteen
factors nonzero, or a nonunit basis in either exact proof path.
