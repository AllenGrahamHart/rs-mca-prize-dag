# E1 profile-(2,10) cofactor-514 outer-energy exclusion

- **status:** PROVED
- **closure:** exact bounded-deviation logarithm bounds
- **scope:** binding prize rate-`1/8` row, profile `(2,10,S=18)`, cofactor `514`

No profile-`(2,10,S=18)` collision on a prize-envelope row with cofactor
`514=2*257` has autocorrelation energy

```text
E in {0,1,2,3,4,14,15,16,17}.
```

At energies one through four, a logarithm minorant on `[-8,8]` puts the norm
strictly above `514*p_max`; energy zero has the wrong 2-adic norm valuation.
At energies fourteen through seventeen, energy-dependent logarithm majorants
put the norm strictly below `514*p_min`.

The cofactor-`514` branch is therefore reduced from `E=0,...,17` to

```text
E in {5,6,7,8,9,10,11,12,13}.
```
