# KoalaBear positive 433-1a common root-sign symmetry quotient

- **status:** PROVED
- **scope:** all 60 common matching/root-sign rows of the positive residual
  route `433-1a -> O0b`
- **dependencies:**
  `rate_half_kb_m2_r4_coordinate_coefficient_normal_form`,
  `rate_half_kb_m2_r4_coordinate_complete_fiber_vieta_compiler`,
  `rate_half_kb_m2_r4_coordinate_positive_433_1a_common_vieta_minor_compiler`,
  and
  `rate_half_kb_m2_r4_coordinate_positive_433_1a_cell58_complete_root_sign_orbit_exclusion`
- **consumer:** `rate_half_band_closure`

The source projectivities commuting with the normalized deck `X -> -X`
act exactly on the common root-sign rows.  If the loop `LC` lies in the
first complete source pair, as it does in cells `3,...,14`, then

```text
H(T,X) -> H(T,-X)          flips epsilon_1,
H(T,X) -> X^4H(T,-1/X)    flips epsilon_2.         (KBRSQ-1)
```

The loop is the canonical root-`1` anchor and has `q=0`, so its deck mate
represents the same loop record.  Hence all four sign rows of each such cell
form one exact orbit.

When `LC` is the singleton:

1. In cell `0`, transposing the two identical `AB+` roles and rescaling the
   source flips `epsilon_1`; source reciprocity `X -> 1/X` flips both signs.
   Thus its four rows form one orbit.
2. In cells `1,2`, source reciprocity flips both signs.  Transposing the two
   identical `AB+` roles exchanges the cells and swaps
   `(epsilon_1,epsilon_2)`.  Their eight rows therefore form exactly two
   orbits, distinguished by `epsilon_1 epsilon_2`.

Combining these source actions with the proved duplicate-role cell quotient

```text
[0] | [1,2] | [3,6] | [4,7] | [5,8] |
[9,10] | [11] | [12,13] | [14]                     (KBRSQ-2)
```

reduces the 60 raw rows to exactly ten algebraically distinct
matching/root-sign representatives:

```text
cell orbit [0]:      1 representative,
cell orbit [1,2]:    2 representatives,
each other orbit:    1 representative.             (KBRSQ-3)
```

The complete cell-5/8 theorem deletes one of these ten representatives, so
the positive common frontier has exactly nine unclosed symmetry
representatives.

This is an exact quotient, not a deletion of the other nine representatives,
the positive route, K3, a Prize row, LIST, or MCA.

## Falsifier

A common row outside the ten printed source-projectivity orbits, a source
projectivity that leaves the positive coefficient space or complete Vieta
system, or a second closed representative incorrectly identified with the
cell-5/8 orbit.
