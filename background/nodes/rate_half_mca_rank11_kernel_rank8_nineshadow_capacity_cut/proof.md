# Proof

Let `u_d` be the normalized individual ambient/record cap. The two proved
shared resources give a two-constraint linear program maximizing
`sum_d x_d` subject to

```text
0<=x_d<=u_d,
sum_d w_d x_d<=B,
sum_d v_d x_d<=E_0 B,                              (1)
```

where `B=C(m',9)`, `v_1=52+3E_0/E_1`,
`v_2=55+6*C(67474,2)/E_2`, and `v_d=55` for `d>=3`.

The exact dual is

```text
min_(lambda,mu>=0)
 lambda B+mu E_0B
 +sum_d u_d max(0,1-lambda w_d-mu v_d).             (2)
```

Its objective is convex and piecewise linear. A minimum occurs at the
origin, on an axis crossing `lambda w_d+mu v_d=1`, or at the intersection
of two such lines. The primary verifier enumerates all these exact rational
candidates on every row.

The independent audit uses the resulting finite pattern ledger but does
not enumerate dual vertices. Coranks with dual coverage below one are set
to their cap, those above one to zero, and the one or two tight coranks are
solved from the active resource equalities. The reconstructed primal point
is feasible and has objective equal to (2), proving optimality row by row.

There are 17,599 closed rows. At `K'=17608`, the exact normalized optimum is

```text
351384025841645250492987960935683222721168188857643755340754427565809840
-----------------------------------------------------------------------------
16755791041146967191306857.
```

After multiplication by `N_min`, the endpoint demand and floored capacity
are

```text
5766720021220518691788374977933306399161304279392717935102046102,
5766593474179978862242020061185340786272169030143033615685046898.
```

At `K'=17609`, the corresponding values are

```text
5767465688556047382344501369431569786611530849829691249987271475,
5767631351415051154168368391262648380427518911976610852882120489.
```

The unrounded rational differences have the same signs.
