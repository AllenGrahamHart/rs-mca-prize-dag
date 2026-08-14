# Proof

Let `rho=990810934/10^9` be the proved global component-incidence density,
and let `alpha` be the fraction of records whose own component density is at
least `tau=98/100`. Records below the threshold contribute at most `tau` and
the rest at most one, so

```text
rho<=alpha+(1-alpha)tau.
```

Therefore

```text
alpha>=(rho-tau)/(1-tau)
     =10810934/20000000
     =540546700/10^9.                               (1)
```

Multiplying (1) by the unsafe non-dense floor `274980728111260126` and
rounding upward gives `148639925144138894` records.

Fix one such record with exact support `S`, `|S|=m'`. Count pairs `(B,x)`
where `B subset S` has size ten, `x in S minus B`, and `B union {x}` is a
component eleven-subset. Each component eleven-subset is counted eleven
times. Since

```text
11*C(m',11)=C(m',10)(m'-10),
```

some `B` has at least

```text
E(K')=ceil(98(m'-10)/100)                            (2)
```

component extensions.

## Full evaluation rank

If `ev_B:V'->F^B` has rank ten, the ten normalized coordinate equations
determine one rational correction curve. After multiplication by the dense
locator, it is one affine owner pair. An extension is a component precisely
when its coordinate equation vanishes identically on that curve. Thus all
component extensions belong to the same owner core. Its intersection with
`S` contains `B` and all those extension coordinates, hence has size at
least `10+E(K')`.

Its deficiency is at most

```text
m'-10-E(K')=floor(2(m'-10)/100).
```

This increases with `K'` and at `K'=1048576` equals `22320`.

## Evaluation rank nine

Suppose `rank ev_B=9` and let `u` span its kernel. The polynomial `u` is
nonzero of degree below `K'` and already vanishes at the ten coordinates of
`B`. It can vanish at no more than `K'-11` further coordinates. Therefore
at least

```text
E(K')-max(0,K'-11)                                  (3)
```

component extensions have full evaluation rank ten.

All corresponding owner pairs agree with the received pair on `B` and own
the fixed record at slope `gamma`. Differences of any two such pairs have
both components in `ker ev_B=F*u`, say `(alpha*u,beta*u)`. Ownership of the
same explanation at `gamma` gives `alpha+gamma*beta=0`. Hence every pair is
on one affine pencil with direction `(-gamma*u,u)`.

Expression (3) is nonincreasing up to rounding as `K'` grows: `E` gains at
most one per step while the root allowance gains one. Its minimum is at
`K'=1048576`, where

```text
E=1093718,       K'-11=1048565,       E-(K'-11)=45153.
```

## Lower evaluation rank

If `rank ev_B<=8`, rank-nullity in the ten-dimensional `V'` gives

```text
dim ker ev_B>=2.
```

The three alternatives exhaust the possible evaluation ranks. They are
recordwise statements; owners, pencils, and kernel planes attached to
different records are not identified or summed.
