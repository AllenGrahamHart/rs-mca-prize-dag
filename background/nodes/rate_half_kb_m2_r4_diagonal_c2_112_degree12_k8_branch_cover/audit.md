# Audit

- Modal app `ap-C9PO1BEv6lx1ZBmeNNX5fO` ran all eight literal branches in
  parallel with eight passes and no timeout or remote error.
- Jobs completed in `30.0`--`56.8` seconds at at most `0.39 GB` peak child
  RSS.
- The first replay exposed a false instrumentation assertion that every A0
  core had degree 37. Literal factorization gives degree 38 in F05 and F07;
  the assertion was removed and the exact products were replayed. No theorem
  had depended on the failed run.
- Every `K10=0` residual deliberately omits the quartic cores, proving
  emptiness of a superset rather than cancelling a zero leading coefficient.
- Every source pseudo-remainder identity is asserted before factor stripping.
- The original two-job `F04-R02` output remains as an independent replay and
  has the same basis hashes as the all-cell run.
