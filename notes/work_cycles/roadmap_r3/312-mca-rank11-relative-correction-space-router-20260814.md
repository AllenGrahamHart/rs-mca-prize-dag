# Cycle 312: MCA rank-11 relative correction spaces (2026-08-14)

The new PROVED node
`rate_half_mca_rank11_relative_correction_space_router` transfers the next
two spread-residual compilers to arbitrary global-core shortening.

For a correction span `W` of dimension `s`, every coordinate equation has
bidegree at most `(31,1)` on `P^1 x P^s`. Proper intersection and incidence
double counting give

```text
N_W <= floor(31(s+1) C(n',s+1)/C(m',s+1)).
```

For fixed `s`, every factor `(R+K'-i)/(d+K'-i)` decreases with `K'`. The
worst admissible row is therefore `K'=max(10,s)`. Exact evaluation gives

```text
s=11:  73766883380602812 < B_*,
s=12: 1241731241521316220 > B_*.
```

Thus proper spaces are uniformly paid through dimension 11. A nonproper
`s+1`-tuple is not left untyped: evaluation rank below `s` gives a rank-flat,
while rank `s` gives an exact polynomial correction curve on which the extra
coordinate equations vanish identically.

For `V=span(W,H_2,...,H_31)` with minimum support `R+a`, generalized-weight
basis counting gives, whenever `W` does not absorb the high core,

```text
N_W <= floor(M_a n'_fall_s/(d+a)_rise_s),
M_a=floor(31(R+a)/(d+a)).
```

The worst endpoint is the deployed `n` and `a=1`. It pays through dimension
9 with cap `13013823503882165`; the adjacent dimension-10 value
`404431535289439486` is a method wall.

The exact residual is now:

```text
dimension >=12,
or a positive-dimensional rank-flat / polynomial clone component;
dimension <=9 survivors must absorb the high core.
```

Focused verification:

```text
RATE_HALF_MCA_RANK11_RELATIVE_CORRECTION_SPACE_ROUTER_PASS
  proper11=73766883380602812 proper12=1241731241521316220
  clone9=13013823503882165 controls=6/6
RATE_HALF_MCA_RANK11_RELATIVE_CORRECTION_SPACE_ROUTER_AUDIT_PASS
  proper11=73766883380602812 clone9=13013823503882165 controls=5/5
```

A written cross-multiplication around the floored clone multiplier was
repaired during proof review: the valid step is
`N(B)<=floor(real quotient)<=M_a`. No Modal computation was used.

```text
start:                   a0f0adc4d
DAG delta:               +1 PROVED correction-space router,
                         +2 requirement edges, +1 evidence edge
critical status delta:   none
upstream terminal delta: H_C reduced to dimension>=12 or typed components
delta-star movement:     none
compute:                 twelve exact local endpoint evaluations
next route action:       classify positive-dimensional relative components
                         or prove an aggregate high-dimensional census
```
