# Claim contract

- **Claim:** the sole macroscopic-floor equality branch has exactly three
  center-line slopes and at least `2e` off-line slopes producing exact RS
  minimum words by affine second difference.
- **Inputs:** the macroscopic pair floor and feasibility bounds, exact light
  incidence, packet deficit `e-6`, affine received/codeword geometry, and RS
  minimum distance.
- **Outputs:** dichotomy `(ETR1)--(ETR3)`, exact excess sum `(ETR5)`, and the
  minimum-word family `(ETR6)--(ETR7)`.
- **Falsifier:** an equality pair with line size other than three, an
  off-line excess sum different from `e`, or a zero/non-minimum second
  difference at `a_delta=0`.
- **Nonclaims:** the minimum words are not asserted distinct or contained in
  a low-dimensional pencil, and the extremal branch is not excluded.
