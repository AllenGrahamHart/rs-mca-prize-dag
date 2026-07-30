# E1 profile-(0,18) Galois/norm occupancy dictionary

- **status:** PROVED
- **closure:** exact diagonal-Galois fiber dictionary
- **scope:** profile `(0,18,S=18)`, cofactor 514

Fix an official row prime `p` and one primitive quotient root `r mod p`.
Let `O_514(p,r)` count the degree-one ideals `Q_s` above 257 occupied by a
profile-`(0,18)` collision with principal ideal

```text
P_r (1-zeta_256) Q_s
```

and norm `514p`. Then `O_514(p,r)` equals the number of diagonal Galois
orbits of profile-`(0,18)` shift/sign collision orbits having exact norm
`514p`.

Consequently the five-ideal occupancy target is equivalent to this
profile-specific exact norm-multiplicity statement:

```text
for every official p, at most five diagonal Galois orbits have norm 514p.
```

The count is independent of the chosen primitive row root `r`.
