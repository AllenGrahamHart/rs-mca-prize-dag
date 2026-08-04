# XR deficient window: uniform higher-ell envelope payment

- **status:** PROVED
- **consumer:** `xr_band_forced_commonroot_syzygy_count` (evidence)

For an `r`-point selected block with nonempty `phi=[P:Q]` fiber sizes
`m_i<=ell`, let `T_p(B)` count unordered `p`-subsets using `p` distinct
fibers. Write

```text
r=q ell+u,       0<=u<ell.
```

For every `p>=2`,

```text
T_p(B)>=T_pack,p(r,ell)
 =binom(q,p)ell^p+binom(q,p-1)ell^(p-1)u,           (UE1)
```

and equality is attained by the packed profile `(ell,...,ell,u)`.

Now let the active-defect target family have affine dimension `s` and put

```text
x=d+ell,       y=x+(s-1)(ell-1).
```

If the proved `ell=1` common-ray cap pays at `y`, then the higher-`ell`
family pays at `x`. In particular, the next-dimensional official slices are
proved whenever

```text
rates 1/4,1/8 (s=11): d+11ell-10<=8,500,560,263,
rate 1/16     (s=10): d+10ell-9 <=4,265,559,234.   (UE2)
```

The condition in `(UE2)` automatically gives `r>s ell`, so every selected
block has at least `s+1` `phi` fibers and the full-affine tuple count applies.

This is a conservative uniform envelope. Exact `(UE1)` and lower-dimensional
tuple choices pay additional tuples outside it. Failure of `(UE2)` is not a
falsifier, and the target remains open.

There is also an exact no-go fence for this family of incidence bounds. Put

```text
ell_0=floor((h-4)/7),       r_0=2ell_0+1,
d_0=h-r_0,                  e_0=d_0-ell_0-1.        (UE3)
```

The allowed packed profile `(ell_0,ell_0,1)` has

```text
T_2=ell_0^2+2ell_0,       T_3=ell_0^2,
T_p=0 for p>=4.
```

At the next dimensions, the exact pair and triple incidence caps are:

| rates | pair cap | triple cap | `B_0` |
|---|---:|---:|---:|
| `1/4,1/8` | `45,181,176,163,178,354,561,043,298` | `371,272,336,285,157,761,266,139,535,266,618` | `3,288,278,229,349,592,331,945,250` |
| `1/16` | `77,453,444,237,271,295,453,973,206` | `159,116,714,494,935,354,830,177,169,055,992` | `3,288,278,229,349,592,331,945,250` |

Thus no optimization over tuple order can prove the complete target using
only the current fiber cap, core incidence, and independent block counts.
This is a no-go for those currencies, not a target counterexample: the next
route must exploit realizability or coupling absent from the numerical model.
