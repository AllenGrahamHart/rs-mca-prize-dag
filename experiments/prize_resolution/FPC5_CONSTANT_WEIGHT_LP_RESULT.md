# FPC5 constant-weight LP screen result

## Verdict

`NO_IMPROVEMENT`. The ordinary Johnson-scheme Delsarte LP does not improve
the proved support-shortening cap on the dominant rate-`1/16`, `M=68`
shell.

For `(N,w,sigma)=(511,255,112)`, the proved shortening cap is

```text
1751945892004456252745,       log2=70.5694.
```

The numerical Delsarte relaxation returned

```text
2.9298224240061854e22,        log2=74.6332.
```

Thus the minimum of the two available support-only bounds is still the
existing shortening cap. The LP is about four bits weaker, while the
dominant `M=68` cells need roughly 20 bits of additional saving.

## Replay record

The worker constructed all `255` exact dual-Hahn rows on `144` distance
variables. The first solve exposed a HiGHS scaling issue: bounds above
`1e20` were treated as numerical infinity. A second run scaled variables by
`10^6` and terminated normally. Its absolute slack report reflects severe
cancellation at large variable scale, so the decimal optimum is evidence,
not an exact LP certificate. That caveat cannot turn this into a positive
route signal: the numerical LP is already weaker than a proved bound by four
bits and misses the target by about 24 bits.

Modal runs:

- scaling diagnostic: `ap-Wn0tpWIChceoTcuIuoBwxi`;
- completed scaled solve: `ap-yz9TEuekw6kzA3keERcKVY`.

## Consequence

Do not spend further compute on the ordinary support-only Delsarte LP for
this cell. A useful next theorem must retain information erased by the
binary support projection: nonzero Cramer amplitudes, required-background
Cauchy equations, chronology, or the split-divisor/Pade structure. No DAG
status changes.
