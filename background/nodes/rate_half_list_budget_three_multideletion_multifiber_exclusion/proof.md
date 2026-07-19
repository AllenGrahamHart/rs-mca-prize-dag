# Proof

For a polynomial of degree `q`, write its reverse as

```text
rev_q F(z)=z^q F(1/z).
```

Since each `B_i` is monic of degree `sm` and is a polynomial in `X^m`,

```text
rev_(sm) B_i(z)=1+O(z^m).                              (1)
```

Also

```text
rev_(ell_i) P_i(z)=product_(r in R_i)(1-rz)=:D_i(z).  (2)
```

Pad every `A_i` to the common degree `sm-ell_0`. Dividing `(1)` by `(2)`
in the formal power-series ring gives

```text
z^(sm-ell_0) A_i(1/z)
 =z^(ell_i-ell_0)/D_i(z)+O(z^m).                       (3)
```

Suppose `sum_i lambda_i A_i=0`. Reading the highest `m` coefficients through
`(3)` yields

```text
sum_i lambda_i z^(ell_i-ell_0)/D_i(z)=O(z^m).          (4)
```

Put `D(z)=product_i D_i(z)`. After multiplying `(4)` by `D`, the numerator

```text
N(z)=sum_i lambda_i z^(ell_i-ell_0) product_(j!=i)D_j(z)   (5)
```

has degree at most

```text
(ell_i-ell_0)+(L-ell_i)=L-ell_0.                       (6)
```

Condition `(MME3)` and `(4)` say that the first `m` coefficients of `N`
vanish while its degree is less than `m`. Thus `N=0`.

Fix `r in R_i` and evaluate `(5)` at `z=r^(-1)`. Every term with index
different from `i` contains `D_i(r^(-1))=0`. The `i`th term is nonzero apart
from its scalar `lambda_i`: the exceptional sets are disjoint, `r` is
nonzero, and no other `D_j` vanishes there. Hence `lambda_i=0`. This holds for
every `i`, proving `(MME4)`.

The degree rows in the linear Grassmann atlas translate directly to deletion
counts from a completed size-`d` block: `deg A_i=d-ell_i`. Substitution gives
the five thresholds in `(MME5)`. Every quotient-fiber size at the
power-of-two prize row is a power of two, so all thresholds are met once
`m>=8`. The sharper one-root thresholds for cycle and path are the preceding
theorem. This proves `(MME6)` and the residual inventory. QED.
