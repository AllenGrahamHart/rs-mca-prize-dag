# DSP8 nodal cube-preimage envelope

- **status:** PROVED
- **closure:** proof
- **consumer:** `f3_h3_dsp8_correlation_bound`
- **dependencies:** `f3_h3_dsp8_nodal_trace_parameter_router`,
  `f3_affine_coset_pair_cubic_preimage_stepanov`

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
N_sing<(51/16)(gn)^(2/3)+1.                         (NCE3)
```

Let `G_sing^0,G_sing^A` be the raw nodal DSP8 records from the trace-curve
router. Then

```text
G_sing^0+G_sing^A
 <(51/16)n^(2/3)((51/16)(gn)^(2/3)+1)^2.            (NCE4)
```

Consequently, on every official row,

```text
10G_sing^0+17G_sing^A < 552n^2    if p=2 (mod 3),
10G_sing^0+17G_sing^A <2387n^2    if p=1 (mod 3).   (NCE5)
```

This replaces the former class-weighted leading constant `29376` by a
uniform constant below `2387`, and by `552` in the one-cubic-root case. It
does not close DSP8: smooth traces remain, and the three-cubic-root nodal
constant still exceeds the live uniform `G=4K` allowance
`76599/40=1914.975`. The older `892` constant was the former stronger
`J=G` target used by F-round 1, not the current sufficient allowance.
