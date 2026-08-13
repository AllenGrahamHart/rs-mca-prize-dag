# Cycle 227: MCA full-lift common-core continuation (2026-08-13)

The exact-layer affine-line mechanism survives beyond `e=d`.  What changes
is that the highest possible deficit is `m` and the first few line layers
can have at most `K-1` outside agreements, where the outside-core quotient
is unavailable.

On an affine explanation line `a_gamma=A+gamma p`, the coordinates agreeing
for every parameter are exactly those where the base and direction pair
`(A,b+p)` explains the received pair.  Pair noncontainment limits this total
common core to `m-1`.  Off the core, agreement sets are disjoint, giving

```text
L <= N-m+1.
```

Use this cap when the exact outside agreement `A_r` is at most `K-1`, and
the sharper outside-zero-core cap otherwise.  Combining the top-third
layers with the Johnson prefix gives exact new walls

```text
KoalaBear:   e<=95943, endpoint bound 27414298;
Mersenne-31: e<=67452, endpoint bound 16266965.
```

KoalaBear stops at `e=95944` because the prefix denominator at `H` is
`-1037`.  Mersenne stops at `e=67453` with valid bound `17248067`, missing
budget by `470852`.

```text
start:                   d195e43ea
canonical prize:         c8d48cd4b (no newer Fable commit)
upstream export head:    #1165 @ 1913917f; import note posted to #1164
result:                  NARROWED + EXPORTED; one PROVED
                         full-lift/common-core compiler
DAG delta:               +1 PROVED node, +3 edges
critical status delta:   none; replacement target remains TARGET
full-lift residuals:     KoalaBear 95944<=e<=1044238;
                         Mersenne 67453<=e<=1044241
delta-star movement:     none
compute:                 exact local integer scans under RAMguard;
                         no Modal
next route action:       replace the low-agreement prefix Johnson cap and
                         seek a 470852 saving at the first unpaid Mersenne
                         support
```
