# Cycle 181: rate-half `A=1` nonreduced divided-row quintic (2026-08-12)

Substitution of the quadratic heavy-row residual into the Pade syzygy
forces the common divisor `g_*S_B` through every canonical divided-row
moment:

```text
M(t)u(t)=g_*(t)S_B(t)C(t),       deg C<=5,
C_(i+1)=x_*C_i-a_QS_B^2h_i.
```

The initial quotient is nonzero at the correction and the entire value
vector there is the geometric progression `x_*^iC_0(tau)`. Thus the
nonreduced arm is a six-coefficient quotient problem rather than a full
degree-`e+1` moment problem.

```text
result:                  PROVED nonreduced divided-row quintic quotient
DAG delta:               +1 PROVED leaf, 2 req edges, 1 evidence edge
critical status delta:   none
compute:                 23 exact recurrence checks; no Modal spend
new assumptions:         none
```

The next target is an incompatibility between this bounded quintic vector,
the unique scalar weld, and the two-directional split-factor trichotomy.
