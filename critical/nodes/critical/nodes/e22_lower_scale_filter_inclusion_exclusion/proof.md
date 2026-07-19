# proof: e22_lower_scale_filter_inclusion_exclusion

Let `U=U_{i,j}` be the finite residual-profile universe for the dyadic pair
`M_i<M_j`. For each smaller dyadic scale `M'<M_i`, define

```text
A_{M'} = {R in U : |B_{M'}(R)| < M'}.
```

The tail-minimality condition for selecting `M_i` says precisely that none of
these smaller-scale admissibility events occurs:

```text
R is minimal at M_i
    iff R in U \ union_{M'<M_i} A_{M'}.
```

Finite inclusion-exclusion gives the indicator identity

```text
1_{U \ setminus union A_{M'}}
  = sum_{S subset Smaller(M_i)}
      (-1)^|S| 1_{intersection_{M' in S} A_{M'}},
```

with the convention that the empty intersection is `U`.

Multiplying this pointwise identity by any declared nonnegative integer
multiplicity weight `w(R)` and summing over `U` gives

```text
W(minimal profiles)
  = sum_S (-1)^|S| W(intersection_{M' in S} A_{M'}).
```

This proves that the lower-scale filter is formal inclusion-exclusion once
the weighted intersection counts are known.
