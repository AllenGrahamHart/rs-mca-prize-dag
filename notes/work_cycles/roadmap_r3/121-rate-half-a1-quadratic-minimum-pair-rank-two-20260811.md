# Cycle 121: quadratic minimum-pair rank-two normal form (2026-08-11)

## Cycle pins

```text
our start:       4a725251c
canonical prize: 3edb8b31b6735a0a2302a578a21dc6e50bd64046
upstream local:  fde7d56d0f2d8f135db4f2226e1978644a6c9f44
compute:         two local tiny exact verifiers
critical open:   28
```

## Exact new-boundary pencil

At pair union `rho+3`, the weighted coefficient-chain Vandermonde nullspace
has dimension two with basis `1/L_X'` and `x/L_X'`. Rank one would recreate
an `e+1`-center pencil and is impossible by the Cycle-120 light-incidence
count. Therefore

```text
eta_x L_X'(x)Qbar(-;x)=A+xB
```

for independent parameter forms `A,B`. Distinct difference points give
distinct squarefree supported row forms. After their common gcd `G`, all
residual root sets are disjoint, so for `m=r_sigma+3`,

```text
g+m(e-g)<=3e+3,
g>=max(1,ceil((r_sigma e-3)/(r_sigma+2))).
```

Every root of `G` is center-owned by the endpoint codeword pencil.

## Burn-down

```text
result:                  CLASSIFIED rho+3 as an injective rank-two split pencil
DAG delta:               +1 PROVED leaf, +3 req edges, +1 ev edge
critical status delta:   narrowed, still TARGET
upstream terminal delta: none
delta-star movement:     none
new assumptions:         none
compute requests:        none
```

Next compare the large forced gcd in the positive-deficit cases with the
heavy-row cube/Forney divisors and the reverse-oriented pencil. The
zero-deficit `m=3` case needs a different coupling because root budget alone
forces only the endpoint common root.
