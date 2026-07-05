# conditional: dli_odd_phase_noncollapse_conductor

## Predicate nodes

- `dli_artin_schreier_conductor_criterion`
- `dli_odd_phase_reduced_pole_budget`

## Claim

Conditional on the actual odd-phase reduced-pole budget, the odd-evaluation
phases are geometrically nontrivial with conductor bounds whose harmonic total
is `o(t)`.

## Proof

The proved node `dli_artin_schreier_conductor_criterion` gives the exact
standard criterion: an additive phase is geometrically trivial precisely when
it is of Artin-Schreier form `g^p-g+c`, and otherwise its conductor is bounded
by the reduced polar divisor after Artin-Schreier reduction.

The predicate `dli_odd_phase_reduced_pole_budget` applies this criterion to
the actual phases `P_lambda(sigma(y))`: it rules out the Artin-Schreier form
on every relevant component and supplies a reduced-pole divisor budget whose
harmonic total is `o(t)`.

Combining these two statements gives geometric nontriviality/noncollapse and
the required conductor budget for every central profile, nonzero frequency,
and DLI harmonic.
