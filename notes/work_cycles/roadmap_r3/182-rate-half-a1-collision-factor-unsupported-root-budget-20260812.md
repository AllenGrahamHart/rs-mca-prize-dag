# Cycle 182: rate-half `A=1` collision factor unsupported-root budget (2026-08-12)

The exact heavy row has only four roots beyond the `e-6` supported
padded-heavy roots. Adding that row to the saturated classified
factor-incidence grid gives, factor by factor,

```text
s_j<=3e n_j-Rm_j,
u_j=m_j-s_j,
sum_j u_j<=4.
```

This raises the large/huge factor thresholds. In the `d_A=1` branch, two
large odd factors cannot fit in total degree `e-2`, and neither can one
huge even factor. The exact trichotomy collapses to profile I: one large
odd factor plus ordinary-even companions.

```text
result:                  PROVED four-root factor-profile compression
DAG delta:               +1 PROVED leaf, 2 req edges, 1 evidence edge
critical status delta:   none
compute:                 378 exact integer checks; no Modal spend
new assumptions:         none
```

The remaining `d_A=1` component has official parameter degree at least
`109951162777`; the next attack is its incompatibility with the quintic
source quotient and correction jets.
