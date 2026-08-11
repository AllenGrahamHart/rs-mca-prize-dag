# Cycle 152: rate-half `A=1` extremal regular-quartic eliminant (2026-08-11)

Taking the `X`-resultant of the Cycle-151 Pade syzygy cancels the complete
leading-coefficient power and gives

```text
Lambda^d Res_X(Q,G)=c D_1 Res_X(Q,L_U0).
```

The exact source-row and rank-loss factorizations cancel every center-line
factor and combine every off-line padding factor with its row incidences:

```text
Res_X(Q,G)
 =c E_4 product_(delta off line)ell_delta^(n-a_delta).
```

Thus the parameter pushforward of the residual four-cycle is exactly
`div(E_4)`: twice the quadratic correction in the double-root arm, or the
degree-one plus degree-three corrections in the two-simple arm. The next
attack is local: test whether the resulting order-eight/order-seven marked
Hankel jets can occur in a symmetric affine Hankel pencil with the retained
source recurrence.

```text
result:                  PROVED exact regular-quartic eliminant
DAG delta:               +1 PROVED leaf
critical status delta:   none
compute:                 integer degree/tamper checks only
new assumptions:         none
```
