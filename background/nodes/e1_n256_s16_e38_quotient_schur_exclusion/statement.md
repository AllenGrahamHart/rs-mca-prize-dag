# E1 N=256 square-mass-16 E=38 quotient-Schur exclusion

- **status:** PROVED
- **closure:** proof plus complete finite quotient census

Let `F` have folded profile `(3,4,0)` in the `N=256,s=5` band, and
write

```text
E=V/2=sum_(d=1)^63 A_d^2,
L=sum_(d=1)^63 |A_d|.
```

There is no pair-feasible collision at `V=76`. Indeed, the exact slack
recurrence gives `E=38` and `L<=22`. Of the 32 possible autocorrelation
magnitude profiles, only

```text
(6,8),       (9,5,1),       (2,9)
```

have the abstract nested-layer third-moment cap above 2806. For symmetric,
zero-free nested layers, an exact mod-16 quotient census gives the following
caps whenever the outer support contains an odd distance:

```text
profile       group Z/128 Z       divided group Z/64 Z
(6,8)              2782                    2760
(2,9)              2580                    2422
|outer|=30          R(A,A,A)<=840           R(A,A,A)<=840.
```

For `(9,5,1)`, the remaining abstract layer terms total 1956 and its
two-point top layer `C={c,-c}` has `R(C,C,C)=0`; hence its total cap is
`840+1956=2796`. Every other magnitude profile has abstract cap at most
2668.

If the outer support is contained in `2 Z/128 Z` but not in
`4 Z/128 Z`, division by two preserves the Schur count and puts an odd
distance in `Z/64 Z`, so the second census column applies. Support contained
in `4 Z/128 Z` is impossible for a live `V=76` row by
`e1_n256_s16_autocorrelation_subfield_exclusion`. Consequently every live
candidate satisfies

```text
M_3<=2796<2806.
```

The exact rational cubic-Hermite certificate at contacts 14 and 57 closes
`V=76` for every `M_3<=2806`, placing the collision norm strictly below
`2^250`. Combined with the parent variance exclusion, every unresolved
profile-`(3,4,0)` vector therefore has positive even `V<=74`.
