# `A=1` quadratic gap-four Pade-Bezout contact-module presentation

- **status:** PROVED
- **closure:** complete local Smith refinement of the Pade resultant
- **consumer:** nonreduced exact-collision Smith router

Retain the contracted Pade notation and let `tau` be a finite parameter
value at which the leading `X`-coefficient of the degree-`d` locator `Q`
is a unit. Put

```text
K_Q(X,Z)=[Q(X)-Q(Z)]/(X-Z),
P_F(X)=Phi(K_Q(X,Z)),
H=(Phi(X^(i+j)))_(0<=i,j<d).                       (BCM1)
```

Use the Bezoutian convention

```text
Bez_(Q,P_F)(X,Y)
 =[Q(X)P_F(Y)-P_F(X)Q(Y)]/(X-Y).                  (BCM2)
```

If `T_Q` is the coefficient matrix of `K_Q(X,Z)` in the monomial bases,
then

```text
Bez_(Q,P_F)=T_Q H T_Q^T,
det T_Q=+-lc_X(Q)^d.                              (BCM3)
```

The regular quotient of the full Hankel matrix is congruent to `H`.
Consequently it has the same complete local Smith invariants as the
Bezoutian, not merely the same determinant.

Let

```text
A_tau=O_tau[X]/(Q).
```

Euclidean reduction identifies the Bezoutian cokernel with the Pade
contact algebra:

```text
coker Bez_(Q,P_F)  isomorphic to  A_tau/P_F A_tau. (BCM4)
```

Thus the regular Hankel Smith factors at every finite degree-preserving
fiber are the invariant factors of the local intersection module of
`Q=0` and `P_F=0`.

## Scope

The presentation is local where `lc_X(Q)` is a unit. Degree-drop and
parameter-infinity fibers require a separate chart. The theorem does not
infer Smith factors from the contact-divisor length alone; it supplies the
module whose invariant factors must be computed.
