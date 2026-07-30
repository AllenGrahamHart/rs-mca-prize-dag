# Source evidence

- `rate_half_kb_m2_r4_diagonal_c2_square_fiber_linear_cut` supplies the
  source-line ramified orbit, the two coincident square-root stars, and the
  exact unramified `4/3` conclusion.
- `rate_half_kb_m2_v4_outer_recurrence_router` imports the actual
  complete-source quartic defect bound
  `sum_v binom(weight(v),2)<=3`.
- `(KBDM-8)`, already in the first parent chain, supplies four unramified
  common-`K` fibers with eight reduced stars on `J_0` once the branch orbit
  is occupied by `k_*` and `tau(k_*)`.
- The six-vertex occupancy floor is independently exhausted by the local
  audit. No field enumeration or genericity assumption is used.

## Upstream custody

The theorem is vendored into the diagonal source-facet packet in draft PR
`przchojecki/rs-mca#1132` at commit
`3584deccfc92aa4b1c1125b40017eabd15167079`:

```text
note blob:        20559b894d129dfe1094a0b3dac70ed1f8d595da
verifier blob:    73be19232ad839ac1be4fadc7c7d8cefd30a66f7
certificate blob: e82f08722dd2bfba564b51a25d3e7f4d6e692c67
payload SHA-256:  22e3cc5c5100d2b90e6487b6216fc8e5c0d6cd3f5eeefef90bac325643cbcd71
```

The upstream replay exhausts all `1,287` six-vertex occupancies, certifies
the defect floor four against budget three, includes the full-row
strengthening and the saturated `(1,1,2)` classifier, and rejects `83` of
`83` hostile mutations across the packet.
