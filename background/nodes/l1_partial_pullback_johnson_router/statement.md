# L1 partial-pullback Johnson router

- **status:** PROVED
- **role:** pay arbitrary anchored polynomial pullbacks when partial-fiber
  agreement and sparse-coverage losses remain on the Johnson side
- **consumers:** `l1_mixed_residual_intersection_pin`,
  `l1_mixed_petal_amplification`, `petal_mixed_amplification`

## Setup

Work over a field of order `q` with a length-`n` evaluation domain, dimension
`k`, source-petal size `ell=sigma+1`, and threshold

```text
a_*=k+ell-1.                                           (PJ1)
```

Fix a monic degree-`s` map `P`. Let `B` be the labels of all complete
`s`-point `P`-fibers in the domain and put

```text
b=|B|,       K_0=ceil(k/s),       d=K_0-1,
k_j=max(0,ceil((k-j)/s)),
kappa=sum_(j=0)^(s-1) max(0,k_j-b).                   (PJ2)
```

For a listed codeword `f`, let `E_f subset B` be the labels on whose complete
fibers `f` agrees with the received word everywhere. Define the partial loss

```text
z(f)=|Agr(f,U)\disjoint_union_(a in E_f) T_a|.         (PJ3)
```

This counts every agreement in an incomplete domain fiber and every agreement
inside a complete fiber that is not fully agreed.

## Router

For any cap `Z>=0`, put

```text
h_Z=max(0,ceil((a_*-Z)/s)).                            (PJ4)
```

If

```text
h_Z^2>b d,                                             (PJ5)
```

then for every fixed `P`,

```text
#{f:|Agr(f,U)|>=a_*, z(f)<=Z}
 <=q^kappa floor(b(h_Z-d)/(h_Z^2-bd))
 <=q^kappa b^2.                                       (PJ6)
```

If the map carries a whole fixed-source petal, is tame in the sense of
`l1_tame_fixed_petal_refinement_census`, `kappa<=K` for a fixed constant,
and `q<=n^gamma`, then the aggregate across every such map is at most

```text
n q^K b^2 <= n^(3+gamma K).                           (PJ7)
```

## Scope

This theorem itself leaves the nonpositive gate `h_Z^2<=bd`, unbounded
`kappa`, maps without a whole-petal anchor, and wild fixed-petal
decompositions. The later `l1_pullback_coverage_kernel_tradeoff` proves that
`kappa<=max(0,z-ell+1)`, so it is not an independent escape. This router does
not infer that `z` is bounded. The
`F_17^*` affine-quadratic obstruction has `z=5`, `kappa=0`, and lies on the
nonpositive side, so it is not removed by this router.
