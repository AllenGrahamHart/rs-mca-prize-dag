# Audit

- `(UE1)` is the exact minimum over all fiber profiles with cap `ell`; it is
  not merely the sequential avoidance lower bound.
- The official envelope deliberately uses the weaker product bound because
  it permits a factorwise comparison with the already audited `ell=1` row.
- The shifted variable is `y=x+(s-1)(ell-1)`, not `x+(s-1)ell`. The former
  recovers `y=x` when `ell=1`.
- The actual defect ceiling is `e<=d-ell-1=x-2ell-1`.
- Positivity of every denominator is checked through the smallest `j=s`
  factor; it also proves `r>s ell`.
- Tuples outside `(UE2)` may still be paid by `(UE1)` or by another residual
  dimension. They must not be labeled counterexamples.
