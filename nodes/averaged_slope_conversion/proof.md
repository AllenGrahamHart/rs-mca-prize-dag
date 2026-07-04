# averaged_slope_conversion proof

## Claim

For a post-paid support family, if the v8-normalized FM locator mean crosses
`B*`, then some received pair `(u,v)` has at least `B*` distinct bad slopes.

## Proof

The node `fm1` supplies the exact aligned-locator first moment

```text
E[#aligned] = binom(n,j) (1 - q^(-t)) q^(1-t).
```

The node `averaged_xr` supplies the slope-resolved second moment. Same-slope
pairs have the closed-form close-shell correlation, while distinct-slope pairs
are independent on the plateau. Therefore the usual second-moment averaging
argument applies to the post-paid family: once the normalized FM mean crosses
the threshold, there is at least one pair `(u,v)` whose post-paid aligned
locator count reaches the corresponding locator threshold.

It remains to pass from locators to slopes. The proved `v8_ledger` gives the
per-slope locator cap in the post-paid family. Thus if one slope accounts for
at most `C_v8` locators, the raw locator threshold `C_v8 B*` forces at least
`B*` distinct slopes. Equivalently, using the v8-normalized locator count,
crossing `B*` directly forces `B*` distinct bad slopes.

The paid-fiber exclusion is essential but not an extra predicate: it is the
scope of this node. Without first removing paid fibers, the same moment
calculation would count paid slopes rather than unsafe bad slopes. Within the
post-paid support-family scope, the conversion follows from `fm1`,
`averaged_xr`, and `v8_ledger`.
