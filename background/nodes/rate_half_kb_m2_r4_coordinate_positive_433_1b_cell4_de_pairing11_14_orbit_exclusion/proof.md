# Proof

The parallel-`DE` quotient theorem gives the matching permutation

```text
(0,1,2,6,9,12,3,10,13,4,7,14,5,8,11).
```

For missing roles `xi=0,1`, exchange of the two identical positive records
exchanges the missing roles and fixes the matching index. Thus

```text
{(0,11),(1,11)}
```

is one orbit. For `xi=2`, the missing role is fixed and matching 11 is sent
to matching 14, giving the second orbit

```text
{(2,11),(2,14)}.
```

The matching-11 theorem supplies `(0,11),(1,11),(2,11)`; the quotient
supplies `(2,14)`. No action sends `(0,11)` or `(1,11)` to pairing 14.

The previous complete block paid 39 labels in 21 orbits. The two new orbits
are disjoint from it and contain four labels, so the cumulative paid ledger
is `39+4=43` labels in `21+2=23` orbits. Consequently

```text
105-43 = 62 live labels,       60-23 = 37 live orbits.
```

Multiplying the four new labels by four source signs and four target lanes
gives 64 raw cases. QED.
