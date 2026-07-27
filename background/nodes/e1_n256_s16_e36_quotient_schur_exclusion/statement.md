# E1 N=256 square-mass-16 E=36 quotient-Schur exclusion

- **status:** PROVED
- **closure:** proof plus two complete finite censuses

Let `F` have folded profile `(3,4,0)` in the `N=256,s=5` band. There is no
pair-feasible collision at `V=72`. The exact slack recurrence gives

```text
E=V/2=36,       L=sum_(d=1)^63 |A_d|<=20.
```

Among the 26 integer autocorrelation magnitude profiles, only `(4,8)`,
`(0,9)`, and `(7,5,1)` have an abstract layered third-moment cap above the
cubic threshold 2377. A complete mod-16 quotient census gives

```text
profile/chamber                     cap
(4,8), odd outer, B outside 2Z     2208
(4,8), odd outer, B inside 2Z      2344
(4,8), divided outer               2332
(0,9), odd outer                   2000
(0,9), divided outer               1924
|outer|=26, odd/divided             556/540.
```

The inner-layer refinement uses a separate complete census of all
`binom(31,8)=7,888,725` symmetric 16-point subsets of `Z/64 Z` avoiding 0
and 32. It proves `R(B,B,B)<=174`.

For `(7,5,1)`, the abstract terms other than `R(A,A,A)` and the impossible
two-point top-layer triple total 1788, so its odd-support cap is
`556+1788=2344`. Every other profile is at most 2288. Supports contained in
`4 Z/128 Z` are excluded directly by the small-field norm bound
`56^32<2^250`. Thus every live row has

```text
M_3<=2344<2377.
```

The exact rational cubic-Hermite certificate at contacts 14 and 57 has
positive margin at 2377 and negative margin at 2378. It puts the collision
norm below `2^250` and excludes `V=72`. Combined with the parent closures,
every unresolved profile-`(3,4,0)` vector has positive even `V<=70`.
