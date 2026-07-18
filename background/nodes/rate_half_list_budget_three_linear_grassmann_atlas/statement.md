# Budget-three linear Grassmann atlas

- **status:** PROVED
- **closure:** proof
- **consumer:** `rate_half_list_adjacent_crossing`

Among the thirteen edge-degree chambers in the split-fiber atlas, exactly
nine have `deg b_ij<=1` on all six edges:

```text
4-cycle:                 4 chambers,
K_4-e:                   1 chamber,
K_4:                     1 chamber,
path plus singleton:     2 chambers,
triangle plus singleton: 1 chamber.                 (LGA1)
```

For every such chamber over a field of odd characteristic, the Plucker
bivector is a projective line on `Gr(2,4)`:

```text
B(X)=sum_(i<j)b_ij(X)e_i wedge e_j
    =w wedge (u+Xv),                                 (LGA2)
```

where `w,u,v` are linearly independent base-field vectors. The locator vector
`A=(A_0,A_1,A_2,A_3)` lies in the moving plane `<w,u+Xv>` and hence obeys
one constant base-field relation. Its exact form by chamber is:

| type | chambers | nonzero relation support | `deg(A_0,A_1,A_2,A_3)` | exceptional degree |
|---|---:|---|---|---:|
| 4-cycle | 4 | `0123` | `(d-1,d-1,d-1,d-1)` | 4 |
| `K_4-e`, linear | 1 | `0123` | `(d-2,d-2,d-1,d-1)` | 6 |
| `K_4` | 1 | `0123` | `(d-2,d-2,d-2,d-2)` | 8 |
| path plus singleton | 2 | `013` | `(d-1,d-1,d,d-1)` | 3 |
| triangle plus singleton | 1 | `0123` | `(d-1,d-1,d-1,d-2)` | 5 |

Here support `0123` means

```text
lambda_0A_0+lambda_1A_1+lambda_2A_2+lambda_3A_3=0,
lambda_0lambda_1lambda_2lambda_3!=0,                (LGA3)
```

with no proper vanishing subsum. In the path type the annihilator is the
already-printed tight-triangle relation

```text
lambda_0A_0+lambda_1A_1+lambda_3A_3=0,
lambda_0lambda_1lambda_3!=0.                         (LGA4)
```

In every row, if `E` is the product of its singleton, full, and edge
locators, then

```text
Lambda_D=E A_0A_1A_2A_3                             (LGA5)
```

and `deg E` is the exact value in the table.

Consequently nine chambers are base-field split-unit equations with at most
eight exceptional roots. The only edge chambers not covered by `(LGA2)` are
the three pendant chambers and the quadratic `K_4-e` chamber. Those four
have a genuinely quadratic edge and remain Plucker-conic problems. This
classification does not exclude any chamber.
