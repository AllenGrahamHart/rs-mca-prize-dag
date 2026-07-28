# E1 prize N=256 profile-(3,6) cofactor-1028 exclusion

- **status:** PROVED
- **closure:** dual exact finite enumeration plus split-prime test
- **scope:** prize-envelope `N=256`, profile `(3,6,S=18)`
- **dependency:** `e1_prize_n256_s18_profile_36_sharp_product_window`

There is no profile-`(3,6,S=18)` prize collision with norm cofactor

```text
m=1028=4*257.
```

Cofactor `1028` forces singleton multiplicity `mu=2`. The sharp product
window leaves only autocorrelation energy

```text
E in {2,3,4,5,6}.                                   (1)
```

Two independent exact engines find 16 normalized vectors in (1), all at
`E=5`. None vanishes at any primitive `256`th root modulo 257. Hence none has
norm divisible by 257, as every cofactor-1028 collision would require.

This removes cofactor `1028`; nine profile-`(3,6)` cofactors remain.
