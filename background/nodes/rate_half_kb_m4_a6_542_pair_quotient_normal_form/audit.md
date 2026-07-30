# Audit

The primary verifier rebuilds the pinned companion factorizations, pair
determinant, rank-eight adjoint space, normalized parameter identities,
quotient factorization, branch profile, and both KoalaBear embeddings. It
then compares the result with a hash-bound certificate and rejects hostile
mutations.

The independent verifier uses only `Fraction` arithmetic in the quadratic
field and a separate polynomial implementation. It reconstructs `T`, proves
that `T-1` has the printed factors, checks squarefreeness and coprimality, and
replays the finite-field descent.

`verify_elimination.py` is the slower derivation audit. It recomputes both
cubic-adjoint resultants and proves that their unique moving `(1,5)` factors
recover the frozen `y(u),z(u)` coordinates.
