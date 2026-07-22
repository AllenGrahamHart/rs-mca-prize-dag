# Audit - L1 cofactor-prefix Pade graph

## Checked axes

1. Reversal includes the leading `t=0` coefficient.
2. The truncation depth is `d=h-k=w+e`.
3. `e<k` is exactly the range `d<a`.
4. `Qhat(0)=lc(U)` is nonzero, so truncated division is valid.
5. The graph has `e` free and `w` dependent coordinates.
6. Projection to the first `e` locator coefficients is bijective, not merely
   finite-to-one.
7. The cofactor inverse retains all `e+1` coefficients.
8. The product congruence forces `deg(U-QL)<k`, not merely `<=k`.
9. The complement gcd guard is retained and is equivalent to exactness.
10. Ambient density is recorded as a target scale, not a proved intersection
    estimate.

## Route effect

The live global L1 object is one received-word-dependent Pade graph section
of the split-divisor prefix variety.  Effective-image collapse is no longer
best phrased as an unstructured cofactor occupation problem: it is possible
alignment of two explicit algebraic sets.  The decorated shift-pair compiler
is the exact second moment of this intersection.
