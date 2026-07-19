# averaged_slope_conversion conditional proof

## Predicate nodes

- `fm1`
- `averaged_xr`

## Claim

For a post-paid support family, if the FM locator mean crosses `B*`, then some
pair `(u,v)` has at least `B*` distinct bad slopes.

## Proof

The predicate `fm1` supplies the exact first moment for aligned locators. The
predicate `averaged_xr` supplies the slope-resolved second moment: same-slope
pairs have the closed-form correlation term, while distinct-slope pairs are
independent. Applying the standard Paley-Zygmund/second-moment conversion to
these two moments gives a pair whose number of aligned locators is at least the
threshold carried by the FM mean, after the paid fibers have been removed.

The remaining conversion is from locator count to slope count. The already
proved v8 ledger bounds the number of locators charged to one slope in the
post-paid family, so the aligned-locator lower bound yields the required lower
bound on distinct bad slopes. The paid-fiber exclusion is part of the
post-paid-family hypothesis recorded in the node statement; without it the
conclusion would count paid slopes and would not be the intended unsafe
certificate.

Thus the local conversion follows from `fm1`, `averaged_xr`, and the proved v8
ledger convention, conditional only on the post-paid support-family scope
recorded in the DAG.
