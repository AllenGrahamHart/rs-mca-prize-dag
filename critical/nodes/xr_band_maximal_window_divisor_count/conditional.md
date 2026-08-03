# Conditional proof

Assume `xr_band_fullrank_window_divisor_count` and
`xr_band_forced_commonroot_syzygy_count`.

Fix one official row and high band-proper depth. If `rank J_d=2d`,
the first premise gives `25|R_d|<=17n^2`.

Otherwise `rank J_d<2d`. Define the forced common-root set `G_d` of
the left syzygy kernel. If `|G_d|<2(h-d)`, the proved
`xr_deficient_window_rational_direction_payment` gives the stronger
bound `|R_d|=N_d<=n`. If `|G_d|>=2(h-d)`, the second premise gives
the required bound directly.

The cases are exhaustive and are alternatives for the fixed matrix at
one depth, so their bounds are not added. This proves SL-2-RES
conditional on the two named targets.
