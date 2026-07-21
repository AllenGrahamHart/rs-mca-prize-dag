# HGE4 swap-norm and Haar-band exclusion

- **status:** PROVED
- **closure:** proof
- **consumer:** `f3_hge4_norm_gate_count`
- **dependencies:** `f3_hge4_primitive_swap_odd_moment_router`,
  `f3_hge4_cyclotomic_haar_near_quarter_swap_router`

Let `m=2^s>=16`, let `p` be prime with `p=1 mod m` and `p>=m^2`, and let
`h` be odd. A primitive exact-level antipodal-swap pair of width `h` can exist
only if

```text
m^(h-1)<h^(m/4).                                    (SNH1)
```

Therefore the swap class is empty whenever

```text
m^(h-1)>=h^(m/4).                                   (SNH2)
```

In particular, put `h=m/4-d`, `d>=1`. Every swap pair is absent throughout
the explicit dyadic band

```text
s(d+1)<=m/2.                                        (SNH3)
```

Equivalently, the band contains

```text
1<=d<=floor(m/(2s))-1.                              (SNH4)
```

At `m=2^41`, this is `1<=d<=26,817,356,774`.

For the exact Haar-router band, put

```text
X=4(d+1)log m,       B=2^ceil(log_2 X),
B<h,       BX<m^(1-(4d+8B)/m).                     (SNH5)
```

This band lies inside `(SNH3)`; the closed-form condition
`64(d+1)^2(log m)^2<m` is a sufficient sub-band. The dependency proves that
every pair in `(SNH5)` is antipodal-swap; `(SNH2)` then excludes that swap.
Hence

```text
E_h^prim(m,p)=0       throughout the full Haar band. (SNH6)
```

At this node's standalone interface, outside the Haar overlap `(SNH3)`
deletes only the swap class, so free pairs remain possible. The downstream
Vandermonde-defect theorem deletes a much larger initial part of that region.
This theorem does not count the residual free pairs, settle deeper widths,
prove the exact-level aggregate, or close HGE4.
