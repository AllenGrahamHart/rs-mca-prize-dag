# Claim contract

## Inputs

- A finite affine plane.
- Pairwise distinct record lines.
- Pairwise disjoint owner petals of total size at most `S`, each of size at
  most `A-1`.
- On each record line, one selected-support partition of exact total `A`,
  with each selected part contained in its owner petal.

## Output

The weighted same-owner pair charge satisfies `(SP1)` in `statement.md`.

## Scope pins

- The `x_(L,p)` are line-specific selected masses; the proof does not assume
  that a record has no additional accidental agreements.
- Balanced cross-petal coordinate pairs, not owner pairs alone, are the
  globally injective resource.
- A dominant line containing another globally heavy owner is charged to the
  explicit heavy-pair exception before complement disjointness is used.
- The line set must not contain duplicate copies of one affine line.
