# KoalaBear m2 r4 positive 433-1a product-base rank five-orbit exclusion

- **status:** PROVED
- **scope:** five of the nine common role orbits for the positive route
  `433-1a -> O0b`
- **dependencies:**
  `rate_half_kb_m2_r4_coordinate_positive_433_1a_common_vieta_minor_compiler`
  and
  `rate_half_kb_m2_r4_coordinate_positive_433_1a_product_base_rank_three_orbit_exclusion`
- **consumer:** `rate_half_band_closure`

In addition to singleton cells `[0]`, `[11]`, and `[14]`, the product block
has rank five throughout the duplicate-role orbits `[4,7]` and `[5,8]`.
Consequently the six-row base has rank six in exactly the five certified
role orbits

```text
[0], [4,7], [5,8], [11], [14].                   (KBPB5-1)
```

For cells `4,7`, put `R=r^2,T=t^2` and

```text
A=-RT+3R+3T-1,       B=(R+1)(T+1).
```

Two stripped maximal product minors are

```text
E_1=bA+c^2B,          E_4=-bB-c^2A.               (KBPB5-2)
```

Their coefficient determinant is

```text
B^2-A^2=8(R-1)(T-1)(R+T),                         (KBPB5-3)
```

which is nonzero by source-label distinctness.

For cells `5,8`, put

```text
S=R+T,  B=(R+1)(T+1),  C=(R-1)(T-1).
```

Two stripped maximal product minors are

```text
F_1=2bS+c^2B+cC,
F_4=b(cC+B)+2c^2S.                                (KBPB5-4)
```

Eliminating `b` without division gives

```text
c[(cB+C)(cC+B)-4cS^2]=cBC(c+1)^2,                (KBPB5-5)
```

again nonzero on the admissible stratum.

The four role orbits `[1,2]`, `[3,6]`, `[9,10]`, and `[12,13]` retain a
base-rank-drop branch.  This theorem does not solve a principal chart,
append outside rows, delete `433-1a -> O0b`, close positive coordinate
parity, close K3 or a Prize row, or prove either Prize result.

## Falsifier

An admissible point in cells `4,5,7,8` with product rank below five, or
failure of `(KBPB5-2)--(KBPB5-5)`.
