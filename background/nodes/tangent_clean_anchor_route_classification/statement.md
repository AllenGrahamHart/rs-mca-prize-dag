# Tangent clean-anchor route classification

- **status:** PROVED
- **closure:** proof plus exact arithmetic

At target `2^-128`, put `B*=floor(q/2^128)`. For an integer agreement
`a`, the tangent supplier uses

```text
e = n-a
```

distinct certified slopes. This guaranteed payload clears the unsafe budget
exactly when

```text
e > B*,
```

or equivalently

```text
q <= q_tan_max := e*2^128-1.
```

At the six clean candidate predecessors, the exact cutoffs are:

| row | rate | `a` | `e=n-a` | `q_tan_max` | bits |
|---|---:|---:|---:|---:|---:|
| RowC | `1/4` | `260` | `764` | `259975728327596986086018200077870913552383` | `138` |
| RowC | `1/8` | `132` | `892` | `303531871293477109409330149829137244618751` | `138` |
| RowC | `1/16` | `66` | `958` | `325990507510259047997912873919633946574847` | `138` |
| prize | `1/4` | `558345748480` | `1640677507072` | `558293625460404914753807606097620113508566231416831` | `169` |
| prize | `1/8` | `283467841536` | `1915555414016` | `651829730249582701518843435391462226766545914167295` | `169` |
| prize | `1/16` | `141733920768` | `2057289334784` | `700059284281502497819565034871099566415191688085503` | `169` |

Thus the tangent theorem pays every instance of these predecessor formulas
whose actual field order lies at or below its printed cutoff. Its guaranteed
`e`-slope payload pays none of the six named envelope anchors: RowC fixes
`B*=2^122`, and the prize envelope fixes

```text
B* = 317494674775468773183020924238786383963,
```

both much larger than the corresponding `e`.

This is an exact low-field branch and an exact applicability cut for this
guaranteed payload. Failure of the tangent inequality is not safety, does not
upper-bound the full bad set of the constructed line, and does not refute
quotient, direct-value, or averaged-occupancy suppliers.
