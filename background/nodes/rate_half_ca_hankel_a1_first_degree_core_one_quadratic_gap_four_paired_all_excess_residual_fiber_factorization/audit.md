# Audit

1. `g_delta` need not have support exactly `W_delta`; containment suffices
   and is represented by the residual polynomial `H_delta`.
2. The degree of `H_delta` is at most, not necessarily equal to,
   `a_delta`. The difference is exactly the specialized `X`-degree drop.
3. The source equality is used on `X_delta`, where the actual error
   vanishes. The actual error is retained at incidences when the first jet
   is computed.
4. The interpolation degree is exactly the biform `X`-degree `n`; no value
   outside `U_0` is used.
5. The outside-support values satisfy `g_delta=-e_delta!=0`, so
   `H_delta` is coprime to `B_delta`. It may still share roots with
   `A_delta` or `R_delta`, which changes multiplicity in `G` but not the
   squarefree full-locator gcd.
6. The proof is field-general and uses no numerical experiment.
