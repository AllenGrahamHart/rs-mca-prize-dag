# E1 square-mass-18 cofactor-1028 energy-four cubic exclusion

- **status:** PROVED
- **closure:** complete finite-field type screen and cubic logarithm bound
- **scope:** conductor 256, square mass 18, local valuation two, cofactor `1028`

No square-mass-18 collision with cofactor `1028=4*257` has positive-half
autocorrelation energy `E=4`.

Local multiplicity four and a fixed primitive-root equation modulo `257`
leave exactly 8,385 signed four-lag types. For every one, the exact cubic
conjugate moment has the form

```text
sum_u x_u^3=64K,
K<=24.
```

The global cubic Taylor majorant then gives

```text
log Norm(F(zeta_256))
 <=64log(18)-512/729
 <log(1028*p_min).
```

Thus every compatible energy-four norm lies below the official field floor.
The claim is profile-independent: it applies to every coefficient profile
with square mass 18 and local valuation two.
