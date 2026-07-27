# DSP8 nodal cube-preimage envelope

- **status:** PROVED
- **closure:** proof
- **consumer:** `f3_h3_dsp8_correlation_bound`
- **dependencies:** `f3_h3_dsp8_nodal_trace_parameter_router`,
  `f3_affine_coset_pair_mattarei_bound`

Let `g=gcd(3,p-1)`, so `g` is `1` when `p=2 (mod 3)` and `3` when
`p=1 (mod 3)`. Define the cube-preimage subgroup

```text
K={x in F_p^*:x^3 in H},       |K|=gn.              (NCE1)
```

Across all singular traces `sigma=3c`, the nonnode ordered subgroup points
are in exact bijection with

```text
{theta in K:1+theta in K,
 theta notin {0,-1}, theta^2+theta+1!=0}.            (NCE2)
```

If `N_sing` is the total number of ordered subgroup points over every
singular trace, including nodes, then

```text
N_sing<C_M(gn)^(2/3)+1,       C_M=3*2^(-2/3).      (NCE3)
```

Let `G_sing^0,G_sing^A` be the raw nodal DSP8 records from the trace-curve
router. Then

```text
G_sing^0+G_sing^A
 <C_M n^(2/3)(C_M(gn)^(2/3)+1)^2.                  (NCE4)
```

Consequently, on every official row,

```text
10G_sing^0+17G_sing^A <116n^2    if p=2 (mod 3),
10G_sing^0+17G_sing^A <498n^2    if p=1 (mod 3).    (NCE5)
```

This replaces the former class-weighted constants `552` and `2387` by `116`
and `498`. In particular the three-cubic-root nodal locus now fits inside the
live uniform `G=4K` allowance `48536/25=1941.44`, leaving more than
`1443n^2` for smooth traces. It does not close DSP8: the smooth slice and its
quotient-weighted correlation remain open. The older `892` constant was the
former stronger `J=G` target used by F-round 1, not the current sufficient
allowance.
