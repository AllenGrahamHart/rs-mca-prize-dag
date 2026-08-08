# Proof

The parallel-`DE` quotient theorem gives the matching permutation

```text
(0,1,2,6,9,12,3,10,13,4,7,14,5,8,11).
```

For missing roles `xi=0,1`, exchange of the two identical positive records
exchanges the missing roles and fixes the matching index. Thus

```text
{(0,7),(1,7)}
```

is one orbit. For `xi=2`, the missing role is fixed and matching 7 is sent
to matching 10, giving the second orbit

```text
{(2,7),(2,10)}.
```

The matching-7 theorem supplies `(0,7),(1,7),(2,7)`; the quotient supplies
`(2,10)`. No action sends `(0,7)` or `(1,7)` to pairing 10.

The previous complete block paid 27 labels in 15 orbits. The two new orbits
are disjoint from it and contain four labels, so the cumulative paid ledger
is `27+4=31` labels in `15+2=17` orbits. Consequently

```text
105-31 = 74 live labels,       60-17 = 43 live orbits.
```

Multiplying the four new labels by four source signs and four target lanes
gives 64 raw cases. QED.
