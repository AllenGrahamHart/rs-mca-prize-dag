# Lineage

- The pairing-7 FLINT function-field backend supplies the exact
  quadratic-over-cubic arithmetic and exceptional-root lift.
- Pairing 8 moves the second quadratic cut from `paired(second_de,bf)` to
  `paired(second_de,sigma_c c f)` and leaves `paired(df,bf)` for the
  terminal check.
- Both target signs are fixed in each exact source row.
- No target-label exchange is used: that map sends source role cell 3 to
  duplicate cell 6 and does not close a within-cell matching.
- The direct six-basis norm is independently checked against the
  quadratic-over-cubic tower norm.
- Exact parallel-edge transport adds the second positive `DE` deletion.
