# Proof

By `(CRF3)`, condition `(FJP1)` gives

```text
ord_gamma(D_0)=c_gamma=c.                           (1)
```

Work over the local DVR at `gamma`. The generic right kernel contributes
one identically zero Smith invariant. The specialized rank falls by `c`, so
exactly `c` of the remaining invariants have positive valuation. Their
valuation sum is `ord_gamma(D_0)=c`; hence every positive Smith exponent is
exactly one. The first derivative of the pencil therefore induces an
isomorphism from the `c` transverse right-kernel directions to the
`c`-dimensional left cokernel.                              (2)

We identify these spaces in apolar coordinates. The specialized moment
functional has socle degree `2rho-1` and minimal apolar generator `Q_min`
of degree `rho-c`. Its other complete-intersection generator has degree

```text
(2rho+1)-(rho-c)=rho+c+1.                           (3)
```

Thus no second generator occurs in degrees at most `rho`. The degree-`rho`
and degree-`rho-1` apolar pieces are precisely

```text
Q_min F[X]_(<=c),       Q_min F[X]_(<=c-1),         (4)
```

which proves `(FJP3)` and their dimensions `c+1,c`.

For coefficient vectors represented by polynomials `Q_min A` and
`Q_min B`, the derivative Hankel pairing is

```text
(Q_min A)^T dot M (Q_min B)
 =dot Phi(Q_min^2AB).                                (5)
```

This is `(FJP4)`. Differentiate the generic kernel identity

```text
M_0(z)Q(z)=0
```

at `z=0`. Since `Q(0)=Q_min R_gamma`, left multiplication by every
specialized left-kernel vector gives

```text
B_gamma(A,R_gamma)=0.                               (6)
```

Thus `R_gamma` lies in the right radical. The Smith calculation `(2)` says
that the induced derivative pairing has rank `c`. Since its right space has
dimension `c+1`, its radical has dimension one. Equation `(6)` therefore
proves `(FJP5)` and `(FJP6)`.

If `c=1`, the right space consists of linear polynomials and its radical is
the line spanned by the monic linear polynomial `X-r_gamma`. The constant
polynomial is not on that line, so `(FJP7)` follows.

Finally `(CRF4)` gives `w=0` in the last three packets, so `E_0=1` and
`(FJP1)` holds at every supported rank-loss slope. In the first packet,
`E_1` has one projective zero, which is the only possible exception. QED.
