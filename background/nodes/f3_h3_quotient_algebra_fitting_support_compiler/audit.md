# Audit

## Checked points

1. The leading coefficient of the cleared quotient polynomial is
   `n^(d-1)`, a unit only after inverting two.
2. The cutoff restriction `c>=2` is load-bearing: product roots can have
   characteristic-zero multiplicity two.
3. The `X` module records `min(R,q)`, not `Rq`; the `Y` module records
   `min(R-1,q)`, not `(R-1)q`.
4. Adding `Qhat_n'` detects a repeated quotient root. It does not use a
   nonexistent characteristic-zero polynomial `gcd(Qhat_n,Qhat_n')`.
5. Exact support follows because the min-depth sums are positive exactly on
   the positive weighted moments.
6. The Fitting presentation uses the gcd of all full-rank minors. One
   selected determinant may add spurious prime factors.
7. Candidate-prime support needs only the largest Smith invariant, or scalar
   annihilator. The full product of invariant factors is not the preferred
   computational target.
8. A Bezout identity proves that a proposed scalar annihilates the module;
   exact minimality additionally needs a Smith/determinantal-divisor or
   equivalent elimination certificate.

The primary verifier constructs the global resultants at `n=8`, checks the
quotient-algebra block ranks at one positive and one empty row, and compares
them with direct min-depth sums. The independent audit uses separate
finite-field polynomial arithmetic at official-aspect order-16 fixtures.
