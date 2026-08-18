# Audit

## Semantic checks

1. The common support is the exact intersection from the parent seed. Its
   proved bound `c<K-2` gives `K-c>=3`; no maximal-support claim is used.
2. Actual support-wise MCA-badness and non-affinity are parent outputs, not
   inferred from formal polynomial division.
3. The homogeneous system counts two equations at a multiply covered
   coordinate, one at a singleton, and none at an unused coordinate. Its
   row count is therefore at most `chi'`.
4. The denominator degree is the shortening invariant
   `(m-c)-(K-c)=m-K=67472`.
5. The scalar-zero rational case is excluded using all 32 polynomial
   identities and the certified off-line explanation.
6. Denominator roots are retained. No division by `Q` is used.
7. The exact lift checks both degree contributions and adds exactly `2c` to
   two-cover complexity.
8. First ownership is preserved only as a label on the selected records; no
   aggregate chronology owner is asserted.

## Executable controls

The primary verifier checks the full allowed shortening interval, sampled
cores, unknown counts, exact threshold lift, and a finite-field certificate
lift. Hostile mutations cover the degree pin, residual-dimension endpoint,
denominator bound, complexity threshold, and toy certificate. The
independent audit recomputes the endpoint arithmetic and checks the toy
identity pointwise with a separate implementation.
