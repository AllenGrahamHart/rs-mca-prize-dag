# Audit

## Checked points

1. `F_n` is monic only after retaining the sign from `d=n-1` odd.
2. The diagonal quotient product is `n(T-1)^d`, not merely `(T-1)^d`.
3. The clearing exponent in `G_uv` is `N=d^2`, while the polynomial
   `H_(C,D)` uses degree `d`.
4. The quotient product is integral by Galois invariance, so `(GRC3)` is an
   identity in `Z[T]`, not only in a fraction field.
5. Truncation modulo `U^19` is exact because `(GRC4)` is an identity in
   `O[U]`; no coefficient-height or running-time estimate is inferred.
6. The global polynomials no longer require factor enumeration, but the
   derivative ideals remain indexed by all ordered quotient lifts.

The primary verifier compares all three resultants with independent direct
products at exact order-4 and order-8 finite-field specializations. The
independent audit evaluates Sylvester determinants modulo primes at orders
4, 8, and 16, without SymPy's resultant implementation.
