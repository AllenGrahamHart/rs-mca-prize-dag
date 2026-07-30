# E1 square-mass-18 cofactor-1028 global energy window

- **status:** PROVED
- **closure:** exact low-energy resultants and sharp two-moment product ceiling
- **scope:** every conductor-256 square-mass-18 collision, cofactor `1028`

Let `F` have coefficient square mass 18 and positive-half autocorrelation
energy

```text
E=sum_(d=1)^63 A_d^2.
```

If `|Norm(F(zeta_256))|=1028p` on a prize-envelope row, then

```text
E in {2,3,4,5,6}.
```

Energy zero has the wrong 2-adic norm valuation. At energy one, local
multiplicity forces a lag of 2-adic order one, whose exact Lucas resultant is
not divisible by 1028. At energy seven, all 61 feasible two-level product
chambers lie below `1028*p_min`; chamberwise monotonicity excludes every
larger energy. The adjacent energy-six envelope remains above threshold, so
no middle energy is silently removed.
