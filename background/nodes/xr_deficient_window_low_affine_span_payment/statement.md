# XR deficient-window low-affine-span payment

- **status:** PROVED
- **consumer:** `xr_band_forced_commonroot_syzygy_count`
- **scope:** three official prize rows, active-defect-local deficient family

Use the exact punctured-list currency from
`xr_deficient_window_active_defect_list_router`. Put

```text
N=n-e,       K=k-ell,       a=k+d,       w=a-K=d+ell,
```

and let `s` be the affine dimension of the surviving parameter set `Tau`
inside `F[X]_{<K}`. Then

```text
|Tau| <= floor(C(N-K+s,s)/C(w+s,s))
       = floor(C(R+ell-e+s,s)/C(d+ell+s,s)).             (LA1)
```

For fixed `s<=10`, the right side is maximized over the complete active
defect range

```text
ceil((2h+2)/3)<=d<=h-2,
1<=ell,       2(h-d)<=e<=d-ell-1
```

at the single corner

```text
d_0=ceil((2h+2)/3),       ell_0=1,
e_0=2(h-d_0).                                             (LA2)
```

Exact official-row evaluation gives:

| rate | paid `s` | worst affine cap | local target budget | first unpaid `s` |
|---|---:|---:|---:|---:|
| `1/4` | `9` | `13,211,041,760,784,548,301,820` | `3,288,278,229,349,592,331,945,250` | `10` |
| `1/8` | `9` | `53,137,761,854,335,542,656,230` | `3,288,278,229,349,592,331,945,250` | `10` |
| `1/16` | `8` | `71,421,853,205,846,145,996,360` | `3,288,278,229,349,592,331,945,250` | `9` |

Here the local target budget is

```text
floor((17n^2-25(n-e))/25),
```

The allowed range has `d<=h-2`, hence `e>=2(h-d)>=4`. The displayed budget
uses `e=4` and is therefore a uniform lower bound, including away from the
cap-maximizing corner. Therefore
`(SL2-D)` is proved whenever

```text
s<=9 at rates 1/4 and 1/8,
s<=8 at rate 1/16.                                      (LA3)
```

Any counterexample has affine parameter dimension at least `10,10,9` on
the three rows. No active-block condition beyond the proved punctured-list
embedding is needed for this payment.

## Falsifier

An allowed official parameter tuple where the affine cap exceeds its value
at `(LA2)`; an exact table mismatch; or an active-defect-local family of
affine dimension at most `9,9,8` violating `(SL2-D)`.
