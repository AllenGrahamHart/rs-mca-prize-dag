# Claim contract

- **Claim:** the `e = m` stratum at `m = 2` is NONEMPTY: `(4m+1) x 4m`
  syndrome Hankel pencils exist with minimal index exactly 2, generic rank
  7, `s = 0`, `delta = 1` and independent `Q_0, Q_1, Q_2` — twelve
  certified over five prime fields, the published `q = 97` object replayed
  from scratch by both verifiers.
- **Dependencies:** the (RNC2) separation requirement (cited); elementary
  Hankel/polynomial algebra.
- **Output:** the emptiness route to the strict endpoint is dead at
  `m = 2` constructively; the honest existence count (`11m-4`, positive at
  every `m`); the excess-component correction (planted common roots,
  dimension 21); the `T = 0` structural observation (a pencil buys nothing
  at the splitting layer).
- **Consumer:** `rate_half_band_crossing_location`.
- **Nonclaims:** no `m >= 3` witness; no large-`q` or characteristic-0
  statement; (SAT2)-(SAT5) not verified (vacuous at `T = 0`); the (D-F)
  squareness is an `m = 2` accident; no contradiction with the PROVED
  pole-interpolation exclusion (the witness is outside its hypotheses on
  both counts).
- **Falsifier:** failure of any certificate check on replay (E1/E2,
  degrees, `s = 0`, pencil blocks, nullity 1, generic rank 7, single drop,
  no deg<=1 kernel).
- **Replay:** `tools/ramguard local -- python3
  background/nodes/rate_half_l2_stratum_nonempty_at_m_two/verify.py` and
  the coordinator's from-scratch audit `verify_audit.py` (tiny).
