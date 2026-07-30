# KoalaBear decomposition source-pencil compiler

- **status:** PROVED
- **scope:** residual actual KoalaBear `Q=6,s=6,u=2` decomposition branch
- **upstream:** PR `#1130`, head `a14a05d9ba80068133e93e2fa77d6d1dc8828829`
- **dependencies:** `rate_half_kb_degree60_decomposition_divisor_adapter`,
  `rate_half_kb_degree5_decomposition_exclusion`
- **consumer:** `rate_half_band_closure`

For an inner degree `m`, every geometric decomposition of
`f=V_act/A^5` is equivalent to a coprime binary pencil

```text
W=<H_0,H_1> subset H^0(P^1,O(m))
```

containing each complete source locator and the fifth power of every
exceptional source locator, with

```text
V_act in Sym^(60/m)(W).                              (KBSP-1)
```

Two distinct complete active fibers descend a target transform of the inner
map to `K=F_(2130706433^6)`; the corresponding outer map is also defined
over `K`.

The exact row consequences are:

1. inner degree `30` factors through a degree-six inner map and is not a
   separate producer;
2. inner degree `12` has one canonical candidate pencil
   `W_12=<A,N_0>`, where `N_0^5=V_act mod A`, and survives exactly the
   six-dimensional membership test
   `V_act in span{A^5,A^4N_0,...,N_0^5}`;
3. at inner degree `2`, the unique deck involution belongs to `PGL_2(K)`;
4. conditional on a separate same-record bridge to a prime-field projective
   action preserving the order-`2^21` carrier, that action is `x->kappa x`
   or `x->kappa/x`; complete involution fibers are the power-pair and
   fixed-point-free reciprocal-pair cases.

Together with the degree-five deletion, the six live degree rows are

```text
{2,3,4,6,10,12}.
```

The endpoint parameter line is not the evaluation carrier. The conditional
carrier classification supplies no parameter-to-carrier bridge, witness-data
descent, owner, charge, cap `68`, `u=2` close, adjacent certificate, or row
close. Ledger movement is zero.

## Falsifier

A decomposition that has no pencil `(KBSP-1)`, failure of challenge-field
descent from two rational active fibers, a degree-30 row not factoring
through degree six, a second degree-12 candidate pencil, or a prime-field
projectivity outside the two printed forms that stabilizes the carrier.
