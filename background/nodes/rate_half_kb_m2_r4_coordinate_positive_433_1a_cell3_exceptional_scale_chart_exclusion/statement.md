# KoalaBear positive 433-1a cell-3 exceptional scale-chart exclusion

- **status:** PROVED
- **scope:** every deployed-field point on a denominator, projective-scale,
  projected-scale, or plane-leading zero omitted by the cell-3 compact
  plane-kernel chart, for signs `(-1,-1)`
- **dependencies:**
  `rate_half_kb_m2_r4_coordinate_positive_433_1a_cell3_genus3_plane_kernel_reduction`,
  `rate_half_kb_m2_r4_coordinate_positive_433_1a_common_root_sign_symmetry_quotient`,
  and
  `rate_half_kb_m2_r4_coordinate_positive_433_1a_o0b_signed_edge_atlas`
- **consumer:** `rate_half_band_closure`

Over `F_2130706433`, exact factorization of all six exceptional univariate
scales from the compact cell-3 model gives precisely the base-field roots

```text
0, 1, 16711679, 1288361599, 2113994754, 2130706432. (KBC3E-1)
```

All remaining factors are irreducible cubics and hence have no deployed-field
root.  Intersecting the original seven-element common lex ideal and its full
guard with each value in `(KBC3E-1)` gives the unit ideal except at
`t=1288361599`.  The sole nonunit fiber has basis

```text
t=1288361599,                  r=700051530,
c=736842529 b+915102487,
b^2-891442763 b+1=0.                              (KBC3E-2)
```

The quadratic in `(KBC3E-2)` splits into exactly two deployed points:

```text
(t,r,b,c)=(1288361599,700051530,1068789879,393847656),
(t,r,b,c)=(1288361599,700051530,1953359317,159222518). (KBC3E-3)
```

At either point evaluate the unique common kernel and, for proposed source
roots `z_0,z_1`, put

```text
D_j=A_2(z_j^2),  N_j=A_0(z_j^2),  Q_j=z_j B_1(z_j^2).
```

Every complete outside packet contains distinct source labels carrying
`DE+=de` and `DE-=-de`, so it necessarily satisfies

```text
N_1D_0+N_0D_1=0,
Q_0^2D_1^2-Q_1^2D_0^2-4N_0D_0D_1^2=0.          (KBC3E-4)
```

For each point in `(KBC3E-3)`, saturating `(KBC3E-4)` by `z_0z_1D_0D_1`,
source-label distinctness, and exclusion of all five common labels gives the
unit ideal.  Therefore no complete cell-3 packet lies on any exceptional
scale chart.  The proved source symmetries give the same conclusion for cell
6.

This node does not exclude the main genus-three chart, close `[3,6]`, the
positive route, K3, LIST, MCA, or either Prize problem.

## Falsifier

A deployed-field exceptional root missing from `(KBC3E-1)`, an admissible
common point outside `(KBC3E-3)`, failure of either unit basis, or an actual
complete packet on an exceptional chart that violates the necessary pair
identities `(KBC3E-4)`.
