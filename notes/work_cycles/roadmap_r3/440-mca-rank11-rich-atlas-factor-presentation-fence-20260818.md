# Cycle 440: rank-eleven rich-atlas factor-presentation fence

## Starting pins

```text
our branch: codex/full-prize-resolution-v12-20260807
our SHA: 4fb9f49ab
canonical prize SHA: 0dd5b3244
upstream main SHA: 93fba1be3
relevant open PRs: #1173 (2788d5ec3), #1172, #1171, #1170
critical mandatory-open count: 28 TARGET nodes
```

Canonical and upstream heads are unchanged. No source tree was modified.

## Action

Adversarially test whether the full-span rich-container population alone can
force the exact `2 x 5` factor presentation used by the conditional router.

## Result: BARE INFERENCE REFUTED

`rate_half_mca_rank11_full_span_rich_atlas_factor_presentation_fence` is
PROVED. Let `H=38385`, take two coprime split degree-`H` locators, and multiply
them by generic five-spaces of polynomials of degree at most `H+4`. Their
direct sum is ten-dimensional, has global gcd one, and contains more than
`16384884` rich two/three-spaces spanning the whole correction space.

The family of such ten-spaces has dimension `383850`. Every polynomial
`2 x 5` product locus has dimension at most `383845`. Exact Gaussian bounds
show this five-dimensional gap survives over official-size finite fields,
with ambient degree `76774<K`.

Thus presentation existence must use omitted received-line data: anchored
row-space chronology, slope mass, or ownership compatibility.

## Upstream export

The prior factor router and its two-threshold wall were posted to PR `#1173`:
`https://github.com/przchojecki/rs-mca/pull/1173#issuecomment-5327317502`.
The new presentation fence should travel in the next consolidated successor
packet, not as a competing PR while `#1173` remains open.

## Burn-down

```text
node/workboard item: KoalaBear rank-eleven factor-presentation existence
result: bare-atlas inference refuted; chronology-aware target isolated
DAG delta: +1 PROVED background node; critical open count remains 28
upstream delta: factor router/wall exported to #1173
delta-star movement: none
new assumptions: none
live compute requests: none
Modal spend: zero
next action: formulate a chronology-weighted synchronization inequality, or
             move to a nearer mandatory critical closure
```

## Replay

```text
tools/ramguard tiny -- python3 background/nodes/rate_half_mca_rank11_full_span_rich_atlas_factor_presentation_fence/verify.py
tools/ramguard tiny -- python3 background/nodes/rate_half_mca_rank11_full_span_rich_atlas_factor_presentation_fence/verify_audit.py
tools/ramguard tiny -- python3 background/nodes/rate_half_mca_rank11_full_span_rich_atlas_factor_presentation_fence/verify.py --tamper-selftest
tools/ramguard local -- python3 tools/verify_prize_dag.py
```
