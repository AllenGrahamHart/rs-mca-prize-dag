# XR mismatch-descent dimension area law

- **status:** PROVED
- **consumer:** `xr_tangent_support_mismatch_bridge`
- **dependency:** `xr_mismatch_nongeneric_invariant_excess_descent`

Consider a live nongeneric mismatch chain with states `(N_j,K_j,A_j)` and
transitions `j=0,...,L-1`. Put

```text
h=A_j-K_j>=1,              H=h+1,
N_(j+1)<=N_j-K_j-h,        K_(j+1)=K_j-d_j,
0<=d_j<=K_j-1.
```

Then

```text
sum_(j<L)(K_j+h)<=N_0-H,                              (XDA1)
sum_(j<L)d_j=K_0-K_L<=K_0-1.                         (XDA2)
```

Thus the excess-dimension area satisfies

```text
sum_(j<L)(K_j-1)<=N_0-H-LH.                          (XDA3)
```

For every integer threshold `kappa>=1`, let

```text
L_kappa=#{j<L:K_j>=kappa}.
```

Then

```text
L_kappa<=floor((N_0-H)/(kappa+h)),                    (XDA4)
sum_(j<L)K_j=sum_(kappa=1)^K_0 L_kappa.              (XDA5)
```

Equivalently, put `D=floor(N_0/H)-1` and
`r=N_0-H-DH`, so `0<=r<H`. If a chain has `L=D-s`
transitions, then

```text
sum_(j<L)(K_j-1)<=r+sH.                              (XDA6)
```

Hence a chain close to the old worst-case depth is forced to spend almost
all of its time at dimension one. Large external-zero drops cannot be paid
again later: their total along one chain is at most `K_0-1`.

At the six clean-rate roots, `(XDA4)` gives the following caps for dimensions
at least `H,2H,4H,8H,16H,32H`; a dash means the threshold already exceeds
the initial dimension.

| row | `H=h+1` | `K_j>=H` | `K_j>=2H` | `K_j>=4H` | `K_j>=8H` | `K_j>=16H` | `K_j>=32H` |
|---|---:|---:|---:|---:|---:|---:|---:|
| RowC `1/4` | 6 | 92 | 59 | 35 | 19 | 10 | 5 |
| RowC `1/8` | 6 | 92 | 59 | 35 | 19 | 10 | - |
| RowC `1/16` | 4 | 145 | 92 | 53 | 29 | 15 | - |
| prize `1/4` | 8589934594 | 127 | 84 | 50 | 28 | 14 | 7 |
| prize `1/8` | 8589934594 | 127 | 84 | 50 | 28 | 14 | - |
| prize `1/16` | 4294967298 | 255 | 170 | 102 | 56 | 30 | - |

This theorem controls one chain's depth-dimension profile. It does not bound
branch multiplicity, slopes per explanation, or generic-chart slope unions.
