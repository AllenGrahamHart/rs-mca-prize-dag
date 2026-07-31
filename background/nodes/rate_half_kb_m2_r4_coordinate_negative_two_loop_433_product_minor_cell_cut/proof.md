# Proof

The complete-fiber compiler supplies the product row

```text
[-p,-pk,1,k].                                     (1)
```

Substitute the five products `(KB43P-1)` and the nine label rows from
`(KB43-3)` into the five maximal minors of `(1)`.

For `X1` and `N2`, the determinant on rows `(A,C,AB+,AB-)` is the first
formula in `(KB43P-4)`.  For `Z1`, reduce the same determinant by `M^2+1`;
it is the second formula.  Actual labels have `M!=0,+/-1`, and actual signed
pairs have `b!=+/-c`.  Characteristic is odd.  Thus these determinants are
nonzero, proving `(KB43P-2)`.

For `X2` and `N1`, use the determinant on rows `(C,AB+,AB-,BC)`.  It is the
first formula in `(KB43P-5)`.  In `L1`, reduce the same determinant by
`M^2+1`; it becomes the second formula.  The factors `2,4,b,M,M-1,M+1`
are nonzero in their stated cells, so product rank at most three forces
`b+c^3=0`.  This is `(KB43P-3)`.

The nine-cell atlas contains no other rows.  Removing the three deleted
cells and recording the forced relation on three survivors gives exactly
`(KB43P-6)`.  No assertion about the unused minors is made. QED.
