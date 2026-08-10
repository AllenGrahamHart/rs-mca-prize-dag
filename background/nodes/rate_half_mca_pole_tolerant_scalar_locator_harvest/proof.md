# Proof

This node imports the two proved local theorems at the immutable source pin.

For localization, evaluating the certificate on a support coordinate gives

```text
(A-Qr0)(x) + gamma_i (B-Qr1)(x) = 0.
```

Outside `G_Q` this is a nonzero affine equation in the distinct slope, so at
most one support can use the coordinate. Disjoint outside incidences give the
small-core bound and the crossing-support term in the punctured-core bound.
At `g=m`, two bad slopes on the same full core would interpolate a simultaneous
degree-`<k` explanation, so the punctured numerator is at most one.

For cancellation, `c_i != 0` and the certificate evaluated at a common zero
of `Q,A,B` force the exact locator to vanish there. Hence every such pole is
in every support. The product `R` of the distinct domain poles divides all
five relevant polynomials. Exact division gives the reduced identity and
monic reduced locator. Since `R` is nonzero off `P`, the coincidence equations
before and after division are equivalent there; any remaining root of `Q/R`
on the reduced core would have belonged to `P`. Degrees fall by `|P|`.

These are exactly the source arguments. QED.
