# Proof

Because `r<R/2`, the matrix has at least `r+1` rows. Hypothesis `(HF1)` gives
an `(r+1) x (r+1)` minor `Delta(Z)` that is not the zero polynomial. Every
entry of the pencil is affine linear in `Z`, hence

```text
deg Delta<=r+1.
```

If `M(gamma)` has a nonzero kernel, its column rank is below `r+1`, so every
maximal minor vanishes and in particular `Delta(gamma)=0`. A nonzero
polynomial of degree at most `r+1` has at most `r+1` roots in `F`. This proves
the first assertion.

A domain-split kernel locator is nonzero, so its supported slopes are a subset
of those rank-drop roots. The Hankel equivalence identifies those supported
slopes with close slopes, and for a column-far pair close slopes are exactly
CA-bad slopes. This proves `(HF2)` and the official specialization. QED.
