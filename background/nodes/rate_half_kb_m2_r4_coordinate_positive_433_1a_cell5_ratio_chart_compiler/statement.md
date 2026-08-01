# KoalaBear m2 r4 positive 433-1a cell-5 ratio-chart compiler

- **status:** PROVED
- **scope:** deployed-field cell `5`, root signs `(-1,-1)`, common pivot chart
  `C1` with minors `12,13,14`
- **dependencies:**
  `rate_half_kb_m2_r4_coordinate_positive_433_1a_common_vieta_pivot_chart_reduction`,
  `rate_half_kb_m2_r4_coordinate_positive_433_1a_product_base_rank_global_certificate`
- **consumer:** `rate_half_band_closure`

Work over the official field `F_2130706433` with
`iota=16711679`, `iota^2=-1`.  Cell `5` has common labels

```text
1, t^2, r^2, -r^2, -1.                           (KBRAT-1)
```

Atomically localize the three `C1` minors at the declared common and target
guards.  The first fast-stripped minor has one further unit factor `t-r`;
the other two have none.  The resulting generators have

```text
degrees: 10,10,11          terms: 28,40,40.       (KBRAT-2)
```

Because `b,c` are nonzero, set `x=c/b` and divide every substituted
generator by the unit `b^2`.  The three equations become

```text
L0=a0(x,r,t)+a1(x,r,t)b,
L1=q10+q11 b+q12 b^2,
L2=q20+q21 b+q22 b^2.                             (KBRAT-3)
```

Their exact coefficient term counts are

```text
L0: 14,14       L1: 10,20,10       L2: 10,20,10. (KBRAT-4)
```

On `a1!=0`, reconstruct `b=-a0/a1`.  The chart is then exactly equivalent
to the two cleared equations

```text
Ej=qj0 a1^2-qj1 a0 a1+qj2 a0^2=0,  j=1,2,        (KBRAT-5)
```

of total degrees `24,25` and term counts `244,340`.  The complementary
denominator branch is retained exactly as `a0=a1=0` together with `L1=L2=0`.

This theorem is a common-source chart reduction only.  It does not close the
exceptional branch, impose any outside equation or unsquared `q` sign, delete
cell `5` or `433-1a -> O0b`, close K3, or prove either Prize result.

## Falsifier

An admissible deployed-field cell-5 point lost by `x=c/b`, an additional
nonunit factor division, a chart solution with `a1!=0` not represented by
`(KBRAT-5)`, or a solution on `a1=0` omitted by the printed exceptional
branch.
