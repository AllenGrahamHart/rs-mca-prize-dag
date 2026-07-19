# Claim contract

- **Claim:** a concrete rate-half Reed-Solomon counterexample to the universal
  post-quadratic bound `B_ca^far(n-r)<=r+1`.
- **Quantifiers:** the single row `(q,n,k,r)=(5,4,2,1)`.
- **Dependencies:** parity-check syndrome characterization of Hamming distance
  and the standard dual description of Reed-Solomon codes.
- **Consumer:** route selection inside `rate_half_band_closure`.
- **Nonclaims:** no counterexample at the official `n=2^41` row and no
  asymptotic lower family.
- **Falsifier:** failure of column farness or of any one of the four explicit
  one-column syndrome identities.
