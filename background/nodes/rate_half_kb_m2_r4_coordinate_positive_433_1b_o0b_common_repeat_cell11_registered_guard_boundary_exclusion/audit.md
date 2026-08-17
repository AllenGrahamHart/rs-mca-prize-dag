# Audit

The audit is independent of the FLINT replay for the load-bearing finite
arithmetic. It reconstructs all common cofactors with modular Gaussian
elimination, implements polynomial arithmetic directly, checks every printed
quartic root list using `gcd(f,X^p-X)`, and recomputes all 34,560 paired-
product cases. Hostile controls remove a source point, alter a reconstructed
value, introduce a candidate, corrupt an endpoint root list, and alter DAG
status; each mutation must fail.
