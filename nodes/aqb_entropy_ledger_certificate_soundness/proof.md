# proof: aqb_entropy_ledger_certificate_soundness

Let the true positive shared-entropy terms be `P_k`, and let the true charged
cost terms be `C_l`. The ledger supplies certified intervals

```text
P_k >= L_k,
C_l <= U_l.
```

The true net gain is

```text
G = sum_k P_k - sum_l C_l.
```

Using the certified inequalities,

```text
G >= sum_k L_k - sum_l U_l.
```

Therefore, if the ledger proves

```text
sum_k L_k - sum_l U_l >= 429,645,547,
```

then the true gain also satisfies

```text
G >= 429,645,547.
```

This is monotone interval arithmetic only: every positive term is rounded
down and every cost is rounded up. Thus a passing ledger soundly proves
`aqb_shared_entropy_gain` for the family whose terms it enumerates.
