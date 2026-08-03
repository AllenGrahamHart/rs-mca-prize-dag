# XR window-divisor maximality filter

- **status:** PROVED
- **purpose:** prevent the raw-subset count from replacing selected
  maximal occupancy

For a received pair `(u,v)`, let `MAX_e` be the number of distinct
codeword pairs whose full joint agreement set has size exactly `k+e`.
Let `RAW_d` count `(k+d)`-sets on which both received words interpolate
to degree-`<k` codewords, equivalently the degree-`n-k-d` locators
satisfying both window systems. Then

```text
RAW_d = sum_{e>=d} MAX_e binom(k+e,k+d).                  (F)
```

The identity remains true before any selected-live-slope filter. A
selected maximal depth-`d` pair contributes exactly one locator to
`N_d`; a deeper pair contributes zero to `N_d` but
`binom(k+e,k+d)` locators to `RAW_d`. Therefore a bound on all divisors
in the affine window intersection is not equivalent to SL-2 and is in
general false at its `17n^2/25` threshold.

The exact residual object must impose both:

1. **maximality:** the reconstructed pair disagrees in at least one
   coordinate at every point of `T`, so its full joint core is `H\T`;
2. **selection/liveness:** that maximal pair has `L_P>=2` under the
   support-wise first-match selector.

The two single-word window matrices each have rank `d`, but this also
does not imply joint codimension `2d`; their row spaces can intersect.

## Falsifier

A raw locator not lying over a unique maximal joint pair, or failure of
the fiber identity `(F)`.
