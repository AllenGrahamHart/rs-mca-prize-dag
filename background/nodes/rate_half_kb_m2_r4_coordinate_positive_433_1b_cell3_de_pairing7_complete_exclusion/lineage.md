# Lineage

- The pairing-4/5 FLINT function-field backend supplies the exact
  quadratic-over-cubic arithmetic and exceptional-root lift.
- Pairing 7 exchanges the auxiliary role from `u=df` to `u=ef`, moves
  the fixed lane sign to `paired(de,sigma_o u)`, and leaves
  `paired(df,sigma_c c f)` for the terminal check.
- No target-label exchange is used: that map sends source role cell 3 to
  duplicate cell 6 and does not close a within-cell matching.
- The direct six-basis norm is independently checked against the
  quadratic-over-cubic tower norm.
- Norm work is shared across the two `sigma_c` lanes at fixed `sigma_o`.
- Exact parallel-edge transport adds the second positive `DE` deletion.
