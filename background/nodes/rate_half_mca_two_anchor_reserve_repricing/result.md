# Result

The route-comparison reserve probe returns:

```text
verdict:                         SURVIVES_WITH_EXPLICIT_PRICE
old exception cap:              31
new separate owner charges:     2w and 31
large-owner target movement:    exactly -2w
KoalaBear full target:          274980728111260112
Mersenne-31 full target:        16642288
Mersenne average-ceiling ratio: >9
```

The direct S/A/E route is not killed by integer arithmetic.  Its first
missing source repair is now exact: declare the near-rational owner before
the residual exception set and replace every large-owner target by `(RR1)`.
Proving that stricter large-owner input remains open.
