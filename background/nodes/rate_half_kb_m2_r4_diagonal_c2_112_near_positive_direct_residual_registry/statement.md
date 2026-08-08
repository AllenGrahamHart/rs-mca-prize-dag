# KoalaBear near-positive 30-cell direct residual registry

- **status:** PROVED
- **scope:** the residual affine positive near-aligned literal q-slice frontier
- **dependency:** the exact near-positive literal inversion transport
- **consumer:** source-line literal-assignment coverage

The residual orbit representatives are exactly

```text
{F02,F04,F06,M01,M03} x {A,OB} x {RX,RL,RM}.     (KBDR-1)
```

Here `A` represents the `{A,TA}` target orbit and `OB` represents the
semantic `other` orbit. For each cell, reconstruct the positive source form
over `QQ(b,c,d)`, form the two residual quadratics, and impose projective
equality with the two printed monic target quadratics. Clearing recorded
denominators gives exactly four nonzero equations.

The compiled registry has

```text
cells                    30
equations               120
registry SHA-256         2607f88572c63091b06a1c35dd55c80a3e4f10daff2fb3423f5bb8c03f0f116e
maximum total degree     30
maximum term count       1098
four-equation gcd        1 in every cell.         (KBDR-2)
```

Every cell also records the complete radical factor set of its reconstruction
and q-slice named open. There are 10 localizer factors for `F02`, 12 for
`F04/F06`, and 11 for `M01/M03`.

This theorem is only an exact compiler and disjoint census. It does not
assert that any cell is empty or nonempty, and it does not cover projective
or negative-sign branches.

## Falsifier

A residual orbit absent from `(KBDR-1)`, a duplicate cell, a zero or wrongly
cleared equation, a fingerprint mismatch, or an omitted named-open factor.
