# Audit

Errors of weight below `r` are handled by padding their support with unused
domain points. Conversely, coefficients recovered on an `r`-root locator may
vanish, so the represented error may have smaller support. This makes `(HS1)`
an exact `<=r` statement.

The locator is monic, squarefree, and split over the actual evaluation domain,
not merely over the ambient field or its algebraic closure. The dual
multipliers are nonzero and are absorbed into the recovered error values.

Component bounds for the ambient Hankel incidence do not by themselves bound
the number of slopes carrying a domain-split locator. The generic horizontal
SPI point-counting problem remains visible rather than silently consumed.
