# Direction-support common-zero envelope

- **status:** REFUTED
- **refuter:** `rate_half_mca_affine_span_incidence_counterexample`

The asserted envelope

```text
|Z| <= floor(max_(x=R+r..R+K)
  ((x)_(fall r+1)-(x-e)_(fall r+1))
  /((x-R+d)d_(rise r)))
```

is false.  At `(R,d,K,r,e)=(99,20,1,1,80)` it equals 22, while the exact
counterexample contains 31 slopes.  The one-dimensional maximization is
arithmetically correct for the printed expression; the expression itself
inherits the invalid incident-basis denominator.

All former KoalaBear and Mersenne common-zero support walls are retracted.
