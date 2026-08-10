# Clean-endpoint resultant boundary saturation

- **status:** PROVED
- **closure:** leading-coefficient Bezout and exact resultant degree
- **consumer:** `rate_half_band_crossing_location`

Retain the clean linear unit-resultant gate in an affine parameter coordinate
with all supported slopes finite. Write

```text
q_inf(X)=[z^m]Q,       b=deg_z B,
P(X)=(X^N-1)/(X-x_0),
rho=4m-1,       N=16m,       T=4m+1.                (RBS1)
```

Then the parameter degrees and the top domain-complement coefficients are
exact:

```text
deg_z W=T,       deg_z V=3m+1,
q_inf nu+P omega=1,                                  (RBS2)

nu=[z^(3m+1)]V,       omega=[z^T]W.                  (RBS3)
```

In particular `gcd(q_inf,P)=gcd(q_inf,omega)=1`. If

```text
beta=[z^b]B,
kappa=[z^(T+b-m)]K,
```

then the top weld coefficient satisfies

```text
omega beta=q_inf kappa,       q_inf divides beta.    (RBS4)
```

The resultant allocation from the preceding gate is therefore exact, not
merely supported on `q_inf`:

```text
Res_z(Q,W)=c_W (X-x_0)^(m-1),
Res_z(Q,B)=c_B q_inf(X)^(T+b)(X-x_0),
c_B c_W=1.                                           (RBS5)
```

Finally the former upper bound on the dual-complement `X`-degree is sharp:

```text
deg_X B=N=16m.                                       (RBS6)
```

Thus every one of the `rho` points of the parameter-infinity fibre is
assigned to `B`, while `W` is a unit there. The boundary-free shortcut
`J_B=1` is impossible; all of `q_inf^(T+b)` is load-bearing.

## Scope

This saturates the boundary and degree ledgers but does not exclude them.
The remaining clean theorem must combine `(RBS2)--(RBS6)` with the
Hankel/apolar coefficient structure. No claim is made that `b=m-1` or that
the saturated dual complement factors in the ambient polynomial ring.
