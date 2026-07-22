# Audit

- The theorem applies only when the circuit rows form a proper subset of the
  declared host core. A circuit considered without its host does not inherit
  the minimal-core proper-subset inequality.
- `Delta_J>=1` is strengthened by parity to `2` for four rows and remains `1`
  for five rows.
- The proper and full defect ranges differ by one integer charge. They are
  not overlapping estimates of the same ownership class.
- A defect type is forced only when `D_0<delta_t`. Baseline-positive proper
  circuits may have `C=0` and are not deleted.
- `(PC5)` uses only monotonicity of the block union when the host is enlarged;
  it is a necessary host-size floor, not an existence assertion.
- The parity branches in `(PC6)` are both load-bearing.
- No Modal or large local computation is used.
