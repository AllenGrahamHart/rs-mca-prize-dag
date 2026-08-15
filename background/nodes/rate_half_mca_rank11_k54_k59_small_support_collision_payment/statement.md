# Small-support collision payment closes K'=54..59

- **status:** PROVED
- **closed residual rows:** `K'=54..59`
- **new closed component prefix:** `K'=10..59`

Refine the completion maxima at supports `2,3,4,5` to every exact defect,
apply the same-source collision charge at each support, retain the joint
support-four charge when `s_4+s_5<q`, and retain every support-`6..9`
terminal/fallback branch.

On every row `K'=54..60`, Pareto compression leaves one maximal vector from
the support-`2,3` group, one from the support-`4,5` group, and seven from the
support-`6..9` group.  The active branch is

```text
s_2=s_3=s_4=s_5=floor(q/2),
c6F/c7F/c8F/c9F.
```

Every row `K'=54..59` is safe.  The smallest positive gap is at `K'=59`:

```text
2662571195028360324230500777441238424043251068116179184680206.
```

The same payment first fails at `K'=60`, where complete capacity exceeds
demand by

```text
3672733965923291717387950853821894967875078243379846951201638.
```

## Falsifier

A missing exact defect; a collision cap used at support at least six; a
discarded non-dominated vector; a nonpositive gap on `54..59`; or closure
of `K'=60` by this payment.
