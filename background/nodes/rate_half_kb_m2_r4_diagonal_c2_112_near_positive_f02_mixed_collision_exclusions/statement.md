# KoalaBear near-positive F02 mixed collision exclusions

- **status:** PROVED
- **scope:** the two affine positive near-aligned `F02` mixed-allocation
  orbit representatives over characteristic `p=2130706433`
- **dependencies:** the exact 30-cell residual registry and source-line
  q-slice gate
- **consumer:** source-line literal-assignment coverage

In the near-aligned chart, `q=(T-c)(T-d)` is the locator of the two
distinct `J_1` labels, so the ambient chart requires `c-d!=0`. For each of

```text
F02-A-RM,       F02-OB-RM,                         (KBF2M-1)
```

saturate the four exact q-slice equations by the ten reconstruction-generated
nonmonomial localizers and the torus units `b,c,d`. The resulting bases have
sizes `6,7`, and in both quotients the normal form of `c-d` is zero.
Consequently saturation by the required collision unit `c-d` gives the unit
ideal.

Independently, if `L` is the product of all fourteen factors (the ten
reconstruction factors and `b,c,d,c-d`), the two Rabinowitsch ideals

```text
<I, 1-yL> subset F_p[y,b,c,d]                     (KBF2M-2)
```

both have basis `[1]`. Hence both mixed cells are empty over the algebraic
closure and therefore over `F_(p^6)`. Together with the four square-orbit
exclusions, all six `F02` representatives are closed and the direct affine
frontier decreases from `26` to `24`.

This theorem does not classify any `F04`, `F06`, `M01`, or `M03` cell, and
does not cover projective-boundary or negative-sign branches.

## Falsifier

A point satisfying either cell's four equations with all fourteen factors
nonzero, a nonzero normal form of `c-d`, or a nonunit audited ideal.
