# proof: e22_fiber_locator_saturation

Let `D` be a cyclic multiplicative subgroup, and fix `M | |D|`. Since `z` is
in the image of `pi_M`, choose `y in D` with `y^M=z`. The kernel of `pi_M` on
`D` is the subgroup `mu_M` of `M`-th roots of unity, of size `M`. Therefore
the fiber over `z` is exactly the coset

```text
F_z = y mu_M.
```

The roots of `X^M-z` are precisely the elements `y eta` with
`eta in mu_M`, because

```text
(y eta)^M = y^M eta^M = z.
```

There are `M` such roots, and `X^M-z` is monic of degree `M`; hence

```text
X^M-z = prod_{x in F_z} (X-x) = L_{F_z}(X).
```

Now let `L_R` be a squarefree locator for a support `R subset D`. If
`F_z subset R`, then the product defining `L_R` contains every linear factor
of `L_{F_z}`, so `X^M-z` divides `L_R`. Conversely, if `X^M-z` divides
`L_R`, every root in `F_z` is a root of `L_R`; since `L_R` is squarefree with
root set exactly `R`, this means `F_z subset R`.

Distinct quotient values have disjoint fibers. Therefore a product of
distinct factors `X^M-z` divides a squarefree support locator exactly when the
support contains the union of the corresponding full fibers. This is the
local locator-to-saturation implication used by the E22 fixed-tail node.
