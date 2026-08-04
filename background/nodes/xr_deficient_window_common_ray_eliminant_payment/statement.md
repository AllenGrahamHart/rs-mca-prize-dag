# XR deficient window: common-ray eliminant payment

- **status:** PROVED
- **consumer:** `xr_band_forced_commonroot_syzygy_count` (evidence)

Let `A_m` be any `m`-dimensional affine slice of an active-defect parameter
hull, and fix `m+1` points `x_0,...,x_m in D` with pairwise distinct values
of `phi=[P:Q]`. Then

```text
N_(A_m)(x_0,...,x_m)<=m+1,                          (CRE1)
```

where the left side counts target parameters for which the fixed tuple lies
in one selected block. This improves the generic `2^m` affine Bezout cap.

If the full hull has dimension `s`, cutting by `s-m` independent core
hyperplanes and counting distinct-fiber tuples gives

```text
2|Tau| B_(s-m) T_(m+1)
 <=(m+1)binom(N,s-m)binom(e,m+1),                   (CRE2)

B_(s-m)=product_(j=m+1)^s(w+j)/(s-m)!,
```

where `T_(m+1)` is the number of distinct-`phi` `(m+1)`-tuples in a
selected block. In particular, on the full hull with `ell=1`,

```text
|Tau| <= (s+1)binom(e,s+1)/(2binom(r,s+1)).         (CRE3)
```

At the next unpaid affine dimensions, `(CRE3)` pays through

| rates | `s` | last paid `d+1` | floor of cap there | floor at next value |
|---|---:|---:|---:|---:|
| `1/4,1/8` | 11 | `8,500,560,263` | `3,288,277,985,160,426,079,436,569` | `3,288,278,431,308,817,786,569,954` |
| `1/16` | 10 | `4,265,559,234` | `3,288,277,482,901,370,162,501,687` | `3,288,278,721,352,163,199,241,837` |

The conservative local budget remains

```text
B_0=3,288,278,229,349,592,331,945,250.              (CRE4)
```

The next values are failures of this cap only. The final `ell=1` tails,
higher `ell`, and split-pencil endpoint remain open.
