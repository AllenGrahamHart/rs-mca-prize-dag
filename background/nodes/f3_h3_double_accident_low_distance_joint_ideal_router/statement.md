# H3 double-accident low-distance joint-ideal router

- **status:** PROVED
- **closure:** proof
- **consumer:** `f3_h3_mobius_excess_half`
- **dependencies:** `f3_h3_cutoff18_double_accident_reduction`,
  `f3_h3_low_distance_ideal_star_router`,
  `f3_h3_shifted_product_sidon`

Let `n=2^s`, `s>=2`, put `O=Z[zeta_n]` and `pi=1-zeta_n`, and use the
shifted products `beta_E` and half-basis vectors `v_E` from the low-distance
ideal-star router. For an ordered quotient lift

```text
Q_i=(u_i,v_i),       C_i=1-zeta_n^(u_i),
                     D_i=1-zeta_n^(v_i),            (DAJ1)
```

require `u_i,v_i` to be nonzero modulo `n`, `u_i!=v_i`, and `Q_0!=Q_1`.
For a rooted product star `(E;F,G)` satisfying `(ISR2)`, define

```text
alpha_F=(beta_F-beta_E)/pi^2,
alpha_G=(beta_G-beta_E)/pi^2,
theta=(D_1 C_0-D_0 C_1)/pi^2,
lambda=(beta_E C_0-D_0)/pi,                         (DAJ2)

K^DA_(E;F,G;Q_0,Q_1)=(alpha_F,alpha_G,theta,lambda)
                       subset O.                    (DAJ3)
```

All four elements in `(DAJ2)` are algebraic integers. The first two are
nonzero by shifted-product Sidonicity. The quotient element `theta` is also
nonzero: equality of the two characteristic-zero quotients would force
`Q_0=Q_1`, because both quotients are nonidentity. The coupling element
`lambda` may vanish when product/quotient equality already holds in
characteristic zero; the two nonzero product generators still make `K^DA` a
nonzero ideal.

Let `D_n^DA` be the finite set of odd prime divisors of the ideal norms in
`(DAJ3)`, over all rooted stars satisfying `(ISR2)` and all ordered quotient
lifts satisfying `(DAJ1)`. On a finite row put `A=(1-H)\{0}` and

```text
P(t)=#{(a,b) in A^2:ab=t},
R(t)=#{(c,d) in A^2:d/c=t}.
```

If `p=1 mod n` is prime and an order-`n` row over `F_p` has

```text
t!=1,       P(t)>=19,       R(t)>=2,                (DAJ4)
```

then one can choose the star and quotient lifts so that

```text
p divides N(K^DA_(E;F,G;Q_0,Q_1))
  divides gcd(|Norm(alpha_F)|,|Norm(alpha_G)|,
              |Norm(theta)|,|Norm(lambda)|)
  <= 6^(n/4)/4.                                    (DAJ5)
```

In particular,

```text
Y_18>0  =>  p in D_n^DA.                            (DAJ6)
```

Every official row prime outside `D_n^DA` therefore has `Y_18=0`, and the
proved cutoff-18 double-accident reduction gives the C36' target
`17X_18<=300n^2` on that row.

The generator `lambda` is load-bearing: the product star and the quotient
collision must reduce to the same target. Omitting it would only detect two
possibly unrelated accidents at one prime. The joint ideal is never a weaker
fixed-order sieve than its product-star ideal, because adding `theta` and
`lambda` can only enlarge the ideal and reduce its norm.

Odd Galois dilation, exchange inside any unordered product pair, and exchange
of the leaves `F,G` preserve the candidate condition and ideal norm. No
exchange of `Q_0,Q_1` is claimed, because `Q_0` is the distinguished anchor
in `lambda`.

This theorem is a finite fixed-order router. It does not construct
`D_n^DA` efficiently, factor its ideal norms, bound the number of surviving
primes, or prove the global `Y_18` estimate on survivors.
