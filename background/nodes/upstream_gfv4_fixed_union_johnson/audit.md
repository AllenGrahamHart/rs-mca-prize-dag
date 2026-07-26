# Audit

The proof was reconstructed independently. The scope checks are:

1. `U` is one fixed union; summing `(FU1)` or `(FU3)` over charts would add a
   combinatorial factor.
2. `(FU1)` requires the printed transversality for every selected slope.
3. `(FU3)` requires `h^2>N(nu-1)` before division.
4. The MDS kernel is `[R+nu,nu,R+1]`; replacing `R+1` by an ambient-code
   distance changes both proofs.
5. Separate lifts of `y_0,y_1` are chosen only after two supported slopes
   show that both syndromes lie in the span on `U`; the zero/one-slope cases
   are discharged first.

The focused verifier checks the algebra and matroid multiplicity. The audit
verifier exhausts small set systems satisfying the only combinatorial input
to the Johnson argument.
