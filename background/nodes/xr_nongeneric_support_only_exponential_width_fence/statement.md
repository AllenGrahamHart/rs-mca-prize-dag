# XR nongeneric support-only exponential-width fence

- **status:** PROVED
- **consumer:** `xr_tangent_support_mismatch_bridge`
- **scope:** the six clean-rate root parameter triples

At one root write

```text
N=n,       A=K+h,       H=h+1.
```

The support condition available for distinct joint explanations is

```text
|Y|=A,       |Y intersect Y'|<=K-1=A-H.             (XEF1)
```

For every one of the six clean-rate roots there is an abstract family
`mathcal Y` of `A`-subsets of an `N`-set satisfying `(XEF1)` and

```text
|mathcal Y|>16n^3.                                  (XEF2)
```

More precisely, the binary Gilbert construction gives

```text
|mathcal Y|>2^(5A/8).                               (XEF3)
```

Therefore the pairwise support-intersection statement by itself cannot prove
the `16n^3` XR residual budget before the terminal Plotkin window. A closing
argument must use additional RS/codeword realization, first-match ownership,
actual-slope fibers, or another property absent from arbitrary set systems.

This is a route fence. The constructed supports are not claimed to be joint
codeword-pair explanations, and `(XEF2)` is not a counterexample to
`xr_tangent_support_mismatch_bridge`.
