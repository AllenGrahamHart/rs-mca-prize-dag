# F3 h=3 repeat loose normalized system

Status: PROVED ALGEBRAIC COMPILER PLUS FINITE GUARDRAILS.

This packet normalizes the loose six-point system by scaling one core
reciprocal vertex.

## Normalization

For a loose core triple `r,s,t`, set

```text
s = a r,
t = b r,
X = 1/r.
```

The six reciprocal points become

```text
r * {1, a, b, -(1+a), -(1+b), -(a+b)}.
```

The loose condition is

```text
1+a+b != 0.
```

If `1+a+b=0`, the triangle is the contained zero-sum triangle instead.

## Membership Functions

The six coordinate membership tests are

```text
1 + X/q in H
```

for

```text
q in {1, a, b, -(1+a), -(1+b), -(a+b)}.
```

The three lambda membership tests are

```text
1 + X*(1 + 1/a - 1/(1+a)) in H,
1 + X*(1 + 1/b - 1/(1+b)) in H,
1 + X*(1/a + 1/b - 1/(a+b)) in H.
```

Together with the non-pole and distinctness exclusions, this is equivalent to
the loose six-point system.

## Guardrails

Boundary-style witness rows have no normalized loose systems:

```text
p=337   n=16  loose_systems=0
p=2017  n=32  loose_systems=0
p=4801  n=64  loose_systems=0
p=7937  n=64  loose_systems=0
p=65537 n=256 loose_systems=0
p=91393 n=256 loose_systems=0
```

The contrast row has two loose systems and six ordered normalizations for each:

```text
p=97 n=32 loose_systems=2 ordered_normalizations=12
```

## Role in h=3

The pairwise-coreless branch is now a two-ratio plus scale problem:

```text
find X,a,b satisfying the six coordinate tests,
the three lambda tests, and 1+a+b != 0.
```

Proving no such normalized system exists in the boundary regime proves
`H3-NO-LOOSE-TRIANGLE`.

## Replay

Standalone:

```bash
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_repeat_loose_normalized_system.py
```

Expected digest:

```text
H3_REPEAT_LOOSE_NORMALIZED_SYSTEM_PASS
```
