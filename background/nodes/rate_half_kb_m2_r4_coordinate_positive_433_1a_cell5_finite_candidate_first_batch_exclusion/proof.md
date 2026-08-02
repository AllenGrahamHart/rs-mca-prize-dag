# Proof

For every routed value, specialize the exact primitive factors and coordinate
maps, factor each parent over `F_p`, reconstruct `b,x0,x1,r,c` on each finite
subfactor, and freshly rebuild the `DE+` necessary polynomial and colored
`BE` resultant.  No generic colored Bezout coefficient is specialized in
this recomputation.

The specialized parent-factor degrees sum to `4,4,4,8,4` at every fiber, so
the 433 rows are a complete factor ledger for these 23 routes.  The checker
also verifies on every row

```text
s = x1+2*x0+3b
```

modulo the printed irreducible factor.

If the fresh gcd is `1`, the two necessary equations have no common root.  If
it is `e^2-1`, every common root violates target square distinctness.  These
are the 383 `bezout_guard` rows.

On 16 rows the only outside gcd occurs over an irreducible primitive factor
of degree greater than one.  For an actual deployed packet all target and
source-square coordinates lie in `F_p`, hence their printed linear
combination `s` lies in `F_p`.  But the residue class of `s` on an irreducible
factor of degree greater than one is not in `F_p`.  Such a row has no
deployed-field point.

The remaining 34 rows have linear primitive factors, so the checker factors
their scalar gcds independently over `F_p`.  Every root has either `e=0` or

```text
e^2 in {1,b^2,c^2}.
```

These are explicit target nonzero/collision guards.  Thus no row contains an
admissible target root `e`.  All 433 rows are empty, proving the 23-fiber
exclusion. QED.
