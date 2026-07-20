# Audit

- The adapter uses decorated roots `r,s`; forgetting them can identify
  multiple decompositions of one cubic pair and would not prove `K=2D`.
- The pair has degree three and depth one. It is not the constant-shift top
  stratum: its nonzero difference is `lambda X`.
- Coefficient primitivity uses the load-bearing dyadic fact
  `gcd(2^s,3)=1`. It does not classify arbitrary degree-three shift pairs.
- The equal-constant condition `A(0)=B(0)=-rs` is required for the converse.
  A generic pair of cubics differing by `lambda X` need not be a DSP8 pair.
- The factor four from `K` to `J` is only the two internal root orders at
  each endpoint. Endpoint order is already retained by `K`, and the quotient
  pair is already ordered by `R(t)`.
- A marginal SP bound does not pay `(SPA7)` unless it retains the target-local
  quotient-line multiplicity and the antipodal class weight.
- The verifier independently enumerates every reduced decorated cubic pair at
  the `n=16` controls and compares that set with the forward DSP8 construction;
  this tests the converse rather than replaying only generated records.
