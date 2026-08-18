# Cycle 441: DLI unreduced coset counterexample and primitive-scope repair

## Starting pins

```text
our branch: codex/full-prize-resolution-v12-20260807
our SHA: 427ce12d2
canonical prize SHA: 0dd5b3244
upstream main SHA: 93fba1be3
relevant open PRs: #1173 (2788d5ec3), #1172, #1171, #1170
critical mandatory-open count: 28 TARGET nodes
```

Canonical and upstream sources were unchanged. No Modal job was launched.

## Action

Audit the `dli_c2pp_joint_reserve` endpoint after rounds 25--26 exposed a
near-cap quotient atom, and reconcile the old `_reduced` C2'' input with the
unreduced `W_cen` string used by its consumer assembly.

## Result: FALSIFIED AND REPAIRED

`dli_unreduced_coset_endpoint_counterexample` is PROVED. The explicit number

```text
q = 340282366920938463463374607431768211201 * 2^128 + 1
```

is prime by Proth's theorem, is below `2^256`, and is `1 mod 2^41`. At
`n=2^41,t=2^33`, unions of `1..64` among the 128 quotient fibers give

```text
sum_(m=1)^64 binom(128,m)
  = 182116756481433273164755097604074381602 > 2^127
```

central `t`-null supports. Exact Bernoulli arithmetic gives
`q^t/2^n>1/2`, so their unreduced normalized mass exceeds `2^126`. The
unreduced `2^121` endpoint is false.

Every witness is quotient-periodic and nonprimitive. The x4 consumer already
assigns that class to the structured column and asks DLI for the primitive
residue. The live nodes are therefore re-posed on

```text
q^(-t+H) W_cen^prim = E_U[product_j rho_j]_reduced.
```

The current two-input implication is replayed by
`verify_reduced_assembly.py`; it remains conditional on reduced C2'' and the
100-bit marginal baseline. Rounds 23--26 retain their exact telescoping and
freeze-tail theorems, but their unreduced fits no longer count as evidence for
the repaired red.

## Burn-down

```text
node/workboard item: DLI C2'' / B-WEAK primitive ownership
result: unreduced target refuted; live target repaired
DAG delta: +1 PROVED counterexample, +1 scope-evidence edge; open count unchanged
upstream delta: possible quotient/prefix ownership warning; no PR opened
delta-star movement: none
new assumptions: none
live compute requests: none
Modal spend: zero
next action: derive a first-owner-deleted telescoping identity for X_prim,
             then attack the primitive endpoint analytically
```

## Replay

```text
tools/ramguard tiny -- python3 background/nodes/dli_unreduced_coset_endpoint_counterexample/verify.py
tools/ramguard tiny -- python3 background/nodes/dli_unreduced_coset_endpoint_counterexample/verify_audit.py
tools/ramguard tiny -- python3 critical/nodes/dli_prime_weighted_large_block_support/verify_reduced_assembly.py
tools/ramguard local -- python3 tools/verify_prize_dag.py
```
