# Attack plan

## Required first step: define the charged fiber

For one canonical staircase datum, print every G1 chart charging it. The
row-uniform numerical allowance is pinned: the aggregate over all chart-codeword
charges may inflate the canonical-profile count by at most 719. An unspecified
exponent `b3` is not a finite adjacent-row bound.

The actual E22 datum is the full agreement support `R` of size at least `k`, so
`petal_g3_full_support_codeword_injectivity` proves at most one codeword per
canonical class. If an attack replaces it by a partial support of size `r<k`,
then `petal_g3_subk_support_only_no_go` applies: there can be at least

```text
q^(k-r) - (n-r)q^(k-r-1)
```

degree-`<k` codewords with exactly that partial support. Such a replacement
therefore reopens, rather than solves, the numerator problem.

## Live route

Use the union-injective chart recoveries already proved for the distinct-label
residual-free regimes, then extend their recovery data to the arbitrary-word
G1 atlas. A closure needs one of:

1. a joint chart recovery map with average overlap at most 719;
2. a first-match rule selecting one chart per canonical support;
3. an exact aggregate chart census that fits the quotient profile without
   multiplying the planted column by an unpriced `n^b`.

Small-row experiments should enumerate charts per full canonical support, not
polynomials matching a partial support. Aggregate profile overlap above 719 is
the relevant falsifier.
