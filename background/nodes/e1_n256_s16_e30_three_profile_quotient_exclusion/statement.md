# E1 N=256 E=30 three-profile quotient exclusion

- **status:** PROVED
- **closure:** exact quotient-allocation computation

At `N=256`, folded profile `(3,4,0)`, and autocorrelation variance `V=60`,
none of the magnitude profiles

```text
(0,3,2), (6,2,0,1), (3,0,3)
```

can occur in a pair-feasible collision.

A complete mod-16 quotient-allocation census gives the exact third-moment
upper bounds

```text
profile       order 128             order 64
(0,3,2)       6,892 / 936           6,084 / 936
(6,2,0,1)     1,154,703 / 1058      724,659 / 1048
(3,0,3)       25,884 / 1002         21,368 / 940
```

where each entry is `allocations / maximum`. Every maximum is below the exact
`V=60` cubic cutoff `M_3=1087`. An independent checker reconstructs all shard
totals, capacities, maximizing allocations, and objective values.
