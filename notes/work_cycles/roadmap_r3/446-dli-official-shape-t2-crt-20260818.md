# Cycle 446: DLI official-shape `t=2` CRT falsifier

## Starting pins

```text
our branch: codex/full-prize-resolution-v12-20260807
preregistered SHA: 988916c3c
canonical prize SHA: 0dd5b3244
upstream main SHA: 93fba1be3
newest open upstream PR: #1173 (2788d5ec3)
critical mandatory-open count: 28 declarations / 27 orbit targets
```

Canonical, upstream main, and the open-PR frontier were unchanged.

## Action

Use exact additive Fourier inversion, cyclic dual-orbit reduction, and a
ten-prime CRT to test `J_prim<=sqrt(2n)` at the first depth-one row with the
official aspect ratio `n/t=256`.

## Result: SURVIVED, NOT PROVED

At `(n,t,q)=(512,2,7681)`, all 12 Modal tasks returned in at most `6.989`
seconds. Nine 60-bit moduli uniquely reconstruct each count; the tenth is an
independent residue check. The exact result is

```text
J_prim < 1,
log2 J_prim = -9.5700325316325287361066757089202379707183e-74.
```

The square-root envelope is `32`, so this row has slightly more than five
bits of slack. It says nothing about depths above one.

## Burn-down

```text
node/workboard item: reduced DLI C2'' / C2-INT
result: exact official-aspect depth-one survivor
DAG delta: none; evidence appended to existing TARGET
upstream delta: none
delta-star movement: none
new assumptions: none
live compute requests: none
Modal run: ap-ofdfyMZFhdeIDNYzJZwyX8
Modal spend: small 12-container run, each <=6.989 seconds
next action: stop depth-one scale scans and prove or refute the full-depth
             support-overlap-times-tail estimate
```

## Replay

```text
tools/ramguard modal -- modal run notes/pilots_20260818/c2_official_shape_t2_crt/modal_run.py --output notes/pilots_20260818/c2_official_shape_t2_crt/results.json
tools/ramguard tiny -- python3 notes/pilots_20260818/c2_official_shape_t2_crt/analyze.py
tools/ramguard tiny -- python3 notes/pilots_20260818/c2_official_shape_t2_crt/analyze.py --tamper-selftest
```
