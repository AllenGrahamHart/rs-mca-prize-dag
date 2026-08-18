# Cycle 443: DLI primitive joint-ratio telescoping

## Starting pins

```text
our branch: codex/full-prize-resolution-v12-20260807
our SHA: 832c0788e
canonical prize SHA: 0dd5b3244
upstream main SHA: 93fba1be3
newest open upstream PR: #1173 (2788d5ec3)
critical mandatory-open count: 28 declarations / 27 orbit targets
```

Fable remained clean and unchanged. Upstream had no PR newer than #1173.
No Modal job was used.

## Action

Insert the proved antipodal subtraction into the exact full-tower
telescoping ratio without losing cancellation.

## Result: NARROWED

`dli_primitive_joint_ratio_telescoping` is PROVED. With `t=2^m`, exact
level censuses `Z_j`, junction censuses `B_j`, and first coset census `C_1`,

```text
C_1 = Z_0(q,n/2,t/2),
J_prim = 2^(nm)(Z_0-C_1)/(Z_m product_(j<m) B_j).
```

The central primitive ratio is at most `J_prim`, so repaired C2'' reduces
to one positive integer inequality `J_prim<=2^21`. On all 45 banked exact
full towers, 29 primitive numerators vanish and the maximum is
`14680064/5498847`, or `1.4166572071` bits. This is evidence only.

## Burn-down

```text
node/workboard item: reduced DLI C2''
result: NARROWED to C2-INT, one positive integer inequality
DAG delta: +1 PROVED evidence node; critical open count unchanged
upstream delta: portable primitive-prefix correction identity; no PR opened
delta-star movement: none
new assumptions: none
live compute requests: none
Modal spend: zero
next action: derive an official-scale upper bound for Z_0-C_1 relative to
             the exact terminal and block marginals
```

## Replay

```text
tools/ramguard local -- python3 background/nodes/dli_primitive_joint_ratio_telescoping/verify.py
tools/ramguard tiny -- python3 background/nodes/dli_primitive_joint_ratio_telescoping/verify_audit.py
tools/ramguard local -- python3 tools/verify_prize_dag.py
```
