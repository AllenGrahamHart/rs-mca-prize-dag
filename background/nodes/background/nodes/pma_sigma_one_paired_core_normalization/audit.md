# Audit - PMA sigma-one paired-core normalization

## Checked points

1. `Q_C` uses degree at most `k-2`, so it is uniquely fixed by the `k-1`
   core values. Allowing degree below `k` here would destroy uniqueness.
2. The base polynomial differs from `Q_C` by one scalar multiple of `L_C`.
   The singleton value supplies that scalar; it need not be zero before the
   shift.
3. Maximality is used through the exhaustive size identity
   `|H\C|=n-k+1=2M+1`. No unclassified point remains outside the singleton
   and doubletons.
4. Pairwise distinct nonzero source labels are exactly equivalent to the
   doubleton values being distinct from one another and from the singleton
   value.
5. The two-anchor uniqueness uses exact degree `k-1` and split locator
   roots. It does not claim that one planted codeword identifies a layout.
6. `(PC4)` is an identity after first match, not a polynomial chart census.
   In particular, multiplying a per-core bound by an unproved number of
   cores remains invalid.

## PR #771 route audit

The current one-added-locator PMA paving bridge does not turn PR `#771` into
a global chart owner. For a source auxiliary code of length `N=L+1`,
dimension `kappa`, and `sigma=1`, its error budget is `t=L-kappa-1`, so the
LineRay deficiency is

```text
d_LR=2t-(N-kappa)=L-kappa-3.
```

The complete fixed-deficiency bound would therefore be

```text
binom(L+1,d_LR+1)=binom(L+1,kappa+3).
```

Before flooring, the existing pinned paving bound is
`binom(L,kappa)/(kappa+1)`, and their exact ratio is

```text
(L+1)(L-kappa)(L-kappa-1)/((kappa+2)(kappa+3)).
```

This is greater than one throughout the official low-defect cells and both
bounds are still per paired core. PR `#771` remains useful for genuinely
source-bridged global syndrome lines, but this particular specialization
neither improves the local payment nor removes `(PC4)`'s core sum.

## Nonclaims

- No bound on the number of paired cores is proved.
- No global first-match atlas is inferred from two-anchor uniqueness.
- No theorem from open PR `#771` is imported as a local dependency; only the
  displayed specialization arithmetic is audited.
- The theorem does not cover larger fibers, nonmaximal layouts, or general
  `sigma`.
