# Audit

The source normalization uses square-root lifts of the deleted roots, not the
deleted roots themselves. This is why `r^4=t` rather than `r^2=t`.

There is only one lift-sign type. Within either antipodal deleted pair, swap
the two labels if necessary so that the lift ratio is `iota`; the resulting
change is absorbed into `r`. The three equations enumerate perfect matchings,
not 24 point permutations.

The cross-ratio equation is cleared without dividing by `1+q` or by
`z+1`. Thus the harmonic branch `q=-1` is retained. Dropping it would make
the router incomplete.

The condition `q in mu_N` comes from the constant terms of the monic reversed
root-cell factors. It is not inferred merely from `q in F_p`, which would be
far weaker.

The router is applied only after distinct outer splitting and the base-field
descent. It does not assert that an arbitrary solution of one ratio equation
extends to the polynomial square-pencil identity.
