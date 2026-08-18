# Cycle 476: anchor-exchange pencil synchronization

## Starting pins

```text
our SHA: 1c870abc4
canonical prize SHA: 0dd5b3244
upstream main SHA: 93fba1be3
upstream factor-synchronization tip: #1173 at 2788d5ec3
```

## Result: PROVED synchronization dichotomy

The triple-owner packet has one anchor pair owning at least 5,524 slopes and
`t in {1,2,3,4}` secondary pair types. Select exactly 5,524 anchor slopes,
fix three records from each secondary type, and globally fix core-saturated
supports. Each packet uses

```text
s=32-3t in {29,26,23,20}
```

anchor slopes. A base packet and every one-swap packet cancel the same core
and share at least `s-1>=19` anchor exception locators.

If any packet emits high complexity, `chi>=2299571`. Otherwise every packet
is rational. Two common distinct monic locators determine the
two-dimensional polynomial pencil, so every one-swap pencil equals the base
pencil. One fixed coprime degree-`1..11` pencil then contains all 5,524
anchor locators.

## Burn-down

```text
critical target attacked: rate_half_band_crossing_location
DAG delta: +1 background PROVED node, +3 edges
critical status delta: none
route delta: dense-anchor packet-local pencil ambiguity removed
new assumptions: none
next action: compose fixed-pencil caps; pay high complexity
```

## Nonclaims

- no payment of `chi>=2299571`;
- no classification of the synchronized pencil;
- no aggregate charge over unrelated pair types.
