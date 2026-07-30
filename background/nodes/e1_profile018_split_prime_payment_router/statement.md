# E1 profile-(0,18) split-prime payment router

- **status:** PROVED
- **closure:** local cofactor census, profile-invariant exclusions, and exact payment threshold
- **scope:** binding prize rate-`1/8` row, profile `(0,18,S=18)`

Every profile-`(0,18,S=18)` collision has exactly the same thirteen possible
cofactors as the preceding square-mass-18 profiles:

```text
2,4,8,16,32,64,128,256,512,1024,514,1028,1538.
```

The cofactor-1538 branch is empty. The complete global window and five
energy exclusions make the cofactor-1028 branch empty. Cofactor 514 is
confined to the 15 proved autocorrelation magnitude profiles at energies
five through twelve. Therefore

```text
T_018<=10+128=138,
|D_018|<=35328.
```

Let `O_514` be the number of the 128 prime ideals above 257 occupied by a
cofactor-514 collision for one fixed row prime and quotient root. If

```text
O_514<=5,
```

then `T_018<=15` and `|D_018|<=3840<3994`, so profile `(0,18)` is paid. At
that worst-case threshold its exact charge is

```text
2145265610605098043549680394481864540160,
```

the residual edge budget is

```text
86073582443276011446219038016747383207,
```

and the next dictionary profile is `(4,4,S=20)` with tight uniform oriented
cap `329`. The implication and all arithmetic are proved; the five-ideal
occupancy bound is the remaining premise.
