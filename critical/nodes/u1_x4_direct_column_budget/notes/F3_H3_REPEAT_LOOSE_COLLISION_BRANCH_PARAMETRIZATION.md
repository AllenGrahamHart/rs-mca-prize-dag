# F3 h=3 repeat loose collision-branch parametrization

Status: PROVED ALGEBRAIC COMPILER PLUS FINITE GUARDRAILS.

This packet turns the two normalized lambda-coordinate collision branch types
into one-parameter families.

## Parametrization

Let

```text
D(a) = a^2 + a + 1.
```

The two `S_3`-normalized branch representatives are linear in `b`.

### Branch A

Representative:

```text
L_a = 1/b.
```

The divisor is

```text
b(a^2+a+1) - a(a+1) = 0,
```

so

```text
b = a(a+1)/(a^2+a+1).
```

### Branch B

Representative:

```text
L_a = -1/(1+b).
```

The divisor is

```text
b(a^2+a+1) + 2a^2 + 2a + 1 = 0,
```

so

```text
b = -(2a^2+2a+1)/(a^2+a+1).
```

On the original loose-system locus the denominator `D(a)` is nonzero; if
`D(a)=0`, neither representative divisor can vanish without violating the
existing non-pole exclusions.

## Secondary Collisions

Pulling the remaining eight lambda-coordinate divisors back along either
branch gives explicit one-variable secondary-collision subcells.  These are
emitted by the replay.  Thus the special loose-line analysis can be organized
as:

```text
generic branch:       no lambda-coordinate divisor;
branch A:             b = a(a+1)/(a^2+a+1);
branch B:             b = -(2a^2+2a+1)/(a^2+a+1);
secondary subcells:   one-variable pullbacks inside A or B.
```

## Role in h=3

The loose affine-line target is now reduced to a generic nine-slope condition
plus two one-parameter special families after the normalized `S_3` quotient.
This is a cleaner input for a future line-counting or incidence theorem.

## Replay

Standalone:

```bash
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_repeat_loose_collision_branch_parametrization.py
```

Expected digest:

```text
H3_REPEAT_LOOSE_COLLISION_BRANCH_PARAMETRIZATION_PASS
```
