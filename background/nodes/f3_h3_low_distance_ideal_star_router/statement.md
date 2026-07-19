# H3 low-distance two-generator ideal-star router

- **status:** PROVED
- **closure:** proof
- **consumer:** `f3_h3_mobius_excess_half`
- **dependencies:** `f3_h3_rich_fiber_norm_cutoff`,
  `f3_h3_rich_fiber_ideal_batching`,
  `f3_h3_distance_two_collision_2primary_exclusion`

Let `n=2^s` with `s>=2`, let `zeta=zeta_n`, put

```text
O=Z[zeta],       pi=1-zeta,
```

and use the unordered shifted-root pairs, products `beta_E`, and half-basis
vectors `v_E` from the rich-fiber norm-cutoff theorem. For distinct pairs
`E,F,G`, define the normalized two-generator ideal

```text
K_(E;F,G)=((beta_F-beta_E)/pi^2,
           (beta_G-beta_E)/pi^2) subset O.          (ISR1)
```

The displayed quotients are algebraic integers. Let `D_n` be the finite set
of odd prime divisors of `N(K_(E;F,G))` over all rooted stars satisfying

```text
||v_E||_2^2,||v_F||_2^2,||v_G||_2^2<=3,
||v_E-v_F||_2^2<=6,       ||v_E-v_G||_2^2<=6.       (ISR2)
```

If `p=1 mod n` and an order-`n` subgroup row has `P(t)>=19` for some nonzero
target, then

```text
p in D_n.                                             (ISR3)
```

More precisely, the rich fiber contains a rooted star `(E;F,G)` satisfying
`(ISR2)` for which

```text
p divides N(K_(E;F,G))
  divides gcd(|Norm((beta_F-beta_E)/pi^2)|,
              |Norm((beta_G-beta_E)/pi^2)|)
  <= 6^(n/4)/4.                                      (ISR4)
```

Consequently every official row prime outside `D_n` has empty cutoff-18 rich
locus, so `X_18=Y_18=0` and C36' holds on that row.

Odd Galois dilation, exchange inside any unordered root pair, and exchange of
the two leaves `F,G` preserve the star condition and ideal norm. One rooted
star representative from each such orbit is complete.

This is a strictly sharper finite fixed-order router than the single-norm
union. It does not bound the number of ideal stars, factor their norms, or
prove C36' at primes that survive the filter.

The selected seven small vectors have at least six distance-at-most-six edges:
distance two is 2-primary and therefore impossible in the common odd-prime
fiber. Only two incident edges are needed to define `(ISR1)`.
