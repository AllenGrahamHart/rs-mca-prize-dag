# averaged_xr

- **status:** TARGET
- **status authority:** `dag.json`
- **adjudication:** canonical Fable commit `3cca68b7` (2026-07-27)

## Statement

The sought averaged-XR theorem is a slope-resolved second-moment estimate.
Second moments of `|A_(u,v)|` over pairs or slopes should admit explicit
Cauchy double sums over support pairs `(T,T')`, graded by intersection size,
so that the Johnson-scheme decomposition and its `lambda_0-lambda_1=n` gap
control variance. Same-slope pairs should carry the reconciled closed-form
correlation term, while distinct-slope pairs should decorrelate. This is the
second-moment input consumed by `averaged_slope_conversion`.

The node is open. Its former automatic proof was invalid for three independent
reasons:

1. `proof.md` invokes a nonexistent `conditional.md`;
2. `xr_ledger_exponent_reconciliation` reconciles the exponent used by this
   claim and therefore cannot prove the de-correlation claim itself; and
3. the source says only that the averaged form looks provable and leaves
   worst-case de-correlation open.

The preferred attack is the Hooley--Katz / Scott exponential-sum lane named
in `proof_sketch/s3b_iii_2_displacement_spectral.md#5`.

## Falsifier

A shell on which the reconciled exponent `c(s,t)` fails to yield the variance
control required by `averaged_slope_conversion`.

## Ledger (migrated notes)

The graded-by-intersection second-moment table is now CLOSED FORM via the pair-rank ledger: correlations q^{-min(s,t)} extra for s < t, exact independence beyond — the variance is dominated by close pairs, as the FM model hoped. | PROVED 2026-07-04 from xr_ledger_qpower by summing the Johnson distance shells.
