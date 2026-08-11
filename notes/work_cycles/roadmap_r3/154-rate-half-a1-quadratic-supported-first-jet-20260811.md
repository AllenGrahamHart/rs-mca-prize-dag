# Cycle 154: rate-half `A=1` quadratic supported first jet (2026-08-11)

The exact correction factorization separates ordinary supported rank loss
from the correction divisor. At a supported slope `gamma` away from that
divisor,

```text
ord_gamma(D_1)=c_gamma.
```

The contracted source has `d-c_gamma` distinct nonzero sources, so the
specialized symmetric Hankel kernel is

```text
Q_min F[X]_(<=c_gamma).
```

Local Smith form now forces all `c_gamma` positive exponents to equal one.
The derivative moment form is a perfect symmetric pairing modulo the actual
excess locator:

```text
B_gamma(A,B)=dot Phi(Q_min^2AB),
rank B_gamma=c_gamma,
rad B_gamma=span{R_gamma}.
```

Only the correction divisor is left out: at most two projective slopes in
the double-root arm and at most four in the two-simple arm. This does not
exclude either packet, but it proves that all extensive supported rank-loss
mass is first-order transverse. Any higher-order obstruction is confined to
the same constant-size correction locus already identified by the exact
four-core.

```text
result:                  PROVED supported first-jet perfect pairing
DAG delta:               +1 PROVED leaf
critical status delta:   none
compute:                 integer dimension/tamper checks only
new assumptions:         none
```
