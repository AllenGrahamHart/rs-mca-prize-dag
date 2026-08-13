# E1 profile-(4,4) official energy-at-most-four exclusion

- **status:** PROVED
- **closure:** exhaustive exact cyclotomic-resultant certificate
- **scope:** binding prize rate-`1/8` row, profile `(4,4,S=20)`
- **consumer:** `e1_profile44_energy_floor_cofactor_contraction`

Let

```text
alpha=F(zeta_256)=sum_(i=0)^127 c_i zeta_256^i
```

have four coefficients of magnitude two and four coefficients of magnitude
one. In `Z[X]/(X^128+1)`, write

```text
F(X)F(X^-1)-20=sum_(d=1)^63 A_d(X^d-X^(128-d)),
E=sum_(d=1)^63 A_d^2.
```

Suppose the norm of `alpha` has the official collision form

```text
|Norm(alpha)|=p m,
B_P 2^128 <= p < (B_P+1)2^128,
```

where `p` is the row prime and `m` is one of the `1133` cofactors left by
the exact profile-`(4,4)` local-norm sieve. Then

```text
E>=5.                                                   (P44-E)
```

Equivalently, the conjugate-square variance `V=2E` satisfies `V>=10`.

The certificate exhausts every abstract integer autocorrelation spectrum of
energy at most four, whether or not that spectrum is realizable by a profile
vector:

```text
E=1:       126 spectra
E=2:      7812 spectra
E=3:    317688 spectra
E=4:   9530766 spectra
```

No energy-`1`, `2`, or `3` norm has a legal cofactor and official-interval
quotient. No energy-`4` norm even has an integer cofactor whose quotient lies
in the official interval.

This does not count the vectors with `E>=5`, pay the profile, or close the
official pair budget.

## Falsifier

An energy-at-most-four profile vector whose exact cyclotomic norm equals
`p m` for an official-interval prime `p` and one of the `1133` legal
cofactors, or a missing integer spectrum in the four displayed counts.
