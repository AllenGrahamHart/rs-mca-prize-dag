# Exact cap for a fixed nonzero affine-reflection pencil

- **status:** PROVED
- **closure:** complete official-field cyclotomic census
- **consumer:** `rate_half_band_crossing_location` (evidence)
- **dependency:**
  `rate_half_mca_rank11_exception_spi_affine_reflection_fence`

Let

```text
p=2130706433,       H=mu_N subset F_p^*,       N=2^21,
R_c=#{x in H:c-x in H}.
```

For every `c in F_p^*`,

```text
R_c <= 2308.                                           (FC1)
```

The reflection `x -> c-x` has at most one fixed point. Its nonfixed
two-element orbits therefore number at most `floor(R_c/2)<=1154`. Each such
orbit is exactly one pairwise-disjoint split squarefree fiber of the fixed
pencil

```text
X^2-cX+gamma.
```

The bound is sharp. The unique maximizing multiplicative `H`-coset is
represented by

```text
c=3^74 mod p=1177199610,
R_c=2308,
fixed points=0,
fibers=1154.
```

This theorem concerns one fixed nonzero affine-reflection pencil. It does not
assign one pencil to a heavy pair type and does not identify packet pencils
chosen from different twenty-record subsets. The antipodal case `c=0`, which
has `N/2` two-cycles and belongs to the quotient-periodic boundary, is outside
the statement.

## Falsifier

A nonzero coset with more than `2308` reflection points, a fixed pencil with
more than `1154` nonfixed two-cycles, an implementation disagreement, a
missing coset, failure of the exact first moment, or any aggregate heavy-ruling
payment made without a separate pencil-synchronization theorem.
