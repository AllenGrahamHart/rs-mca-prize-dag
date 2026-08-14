# Cycle 283: rate-half Shape-A locator-interpolation rank amplification (2026-08-13)

The primitive locator has `n+1` exact `X`-interpolation parity checks. After
the three-source-class row decomposition, every check is a restricted
Koszul syzygy. Projection to either class of size `n+2` has rank at least
`r-1` by Sylvester's inequality.

```text
dim Koszul kernel=3r-(e+1)>=r-1,
r>=(e+1)/2=91625968982.
```

```text
former floor:          61083979322 [excluded]
new floor:             91625968982
new boundary kernel:   91625968982
live rank interval:    [91625968982,e-1]
critical status effect:none
hostile mutations:     7/7
```

The next rank improvement requires controlling the common kernel of the
three classwise interpolation maps, or proving that their combined map is
closer to injective than one projection alone detects.
