# Proof

The general middle-adjugate theorem identifies `D_1` with the determinant
of the size-`e-2` regular Kronecker block. At a projective parameter
`gamma`, if its residual rank loss is `c_gamma`, local Smith form gives

```text
c_gamma<=ord_gamma(D_1).                              (1)
```

At `u=4`, zero omission and exact excess accounting give

```text
C_tot=sum_gamma c_gamma=e-6.                         (2)
```

Every excess root is simple and new relative to the specialized minimal
locator, and there is no excess degree away from the named heavy rows.

In the double-root arm, precisely the `e-6` roots of `g_*` carry rank loss
one. Equation `(1)` therefore gives `g_*|D_1`. Since

```text
deg D_1-deg g_*=(e-2)-(e-6)=4,                       (3)
```

the quotient is a nonzero binary quartic, proving `(RQP2)`.

In the two-simple arm, a slope carries rank loss

```text
c_gamma=1_(G_1(gamma)=0)+1_(G_2(gamma)=0).           (4)
```

Thus `(1)` gives `G_1G_2|D_1`, including exponent two at every common root.
The product degree is

```text
(e-3)/2+(e-9)/2=e-6,                                 (5)
```

so its quotient is again a nonzero quartic. This proves `(RQP4)`.

Finally the marked determinant identity is

```text
det(M_1+tau nu(x)nu(x)^T)=tau D_1Q(U,V;x)^2.         (6)
```

Substitute `(RQP2)` and `Q(-;x_*)=c g_*S_B^3` into
`(6)` to obtain `(RQP3)`. Substitute `(RQP4)` and the two factorizations
`Q(-;x_i)=c_iG_i^2S_i^3` to obtain `(RQP5)`. QED.
