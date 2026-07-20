# H3 quotient anharmonic symmetry and antipodal twin

- **status:** PROVED
- **closure:** proof
- **consumer:** `f3_h3_dsp8_correlation_bound`
- **dependencies:** `f3_h3_quotient_block_identity`,
  `f3_h3_dsp8_antipodal_cayley_product_router`

Let `H<=F_p^*` have even order, put `A=(1-H)\{0}`, and define

```text
P(t)=#{(a,b) in A^2:ab=t},
R(t)=#{(c,d) in A^2:d/c=t}.
```

For every `t notin {0,1}`, `R` is constant on the full anharmonic orbit

```text
O(t)={t,1/t,1-t,1/(1-t),t/(t-1),(t-1)/t}.          (AAT1)
```

Put `tau(t)=t/(t-1)`. If `t=1-a^2` for `a in H\{1,-1}`, then

```text
tau(t)=1-a^(-2),
P(t)=P(tau(t)),       R(t)=R(tau(t)).                (AAT2)
```

Thus the antipodal retained-target set is closed under `tau`, with identical
richness and quotient weight on each orbit. The only possible nonzero fixed
target is `t=2`.

Moreover, an antipodal target has either zero or two diagonal product
representations. Hence `P(t)` and `M_a=P(t)-2` are even, and the exact
antipodal richness gate sharpens to

```text
P(t)>=25 iff P(t)>=26 iff M_a>=24.                  (AAT3)
```

This theorem does not identify the signed-support graphs at `t` and
`tau(t)`. In particular, it does not assert equality of `N_6^disj`, `E_a`,
`K_25^A`, or their targetwise summands.
