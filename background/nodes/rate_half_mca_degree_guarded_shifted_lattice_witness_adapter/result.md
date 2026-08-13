# Result

The effective source envelope and actual code census differ by one explicit
coefficient:

```text
effective K=k+1 envelope:  deg(N/W)<=k
actual K=k explanation:    deg(N/W)<k
repair:                     reject the degree-k quotient coefficient
shifted-degree gap:         always 0 or 1
same-support badness:       exact interpolation-degree test
```

This closes witness reconstruction and degree guarding, but not frozen-owner
equivalence or coverage.
