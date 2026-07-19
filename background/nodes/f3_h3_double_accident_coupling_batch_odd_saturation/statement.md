# H3 double-accident coupling-batch odd saturation

- **status:** PROVED
- **closure:** proof
- **consumer:** `f3_h3_mobius_excess_half`
- **dependencies:**
  `f3_h3_double_accident_low_distance_joint_ideal_router`,
  `f3_h3_double_accident_nonzero_coupling_ideal_router`

Let `n=2^s`, `s>=3`, put `O=Z[zeta_n]`, `pi=1-zeta_n`, and define the
normalized shifted units

```text
c_a=(1-zeta_n^a)/pi,       0<a<n.                 (CBS1)
```

If `a=2^r A` with `A` odd, then

```text
|Norm(c_a)|=2^(2^r-1).                              (CBS2)
```

Thus every `c_a` is a unit in `O[1/2]` and at every prime ideal above an odd
rational prime.

Fix a lifted product representation `E`, and for distinct ordered
nonidentity quotient lifts `Q_i=(u_i,v_i)` put

```text
lambda_i=beta_E c_(u_i)-c_(v_i),
theta_01=c_(v_1)c_(u_0)-c_(v_0)c_(u_1).           (CBS3)
```

Here `lambda_i` is the normalized product-to-quotient coupling and `theta_01`
is the normalized quotient-collision generator from the joint-ideal router.
They satisfy the exact syzygy

```text
c_(u_0)lambda_1-c_(u_1)lambda_0=-theta_01.         (CBS4)
```

Consequently, for every integral ideal `J subset O`,

```text
(J,lambda_0,theta_01)O[1/2]
  =(J,lambda_0,lambda_1)O[1/2].                    (CBS5)
```

The two integral ideals therefore have identical valuations at every odd
prime ideal and identical odd parts of their absolute ideal norms.

More generally, for distinct quotient lifts `Q_0,...,Q_(R-1)`, let

```text
I_anchor=(J,lambda_0,theta_(0,1),...,theta_(0,R-1)),
I_batch =(J,lambda_0,lambda_1,...,lambda_(R-1)).    (CBS6)
```

Then

```text
I_anchor O[1/2]=I_batch O[1/2].                    (CBS7)
```

Taking `J=(alpha_F,alpha_G)`, the complete odd-prime double-accident ideal can
therefore be represented by a symmetric batch of coupling generators; no
separate quotient-collision generator type is needed. On a positive `Y_18`
target, at least `R(t)-1` of these generators are nonzero by the proved
nonzero-coupling router.

This is an exact algebraic simplification. It does not say the two integral
ideals agree at the prime above two, give a lower bound for their common odd
ideal norm from the number of generators, or bound the surviving row primes.
