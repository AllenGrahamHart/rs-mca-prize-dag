# Claim contract

## Consumed theorem

- `e1_conductor256_character_diagonal_exponent_router`: the exact spectrum
  definition and the necessary exponent bounds `(CER7)--(CER10)`.

## New proved content

1. Certified outward intervals for all 63 nontrivial conductor-256
   character eigenvalues.
2. The uniform prize bounds `|xi_t|<=7` and `sum xi_t^2<=101`.
3. The exact coarse zero-sum envelope count `(CEP4)`.
4. A 38-trillion-point explicit family inside the universal weighted
   ellipsoid, proving that ellipsoid-first enumeration is not a priced route.

## Guards

1. The interval table is a theorem about the Fourier filter, not an associate
   count.
2. The lower family in `(CEP5)` lies in the universal enclosing ellipsoid; it
   is not asserted to pass the sharper row-specific `L1` log body, the
   coefficient boxes, or the sparse collision-product test.
3. The 367 cap counts torsion orbits across four cofactors.  Neither `(CEP4)`
   nor `(CEP5)` is that count.
4. No floating-point transcendental function, FFT, `assert`, or optional
   numerical package is used by the verifier.
5. A future sparse-first algorithm needs a fresh count, RAM, time, and cost
   projection before any enumeration.
