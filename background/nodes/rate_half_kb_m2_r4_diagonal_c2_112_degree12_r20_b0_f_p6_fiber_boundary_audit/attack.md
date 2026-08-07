# Attack

This is evidence for a uniform field-point obstruction, not a global
certificate. Scanning further base-field values of `s` is not a closure
strategy because the required quantifier ranges over all of `F_(p0^6)`.

The unspecialized complete-open R20 ideals remain one-dimensional, with
basis sizes `44,39,33,35` for F04 through F07. Two attempts to expose their
generic component structure were bounded and failed closed:

- degree-reverse-lexicographic bases over `Q(s)` timed out after 480 seconds
  for the F04 and F05 symmetry representatives;
- target-prime lexicographic elimination of `x` in F04 timed out after 780
  seconds.

Both jobs completed source compilation and stayed below 0.4 GB child RSS.
Their exact partial records are retained. Do not increase those caps merely
to continue the same monolithic elimination.

The uniform theorem is now proved by
`rate_half_kb_m2_r4_diagonal_c2_112_degree12_r20_b0_generic_boundary_exclusion`.
Its block-order basis forces `(1+s+pvar)^2=0` away from three explicit
normalization factors, and all three exceptional ideals are unit. Do not
extend this sampled audit further.
