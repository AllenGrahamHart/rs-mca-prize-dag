# Audit

The statement in `node.json` records the corrected packing inequality. The
left binomial is `binom(m-t,k)`, not `binom(n-t,k)`; using the latter would
collapse the conclusion to `|T|<=1` and is false.

Showing that an upper bound exceeds the row budget does not construct an
over-budget family. The result is a route fence only: the elementary shadow
count, by itself, is quantitatively insufficient.
