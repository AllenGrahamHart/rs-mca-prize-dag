# `A=1` core-one distance-three pair-Lagrange normal form

- **status:** PROVED
- **closure:** proof
- **consumer:** `rate_half_band_closure`
- **dependency:**
  `rate_half_ca_hankel_a1_core_one_exceptional_only_distance_three_mds_escape_router`

Retain the quotient-distance-three chart. Let the `e` internal slopes be
`xi_1,...,xi_e`, and let their cancelled pairs partition the roots of `A`:

```text
D_i(X)=(X-a_i)(X-b_i),
R_A=disjoint_union_(i=1)^e {a_i,b_i}.                 (PLN1)
```

Write `B(X)=product_(t in T)(X-t)`. Normalize the residual generator by
`Q(0;X)=A(X)`. For each internal slope there is a unique nonzero scalar
`lambda_i` such that

```text
Q(xi_i;X)=lambda_i B(X)A(X)/D_i(X).                  (PLN2)
```

Define

```text
Phi(z)=product_i(z-xi_i)/product_i(-xi_i),
L_i(z)=product_(j!=i)(z-xi_j)/(xi_i-xi_j).           (PLN3)
```

Then the entire residual generator is forced by the pair-Lagrange formula

```text
Q(z;X)=Phi(z)A(X)
       +z B(X) sum_(i=1)^e
          (lambda_i/xi_i)L_i(z) A(X)/D_i(X).         (PLN4)
```

In particular,

```text
Q(z;t)=Phi(z)A(t)                         (t in T),
Q(z;a)=c_a z L_i(z)                      (a in {a_i,b_i}), (PLN5)
```

where every `c_a` is nonzero. Thus each exceptional root occurs at the
exceptional slope and at all internal slopes except the one that cancels its
pair, while each triple point occurs at every internal slope and at no other
root of its parameter form.

The expression in `(PLN4)` is a minimal separated expansion of rank `e+1`.
Both polynomial families

```text
{A, B A/D_1,...,B A/D_e},
{Phi, zL_1,...,zL_e}                                  (PLN6)
```

are linearly independent.

Consequently a distance-three census must not allocate arbitrary
coefficients for `Q`. Its remaining data are the unordered root-pair
partition, the distinct nonzero internal slopes, and the `e` nonzero fiber
scalars. The open condition is that exactly `3e` other slopes make `(PLN4)`
split over `D_res\(R_A union T)` with the previously proved incidence
ledger and all lower Hankel and reciprocal constraints.
