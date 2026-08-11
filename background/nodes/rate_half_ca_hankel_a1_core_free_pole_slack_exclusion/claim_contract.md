# Claim contract

- **Claim:** a core-free `A=1` failure satisfying `(A1P3)` is impossible.
- **Dependencies:** the core-free contact section and the half-distance
  slope-slack ledger.
- **Output:** the pole-length lower bound `(A1P4)` and the three first-degree
  survivor chambers `(A1P5)`.
- **Consumer:** `rate_half_band_crossing_location`.
- **Nonclaim:** profiles failing `(A1P3)` and all fixed-core profiles remain
  open.
- **Falsifier:** pole colength above `O`, an interpolant containing the
  contact-active component in one piece of `(A1P2)`, nonvanishing of the
  surface cohomology in `(6)`, or an omitted first-degree chamber.
- **Replay:** run `verify.py` and `verify_audit.py` in this node directory
  under `tools/ramguard tiny --`.
