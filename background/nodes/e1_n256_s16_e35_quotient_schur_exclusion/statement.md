# E1 N=256 square-mass-16 E=35 quotient-Schur exclusion

- **status:** PROVED
- **closure:** proof plus complete quotient and coupling censuses

Let `F` have folded profile `(3,4,0)` in the `N=256,s=5` band. There is no
pair-feasible collision at `V=70`. The exact slack recurrence gives

```text
E=V/2=35,       L=sum_(d=1)^63 |A_d|<=19.
```

Among the 21 integer autocorrelation magnitude profiles, only `(3,8)` and
`(6,5,1)` have an abstract layered third-moment cap above the cubic threshold
2162. A complete 2,946,287-allocation mod-16 quotient census gives

```text
profile/chamber                         cap
(3,8), odd outer, B outside 2Z         2010
(3,8), odd outer, B inside 2Z          2152
(3,8), divided outer                   2100
(6,5,1), outer AAA, odd/divided         460/454.
```

For `(6,5,1)`, the abstract terms other than `R(A,A,A)` and the impossible
two-point top-layer triple total 1704. Exactly four of 104,750 odd outer
allocations have `R(A,A,A)>458`; each has value 460. Exhausting all 276
compatible middle/top allocations for those four cases bounds their complete
three-layer objective by 2054. Every other odd allocation is at most
`458+1704=2162`, every divided allocation is at most `454+1704=2158`, and
every other magnitude profile is at most 2110.

Supports contained in `4 Z/128 Z` are excluded directly by the small-field
norm bound `54^32<2^250`. Thus every live row has

```text
M_3<=2162.
```

The exact rational cubic-Hermite certificate at contacts 14 and 57 has
positive margin at 2162 and negative margin at 2163. It puts the collision
norm below `2^250` and excludes `V=70`. Combined with the parent closures,
every unresolved profile-`(3,4,0)` vector has positive even `V<=68`.
