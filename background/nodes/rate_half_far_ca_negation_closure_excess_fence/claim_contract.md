# Claim contract

- **Claim:** on a negation-closed domain with `e_1 = x^2 e_0`, an even
  locator covering the orbits missed by a one-sided support collapses every
  odd-index Hankel row exactly, leaving `ceil(rho/2)` conditions on the one
  unknown slope; hence at `rho = 2` every covering even locator yields a bad
  slope (`C(m-off, r/2-off)` of them, `off = m-(r+1)`), at `rho >= 3`
  generically none, and at razor (`M = 2`, `rho = 2^34`) the carrier is
  over-determined by exactly `2^33 - 1` conditions.
- **Dependencies:** elementary Lagrange/residue identities on point
  evaluations; the banked e22 orbit-invariant locator algebra (carrier
  form); banked cell data from round-36 bank 3.
- **Output:** the (NCE) mechanism, the corrected general count (CNT), the
  MISS-2 locator-vs-slope distinction at H3, and the (KILL) rho-threshold
  fence — plus the warning that first-moment counting on structured domains
  is unsound at small rho.
- **Consumer:** the far-CA lane inside `rate_half_band_crossing_location`.
- **Nonclaims:** no total-T census at `rho >= 3`; no characteristic-2
  claim; no razor-scale measurement; the `rho >= 3` zero-count is generic
  in `q`, not field-uniform (exhibited accident at `q = 1009` on record).
- **Falsifier:** an odd-index row failing to collapse on a covering even
  locator; a rho = 2 covering locator without a bad slope; a covering count
  differing from (CNT); or a carrier evading the `ceil(rho/M)` count at
  razor.
- **Replay:** `tools/ramguard local -- python3
  background/nodes/rate_half_far_ca_negation_closure_excess_fence/verify.py`
  and the independent direct-functional audit `verify_audit.py` (tiny).
