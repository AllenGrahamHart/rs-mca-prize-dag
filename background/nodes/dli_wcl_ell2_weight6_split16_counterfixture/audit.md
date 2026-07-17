# Audit - DLI ell-two weight-six split-16 counterfixture

## Load-bearing checks

- primality of `65537` and exact order `1024` of `omega`;
- six distinct exponents with no antipodal pair;
- both odd moments, not merely the first;
- full-order ratio generation rather than a lower-order lift;
- exact `v_2(q-1)=16` scope pin;
- explicit refusal to infer an official-row counterexample.

## Nonclaims

- The fixture does not satisfy the official `v_2>=41` ambient split.
- It neither closes nor refutes `dli_wcl_zone_coverage`.
- The 128-candidate random adversary is evidence provenance, not an exhaustive
  theorem.

## Discovery provenance

Modal app `ap-D951m912raeZd4GsqlmNqR` completed 128 deterministic order-1024
norm candidates; app `ap-nAQAeumsj1vQ2HJ2SLwppo` replayed every sampled factor
with `v_2(p-1)>=11` at the same cyclotomic embedding and with all cubic guards.
The compact theorem does not depend on the full transcript.
