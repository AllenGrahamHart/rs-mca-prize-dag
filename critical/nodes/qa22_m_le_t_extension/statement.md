# QA.22 small-scale ledger extension

- **status:** PROVED
- **closure:** exact arithmetic

For `n=2^s`, `13<=s<=44`, rate
`rho in {1/2,1/4,1/8,1/16}`, `k=rho*n`, and `t=(n-k)/2`, let

```text
A_own(M) = M ceil((k+1)/M),
Q_M(A) = C(n/M-1, floor(A/M))
```

for every dyadic `2<=M<=t`. Then all extension cells are nondegenerate,
the column landing fits the allowance `719 Q_M(A_own)`, and the new cells
are disjoint from both the `M>t` composite and the seven banked odd-agreement
QA.22 rows. Moreover,

```text
sum_{2<=M<=t, M dyadic} Q_M(A_own(M))
    <= (1 + 2^-690) Q_2(k+2).
```

The constant `2^-691` is false at `(s,rho)=(13,1/16)`; the exact excess is
approximately `2^-690.2765`. The theorem is the ledger side only. It does not
prove a count bound outside the P1-OWN cells or price a widest-ALL reading.

The full statement, conventions, and scope guards are in `qme_statement.md`.
