# XR prize proper rank-two circuits have a private-point rank floor

- **status:** PROVED
- **closure:** proof
- **consumer:** `xr_highcore_collision_count`
- **dependencies:** `xr_rank_two_proper_circuit_defect_host_router`,
  `xr_rank_two_extension_family_collision_ledger`,
  `xr_higher_rank_uniform_split_pencil_reduction`,
  `xr_prize_primitive_rank_two_shell_band`,
  `xr_trade_circuit_arity_segre_atlas`,
  `xr_rank_two_fullcore_global_rank_floor`

Let `J` be a proper rank-two row-scaling circuit inside a prize-row minimal
Maxwell core `G`. Put

```text
t=|J| in {4,5},       D=d+1,       Z=sum_i z_i,
I=sum_i|I_i|,         C=(t-2)I+sigma+H,
L=the row-specific upper bound on |G|.              (PF1)
```

Let `P_1` be the number of points outside the active union `X` that occur in
exactly one circuit extension `O_i`. Then

```text
P_1 >= t h+t(t-2)D-(2t-3)Z+2C+I.                  (PF2)
```

Every point counted by `P_1` is private to one selected circuit block within
`J`. Minimal-core private-point control and the pairwise block-intersection
cap give

```text
P_1 <= t(h-1-e)/2+(|G|-t)t a
    <= t(h-1)/2+(L-t)t a.                          (PF3)
```

Using `Z<=a+D` and `D>=3`, every such proper circuit therefore satisfies

```text
a >= A_t(h,L):=
 ceil((t(h+1)/2+3(t-1)(t-3))
      /(tL-t(t-2)-3)).                             (PF4)
```

The exact prize arithmetic is:

| rate | `h` | `L` | four-block floor `A_4` | five-block floor `A_5` | proper-circuit floor |
|---|---:|---:|---:|---:|---:|
| `1/4` | `2^33+1` | `384` | `11,265,488` | `11,290,661` | `11,265,488` |
| `1/8` | `2^33+1` | `448` | `9,646,193` | `9,664,643` | `9,646,193` |
| `1/16` | `2^32+1` | `960` | `2,243,389` | `2,245,383` | `2,243,389` |

Composing this with `xr_rank_two_fullcore_global_rank_floor` and the circuit
decomposition proves that no prize-row minimal Maxwell core carries any
rank-two trade below affine ranks

```text
11,265,488;       9,646,193;       2,243,389.       (PF5)
```

Thus every uniform trade below those floors has trade-matrix rank at least
three.

This theorem does not count rank-two records above the floor, classify
trade-rank-at-least-three cores, handle nonuniform cells, or prove the P-A
aggregate. It is a necessary exclusion, not an existence theorem at the
printed boundary.
