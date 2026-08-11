# Cycle 109: quadratic gap-four two-simple marked factorization (2026-08-11)

## Cycle pins

```text
our start:       3181e32b0
canonical prize: 3edb8b31b6735a0a2302a578a21dc6e50bd64046
upstream local:  fde7d56d0f2d8f135db4f2226e1978644a6c9f44
compute:         none
critical open:   28
```

## Field-valued squarefree-arm gate

Pushing the exact vertical divisors to the parameter line gives

```text
Q(-;x_1)=c_1G_1^2S_1^3,   deg(G_1,S_1)=((e-3)/2,1);
Q(-;x_2)=c_2G_2^2S_2^3,   deg(G_2,S_2)=((e-9)/2,3).
```

The marked middle-Hankel determinants are therefore

```text
tau c_i^2D_1G_i^4S_i^6.
```

This exposes exact field-valued constraints for the two-simple arm. Shared
roots among the factors remain allowed; no overlap bound or exclusion is
claimed.

## Burn-down

```text
result:                  EXPOSED two heavy square-times-cube row forms
DAG delta:               +1 PROVED leaf, +2 req edges, +1 ev edge
critical status delta:   narrowed, still TARGET
upstream terminal delta: none
delta-star movement:     none
new assumptions:         none
compute requests:        none
```

Next use a simultaneous two-row invariant or Forney-value relation. Treating
the two factorizations independently is unlikely to close the packet.
