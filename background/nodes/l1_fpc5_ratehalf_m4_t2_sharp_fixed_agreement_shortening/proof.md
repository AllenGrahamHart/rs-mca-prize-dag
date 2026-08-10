# Proof: sharp fixed-agreement shortening

At the sharp endpoint the background has `ell-3` points and both touched
petals have `ell` points, proving `(SH1)`. Every contributor agrees with the
received word on all of `S_0`. Interpolation gives the unique `Q_0` of
degree below `|S_0|`. Therefore `P-Q_0` vanishes on `S_0` and is divisible
by `L_(S_0)`, giving `(SH2)`. The quotient is unique and

```text
deg T <= (k-1)-|S_0|
      =(5ell-5)-(3ell-3)=2ell-2.
```

The core is disjoint from `S_0`, so its locator is nonzero at every core
point and `(SH3)` is defined. For `x in C`, equation `(SH2)` gives

```text
P(x)=U(x)  iff  T(x)=v(x).                            (1)
```

The exact defect locator has `2ell-3` roots in `C`. On its complement the
candidate agrees with `U`; at each defect root it does not agree, by the
exact core-defect condition `gcd(F,W)=1`. Hence `T` has exactly
`(5ell-5)-(2ell-3)=3ell-2` agreements with `v` on `C`. This proves the
injection into `(SH4)`. The arithmetic in `(SH5)` follows directly, since
`N-K_0=3ell-4` and

```text
floor(2(3ell-4)/3)=2ell-3.
```

Finally, `P` is recovered uniquely from `T` by `(SH2)`, so the map is
injective. The remaining FPC5 guards can only shrink the shortened list.
QED.
