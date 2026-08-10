# Proof

At every live missing-`CF` point, reconstruct the six common product-kernel
coefficients from the five-by-six cofactor matrix. Evaluation at the missing
source label `-r^4` reproduces the certified source product `c*f`, so the
recovered value of `f` is pinned independently of the residual solver.

For coefficient triples `A=(a0,a1,a2)` and `B=(b0,b1,b2)`, define

```text
p_i(x) = b_i-x a_i,
q(y)   = (b0-y a0, -b1+y a1, b2-y a2),
P(x,y) = (p2 q0-p0 q2)^2-(p2 q1-p1 q2)(p1 q0-p0 q1).
```

The six residual target records are

```text
BE=b e, DE+=d e, DE-=-d e,
DF+=d f, DF-=-d f, EF=sigma_o e f.
```

Each matching therefore gives three explicit bivariate equations `P(x,y)=0`.
For every one of the 480 systems, the certificate selects two equations and
their nonzero resultant in `d`. The resultant degrees are 8, 12, or 16.
Exact `gcd(R,d^p-d)` gives 432 projected roots in total, with per-system root
profile `160:0`, `208:1`, `112:2`. At every projected root, the gcd of all
three specialized equations in `e` is exactly one. Thus no system has an
`F_p` point.

The primary verifier independently reconstructs the kernel and equations,
checks every selected resultant up to its nonzero scalar by 33 evaluations
(the resultant degree bound is 32), proves the projected root lists complete
using `gcd(R,d^p-d)`, and replays all 432 unit fiber gcds. The 120-system and
transport conclusions follow. QED.
