# XR prize uniform trades have a private-point rank floor

- **status:** PROVED
- **closure:** proof
- **consumer:** `xr_highcore_collision_count`
- **dependencies:** `xr_higher_rank_uniform_split_pencil_reduction`,
  `xr_prize_primitive_rank_two_shell_band`, `xr_target_budget_audit`

Use a prize-row uniform split-pencil minimal Maxwell core `G`, and let `J` be
the active block set of any nonzero trade supplied by its left kernel. Put

```text
t=|J|,       P_J=#{points in exactly one selected block of J},
L=floor((2R+h-1)/h).                                (UF1)
```

Then

```text
P_J>=t h-t(t-2)a,                                   (UF2)
P_J<=t(h-1-e)/2+(|G|-t)t a
   <=t(h-1)/2+(L-t)t a.                             (UF3)
```

Consequently every nonzero trade in a prize-row minimal uniform core obeys

```text
a>=A_unif(h,L):=ceil((h+1)/(2(L-2))).               (UF4)
```

The exact prize floors are:

| rate | `h` | `L` | necessary affine kernel rank `a` |
|---|---:|---:|---:|
| `1/4` | `2^33+1` | `384` | `11,243,370` |
| `1/8` | `2^33+1` | `448` | `9,629,972` |
| `1/16` | `2^32+1` | `960` | `2,241,633` |

Every over-budget uniform selector contains such a core and trade. Therefore
the uniform P-A branch has no prize-row counterexample below these affine
ranks; equivalently it is paid through selector ranks

```text
11,243,370;       9,629,972;       2,241,633.       (UF5)
```

This theorem covers every trade-matrix rank. It supersedes rank-two
classification as the low-rank prize uniform-cell obligation, while the
stronger rank-two-specific floors remain valid above it.

The theorem does not handle a uniform cell at or above the printed floor,
any nonuniform cell, or the cross-component aggregate. It is a necessary
exclusion, not an existence theorem at the boundary.
