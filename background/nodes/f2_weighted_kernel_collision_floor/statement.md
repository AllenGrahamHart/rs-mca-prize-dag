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

After identifying the image with `F_p^d`, let `a_s` be the syndrome column
at coordinate `s` and let `chi(x)=exp(2 pi i x/p)`. Then also

```text
Z(A)=p^-d sum_(u in F_p^d) prod_s (1+cos(2 pi <u,a_s>/p))
    =(2^m/p^d) sum_u prod_s cos^2(pi <u,a_s>/p).       (FLOOR-3)
```

For every nonempty fiber, `N(v)` is also the full-agreement list-recovery
output size of the linear code `K` with two allowed symbols at every
coordinate. The theorem is pointwise for every linear map; it is not an
ensemble heuristic and supplies no upper bound on `Z(A)`.

## Addendum (2026-08-07, wave-47 integration, coordinator)

Citation correction (CATCH-47F-3): the collision identity
(FLOOR-1) is BANKED prior art (dli_c1_l1_block_owner_ledger:15,18,
as canonical's z1_ternary_mass already records: "BANKED — the
collision identity is NOT ours"); this node's contribution is its
deployment here, not the identity. The "does not inherit its row
classification" distinction is struck as hollow (canonical's
Z-FLOOR was already hypothesis-free).
