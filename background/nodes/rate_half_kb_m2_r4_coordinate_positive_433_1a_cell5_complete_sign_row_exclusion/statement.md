# KoalaBear positive 433-1a cell-5 complete sign-row exclusion

- **status:** PROVED
- **scope:** every deployed `t`, cell 5, signs `(-1,-1)`
- **consumer:** `rate_half_band_closure`

The generic colored exclusion proves the cell-5 sign row empty outside an
explicit 69-value exceptional router.  Three pairwise-disjoint proved finite
packets exclude respectively 23, 38, and eight values, and their union is
exactly that router.  Therefore no admissible deployed-field
`DE+/DE-/BE` packet exists in cell 5 with signs `(-1,-1)` for any admissible
`t`.

This closes one complete sign row.  It does not treat another common sign
row or matching cell, delete cell 5 or `433-1a -> O0b`, close K3, a Prize
row, LIST, or MCA.

## Falsifier

A deployed value outside the generic-plus-finite partition or an admissible
packet in any covered fiber.
