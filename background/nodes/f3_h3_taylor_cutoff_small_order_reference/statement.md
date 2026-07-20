# H3 Taylor-cutoff small-order reference

- **status:** PROVED
- **closure:** finite exhaustive verification
- **consumers:** `f3_h3_official_order_template_survivor`
- **dependencies:** `f3_h3_global_resultant_compression`,
  `f3_h3_quotient_orbit_canonical_resultant_manifest`,
  `f3_h3_quotient_orbit_taylor_cutoff_ladder`

The dense reference program
`tools/c36_taylor_cutoff_reference.py` is hard-capped at exponent four. On the
fully checked packet `n=8`, cutoffs `c=2,3`, it:

1. constructs the degree-49 shifted-product polynomial by an exact resultant;
2. constructs all 12 canonical quotient-orbit blocks by the proved resultant
   formulas;
3. computes every Taylor-resultant coefficient content; and
4. writes an atomic checkpoint before each stage and after every block.

The resulting block union agrees with independent direct finite-field
enumeration at the official congruence primes

```text
p in {17,41,73,89,97,113,137,193}.
```

For cutoff two the surviving primes are exactly `{17,41}`; for cutoff three
the survivor is exactly `{17}`. A synthetic timeout preserves a JSON packet
with `complete=false` and `stage=timeout`, and a deliberately truncated run
preserves `stage=partial_selection`.

This node proves a small-order correctness oracle and output contract only. It
does not validate `n=16`, permit `n>16`, establish an official-order resource
bound, compute an official row, factor a content, bound a moment, or close
C36'.
