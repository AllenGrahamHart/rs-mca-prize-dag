# Shortening-weighted terminal kernel capacity cut

Let `796599<=K'<=1048576`, `S=K'-10`, `n'=1048576+K'`, and
`m'=67472+K'`.  For corank `d`, put

```text
U_d(K') = P_d C(S,d+1)                 for d=1,2,3,
U_d(K') = F_d(1) C(S-1,d+1)           for d=4,...,9.
```

Then the complete kernel-lane incidence capacity is at most

```text
sum_(d=1)^9 C(n',10-d) U_d(K')/(d+2),
```

which is strictly below

```text
(495405467/10^9) N_min C(m',11),
N_min=274980728111260126.
```

Together with the proved lower-interval cuts, the rank-eleven fixed-kernel
branch is excluded for every official `10<=K'<=1048576`.
