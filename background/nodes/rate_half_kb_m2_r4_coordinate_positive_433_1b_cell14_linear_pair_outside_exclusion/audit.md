# Audit

- The claim is a 144-case route cut, not complete cell-14 exclusion.
- Open fibers and every factor of the `gcd(L_0,L_1)` boundary are separate;
  no generic-fiber conclusion is extended across an untested boundary.
- Only route factors already excluded by the guarded cell-14 structure are
  stripped.
- Missing roles `y_0,y_1` are computed separately even though their generated
  programs agree exactly.
- The one timeout is retained in the raw ledger and replaced only by a replay
  with identical definition and complete-program hashes.
- All arithmetic is exact over `F_2130706433`; no sampled prime or floating
  computation is used.
