# L1 quotient-chart bounded core-boundary closure

- **status:** PROVED
- **role:** close bounded core boundary throughout each common-pencil strip
- **consumers:** `l1_mixed_residual_intersection_pin`,
  `l1_mixed_petal_amplification`, `petal_mixed_amplification`

## Statement

Work in one genuine quotient/coset source chart on a length-`n` row. Its
`M` petal fibers and `N` core fibers are disjoint complete fibers of the same
monic degree-`ell` polynomial `P`, so

```text
(M+N)ell<=n.                                           (BC1)
```

Assume the L1 lower cutoff and generated-field bounds

```text
ell>=c_0 n/log_2 n,       ell>2P_0,       q<=n^gamma  (BC2)
```

for fixed positive `c_0,gamma`. Restrict to one marked common-pencil strip

```text
p<=P_0,       beta(D)<=B_0,
m ell<d<(m+1)ell.                                     (BC3)
```

where `p` is polarized petal entropy and `beta(D)` is the canonical
partial-core-fiber boundary from
`l1_marked_common_pencil_quotient_boundary_router`.

Then the number of contributors in this one source chart is at most

```text
(P_0+1)(B_0+1) 2^(M+N) n^(P_0+B_0) q^(2P_0)
 <=(P_0+1)(B_0+1)
   n^(1/c_0+P_0+B_0+2 gamma P_0).                    (BC4)
```

In particular it is polynomial in `n`, with an exponent independent of the
strip index, defect degree, and cofactor excess. Thus an unowned
super-polynomial common-pencil family in quotient/coset charts cannot remain
in any fixed `(p,beta)` box in any degree strip.

## Scope

This is a per-source-chart closure. It does not aggregate first-match
multiplicity across source charts, cover a core not partitioned by `P`, treat
arbitrary petal locators, or bound families in which `p` or `beta(D)` escapes
every fixed cap.
