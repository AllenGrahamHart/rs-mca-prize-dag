# L1 below-band full-petal FPC5 payment

- **status:** TARGET
- **consumer:** `imgfib`

## Statement

Fix an official row, a received word, and the first carried maximal sunflower
source assigned to one full-petal contributor. Let

```text
M   = number of petals in the carried source,
t   = number of those petals touched by the contributor,
ell = petal size,
d   = exact core defect,
e   = max(0, 2d+1-t ell).
```

After the proved top-band and root-pinning payments, the only possible
full-petal residual satisfies

```text
M>=4,       d<ell(M-2),       t<2M-4,       e->infinity.       (FPC5)
```

The target is a disjoint aggregate allocation of every such contributor to
one polynomial or legitimate quotient/profile column under `imgfib`'s
reserve, uniformly over official rows and received words.

The source-petal count `M` and touched-petal count `t` are different
parameters. No proof may replace one by the other. Mixed and partial petals
belong to `l1_mixed_petal_amplification`, not this node.

## Proven reduction

`pma_full_petal_band_composition` proves that this is the exact complement of
the following payments:

```text
d>=ell(M-2)       or       t>=2M-4.
```

The first is the layout-anchored top band paid by `petal_growth`. In the
second below-band branch, `e=0`, so the root-pinning ledger pays the complete
aggregate. Consequently no full-petal residual remains for `M<=3`; FPC5 is
the precise unpaid branch, not a synonym for all below-band words.

## Falsifier

A reserve-valid official-row family in FPC5 whose first-owner contribution
exceeds every polynomial and every legitimate quotient/profile column.
