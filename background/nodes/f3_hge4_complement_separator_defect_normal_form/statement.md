# HGE4 complement-separator defect normal form

- **status:** PROVED
- **consumer:** `f3_hge4_norm_gate_count`
- **dependency:** `f3_hge4_nonfull_complement_third_gate`

Retain the notation and hypotheses of the complement-third gate:

```text
Q=P+d,       PQR=X^m-1,       c=m-2h>0,
H=(d/m)XP'R,
H-1=PA,      H+1=QB.
```

Put

```text
e=c-h=m-3h,       G=B-A.                              (SDN1)
```

Then `e>=0`, and in fact

```text
deg G=e,
lc(G)=-d^2 h/m.                                      (SDN2)
```

The cofactors and separator obey the exact identities

```text
A=(2-QG)/d,       B=(2-PG)/d,                        (SDN3)

m(P+Q-PQG)=d^2 XP'R.                                (SDN4)
```

At a dyadic exact ratio level, `e>=1`. Hence a retained width a fixed distance
below the third line has a defect polynomial of exactly that bounded degree.
In particular, the closest possible widths have `e=1` when `m=1 mod 3` and
`e=2` when `m=2 mod 3`.

This is a necessary normal form. It does not assert that a solution of
`(SDN4)` has split, disjoint subgroup roots, nor does it count its solutions.
