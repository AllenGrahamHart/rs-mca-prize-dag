# Cycle 491: pole-simple small-owner payment

## Result: PROVED owner localization import and pole adapter

Upstream `thm:owner-localization` and `cor:small-owner` pay every pole-free
coherent atom whose owner set has size at most `2m-K`. For our pole-simple
certificates, at most one selected support uses each denominator root. Remove
those at most `rho<=67472` records and puncture the roots.

If `g<m`, owner localization gives at most `n-rho-m+1` retained records; if
`m<=g<=2m-K`, the upstream half-distance pincer and outside-owner injection
give at most `n-rho`. Restoring `rho` pole records yields exact caps

```text
g<m:          981105,
g<=2m-K:     2097152.
```

Hence any larger coherent atom has `g>=1183521`.

## Burn-down

```text
starting local pin:       a21431ef5
canonical prize pin:      0dd5b3244
upstream source pin:      93fba1be3
DAG delta:                +1 PROVED import/adapter node, +3 edges
critical status delta:    none
closed interface:         pole-simple small-owner atom payment
compute spend:            none
next action:              exclusive large-owner image bound
```

## Nonclaims

- no large-owner image/fiber bound;
- no pair-pencil payment or high-complexity payment;
- no rank-eleven closure or MCA closure.
