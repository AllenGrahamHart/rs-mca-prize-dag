# conditional: sov_fiber_budget_translation

## Predicate node

- `sov_obstruction_equidistribution`

## Claim

Conditional on `sov_obstruction_equidistribution`, the first-obstruction fiber
bound is below the active-core budget used by `midlarge_h20_A`.

## Proof

The predicate `sov_obstruction_equidistribution` is already stated in the
budget-normalized form: for official-shape rows and `h in (20,A]`, every fiber
of the first obstruction map `O_{h-1}` on anchored cores is small enough to
prevent a super-budget concentration of active cores.

The `midlarge_h20_A` consumer only needs the zero fiber of this same map,
because every active core forces the first obstruction to vanish. Therefore,
under `sov_obstruction_equidistribution`, the zero fiber is below the per-`h`
active-core budget. This is exactly the translation required here.
