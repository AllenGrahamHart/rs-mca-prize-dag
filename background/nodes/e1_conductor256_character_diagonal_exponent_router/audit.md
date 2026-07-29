# Audit

## Checked seams

- `G` has 64 classes and the class of `5` has order 64.
- The representatives `1,3,...,127` are exactly one choice modulo sign.
- Squared-modulus logs account for the factor two in `(CER1)`.
- Extending `x` by `xi(1)=-sum x_a` converts sine ratios to one convolution.
- The Fourier convention sends `xi` to index `-j`; dropping that sign would
  not alter scalar bounds but would make `(CER4)` false as written.
- The trivial character vanishes because `xi` has sum zero.
- All nontrivial eigenvalues are nonzero by log-map injectivity; numerical
  evaluation is not used for this conclusion.
- Parseval carries the factor `1/64` in `(CER8)` and the factor `64` in
  `(CER10)`.

## Scope ruling

This is a proof-producing preflight for the 367-orbit E1 target. It is not an
orbit count. A future implementation must preserve the cofactor, anchor,
torsion quotient, exact inverse-pair coefficient box, and sparse profile
test. A count of all lattice points in the ellipsoid without the sparse
filter is valid only as an upper bound and may be far too large.

## Compute ruling

No Modal or local numerical search is authorized by this packet. The first
implementation step is a certified interval evaluation of the 63 Fourier
eigenvalues and a conservative count projection. If that projection is not
comfortably below the repository spend and RAM limits, the run becomes an
external contributor request.
