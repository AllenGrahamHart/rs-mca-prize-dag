# Upstream crosswalk - tangent descent to a primitive shell

## Split-pencil terminology

The base-field tangent/common-factor stratum with exact owner `D` is not an
unstructured exceptional component.  Removing its forced double roots sends
it bijectively to the primitive part of a lower-dimensional split-pencil
census on the punctured domain:

```text
(n,k,a,e,w) -> (n-r,k-2r,a-r,e-r,w+r).
```

This is an exact SPI/exchange-degree ledger: cofactor degree is consumed at
the same rate that section surplus is gained.

## Portable consequence

Any primitive census theorem stable under deletion of `r` evaluation points
immediately bounds a fixed exact tangent owner after this transform.  The
large-owner range `2r>k` costs at most one codeword per owner.

## Remaining statement

Smooth-domain arguments do not automatically survive arbitrary puncturing,
and summing over all owners can still be exponential.  An upstream use must
either prove puncture-stable primitive flatness or absorb feasible owners via
its tangent/quotient first-match ledger.
