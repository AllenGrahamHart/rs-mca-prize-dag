# Cycle 470: triple-owner pole-simple rational router

## Starting pins

```text
our SHA: d1c220797
canonical prize SHA: 0dd5b3244
upstream main SHA: 93fba1be3
upstream factor-synchronization tip: #1173 at 2788d5ec3
upstream split-pencil tip: #1170 at d296510e80
```

## Result: PROVED denominator-root localization

Pair types with at most two owners cost at most `2*58361=116722` records.
The heavy orientation therefore retains `322359637` records on triple-owner
types. If their common core contained `K-2` points, dimension-two
shortening and restoration of all low-multiplicity records would cap the
orientation at

```text
241*981115+116722=236565437,
```

short by `85910922`. One triple-owner pair owns at least `5524` records.

Use three records from every one of at most four nonanchor component-basis
types and fill the order-32 packet from the anchor. At least 20 anchor
records remain. Core-saturated exact supports have common intersection
equal to the recovered core; exact cancellation gives degree `20..31` and
empty residual common support. Pure locators are excluded by the same
`m'+67451` two-core root surplus.

For a rational certificate, the affine locator scalar has at most one zero.
At a common domain pole `Q=A=B=0`, at least two of the three supports from
every represented pair must contain the pole. Core saturation would put it
in every residual pair core, contradicting their empty intersection. Thus
common poles do not occur. If any root of `Q` lay in two selected supports,
their two distinct slopes would force `A=B=0` there, again a common pole.
Consequently

```text
support multiplicity of each denominator root <=1,
total denominator-root support incidence <=deg Q<=67472.
```

## Burn-down

```text
critical target attacked: rate_half_band_crossing_location
DAG delta: +1 background PROVED node, +4 edges
critical status delta: none
route delta: arbitrary rational poles -> no common poles plus <=67472 singleton incidences
new assumptions: none
next action: build a root-free-on-support skeleton or pay chi with the explicit pair blocks
```

## Nonclaims

- `Q` need not be root-free on the whole domain;
- no rational-profile or high-complexity payment;
- no packet globalization, whole-line owner, adjacent safety, or MCA closure.

## Replay

```text
tools/ramguard tiny -- python3 background/nodes/rate_half_mca_rank11_heavy_ruling_triple_owner_pole_simple_router/verify.py
tools/ramguard tiny -- python3 background/nodes/rate_half_mca_rank11_heavy_ruling_triple_owner_pole_simple_router/verify.py --tamper-selftest
tools/ramguard tiny -- python3 background/nodes/rate_half_mca_rank11_heavy_ruling_triple_owner_pole_simple_router/verify_audit.py
```
