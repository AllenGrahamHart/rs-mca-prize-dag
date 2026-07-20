# L1 quotient-chart bipolar entropy closure

- **status:** PROVED
- **role:** close bounded petal and symmetric core polarity per source chart
- **consumers:** `l1_mixed_residual_intersection_pin`,
  `l1_mixed_petal_amplification`, `petal_mixed_amplification`

## Statement

Use one genuine quotient/coset common-pencil source chart with `M` complete
petal fibers and `N` complete core fibers of degree `ell`, so

```text
(M+N)ell<=n.                                           (BE1)
```

For exact petal supports `S_i` and exact missed-core set `D`, define the two
polarized entropies

```text
p_pet=sum_(petals i) min(|S_i|,ell-|S_i|),
p_core=sum_(core fibers T_a) min(|D intersect T_a|,
                                  ell-|D intersect T_a|).   (BE2)
```

Assume fixed bounds and the L1 cutoff

```text
p_pet<=P_0,       p_core<=B_0,
ell>=c_0 n/log_2 n,       ell>2P_0,       q<=n^gamma. (BE3)
```

Across every degree strip and every cofactor excess, the number of
common-pencil contributors in this source chart is at most

```text
(P_0+1)(B_0+1) 2^(M+N) n^(P_0+B_0) q^(2P_0)
 <=(P_0+1)(B_0+1)
   n^(1/c_0+P_0+B_0+2 gamma P_0).                    (BE4)
```

Thus a super-polynomial fixed-chart common-pencil family at the L1 cutoff
must have `p_pet` or `p_core` escape every fixed cap. This strictly sharpens
the one-sided partial-fiber-boundary pin: an almost-full core fiber costs only
its missing points in `p_core`, not all of its selected points.

## Scope

The theorem is per source chart and assumes both petals and core use the same
complete quotient fibers. It does not aggregate first-match multiplicity
across source charts or treat non-quotient cores and arbitrary petal locators.

