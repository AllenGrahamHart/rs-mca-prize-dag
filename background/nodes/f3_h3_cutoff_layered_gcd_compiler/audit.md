# Audit

## Checked points

1. `Qcal` omits the identity quotient, matching the critical `t!=1` sum.
2. The first gcd uses derivatives through order `c`, so its root
   multiplicity is `(P-c)_+`, not `(P-c+1)_+`.
3. `G_j` uses derivatives through order `j-1`, making its live condition
   exactly `(P-c)_+>=j`.
4. The exponent `d=n-1` is a saturation exponent because every product and
   quotient fiber has size at most `d`.
5. `Qcal_+=gcd(Qcal,Qcal')` has multiplicity `(R-1)_+`, which is the
   double-accident weight rather than quotient support.
6. The hypothesis `p>=n^2` makes every multiplicity, derivative order, and
   factorial smaller than `p`; no Hasse leading coefficient vanishes.
7. One saturated gcd detects only rich support. Every derivative layer is
   required to restore the full excess weight.
8. The Stepanov cap applies only on the official orders; the general algebraic
   identity retains the complete range `1<=j<=d-c`.
9. A divisor alone certifies only a lower bound on gcd degree. The printed
   quotient Bezout identity is required to certify exactness.

The primary verifier replays `(LGC3)` with SymPy polynomial gcds. The
independent audit uses a separate low-level finite-field Euclidean
implementation. Both retain examples with positive `Y_c`.
