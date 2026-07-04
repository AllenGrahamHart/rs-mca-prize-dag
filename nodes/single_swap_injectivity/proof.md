# single_swap_injectivity proof

If two classes differ by one swap, then

```text
e1(B) - e1(B') = zeta^i - zeta^j
```

for two distinct roots. Every archimedean conjugate has absolute value at
most `2`, so the norm has absolute value at most `2^phi(N')`.

The difference is nonzero by `char0_collision_classification`, equivalently
by the nonzero input used in `collision_norm_criterion`. At prize scale the
admissible row prime satisfies

```text
2^phi(N') < p
```

for the single-swap rung under discussion. Hence the nonzero norm is too
small to be divisible by `p`. By `collision_norm_criterion`, no finite-field
single-swap collision can occur.

This is exactly the `s = 1` case of `graded_collision_radius`.
