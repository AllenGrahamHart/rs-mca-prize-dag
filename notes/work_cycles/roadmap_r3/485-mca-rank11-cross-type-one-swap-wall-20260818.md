# Cycle 485: cross-type one-swap synchronization wall

## Result: PROVED sharp overlap obstruction

In a packet of size 32, an anchor type represented at least 18 times is
unique. Two packets anchored at different pair types can overlap in at most

```text
2*32-2*18=28
```

records. Under the stronger local heavy-ruling threshold 20, the cap is 24.
Both are below the 31-record overlap required by the existing split-pencil
one-swap mechanism. Therefore one-swap connected components preserve their
anchor type and cannot synchronize the 520-type quotient population.

The general atom-collision theorem is stronger than that local mechanism: its
primitive uniqueness corollary needs only two shared slopes. A distinct
quotient atom on the 28-record bridge instead enters its large-core exception:

```text
|G|>=1079711-c,
|G\H|>=1012239-c,
K'-1=1048575-c.
```

Thus current pair uniqueness misses by 36,336 coordinates. The live theorem
is payment of this large-core/nonprimitive output, not a generic 28-overlap
collision theorem.

The 28 and 24 bounds are sharp as set-system bounds. This does not prove that
cross-type quotient certificates are compatible or incompatible; it only
closes the proposed 31-overlap method.

## Audit

The primary verifier independently maximizes overlap over every three-class
count profile for 32-record packets and obtains 28 and 24. The proof audit
reconstructs the formula `64-2a`; nine contract mutations are rejected. No
Modal computation was used.

## Burn-down

```text
starting local pin:       e2f37a5e9
canonical prize pin:      0dd5b3244
upstream main pin:        93fba1be3
critical target attacked: rate_half_band_crossing_location
DAG delta:                +1 PROVED method-wall node, +4 edges
critical status delta:    none
closed method:            31-overlap split-pencil one-swap synchronization
compute spend:            none
next action:              <=28-overlap rigidity, larger packets, or chronology
```

## Nonclaims

- no cross-type incompatibility or large-core collision payment;
- no quotient population payment;
- no shifted or nonquadratic split-pencil payment;
- no high-complexity payment, rank-eleven closure, or MCA closure.
