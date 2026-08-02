# KoalaBear m2 r4 positive 433-1b common Vieta minor compiler

- **status:** PROVED
- **scope:** the five common fibers of the positive residual route
  `433-1b -> O0a`
- **dependencies:**
  `rate_half_kb_m2_r4_order2_coordinate_source_facet_signature`,
  `rate_half_kb_m2_r4_coordinate_complete_fiber_vieta_compiler`, and
  `rate_half_kb_m2_r4_coordinate_positive_433_1b_o0a_signed_edge_atlas`
- **consumer:** `rate_half_band_closure`

Normalize common target representatives to `A=1,B=b,C=c`.  Name the five
common records

```text
roles:     LA,    AB,   AC,   BC+,   BC-
products: -1,     b,    c,    bc,    -bc
sums:       0,   1+b,  1+c,  b+c,    b-c.        (KBP1BC-1)
```

The five distinct common quotient labels form two opposite pairs and one
singleton.  There are fifteen assignments of the five roles to that shape.
Choose source square roots so the first pair is `(1,epsilon_1 i)`, the
second is `(r,epsilon_2 i r)`, and the singleton is `t`, where `i^2=-1`
and `epsilon_j in {+1,-1}`.  Thus there are sixty matching/root-sign rows.
No role quotient is assumed.

For role `j`, put `lambda_j=z_j^2`, product `p_j`, sum `s_j`, and
`q_j=z_j s_j`.  In coefficient order

```text
(d_0,d_1,d_2,e_0,e_1,e_2,beta_0,beta_1),
A_2=d_0+d_1W+d_2W^2,
A_0=e_0+e_1W+e_2W^2,
B_1=beta_0+beta_1W,
```

the exact positive Vieta rows are

```text
P_j=(-p_j,-p_j lambda_j,-p_j lambda_j^2,
      1,lambda_j,lambda_j^2,0,0),
Q_j=(q_j,q_j lambda_j,q_j lambda_j^2,
      0,0,0,lambda_j,lambda_j^2).                 (KBP1BC-2)
```

Let `B` consist of all five product rows and the loop row `Q_LA`.  On the
principal stratum `rank B=6`, the full `10 x 8` common Vieta matrix has
rank at most seven if and only if all six minors

```text
det(B,Q_i,Q_j)=0,       1<=i<j<=4                 (KBP1BC-3)
```

vanish over the four nonloop sum rows.

Exact Modal compilation over `F_2130706433` completed all sixty rows in
both raw and guard-stripped modes.  The 360 raw minors have degree histogram

```text
18:72, 19:84, 21:104, 22:88, 23:4, 24:8,
```

term range `80..204`, and 165 distinct digests.  Stripping repeated factors
from the ten source-label differences and

```text
r,t,b,c,b-1,b+1,c-1,c+1,b-c,b+c                  (KBP1BC-4)
```

gives degree histogram

```text
8:4, 9:52, 10:16, 12:120, 13:144, 14:24,
```

term range `20..100`, again with 165 distinct digests.  Every raw and
stripped row has six distinct minors.

This is an exact compiler on the base-rank-six stratum.  It does not delete
the base-rank-drop branch, solve a common ideal, close the route, K3, LIST,
MCA, or either Prize result.

## Falsifier

A missing role assignment/root-sign row, incorrect Vieta row, failed minor
equivalence on `rank B=6`, invalid guard division, or compilation mismatch.
