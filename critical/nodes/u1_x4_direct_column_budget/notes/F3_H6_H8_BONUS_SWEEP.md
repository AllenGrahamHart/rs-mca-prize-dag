# F3 h=6/7/8 bonus sweep status

Status: VERIFIED-AT-ROWS + HONEST H8 PARTIAL.  This is bonus item (ii) after
Terminals A/B/C: sweep `h = 6,7,8` with the ladder machinery.

No new heavy computation is claimed here.  The pass consolidates the existing
Modal artifacts into a replayed status ledger and separates full certificates
from partial slices.

## Pre-registration

Success criterion for this pass:

- verify every existing full h=6/h=7 boundary/smooth row has zero anchored
  nontoral trades and no `n^3` alarm;
- verify the h=8 rows are present but marked partial, with no alarm in the
  checked slices;
- state the next h=8 action without promoting partial evidence.

Failure criterion:

- if any full h=6/h=7 row has nonzero primitive residue or an `n^3` alarm, the
  sweep has found a bonus counterexample;
- if any h=8 row is silently treated as full when it is partial, the handoff is
  invalid.

## Verified Rows

From `f3a1_results.json`:

```text
boundary_n32_h6_p1153_FULL  zero, full
boundary_n32_h7_p1153_FULL  zero, full
boundary_n32_h6_p3137       zero, full
boundary_n32_h7_p3137       zero, full
boundary_n32_h6_p12289      zero, full
```

From `f3a2_results.json`:

```text
smooth_n32_h6_p40961        zero, full
smooth_n32_h7_p40961        zero, full
smooth_n32_h6_p61441        zero, full
smooth_n32_h7_p61441        zero, full
smooth_n32_h6_p65537        zero, full
smooth_n32_h7_p65537        zero, full
```

Existing h=8 rows:

```text
boundary_n32_h8_p1153_FULL  zero in checked slice, partial=True
boundary_n64_h8_p193        zero in checked slice, partial=True
q3_n64_h8                   zero in checked slice, partial=True
```

The h=8 evidence is useful but not a certificate.

## Interpretation

The h=6/h=7 rows continue the pattern from the shallow ladder: no primitive
residue appears in the q>=n^2 boundary/smooth tests.  The h=8 rows do not yet
meet the same standard because the runs were sliced by the 60-second Modal
budget.

Next h=8 action:

```text
replace the partial W-window runs by shard-complete anchor certificates, or use
the x83 square-shift certifier keys to reduce h=8 to explicit norm-gate keys.
```

## Replay

```bash
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h6_h8_bonus_sweep_replay.py
```

Expected digest:

```text
H6_H8_BONUS_SWEEP_PASS
```

