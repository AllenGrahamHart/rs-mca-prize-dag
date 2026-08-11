# Two-type-1 fibre spend calibration

- **status:** PROVED
- **closure:** proof
- **consumer:** `rate_half_band_crossing_location`

Retain the strict endpoint parameters

```text
N=16m,       rho=4m-1,       a=|W|=7m-1,
```

with `4|m`. Let `V` be the two-dimensional representation space whose
projective members are `z_g`, and let `W` be its joint support. For each
`x in W`, evaluation on `V` has a unique projective kernel. This defines
the fibre partition

```text
W = disjoint_union_g F_g,       n_g=|F_g|,
supp(z_g)=W\F_g.                                      (TFC1)
```

For a supported slope `gamma` with root set `S_gamma`, minimum joint-support
minimality gives, for every `g!=gamma`,

```text
|S_gamma intersect supp(z_g)|<=|S_gamma|-n_g.         (TFC2)
```

Consequently, for distinct `g_1,g_2`, both different from `gamma`,

```text
|S_gamma intersect W|
 <=2|S_gamma|-n_(g_1)-n_(g_2),
|S_gamma\W|>=n_(g_1)+n_(g_2)-|S_gamma|.              (TFC3)
```

In the stratum with exactly two type-1 slopes `g_1,g_2`, their root sets are
`supp(z_(g_i))` and have size at most `rho`. Hence

```text
n_(g_i)>=a-rho=3m,
|S_gamma\W|>=2m+1                                    (TFC4)
```

for every type-2 slope `gamma`.

This is a valid algebraic improvement over the minimum-distance spend, but
it does not close the printed outside-capacity ledger. With
`C=(N-a)m=(9m+1)m`, `(TFC4)` gives only

```text
T<=2+floor(C/(2m+1))=9m/2,                            (TFC5)
```

whereas the target is `4m`.

The exact concentration needed for the lower bound in `(TFC3)` to reach the
calibrated closing spend `p_req=9m/4+1` is

```text
n_(g_1)+n_(g_2)>=rho+p_req=25m/4.                    (TFC6)
```

Thus the two-type-1 baseline is short by exactly `m/4` fibre points. If
`d_i=rho-|S_(g_i)|`, condition `(TFC6)` is equivalently
`d_1+d_2>=m/4`; it leaves at most `3m/4-1` points of `W` in all other
fibres.

This theorem calibrates the two-fibre mechanism. It does not assert that
two type-1 slopes exist, that `(TFC6)` is forced, or that the bound in
`(TFC3)` is tight for a realizable pencil.
