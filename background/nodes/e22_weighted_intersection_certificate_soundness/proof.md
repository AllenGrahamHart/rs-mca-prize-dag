# proof: e22_weighted_intersection_certificate_soundness

Fix a dyadic pair `M_i<M_j` and a subset `S` of smaller dyadic scales. Let
`U_{i,j}` be the residual-profile universe supplied by
`e22_residual_profile_generating_function`.

The certificate gives a finite set of formula atoms `A_S` and a verified
bijection

```text
phi_S : A_S -> {R in U_{i,j} : R is admissible at every scale in S}.
```

It also verifies that the atom weight equals the
`dyadic_profile_evaluation` multiplicity of the corresponding profile:

```text
w_A(a) = w(phi_S(a)).
```

Therefore

```text
sum_{a in A_S} w_A(a)
  = sum_{R in intersection_S} w(R),
```

by substitution through the bijection. The left side is exactly the coefficient
formula declared by the certificate, and the right side is the weighted
intersection count required by
`e22_lower_scale_intersection_profile_counts`.

Since the argument applies to every dyadic pair and every subset `S`, a
complete certificate of this form supplies all required lower-scale
intersection counts.
