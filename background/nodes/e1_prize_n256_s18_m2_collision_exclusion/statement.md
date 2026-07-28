# E1 prize N=256 square-mass-18 cofactor-2 exclusion

- **status:** PROVED
- **closure:** dual exhaustive certificate plus exact cyclotomic resultants
- **scope:** prize-envelope `N=256`, profile `(a,b,c)=(4,2,0)`, cofactor `m=2`
- **dependencies:** `e1_prize_n256_s18_m2_high_variance_exclusion`

There is no prize-row collision in the leading square-mass-18 profile with
local-norm cofactor `m=2`.

After the parent high-variance exclusion, two independent normalized streams
cover all `511272` residual vectors in

```text
V in {10,18,26,...,98}.
```

FLINT and PARI independently compute every exact cyclotomic resultant and
agree through a 64-bucket multiset commitment. Every quotient `R/2` is
outside the exact prize interval: `510396` are below, none are inside, and
`876` are above. Therefore cofactor `m=2` is impossible.
