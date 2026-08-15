# Proof

Fix a rank-ten eleven-set and let its unique circuit have support `c`.
Omitting a coordinate pair leaves rank eight exactly when the pair is
disjoint from the circuit.  Thus among all `C(11,2)=55` nine-shadows,

```text
rank eight: C(11-c,2),
rank nine:  q_c=55-C(11-c,2).                         (1)
```

Summing the rank-nine marks of every incidence inside the one global
capacity gives `(FD1)`.  Now add the exact missing number of shadows to
both sides:

```text
55 sum_c I_c
 =sum_c q_c I_c+sum_(c=2)^9 C(11-c,2)I_c
 <=G+sum_(c=2)^9 C(11-c,2)I_c.                       (2)
```

Supports ten and eleven have zero deficit.  A recordwise cap gives
`I_c<=R L_c`; substituting in (2), dividing by 55, and taking the final
integer floor proves `(FD2)`.

For alternative recordwise branches, maximize the complete weighted
deficit for one record and then sum that common maximum over the records.
No rank-nine mark is spent twice.
