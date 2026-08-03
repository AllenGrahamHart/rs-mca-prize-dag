# Conditional proof

Assume `xr_band_fullrank_window_divisor_count` and
`xr_band_forced_commonroot_syzygy_count`.

Fix one official row and high band-proper depth. If `rank J_d=2d`,
the first premise gives `25|R_d|<=17n^2`.

Otherwise `rank J_d<2d`. Define the forced common-root set `G_d` of
the left syzygy kernel and put `g=|G_d|`. Partition

```text
R_d = R_d^out disjoint-union R_d^G
```

according as some selected off-core point lies outside `G_d` or every
selected off-core point lies in `G_d`. The proved
`xr_deficient_window_rational_direction_payment` gives

```text
|R_d^out| <= n-g.
```

If `g<2(h-d)`, it also gives `R_d^G=empty`, so the desired bound follows.
Otherwise the second premise gives the exact complementary allowance

```text
25|R_d^G| <= 17n^2-25(n-g).
```

Adding the two disjoint currencies yields `25|R_d|<=17n^2`.

The cases are exhaustive and are alternatives for the fixed matrix at
one depth. The full-rank and deficient-rank budgets are not added; only
the proved disjoint partition inside the deficient case is summed. This
proves SL-2-RES conditional on the two named targets.
