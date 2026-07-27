# E1 N=256 E=34 route boundary

This report records an exact preflight and route decision. It is not a proof
node and changes no DAG status.

For `V=68`, put `E=34`. Parity in the relaxed slack recurrence makes the L1
ceiling increase again:

```text
L=21: slack 16, minimum energy 38 > 34,
L=20: slack 20, minimum energy 34.
```

Thus `L<=20`. There are 24 integer magnitude profiles. The rational cubic at
contacts 14 and 57 has positive exact margin at `M_3=1947` and negative exact
margin at 1948. Its boundary log forms are

```text
M_3=1947: (74945/79507, 4562/79507, -17729/1475502),
M_3=1948: (74947/79507, 4560/79507, -2943/245917).
```

Six profiles exceed the threshold:

```text
2428  (6,7),
2264  (9,4,1),
2252  (2,8),
2124  (12,1,2),
2084  (5,5,1),
1956  (14,1,0,1).
```

This is the boundary of the cheap one-exception quotient descent. Unlike
`E=35`, several three- and four-layer profiles miss by hundreds, so an
outer-only quotient census cannot decide the slice. No new Modal campaign is
authorized. A future return should first derive a common nested-layer
compiler for all six profiles, with a proved completeness router and a
sub-`$1` pilot, or replace the cubic by a stronger analytic certificate.
