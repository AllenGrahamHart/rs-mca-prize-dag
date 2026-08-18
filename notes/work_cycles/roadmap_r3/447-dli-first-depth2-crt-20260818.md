# Cycle 447: DLI first depth-two CRT falsifier

## Starting pins

```text
our branch: codex/full-prize-resolution-v12-20260807
preregistered SHA: d07559503
canonical prize SHA: 0dd5b3244
upstream main SHA: 93fba1be3
newest open upstream PR: #1173 (2788d5ec3)
critical mandatory-open count: 28 declarations / 27 orbit targets
```

Canonical and upstream remained unchanged.

## Action

Use a first-nonzero dual gauge and three-prime CRT to compute the first exact
row with a genuine DLI tail, `(n,t,q)=(64,4,193)`, and try to falsify
`J_prim<=sqrt(2n)`.

## Result: SURVIVED, NOT PROVED

All four tasks returned in at most `10.219` seconds. The exact factor ledger
is

```text
first primitive junction: -4.9382958030e-6 bits
unreduced tail:            +5.3042421974e-6 bits
full primitive ratio:      +3.6594639437e-7 bits
square-root slack:          3.4999996341 bits
```

This is the first measured reversal by a genuine tail. It does not provide
depth monotonicity or official transport.

## Burn-down

```text
node/workboard item: reduced DLI C2'' / C2-INT
result: first exact overlap-times-tail balance
DAG delta: none; evidence appended to existing TARGET
upstream delta: none
delta-star movement: none
new assumptions: none
live compute requests: none
Modal run: ap-Xv3PG5iFZZ94Z09Qedpmko
Modal spend: small four-container run, each <=10.219 seconds
next action: analytic joint control; do not replace it by separate factor caps
```

## Replay

```text
tools/ramguard modal -- modal run notes/pilots_20260818/c2_first_depth2_crt/modal_run.py --output notes/pilots_20260818/c2_first_depth2_crt/results.json
tools/ramguard tiny -- python3 notes/pilots_20260818/c2_first_depth2_crt/analyze.py
tools/ramguard tiny -- python3 notes/pilots_20260818/c2_first_depth2_crt/analyze.py --tamper-selftest
```
