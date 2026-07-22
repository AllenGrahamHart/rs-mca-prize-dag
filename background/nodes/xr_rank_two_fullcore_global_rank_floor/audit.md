# Audit

- The strict `+1` in `(GF2)` and `(GF3)` is load-bearing: `D_0<0` is a strict
  integer inequality, not `D_0<=0`.
- The pair-mass term `M_t(D)` is retained even when it exceeds the baseline
  floor. It dominates many high-arity RowC cells.
- The pair-mass floor makes `Z-D` dominate the otherwise independent shell
  requirements `D` and `t-2`; retaining a three-term maximum is harmless but
  obscures this simplification.
- Prize minimization uses the exact core caps `384,448,960`; RowC uses only
  `t<=k+2` and does not import a prize-only cap.
- The prize `1/16` minimizer is `t=958`, not the endpoint `960`.
- The table is an exact necessary arithmetic floor. It is not an existence
  theorem for any displayed minimizer.
- Proper four/five-block circuits inside larger cores are outside scope
  because they need not have `Delta=-e<=0` on their own selected rows.
- No Modal or large local computation is used; the official sweep has fewer
  than one thousand arities per row.
