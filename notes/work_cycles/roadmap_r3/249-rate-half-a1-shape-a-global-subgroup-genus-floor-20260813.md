# Cycle 249: rate-half shape-A global subgroup genus floor (2026-08-13)

The canonical `prize` tree and the current upstream PR board were
reconciled before selecting the next action. PR `#1165` remains the current
draft affine-incidence repair packet; PRs `#1161/#1162` contain the
rate-half pair/crossing reductions already represented locally. Two prior
M31 export cycles moved neither critical status nor an adjacent bracket, so
the joint protocol's self-kill rule returns the campaign to a direct
critical branch.

On the sole surviving prime-field shape-A biform, all `R` classified rows
split into `m` distinct official subgroup slopes. This gives exactly

```text
P=Rm=151115727450087753427630
```

distinct subgroup points on the normalization. The coordinate functions
are multiplicatively independent: a translated-subtorus biform would give
at most one subgroup row per parameter because `gcd(n,2^41)=1`, while the
proved pure fiber has `n>1` such rows.

Applying the already audited positive-characteristic gcd theorem to
`t^N,X^N` forces

```text
chi_C >= 262353693488940318721,
g(C)  >= 131176846286340314460.
```

The full bidegree genus ceiling is
`50371909149143533442400`, less than `385` times the new floor. Thus a
source/Pade genus upper bound below the printed floor would close shape A;
the generic bidegree ceiling cannot. This is a direct route condition, not
a crossing closure.

```text
start:                   74ce4e1c2
canonical prize:         fdfb20a42
result:                  PROVED shape-A Euler/genus floor
DAG delta:               +1 PROVED node, +3 req edges, +1 ev edge
critical status delta:   none; rate_half_band_crossing_location remains open
upstream terminal delta: candidate Lane-T PR #1161 extension
delta-star movement:     none
compute:                 exact local arithmetic only; no Modal spend
next route action:       derive a source/Pade genus upper bound below the
                         floor, or retire genus as a closure route
```
