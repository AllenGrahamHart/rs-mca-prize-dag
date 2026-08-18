# Cycle 449: DLI orthogonal-correlation no-go

## Starting pins

```text
our branch: codex/full-prize-resolution-v12-20260807
our SHA: 8d1c4edd0
canonical prize SHA: 0dd5b3244
upstream main SHA: 93fba1be3
newest open upstream PR: #1173 (2788d5ec3)
critical mandatory-open count: 28 declarations / 27 orbit targets
```

Canonical and upstream remained unchanged.

## Action

Audit whether the new all-depth Haar-event target can be supplied by a
generic discrete Brascamp-Lieb, entropy, or orthogonal-subspace theorem.

## Result: PROVED route fence

On each four-bit block, the balanced Walsh forms

```text
U=X1+X2-X3-X4,       V=X1-X2+X3-X4
```

are orthogonal. Their individual null counts are `6` and `6`, while their
joint null count is `4`. Tensoring `r` disjoint blocks gives exact correlation
excess `(16/9)^r`. At `r=3`, `n=12`, it already exceeds `sqrt(2n)`; in
general it exceeds every fixed polynomial.

Therefore coordinate independence, coefficient balance, and orthogonality
cannot close C2''. A surviving theorem must exploit target-specific cyclic
root-of-unity coefficients, nested frequency allocation, antipodal
first-owner deletion, or another comparably strong property. The fixture
does not falsify the DLI square-root candidate.

## Burn-down

```text
node/workboard item: reduced DLI C2'' / C2-INT
result: generic orthogonality/entropy route excluded
DAG delta: +1 PROVED background node, +1 evidence edge
upstream delta: future Q/SPI packet fence recorded; no live-PR export
delta-star movement: none
new assumptions: none
live compute requests: none
Modal spend: zero
next action: isolate a cyclic/nested property strong enough to control the
             primitive Haar correlation, or falsify that sharper pose
```

## Replay

```text
tools/ramguard tiny -- python3 background/nodes/dli_orthogonal_bernoulli_correlation_no_go/verify.py
tools/ramguard tiny -- python3 background/nodes/dli_orthogonal_bernoulli_correlation_no_go/verify_audit.py
```
