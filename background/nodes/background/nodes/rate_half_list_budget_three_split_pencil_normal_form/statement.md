# Budget-three split-pencil normal form

- **status:** PROVED
- **closure:** proof
- **consumer:** `rate_half_list_adjacent_crossing`

Assume the four-codeword predecessor witness and selected supports from
`rate_half_list_budget_three_intersection_reduction`. Label the six unordered
pairs in the order

```text
01,02,03,12,13,23.
```

Let `T_i` be the coordinates whose selected incidence triple omits codeword
`i`, let `E_ij` be the coordinates of selected incidence degree two labeled
`{i,j}`, let `F` be the degree-four coordinates, and let `S` be the singleton
coordinates. Write their monic locators as

```text
A_i=Lambda_(T_i),   e_ij=Lambda_(E_ij),
J=Lambda_F,         W=Lambda_S.
```

For `g_ij=f_j-f_i` and `{k,l}={0,1,2,3}\{i,j}`, there is a nonzero polynomial
`q_ij`, with `q_ji=-q_ij`, such that

```text
g_ij = J A_k A_l e_ij q_ij,
deg q_ij <= delta_ij,
delta_ij=(2d-1)-|S_i intersect S_j|.                 (SP1)
```

Put `b_ij=e_ij q_ij`. For every ordered triple of distinct indices, with the
orientation inherited from `g_ij+g_jk=g_ik`, cancellation gives

```text
A_k b_ij + A_i b_jk = A_j b_ik.                     (SP2)
```

The six incidence types give the following complete constant-degree ledger.
Tuples `p`, `delta`, and `p+delta` use the fixed pair order above; `p_ij` is
`|E_ij|`, and `t-d` lists `|T_i|-d`.

| type | singleton labels | `p` | `t-d` | `delta` | `deg b <= p+delta` |
|---|---|---|---|---|---|
| pendant | `(0,0,0,0)` | `(0,0,1,1,1,1)` | `(-2,-1,-1,0)` | `(0,0,0,0,1,1)` | `(0,0,1,1,2,2)` |
| 4-cycle | `(0,0,0,0)` | `(0,1,1,1,1,0)` | `(-1,-1,-1,-1)` | `(1,0,0,0,0,1)` | `(1,1,1,1,1,1)` |
| `K_4-e` | `(0,0,0,0)` | `(0,1,1,1,1,1)` | `(-2,-2,-1,-1)` | `(0,0,0,0,0,1)` | `(0,1,1,1,1,2)` |
| `K_4` | `(0,0,0,0)` | `(1,1,1,1,1,1)` | `(-2,-2,-2,-2)` | `(0,0,0,0,0,0)` | `(1,1,1,1,1,1)` |
| path + singleton | `(0,0,0,1)` | `(0,1,0,1,0,0)` | `(-1,-1,0,-1)` | `(0,0,0,0,0,1)` | `(0,1,0,1,0,1)` |
| triangle + singleton | `(0,0,0,1)` | `(1,1,0,1,0,0)` | `(-1,-1,-1,-2)` | `(0,0,0,0,0,0)` | `(1,1,0,1,0,0)` |

In particular, four types have only constant/linear `b_ij`; the pendant type
has two possible quadratics and `K_4-e` has one. The block locators also obey

```text
Lambda_D = W J A_0 A_1 A_2 A_3 product_(i<j)e_ij,   (SP3)

product_(i<j)Lambda_(S_i intersect S_j)
  * W^3 * product_(i<j)e_ij^2
  = Lambda_D^3 J^3.                                  (SP4)
```

Thus the official B*=3 question is a base-field-normalized split-pencil
problem with four large disjoint subgroup blocks and at most quadratic edge
coefficients. This is a reduction, not a proof that the pencil is absent.
