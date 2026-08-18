# Cycle 444: DLI primitive square-root falsifier

## Starting pins

```text
our branch: codex/full-prize-resolution-v12-20260807
our SHA: a4804cce7
canonical prize SHA: 0dd5b3244
upstream main SHA: 93fba1be3
newest open upstream PR: #1173 (2788d5ec3)
critical mandatory-open count: 28 declarations / 27 orbit targets
```

Fable and upstream remained unchanged during the run.

## Action

Preregister and try to falsify `J_prim<=sqrt(2n)`, which would specialize to
the exact 21-bit C2'' reserve at `n=2^41`. Run only exact `t=2` towers, with
one Modal task per row and a hard partial-result timeout.

## Result: SURVIVED, NOT PROVED

All 13 rows returned. The controls reproduce the frozen bank. The previous
maximum remains

```text
(n,t,q) = (32,2,5857),
J_prim = 14680064/5498847,
log2 J_prim = 1.4166572071 < 3 = log2 sqrt(2n).
```

Every new ratio at `n=64,128,256` is strictly below one. No candidate firing
occurred. This supplies no depth transport and does not add a DAG premise.

## Burn-down

```text
node/workboard item: reduced DLI C2'' / C2-INT
result: square-root closing scale survives exact t=2 falsification
DAG delta: none; evidence appended to existing TARGET
upstream delta: none
delta-star movement: none
new assumptions: none
live compute requests: none
Modal run: ap-Wp4hwSuVlFwEDllxpual4c
Modal spend: small 13-container run, each <=8.29 seconds
next action: derive primitive support-pattern overlap/collision identities
             and determine whether they can prove the square-root constant
```

## Replay

```text
tools/ramguard modal -- modal run notes/pilots_20260818/c2_primitive_sqrt_falsifier/modal_run.py --output notes/pilots_20260818/c2_primitive_sqrt_falsifier/results.json
tools/ramguard tiny -- python3 notes/pilots_20260818/c2_primitive_sqrt_falsifier/analyze.py
tools/ramguard tiny -- python3 notes/pilots_20260818/c2_primitive_sqrt_falsifier/analyze.py --tamper-selftest
```
