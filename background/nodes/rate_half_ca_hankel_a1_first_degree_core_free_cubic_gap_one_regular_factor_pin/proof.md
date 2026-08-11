# Proof

The marked-Hankel theorem identifies `D_0`, up to a nonzero scalar, with
the determinant of the size-`Delta` regular Kronecker block of the
contracted core-free pencil, where

```text
Delta=rho-e=2e-1.                                   (1)
```

Fix a projective parameter slope `gamma` and work over its local DVR. The
singular Kronecker block has constant rank. The residual rank loss is
therefore the number of positive Smith exponents of the regular block. By
the specialized recurrence factorization, this loss is

```text
c_gamma=deg R_gamma.                                (2)
```

If the positive Smith exponents are `b_1,...,b_c_gamma`, each is at least
one, and hence

```text
c_gamma<=sum_i b_i=ord_gamma(D_0).                   (3)
```

Equation `(3)` at every supported slope proves the homogeneous divisibility

```text
P_C | D_0.                                           (4)
```

The packet normal-form theorem defines

```text
C_tot=sum_gamma c_gamma=Delta-w.                     (5)
```

Consequently the quotient in `(4)` is a nonzero homogeneous form of degree

```text
deg D_0-deg P_C=Delta-C_tot=w.                       (6)
```

This proves `(CRF3)`. The four values of `w` in `(DGN2)` are respectively
`1,0,0,0`, which gives `(CRF4)`. Finally the cofactor identity `(MHD3)` is

```text
det M_0[x]=D_0Q(U,V;x).
```

Substitution of `(CRF3)` proves `(CRF5)`. QED.
