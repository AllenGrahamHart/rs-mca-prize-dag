# proof: f_descent_termination (auto-discharged)

The conditional implication (see conditional.md) is proved and every predicate is now green:

- `f_sparse_descent_step` [PROVED]
- `f_support_lattice` [PROVED]
- `f_termination_mds` [PROVED]
- `f_termination_hankel` [PROVED]
- `f_spread_moment_count` [PROVED]

By modus ponens the statement is PROVED. Auto-discharged by tools/auto_discharge.py; the audit lives at the red->amber referee step.
