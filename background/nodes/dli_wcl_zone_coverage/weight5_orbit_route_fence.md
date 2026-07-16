# Weight-five affine-orbit route fence

Date: 2026-07-13.

This packet sizes the direct terminal norm-census route. The orbit count is
exact; the norm factor sample is route evidence only.

## Exact orbit count

Represent a reduced signed weight-`w` word at `ell=1` by an antipodal-free
`w`-subset of `Z/512`. Global sign is translation by `256`. Translation of
the exponents and odd Galois dilation give the affine action

```text
x -> a*x+b mod 512,    a odd.
```

For each affine permutation, its cycles are paired by the commuting
antipodal involution `x -> x+256`. A fixed antipodal-free subset cannot use a
self-antipodal cycle; from a pair of distinct antipodal cycles of length `d`
it may choose neither cycle or either one. Thus its fixed-set generating
function is

```text
product_(paired cycles C) (1+2 z^|C|).
```

Burnside averaging over the `512*256` affine maps gives:

| weight | reduced signed words | affine-Galois classes |
|---:|---:|---:|
| 3 | 11,054,080 | 254 |
| 4 | 1,398,341,120 | 24,979 |
| 5 | 140,952,784,896 | 2,296,920 |
| 6 | 11,793,049,669,632 | 185,569,028 |

The first two values reproduce the independently completed weight-three and
weight-four certificate universes exactly. Modal run
`ap-BGQsNwspLE5TFhpfhG3VpY` computed all affine fixed-set counts; the slowest
multiplier worker took `0.103` seconds.

## Norm resource sample

The same run factored the exact `Phi_512` norms of 256 deterministic
weight-five representatives. It completed all 256 rows, producing 722 factor
records and 670 distinct prime factors. No factor `q<2^256` had
`v_2(q-1)>=41`; the maximum was `17`. This is nonexhaustive survival evidence,
not an ambient exclusion. One factorization took `15.95` seconds.

## Route decision

The direct norm census grows by a factor greater than `91` from weight four to
weight five, and by another factor greater than `80` at weight six. A blind
extension would therefore require millions of exact norms merely for the
first residual slot and cannot scale to the second slot. It is not the next
closure route.

The next attack should use the simultaneous odd-moment equations before
enumeration. The proved `dli_wcl_ell2_weight5_pair_quadratic_router` now reduces
`(ell,w)=(2,5)` to two shape variables and two Dickson-recurrence equations. A
successful continuation must exploit that joint system, rather than factor the
first-moment norm class by class. The six-slot statement and its status are
unchanged.

## Replay

```bash
~/.venvs/modal/bin/modal run \
  experiments/prize_resolution/dli_wcl_weight5_orbit_probe_modal.py \
  --sample-size 256
```

Expected digest:

```text
DLI_WCL_WEIGHT5_ORBIT_PROBE orbits_w3=254 orbits_w4=24979
orbits_w5=2296920 orbits_w6=185569028 sample=256/256 errors=0
eligible=0 max_v2=17
```
