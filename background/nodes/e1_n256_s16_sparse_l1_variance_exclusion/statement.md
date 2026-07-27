# E1 N=256 square-mass-16 sparse-L1 variance exclusion

- **status:** PROVED
- **closure:** proof plus exact rational arithmetic

Let `F=sum_i c_i X^i` have folded profile `(3,4,0)` in the
`N=256,s=5` band. Retain the exact autocorrelation variance `V`
from the parent theorem. Then no pair-feasible row-prime collision is possible
when

```text
84<=V<=134.
```

Together with the zero- and high-variance exclusion, every unresolved vector
in this profile therefore satisfies

```text
0<V<=82,       V even.
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

An exact classification and relaxed minimum-energy table for the low-slack
chord classes gives the needed L1 ceilings at every energy from 43 through
52. Every conjugate square obeys `y_u<=16+2L`. Eight optimized
quadratic row certificates exclude `V=86,88,...,100`. At `V=84`,
a nested-layer count bounds the third central moment by `3660`, and a
two-contact cubic Hermite majorant excludes the endpoint. Nine exact
mean-tangent majorants handle the
remaining range and put the norm strictly below `2^250` throughout the
statement.

This does not classify or exclude the positive even residual `V<=82`.
