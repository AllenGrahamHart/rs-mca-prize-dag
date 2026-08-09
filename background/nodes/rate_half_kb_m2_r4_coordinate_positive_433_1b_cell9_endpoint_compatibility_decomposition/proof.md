# Proof

Write the common kernel section as `A(x), B(x), beta(x)` and put
`x=-t^2`.  For endpoint coordinate `u=b` or `u=c`, every leading-open lift
satisfies the cleared source equation

```text
(u^2 A(x)+B(x))^2 - x beta(x)^2 u^2 = 0.       (EP9-1)
```

For each source-sign row, exact saturation of the global common ideal by all
source guards gives dimension one and basis size 40.  Adjoining `(EP9-1)`
gives dimension zero, with basis size 38 for `u=b` and 30 for `u=c`.
The ideal `A(x)=0` is finite, and the simultaneous ideal
`A(x)=B(x)=beta(x)=0` has basis size 21.

FGLM produces a five-polynomial triangular lex basis for both the endpoint
and simultaneous-zero ideals.  Complete factorization and triangular replay
over `F_2130706433` gives six guarded endpoint points: four with `A(x)!=0`
and two on the simultaneous-zero scheme.  Replaying the latter independently
from its own lex basis gives exactly the same two points, and the `b` and `c`
rows have the same two points sign by sign.  Thus the stated disjoint
decomposition is complete for deployed points. QED.
