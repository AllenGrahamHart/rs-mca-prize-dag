# E1 profile-(2,10) cofactor-514 middle-shape logarithm router

- **status:** PROVED
- **closure:** exact shape-sensitive bounded-deviation logarithm bounds
- **scope:** binding prize rate-`1/8` row, profile `(2,10,S=18)`, cofactor `514`

For an autocorrelation magnitude profile `(n_1,n_2,n_3)`, where `n_j` counts
positive-half lags with magnitude `j`, every live cofactor-`514` collision at
energy `5<=E<=13` lies in exactly one of these 17 profiles:

```text
E=5:  (5,0,0)
E=6:  (6,0,0), (2,1,0)
E=7:  (7,0,0), (3,1,0)
E=8:  (8,0,0), (4,1,0), (0,2,0)
E=9:  (9,0,0), (5,1,0), (1,2,0)
E=10: (10,0,0), (6,1,0)
E=11: (11,0,0), (7,1,0)
E=12: (12,0,0)
E=13: (13,0,0).
```

The omitted `E=5` profile `(1,1,0)` has norm above `514*p_max`. At energies
9 through 13, all profiles whose autocorrelation `L1` is at most

```text
(E,L1)=(9,3),(10,6),(11,7),(12,10),(13,11)
```

have norm below `514*p_min`. No coefficient-support realization is assumed or
enumerated.
