# proof: e22_tail_removed_factor_manifest_soundness

Fix a touched petal in the manifest. The manifest gives a dyadic modulus
`M_i`, a quotient-value set `Z_i`, and the squarefree identity

```text
L_{T_i\B}(X) = prod_{z in Z_i} (X^{M_i}-z).
```

By `e22_fiber_locator_saturation`, each factor `X^{M_i}-z` is exactly the
locator of the full fiber

```text
{x : x^{M_i}=z}
```

inside the multiplicative subgroup domain. Distinct quotient values have
disjoint fibers, and the manifest identity is squarefree. Therefore
`T_i\B` is a union of full fibers of `x -> x^{M_i}`.

By `e22_kernel_invariance_full_fiber_criterion`, a union of full
`M_i`-fibers is invariant under multiplication by the `M_i`-th-root kernel.
The manifest also supplies the same common tail `B` for every touched petal,
dyadic moduli satisfying `M_i>t`, and the bound

```text
|B| < min_i M_i.
```

These are exactly the predicates required by
`e22_common_tail_invariance_payload`. Hence a verified factor manifest of
this form proves the common-tail invariance payload.
