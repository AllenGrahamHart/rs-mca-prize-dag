# Cycle 328: MCA rank-11 rank-eight dense-owner terminal bridge (2026-08-14)

One PROVED node connects the weighted rank-eight chart to the exact
dense-owner chronology terminal imported from upstream PR #1168.

For a fixed rank-eight nine-set, write `q_p` for the number of independent
coordinate pairs determining owner `p` and `t_p` for the selected records
owned by it. The marked ledger satisfies

```text
W_B <=sum_p t_p q_p,
sum_p q_p <=C(n'-9,2).
```

At `K'=22526`, exact weighted demand gives

```text
W_B - 200631*C(n'-9,2) = 11714977255865.
```

Therefore some owner has at least `200632` records. If its pair-core
deficiency were at least five, fixed-owner exception disjointness would cap
it at

```text
1+floor(981104/5)=196221,
```

a contradiction. Hence the owner has deficiency at most four. The
unrounded weighted-average ratio is a constant times
`C(m',11)/C(n',11)` and increases with `K'`, so the bridge is uniform
through `K'=37995`. At `K'=22525`, the comparison still fails by
`1170919108090`.

This reaches the existing chronology terminal but does not close it. The
explicit twelve-owner fence remains valid and prevents any inference that
the dense owner is unique across the received line.

Focused verification:

```text
RATE_HALF_MCA_RANK11_RANK8_DENSE_OWNER_TERMINAL_BRIDGE_PASS
  last_deficit=1170919108090 first_excess=11714977255865
  delta5_cap=196221 controls=6/6
RATE_HALF_MCA_RANK11_RANK8_DENSE_OWNER_TERMINAL_BRIDGE_AUDIT_PASS
  last_deficit=1170919108090 first_excess=11714977255865 proof_pins=5/5
```

No Modal computation was used.

```text
DAG delta:             +1 PROVED dense-owner bridge,
                       +3 requirement edges, +1 evidence edge
critical status delta: none
rank-eight delta:      K'=22526..37995 reaches the delta<=4,
                       200632-record chronology terminal
remaining rank eight: K'=10..22525 structural; K'=22526..37995 chronology;
                       impossible from K'=37996 onward
delta-star movement:   none
compute:               constant-memory exact boundary arithmetic
next route action:     chronology-correct multi-owner payment or a stronger
                       cross-owner coupling theorem
```
