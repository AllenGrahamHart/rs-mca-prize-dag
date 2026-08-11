# Cycle 115: core-free cubic coefficient clone-rank gate (2026-08-11)

## Cycle pins

```text
our start:       7fb10f08f
canonical prize: 3edb8b31b6735a0a2302a578a21dc6e50bd64046
upstream local:  fde7d56d0f2d8f135db4f2226e1978644a6c9f44
compute:         local tiny verifier only
critical open:   28
```

## Whole coefficient-chain gate

Pair every equation in the complete chain

```text
M_0q_i+M_1q_(i-1)=0
```

with the specialized left apolar kernel. On
`X=S_beta\S_alpha`, every coefficient row lies in the same weighted
Vandermonde nullspace. Consequently

```text
rank (Q_i(x))_(x in X,0<=i<=e)
 <=|S_alpha union S_beta|-rho.
```

At minimum union `rho+1`, all `c_alpha+1` row forms `Q(-;x)` on the
difference are nonzero and proportional. This applies even at the possible
`E_1` slope.

## Burn-down

```text
result:                  REDUCED small-union pairs to low-rank row fibres
DAG delta:               +1 PROVED leaf, +4 req edges, +1 ev edge
critical status delta:   narrowed, still TARGET
upstream terminal delta: none
delta-star movement:     none
new assumptions:         none
compute requests:        none
```

Next prove point separation or classify low-rank fibres of
`x |-> [Q(-;x)]` using the Hankel/apolar origin and the exact heavy/light row
divisors. A bare separation claim is not assumed.
