# KoalaBear aligned-positive fixed balanced four-cell exclusion

- **status:** PROVED
- **field:** `F_p`, `p=2130706433`; hence every extension, including `F_(p^6)`
- **cells:** `F04-R11`, `F05-R11`, `F06-R11`, `F07-R11`
- **upstream source:** PR #1149 at
  `55ac3e07477bd7a768190a3e755f22b0d44354b0`

For each listed literal cell, let the first two q-slice rows be
`P=Aw^2+Bw+C` and `Q=Dw^2+Ew+F`, and put

```text
U=AF-CD,   V=AE-BD,   Z=BF-CE,   R=U^2-VZ.       (KBBR-1)
```

On `V!=0`, reconstruct `w=-U/V`, clear powers of `V` in the remaining
two rows, and invert `V` together with every transported named-open factor.
After exact factor cancellation the three retained equations have degrees
`12`, `43/44`, and `34`. Their deployed-prime ideal has a 151-element
Groebner basis. The square-free product of the transported unit factors
reduces to zero modulo that basis, so the generic chart is empty.

On `V=0`, factor `V` only after removing factors already inverted by the
original four-variable named-open chart. Exactly two factors remain in each
literal cell: one of degree 2 with 6 terms and one of degree 10 with 112
terms. For each of the eight literal factor branches, the ideal generated
by the four original q-slice rows and the selected factor has zero original
named localizer modulo its exact Groebner basis. Thus every rank-drop branch
is empty.

The two charts exhaust `V!=0` and `V=0`. Therefore all four literal balanced
fixed cells are empty.

## Nonclaims

This node does not close `R02`, `R20`, `M01-R11`, or `M02-R11`; it does not
move an owner or row ledger; and it does not infer emptiness from the
small-prime probes.
