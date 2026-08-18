# Cycle 442: DLI primitive two-scale subtraction

## Starting pins

```text
our branch: codex/full-prize-resolution-v12-20260807
our SHA: work-cycle 441 pending
canonical prize SHA: 0dd5b3244
upstream main SHA: 93fba1be3
relevant open PRs: #1173 (2788d5ec3), #1172, #1171, #1170
critical mandatory-open count: 28 TARGET declarations / 27 orbit targets
```

Fable and the open upstream PR heads were unchanged. No Modal job was used.

## Action

Make the primitive first-owner deletion in repaired C2'' exact rather than
leaving it as an ownership instruction.

## Result: NARROWED

`dli_primitive_first_owner_antipodal_subtraction` is PROVED. In a cyclic
`2`-group, every nontrivial stabilizer contains the unique order-two shift.
Hence a support is nonprimitive exactly when it is an antipodal lift. Odd
moments cancel on each pair and even moments descend, giving at every weight

```text
T_prim(n,t,b) = T(n,t,b)                                  (b odd),
T_prim(n,t,b) = T(n,t,b)-T(n/2,floor(t/2),b/2)            (b even).
```

For the official even `t` and any central interval `I`, this becomes

```text
X_I^prim(n,t)
  = X_I(n,t) - (q^(t/2)/2^(n/2)) X_(I/2)(n/2,t/2).
```

The theorem was checked exhaustively at `n=8,16`, all weights, with one row
containing 208 genuinely primitive solutions. It removes every periodic
class in one subtraction and leaves no inclusion-exclusion tail.

## Burn-down

```text
node/workboard item: reduced DLI C2'' first-owner interface
result: NARROWED to one signed two-scale census inequality
DAG delta: +1 PROVED evidence node; critical open count unchanged
upstream delta: portable quotient/primitive ownership identity; no PR opened
delta-star movement: none
new assumptions: none
live compute requests: none
Modal spend: zero
next action: couple the existing telescoping formulas at (n,t) and
             (n/2,t/2), preserving subtraction before inequalities
```

## Replay

```text
tools/ramguard tiny -- python3 background/nodes/dli_primitive_first_owner_antipodal_subtraction/verify.py
tools/ramguard tiny -- python3 background/nodes/dli_primitive_first_owner_antipodal_subtraction/verify_audit.py
tools/ramguard local -- python3 tools/verify_prize_dag.py
```
