# Joint sparse/high rank-nine shadow ledger

- **status:** PROVED
- **component subset size:** `11`
- **shadow size:** `9`

Suppose every full-rank eleven-set has one circuit of size `c>=2`.  Omitting
a pair disjoint from the circuit leaves rank eight; omitting a pair meeting
the circuit leaves rank nine.  Thus the number of rank-nine shadows is

```text
q_c=55-C(11-c,2).
```

In particular:

```text
c:                   2   3   4   5   >=6
q_c:                19  27  34  40   >=45
premium 45-q_c:     26  18  11   5
```

Let the total capacity of all rank-nine marks be `G`.  Let there be `R`
records.  If one record has low-support incidence bounds `L_c` for
`c=2,3,4,5`, then complete full-rank incidence is at most

```text
floor((G+R sum_(c=2)^5 (45-q_c)L_c)/45).           (JL)
```

If each record lies in one of several structural branches with cap vectors
`L_c^(a)`, replace the sum in `(JL)` by its maximum over `a`.

## Falsifier

A wrong shadow multiplicity; reuse of a rank-nine mark outside `G`; a
high circuit with fewer than 45 rank-nine shadows; or a feasible incidence
vector above `(JL)`.
