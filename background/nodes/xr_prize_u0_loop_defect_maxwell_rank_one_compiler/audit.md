# Audit

- Exceptional slopes are deleted before puncturing; at most one slope is
  charged to each root of `G\P_0`.
- The retained block size and pair cap are `a+h+v` and `a+v`, not their
  uniform-cell values.
- The dense-core coefficient remains `h`; the parity-row count is `h+v`.
  Their difference is exactly the `v(t-2)` term in `(LC3)`.
- Rank one is not discarded. It is the new common-support stratum
  `a+1<=|S|<=a+v` and is classified in both directions.
- The official intervals are necessary ranges only and are not asserted to
  contain realized cells.
- No Modal or large local computation is used.
