# Audit

The ambient order `n` and exact ratio order `m` must remain distinct. Replacing
`p>n^2` by the weaker `p>m^2` erases the proper-level gain and returns only
the quarter-width theorem.

The exponent is `floor(h/2)`, not `h/2`. The even cutoff in `(ALC2)` ensures
that every admitted odd width has the same valid integer lower bound.

The exact gate is applied width by width. An even width can pass one step
before the following odd width because `floor(h/2)` does not increase; no
continuous suffix is claimed without a separate monotonicity proof.

The free/swap dichotomy is exhaustive. For nonzero antipodal defect,
Vandermonde gives `L>=v_h`; for zero defect, the primitive swap router forces
odd width and the separate one-side norm is required. Applying the free-class
bound `D<=4h-v_h` directly to a swap would be invalid.

The strict lower-quarter guard `h<m/4` is load-bearing because it supplies
`4h<m`. Equality and the strip above it are delegated to the existing
quarter-width theorem, whose special first-odd-width argument must not be
dropped.

The cutoff is maximal for the coarse comparison with `m^(m/4)`: at
`h=c_(n,m)-1`, one has

```text
2s floor(h/2)<mr/4.
```

This does not prove that a survivor exists there; it prevents the arithmetic
router from being overstated as a sharper theorem.
