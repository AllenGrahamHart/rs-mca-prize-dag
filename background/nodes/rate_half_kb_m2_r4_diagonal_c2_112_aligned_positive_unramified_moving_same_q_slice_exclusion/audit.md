# Audit

The exact checker reconstructs three layers independently: corrected source
normalization and reciprocal trace descent; determinant/conic projections;
and finite-field replay for every irreducible endpoint factor. The direct
component ledger reports `factors=21`, `rank_candidates=5`, `empty=13`,
`boundary=8`. The off-common ledger reports `t_factors=7`,
`p_candidates=7`, `boundary=7`.

All exceptional fields are instantiated from their irreducible modulus,
including degrees 5, 9, and 60. A nonlinear `p` factor, nonlinear `w`
candidate, or surviving trace root is a hard checker failure.
