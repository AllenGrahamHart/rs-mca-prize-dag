# E1 N=256 E=33 profile-(4,5,1) quotient exclusion

- **status:** PROVED
- **closure:** computation plus proof

No pair-feasible folded-profile `(3,4,0)` collision at `N=256`, `V=66` has
autocorrelation magnitude profile

```text
(n_1,n_2,n_3)=(4,5,1).
```

The exact nested layer sizes are `(20,12,2)`. A complete mod-16 quotient
allocation census gives

```text
order 128, outer support not in 2Z: 5,421,301 allocations, M_3<=1732;
order  64, divided support not in 2Z: 3,086,861 allocations, M_3<=1670.
```

If the outer support lies in `4Z`, the degree-32 small-field norm is nonzero
and at most `50^32<2^250`. These cases are exhaustive. Since 1732 is the
exact safe side of the `V=66` cubic-Hermite threshold, the profile is empty.
