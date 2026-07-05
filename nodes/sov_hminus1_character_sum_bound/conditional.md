# conditional: sov_hminus1_character_sum_bound

## Predicate nodes

- `sov_nonconstant_affine_character_cancellation`
- `sov_hminus1_affine_piece_decomposition`

## Claim

Conditional on the affine/paid-piece decomposition of each conditioned
anchored-core cell, the nontrivial character sums of `[X^{h-1}]L` are below
the budget needed by the SOV Fourier-duality step.

## Proof

The predicate `sov_hminus1_affine_piece_decomposition` partitions each
forced-root conditioned anchored-core cell into affine pieces on which

```text
c(L) = [X^{h-1}]L
```

is nonconstant affine-linear, plus exceptional paid or norm-structured pieces
whose total size is below the required character-sum budget.

The proved predicate `sov_nonconstant_affine_character_cancellation` says that
every nontrivial additive character sum over a nonconstant affine piece is
zero. Therefore the only contribution to any nontrivial sum over the whole
conditioning cell comes from the exceptional pieces, and its absolute value is
bounded by their total size.

By the decomposition predicate, that exceptional total is below the budget
needed by `sov_hminus1_fiber_fourier_duality`. Hence the character-sum bound
holds.
