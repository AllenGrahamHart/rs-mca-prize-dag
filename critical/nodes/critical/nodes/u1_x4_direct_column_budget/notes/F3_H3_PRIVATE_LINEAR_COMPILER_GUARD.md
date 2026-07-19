# F3 h=3 private-linear compiler guard

Status: PROVED ARITHMETIC GUARDRAIL / ROUTE SPLIT, NOT `RC-RANK`.

This packet prevents a subtle overclaim in the h=3 rank route.  The current
non-diagonal bridge-budget compiler uses the full degree-2 denominator cap

```text
L(A,B,H) = (A - 1) + 6H(B - 1).
```

A private-linear rank theorem would only give the smaller one-curve degree
space

```text
L_private(A,B,H) = (A - 1) + 3H(B - 1).
```

The existing compiler witnesses cannot be justified by that smaller rank cap.

## Pre-registration

Question:

```text
If the next rank theorem proves only private-linear degree-space fullness, can
it be plugged into the current h=3 non-diagonal compiler unchanged?
```

Success criterion:

- check every current official non-diagonal witness row;
- prove that each current row needs the full degree-2 rank room, not merely
  the private-linear degree room;
- verify a few representative private-linear retuned witnesses, without
  claiming maximality.

Failure criterion:

- silently use a degree-2 compiler with only a private-linear rank theorem;
- claim the representative private-linear witnesses are optimal;
- promote this arithmetic guard to `H3-ACT`.

## Current-Witness Guard

For each official row `s=13..41`, the banked non-diagonal witness has

```text
C_red D(A+D) < A + 6n(B-1),
```

as required by the degree-2 rank target, but

```text
C_red D(A+D) >= A + 3n(B-1).
```

Thus a theorem proving only private-linear degree-space fullness would not
justify the current bridge-budget table.  The next proof route must choose one
of two tracks:

```text
Track 1: prove rank for genuine repaired degree-2 signature curves and keep
         the current compiler;
Track 2: prove only private-linear rank, then rerun the compiler with
         L_private and new parameters.
```

## Representative Retuned Witnesses

The verifier also checks six representative private-linear retuned boxes.  They
are not claimed optimal; they only show the private-linear track is not
automatically dead.

```text
s=13, Z=23
s=16, Z=47
s=20, Z=119
s=23, Z=238
s=32, Z=1908
s=41, Z=11563
```

For each row it verifies:

```text
13 D(A+D) Z < A B^3,
13 D(A+D) Z < Z (L_private + 1),
ceil(Z L_private / D) <= 16 n.
```

These are representative passing boxes only.  A full private-linear compiler
would need an exact maximality scan analogous to the existing non-diagonal
compiler.

## Replay

```bash
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_private_linear_compiler_guard.py
```

Expected digest:

```text
H3_PRIVATE_LINEAR_COMPILER_GUARD_PASS
```
