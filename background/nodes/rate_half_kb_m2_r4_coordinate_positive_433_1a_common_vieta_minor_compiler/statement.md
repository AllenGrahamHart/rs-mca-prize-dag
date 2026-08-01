# KoalaBear m2 r4 positive 433-1a common Vieta minor compiler

- **status:** PROVED
- **scope:** the five common fibers of the positive residual route
  `433-1a -> O0b`
- **dependencies:**
  `rate_half_kb_m2_r4_order2_coordinate_source_facet_signature`,
  `rate_half_kb_m2_r4_coordinate_complete_fiber_vieta_compiler`, and
  `rate_half_kb_m2_r4_coordinate_positive_433_1a_o0b_signed_edge_atlas`
- **consumer:** `rate_half_band_closure`

Normalize common target representatives to `A=1,B=b,C=c`.  Name the five
common records

```text
roles:     LC,       AB+1, AB+2, AB-, AC
products: -c^2,     b,    b,    -b,  c
sums:      0,        1+b, 1+b,  1-b, 1+c.         (KBPCM-1)
```

The five distinct common quotient labels form two opposite pairs and one
singleton.  There are fifteen assignments of the roles in `(KBPCM-1)` to
that shape.  Choose source square roots so the first pair is
`(1,epsilon_1 i)`, the second is `(r,epsilon_2 i r)`, and the singleton is
`t`, where `i^2=-1` and `epsilon_j in {+1,-1}`.  Thus there are sixty
root-sign rows.  Swapping the two identical `AB+` roles gives the exact
nine role-cell orbits

```text
[0] | [1,2] | [3,6] | [4,7] | [5,8] |
[9,10] | [11] | [12,13] | [14].                  (KBPCM-2)
```

For role `j`, put `lambda_j=z_j^2`, product `p_j`, sum `s_j`, and
`q_j=z_j s_j`.  In coefficient order

```text
(d_0,d_1,d_2,e_0,e_1,e_2,beta_0,beta_1),
A_2=d_0+d_1W+d_2W^2,
A_0=e_0+e_1W+e_2W^2,
B_1=beta_0+beta_1W,
```

the exact positive product and sum rows are

```text
P_j=(-p_j,-p_j lambda_j,-p_j lambda_j^2,
      1,lambda_j,lambda_j^2,0,0),
Q_j=(q_j,q_j lambda_j,q_j lambda_j^2,
      0,0,0,lambda_j,lambda_j^2).                 (KBPCM-3)
```

Let `B` be the six-row matrix consisting of all five `P_j` and the loop
row `Q_LC`.  On the principal stratum `rank B=6`, the full `10 x 8`
common Vieta matrix has rank at most seven if and only if all six minors

```text
det(B,Q_i,Q_j)=0,       1<=i<j<=4                 (KBPCM-4)
```

vanish, where `i,j` run over the four nonloop rows.

Over the deployed field `p=2130706433`, exact symbolic compilation
completed all sixty rows: 360 minors total, with degree histogram
`18:156, 20:16, 21:180, 23:8`, term range `64..240`, and 110 distinct
polynomial digests.  On the admissible open stratum, strip every repeated
factor drawn from the ten source-label differences and

```text
r,t,b,c,b-1,b+1,c-1,c+1,b-c,b+c.                 (KBPCM-5)
```

All sixty stripped rows also compile exactly.  Their 360 minors have degree
histogram

```text
6:4, 7:12, 8:40, 9:16, 10:168, 11:112, 12:8,
```

term range `16..88`, and 110 distinct polynomial digests.  This is a
localization-preserving reduction, not a solution of the minor systems.
The separate branch `rank B<6` is retained and is not deleted by
`(KBPCM-4)`.

This theorem does not solve the six-minor systems, assign the seven
outside fibers, impose their Vieta rows, prove either sign lane realizable
or empty, delete positive coordinate parity, close K3 or a Prize row, or
prove either Prize result.

## Falsifier

An actual principal-stratum common packet outside the fifteen matching
cells or violating `(KBPCM-3)--(KBPCM-4)`, a guard in `(KBPCM-5)` vanishing
on an admissible packet, or a compiled row not matching its direct
`10 x 8` determinant.
