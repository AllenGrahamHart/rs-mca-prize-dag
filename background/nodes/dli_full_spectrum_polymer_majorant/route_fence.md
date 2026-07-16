# Full-spectrum primitive-mass route fence

Date: 2026-07-13.

The polymer majorant

```text
Z <= I_primitive <= exp(W_full)
```

is exact, but the second inequality is too lossy to serve as the new DLI
baseline by itself. Modal replay `ap-2EZdsg3MyhkScufWIalOTX` gives the exact
partial raw ledgers through weight 7 on the three C1' kill rows:

| `q` | orbit counts `w=2..7` | `W_<=7` | `(E-1)/(r(1+W_<=7))` |
|---:|---|---:|---:|
| 63361 | `0,1,3,10,36,131` | `141.5` | `3.3497` |
| 65921 | `0,1,3,9,34,119` | `131.5` | `2.4689` |
| 204353 | `0,1,3,6,18,45` | `72.5` | `2.9732` |

Thus extending C1' through weight 7 repairs its literal linear kills. However,
the sufficient one-level 100-bit primitive-mass budget

```text
W_full <= 100 log(2) + log(1/r),       r=q/2^32,
```

is already impossible on the first two rows using only `W_<=7`. Indeed
`q=63361>2^15` makes the right side smaller than `117 log(2)<117`, while
`141.5>117`; and `q=65921>2^16` makes it smaller than
`116 log(2)<116`, while `131.5>116`. Adding higher weights only increases the
left side.

This is a route kill, not a counterexample to the theorem and not a
counterexample to B-WEAK. The loss is specifically

```text
I_primitive <= product_p (1+z_p) <= exp(sum_p z_p),
```

which discards the severe support conflicts among shift shadows and additive
clusters. The next viable interface must retain the primitive conflict graph:
bound `log I_primitive` (or a cluster-corrected pressure) in aggregate, rather
than bound it by the raw total activity `W_full`. No new conditional node is
posed until such an overlap correction has a theorem-scale formulation.

The first such correction is now proved in
`dli_primitive_matching_truncation_majorant`. The support exclusions cap a
compatible primitive collection at `51,102,113`, or at most `127` polymers,
depending on the production level. Weighted clique symmetrization therefore
replaces `exp(W_full)` by the sharper balanced pressure
`(1+W_full/K)^K` (the truncated exponential is an intermediate bound). This
does not yet prove the aggregate pressure budget, but the uncorrected
exponential route is no longer the live endpoint.
