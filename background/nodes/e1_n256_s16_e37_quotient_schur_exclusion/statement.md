# E1 N=256 square-mass-16 E=37 quotient-Schur exclusion

- **status:** PROVED
- **closure:** proof plus complete finite quotient censuses

Let `F` have folded profile `(3,4,0)` in the `N=256,s=5` band. There is no
pair-feasible collision at `V=74`. The exact slack recurrence gives

```text
E=V/2=37,       L=sum_(d=1)^63 |A_d|<=21.
```

Among the 29 integer autocorrelation magnitude profiles, only
`(5,8)`, `(8,5,1)`, and `(1,9)` have an abstract layered third-moment cap
above the cubic threshold 2592. A complete mod-16 quotient census gives

```text
profile       Z/128 Z       divided Z/64 Z
(5,8)           2626              2576
(1,9)           2372              2168
|outer|=28       678               678.
```

The apparent 2626 obstruction has its weight-two layer `B` inside
`4 Z/128 Z`. If `B` is not so contained, the exact chamber maximum is 2576.
If `B` is contained there, division by four reduces its cubic Schur count to
a 6,435-set census in `Z/32 Z`, where `R(B,B,B)<=174`; maximizing the refined
full expression over every such quotient allocation gives 2560.

For `(8,5,1)`, the abstract terms other than `R(A,A,A)` and the impossible
two-point top-layer triple total 1872, so its cap is `678+1872=2550`.
Every other profile is at most 2474. Supports contained in
`4 Z/128 Z` are excluded directly by the small-field norm bound
`58^32<2^250`. Thus every live row has

```text
M_3<=2576<2592.
```

The exact rational cubic-Hermite certificate at contacts 14 and 57 has
positive six-bit margin at 2592 and negative margin at 2593. It puts the
collision norm below `2^250` and excludes `V=74`. Combined with the parent
closures, every unresolved profile-`(3,4,0)` vector has positive even
`V<=72`.
