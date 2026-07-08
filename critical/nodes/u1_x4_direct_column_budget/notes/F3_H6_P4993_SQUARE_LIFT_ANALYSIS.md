# F3 h=6 p4993 square-lift classification

Status: MACHINE-VERIFIED ROW CLASSIFICATION.

This note repairs the first reading of the `n=64,h=6,p=4993` extra-prime row.
The row has six anchored "nontoral" trades under the coarse toral-only
classifier, but all six are paid square-shift pullbacks.

## Pre-registration

Object:

```text
n = 64, h = 6, p = 4993,
the six witnesses in f3_h6_n64_extra_primes_certificate.json.
```

Test:

- decode every witness mask;
- verify each side is an antipodal support `A union (A+32)`;
- descend by the square map `mu_64 -> mu_32`;
- verify the descended 3-subsets have equal `e1,e2` and unequal product in
  `F_4993`;
- independently enumerate every anchored h=3 trade on `mu_32` at `p=4993`;
- require the descended witness set to equal that complete h=3 enumeration.

Failure criterion: any witness that is not an antipodal square-lift is a genuine
new h=6 residue for this row.

## Result

Replay:

```bash
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h6_p4993_square_lift_analysis.py
```

Expected digest:

```text
H6_P4993_SQUARE_LIFT_ANALYSIS_PASS
```

The verifier reports:

```text
h=3 n32 p4993 anchored trades: 6
h=6 n64 p4993 witnesses: 6
all h=6 p4993 witnesses are antipodal square-lifts of h=3 quotient trades
H6_P4993_SQUARE_LIFT_ANALYSIS_PASS
```

## Interpretation

The `p=4993` row is a falsifier for the crude anchored-nontoral emptiness
heuristic, not for the fully stripped primitive h=6 column.  After the
square-shift/pullback strip, this row contributes no unclassified h=6 residue.
The live h=6 target should therefore explicitly separate:

```text
paid square-lifts of h=3 norm-gate accidents
versus
genuinely primitive h=6 norm-gate accidents.
```

This mirrors the h=4 tail story in `F3_SHALLOW_LADDER.md`: the probe's
toral-only "nontoral" column is intentionally conservative and can overcount
paid pullback structure.
