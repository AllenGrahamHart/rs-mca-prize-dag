# KoalaBear m12 outer normal-form compiler

- **status:** PROVED
- **scope:** both surviving inner-degree-12 transverse outer types
- **dependencies:** `rate_half_kb_m12_outer_subdegree_route_cut`,
  `rate_half_kb_m12_r4_low_genus_branch_profile_reduction`
- **consumer:** `rate_half_band_closure`

Over the algebraic closure, every live degree-five outer map is affine
equivalent in source and target to one of the following forms:

```text
r=2, D5:
  D5(x,a)=x^5-5a*x^3+5a^2*x,                    a!=0

r=4, A5, finite types (3),(2,2):
  x^3(12x^2-15(1+t)x+20t),       3t^2+4t+3=0

r=4, A5, finite types (3),(3):
  x^3(6x^2-15x+10)

r=4, S5, finite types (2),(3,2):
  x^3(x-1)^2

r=4, S5, finite types (2),(4):
  x^4(5-4x)

r=4, S5, finite types (2),(2),(2,2):
  x^2(x-1)^2(2x-5t),             t in algebraic closure,
```

where the last parameter is restricted to the open locus with exactly the
printed branch profile. Thus the arbitrary outer quintic is replaced by
five rigid affine classes plus one one-parameter family.

For the Dickson form, if `s^2=5`, the off-diagonal divided difference
factors into the two surviving bidegree-`(2,2)` components:

```text
[x^2+((1+s)/2)xy+y^2+((-5+s)/2)a]
[x^2+((1-s)/2)xy+y^2+((-5-s)/2)a].                 (KBN-1)
```

This compiler does not assert that any family is empty or realized by an
endpoint record. It does not close `r=2`, `r=4`, `m=12`, construct an owner,
move the ledger, close `u=2`, establish cap `68`, or close the KoalaBear row.

## Falsifier

A surviving tame degree-five outer map not geometrically affine-equivalent
to one of the six printed families, or failure of `(KBN-1)`.
