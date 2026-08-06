# Conditional F-4 minimal-record direct-column budget

- **status:** CONDITIONAL
- **closure:** proof of the printed implication

At every official `X4`/LIST corridor row, use the fixed quotient, dihedral,
moment-trade, U2-boundary, and DLI/skew first-owner strips.  For `h>=2`, let
`R_h^min` count the remaining width-`h` records in the established `u1`
direct-column convention satisfying

```text
e_j(P)=e_j(Q)  for 1<=j<=h-1.
```

Put `R_1^min=0` as a bookkeeping term and
`H_max=min(k+t,floor(n/2))`.  Conditional on the wired h=3 and h>=4 inputs,

```text
R_min
 = R_1^min + R_2^min + R_3^min
   + sum_(h=4)^H_max R_h^min
 < 16n^3.
```

This is a budget for F-4 minimal records only.  It does not assert that every
general order-`t` primitive star-PTE record is minimal, nor that `R_min`
equals the post-strip primitive exact-list residue.  The separate target
`x4_primitive_star_u1_coverage` owns that coverage and multiplicity theorem.
