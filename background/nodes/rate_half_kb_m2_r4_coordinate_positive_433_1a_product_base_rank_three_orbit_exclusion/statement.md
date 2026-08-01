# KoalaBear m2 r4 positive 433-1a product-base rank three-orbit exclusion

- **status:** PROVED
- **scope:** common matching cells `0`, `11`, and `14` of the positive route
  `433-1a -> O0b`
- **dependency:**
  `rate_half_kb_m2_r4_coordinate_positive_433_1a_common_vieta_minor_compiler`
- **consumer:** `rate_half_band_closure`

Let `P` be the `5 x 6` matrix of the five common product rows, and let
`D_j` be its minor obtained by omitting column `j`, indexed from zero.  On
the admissible source/target guard stratum, `rank P=5` in each of the three
singleton duplicate-role orbits

```text
cell 0:  singleton LC,  pairs (AB+1,AB+2),(AB-,AC);
cell 11: singleton AB-, pairs (LC,AC),(AB+1,AB+2);
cell 14: singleton AC,  pairs (LC,AB-),(AB+1,AB+2). (KBPBR-1)
```

The exact certificates over the deployed field are:

1. In cell 11, `D_1` is a nonzero scalar times

```text
r^2(r^2-1)(r^2+1)(t^2-1)(t^2+1)b c(c+1).         (KBPBR-2)
```

2. In cell 0, guard stripping gives `D_1 ~ b+c^2`.  If `b=-c^2`,
   the specialized `D_0` is a nonzero scalar times

```text
(t^2-1)(t^2+1) r^4 c^3(c+1).                     (KBPBR-3)
```

3. In cell 14, guard stripping gives `D_1 ~ -b+c^2`.  Put
   `R=r^4,T=t^4` after imposing `b=c^2`.  Two further stripped minors are

```text
E_2=-cR+2cT-c-R+1,
E_5=-cR+c-R+2T-1.                                (KBPBR-4)
```

   They satisfy

```text
c E_5-E_2=-(c^2-1)(R-1),                          (KBPBR-5)
```

   which is nonzero on the target/source distinctness guards.

The loop sum row has nonzero last-two-column support while all product rows
have zero last-two-column support.  Therefore `rank B=rank P+1=6` in these
three cells.  Their base-rank-drop branches are empty.

The other six role orbits remain open.  This theorem does not solve a
principal pivot chart, impose outside rows, delete `433-1a -> O0b`, close
positive coordinate parity, close K3 or a Prize row, or prove either Prize
result.

## Falsifier

An admissible deployed-field point in cell 0, 11, or 14 with `rank P<5`, or
failure of one of the polynomial-division identities `(KBPBR-2)--(KBPBR-5)`.
