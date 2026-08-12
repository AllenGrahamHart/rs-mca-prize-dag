# `A=1` quadratic nonreduced normalization/collision dichotomy

- **status:** PROVED
- **closure:** exact order-four close or order-two quotient-root collision
- **consumer:** `rate_half_band_crossing_location`

Retain an unshared nonreduced correction

```text
S_B=c_S ell_tau^2,       g_*(tau)!=0,       z=ell_tau. (NCD1)
```

Write the degree-two correction divisor over `tau` on the normalization as

```text
B=sum_b m_b b,       sum_b m_b=2,                   (NCD2)
```

and let `e_b=ord_b(z)` be the parameter ramification index. If

```text
s=ord_tau F_0,
```

then every `b` in `(NCD2)` obeys the exact valuation identity

```text
e_b s=2m_b.                                        (NCD3)
```

Consequently exactly one of the following occurs.

```text
smooth doubled point:
  B=2b,       e_b=1,       s=4;
  kappa_2=kappa_3=0,
  Smith=[4],
  x_* is a simple root of Q(tau,X);

collision:
  s=2,       kappa_2!=0,
  sum_b e_b=2,
  ord_(X=x_*) Q(tau,X)=2.                          (NCD4)
```

The collision alternative consists either of `B=2b` with `e_b=2`, or of
`B=b_1+b_2` with two distinct normalization branches and
`e_(b_1)=e_(b_2)=1`.

In particular, no unshared nonreduced packet has

```text
kappa_2=0,       kappa_3!=0.                       (NCD5)
```

Every nonzero-jet survivor therefore carries a nonzero second jet and an
exact double quotient-root collision. The three noncollision profiles of
the higher-corank Smith router are empty in the geometric packet.

## Scope

The theorem does not exclude the exact collision in `(NCD4)` and does not
classify its regular Smith partition. All four higher-corank partitions of
determinant order four remain abstractly possible there because
`U_tau(x_*)=0` removes the self-pairing evaluation used by the noncollision
router. Shared nonreduced roots are not covered.
