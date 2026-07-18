# Budget-three split-fiber atlas

- **status:** PROVED
- **closure:** proof
- **consumer:** `rate_half_list_adjacent_crossing`

Work in the six-type split-pencil normal form and keep the pair order

```text
01,02,03,12,13,23.
```

Write `p_ij=deg e_ij`, let `delta_ij` be the slack in `(SP1)`, and let

```text
c_i=[X^(2d-1)]f_i.
```

Then every edge degree is exact up to the printed one-bit slack:

```text
deg b_ij=p_ij+deg q_ij,

delta_ij=0  ==>  deg q_ij=0 and c_i!=c_j,
delta_ij=1  ==>  deg q_ij=0 iff c_i=c_j,
                    deg q_ij=1 iff c_i!=c_j.       (SF1)
```

Consequently the complete six-type ledger has only the following thirteen
possible degree chambers. A row lists all possible sextuples `deg b_ij`; it
does not assert that every chamber is realized.

| type | possible `deg b` sextuples |
|---|---|
| pendant | `(0,0,1,1,1,2)`, `(0,0,1,1,2,1)`, `(0,0,1,1,2,2)` |
| 4-cycle | `(0,1,1,1,1,0)`, `(0,1,1,1,1,1)`, `(1,1,1,1,1,0)`, `(1,1,1,1,1,1)` |
| `K_4-e` | `(0,1,1,1,1,1)`, `(0,1,1,1,1,2)` |
| `K_4` | `(1,1,1,1,1,1)` |
| path + singleton | `(0,1,0,1,0,0)`, `(0,1,0,1,0,1)` |
| triangle + singleton | `(1,1,0,1,0,0)` |

In particular, at least one of `b_13,b_23` is genuinely quadratic in the
pendant type.

There is also a split-fiber compiler. Whenever a triangle `ijk` has
`delta_ij=delta_ik=delta_jk=0` and the three displayed products have common
degree `h`, `(SP2)` is a constant-coefficient relation among

```text
A_k e_ij,  A_i e_jk,  A_j e_ik.                    (SF2)
```

These are three distinct, pairwise-coprime, monic degree-`h` polynomials,
each split over a disjoint part of the evaluation domain. The complete atlas
of such triangles is

| type | triangles of degree `d` | triangles of degree `d-1` |
|---|---|---|
| pendant | none | `012` |
| 4-cycle | none | none |
| `K_4-e` | none | `012,013` |
| `K_4` | none | `012,013,023,123` |
| path + singleton | `012` | `013` |
| triangle + singleton | `012` | `013,023,123` |

For a gcd-trivial constant pencil on `D`, a domain point is a root of at most
one projective member. Hence the number of degree-`h` members split completely
over `D` is at most

```text
floor(4d/h).                                        (SF3)
```

Thus every degree-`d` pencil in the table already uses three of at most four
split members. For `d>=6`, the same is true for degree `d-1`; in particular it
holds on the power-of-two official scales with `d>=8`. The cycle is the unique
incidence type with no deficit-free three-member split pencil. This theorem
does not classify the remaining member, couple the printed pencils, or locate
the budget-three adjacent crossing.
