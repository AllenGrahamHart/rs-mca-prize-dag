# f_scale_recursion

- **status:** PROVABLE
- **closure:** proof
- **refs (legacy repo):** ['proof_sketch/s3b_ii_strip_periodic.md#1']

## Statement

P cap D_j^per(M) is linearly isomorphic to P' cap D'_{j/M} at scale n/M (an M-pullback ell = g(X^M) places g's coefficients at multiples of M — a linear embedding). Hence F(n) <= F_primitive(n) + sum over M | gcd(n,j) of F(n/M): the periodic branch recurses, bottoming out at checkable scales.

## Ledger (migrated notes)

the same multi-scale self-similarity as Q_M = Q_1 and the coset-move dynamics — third appearance of the recursion | IN FLIGHT: PR #182 (Codex) proves this (verifier replayed green locally, 13792 reduction checks; tip adds a bonus common-root consumer bound). Flips to PROVED on integration. | NEEDS THE DIHEDRAL ANALOGUE: plane sections of the reciprocal stratum should be plane sections of the Chebyshev-quotient instance (y = x + x^{-1}), mirroring the multiplicative case — plausibly provable identically (the X^m h(X + X^{-1}) factorization is the pullback map).
