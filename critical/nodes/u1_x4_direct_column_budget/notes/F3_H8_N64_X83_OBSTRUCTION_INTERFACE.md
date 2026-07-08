# F3 h=8 n=64 x83 obstruction interface

Status: MACHINE-VERIFIED STRUCTURAL INTERFACE, NOT A FULL H8 CERTIFICATE.

The remaining `h=8,n=64` rows cannot be promoted by a blind all-left hash run
under the light-compute rule.  This packet banks the next x83-facing interface:
given a 16-point support `R`, compute the forced degree-8 square root candidate
from the top nine coefficients of the locator `L_R`, then use the seven low
coefficients of `S^2 - L_R` as obstruction keys.

## Pre-registration

Question:

```text
Does the existing x83 forced-root obstruction interface recognize the paid
antipodal square-lift branch for the h=8,n=64 rows, and does it give a concrete
non-antipodal key suitable for later sharded certification?
```

Success criteria:

- every h=4 quotient trade from the square-lift probe, lifted antipodally to
  `mu_64`, has all seven x83 obstructions zero and nonzero square `lambda`;
- the h=8 first-obstruction sensitivity check holds: changing only the
  `X^7` coefficient of the 16-support locator leaves the forced root unchanged
  and changes the top obstruction by `-1`;
- deterministic non-antipodal support samples at the two boundary-style primes
  have no full x83 zero vector.

Failure criteria:

- any paid antipodal lift has a nonzero obstruction, which would mean the
  interface is misaligned with the already-banked square-lift branch;
- any sampled non-antipodal support has all obstructions zero with square
  `lambda`, which would be a concrete h=8 candidate to isolate and charge.

## Replay

```bash
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h8_n64_x83_obstruction_interface.py
```

Expected digest:

```text
H8_N64_X83_INTERFACE_PASS
```

## Result

The replay reports:

```text
p=193 lifted h8 branch: total=15 toral=7 x83_zero=15
p=4289 lifted h8 branch: total=7 toral=7 x83_zero=7
p=262337 lifted h8 branch: total=7 toral=7 x83_zero=7
p=4289 nonantipodal x83 sample: samples=4096 full_zero=0 first_obstruction_zero=2
p=262337 nonantipodal x83 sample: samples=4096 full_zero=0 first_obstruction_zero=0
H8_N64_X83_INTERFACE_PASS
```

Interpretation:

- The paid antipodal h=8 branch is exactly aligned with the x83 obstruction
  gate.  At `p=262337`, the `q3_n64_h8` antipodal branch has only the seven
  toral h=4 quotient lifts and all are x83-zero as expected.
- The low diagnostic row `p=193` also has eight nontoral h=4 quotient lifts.
  They are x83-zero because they are genuine lifted h=4 quotient trades, but
  this row remains below the `q >= n^2` boundary and is not a boundary
  certificate.
- The non-antipodal sample is evidence only.  It does not rule out a
  non-antipodal primitive h=8 branch, but it gives the exact key format for a
  future sharded certifier: enumerate candidate 16-supports, bucket by the
  seven obstruction coordinates plus the square/nonzero `lambda` predicate,
  and only send full-zero candidates to the expensive trade/pair decoder.

Next h=8 work:

```text
Use this x83 key as the front-end for a true sharded non-antipodal support
certifier.  Do not promote the two h=8 n=64 partial rows until such a certifier
has either enumerated the non-antipodal branch or isolated every full-zero
support as a paid quotient/norm-gate event.
```
