# KoalaBear positive 433-1a cells 1/2 common root-sign orbit exclusion

- **status:** PROVED
- **scope:** the eight common matching/root-sign rows in cells `1` and `2`
  of the deployed positive residual route `433-1a -> O0b`
- **dependencies:**
  `rate_half_kb_m2_r4_coordinate_positive_433_1a_common_vieta_minor_compiler`
  and
  `rate_half_kb_m2_r4_coordinate_positive_433_1a_common_root_sign_symmetry_quotient`
- **consumer:** `rate_half_band_closure`

For cell `1`, one representative of each exact sign-product class has
guard-saturated common ideal

```text
<M_12,M_13,M_14,M_23,M_24,M_34, zG-1>
    = <1> in F_2130706433[z,t,r,c,b].             (KBC12-1)
```

Here the `M_ij` are the six stripped `8 x 8` Vieta minors and `G` is the
product of all ten source-label differences and the ten printed nonzero,
target-collision, and target-distinctness guards.  Exact Singular standard
bases give `(dimension,size)=(-1,1)` for both
`(epsilon_1,epsilon_2)=(-1,-1)` and `(-1,+1)`.  In each case the smaller
three-minor chart ideal is independently already `<1>`.

The two representatives cover the two invariants
`epsilon_1 epsilon_2=+1,-1`.  Source reciprocity supplies the other sign in
each class, and duplicate-`AB+` transport exchanges cells `1` and `2`.
Consequently all eight common rows in those cells are empty.

Together with the earlier cell-5/8 exclusion, this leaves exactly seven
unclosed common symmetry representatives, covering 44 raw rows.

This does not delete those seven representatives, close the positive
route, K3, a Prize row, LIST, or MCA.

## Falsifier

An admissible zero of either saturated ideal, a mismatch between the
hash-pinned compiler input and the Singular program, or a failure of the
proved two-class cells-1/2 symmetry.
