# proof: e1_exceptional_set_reduction

The reduction has four proved inputs.

First, `collision_norm_criterion` proves that if two non-quotient classes
`B != B'` collide in `e_1` modulo a prime ideal above the row prime `p`, then
`p` divides the nonzero integer

```text
Norm_{Q(zeta_N')/Q}(e_1(B) - e_1(B')).
```

The nonzero assertion is supplied by the characteristic-zero collision
classification inside that node. The same proof bounds every archimedean
conjugate by `2l'`, so the exceptional integers have explicit bounded height.

Second, `kernel_lattice_reframing` gives the per-prime equivalent form:
collisions are sparse ternary kernel vectors for the explicit row lattice

```text
K_p = {v : sum v_x zeta^x = 0 mod p},
```

modulo the known cyclotomic relations. This is the certification form of the
same exceptional-prime condition.

Third, `graded_collision_radius` removes all sufficiently small
swap-distance pairs at prize-scale primes: if `(2s)^phi(N') < p`, then the
nonzero norm is smaller than `p` and cannot be divisible by `p`.

Fourth, `are_exceptional_density` sums the bounded-height norm divisors and
proves an almost-all-primes density bound for this exceptional set. That
result does not by itself identify the official row primes as typical, but it
proves that the residual obstruction is exactly official-prime incidence with
a sparse explicit exceptional set.

Therefore `e1_fullness` is reduced to the remaining predicate
`e1_official_prime_exception_control`, which must show that the admissible
prize row primes avoid, or are sufficiently sparse inside, the exceptional
norm-divisor set, or else provide direct folded-lattice certificates for the
pinned rows.
