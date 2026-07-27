# E1 N=256 square-mass-16 sparse-L1 variance exclusion

- **status:** PROVED
- **closure:** proof plus exact rational arithmetic

Let `F=sum_i c_i X^i` have folded profile `(3,4,0)` in the
`N=256,s=5` band. Retain the exact autocorrelation variance `V`
from the parent theorem. Then no pair-feasible row-prime collision is possible
when

```text
106<=V<=134.
```

Together with the zero- and high-variance exclusion, every unresolved vector
in this profile therefore satisfies

```text
0<V<=104,       V even.
```

The improvement uses autocorrelation sparsity and the profile's chord weights.
If `E=V/2=sum_(d=1)^63 A_d^2` and
`L=sum_(d=1)^63 |A_d|`, at most 21 terms are nonzero and integer
arithmetic gives `E>=3L-42`. More sharply, the 21 raw chord magnitudes
are three `4`s, twelve `2`s, and six `1`s. A classwise cancellation
lemma gives

```text
4L<=E+66.
```

Every conjugate square obeys `y_u<=16+2L`. Seven exact pointwise
logarithmic majorants then put the norm strictly below `2^250` throughout
the stated range.

This does not classify or exclude the positive even residual `V<=104`.
