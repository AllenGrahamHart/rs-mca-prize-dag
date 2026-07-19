# Proof

Intrinsic stabilizer size is unique, so the scale classes are disjoint. Sum
their assumed quotient-row bounds:

```text
sum_(j=1)^s C(n/2^j)^B
  = C n^B sum_(j=1)^s 2^(-jB)
  = C n^B (1-2^(-sB))/(2^B-1)
  < C n^B/(2^B-1).
```

At `B=6`, the denominator is `2^6-1=63`. Adding a current-row primitive
bound `C n^6` gives a total strictly below `(1+1/63)C n^6=(64/63)C n^6`.
The inequality is at most `n^6` when `C<=63/64`.

The argument also applies to any subset of the dyadic scales, such as the
petal range `2<=M<=t`; extending the sum to every `M>=2` is the safe direction.

