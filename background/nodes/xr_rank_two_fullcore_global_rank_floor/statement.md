# XR rank-two full cores have a global official-row rank floor

- **status:** PROVED
- **closure:** proof
- **consumer:** `xr_highcore_collision_count`
- **dependencies:** `xr_rank_two_zero_baseline_arithmetic_router`,
  `xr_rank_two_maxwell_collision_defect_identity`,
  `xr_higher_rank_rank_two_shell_maxwell_router`,
  `xr_higher_rank_uniform_split_pencil_reduction`,
  `xr_prize_primitive_rank_two_shell_band`

Use an official uniform rank-two relation whose `t>=4` active rows are
exactly all blocks of one minimal Maxwell core. Put

```text
D=d+1>=3,       Z=sum_i z_i,
D_0=t h+(t-2)((t-1)D-2Z).                         (GF1)
```

For fixed `h,t`, define

```text
D_-(h,t)=max{3,
  floor((t h+2t(t-2))/((t-2)(t+1)))+1},            (GF2)

M_t(D)=tD/2                         if D is even,
       t(D+1)/2-1                  if D is odd,

B_t(D)=t h+(t-2)(t-1)D,
Z_-(h,t)=max{M_t(D_-),
             floor(B_t(D_-)/(2(t-2)))+1},
a_-(h,t)=Z_--D_-.                                  (GF3)
```

If `D_0<0`, then necessarily

```text
D>=D_-(h,t),       Z>=Z_-(h,t),       a>=a_-(h,t). (GF4)
```

Minimizing this exact arithmetic floor over the official arity ranges gives:

| row | arity range | minimizing `t` | `D_-` | `Z_-` | `b=-D_0` | negative-baseline `a_-` | zero-baseline floor | all-baseline floor |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| RowC `1/4` | `4..258` | `4` | `4` | `12` | `4` | `8` | `10` | `8` |
| RowC `1/8` | `4..130` | `4` | `4` | `12` | `4` | `8` | `10` | `8` |
| RowC `1/16` | `4..66` | `4` | `3` | `8` | `2` | `5` | `6` | `5` |
| prize `1/4` | `4..384` | `384` | `22,428,335` | `8,612,480,189` | `174` | `8,590,051,854` | `8,601,474,050` | `8,590,051,854` |
| prize `1/8` | `4..448` | `448` | `19,217,050` | `8,609,237,915` | `416` | `8,590,020,865` | `8,601,474,050` | `8,590,020,865` |
| prize `1/16` | `4..960` | `958` | `4,487,961` | `4,299,465,631` | `734` | `4,294,977,670` | `4,302,648,690` | `4,294,977,670` |

The last column applies because the zero-baseline arithmetic router gives the
larger printed floor on every row, while the collision-defect identity forces
`D_0<=0` for a full minimal core.

This is a necessary rank floor, not an existence theorem. It does not treat a
proper four/five-block circuit inside a larger core, count the surviving
high-rank full cores, classify trade rank at least three or nonuniform cells,
or prove the P-A aggregate.
