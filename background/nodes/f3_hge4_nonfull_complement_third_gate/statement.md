# HGE4 non-full complement-third gate

- **status:** PROVED
- **consumer:** `f3_hge4_norm_gate_count`
- **dependencies:** `f3_hge4_exact_ratio_tower_orbit_compiler`,
  `f3_hge4_primitive_shift_pair_near_square_union_router`

Let `K` have characteristic zero or characteristic greater than `m`. Let
`P,Q in K[X]` be monic degree-`h` polynomials with disjoint, simple root sets
in `mu_m`, and suppose

```text
Q-P=d in K^*.
```

Assume the pair is non-full, so

```text
PQR=X^m-1,       c=deg R=m-2h>0.                    (CTG1)
```

Then

```text
h<=c,       equivalently 3h<=m.                     (CTG2)
```

For a dyadic order `m`, equality in `(CTG2)` is impossible. Consequently
every non-full exact-ratio primitive shift-pair orbit satisfies

```text
3h<m,
E_h^prim(m,p)=0                         whenever 3h>=m,  (CTG3)
```

and the exact-level HGE4 sum may be restricted to

```text
4<=h<=floor((m-1)/3).                               (CTG4)
```

This is a uniform analytic deletion. It does not prove the remaining
exact-level estimate or bound any width below the complement-third line.
