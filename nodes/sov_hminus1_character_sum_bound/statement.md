# sov_hminus1_character_sum_bound

- **status:** CONDITIONAL
- **closure:** proof

## Statement

For every official-shape row, every `h in (20,A]`, and every forced-root
higher-coefficient conditioning cell of anchored-core locators, the
nontrivial additive character sums

```text
S(xi) = sum_L psi(xi [X^{h-1}]L),    xi != 0,
```

are small enough that the Fourier-duality bound in
`sov_hminus1_fiber_fourier_duality` puts every `[X^{h-1}]L` fiber below the
active-core budget.

This is reduced to the proved affine-piece cancellation lemma plus the
remaining decomposition of actual conditioned anchored-core cells into
cancellative affine pieces and budget-small paid/norm-structured exceptions.

## Falsifier

A forced-root conditioning cell and a nontrivial additive character whose sum
is large enough to permit an above-budget `h-1` coefficient fiber.
