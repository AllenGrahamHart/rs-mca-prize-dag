# Proof

The unit-trace elliptic-curve router partitions every raw record according to
whether its common trace cubic is smooth (`sigma^3!=27`) or singular
(`sigma^3=27`). The classes and weights are unchanged, so `(SRR1)` is an
exact disjoint partition.

The global overlap-cover payment proves

```text
25(10K_25^0+17K_25^A)<=12134n^2                   (1)
```

as a sufficient uniform target. Since the unit-trace router gives
`G_25^c=4K_25^c`, equation `(1)` is exactly `(SRR2)` because

```text
4*(12134/25)=48536/25.                              (2)
```

When `p=2 (mod 3)`, the nodal envelope gives `W_sing<116n^2`. Hence the
first line of `(SRR3)` implies

```text
W_sm+W_sing
 <(45636/25+116)n^2
 =(48536/25)n^2.                                   (3)
```

When `p=1 (mod 3)`, it gives `W_sing<498n^2`, and the second line implies

```text
W_sm+W_sing
 <(36086/25+498)n^2
 =(48536/25)n^2.                                   (4)
```

Thus either branch of `(SRR3)` proves `(SRR2)`. The second allowance is the
smaller one, so `(SRR4)` is uniform. Finally `G_sm^c=4K_sm^c`; dividing
`(SRR4)` by four gives `(SRR5)`. QED.

