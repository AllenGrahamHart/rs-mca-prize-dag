# Audit

Date: 2026-07-27.

The row table is pinned to
`critical/nodes/xr_smallcore_spread_count/notes/audit_consumption_replay_20260710.py`.
The theorem sources are the local proved statements `fm1` and
`averaged_slope_conversion`; hashes are recorded in `source_pin.json`.

The proof deliberately avoids computing any prize-scale binomial integer. The
three prize comparisons use exact fifth-power rational bounds and integer
exponent inequalities. The three RowC binomials are evaluated exactly. A
separate small-parameter replay checks the geometric mixed-size tail.

The conclusion is stronger than an overlap-profile failure: the uncorrected
first moment itself is below budget. It remains only a route cut; direct
received lines can be highly non-average and are not constrained.
