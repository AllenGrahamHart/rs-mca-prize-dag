# Proof

Let `P` exchange common roles `AB,AC` and fix `LA,BC+,BC-`. On target
coordinates apply

```text
(a,b,c,d,e,f) -> (a,c,b,d,f,e).
```

The outside records move as

```text
BE <-> CF,       DE+ <-> DF+,       DE- <-> DF-,       EF -> EF.
```

Thus `S0` is fixed, `SDE,SDF` are exchanged, and `sigma_o` is fixed. Every
target product is preserved. Every target sum is preserved except `b-c`,
which changes sign. The coordinate permutation also preserves the complete
nonzero and pairwise-signed-distinct target guard set.

Write the five common source roots in the compiler normalization as

```text
1, epsilon_1*i, r, epsilon_2*i*r, t,       i^2=-1,
```

placed according to the role cell. After `P`, negate the root attached to
`BC-`; this cancels the sign change of `b-c`. Re-normalizing the first deck
pair gives the following nontrivial source actions; the five omitted paired
cell actions are the familiar sign changes printed by the executable.

```text
cell 0:  (e1,e2,r,t) -> (-e1,-e2,-e1*i*r,-e1*i*t), lambda=-e1*i
cell 1:  -> cell 2, (-e2,e1,1/r,t/r),                lambda=1/r
cell 2:  -> cell 1, (e2,-e1,1/r,t/r),                lambda=1/r
cell 11: (e1,e2,r,t) -> (-e1,-e2,e2*i*r,t),          lambda=1
cell 14: (e1,e2,r,t) -> (e1,-e2,e2*i*r,-t),          lambda=1.
```

Here every transformed source root is `lambda` times the transported old
root, including the `BC-` sign. Hence every source label is multiplied by
`mu=lambda^2`. For cell `0`, `mu=-1`; for cells `1,2`, `mu=r^-2`; elsewhere
`mu=1`. The common source labels include `-1` and `r^2`, so all three
multipliers lie in the multiplicative evaluation domain and scaling by
`mu` permutes that domain. It commutes with the deck involution.

For completeness, the eight incidence columns transform diagonally by

```text
1,mu,mu^2; 1,mu,mu^2; mu/lambda,mu^2/lambda.
```

Product rows map directly. Multiplying each transported sum row by the
nonzero scalar `lambda` maps it directly, because its `q` value scales by
`lambda`. Thus rank, vanishing minors, missing-row equations, and all source
guards are preserved.

The induced outside-record permutation bijects the seven missing-record
choices and the fifteen perfect matchings of the other six records. The
source action is involutive on all sixty cell/sign states. On fixed cells it
changes at least one source sign; on paired cells the cell changes. The lane
action is also involutive, so none of the 360 combined states is fixed.
Burnside therefore gives `360/2=180` state orbits. Appending 105 labels per
state gives `37,800/2=18,900` formal-row orbits. The executable enumerates
the complete action and independently confirms this count. QED.
