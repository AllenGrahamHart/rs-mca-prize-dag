# XR five-row rank-two full cores have a negative-baseline rank floor

- **status:** PROVED
- **closure:** proof
- **consumer:** `xr_highcore_collision_count`
- **dependencies:** `xr_rank_two_zero_baseline_arithmetic_router`,
  `xr_rank_two_maxwell_collision_defect_identity`,
  `xr_higher_rank_rank_two_shell_maxwell_router`

Use an official uniform rank-two relation with exactly five active rows, and
assume those rows are exactly all blocks of one minimal Maxwell core. Put

```text
D=d+1,       Z=sum_i z_i,
D_0=5h+12D-6Z.                                      (F5N1)
```

Then `D_0<0`. Writing `b=-D_0`, one has

```text
b>0,       b congruent -5h (mod 6).                 (F5N2)
```

Let `b_0` be the least positive integer in that residue class. The zero-fiber
degree cap and disjointness give

```text
Z<=5(D-1),       Z<=a+D,
D >= D_min:=ceil((5h+b_0+30)/18),
a >= a_min:=(5h+6D_min+b_0)/6.                      (F5N3)
```

The exact official floors are:

| rows | `h mod 6` | `b mod 6` | `b_0` | `D_min` | necessary `a_min` |
|---|---:|---:|---:|---:|---:|
| RowC `1/4,1/8` | `5` | `5` | `5` | `4` | `9` |
| RowC `1/16` | `3` | `3` | `3` | `3` | `6` |
| prize `1/4,1/8` | `3` | `3` | `3` | `2386092945` | `9544371773` |
| prize `1/16` | `5` | `5` | `5` | `1193046474` | `4772185889` |

There is also an exact defect window. If

```text
C=3I+sigma+H
```

is the collision-defect charge and `e` is the minimal-core surplus, then

```text
b=e+2C,       0<=e<=h-1,
ceil(max(0,b-h+1)/2)<=C<=floor(b/2).                (F5N4)
```

In particular the minimum-baseline RowC cases require `C>=1`; the two prize
reserve classes permit `C=0` at their minimum baseline.

This theorem does not treat a proper five-block circuit inside a larger core,
count any surviving high-rank full core, handle another active-row arity,
classify higher trade rank or nonuniform cells, or prove P-A.
