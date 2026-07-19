# height_only_impossibility proof

The pure height certificate is exactly the criterion proved in
`graded_collision_radius`: a pair at swap distance `s` is certified
collision-free when

```text
(2s)^phi(N') < p.
```

To certify an entire quotient cell by height alone, this inequality must hold
at the cell's maximum swap distance `s_max`.

At `N' = 128`, `phi(N') = 64`. Official row primes satisfy `p < 2^256`, so a
height-only full-cell certificate would require

```text
(2s_max)^64 < 2^256,
```

hence

```text
2s_max < 16,
```

or `s_max <= 7`.

The official in-corridor `N' = 128` quotient cells have maximum swap distance
at least `8` in all four rate rows recorded by the node. Therefore their full
cell cannot be certified by the pure height gate. Any full-strength
certification at those scales must use additional `p`-specific information,
such as the lattice or MITM certificate branches.
