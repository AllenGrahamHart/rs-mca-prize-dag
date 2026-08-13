# Audit

- The split is on the unknown actual total core, not on its forced lower
  bound.  The two integer branches are exhaustive.
- The high-core branch bounds the original family immediately.  It does not
  add a line charge to previously removed-line charges.
- The fixed prefix through 65450 intentionally overcounts low explanations
  when `(CD1)` absorbs below 65451; this is safe.
- The low branch changes both the individual fill ceiling and the joint sum
  ceiling to `G_e`.  It retains every forced lower bound.
- The final line is omitted from the charge that forces it and included in
  the packing contradiction.
- At the adjacent row, threshold 14 gives total-core lower bound zero.
  Monotonicity prevents later thresholds from becoming positive-core
  thresholds.
- The primary verifier recomputes all weighted-prefix caps and line-bank
  guards.  The independent audit reconstructs the endpoint ledgers and exact
  rational charges without importing that implementation.
