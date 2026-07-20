# Proof

The nonharmonic scalar compiler gives the exact positive-quadratic field line
and puts every unordered outer trace in `F_p`. Write

```text
p=1+k(2L).
```

If `k` is even, then `4L|p-1` and every source lift already lies in `F_p`.
Suppose `k` is odd. For `r^(4L)=1`,

```text
r^p=r^(1+2L)=eta r,       eta=r^(2L) in {1,-1}.      (1)
```

The case `eta=1` again gives descent. In the only case at issue,
`eta=-1`, the coefficients of all six source traces lie in `F_p`, so an
accepted trace must obey

```text
y_Xj(r)=y_Xj(r)^p=y_Xj(-r).                          (2)
```

Substitute the six cross ratios from the Mobius-router dependency into

```text
tau(z)=4((z+1)/(z-1))^2-2.
```

All denominators below are nonzero because `r!=0` and `r^4!=1`. Direct
subtraction and factorization give

```text
y_R0(r)-y_R0(-r)=0,                                  (3)

y_R1(r)-y_R1(-r)
 =64(1+iota)r(r^2+iota)(r^4+8iota r^2-1)
   /((r^2-1)^2(r^2+1)^2),                            (4)

y_R2(r)-y_R2(-r)=-(right side of (4)),               (5)

y_P0(r)-y_P0(-r)=-32r(r^2+1)/(r^2-1)^2,             (6)

y_P1(r)-y_P1(-r)
 =(-64-128iota)r(r^2-(3+4iota)/5)/(r^2+1)^2,         (7)

y_P2(r)-y_P2(-r)
 =(-64+128iota)r(r^2-(3-4iota)/5)/(r^2+1)^2.         (8)
```

The official characteristic is larger than `2^40`, so every displayed
integer scalar is nonzero. Equations `(2),(4)--(8)` prove the complete list
`(CFR3)`.

If `r^2=-iota`, then `t=r^4=-1`. The primary gap is impossible there because

```text
F_(2M)(-1)=(1/4)_M/M! !=0
```

in the official characteristic range. If `r^2=-1`, then `r^4=1`, contrary
to denominator distinctness.

For the remaining `R1,R2` factor set `v=-iota r^2`. Since
`r^2=iota v`, the equation becomes

```text
v^2+8v+1=0,       v+v^(-1)=-8.                     (9)
```

For `P1`, the Gaussian norm of `(3+4iota)/5` is one, so its inverse is
`(3-4iota)/5`; `P2` exchanges the two values. Hence both give

```text
u+u^(-1)=6/5.                                       (10)
```

Both `u` and `v` belong to `mu_(2L)`: `r^2` does, and multiplication by the
fourth root `-iota` preserves that group. Therefore `(9)--(10)` require the
40-step trace recurrence to terminate at two.

The exact odd-`k` interval in `(CFR5)` is the nonsplit half of the field line.
The preregistered launcher partitions its `2,247,721` values into 16 disjoint
contiguous index shards. Its compact packet records

```text
processed=odd_candidates=2,247,721,
coverage_exact=true,       all_complete=true,       hits=[].
```

The independent checker reconstructs the interval, parity selection, shard
partition, factor-five counts, source hash, and every no-hit digest. It also
directly replays both trace terminals on boundary and midpoint samples from
every shard. It passes. No prime candidate is lost by the factor-five skips,
because every skipped modulus is larger than five and composite.

Thus neither residual trace in `(CFR4)` occurs at an official
characteristic. Equations `(3)--(10)` exclude anti-invariance on all five
branches in `(CFR2)`. Equation `(3)` makes no such conclusion for `R0`, which
is retained. QED.

