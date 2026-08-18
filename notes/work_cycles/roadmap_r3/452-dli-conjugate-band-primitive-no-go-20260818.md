# Cycle 452: DLI conjugate-band primitive no-go

## Starting pins

```text
our branch: codex/full-prize-resolution-v12-20260807
our SHA: eb7067ec5
canonical prize SHA: 0dd5b3244
upstream main SHA: 93fba1be3
newest open upstream PR: #1173 (2788d5ec3)
critical mandatory-open count: 28 declarations / 27 orbit targets
```

Canonical and upstream remained unchanged.

## Action

Falsify the tempting stronger premise that cyclic phase rows, disjoint
frequency bands, and antipodal primitive deletion imply polynomial
correlation loss without using the official one-sided prefix.

## Result: PROVED primitive cyclic no-go

On `n=8r`, the disjoint conjugate bands

```text
F_2={2+8l},       F_6={6+8l}=-F_2
```

define identical null events. Fourier localization gives `36` local event
words and `4` antipodal-owner words. The exact primitive joint-to-product
ratio is

```text
(64/9)^r(1-9^(-r)).
```

It is `512/81>sqrt(16)` at `r=1` and grows exponentially. Independent
direct Fourier replays at `(n,q)=(8,17)` and `(16,97)` reproduce every count.

This does not falsify C2'': the official frequency set lies in `1,...,t`
with `t<n/2`, so it contains no conjugate pair. It proves that the one-sided
low-prefix hypothesis is load-bearing and must appear in any proposed
correlation theorem.

## Burn-down

```text
node/workboard item: reduced DLI C2'' / C2-INT
result: generic primitive cyclic-band premise refuted
DAG delta: +1 PROVED background node, +1 evidence edge
upstream delta: future Q/SPI scope warning recorded; no live-PR export
delta-star movement: none
new assumptions: none
live compute requests: none
Modal spend: zero
next action: attack the one-sided split-Pell prefix itself; do not weaken its
             spectral scope in theorem search
```

## Replay

```text
tools/ramguard tiny -- python3 background/nodes/dli_cyclic_conjugate_band_primitive_no_go/verify.py
tools/ramguard tiny -- python3 background/nodes/dli_cyclic_conjugate_band_primitive_no_go/verify_audit.py
```
