# E1 pair-feasible prime-field reduction audit

Date: 2026-07-27.

## Finding

The ambient-generation reduction alone did not justify the prime-field
hypothesis in `kernel_lattice_reframing`. On the pair-feasible branch it gives
`F=F_p(Q)`. Because the canonical quotient roots contain a primitive `N`-th
root, writing `q=p^d` gives

```text
d=ord_N(p),       N in {256,512}.
```

Every possible `d` is a power of two. Exact integer-root checks over the two
budget intervals exclude all `d>1`. The prize interval contains no possible
perfect power. The RowC interval has only four square-root candidates:
`2^125+j` for `0<=j<=3`; two are even, while the other two have order `1` and
`64` modulo `256` (order `128` modulo `512` for the latter), never order two.

Therefore every named-anchor pair-feasible row has

```text
q=p,       p=1 mod N.
```

## Route impact

The residual E1 target is now pointwise collision control over primes in two
exact intervals. Generated-field transfer and extension degree are no longer
live axes, and the sparse ternary kernel interface is correctly scoped.

This proves no collision allowance, pays no unsafe row, and moves no endpoint.
The verifier performs 14 exact root-interval checks and no prime search,
factorization, Modal run, or unbounded computation.
