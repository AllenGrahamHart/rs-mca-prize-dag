# F3 h=8 n=64 square-lift probe

Status: MACHINE-VERIFIED STRUCTURAL PROBE, NOT A FULL H8 CERTIFICATE.

The remaining h=8 n=64 rows are too large for the current all-left hash
certificate under the light-compute rule.  This probe checks the first structural
branch instead: antipodal h=8 supports on `mu_64` descend under the square map
to h=4 supports on `mu_32`.

## Pre-registration

Question:

```text
For the existing h=8 n=64 partial rows, does the antipodal square-lift branch
already reduce to paid h=4 quotient structure?
```

Test:

- enumerate every anchored h=4 trade on `mu_32` at the relevant primes;
- split the quotient trades into toral versus nontoral under the h=4 toral
  classifier;
- interpret antipodal h=8 square-lifts as paid if the quotient branch is toral
  or otherwise already handled by the h=4 pullback/norm-gate ledger.

This does not count non-antipodal primitive h=8 trades.

## Replay

```bash
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h8_n64_square_lift_probe.py
```

Expected digest:

```text
H8_N64_SQUARE_LIFT_PROBE_PASS
```

## Result

```text
p=193 h4 quotient anchored trades: total=15 toral=7 nontoral=8
p=262337 h4 quotient anchored trades: total=7 toral=7 nontoral=0
p=4289 h4 quotient anchored trades: total=7 toral=7 nontoral=0
H8_N64_SQUARE_LIFT_PROBE_PASS
```

Interpretation:

- The low-field `p=193` h=8 partial row sits below the `q >= n^2` boundary and
  has a real nontoral h=4 quotient branch, so it should remain a low-row
  diagnostic rather than boundary evidence.
- The `q3_n64_h8` row uses `p=262337`; its antipodal square-lift branch has no
  h=4 nontoral quotient residue.  Any remaining h=8 obstruction at that row
  must therefore be non-antipodal primitive structure or a different paid
  quotient branch.
- The h=7 boundary prime `p=4289` gives the same clean h=4 quotient result,
  matching the newly completed h=7 n64 certificate.

Next h=8 work should target the non-antipodal primitive branch through x83
obstruction keys or a true external/sharded join.  This probe does not promote
the h=8 n64 partial rows to full certificates.
