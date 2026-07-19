# Audit

1. The row descriptor is recomputed by the existing compiler; copied or
   tampered scalar fields are not trusted.
2. The theorem packet uses `B*+1` only as an explicit lower witness count and
   `B*` only as a proved upper bound; neither is described as the exact list
   size.
3. `LIST` and `INTERLEAVED_LIST` have distinct explicit arity scopes and claim
   identifiers.
4. The wrapper repeats the descriptor's external preconditions instead of
   silently claiming a primality or domain-realization certificate.
5. The compiler, not the wrapper, performs the safe/unsafe classification and
   endpoint conversion. The wrapper checks the result independently.
6. Refusal tests cover wrong budget, zero budget, wrong rate, non-quarter
   length, wrong object, wrong schema, augmented input, inadmissible subgroup,
   and descriptor tampering.

The verifier pins the generator and its independent behavior audit along with
the already-pinned descriptor/compiler implementations.
