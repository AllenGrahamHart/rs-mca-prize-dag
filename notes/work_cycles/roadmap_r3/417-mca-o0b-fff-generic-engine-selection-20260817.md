## MCA O0b `FFF` generic-fiber engine selection (2026-08-17)

### Singular boundary

The exact `imap` construction used elsewhere in the repo cannot be run at
the deployed prime in Singular's transcendental coefficient-field backend:

```text
characteristic: 2130706433
engine cap:     2^29
failure line:   ideal H=std(imap(R,G))
Modal app:      ap-xIYe6cHFkUBtFeoIUlmDUD
```

No basis was produced. This is an engine limitation, not evidence about the
generic fiber.

### Selected engine

The repository already has a pinned Julia 1.11 image with AbstractAlgebra and
Groebner.jl that constructs `GF(2130706433)(t)`, certifies Groebner bases,
builds quotient bases, and serializes rational-function numerators and
denominators. Reuse that stack.

### Next decision gate

1. Convert the 48 Singular basis strings to Julia expressions with a checked
   parser for compact monomials such as `x2tr3`.
2. Compute and certify the generic basis in
   `GF(p)(t)[x,r,c,b]` using deterministic single-task Groebner.jl.
3. Retain the quotient dimension and full basis. Extract coefficient
   numerator/denominator lists before any FFF reduction.
4. Keep all denominator roots as open exceptional fibers; no generic-only
   result promotes `FFF`.
