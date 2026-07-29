# L1 HNF payoff ladder

## Decision

The colored-Frobenius HNF lane is mathematically sound but currently has
limited critical leverage. It attacks the minimum-width `t=p` split-pencil
stratum on nine Mersenne checkpoint rows. It does not attack wider exchanges,
the arbitrary-target Toeplitz/Pade section, or the aggregate first-owner sum.

After all proved atlas-level reductions, the remaining `(m,h)` obligations
are:

| family | rows | live value degrees | cells |
|---|---:|---|---:|
| `m=4` | 4 | `h=2` | 4 |
| `m=8` | 4 | `h=2,...,7` | 24 |
| `m=16` | 1 | `h=2,...,15` | 14 |
| **total** | **9** | | **42** |

The embedded antipodal family is compatible with 23 even-degree cells. The
19 odd-degree cells cannot contain that family. The current next-to-maximal
program addresses only `h=7` on four rows and `h=15` on one row. Even a full
close of both degrees changes `42 -> 37`; the exceptional J-zero cubic
`3+2+1` chart is only one subchart and changes neither number by itself.

For a complete degree-`h` close at depth `d`, the term removed from the
available complement census is

```text
binom(h,2) floor(
  binom(m(p+1),(m-h+1)p+m-d)
  / binom((m-h)p+m,(m-h+1)p+m-d)).
```

This is an upper cap, not known mass. If all 42 residual cells are eventually
excluded or owned, the immediate generic packing gain is only the transition
from minimum residual width `p` to `p+1`. Before floors, the cap improves by

```text
(n-a+p)/p < m+2 <=18.
```

## Work rule

Treat a full `(m,h)` close or a separately budgeted owner payment as a
critical payoff. Treat a proper HNF subchart as bankable local algebra only.
Do not extend the J-zero packet merely because another finite guard or lift
can be compiled. Extend it when the result is likely to finish the J-zero
chart cheaply, completes a sibling set leading to a full `h=7` cell, or is
valuable for upstream's split-pencil ledger independently of L1.

The higher-priority L1 routes remain:

1. arbitrary-target Toeplitz/Pade split-section flatness;
2. aggregate chronology-valid first-owner payment;
3. a complete owner/exclusion of the `t=p` spectrum, not isolated HNF
   chambers.

The exact theorem and audit contract are in
`background/nodes/l1_mersenne_hnf_payoff_scope_router/`.
