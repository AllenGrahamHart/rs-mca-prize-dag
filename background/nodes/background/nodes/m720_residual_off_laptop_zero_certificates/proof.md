# proof: m720_residual_off_laptop_zero_certificates

The proved node `m720_residual_slice_metadata` classifies every residual
configured h=7..20 cell under the Modal window-selection rule. All residual
cells are either `W<n` window slices, or one of exactly two over-ceiling
complete-window cells:

```text
n=32, h=16, q_exp=2
n=32, h=16, q_exp=3
```

Window slices are not promoted to global zero certificates. The proved node
`m720_overceiling_complete_window_certificates` handles the two complete-window
exceptions by algebra: the only anchored complete-window trade is the paid
toral even/odd coset partition, so the unpaid non-toral count is zero.

Thus every residual cell is either a non-certificate slice or a complete cell
with zero unpaid non-toral anchored active cores.
