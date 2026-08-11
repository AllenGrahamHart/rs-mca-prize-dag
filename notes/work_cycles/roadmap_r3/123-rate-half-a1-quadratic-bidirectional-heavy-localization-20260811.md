# Cycle 123: quadratic bidirectional heavy localization (2026-08-11)

## Cycle pins

```text
our start:       182e55e06
canonical prize: 3edb8b31b6735a0a2302a578a21dc6e50bd64046
upstream local:  fde7d56d0f2d8f135db4f2226e1978644a6c9f44
compute:         two local tiny integer verifiers
critical open:   28
```

## Actual supports couple every orientation

The old orientation restriction came from counting full padded locators.
Every support-difference row is light, so actual supports give a stronger
minimum-distance argument. Both orientations now have rank two for every
endpoint-deficit pattern. Their gcds exchange endpoints and share every
other root.

A residual root with positive deficit already shares enough actual support
with the endpoint union to lie on the endpoint center line, where it would
be a gcd root. Therefore all forward and reverse residual roots have deficit
zero; a second actual-support argument makes every cross-orientation pair of
residual sets disjoint.

For `R=r_alpha+r_beta`, the exact unused supported-slope slack is

```text
s=(R+5)g-(R+3)e+2.
```

All packet deficit `e-6` is now localized to the common center line or this
slack. Combining slack capacity with the exact line missing count sharpens
the official gcd floors through the values printed in `(BHL9)`.

## Burn-down

```text
result:                  FORCED bidirectional coupling and heavy localization
DAG delta:               +1 PROVED leaf, +3 req edges, +1 ev edge
critical status delta:   narrowed, still TARGET
upstream terminal delta: none; not yet a complete Lane-T atom
delta-star movement:     none
new assumptions:         none
compute requests:        none
```

Next use the exact slack formula and the marked heavy-row factors to prove
that the slack cannot absorb the required heavy divisor, or classify the
remaining intersection profile exactly.
