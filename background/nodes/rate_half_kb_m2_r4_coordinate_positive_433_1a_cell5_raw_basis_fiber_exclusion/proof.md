# Proof

The generic quotient basis cannot be specialized at these eight values.
Instead, chart 2 is reconstructed directly modulo the specialized reciprocal
quartic `P`, whose `r` and `c` leading coefficients are invertible at every
fiber.  Substitution into the exact signed-pair interface gives `g3,h` over
the base field.  Adding `u*D0*D1-1` performs the only localization used in
the pair elimination.

Groebner.jl computes and certifies a zero-dimensional basis separately at
each fiber.  The quotient dimensions are

```text
24,24,24,23,24,24,24,24.
```

Thus the vertical fiber `1332924776` has a genuine one-dimensional length
drop; no generic length is imposed on it.

Normal forms of `x1,x0,b` on each raw monomial basis give their full
multiplication matrices.  The independent checker reconstructs `P,g3,h`
as matrix identities and proves `D0*D1` invertible, so these matrices act on
the complete localized quotient.  It verifies pairwise commutation and an
invertible Krylov basis for `ell'=x1+2*x0+b`, then redoes the coordinate
solves and reconstructs every full multiplication matrix.

The eight monic minimal polynomials factor into distinct irreducibles whose
degrees sum to the raw dimension.  On every factor, the checker verifies the
coordinate relation for `ell'` and reconstructs `r,c`.  Fresh exact pair and
colored equations then have gcd `1` on 35 rows and `e^2-1` on 80.  These
respectively have no common root or only target-collision roots.  All 115
components, and therefore all eight fibers, are empty. QED.
