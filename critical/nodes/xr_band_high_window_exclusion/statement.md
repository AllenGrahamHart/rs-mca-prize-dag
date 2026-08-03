# XR band high-window exclusion (SL-2)

- **status:** TARGET
- **scope:** the three prize rows, where the band occupancy budget binds
- **consumer:** `xr_graded_tangent_band_charge`
- **board alias:** SL-2, unstructured high-window exclusion

Let `(u,v)` be any globally generic-branch received pair after the
ratified strip order, and use the support-wise first-match selector. For
each band-proper high depth

```text
ceil(h/2) <= d <= h-2,
```

let `N_d` be the number of selected depth-`d` joint-explanation pairs
having at least two selected live slopes, exactly as in items 7-9 of
`notes/BAND_LANE_DEFINITIONS.md`. Then

```text
25 N_d <= 17 n^2.                                           (SL2)
```

The constant `17/25=0.68` is deliberately uniform. Together with the
banked low-depth envelope and the stronger cascade cap, the exact
full-band ledger fits the row-specific free budget
`H_band=s_lo-16n^3`. It must not be compared directly with the separate
`0.8008/0.6859/0.6596` single-word window thresholds: those price a
stronger sufficient list-size route, not the selected occupancy asserted
here. The three RowC rows are not claimed here because their occupancy
budgets are vacuous.

The proved `xr_mc_depth_quantization` theorem excludes the canonical
MC/coset construction from every band-proper depth at the official odd
values of `h`. Consequently a falsifier to `(SL2)` must use a
non-coset or finite-characteristic-accidental mechanism. This is a
restriction on known adversaries, not an exhaustive classification of
all supports.

The proved `xr_band_windowed_projection_reduction` gives a sufficient
route through the averaged single-member window counts `W_d(z)`, but
that route is not part of the assertion. Large `W_d(z)` values from
codewords which do not assemble into selected joint pairs do not
refute `(SL2)`.

## Falsifier

One prize-row, globally generic-branch pair `(u,v)`, one depth in the
displayed range, and an auditable support-wise first-match ledger with
`25N_d>17n^2`. A large raw list, an unselected support family, a
cascade-tier family at `d=h-1`, or a RowC fixture is not a falsifier.
