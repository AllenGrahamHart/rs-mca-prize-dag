# Audit

## Scope checks

- The boundary layer has missed allowance exactly `s+1`.
- The two anchors come from the already-synchronized high union and each
  misses at most `s` coordinates.
- The new synchronization uses `q>=1`; it is not asserted when `q=0`.
- Prefix suffix minima are recomputed independently for `H` and `H-1`.
- The affine-line cap includes both the high union and the boundary layer.

## Arithmetic checks

- Primary replay evaluates all `65488` cumulative caps at `e=98230`.
- Independent replay reconstructs both Abel profiles in separate code.
- The adjacent `e=98231` result records only a failed upper-bound method.
- Contract and source hashes, exact totals, slack, and mutation controls are
  checked.

## Residual risk

The theorem is a one-support gain for the official Mersenne row. It does not
address the rapidly growing mean-centered boundary cap after `e=98230`.
