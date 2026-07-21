# HGE4 cyclotomic-Haar near-quarter swap router

- **status:** PROVED
- **closure:** proof
- **consumer:** `f3_hge4_norm_gate_count`
- **dependencies:** `f3_hge4_exact_ratio_tower_orbit_compiler`,
  `f3_hge4_primitive_swap_odd_moment_router`

Let `m=2^r>=16`, let `p` be prime with `p=1 mod m` and `p>=m^2`, and put

```text
h=m/4-d,       d>=1,       h>=4.                    (CHQ1)
```

Write

```text
R=log m,       X=4(d+1)R,
T=ceil(log_2 X),       B=2^T.
```

If the exact last-stage inequalities

```text
B<h,       BX<m^(1-(4d+8B)/m)                      (CHQ2-exact)
```

hold, then every primitive exact-level top shift pair of width `h` is
antipodal-swap: its two reciprocal root supports are `I` and `I+m/2`.

The simpler closed-form condition

```text
64(d+1)^2(log m)^2<m,                               (CHQ2)
```

implies `(CHQ2-exact)`. Here and below `log` is the natural logarithm.

Consequently:

1. `E_h^prim(m,p)=0` when `h` is even;
2. when `h` is odd, every exact-level orbit lies in the proved primitive swap
   class and is routed to the half-order perfect-square support test;
3. no free-stabilizer orbit can occur in this growing near-quarter band.

The exact condition first admits widths at `m=2^15`, where it contains
`1<=d<=2`. At the largest official level `m=2^41`, it contains exactly
`1<=d<=9223`. The closed-form sub-band reaches `1<=d<=6521` there.

This is a structural deletion/router. It does not bound the odd swap count,
sum the remaining lower-quarter widths, prove the exact-level budget, or
close HGE4.
