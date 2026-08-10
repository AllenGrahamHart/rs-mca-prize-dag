# Clean-endpoint linear unit-resultant gate

- **status:** PROVED
- **closure:** exact norm and local-intersection calculation
- **consumer:** `rate_half_band_crossing_location`

Retain the two-sided clean weld

```text
W B-(X-x_0)=Q K,       deg_z B<=m-1.                 (LUR1)
```

Work over the algebraic closure and choose the affine parameter coordinate
so that all supported slopes and the root of the linear norm defect `S` are
finite, while

```text
q_inf(X)=[z^m]Q(z;X),
deg_X q_inf=rho,       q_inf(x_0)!=0.                 (LUR2)
```

Let `b=deg_z B` and `w=deg_z W` be the actual degrees. With the standard
first-polynomial-leading resultant convention,

```text
Res_z(Q,W) Res_z(Q,B)
  =q_inf(X)^(w+b) (X-x_0)^m.                         (LUR3)
```

Let

```text
A_0(z)=product_(gamma in Z:Q(gamma;x_0)=0)(z-gamma),
deg A_0=m-1.
```

The exceptional fibre factors exactly as

```text
Q(z;x_0)=c A_0(z)S(z),       c!=0.                   (LUR4)
```

Moreover the two resultants split the entire finite exceptional order:

```text
ord_(X-x_0) Res_z(Q,B)=1,
ord_(X-x_0) Res_z(Q,W)=m-1.                          (LUR5)
```

Equivalently, there are nonzero constants `c_B,c_W` and polynomials
`J_B,J_W` with

```text
Res_z(Q,B)=c_B (X-x_0)J_B,
Res_z(Q,W)=c_W (X-x_0)^(m-1)J_W,
c_B c_W=1,       J_B J_W=q_inf^(w+b).                (LUR6)
```

Neither weld factor is parameter-independent. In fact

```text
1<=b<=m-1,       1<=w<=T.                            (LUR7)
```

The weld quotient is also nonzero, and its actual parameter degree is

```text
deg_z K=w+b-m>=0.                                    (LUR8)
```

Thus after localizing away from the single parameter-infinity fibre
`q_inf=0`, the norm of the nonzero element `B`, whose parameter degree is
strictly below `deg_z Q`, has exactly one simple zero, at `X=x_0`. The norm
of `W` pays the other `m-1` points of that fibre.

## Scope

This is an exact gate, not its exclusion. A general irreducible curve can
carry such a unit equation. The remaining theorem must use the maximal
separation rank and Hankel/apolar origin to rule out the printed linear
unit-resultant profile, or classify its `q_inf`-boundary allocation.
