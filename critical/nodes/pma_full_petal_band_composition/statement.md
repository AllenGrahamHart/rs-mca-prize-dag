# PMA full-petal band/root composition

- **status:** PROVED
- **role:** corrected carried-layout bridge and reserve full-petal reduction
- **consumer:** `petal_mixed_amplification`, hence `imgfib`

## Statement

Fix one maximal sunflower source with core size `k-1`, `M` pairwise disjoint
petals of size `ell`, and background size `b<ell`. Let a non-planted listed
codeword have exact core defect `d`, exactly `r` background agreements, and a
full-petal pattern touching exactly `t` of the source petals. Then

```text
t ell+r >= d+ell,       0<=r<ell,       2<=t<=M.       (FPC1)
```

The carried G1 chart contains all `M` source petals. Thus its chart-petal
count is `m_chi=M`, not the touched-petal count `t`. If the codeword lies in
the green top band

```text
d>=ell(M-2),                                      (FPC2)
```

then

```text
t in {M-1,M}.                                     (FPC3)
```

Equality `m_chi=t` is therefore not a valid bridge: the one-untouched-petal
stratum is allowed and is realized in the banked G1 audit.

At the L1 lower cutoff, combine the green top-band payment with the `E=0`
case of the petal-pattern root-pinning ledger. Every full-petal class with

```text
d>=ell(M-2)       or       t>=2M-4                 (FPC4)
```

is paid. In the second branch below the band,

```text
e=max(0,2d+1-t ell)=0,
```

so the root-pinning aggregate is polynomial with its fixed `E=0` exponent.
Consequently:

- no non-planted full-petal residual remains for `M<=3`;
- for `M=4`, only the `t in {2,3}` strata can remain;
- in general, an unpaid full-petal family must satisfy

  ```text
  M>=4,       d<ell(M-2),       t<2M-4,
  max(0,2d+1-t ell) -> infinity.                    (FPC5)
  ```

For a below-band word put

```text
a=M-t,       v=ell(M-2)-d>=1.
```

Then the exact deficit coordinates obey

```text
(a-1)ell<=r+v,
e=max(0,ell(M+a-4)-2v+1).                         (FPC6)
```

## Scope

This theorem composes already proved payments on the same carried source
layout. It does not count `(FPC5)`, treat partial petals, create a new profile
owner, or prove `petal_mixed_amplification`. The polynomial conclusion for
the root-pinning branch uses the same lower-cutoff and source-multiplicity
contract as `pma_petal_pattern_root_pinning_ledger`.
