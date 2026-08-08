# Proof

The parallel-`DE` quotient theorem gives the matching permutation

```text
(0,1,2,6,9,12,3,10,13,4,7,14,5,8,11).
```

For missing roles `xi=0,1`, exchange of the two identical positive records
exchanges the missing roles and fixes the matching index. Thus

```text
{(0,5),(1,5)}
```

is one orbit. For `xi=2`, the missing role is fixed and matching 5 is sent
to matching 12, giving the second orbit

```text
{(2,5),(2,12)}.
```

The matching-5 theorem supplies `(0,5),(1,5),(2,5)`; the quotient supplies
`(2,12)`. No action sends `(0,5)` or `(1,5)` to pairing 12.

The previous complete block paid 21 labels in 12 orbits. The two new orbits
are disjoint from it and contain four labels, so the cumulative paid ledger
is `21+4=25` labels in `12+2=14` orbits. Consequently

```text
105-25 = 80 live labels,       60-14 = 46 live orbits.
```

Multiplying the four new labels by four source signs and four target lanes
gives 64 raw cases. QED.
