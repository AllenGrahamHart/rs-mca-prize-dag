# Proof

The `S2` skeleton has products

```text
{+/-c d, -e^2, +/-d f, +/-e f}.
```

The outside sign action leaves four forced-record orbits: colored `CD`,
loop `EE`, and one representative each of the full `DF` and `EF`
pairs.  After setting the forced record equal to `m`, eliminate its
determined representative and multiply the six residual linear factors.

Let `F(X,Z)` be that binary sextic and let

```text
M=[[Alpha,Beta],[Gamma,-Alpha]]
```

be the parent involution matrix.  Since
`M^2=(Alpha^2+Beta Gamma)I`, a residual multiset is three involution pairs
exactly when

```text
F(Alpha X+Beta Z,Gamma X-Alpha Z)
 =(Alpha^2+Beta Gamma)^3 F(X,Z).                  (1)
```

The first three coefficient equations of `(1)` are an independent
rank-three system.  In each forced cell they are sparse polynomials in the
two remaining outside representatives.

Exact two-variable Buchberger reduction gives `(KB41BS2-1)` in both
deployed `b` rows.  The colored and loop cells contain `1`, requiring no
guard saturation.  In the forced-`DF` cell the basis contains both
`d^2` and `e^2`; in forced `EF` it contains `e^2`.  These variables
are nonzero target representatives, so those cells are also empty.

Only `c^2` enters the involution coefficients, while the colored products
occur as the full pair `(+cd,-cd)`.  Replacing `c` by `-c` therefore
permutes factors without changing `F` or `(1)`.  The two checked `b`
rows and this sign transport cover every parent common packet. QED.
