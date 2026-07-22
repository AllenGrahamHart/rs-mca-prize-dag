# Upstream crosswalk - Pade sections and support moments

## Exact object identification

Paper D v13.2 writes

```text
cen(U;m)=sum_c binom(agr(U,c),m)
```

and realizes it as a shifted-lattice/split-pencil census.  This node proves
that `cen(U;m)` is exactly the number of split points on our full-locator
Pade section before the complement gcd guard.  The guarded exact-shell count
is the binomial atom `Z_m`, and all atoms are recovered by `(PS2)`.

## Consequence for vendoring

An upstream theorem bounding `cen(U;m)` is immediately an upper bound for
our level-`m` exact shell.  Conversely, exact-shell certificates can print
the complete upstream moment table without re-enumerating support subsets.

## Remaining interface

This identifies the algebraic object, not the final active certificate.
Base-field discrete/soft floors, quotient/prefix first owners, local
shift-pair numerators, and the summed adjacent-row reserve must still be
matched explicitly before a status promotion.
