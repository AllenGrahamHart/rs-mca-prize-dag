# F2 weighted-kernel collision floor

- **status:** PROVED
- **closure:** proof

Let `A:F_p^m -> V` be an `F_p`-linear map of rank `d`, put `K=ker(A)`,
and define

```text
Z(A)=sum_(eps in K intersect {-1,0,1}^m) 2^-wt(eps).
```

For the subset-syndrome map `Phi(S)=A 1_S`, let
`N(v)=#{S subset {1,...,m}:Phi(S)=v}`. Then

```text
2^m Z(A) = sum_v N(v)^2,                              (FLOOR-1)
Z(A) >= max(1, 2^m/p^d).                             (FLOOR-2)
```

For every nonempty fiber, `N(v)` is also the full-agreement list-recovery
output size of the linear code `K` with two allowed symbols at every
coordinate. The theorem is pointwise for every linear map; it is not an
ensemble heuristic and supplies no upper bound on `Z(A)`.
