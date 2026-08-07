# Statement

In the live `F04-R02` degree-12 branch, let `K8` and `K10` be the unique
nonnamed factors of the `B0` and `A0` quadratic leading coefficients.
Assume `K8=0`. Then the complete named-open branch is empty over the
algebraic closure, hence over `F_(2130706433^6)`.

The proof is the exhaustive split:

1. On `K10!=0`, the `A0` pseudo-remainder reduction replaces the quartic
   rows by irreducible degree-37 cores. The ideal
   `(R12,K8,C_A^A,C_B^A)` has a size-62, dimension-one basis, and its full
   localizer reduces to zero.
2. On `K10=0`, the larger residual ideal `(R12,K8,K10)` has a size-27,
   dimension-one basis, and its full localizer reduces to zero without using
   either quartic row.
