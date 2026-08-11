# Proof

The split-pencil equivalence writes every syndrome sequence as

```text
y_k=sum_(x in D)a_xv_xx^k,                            (1)
```

where the dual multipliers `v_x` are nonzero. Contracting the divided-power
form by the fixed apolar factor `X-s_0` replaces the moment sequence by

```text
h_k=y_(k+1)-s_0y_k.                                   (2)
```

Substitute `(1)` into `(2)`:

```text
h_k=sum_(x in D)(x-s_0)a_xv_xx^k
   =sum_(x in D_res)(x-s_0)a_xv_xx^k.                 (3)
```

The omitted `x=s_0` term is zero. For every `x in D_res`, both `x-s_0` and
`v_x` are nonzero. Thus multiplication by their product is an invertible
diagonal map, proving `(SWS3)--(SWS4)`.

It remains to check moment surjectivity. The matrix of `(SWS6)` is the
`(2d+1) x |D_res|` Vandermonde evaluation matrix

```text
V=(x^k)_(0<=k<=2d, x in D_res).                       (4)
```

Choose any `2d+1` points of `D_res`. The corresponding square minor is an
ordinary Vandermonde determinant, nonzero because the evaluation points are
distinct. Hence `V` has full row rank and `(SWS6)` is onto.

For the official core-one profile, `N=4rho` and `d=rho-1`, so

```text
|D_res|=4rho-1>=2rho-1=2d+1.                          (5)
```

Every vector of `2d+1` moments therefore has a source representation. Those
moments are exactly the anti-diagonal data of one symmetric Hankel matrix of
size `d+1`; applying the argument separately to two endpoint vectors proves
the pair assertion.

The construction uses arbitrary word values and does not preserve the
additional column-farness or split-incidence requirements. Consequently it
proves only the printed route fence, not existence of a retained packet.
QED.
