# Audit

The primary checker evaluates `(SP1)` by exact binomial arithmetic, scans all
`1<=e<d` at each first-unpaid row, verifies monotonicity and both adjacent
boundaries, and rejects four mutations.

The independent checker evaluates the same ratio as a gcd-cancelled product,
without `math.comb`, and reconstructs each last-paid support size by a linear
scan.  It rejects three independent controls.

Both checks are tiny local arithmetic under RAMguard.  No Modal compute is
used.
