# Proof

The parallel-`DE` quotient theorem gives the matching permutation

```text
(0,1,2,6,9,12,3,10,13,4,7,14,5,8,11).
```

For missing roles `xi=0,1`, exchange of the two identical positive records
exchanges the missing roles and fixes the matching index. Thus

```text
{(0,4),(1,4)}
```

is one orbit. For `xi=2`, the missing role is fixed and matching 4 is sent
to matching 9, giving the second orbit

```text
{(2,4),(2,9)}.
```

The matching-4 theorem supplies `(0,4),(1,4),(2,4)`; the quotient supplies
`(2,9)`. No action sends `(0,4)` or `(1,4)` to pairing 9.

The previous complete block paid 15 labels in 9 orbits. The two new orbits
are disjoint from it and contain four labels, so the cumulative paid ledger
is `15+4=19` labels in `9+2=11` orbits. Consequently

```text
105-19 = 86 live labels,       60-11 = 49 live orbits.
```

Multiplying the four new labels by four source signs and four target lanes
gives 64 raw cases. QED.
