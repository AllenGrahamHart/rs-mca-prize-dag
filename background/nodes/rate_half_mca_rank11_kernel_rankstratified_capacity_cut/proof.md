# Proof

Partition the rank-deficient component incidences by

```text
r=rank(ev_T),       1<=r<=9,
```

and assign each `T` to one canonical rank basis `B subset T`. Put
`d=10-r`. By the kernel canonical-basis globalizer, one fixed `B` carries at
most

```text
M_d(K') C(K'-10,d+1)                               (1)
```

incidences. There are at most `C(n',r)` possible bases. Summing (1) over
all ranks proves

```text
I_kernel <= Cap(K').                               (2)
```

The dominant-lane theorem would instead require

```text
I_kernel >= D(K').                                 (3)
```

For `d<=8`, the exact support-local cap used in (1) is

```text
M_d=floor(max{
  (R+J)_fall_(d+1)/((w+J)(w+1)_rise_(d-1)),
  (R+d)_fall_(d+1)/(w+1)_rise_d
}),

J=K'-(10-d),       (R,w)=(1048576,67472).
```

For `d=9`, use the proved uniform margin/interleaving cap
`61871313426630599`.

The verifier evaluates (2)--(3) with exact integers for every one of the
4589 declared values. The minimum signed comparison remains positive
through `K'=4598`; the displayed endpoint gap is exact. At `K'=4599`,

```text
ceil(D(4599)) =
929270008258717168172225403738805539487338025945487940222665507,

Cap(4599) =
929365465753464049635514279100756055244773737572652812396430010.
```

Thus (2) contradicts (3) precisely on the claimed interval, while the next
row is retained as an explicit method wall.
