# KoalaBear positive 433-1a cell-4 exceptional scale-chart exclusion

- **status:** PROVED
- **scope:** every deployed-field zero of a denominator, removed common scale,
  or plane-leading coefficient omitted by the compact cell-4 chart
- **dependencies:**
  `rate_half_kb_m2_r4_coordinate_positive_433_1a_cell4_genus1_plane_kernel_reduction`
  and
  `rate_half_kb_m2_r4_coordinate_positive_433_1a_common_root_sign_symmetry_quotient`
- **consumer:** `rate_half_band_closure`

Exact factorization over `F_2130706433` of all six omitted scales gives the
complete base-field root set

```text
t in {0,1,16711679,2113994754,2130706432}.       (KBC4E-1)
```

All non-linear factors are irreducible cubics and have no deployed-field
root.  Since `16711679^2=-1`, every value in `(KBC4E-1)` satisfies

```text
t(1-t^2)(1+t^2)=0.                               (KBC4E-2)
```

The factor in `(KBC4E-2)` is part of the original common-curve guard.
Therefore its localization contains `1` at every deployed exceptional scale
zero, and no admissible common point, hence no complete packet, lies on an
exceptional cell-4 chart.  Source symmetry gives the same conclusion for
cell 7.

This node does not exclude the main genus-one chart, close `[4,7]`, the
positive route, K3, LIST, MCA, or either Prize problem.

## Falsifier

A missing deployed-field scale root, a non-linear factor with a base-field
root, a value in `(KBC4E-1)` not satisfying `(KBC4E-2)`, or an admissible
common point on one of these guard-zero charts.
