# Claim contract

## Proved

- Field descent and Weil restriction preserve `(D,n,kappa)`.
- The extension-pole construction preserves the degree bound `kappa`.
- The imported base-list rate `kappa/n` equals the ambient row rate at every
  tower level.
- Clean-rate pole pricing does not consume the rate-half list crossing.

## Not proved

No list-safe bound, list adjacency theorem, F1 pole count, extension-column
bound, or prize row is proved.  The existing global F1 dependency remains
correct for the full four-rate prize; this result separates its per-rate
instances for the clean-rate milestone.

## Falsifier

An F1 pole or tower step that changes the evaluation domain size or RS degree
bound before invoking the base-list threshold, or an imported list code not
equal to `RS[B,D,kappa]` (possibly interleaved) at the same `D,kappa`.
