# Claim contract - pma_exact_periodic_owner

## Claim

Actual listed source codewords whose full agreement set has nontrivial exact
cyclic stabilizer have a canonical chart-free owner. At exact scale `M` their
count is at most `binom(n/M,ceil((k+sigma)/M))`. On the official dyadic
`sigma=1` grid, the union over all nontrivial scales fits one global
`719(1+2^-690)Q_2(k+2)` profile line.

## Quantifiers and consumer

The owner theorem is uniform in the received word and field. The finite
allowance corollary is restricted to the printed official dyadic grid. It
is a direct requirement of `imgfib` and supplies evidence to the re-posed
`petal_mixed_amplification` target. The retired `pma_wide_residual` node keeps
the theorem as refutation context.

## Dependencies

- `petal_g2_support_forcing`: exact stabilizer gives a unique complete-fiber
  scale;
- `petal_g3_full_support_codeword_injectivity`: a full agreement subset of at
  least `k` points determines the codeword;
- `qa22_m_le_t_extension`: official `sigma=1` column ratios and first-scale
  dominance.

## Falsifier

Two distinct listed codewords with the same exact scale and canonical retained
cosets; a missing dyadic scale in the finite sum; or an official row where the
global exact-periodic count is not absorbed by the displayed first-scale line.

## Nonclaims

No statement is made here about algebraically folded codewords against
nonfolded receivers, stabilizer-one low-defect quotient closures, the B11
`GROW union RES` residual, or an asymptotic profile-envelope comparison. The
precise folded-receiver source class is handled by the downstream scope
theorem. The finite `719` line is not exported to general `sigma`.
