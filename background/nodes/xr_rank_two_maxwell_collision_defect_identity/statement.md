# XR rank-two Maxwell collision-defect identity

- **status:** PROVED
- **closure:** proof
- **consumer:** `xr_highcore_collision_count`
- **dependencies:** `xr_higher_rank_rank_two_shell_maxwell_router`,
  `xr_rank_two_extension_family_collision_ledger`

Use a compatible actual extension family on a rank-two shell, with notation
from the extension-family collision ledger. Put

```text
I=sum_i|I_i|,
m_x=|{i:x in O_i}|,
H=sum_(x outside X, m_x>=1) C(m_x-1,2),               (MD1)
sigma=sum_(i<j)(ell_ij-|I_i|-|I_j|-|O_i intersect O_j|).
                                                               (MD2)
```

Thus `I,H,sigma` are nonnegative integers. Let `Z=sum_i z_i` and define the
shell baseline

```text
D_0=2(d+1)+t(h-2d-2)+(d+1)t(t-1)-2(t-2)Z
   =t h+(t-2)((t-1)(d+1)-2Z).                       (MD3)
```

If `v=|union_i A_i|` and

```text
Delta=2v-2a-ht,
```

then the Maxwell deficit is exactly

```text
Delta=D_0+2((t-2)I+sigma+H).                         (MD4)
```

Consequently, if the rows are all blocks of their minimal Maxwell core, then
`Delta=-e<=0` and

```text
(t-2)I+sigma+H<=floor(-D_0/2).                       (MD5)
```

This recovers the previous exclusion when `D_0>0` and sharpens every
nonpositive-baseline shell. In particular, if `D_0=0`, a primitive full-core
family must satisfy all three conditions

```text
I=0,
every pair budget (EC4) is saturated,
m_x<=2 for every x outside X.                        (MD6)
```

The identity does not count the zero-defect or bounded-defect configurations,
prove first-core ownership, classify higher trade rank or nonuniform cells,
or pay the cross-core slope aggregate.
