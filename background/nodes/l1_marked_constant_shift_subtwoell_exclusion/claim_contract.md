# Claim contract - L1 marked constant-shift sub-two-ell exclusion

## Inputs

- `l1_bounded_polarity_marked_full_pencil_reduction` for the dense-petal
  marked-locator interpretation and the charge `v<=p`;
- `pma_coset_subtwoell_saturation_exclusion` for the common constant-shift
  pencil framework and its two-block rank interface.

## Output

The common-pencil branch with at least three dense petals is empty whenever
the enlarged marked degree satisfies `d+v<2ell`.

## Consumer Rule

Consumers may remove only the common constant-shift subbranch. They must
retain two-dense-petal, arbitrary-locator, and `d+v>=2ell` cases.

## Falsifier

One field and data satisfying `(MS1)--(MS2)`, including exact
`gcd(F,W)=1`, or a failure of the asserted L1 mark-degree map.
