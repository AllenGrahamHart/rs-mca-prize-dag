# xr_expansion conditional proof

## Predicate nodes

- `johnson_gap`
- `exchange_ledger_gen_t`
- `xr_anticode_toolkit`
- `v8_ledger`

## Claim

The expansion/anticode branch gives FM-scale bounds on the large-distance
post-strip strata.

## Proof

Fix a post-strip pair and restrict to a stratum whose aligned supports are
pairwise separated beyond the ledger exclusion radius. By `xr_anticode_toolkit`
and the exact Johnson gap `johnson_gap`, a set of locators with that exchange
separation has anticode-bounded size, with the usual Johnson combinatorial
factor for the chosen radius.

By `exchange_ledger_gen_t`, each close residual constraint within the ledger
reach contributes the q-power suppression given by the generalized exchange
ledger. On the large-distance stratum, this is exactly the algebraic q-scale
input missing from a pure Johnson-graph counting argument.

Finally, `v8_ledger` supplies the one-support-one-slope cap, so the locator
bound cannot be inflated by many slopes on the same support.

Multiplying these three inputs gives the advertised FM-scale expansion bound
on the large-distance strata. The proof intentionally leaves the small-radius
remainder to the XR energy/inverse branch.

