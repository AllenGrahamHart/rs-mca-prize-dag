# XR prize `u=0` loop-defect Maxwell and rank-one compiler

- **status:** PROVED
- **closure:** proof
- **consumer:** `xr_highcore_collision_count`
- **dependencies:** `xr_rs_flat_nullity_basis_charge`,
  `xr_prize_flat_nullity_effective_core_floor`,
  `xr_prize_flat_nullity_nonpersistent_root_cap`,
  `xr_higher_rank_uniform_split_pencil_reduction`

Fix a prize P-A flat-nullity cell with `u=0`, affine kernel rank `a`, and
`v>=1`. From an over-budget family, delete every slope at which one of the
`v` nonpersistent global kernel roots becomes a selected zero. At most `v`
slopes are deleted. After puncturing all global kernel roots, the retained
family is a coherent `GRS_a` extension on

```text
N=R+a,       m=a+h+v,       pair cap=a+v.             (LC1)
```

It contains a minimal dense core `G` with `t=|G|>=3`, union `V`, and

```text
h t=2|V|-2(a+v)+e,       0<=e<=h-1.                  (LC2)
```

The stacked two-syndrome parity matrix has at least

```text
v(t-2)+e+1                                               (LC3)
```

independent left-kernel trades. Every active trade row has support at least
`a+1`, and every active coordinate has degree at least three.

Rank-one trades, which are impossible at `v=0`, are classified exactly. If
`J` is the active block set, all rows have one common support `S` of size

```text
a+1<=w=|S|<=a+v.                                      (LC4)
```

There is a polynomial `Q` with `deg Q<w-a`, nonzero on `S`, and nonzero
coefficients `(alpha_i)_(i in J)` satisfying

```text
sum_i alpha_i=sum_i gamma_i alpha_i=0                 (LC5)
```

such that

```text
lambda_i(x)=alpha_i Q(x)/Lambda'_S(x)   for x in S,
lambda_i(x)=0                              otherwise.  (LC6)
```

Conversely, `(LC4)--(LC6)` give a rank-one trade whenever `S` is contained
in every active block. Thus the complete `u=0` endpoint splits into an exact
common-support rank-one stratum and a trade-rank-at-least-two stratum.

At the first open prize ranks, the only `u=0` values not already paid obey

```text
11,243,354<=v<=1,526,176,110;
 9,629,956<=v<=2,902,067,939;
 2,241,619<=v<=1,962,285,106.                         (LC7)
```

This is a structural compiler, not a count of either stratum.
