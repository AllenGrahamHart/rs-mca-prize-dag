# ATTACK - e22_cofactor_coset_saturation

Status: conditional.

Use the cofactor equations

```text
U(x) L_{Z\C}(x) = a_i L_{C\Z}(x)
```

on all touched petal agreement points. The target is to prove that the root
data outside the fixed tail is saturated on full fibers of some quotient map
`x -> x^M`, with `M > t`.

The pointwise equations have now been converted into petal-locator divisibility
constraints in `e22_cofactor_petal_divisibility`. The dyadic common-modulus
part of gluing is proved in `e22_dyadic_local_to_common_saturation`; the
local fiber-locator conversion is proved in `e22_fiber_locator_saturation`.
The active support-forcing leaf is
`e22_cofactor_common_tail_kernel_invariance`: extract one bounded tail and
local dyadic quotient-kernel invariance from those divisibility constraints.
