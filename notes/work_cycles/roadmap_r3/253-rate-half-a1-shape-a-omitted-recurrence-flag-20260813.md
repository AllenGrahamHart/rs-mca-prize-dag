# Cycle 253: rate-half shape-A omitted-recurrence flag (2026-08-13)

After retiring the automatic residual-section route, the concentrated excess
norm was coupled directly to the source moments.

Write

```text
Q(t,X)=sum_(i=0)^d q_i(t)X^i,
h_j(t)=sum_x omega_x(t)x^j,
R_j(t)=sum_(i=0)^d q_i(t)h_(i+j)(t).
```

The dual-MDS construction gives `H_x=G(t,x)/L_U0'(x)` and
`sum_x H_xx^j=0` through `j=d`. Lagrange coefficient extraction is
unitriangular after this forced zero range. Since `R-d-2=n`, the top
coefficients of `G` are controlled successively by

```text
R_(d+1),R_(d+2),...
```

after division by the nonzero off-line factor `Lambda`. Therefore each
fiber degree drop

```text
q_delta=n-deg_X G(delta,X)
```

is exactly the length of the initial omitted-recurrence zero run at `delta`.
If `H_off` cuts out the `3e` off-line slopes and

```text
C_r=gcd(H_off,R_(d+1),...,R_(d+1+r)),
```

then squarefreeness and the layer-cake identity give

```text
sum_delta q_delta=sum_(r=0)^(n-1)deg C_r,
deg T=e-sum_(r=0)^(n-1)deg C_r.
```

The primary verifier checks official index arithmetic and a finite-field
interpolation fixture with degree drops `2,1,0`; the independent audit uses
a separate nested-count profile.

```text
start:                   900db8b15
canonical prize:         fdfb20a42 (clean; unchanged)
result:                  PROVED omitted-recurrence/norm flag identity
DAG delta:               +1 PROVED node, +3 req edges, +1 ev edge
critical status delta:   none; rate_half_band_crossing_location remains open
new exact frontier:      bound/classify the nested gcd flag C_r
compute:                 two constant-size exact local audits; no Modal spend
next route action:       couple C_r to the unique scalar weld and collision jets
```
