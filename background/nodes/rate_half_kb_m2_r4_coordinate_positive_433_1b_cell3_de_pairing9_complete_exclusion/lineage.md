# Lineage

- The pairing-4 FLINT function-field backend supplies the exact
  quadratic-over-cubic arithmetic and exceptional-root lift.
- Pairing 9 exchanges the two residual `DE` inputs in pairing 4's first
  quadratic cuts: `P_u=paired(second_de,df)` and
  `P_f=paired(de,bf)`.
- The terminal check remains `paired(sigma_o ef,sigma_c cf)` in all four
  target lanes.
- No target-label exchange is used: that map sends source role cell 3 to
  duplicate cell 6 and does not close a within-cell matching.
- The direct six-basis norm is independently checked against the
  quadratic-over-cubic tower norm.
- Exact parallel-edge transport adds the second positive `DE` deletion.
