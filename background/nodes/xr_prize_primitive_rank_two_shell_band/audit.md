# Audit

- The cancellation in `(PB1)` uses `N=R+a`; retaining `a` in the core-size
  bound would hide the decisive row-only constant.
- The lower bound uses `Z<=td`. It is valid on every shell but may be weaker
  than the disjoint-union cap `Z<=a+d+1`.
- Concavity, not monotonicity in `t`, reduces the check to `t=4,L_max`.
- The negative values at `D_row+1` show only that this lower-bound argument
  stops. They are not counterexamples.
- The conclusion concerns a relation active on every block of the minimal
  Maxwell core. Proper local circuits survive and require ownership.
