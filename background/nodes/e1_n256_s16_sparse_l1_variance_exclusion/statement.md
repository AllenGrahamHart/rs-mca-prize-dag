# E1 N=256 square-mass-16 sparse-L1 variance exclusion

- **status:** PROVED
- **closure:** proof plus exact rational arithmetic

Let `F=sum_i c_i X^i` have folded profile `(3,4,0)` in the
`N=256,s=5` band. Retain the exact autocorrelation variance `V`
from the parent theorem. Then no pair-feasible row-prime collision is possible
when

```text
112<=V<=134.
```

Together with the zero- and high-variance exclusion, every unresolved vector
in this profile therefore satisfies

```text
0<V<=110,       V even.
```

The improvement uses autocorrelation sparsity. If
`E=V/2=sum_(d=1)^63 A_d^2` and
`L=sum_(d=1)^63 |A_d|`, at most 21 terms are nonzero and integer
arithmetic gives `E>=3L-42`. Hence every conjugate square obeys
`y_u<=16+2L`. Five exact pointwise logarithmic majorants, one for
each remaining upper variance block, then put the norm strictly below
`2^250`.

This does not classify or exclude the positive even residual `V<=110`.
