# XR deficient window: full-affine tuple payment

- **status:** PROVED
- **consumer:** `xr_band_forced_commonroot_syzygy_count` (evidence)

Let `Tau` be an active-defect target family with affine hull `A` of dimension
`s>=1`. Use

```text
r=h-d,       e=|D|,       phi=[P:Q],
gcd(P,Q)=1,  max(deg P,deg Q)=ell.
```

Fix `s+1` points of `D` with pairwise distinct `phi` values. At most `2^s`
parameters of `Tau` can have all of those points in one selected block:

```text
N_A(x_0,...,x_s)<=2^s.                              (FAT1)
```

Consequently, if `r>s ell`, the fiber cap and the at least two selected
blocks per target give

```text
|Tau| <= 2^(s-1) product_(j=0)^s(e-j)
                    /product_(j=0)^s(r-j ell).       (FAT2)
```

For `ell=1`, `phi` is injective on the evaluation domain and the exact form is

```text
|Tau| <= 2^(s-1) binom(e,s+1)/binom(r,s+1).         (FAT3)
```

At the next unpaid affine dimensions and with the conservative local budget

```text
B_0=floor((17n^2-25(n-4))/25),
```

`(FAT3)` pays the `ell=1` slices through

| rates | `s` | last paid `d+1` | floor of cap there | floor at next value |
|---|---:|---:|---:|---:|
| `1/4,1/8` | 11 | `8,453,534,100` | `3,288,278,171,041,750,515,498,549` | `3,288,278,464,999,855,263,825,729` |
| `1/16` | 10 | `4,250,714,177` | `3,288,277,590,015,144,864,544,565` | `3,288,278,415,892,044,198,197,313` |

Here

```text
B_0=3,288,278,229,349,592,331,945,250.              (FAT4)
```

The next printed value is only the first failure of this particular cap, not
a counterexample. The residual `ell=1` tails and all other unpaid strata stay
open, so no critical status changes.
