# HGE4 Vandermonde-defect band exclusion

- **status:** PROVED
- **closure:** proof
- **consumer:** `f3_hge4_norm_gate_count`
- **dependencies:** `f3_hge4_cyclotomic_haar_near_quarter_swap_router`,
  `f3_hge4_swap_norm_haar_band_exclusion`

Let `m=2^s>=16`, let `p` be prime with `p=1 mod m` and `p>=m^2`, and put

```text
h=m/4-d,       d>=1,       h>=4,
R=log m,       x=4(d+1)R/m,
Y_3=4((d+1)R-d)-8(d+1)^2R^2/m
       +(32/3)(d+1)^3R^3/m^2,
v_h=floor((h-1)/2)+2.                              (VDE1)
```

If

```text
x<=1,       Y_3<=v_h,                              (VDE2)
```

then no primitive exact-level top shift pair of width `h` exists:

```text
E_h^prim(m,p)=0.                                      (VDE3)
```

Indeed, the squared antipodal defect `L` satisfies `L<Y_3`. The consecutive
even moments imply that a nonzero defect needs at least `v_h` nonzero
coordinates and hence `L>=v_h`. Thus the defect vanishes and every pair is
antipodal-swap. Condition `(VDE2)` lies inside the proved swap-norm exclusion
band, which deletes that final class.

The simpler linear condition

```text
4((d+1)R-d)<=v_h
```

implies `(VDE2)` and is retained as a convenient sub-band. For fixed `m`,
`(VDE2)` is an initial interval in `d`. It first admits widths at `m=2^9`,
where `1<=d<=2`. At the largest official level `m=2^41`, it admits exactly

```text
1<=d<=2,677,220,820.
```

Across `m=2^4,...,2^41`, it deletes `5,501,420,621` exact `(m,d)` cells.
This is a width deletion, not a payment for the remaining free-only middle
band or the deeper free/swap aggregate.
