# x4b_moment_trade_exclusion conditional proof

## Predicate nodes

- `u2_per_row_certifier`
- `u2c_boundary_scale_column`

## Claim

The p-specific moment-trade column is handled once the small-row certificates
and the boundary/giant column are supplied.

## Proof

Split possible primitive moment-trade blocks by size.

For Row-C-class small windows, `u2_per_row_certifier` is exactly the required
Reading-B input: it certifies, row by row and for every live `b <= C log n`,
that no primitive `t`-null block in the official domain survives the quotient,
dihedral, and dictionary charges. If a row has such a family, the same
certifier interface emits the exact charged column instead.

For prize-max giant windows, the small range is empty because `b > t` while
`t` is already much larger than `log n`. The remaining giant and boundary-scale
families are precisely the scope of `u2c_boundary_scale_column`: the `M = t`
zero-sum coset class is added to the dictionary and counted, and the residual
mod-p extras are delegated to its stated predicate.

Those two predicates exhaust the size split used in the node statement.
Therefore no additional p-specific moment-trade theorem remains at this node.
