# Budget-three rate-half list intersection reduction

- **status:** PROVED
- **closure:** proof
- **consumer:** `rate_half_list_adjacent_crossing`

Let `C=RS[F,D,2d]` have length `n=4d`. Suppose four distinct codewords are
all listed by one received word at agreement at least

```text
a_0=3d-1.
```

Choose an `a_0`-point agreement set `S_i` for each codeword, and put
`m_x=#{i:x in S_i}` and `n_j=#{x:m_x=j}`. Then the only possible degree-count
patterns are

```text
(n_0,n_1,n_2,n_4) in {
  (0,0,4,0), (0,0,5,1), (0,0,6,2),
  (0,1,2,0), (0,1,3,1)
}.                                                        (B3I1)
```

After also imposing every individual agreement and every pairwise MDS cap,
these split into exactly six labeled incidence types up to relabeling the
four codewords:

| `(n_0,n_1,n_2,n_4)` | singleton labels | degree-two multigraph | types |
|---|---|---|---:|
| `(0,0,4,0)` | none | a 4-cycle, or a triangle with one pendant edge | 2 |
| `(0,0,5,1)` | none | `K_4` minus one edge | 1 |
| `(0,0,6,2)` | none | `K_4` | 1 |
| `(0,1,2,0)` | one isolated singleton | a two-edge path on the other three vertices | 1 |
| `(0,1,3,1)` | one isolated singleton | a triangle on the other three vertices | 1 |

Here a degree-two coordinate labeled `{i,j}` is an edge `ij`. The apparent
sixth degree-count pattern `(0,2,0,0)` is impossible after the individual
pair caps are imposed.

For any one of the six types, subtract codeword zero and form the matrix
`M(S_0,S_1,S_2,S_3)` with `3k` columns indexed by the coefficients of
`h_i=f_i-f_0`, `i=1,2,3`. At coordinate `x`, its row space imposes

```text
h_i(x)=0                         if 0,i in I_x,
h_i(x)-h_j(x)=0                 if i,j in I_x and 0 notin I_x,
I_x={i:x in S_i},                                      (B3I2)
```

using any spanning tree of these equalities. Then a four-codeword witness is
equivalent to a kernel vector for which `0,h_1,h_2,h_3` are pairwise
distinct. Every viable type has `8d-4` matrix rows before dependencies and
`6d` columns. Thus full column rank on all six official fixed-subgroup types
would prove `L_1(3d-1)<=3`.

Pairwise counting alone cannot establish that rank statement. On
`RS[F_17,mu_8,4]`, one explicit matrix of the `(0,1,2,0)` type has rank
`11<12` and its kernel gives four codewords at agreement five.

This theorem is a reduction and route fence. It does not determine the
official `B*=3` crossing.
