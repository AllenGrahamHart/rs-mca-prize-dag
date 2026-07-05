# ATTACK - e22_cofactor_divisor_quotient_gluing

This node is now an assembly point.

The formal pointwise-to-divisor translation is proved in
`e22_cofactor_petal_divisibility`. Start from the divisibility constraints

```text
L_{T_i} | H_i,    H_i = U L_{Z\C} - a_i L_{C\Z}.
```

The proof has been split into:

- `e22_fixed_tail_local_saturation`: assemble the local quotient-factor
  extraction with the proved fiber-locator saturation lemma;
- `e22_dyadic_local_to_common_saturation`: prove that local dyadic saturated
  blocks glue to the minimum local modulus.

The remaining active support-forcing leaf is
`e22_local_quotient_factor_extraction`.

Toy n=16 profile matching is evidence only.
