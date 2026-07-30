# Proof

Put `K=Q(zeta_128)` and

```text
q_1 =(257,zeta_128-9),
q_63=(257,zeta_128-57).
```

The fixed-field calculation in the two-involution node proves

```text
p_66 O_K=q_1q_63=J_63.                              (1)
```

The proved node `e1_qzeta128_p257_j63_residue_obstruction` constructs an
explicit Jacobi element and an exact auxiliary-prime character proving that
`J_63` is nonprincipal in `K`.

If `p_66` were principal in `E_63`, extension of a generator through
`K/E_63` would make the ideal in `(1)` principal. This contradicts the
residue obstruction. Therefore `p_66` is nonprincipal. QED.
