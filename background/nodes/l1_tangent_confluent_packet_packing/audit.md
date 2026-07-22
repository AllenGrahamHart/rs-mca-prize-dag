# Audit

- **Truth status:** PROVED by Hermite uniqueness for degree-below-`k`
  polynomials.
- **Multiplicity check:** a doubled root contributes exactly two conditions;
  `E` is disjoint from the value-only set `V`.
- **Universe check:** packets are keyed by the ordered role pair `(E,V)`, so
  their number is `binom(n,j)binom(n-j,k-2j)`.
- **Complement check:** in the balanced band the weighted intersection law is
  `|C_1 intersect C_2|+|D_1 intersect D_2|<=s-1`; role-labelled
  tangent/complement packets of total size `s` are therefore disjoint.
- **Optimizer check:** the consecutive-bound ratio is exactly
  `(w+j+1)/(r0-j)`, so positive `j` helps only for `r0>w+1`; the verifier
  checks the closed-form minimizer against all legal toy indices.
- **Owner check:** `D_P` is the exact gcd owner; no subset owner is counted as
  a codeword.  Subsets occur only as condition packets in a disjoint packing.
- **Scope check:** the field-independent ceiling may still be exponential and
  does not change the L1 TARGET status.
- **Deployed planning calibration (not a theorem claim):** log-gamma
  evaluation at `n=2097152,k=524288` gives about `588290` bits for the
  all-tangent `j=1` ceiling versus `501080` bits for complement packing on
  the KoalaBear list row.  Optimized mixed packets at the maximal possible
  tangent degree lower this to about `430829` bits, still far beyond a finite
  row numerator.  The Mersenne-31 figures are about `588312`, `501136`, and
  `430868` bits.  Thus the theorem removes the raw owner sum and sharpens a
  tail, but closes no deployed tangent profile by itself.
- **Replay:** `verify.py` exhausts all degree-below-three codewords in two
  exact shells of a nontrivial `F_7` word, recomputes `D_P`, checks Hasse
  conditions, and proves both packet families disjoint at every legal `j`.
- **Negative controls:** `verify_audit.py` rejects nine malformed or
  overclaimed contracts.
