# Cycle 116: quadratic two-slope coefficient-rank spread (2026-08-11)

## Cycle pins

```text
our start:       0b97afbb5
canonical prize: 3edb8b31b6735a0a2302a578a21dc6e50bd64046
upstream local:  fde7d56d0f2d8f135db4f2226e1978644a6c9f44
compute:         local tiny verifier only
critical open:   28
```

## Symmetric extra-row gain

In the core-one residual middle Hankel pencil, a rank-loss-`r` slope has
`r+1` left-kernel multiples. Applying the complete coefficient chain on a
two-error difference gives

```text
|S_alpha union S_beta|>=rho+2,
rank Ev_(alpha,beta)<=|S_alpha union S_beta|-rho-1.
```

The improved pair union changes the center-line count to

```text
2h<=rho+2-sum r_gamma.
```

Every fixed locator pair now has at least
`ceil((rho+6+r_alpha+r_beta)/2)` expanding thirds, instead of only
`3+r_alpha+r_beta`.

## Burn-down

```text
result:                  STRENGTHENED quadratic spread from constant to linear
DAG delta:               +1 PROVED leaf, +3 req edges, +1 ev edge
critical status delta:   narrowed, still TARGET
upstream terminal delta: none
delta-star movement:     none
new assumptions:         none
compute requests:        none
```

Next test the exact double-root and two-simple degree sequences against this
linear-size spread. The Cycle-107 cyclic design only survived the obsolete
constant-size condition and is no longer a route fence for this attack.
