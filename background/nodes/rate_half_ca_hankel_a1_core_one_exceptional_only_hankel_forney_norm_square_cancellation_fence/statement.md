# `A=1` Forney norm-square cancellation fence

- **status:** PROVED
- **closure:** proof
- **consumer:** `rate_half_band_closure`
- **dependencies:**
  `rate_half_ca_hankel_a1_core_one_exceptional_only_hankel_forney_norm_discriminant_square_gate`,
  `rate_half_ca_hankel_a1_core_one_exceptional_only_quotient_forney_numerator_normal_form`

Let `Beta` be the interpolation class in `F_field[X]/(A)` with
`Beta(a)=beta_a` at every exceptional root. Then the norm-discriminant
quantity from `(HNS1)` satisfies the exact identity

```text
Xi_A=(-1)^e Norm_A(Beta) Res(A,q_1)^2.               (HNC1)
```

Moreover, self-duality of the original exceptional evaluation code gives

```text
(-1)^e Norm_A(Beta) in (F_field^x)^2.                (HNC2)
```

Consequently the square condition `(HNS1)` is exactly the determinant
square condition already implied by weighted self-duality. Computing
`Xi_A` from a complete endpoint packet is an audit check, not an independent
endpoint exclusion. It can become an exclusion only if a separate formula
derived from the endpoint profile forces the opposite square class without
assuming the self-dual packet.
