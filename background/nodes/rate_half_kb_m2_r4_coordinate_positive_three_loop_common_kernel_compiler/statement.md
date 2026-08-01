# KoalaBear m2 r4 positive coordinate three-loop common-kernel compiler

- **status:** PROVED
- **scope:** the five common fibers of every positive coordinate three-loop
  packet in profile `(4,4,2)` or `(4,3,3)`
- **dependencies:**
  `rate_half_kb_m2_r4_coordinate_coefficient_normal_form` and
  `rate_half_kb_m2_r4_coordinate_positive_loop_ramification_gate`
- **consumer:** `rate_half_band_closure`

Normalize the two ramified loop labels and the unique nonramified loop label
to `W=0,infinity,1`.  Write their signed target representatives as
`a_0,a_infinity,a_1`, and put

```text
A_2(W)=d_0+d_1 W+d_2 W^2,       B_1(W)=beta(W-1). (KBP3K-1)
```

The three loop product rows force

```text
A_0(W)=-a_0^2 d_0
 +((a_0^2-a_1^2)d_0-a_1^2 d_1
   +(a_infinity^2-a_1^2)d_2)W
 -a_infinity^2 d_2 W^2.                         (KBP3K-2)
```

For either remaining common edge, with source lift `z`, quotient label
`W=z^2`, target product `p`, and target sum `s`, its exact product and sum
rows on `h=(d_0,d_1,d_2,beta)^T` are

```text
[-a_0^2+(a_0^2-a_1^2)W-p,
 -(a_1^2+p)W,
 (a_infinity^2-a_1^2)W-(a_infinity^2+p)W^2,
 0],

[s,sW,sW^2,z(W-1)].                              (KBP3K-3)
```

Thus the two nonloop edges give one exact `4 x 4` common matrix `M`, and
every packet satisfies `M h=0` with `beta!=0` and `A_2` nonzero at all five
common labels.  Conversely, an admissible kernel vector with those guards
reconstructs all five common Vieta rows.

For representative loop/edge placements the determinant has only one
nonguard factor.  With loops `1,b,c` at `0,infinity,1`, respectively:

```text
442: edges {1,b} at x and {1,-b} at y,
R_442=(y-x)(b^2-c^2)+bxy(x+y)(c^2-1);             (KBP3K-4)

433: edges {1,b} at x and {1,c} at y,
R_433=(y-x)(b^2-c^2)
      +(c-1)xy(b(c+1)x-(b^2+c)y).                 (KBP3K-5)
```

Away from the displayed source/target collision guards, `det M=0` is
equivalent to the corresponding `R=0`.  Other loop placements are covered
by the generic matrix `(KBP3K-3)`, not silently identified with these two
representatives.

This theorem does not prove that either residual has no guarded solution,
that every residual solution has an admissible kernel, that the outside
rows interpolate, that either three-loop profile is empty, or either Prize
result.

## Falsifier

An actual packet violating `(KBP3K-1)--(KBP3K-3)`, a guarded representative
whose determinant does not factor as `(KBP3K-4)` or `(KBP3K-5)`, or an
admissible common kernel which fails one of the five original Vieta rows.
