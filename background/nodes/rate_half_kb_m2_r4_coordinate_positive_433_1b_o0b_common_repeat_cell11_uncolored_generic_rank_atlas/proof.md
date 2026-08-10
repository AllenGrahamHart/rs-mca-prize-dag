# Proof

The common-kernel parent reconstructs the missing product `q` and squared sum
`s^2`.  If one endpoint is `X`, the other is `q/X`, and `X` satisfies

```text
X^4 + (2q-s^2)X^2 + q^2 = 0.
```

The exact endpoint algebra therefore has rank four over the degree-six or
degree-four source algebra.  For each missing record, outside sign, and
matching, the universal paired-product determinant identity gives three
polynomials in the remaining endpoint.

Take the Sylvester matrix of the first tested pair.  Replace every endpoint-
quartic coefficient by its rank-four multiplication matrix and every source-
algebra coefficient by its rank-six or rank-four multiplication matrix.  The
result is a square matrix over `F_p(x)`.  A nonzero determinant at one defined
specialization proves that its rational determinant is not identically zero.

The certificate specializes at `x=2`, first checking every construction guard
and every rational denominator.  Exact modular Gaussian elimination returns
full rank and a nonzero determinant in all 720 cases.  Hence the two selected
polynomials are coprime over the generic source algebra, so the three-equation
system is generically empty.  QED.
