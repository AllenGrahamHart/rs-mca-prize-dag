# Cycle 120: quadratic sharp-pair exclusion (2026-08-11)

## Cycle pins

```text
our start:       45b01e4e0
canonical prize: 3edb8b31b6735a0a2302a578a21dc6e50bd64046
upstream local:  fde7d56d0f2d8f135db4f2226e1978644a6c9f44
compute:         two local tiny arithmetic verifiers
critical open:   28
```

## Sharp boundary eliminated

At hypothetical pair union `rho+2`, Cycle 118 gives a light clone class and
`e` common supported locator slopes. Full-locator union counting puts those
slopes and one endpoint on the same codeword pencil in both quadratic root
patterns. After removing the fixed core point, every point of the pencil's
joint support is light and must miss exactly one of its `e+1` slopes. The
missing-incidence count forces pencil deficit `e-2`, but the whole packet
has only deficit `e-6`. Therefore

```text
|S_alpha union S_beta|>=rho+3,
3h<=rho+3-sum r_gamma.
```

Every pair now has at least
`ceil((2rho+9+r_alpha+r_beta)/3)>=2e+3` expanding thirds. The next minimum
boundary has coefficient-row rank at most two.

## Burn-down

```text
result:                  CLOSED the quadratic rho+2 pair boundary
DAG delta:               +1 PROVED leaf, +3 req edges, +1 ev edge
critical status delta:   narrowed, still TARGET
upstream terminal delta: none
delta-star movement:     none
new assumptions:         none
compute requests:        none
```

Next classify the rank-two split row pencil at pair union `rho+3`, or use
the one-third center cap to derive a collective degree contradiction. Do not
retain Cycle 118's sharp clone case as a live realization.
