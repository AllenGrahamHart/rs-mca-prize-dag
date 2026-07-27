# E=42 endpoint route report

Date: 2026-07-27.

## Route fence

The relaxed slack recurrence has 11 equality signatures at
`E=42,L=24` (Modal run `ap-cE86PQGt7q3PObpsuHfh8A`). The proposed repair
`E=42 => L<=23` is false: all 16 bounded workers in run
`ap-vSQu8FYeK53wj13QIITxm8` found exact geometric witnesses within
milliseconds. One full-conductor witness is

```text
(7,-1),(24,-1),(55,-2),(76,-1),(82,-2),(87,1),(103,2),
```

with `(E,V,L,D_64,C)=(42,84,24,0,-30)`. The local verifier replays this
ledger exactly.

## Exploratory evidence

Run `ap-yHtqWXgNjiMMZKpaJ6Eif9` computed exact FLINT norms and moments for
three diameter strata; all three norms were below `2^250`. Run
`ap-PD4vO6nC8zwMm5otuwezpD` visited more than 100,000 exact endpoint
geometries and found `M_3=1278` and maximum sampled conjugate square about
`51.94`. These are evidence only, not universal bounds.

An abstract autocorrelation search (`ap-BwIpKkDLD5uAW6fxAUVCnQ`) reached
`M_3=3000`. A separate shift-gap probe
(`ap-ZLQ8jFVijWhkuBkAPkfB7E`) falsified the tempting uniform local-gap
lemma, finding supported shifts with gap three. The surviving route is
therefore a global weighted layer count, not a pointwise shift estimate.

## Exact replacement

For every integer autocorrelation profile with `E=42,L<=24`, nested level
sets and the missing-zero pair count give `M_3<=3660`. There are 42 such
profiles; the exact maximum is attained in the relaxed ledger only at nine
magnitudes two and six magnitudes one. The local verifier enumerates all 42.

The cubic Hermite interpolant to `log` at 14 and 60 is a global majorant.
Its exact averaged value at `M_3=3660` lies below `(125/32)log 2`; run
`ap-aDQcDVxxeDUhIUnAYkiA4f` derived the rational identities. The proof and
local verifier reproduce the interpolation, layer cap, and logarithmic
margin without Modal, floating point, or sampled geometry.
