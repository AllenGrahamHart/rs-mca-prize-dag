# E1 high-cofactor Schinzel height collapse

- **status:** PROVED
- **closure:** sharp entropy bound plus Schinzel's totally real height theorem
- **dependencies:** `e1_pure_cofactor_common_prime_associate_router`,
  `e1_conductor256_full_unit_circular_basis`, and
  `e1_conductor256_character_eigenvalue_preflight`
- **consumer:** `e1_official_low_square_mass_pair_budget` (evidence)

Fix one prize-envelope row, one primitive quotient root, and one of the
profile-`(3,6,S=18)` cofactors

```text
m=2^mu in {4,8,16},       mu in {2,3,4}.
```

All live collisions in this fixed cofactor form at most one orbit under the
`256` negacyclic shift/sign associates. Equivalently, if `alpha` and `beta`
are two such collisions and `beta=u alpha`, then `u` is a root of unity.
Consequently the three high-cofactor branches contribute at most three
torsion orbits in total.

The numerical separation is explicit. For either collision put

```text
z_a=|alpha(zeta_256^a)|^2/18,       a in (Z/256Z)^x/{+-1}.
```

Then

```text
sum_a z_a=64,
D=-sum_a log z_a=log(18^64/(2^mu p))<6.845.          (SHC1)
```

For every positive 64-vector satisfying `(SHC1)`, the certified entropy
extremum proves

```text
sum_a |log z_a| < 30.645.                            (SHC2)
```

It follows that

```text
||lambda(u)||_1 < 61.29.                             (SHC3)
```

On the other hand, the full-unit theorem writes `u=zeta_256^j v` with `v`
a totally real algebraic unit. If `u` is not torsion, then `v!=+-1` and
Schinzel's theorem gives

```text
h(v) >= (1/2)log((1+sqrt(5))/2),
||lambda(u)||_1=256h(v)
                    >=128log((1+sqrt(5))/2)>61.595.  (SHC4)
```

This contradicts `(SHC3)`.

The cofactor `2` branch is not covered: its worst-case deficit is below
`7.539`, for which this entropy-height comparison does not separate. The
node neither proves any high-cofactor collision exists nor pays lower
profiles or closes E1.

## Falsifier

Two fixed-row, fixed-root collisions in one cofactor `4`, `8`, or `16` that
are not negacyclic shift/sign associates; a positive 64-vector violating
`(SHC2)` under `(SHC1)`; or a non-torsion unit violating `(SHC4)`.
