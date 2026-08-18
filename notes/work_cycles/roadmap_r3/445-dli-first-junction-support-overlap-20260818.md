# Cycle 445: DLI first-junction support overlap

## Starting pins

```text
our branch: codex/full-prize-resolution-v12-20260807
our SHA: 700575513
canonical prize SHA: 0dd5b3244
upstream main SHA: 93fba1be3
newest open upstream PR: #1173 (2788d5ec3)
critical mandatory-open count: 28 declarations / 27 orbit targets
```

Fable and upstream remained unchanged during the derivation.

## Action

Replace the informal `t=2` support intuition by an all-dyadic-depth exact
theorem. Separate the first primitive junction from the unreduced tail and
identify the strongest elementary support exclusions available for free.

## Result: PROVED structural reduction

For `n=2h,t=2L`, conditioned even pair sums and odd pair skews define
probability distributions `p_S,q_S` on the same unsaturated support. The
primitive ratio factors as

```text
J_prim = 2^h sum_(S nonempty) p_Sq_S * K_tail.
```

The even count on `S` is exactly a signed null census on `S^c`. Vandermonde
rank gives `q_S=0` for `1<=|S|<=L` and `p_S=0` for
`1<=|S^c|<=L`. An independent exhaustive verifier reproduces all four
censuses, primitive deletion, and rational normalization on four fixtures.

## Burn-down

```text
node/workboard item: reduced DLI C2'' / C2-INT
result: exact support-overlap-times-tail formulation
DAG delta: +1 PROVED background node, +1 evidence edge
upstream delta: none
delta-star movement: none
new assumptions: none
live compute requests: none
next action: prove a constants-bearing overlap-times-tail bound, beginning
             with exact control of the two conditioned support laws
```

## Replay

```text
tools/ramguard tiny -- python3 background/nodes/dli_first_junction_support_overlap/verify.py
tools/ramguard tiny -- python3 background/nodes/dli_first_junction_support_overlap/verify_audit.py
```
