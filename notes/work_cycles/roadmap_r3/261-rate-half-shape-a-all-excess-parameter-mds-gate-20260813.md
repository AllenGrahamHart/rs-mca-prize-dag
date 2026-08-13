# Cycle 261: rate-half Shape-A all-excess parameter-MDS gate (2026-08-13)

The scalar-weld residual flag from Cycle 259 is exact, but bounding only its
extra degree-drop rows cannot close Shape A: the retained ledger does not
force any `q_delta>0`. The attack was therefore moved to the complete
all-fiber compatibility problem.

For each of the `3e` slopes write

```text
G(delta,X)=D_delta(X)C_delta(X),
D_delta=A_delta R_delta,
C_delta=zeta_delta H_delta.
```

The known factor has degree `n-a_delta`; the unknown block has
`a_delta+1` coefficients. Convolving these blocks with `D_delta` and
applying the exact dual-RS parity checks on the slope set gives one matrix
`K_all`. Its kernel is exactly the set of fiber data interpolating to one
biform of bidegree at most `(e-2,(3e-7)/2)`.

The shape-A excess sum gives the decisive compression

```text
# columns=sum_delta(a_delta+1)=4e
         =733007751852 officially.
```

A valid survivor requires every polynomial block nonzero; block degrees
retain every `q_delta`. In the `e=7` analogue the matrix is `120 x 28`.
The cyclic profile and fifty degree-preserving switches have rank `28` in
each of `F_337` and `F_421`.

```text
start:                   b25caad721a6a11136f4e6576e173cc412e78c63
canonical prize:         fdfb20a42 (clean; unchanged)
upstream Lane-T head:    PR #1161 at bf6e3ab
result:                  PROVED all-excess parameter-MDS equivalence
DAG delta:               +1 PROVED node, +2 req edges, +1 evidence edge
critical status delta:   none; rate_half_band_crossing_location remains open
small analogue:          rank 28/28 in 102 exact profiles across two fields
independent audit:       35 dual-RS parity checks plus corruption rejection
compute:                 subsecond local exact arithmetic; no Modal spend
next route action:       prove K_all has no block-supported kernel, or
                         classify the exceptional incidence profiles
```
