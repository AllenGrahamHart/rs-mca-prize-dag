# Proof

The parallel-`DE` quotient theorem gives the matching permutation

```text
(0,1,2,6,9,12,3,10,13,4,7,14,5,8,11).
```

For missing roles `xi=0,1`, exchange of the two identical positive records
exchanges the missing roles and fixes the matching index. Thus

```text
{(0,8),(1,8)}
```

is one orbit. For `xi=2`, the missing role is fixed and matching 8 is sent
to matching 13, giving the second orbit

```text
{(2,8),(2,13)}.
```

The matching-8 theorem supplies `(0,8),(1,8),(2,8)`; the quotient supplies
`(2,13)`. No action sends `(0,8)` or `(1,8)` to pairing 13.

The previous complete block paid 33 labels in 18 orbits. The two new orbits
are disjoint from it and contain four labels, so the cumulative paid ledger
is `33+4=37` labels in `18+2=20` orbits. Consequently

```text
105-37 = 68 live labels,       60-20 = 40 live orbits.
```

Multiplying the four new labels by four source signs and four target lanes
gives 64 raw cases. QED.
