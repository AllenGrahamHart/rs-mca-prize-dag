# H3 distance-two collisions are 2-primary

- **status:** PROVED
- **closure:** proof
- **consumer:** `f3_h3_low_distance_ideal_star_router`
- **dependency:** `f3_h3_shifted_product_sidon`

Let `n=2^s` with `s>=2`, and use the shifted products `beta_E` and half-basis
vectors `v_E` from the H3 rich-fiber packet. If `E!=F` and

```text
||v_E-v_F||_2^2=2,
```

then the nonzero cyclotomic integer `beta_E-beta_F` has absolute rational norm
equal to a power of two.

Consequently, two distinct shifted-product representations that coincide in
an odd-characteristic order-`n` subgroup row can never have squared vector
distance two.

In particular, among the seven squared-norm-at-most-three vectors selected
from a cutoff-18 rich fiber, at least six of the 21 pairwise distances are at
most six. The previous centroid argument guaranteed only four before the
distance-two class was excluded.
