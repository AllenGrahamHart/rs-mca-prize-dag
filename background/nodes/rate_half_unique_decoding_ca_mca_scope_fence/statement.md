# Unique-decoding CA/MCA scope fence at rate one-half

- **status:** PROVED
- **consumer:** `rate_half_band_crossing_location`

For the official maximal rate-half row

```text
n=2^41,       k=2^40,
```

write `a` for agreement and `r=n-a` for error radius. The proved
MCA-from-CA transfer and its BCIKS correlated-agreement input have the exact
unique-decoding gate

```text
2r<=n-k.                                                   (SC1)
```

At rate one-half this is equivalent to

```text
a>=(n+k)/2=3n/4.                                          (SC2)
```

The live rate-half crossing interval is

```text
k+2^34<=a<3n/4.                                           (SC3)
```

Consequently every agreement in `(SC3)` is outside the scope of the named
unique-decoding CA/MCA conversion. At the closest interior point,
`a=3n/4-1`, its hypothesis fails by exactly two:

```text
2(n-a)-(n-k)=2.                                           (SC4)
```

At `a=3n/4`, `(SC1)` holds with equality and recovers the already-proved
half-distance safe endpoint. It gives no upper bound at any live interior
agreement.

## Scope

This is a route fence for the specific ABF/BCIKS unique-decoding transfer
suggested by the Round-31 supply audit. It does not prove that no CA/MCA
comparison can hold beyond half distance. Such a comparison would require a
new theorem whose hypotheses genuinely cover `(SC3)`.
