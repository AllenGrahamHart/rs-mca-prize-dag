# E1 prize N=256 profile-(3,6) sharp product window

- **status:** PROVED
- **closure:** analytic extremum reduction plus exact rational certificate
- **scope:** prize-envelope `N=256`, profile `(3,6,S=18)`
- **dependency:** `e1_prize_n256_s18_profile_36_cofactor_windows`

For either cofactor

```text
m in {1024,1028},
```

every putative profile-`(3,6,S=18)` prize collision has

```text
V in {4,6,8,10,12}.                                (1)
```

Equivalently, the sharp fixed-mean/fixed-variance product envelope excludes
every even `V` from `14` through `34`. The parent theorem excludes `V=0,2`
and every `V>=36` in these two cofactor classes.

The product envelope itself does not exclude `V=12`; an exact rational lower
certificate at its maximizing two-level chamber remains above the cofactor
`1024` prize floor. Thus (1), rather than a stronger empty-window statement,
is the certified conclusion.
