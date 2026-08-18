# Cycle 504: the 218-plane pure-power router

## Result: PROVED two-degree periodic reduction

Assume the endpoint residual direction pencil is projectively equivalent
on the official cyclic domain to `(X^e,1)`, with `e` a power-of-two divisor
of the domain order. Every represented direction then contains at most `e`
full coordinates. Combining

```text
F>=28396+204K',       F<=r*e<=218e,       e<=K'-1
```

with `2044<=K'<=5025` leaves exactly two degrees:

```text
e=2048:  K'=2049, r=218, 218 lines, missing slots <=72;
e=4096:  4097<=K'<=4237, r>=211, missing slots <=28744.
```

The primary verifier exhausts every one of the 2,982 possible shortened
dimensions and every power-of-two divisor degree. An independent replay
recovers the same one-row and 141-row branches; eight hostile contract
mutations are rejected.

## Burn-down

```text
starting local pin:       773771abc
canonical prize pin:      0dd5b3244
upstream main pin:        93fba1be3
DAG delta:                +1 PROVED pure-power router, +2 edges
critical status delta:    none
compute spend:            none
next action:              classify the rational map or pay the two survivors
```

## Nonclaims

- the endpoint direction pencil is not proved pure-power;
- general quotient-periodic rational maps are not classified;
- neither surviving degree is excluded or paid;
- no rank-eleven or MCA closure follows.
