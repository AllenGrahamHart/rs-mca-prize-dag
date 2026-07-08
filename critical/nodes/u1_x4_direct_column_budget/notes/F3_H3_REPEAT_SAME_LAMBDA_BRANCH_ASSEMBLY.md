# F3 h=3 repeat same-lambda branch assembly

Status: CONDITIONAL BRANCH ASSEMBLY, NOT `H3-VALUE-INJECTIVE`.

This packet records the branch decomposition of the same-lambda value gate.

## Strict Injectivity Route

The strict gate

```text
H3-VALUE-INJECTIVE
```

is implied by two branch gates:

```text
H3-VALUE-GEN-INJECTIVE:
  for lambda != 1, no two admissible generic S_3 ratio orbits occur for the
  same lambda;

H3-VALUE-SCALE-INJECTIVE:
  for lambda = 1, no two admissible primitive-cube scale orbits occur.
```

The current arithmetic interfaces are:

```text
generic:  membership S_total=14, off-orbit product total degree=10;
scale:    membership S_total=6,  scale off-orbit degree=3.
```

Thus

```text
H3-VALUE-GEN-INJECTIVE + H3-VALUE-SCALE-INJECTIVE
  => H3-VALUE-INJECTIVE.
```

## Count Route

The scale-count compiler gives

```text
K_1 <= floor((n-1)/3)
```

for the number of admissible `lambda=1` scale orbits.  Therefore, if the
generic branch is strictly injective but the scale branch is handled by
counting, at most

```text
binom(floor((n-1)/3), 2)
```

same-lambda scale collision pairs remain.  This is below `n^2` on every
official row.

This count route is not the same as proving `H3-VALUE-INJECTIVE`; it is a
separate payment option for arguments that can tolerate a quadratic exceptional
branch.

## Replay

Standalone:

```bash
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_repeat_same_lambda_branch_assembly.py
```

Expected digest:

```text
H3_REPEAT_SAME_LAMBDA_BRANCH_ASSEMBLY_PASS
```
