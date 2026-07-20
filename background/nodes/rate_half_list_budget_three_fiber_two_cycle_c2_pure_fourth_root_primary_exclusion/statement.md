# Budget-three fiber-two c=2 pure fourth-root primary exclusion

- **status:** PROVED
- **closure:** proof
- **consumer:** `rate_half_list_adjacent_crossing`
- **dependencies:**
  `rate_half_list_budget_three_maximal_field_degree_collapse`,
  `rate_half_list_budget_three_fiber_two_cycle_c2_normalized_gap_span_compiler`

Retain the maximal official normalized `c=2` mismatch chamber, with

```text
H=2^37+1,       m=2H-2=2^38.                         (PFR1)
```

Suppose the four denominator roots form a scaled fourth-root quartet. By the
proved common subgroup scaling, normalize it to

```text
{1,iota,-1,-iota},       iota^2=-1,
E(z)=1-z^4.                                             (PFR2)
```

Then

```text
E(z)^(-1/4)=sum_(j>=0) ((1/4)_j/j!) z^(4j),            (PFR3)
```

and therefore

```text
a_m=(1/4)_(2^36)/(2^36)!=0.                           (PFR4)
```

This contradicts the required primary gap `a_m=0`. Hence no scaled pure
fourth-root denominator can occur in an official generic `c=2` mismatch
survivor.

The theorem excludes only this denominator geometry. It does not assert that
the primary gap, or the primary-plus-secondary packet, forces a pure
fourth-root quartet. In particular, bounded non-pure primary-gap witnesses
exist and are recorded in the audit.
