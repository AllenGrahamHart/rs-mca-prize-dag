# Claim contract - L1 marked constant-shift multistrip exclusion

## Inputs

- `l1_bounded_polarity_marked_full_pencil_reduction` for the L1 dense-petal
  interpretation and `v<=p`;
- `pma_coset_subtwoell_saturation_exclusion` for the common constant-shift
  pencil framework and exact saturation interface.

## Output

In strip `m`, every marked common-pencil contributor has at most `2m`
selected dense petals or reaches marked degree `(m+1)ell`. Under the L1
threshold, every away-from-boundary survivor lies in the printed dense-petal
window `(MT4)`.

## Consumer Rule

Consumers must retain arbitrary-locator cells, low-petal cells `t<=2m`, and
the next-boundary cells `d+v>=(m+1)ell`.

## Falsifier

One field and tuple satisfying `(MT1)--(MT2)`, including all distinct-label,
mark-divisibility, and exact-gcd conditions.
