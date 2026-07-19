# H3 double-accident nonzero-coupling ideal router

- **status:** PROVED
- **closure:** proof
- **consumer:** `f3_h3_mobius_excess_half`
- **dependencies:**
  `f3_h3_double_accident_low_distance_joint_ideal_router`,
  `f3_h3_shifted_product_sidon`

Let `n=2^s`, `s>=3`, put `O=Z[zeta_n]` and `pi=1-zeta_n`, and retain the
rooted product star `(E;F,G)` and normalized product generators

```text
alpha_F=(beta_F-beta_E)/pi^2,
alpha_G=(beta_G-beta_E)/pi^2.                     (NZC1)
```

For an ordered nonidentity quotient lift `Q=(u,v)`, put

```text
C_Q=1-zeta_n^u,       D_Q=1-zeta_n^v,
lambda_(E,Q)=(beta_E C_Q-D_Q)/pi.                 (NZC2)
```

## Exact zero locus

The coupling generator vanishes exactly on the binary telescoping family.
Writing `E={x,y}` in roots and `Q=(z,w)`, one has

```text
lambda_(E,Q)=0
  iff {x,y,z}={q,-q,-q^2} and w=q^4              (NZC3)
```

for some `q in mu_n` of order at least eight. There are exactly

```text
3(n-4)/2                                             (NZC4)
```

zero-coupling pairs `(E,Q)`, with `E` unordered and `Q` ordered. Thus the
zero test is an explicit exponent-pattern test, not a cyclotomic norm
calculation.

## Nonzero selection and batching

Fix an official row, a target `t!=1`, and one lifted product representation
`E` reducing to `t`. Among the `R(t)` distinct ordered quotient lifts reducing
to `t`, at most one has `lambda_(E,Q)=0`. Hence

```text
#{Q in Q_t:lambda_(E,Q)!=0} >= R(t)-1.             (NZC5)
```

If `P(t)>=19`, choose the rooted low-distance star supplied by the proved
ideal-star router and define the target-local batched ideal

```text
K_t^NZ=(alpha_F,alpha_G,
        lambda_(E,Q):Q in Q_t, lambda_(E,Q)!=0).   (NZC6)
```

When `R(t)>=2`, this is a nonempty coupling batch and

```text
p divides N(K_t^NZ)
  divides gcd(|Norm(alpha_F)|,|Norm(alpha_G)|,
              |Norm(lambda_(E,Q))|:lambda_(E,Q)!=0)
  <=6^(n/4)/4.                                     (NZC7)
```

For a computation-free finite outer gate, let `D_n^NZ` be the set of odd
prime divisors of

```text
N((alpha_F,alpha_G,lambda_(E,Q)))                  (NZC8)
```

over all rooted stars satisfying `(ISR2)` and all nonidentity quotient lifts
with nonzero `lambda_(E,Q)`. Then

```text
Y_18>0  =>  p in D_n^NZ.                            (NZC9)
```

Every official row prime outside `D_n^NZ` has `Y_18=0` and therefore satisfies
C36' by the proved cutoff-18 double-accident reduction.

This removes the second quotient lift from coarse candidate-template
generation: its existence proves that a nonzero anchor can be selected. The
full batch `(NZC6)` remains available for the exact survivor sieve and gains
at least `R(t)-1` nonzero coupling generators. This theorem does not construct
the official-order candidate set, factor its norms, or bound survivors.
