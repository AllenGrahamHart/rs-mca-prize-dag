# XR rank-two extension-family collision ledger

- **status:** PROVED
- **closure:** proof
- **consumer:** `xr_highcore_collision_count`
- **dependencies:** `xr_higher_rank_rank_two_shell_maxwell_router`,
  `xr_rank_two_actual_block_extension_router`

Use a rank-two shell

```text
|X|=a+d+1,       S_i=X\Z_i,
```

where the `Z_i` are pairwise disjoint and `z_i=|Z_i|`. Let an actual selected
block be

```text
A_i=S_i disjoint_union T_i,
T_i subset E_i,       |T_i|=tau_i=h-d-1+z_i.         (EC1)
```

Split its inactive extension canonically as

```text
I_i=T_i intersect Z_i,       O_i=T_i\X.              (EC2)
```

Then, for every pair `i!=j`,

```text
|A_i intersect A_j|
 =a+d+1-z_i-z_j+|I_i|+|I_j|+|O_i intersect O_j|.    (EC3)
```

Consequently the selected-block cap `|A_i intersect A_j|<=a` is equivalent
to the exact pair budget

```text
|I_i|+|I_j|+|O_i intersect O_j|<=ell_ij,
ell_ij=z_i+z_j-d-1.                                  (EC4)
```

The shell inequalities guarantee `ell_ij>=0`. If `ell_ij=0`, both inside
reuse sets are empty and the two outside extensions are disjoint.

There is also an exact aggregate ledger. Put

```text
Z=sum_i z_i,
m_x=|{i:x in O_i}|                         for x outside X.
```

Summing `(EC4)` over all pairs gives

```text
(t-1)sum_i|I_i|+sum_(x outside X) C(m_x,2)
 <=(t-1)Z-C(t,2)(d+1).                              (EC5)
```

Thus, for fixed supports and external zero sets, compatible actual extension
families are exactly the choices

```text
I_i subset E_i intersect Z_i,
O_i subset E_i\X,
|I_i|+|O_i|=tau_i                                   (EC6)
```

satisfying `(EC4)` for every pair. This is a complete finite extension-family
compatibility ledger.

The theorem does not enumerate coefficient-compatible supports, bound the
number of solutions of `(EC4)--(EC6)`, choose a first Maxwell core, classify
higher trade rank or nonuniform cells, or pay the cross-core slope aggregate.
