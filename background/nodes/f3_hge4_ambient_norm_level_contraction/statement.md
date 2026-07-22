# HGE4 ambient-prime exact-level contraction

- **status:** PROVED
- **consumer:** `f3_hge4_norm_gate_count`
- **dependencies:** `f3_hge4_exact_ratio_tower_orbit_compiler`,
  `f3_hge4_cyclotomic_norm_quarter_width_exclusion`,
  `f3_hge4_nonfull_complement_third_gate`,
  `f3_hge4_vandermonde_defect_band_exclusion`,
  `f3_hge4_primitive_swap_odd_moment_router`,
  `f3_hge4_swap_norm_haar_band_exclusion`

Let

```text
n=2^s,       13<=s<=41,
m=2^r | n,  4<=r<=s,
p prime,     p=1 mod n,       p>=n^2.                (ALC1)
```

Define the ambient cutoff

```text
c_(n,m)=2 ceil(mr/(8s)).                              (ALC2)
```

There is a stronger exact per-width gate. Put

```text
u_h=floor(h/2),       v_h=floor((h-1)/2)+2.
```

If `4<=h<m/4` and

```text
n^(2u_h)>=(4h-v_h)^(m/4),                            (ALC2-exact)
```

then `E_h^prim(m,p)=0`. This exact predicate can delete widths below
`c_(n,m)`; it is intentionally not advertised as one parity-free interval.

For the primitive exact-ratio orbit count from the tower compiler,

```text
E_h^prim(m,p)=0       whenever
max(4,c_(n,m))<=h<m/3.                               (ALC3)
```

Equivalently, after the complement-third and quarter-width exclusions, the
coarse live exact-level envelope contracts to

```text
4<=h<=c_(n,m)-1.                                     (ALC4)
```

The cutoff always satisfies `c_(n,m)<=m/4`. At the top level `m=n` it is
exactly `m/4`, so the closed-form envelope `(ALC4)` reproduces the existing
lower-quarter frontier; `(ALC2-exact)` can still delete individual top-level
widths.
At every proper official level it is at most `m/4-2`, so the range contracts
strictly. This retains the stronger ambient prime size rather than weakening
`p>n^2` to `p>m^2`.

Across all official ambient exponents `13<=s<=41`, `(ALC3)` deletes exactly
`55,050,457,488` additional lower-quarter `(n,m,h)` cells. At the largest
ambient order `n=2^41`, it deletes `26,817,356,728` cells; the two largest
proper levels have

```text
m=2^40: c_(n,m)=268,173,567,752,
m=2^39: c_(n,m)=130,734,614,280,                    (ALC5)
```

and each loses `6,704,339,192` widths. The exact levels `m=32` and `m=64`
are empty in the remaining `h>=4` scope at that ambient row.

The count above records only the closed-form cutoff `(ALC2)`. Additional
cells removed by `(ALC2-exact)` are a strict bonus and must be tested with
their actual parity.

This is a width exclusion, not an orbit estimate. It does not bound any
surviving level sum, prove `(ERT4)`, or promote HGE4.
