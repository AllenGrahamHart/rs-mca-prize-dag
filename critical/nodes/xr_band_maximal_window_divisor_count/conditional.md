# Conditional proof

Assume `xr_band_fullrank_window_divisor_count` and
`xr_band_forced_commonroot_syzygy_count`.

Fix one official row and high band-proper depth. If `rank J_d=2d`,
the first premise gives `25|R_d|<=17n^2`.

Otherwise `rank J_d<2d`. Use the primitive pair supplied by the proved
Padé router, let `D` be the support of its invariant residual, and put
`e=|D|`. Partition

```text
R_d = R_d^out disjoint-union R_d^D
```

according as some selected off-core point lies outside `D` or every
selected off-core point lies in `D`. The proved
`xr_deficient_window_active_defect_list_router` gives

```text
|R_d^out| <= n-e.
```

If `e<2(h-d)`, it also gives `R_d^D=empty`, so the desired bound follows.
Otherwise the second premise gives the exact complementary allowance

```text
25|R_d^D| <= 17n^2-25(n-e).
```

Adding the two disjoint currencies yields `25|R_d|<=17n^2`.

The cases are exhaustive and are alternatives for the fixed matrix at
one depth. The full-rank and deficient-rank budgets are not added; only
the proved disjoint partition inside the deficient case is summed. This
proves SL-2-RES conditional on the two named targets.
