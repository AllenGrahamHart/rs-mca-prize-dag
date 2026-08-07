# KoalaBear aligned-positive fixed-companion inversion transport

- **status:** PROVED
- **scope:** the complete aligned-positive unramified `F00/F01` systems for
  all three root distributions over `F_(2130706433^6)`
- **dependencies:** the aligned-positive literal-cell crosswalk, the three
  canonical fixed-moving exclusions, and the colored quotient compiler
- **consumer:** source-line literal-assignment coverage

In the literal registry

```text
v0=2, v1=1/2, v2=b, v3=b^-1,
F00={E01,E02},       F01={E01,E03},
```

one has the identity of complete parameterized systems

```text
F01(b)-Rxx = F00(b^-1)-Rxx                         (KBFI-1)
```

for each `Rxx` in `{R02,R11,R20}`. This is not a generic endpoint Mobius
transport. It is the literal reparameterization `b -> b^-1`: the unordered
set `J_0` is unchanged, the selected source edges become exactly those of
`F01`, and `q`, `w`, the root-distribution target, the named open, and both
full quotient identities are unchanged.

Inversion is a bijection on the nonzero deployed field. Therefore the three
proved `F00` exclusions imply

```text
F01-R02 = empty,       F01-R11 = empty,
F01-R20 = empty.                                     (KBFI-2)
```

Together with the canonical leaves this closes the six literal
`{F00,F01} x {R02,R11,R20}` cells. No other fixed-moving or moving-moving
assignment is transported.

## Falsifier

A nonzero `b` for which `F00(b^-1)` and `F01(b)` select different source
edges, a target/localizer/full-quotient datum that depends on the orientation
of the unordered pair `{b,b^-1}`, or a survivor in an `F01` cell whose
inverse parameter is excluded in the corresponding `F00` cell.
