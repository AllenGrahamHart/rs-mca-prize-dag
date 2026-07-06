# graded_collision_radius proof

Let two quotient classes differ by swap distance `s`. Their first elementary
sum difference is a sum of at most `s` removed roots and `s` added roots, so
every archimedean conjugate has absolute value at most `2s`.

By `collision_norm_criterion`, a finite-field collision can occur only if the
row prime `p` divides the nonzero cyclotomic norm of this difference. The norm
is bounded by

```text
(2s)^phi(N').
```

Therefore if

```text
(2s)^phi(N') < p,
```

then the nonzero norm is a positive integer strictly smaller than `p`, so `p`
cannot divide it. The pair is collision-free.

At `N' = 128`, `phi(N') = 64`. For a prize-scale prime `p ~ 2^250`,

```text
p^(1/64) ~ 2^(250/64) > 14,
```

so `2s < p^(1/64)` holds through `s = 7`. This gives the recorded
`d* = 7` radius.

If the full class radius satisfies `2l' < p^(1/phi(N'))`, then the same
argument applies to every pair in the cell, giving unconditional fullness at
that scale. The `s = 1` case is `single_swap_injectivity`.
