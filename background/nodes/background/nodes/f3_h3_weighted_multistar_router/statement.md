# H3 weighted low-distance multistar router

- **status:** PROVED
- **closure:** proof
- **consumer:** `f3_h3_mobius_excess_half`
- **dependencies:** `f3_h3_rich_fiber_norm_cutoff`,
  `f3_h3_rich_fiber_ideal_batching`,
  `f3_h3_distance_two_collision_2primary_exclusion`

Use the seven squared-norm-at-most-three coefficient vectors selected from a
cutoff-18 rich product fiber. Give an edge squared-distance weight

```text
w(E,F)=2 if ||v_E-v_F||^2=4,
         1 if ||v_E-v_F||^2=6,
         0 otherwise.
```

There is a center `E` and a set of `2<=r<=4` distinct leaves
`F_1,...,F_r` such that

```text
sum_i w(E,F_i)>=4.                                  (WMS1)
```

Put `O=Z[zeta_n]`, `pi=1-zeta_n`, and define the normalized multistar ideal

```text
K_(E;F_1,...,F_r)
  =((beta_(F_i)-beta_E)/pi^2 : 1<=i<=r) subset O.   (WMS2)
```

For the row prime `p`,

```text
p divides N(K_(E;F_1,...,F_r)),                     (WMS3)
```

and this ideal norm divides every normalized principal collision norm in the
multistar. Thus the candidate union from `(WMS1)` is contained in the proved
two-leaf ideal-star candidate union.

The exact fixed-root sieve is also weighted. For `p=1 mod n` and one fixed
primitive `n`th root `g mod p`, the prime belongs to the weighted-multistar
candidate union if and only if one shifted-product fiber at `g` contains a
vertex of incident weight at least four. No ideal normal form or enumeration
of primes above `p` is needed once a complete principal candidate list is
available.

This theorem strengthens candidate screening. It does not generate the
official-order principal-prime list, bound the number of survivors, or prove
C36' at a surviving prime.
