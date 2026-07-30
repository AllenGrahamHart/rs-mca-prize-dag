# E1 profile-(4,4) local-norm route fence

- **status:** PROVED
- **closure:** exact Hasse census, norm ceiling, and residue-degree sieve
- **scope:** binding prize rate-`1/8` row, profile `(4,4,S=20)`
- **consumer:** `e1_official_low_square_mass_pair_budget`

Let `zeta=zeta_256`, `pi=1-zeta`, and let

```text
alpha=sum_(i=0)^127 c_i zeta^i
```

have exactly four coefficients of magnitude two and four coefficients of
magnitude one. Suppose an official row prime `p` divides
`R=|Norm(alpha)|`, and write `R=p m`. Then

```text
m <= 1707433,
mu=v_pi(alpha)=v_2(m)
   in {1,2,3,4,5,6,8,9,10,12,16,17,18,20},          (P44-1)
m=2^mu(1+256t),                                      (P44-2)
```

for an integer `t>=0`.

Imposing also the necessary cyclotomic residue-degree condition

```text
ord_256(q) divides v_q(m) for every odd prime q|m    (P44-3)
```

leaves exactly `1133` cofactor values. Their counts by `mu` are

```text
mu:       1   2   3  4  5  6  8  9 10 12 16 17 18 20
count:  533 285 155 78 42 23  4  4  3  2  1  1  1  1.
```

In particular, all fourteen pure powers `2^mu` in `(P44-1)` survive these
necessary sieves.

This is a route fence, not a collision lower bound. None of the `1133`
cofactors is asserted to occur at an official row. It shows that local
valuation, local reciprocity, the field floor, and residue degrees do not by
themselves reduce the profile to its required allowance of seven complete
shift/sign orbits. A closing proof must add a profile-specific norm,
autocorrelation, resultant, or collective ideal-occupancy argument.

## Falsifier

A profile-`(4,4)` collision violating `(P44-1)--(P44-3)`, or an exact replay
of the stated necessary sieves with a survivor count other than `1133`.
