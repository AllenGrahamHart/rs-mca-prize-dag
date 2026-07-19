# Budget-three antipodal pure-quartic degree rigidity

- **status:** PROVED
- **closure:** proof
- **consumer:** `rate_half_list_adjacent_crossing`
- **dependency:** `rate_half_list_budget_three_antipodal_pencil_degree_floor`

Retain the centered antipodal quotient pencil

```text
G_i=U+c_iV,       deg U=r,       v=deg V<=r-1,
sum_i c_i=0,
D(Y) product_i G_i(Y)=Y^d-1,     d=4r+4.              (PQ1)
```

Assume the base-field characteristic is zero or exceeds `d`.

Write `e_j` for the elementary symmetric functions of the four `c_i`.
On the pure-quartic parameter stratum

```text
e_2=e_3=0,                                             (PQ2)
```

one has the exact degree identity

```text
v=r-1.                                                 (PQ3)
```

There is also a nonzero linear polynomial `L` such that, for
`A=DU^4` and `B=e_4DV^4`,

```text
A'B''-A''B'=Y^(d-2) U^2 V^2 L,       deg L=1.          (PQ3')
```

Both `U` and `V` are squarefree. In addition,

```text
#(Z(UV) intersect (Z(D) union {0}))<=1.                (PQ3'')
```

If this intersection is nonempty, its unique point is the root of `L`.

On the maximal official row this reads

```text
r=2^37-1,       deg V=2^37-2.                          (PQ4)
```

Thus the stratum in which the centered outer quartic has only fourth-power
terms has no genuine degree gap: its two pencil directions differ in degree
by exactly one, both are squarefree, and its remaining differential residual
is linear. The theorem does not exclude that final codimension-one degree
stratum.
