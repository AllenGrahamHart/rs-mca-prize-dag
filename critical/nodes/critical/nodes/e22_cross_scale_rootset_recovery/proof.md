# proof: e22_cross_scale_rootset_recovery

Let two staircase locators be equal:

```text
L_B(X) G(X^M) = L_{B'}(X) G'(X^{M'}).
```

Both sides are monic locators over distinct field points. A monic locator is
determined by its root set, so equality of the polynomials implies equality
of the underlying support set `R`.

Now fix one of the moduli, say `M`. The proved node
`e22_fixed_scale_staircase_injectivity` says that, once `M` is fixed, the root
set `R` uniquely recovers:

```text
H_M = {z : pi_M^{-1}(z) subset R}
```

and then recovers the tail as the remaining roots after removing those full
fibers. The same argument applies at the other fixed modulus `M'`.

Therefore cross-scale multiplicity has no additional hidden algebraic source:
equal locators are exactly equal supports, and at each participating scale the
tail and selected fibers are the fixed-scale recovery of that same support.
The next formal step is the canonical support-scale recovery recorded in
`e22_cross_scale_support_canonical_form`; after that, the remaining task is
pricing multiplicity.
