# Cycle 49: rate-half type-2 quartic biform-lift obstruction (2026-08-10)

## Decision

Follow the incidence-only `(FR)` route fence into its first genuinely
algebraic question: can the explicit quartic countermodel be placed on the
smooth cyclic domain so that its incidence rows are evaluations of the
endpoint apolar biform?

## Proved result

`rate_half_type2_fr_quartic_coset_biform_lift_obstruction` proves that the
answer is no for every coset-preserving placement. With `n=4m`,
`rho=n-1`, and `D=mu_(4n)`, the leading two parameter coefficients of a
putative lift would be degree-at-most-`n-1` polynomials `A,B` satisfying

```text
B(tau_i x)=xA(tau_i x)
```

on three complete `mu_n` cosets. Each polynomial
`tau_i B-XA` has degree at most `n` and vanishes on one full coset, so
comparison across three cosets forces `A=B=0`. The nonzero row scales make
that impossible.

At the pinned witness scale, `m=64`, `n=256`, `D=mu_1024` exists in
`F_(257^4)`, and the locator-degree cap is exactly `rho=255`. Therefore the
quartic incidence witness has no natural endpoint-biform lift even before
Hankel compatibility.

## Audit and scope

The primary verifier checks full-rank interpolation systems at five cyclic
scales. An independent verifier checks the power-map injection and hostile
scope mutations. Both pass under `ramguard tiny`.

This result does not prove `(FR)`, exclude arbitrary permutations of the
incidence points, close a crossing budget, or change a critical status. It
shows that the algebraic input absent from the incidence fence is already
decisive on the strongest explicit countermodel.

## Frontier

Do not spend another cycle on this quartic construction. The live positive
object is the family

```text
Psi_gamma=(c_0+gamma c_1) Q_gamma|_D
```

inside the shortened apolar MDS code on a minimum joint support `W`.
A useful next theorem must control its aggregate near-minimum-weight fibers
using the common pencil, or else construct a different realizable algebraic
countermodel. The official `9/4` residual remains unchanged.
