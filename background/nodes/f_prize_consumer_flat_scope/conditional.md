# Historical conditional proof: prize consumer flat-scope compiler

> **DISCHARGED 2026-08-07:** `f_imgfib_consumer_descriptor` proved route
> retirement rather than a LIST branch-to-flat map. The strict caller set is
> now the singleton `{spi_point_counting}`. See `proof.md` for the live proof.

## Predicate

- `f_imgfib_consumer_descriptor`

The second interface, `f_spi_hankel_consumer_descriptor`, is proved.

## Strict caller inventory

The local manifests have exactly two `req` edges out of `conj_f`:

```text
conj_f -> imgfib
conj_f -> spi_point_counting.
```

The R2/SPI evidence links do not create additional prize consumers. The
mixed-petal target is separately required by `imgfib`; its full Pade section
is not a linear-flat call. The exact root-free projective cell extracted
inside that route is part of the LIST descriptor predicate.

## Assembly

Grant `f_imgfib_consumer_descriptor`. It emits every LIST-side Conjecture-F
call with its punctured domain, locator degree, projective dimension, root
threshold, and first owner, preserving the counted codeword/section-point
multiplicity. The proved SPI descriptor emits the same data for every
Hankel slope incidence, preserving slope-incidence multiplicity even when a
locator lies over more than one slope.

These are all strict callers by the inventory above. Their union is therefore
the complete prize-consumer descriptor set. Paid descriptors are removed by
their first owners; every residual descriptor is passed unchanged to
the downstream absolute-exponent packing step. This proves the compiler
conditional on the LIST predicate. A new strict caller invalidates the pinned
inventory and re-opens the node.
