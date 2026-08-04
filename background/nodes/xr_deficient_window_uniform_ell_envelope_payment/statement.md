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
