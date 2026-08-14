# Cycle 313: MCA rank-11 correction ten-flat collapse (2026-08-14)

The new PROVED node
`rate_half_mca_rank11_relative_correction_tenflat_collapse` removes Cycle
312's generic dimension-at-least-12 branch.

Every residual explanation has the form

```text
h_gamma'=a_0'+gamma b_0'+d_gamma',
d_gamma' in V',       dim V'=10.
```

The fixed core interpolant satisfies

```text
D_H(X,Z)=H(X,Z)-a_0'(X)-Zb_0'(X),
```

and every coefficient of `D_H` is a linear combination of the 32 anchor
deviations. Hence `D_H` is coefficientwise `V'`-valued. For every selected
slope,

```text
P_gamma=h_gamma'-H(X,gamma)=d_gamma'-D_H(X,gamma) in V'.
```

Thus the complete correction span `W` has dimension at most 10. Dimension
zero is core-compatible and dimension one is one projective ray, so the
previous payment forces `dim W>=2` in an unsafe family. Proper spaces are
paid through dimension 11, hence every survivor is a positive-dimensional
rank-flat or polynomial clone component.

Every survivor also absorbs the high coefficients `H_j`, `j>=2`:

- for `dim W<=9`, this is the clone-tolerant contrapositive;
- for `dim W=10`, the inclusion `W<=V'` is equality.

The exact live shape is therefore

```text
2 <= dim W <= 10,
positive-dimensional rank-flat or polynomial clone,
all high slope coefficients contained in W.
```

Focused verification:

```text
RATE_HALF_MCA_RANK11_RELATIVE_CORRECTION_TENFLAT_COLLAPSE_PASS
  dimension=2..10 routes=2 controls=6/6
RATE_HALF_MCA_RANK11_RELATIVE_CORRECTION_TENFLAT_COLLAPSE_AUDIT_PASS
  dimension=2..10 routes=2 controls=5/5
```

No numerical experiment or Modal computation was used.

```text
start:                   ab6aeb87d
DAG delta:               +1 PROVED ten-flat collapse,
                         +3 requirement edges, +1 evidence edge
critical status delta:   none
upstream terminal delta: H_C has one typed component residual only
delta-star movement:     none
compute:                 finite-dimensional exact linear algebra only
next route action:       classify high-core-absorbing rank-flat/clone
                         components in dimensions 2..10
```
