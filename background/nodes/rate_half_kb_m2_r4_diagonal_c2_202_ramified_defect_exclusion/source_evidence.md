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
`5b8a8dfe12af2236fe28665ff6fc66f54322a4a7`:

```text
note blob:        d69e5c6673a5bff7f181e84dcc10c56a9e1dc71a
verifier blob:    16dcab7f81e033b4f0a40b947ccdd3edc3cfc049
certificate blob: 96c0fd785bec2f761336893db251a349ee2b4e74
payload SHA-256:  ca878fb3aa4e41ab5b7184413decdb50522716fd70267ddd529dc37d57d9bce6
```

The upstream replay exhausts all `1,287` six-vertex occupancies, certifies
the defect floor four against budget three, and rejects `69` of `69` hostile
mutations across the complete packet.
