# E1 prize N=256 profile-(3,6) cofactor-1024 exclusion

- **status:** PROVED
- **closure:** dual exact finite enumeration
- **scope:** prize-envelope `N=256`, profile `(3,6,S=18)`
- **dependency:** `e1_prize_n256_s18_profile_36_sharp_product_window`

There is no profile-`(3,6,S=18)` prize collision with norm cofactor

```text
m=1024.
```

Cofactor `1024` forces singleton multiplicity `mu=10`. The sharp product
window leaves only

```text
V in {4,6,8,10,12},       E=V/2 in {2,3,4,5,6}.     (1)
```

After affine normalization, the complete low-chord singleton census has 68
orbits. Two independent exact heavy-position engines agree on all 194816
targets and prove that no profile vector realizes an energy in (1).

This removes cofactor `1024`; ten profile-`(3,6)` cofactors remain.
