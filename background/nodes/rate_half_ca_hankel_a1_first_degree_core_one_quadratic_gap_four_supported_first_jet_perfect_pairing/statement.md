# `A=1` quadratic gap-four supported first-jet perfect pairing

- **status:** PROVED
- **closure:** exact symmetric local Smith transversality off the correction divisor
- **consumer:** `rate_half_band_crossing_location`

Retain either root arm of the core-one quadratic `u=4` packet. Put

```text
d=rho-1,
M(z)=M_0+zM_1,       size (d+1) x (d+1),
adj M=D_1 q q^T.                                      (QFJ1)
```

Let `gamma` be a supported slope with positive residual rank loss
`c=c_gamma`. Write

```text
Q_gamma=Q_min R_gamma,
deg Q_min=d-c,       deg R_gamma=c.                  (QFJ2)
```

In the double-root arm set `C_corr=S_B`. In the two-simple arm set
`C_corr=S_1S_2`. Assume

```text
C_corr(gamma)!=0.                                    (QFJ3)
```

Choose a local parameter `z` vanishing at `gamma`, and let `dot Phi` be
the derivative of the contracted moment functional. The specialized
Hankel kernel is

```text
ker M_gamma=Q_min F[X]_(<=c).                        (QFJ4)
```

On this `(c+1)`-dimensional space define the symmetric first-jet form

```text
B_gamma(A,B)=dot Phi(Q_min^2 A B),
deg A,deg B<=c.                                      (QFJ5)
```

Then

```text
rank B_gamma=c,
rad B_gamma=span{R_gamma}.                           (QFJ6)
```

Equivalently, `dot M` induces a perfect symmetric pairing on

```text
ker M_gamma / span{Q_gamma}.                         (QFJ7)
```

When `c=1` and `R_gamma=X-r_gamma` is monic, this includes the exact
moment identities

```text
dot Phi(Q_min^2(X-r_gamma))=0,
dot Phi(Q_min^2 X(X-r_gamma))=0,
dot Phi(Q_min^2)!=0.                                 (QFJ8)
```

The exception divisor has degree two in the double-root arm and degree
four in the two-simple arm. Thus the theorem holds at every supported
rank-loss slope except at most two projective slopes in the double-root
arm and at most four in the two-simple arm, counted without multiplicity.

## Scope

The theorem does not control a supported slope shared with the correction
divisor, where `ord_gamma(D_1)` can exceed `c_gamma`. It does not exclude
either root arm. Its conclusion uses the symmetric Hankel kernel and is
strictly stronger than a determinant-order statement, but it is only a
first-order local constraint.
