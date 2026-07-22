# Audit - L1 decorated shift-pair compiler

## Checked axes

1. Ordered pairs, rather than unordered pairs, match `Z(Z-1)`.
2. The four root sets in `(DS1)` are disjoint and exhaustive.
3. Both asymmetric tails have the same degree `d=a-g`.
4. Distinct codewords force `R!=0` and `g<=k-1`.
5. The identity `k-g=d-w` has no off-by-one loss.
6. Exactness gives cross-coprimality with `BN` and `AN`.
7. Scalar cofactor yields `deg(A-B)<=d-w-1`.
8. Primitive uniqueness includes the endpoint `e=w`.
9. Fixed leading coefficients remove the final scalar ambiguity.
10. A common cofactor is routed explicitly rather than called primitive.

## Route effect

The growing-cofactor union has been converted to an exact second-moment
problem. In the large region `e<=w`, primitive cofactor decorations have
multiplicity one per ordered split support pair. The live tasks are now the
support-pair census, common-cofactor payment, and `e>w` decorations.
