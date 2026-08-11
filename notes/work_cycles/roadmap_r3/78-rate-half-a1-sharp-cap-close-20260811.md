# Cycle 78: `A=1` sharp-cap closure (2026-08-11)

## Cycle pins

```text
our start:       6b92b7063
canonical prize: 3edb8b31b6735a0a2302a578a21dc6e50bd64046
upstream main:   93fba1be3f3299b0ba4708d88715377bbb656e45
open upstream:   38 PRs; no new overlap
critical open:   28
```

## All-core corollary

The three- and four-contact inequalities jointly exclude `ell=0` for every
official `A=1` degree and every core size:

```text
s=0: e=m+1,m+2 by four contacts; e>=m+3 by three contacts;
s=1: floor(Delta/3)+2<e throughout;
s=2: already empty.
```

Every core-one survivor satisfies the stronger lower bound

```text
ell>=e-2-floor(Delta/3)>=1.
```

The proved node is
`rate_half_ca_hankel_a1_all_core_sharp_cap_exclusion`.

## Frontier correction

The historical maximal-degree core-one corrected-square chain studies a
sharp-cap profile. It remains valid as a sequence of necessary reductions,
but it is no longer a live endpoint route because the parent profile is now
excluded before that classification is needed.

## Burn-down

```text
result:                  CLOSED every A=1 sharp-cap profile
DAG delta:               +1 PROVED leaf, +3 req edges, +1 ev edge
critical status delta:   none; positive-slack s=0,1 remain
upstream terminal delta: none
delta-star movement:     none
new assumptions:         none
compute requests:        none
```

Further work should attack positive slope slack directly and should not
continue the reciprocal corrected-square sharp-cap classifier.
