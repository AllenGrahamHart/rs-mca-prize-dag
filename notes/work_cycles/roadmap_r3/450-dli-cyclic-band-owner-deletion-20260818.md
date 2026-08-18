# Cycle 450: DLI cyclic-band owner deletion

## Starting pins

```text
our branch: codex/full-prize-resolution-v12-20260807
our SHA: 26ddb109a
canonical prize SHA: 0dd5b3244
upstream main SHA: 93fba1be3
newest open upstream PR: #1173 (2788d5ec3)
critical mandatory-open count: 28 declarations / 27 orbit targets
```

Canonical and upstream remained unchanged.

## Action

Test whether genuine dense cyclic-character rows and disjoint spectral bands
are enough to rescue a generic product-correlation route.

## Result: PROVED cyclic boundary and exact owner repair

On a cyclic domain of size `n=4r`, take the complete frequency bands

```text
F_1={1+4l:0<=l<r},       F_2={2+4l:0<=l<r}.
```

Fourier inversion across quotient fibers reduces them to independent local
order-four equations with null counts `4`, `6`, and joint count `2`.
Therefore the event correlation excess is exactly `(4/3)^r`, exponentially
large despite dense cyclic rows and disjoint bands.

Every joint local word is constant on its four-cycle. Hence every joint word
is invariant under the antipodal shift and primitive first-owner deletion
makes the numerator zero. Exact direct Fourier replays at `(n,q)=(12,13)`
and `(16,17)` reproduce the tensor counts and zero primitive numerator.

The unresolved C2'' object is therefore not generic cyclic correlation. It
is truncated low-frequency-prefix correlation after quotient ownership. No
complete-band result transports automatically across that boundary.

## Burn-down

```text
node/workboard item: reduced DLI C2'' / C2-INT
result: cyclic complete-band obstruction classified and owner-deleted
DAG delta: +1 PROVED background node, +1 evidence edge
upstream delta: future Q/SPI packet theorem recorded; no live-PR export
delta-star movement: none
new assumptions: none
live compute requests: none
Modal spend: zero
next action: derive a boundary theorem for truncating a complete cyclic band,
             with primitive ownership retained throughout
```

## Replay

```text
tools/ramguard tiny -- python3 background/nodes/dli_cyclic_band_tensor_owner_deletion/verify.py
tools/ramguard tiny -- python3 background/nodes/dli_cyclic_band_tensor_owner_deletion/verify_audit.py
```
