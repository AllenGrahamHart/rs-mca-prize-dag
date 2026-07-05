# midlarge_h20_A conditional proof

- **status:** CONDITIONAL
- **closure:** proof from predicate node

## Predicate node

- `single_obstruction_valueset`

## Claim

Conditional on `single_obstruction_valueset`, the asymptotic band
`h in (20, A]` has at most the allowed active-core budget at official-shape
rows.

## Proof

Fix an official-shape row and `h > 20`. In this band, an active core satisfies
the obstruction system at the row's `zeta`; in particular it lies in the zero
fiber of the first obstruction

```text
O_{h-1}
```

restricted to anchored cores.

The predicate `single_obstruction_valueset` is precisely the needed fiber
bound for this map: equivalently, every value fiber of `O_{h-1}` on anchored
cores has size at most the row's active-core budget.

Therefore the zero fiber, which contains all active cores, has size at most
that budget. This certifies the whole `h in (20, A]` asymptotic band.

The additional fact that an active core forces at least `h-1 >= 20`
simultaneous obstruction vanishings motivates the value-set route, but the
conditional implication only needs the first-obstruction fiber bound.
