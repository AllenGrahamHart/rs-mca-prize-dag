# Proof

For a residual magnitude profile, put `b_d=|A_d|` on the symmetric
non-diameter support and define nested layers

```text
S_i={d:b_d>=i}.
```

Distribute each symmetric layer over the nine negation-orbit categories
modulo 16. For three layers `U,V,W`, the directed target-fiber inequality is

```text
R(U,V,W)
 <= sum_c min(
      # ordered (u,v) in U*V with u+v=-c,
      W_c sum_a min(U_a,V_(-c-a))).                    (1)
```

For `c=0`, remove the `min(|U|,|V|)` pairs `(u,-u)` that would force the third
entry to zero. Take the minimum of (1) over all three orientations. Expanding
`b=sum_i 1_(S_i)` with exact ordered-layer multiplicities gives a rigorous
upper bound for `M_3`. A symmetric two-point top layer contributes no cubic
zero-sum triple because a 2-group has no nonzero element of order three.

The category capacities at orders 128 and 64 are

```text
(3,8,8,8,8,8,8,8,4),
(1,4,4,4,4,4,4,4,2).
```

Eight disjoint shards in each chamber enumerate every exact layer allocation
with an odd outer category. The complete allocation/maxima ledger for the
three named profiles is the table in the statement. The same 128-task campaign
also records the five other E30 profiles as route diagnostics; all three
claimed profiles are below 1087 in both quotient orders. An independent
implementation recomputes the exact number of allocations, every displayed
maximizing objective, all category capacities, and the disjoint shard cover.

The quotient chambers are exhaustive. If `S_1` contains an odd distance, use
the order-128 line. If `S_1` is even but not contained in `4Z`, division by two
identifies the weighted zero-sum count with the order-64 line. If
`S_1 subset 4Z`, then the conjugate square belongs to `Q(zeta_64)`. Each named
profile has `L<=14`, so every conjugate square is at most

```text
16+2L <= 44,       44^32 < 2^250.
```

Its nonzero degree-32 small-field norm has no pair-feasible prime divisor, and
the tower identity transfers that conclusion to the full norm.

In the first two chambers, `M_3<=1087`; the exact cubic-Hermite certificate
therefore places the collision norm strictly below `2^250`. All three chambers
are impossible for each named profile. QED.
