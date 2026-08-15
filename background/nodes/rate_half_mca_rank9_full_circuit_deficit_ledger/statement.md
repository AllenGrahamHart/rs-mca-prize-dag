# Full circuit-deficit rank-nine shadow ledger

- **status:** PROVED
- **component subset size:** `11`
- **shadow size:** `9`
- **baseline shadow cost:** `55`

Let `I_c` count selected rank-ten eleven-set incidences whose unique circuit
has support `c`.  Such an incidence creates

```text
q_c=55-C(11-c,2)
```

rank-nine shadows.  If their one global marked capacity is `G`, then

```text
sum_c q_c I_c<=G.                                      (FD1)
```

Suppose one record has incidence caps `L_c` for `2<=c<=9`.  For `R`
records, complete full-rank incidence satisfies

```text
I_full<=floor((G+R sum_(c=2)^9 C(11-c,2)L_c)/55).     (FD2)
```

If records occupy alternative cap branches, take the maximum weighted
deficit over the branch vectors before multiplying by `R`.

## Falsifier

An incorrect shadow multiplicity; a circuit with support ten or eleven and
positive deficit; reuse of a mark outside `G`; or a feasible incidence
vector above `(FD2)`.
