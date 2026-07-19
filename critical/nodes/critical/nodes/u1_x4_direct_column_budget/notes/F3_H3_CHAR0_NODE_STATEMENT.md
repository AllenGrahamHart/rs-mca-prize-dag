# Node candidate: f3_h3_char0_classification

Status: PROVED, with exact replay.

## Statement

Let `mu_n` be the complex roots of unity of order dividing `n`.  For
`h=3`, every unordered pair of distinct disjoint triples

```text
P={x1,x2,x3},  Q={y1,y2,y3} subset mu_n
```

with equal top signatures

```text
e1(P)=e1(Q),   e2(P)=e2(Q)
```

is toral: both `P` and `Q` are cosets of the unique order-3 subgroup of
`mu_n`.  Consequently no non-toral h=3 interior trade is persistent in
characteristic zero.  If a non-toral exponent shape becomes an h=3 trade
modulo a prime `p = 1 mod n`, then it is a norm-gate accident: `p`
divides the norm of at least one nonzero obstruction among `E1,E2`, and
each fixed non-toral shape activates at at most

```text
floor(phi(n) * log(6) / (2 * log(n)))
```

primes `p >= n^2`.

## Replay

```text
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_char0_classification.py
```

Expected digest:

```text
CHAR0_CLASSIFICATION_PASS
```

