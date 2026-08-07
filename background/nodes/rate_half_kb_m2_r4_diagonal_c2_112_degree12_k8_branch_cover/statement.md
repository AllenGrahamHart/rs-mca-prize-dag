# Statement

In each live `R02` degree-12 branch

```text
F04-R02, F05-R02, F06-R02, F07-R02,
```

let `K8` and `K10` be the unique nonnamed factors of the `B0` and `A0`
quadratic leading coefficients. Assume `K8=0`. Then the complete named-open
branch is empty over the algebraic closure, hence over
`F_(2130706433^6)`.

The proof is the exhaustive split:

1. On `K10!=0`, the `A0` pseudo-remainder reduction replaces the quartic
   rows by exact determinant cores. The four ideals
   `(R12,K8,C_A^A,C_B^A)` have dimension-one bases of sizes
   `62,61,61,62`; each full localizer reduces to zero.
2. On `K10=0`, the larger residual ideal `(R12,K8,K10)` has a size-27,
   dimension-one basis in every cell, and each full localizer reduces to zero
   without using either quartic row.
