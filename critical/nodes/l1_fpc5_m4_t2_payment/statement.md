# L1 FPC5 `M=4,t=2` payment

- **status:** CONDITIONAL
- **consumer:** `l1_full_petal_fpc5_payment`

Only rates `1/2` and `1/4` can retain a strict `M=4,t=2` full-petal
residual. They are disjoint, and source-layout multiplicity is removed by
`l1_general_first_layout_domination`.

At rate `1/4`, the source equation gives

```text
4ell+b=3k+1,       b<ell,
```

so `5ell>3k+1` and therefore `2ell>k-1`. Two degree-`<k` codewords agreeing
with `U` on one touched pair of full petals must be equal. One fixed `M=4`
layout has six unordered pairs, hence at most six non-planted contributors;
the global first-layout remainder adds at most four anchors. This branch is
proved polynomial.

The remaining rate-half child writes

```text
d=ell+s,       0<=s<ell,       e=2s+1->infinity.
```

For each touched pair, `pma_two_full_petal_linear_slice_reduction` injects the
contributors into the exact petal-equation envelope of primitive cofactor
pairs `deg A_1,deg A_2<=s` through

```text
F=(L_1A_1-L_2A_2)/(c_2-c_1).
```

The exact cell additionally requires `W=0` on its selected background
agreements and excludes agreements outside the printed pattern. First-layout
domination reduces its aggregate payment to one fixed maximal source plus at
most four anchors.

The proved official codimension sieve removes the apparent endpoint:

```text
rate 1/2:   locator codimension >= 2,
rate 1/4:   locator codimension >= (k+4)/5.
```

At the apparent sharp rate-half codimension-two boundary, every background
point is forced to be an agreement. The proved guarded-slice reduction then
cuts the locator dimension from `2ell-4` to `ell-1`, giving true codimension
`ell-1`. Thus the only remaining hypothesis is
`l1_fpc5_ratehalf_m4_t2_payment`: the split-locator/internal-owner count in
the rate-half guarded slices.
