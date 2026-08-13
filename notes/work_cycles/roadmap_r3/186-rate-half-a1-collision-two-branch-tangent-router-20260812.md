# Cycle 186: rate-half `A=1` collision two-branch tangent router (2026-08-12)

Shapes B and D each have exactly two factors of correction order one at the
collision. Writing their first-order germs as

```text
f_i(z,y)=a_i z+v_i y+O(2),       a_i!=0,
```

the remaining factors form a unit and the product rule gives

```text
G_X(tau,x_*)=0,
[z]G_X(t,x_*)=unit times (a_1v_2+a_2v_1).
```

The exact split-jet dictionary therefore removes profile `[4]` from both
shapes. Their remaining profile is `[1,3]` unless the normalized branch
tangents cancel, in which case it is `[2,2]`. Shapes A and C each have one
order-two collision factor and are not restricted by this calculation.

The companion norm claim contract was also corrected to say "forced
heavy-row divisor" rather than the stale phrase "exact heavy-row order";
the statement and proof already used the weaker, correct claim.

```text
start:                   a22ff2c2e
result:                  NARROWED, new PROVED supporting node
DAG delta:               +1 PROVED node, +2 req edges, +1 ev edge
critical status delta:   none
upstream terminal delta: candidate extension to Lane-T PR #1161
delta-star movement:     none
compute:                 truncated local algebra replay only; no Modal spend
next route action:       attack tangent cancellation and the one-branch shapes
```
