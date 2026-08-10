### 2026-08-10 upstream FPC5 Hankel support-determinant import

The new PROVED node
`l1_fpc5_tpetal_hankel_support_determinantal_system` imports Przemek's
generalized-Vandermonde support criterion at upstream commit
`fde7d56d0f2d8f135db4f2226e1978644a6c9f44` and specializes it to the
weighted FPC5 moment sequence.

For a selected core root set `{x_1,...,x_d}`, every Hankel recurrence is
equivalent to one explicit determinant formed from the power columns
`x_i^r,...,x_i^(r+d)` and the moment column
`mu_r,...,mu_(r+d)`. The punctured primitive guard satisfies

```text
M_0(G/(X-x_i))=w_i G'(x_i),
```

so it is exactly nonzero Cramer amplitude on every selected root. A fixed
required-background cell therefore becomes an `ell-1` equation
quasi-affine support incidence, modulo permutation, with its remaining
background and chronology filters explicit.

No critical status changes. The next mathematical object is now an explicit
base-field point count and component classification, not an implicit flat.
