# Claim contract

## Inputs

- `e1_prime_field_l2_norm_collision_radius`, including the two surviving
  `N=256,s=5` profiles and the lower prime endpoint `p>=2^250`;
- `collision_norm_criterion`.

## Output

No first-band `N=256` folded vector whose actual support differences have a
nontrivial common divisor with `256` collides at a pair-feasible row prime.

## Guards

1. The gcd uses the actual nonzero folded support after coefficient
   cancellation.
2. Monomial translation is allowed, but no coefficient or support point is
   discarded.
3. The small-field norm is proved nonzero using `deg B<phi(M)`.
4. The full norm may exceed the row prime; the proof controls its prime
   divisors through the exact norm-power identity.
5. Full-conductor vectors, including low-variance examples, remain open.

## Falsifier

An excluded proper-conductor profile vector whose nonzero norm is divisible
by a named-interval row prime.
