# Claim contract

- **Claim:** every live `A=1` residual curve for `s in {0,1,2}` carries the
  contact section `(A1S2)`.
- **Dependencies:** the half-distance core ledger and contracted-root charge.
- **Output:** one contact section of degree exactly the residual regular
  Kronecker size `Delta`.
- **Consumer:** the fixed-core pole-slack exclusion.
- **Nonclaim:** this leaf alone excludes no profile.
- **Falsifier:** a contracted matrix with a row count other than `rho`, a
  zero low numerator at positive generic rank, or contact degree different
  from `Delta`.
- **Replay:** run this directory's verifiers under `tools/ramguard tiny --`.
