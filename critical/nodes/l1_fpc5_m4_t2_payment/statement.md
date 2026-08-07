# L1 FPC5 `M=4,t=2` payment

- **status:** TARGET
- **consumer:** `l1_full_petal_fpc5_payment`

Only rates `1/2` and `1/4` can retain a strict `M=4,t=2` full-petal
residual. Write

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
agreements, excludes agreements outside the printed pattern, and retains
first ownership. The target is a disjoint polynomial/profile allocation of
the guarded members for which `F` is a monic degree-`d` locator split on the
source core, summed over all first-owned sources and touched pairs.

The proved official codimension sieve removes the apparent endpoint:

```text
rate 1/2:   locator codimension >= 2,
rate 1/4:   locator codimension >= (k+4)/5.
```

At the apparent sharp rate-half codimension-two boundary, every background
point is forced to be an agreement. The proved guarded-slice reduction then
cuts the locator dimension from `2ell-4` to `ell-1`, giving true codimension
`ell-1`. Thus the next task is the split-locator/ownership count in this
background-guarded slice, not a codimension-two count in the full locator
space.
