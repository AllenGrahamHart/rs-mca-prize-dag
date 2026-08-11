# Cycle 151: rate-half `A=1` quadratic Pade regular factor (2026-08-11)

The contracted source moments define a canonical second-kind numerator
`P_F`. Lagrange interpolation of the split biform gives

```text
QB-Lambda G=L_U0 P_F.
```

The moment Vandermonde factorization and
`adj M_1=D_1qq^T` then give the exact formal resultant

```text
Res_X(Q,P_F)=c a^(2d+1)D_1.
```

After removing the fixed domain-infinity frame, `D_1` is the parameter norm
of the Forney-contact section. The already proved contact divisors therefore
identify the regular quartic:

```text
double root: E_4 proportional to S_B^2,
two simple:  E_4 proportional to S_1S_2.
```

This is an identity, not yet an exclusion.

```text
result:                  PROVED Pade regular-factor identity
DAG delta:               +1 PROVED leaf
compute:                 integer degree/tamper checks only
new assumptions:         none
```
