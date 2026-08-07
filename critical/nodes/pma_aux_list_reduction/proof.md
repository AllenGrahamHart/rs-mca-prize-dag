# pma_aux_list_reduction proof

Fix the defect set `D` and the planted background `R_P`. By
`l1_core_defect_reduction`, every non-planted extra determines a unique
residual polynomial `W_P` of degree at most `d`; uniqueness is part of the
core-defect normal form, so the map

```text
P -> W_P
```

is injective on the extras counted by this node.

On each petal `T_i`, the planted target has the common defect locator
`L_D`, scaled by the petal scalar `c_i`. Since the petals are disjoint, these
values define a single auxiliary received word

```text
U*(x) = c_i L_D(x)  for x in T_i.
```

The background convention imposes `W_P = 0` on `R_P`. Thus every extra maps to
a degree-`<=d` polynomial agreeing with the auxiliary word at exactly the
printed agreement level

```text
N = d + 1 + sigma - |R_P|.
```

Therefore extras for fixed `D` and `R_P` inject into a Reed-Solomon list
decoding problem of degree `d` against `U*`. The choices of `D` contribute the
separate factor `binom(k-1,d)`, which is the reserve line already allocated
to locator combinatorics. This proves the reduction.
