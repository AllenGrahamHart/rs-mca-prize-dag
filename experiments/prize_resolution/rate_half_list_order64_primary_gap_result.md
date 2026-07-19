# Rate-half list order-64 primary-gap high-characteristic pilot

- **status:** experimental route evidence; no theorem promotion.
- **Modal app:** `ap-wLXZpGxaBiBlZ1NZ3MP14e`.
- **resources:** nine parallel functions, one physical CPU, 512 MiB RAM, and
  a 60-second hard timeout each; every exact scan finished.
- **scope:** all `C(64,4)=635376` deleted-root quadruples over the first eight
  primes `p>=64^2` with `p=1 mod 64`, plus the known `p=193` control. The
  square threshold is deliberately strong and is not an analogue of every
  official field branch.
- **result hash:**
  `26d48487a885ccd31a01a7b336e3b3c0c4574ed08c6957721ab4c394a078138e`.

The control field reproduces `3328` single primary gaps and `64` double gaps,
with first example `{0,1,3,62}`. The eight square-threshold fields contain
respectively

```text
p       4289  4481  4673  4801  4993  5441  5569  5953
single    64    64   128    64   192     0     0   128
double     0     0     0     0     0     0     0     0
```

Thus a `p>=d^2` primary double-gap exclusion survives this bounded
falsification attempt even though its one-gap relaxation is populated. The
known `p=193` example already has `p>d=64`, so primary nonvanishing is false
under the theorem chain's generic characteristic hypothesis. Officially the
maximal `B*=3` row has either a prime field with `p>=3*2^128`, or a quadratic
field with only `p>2^64` at `d=2^39`; there is no uniform official `p>=d^2`
or `p>=n^2` premise. The pilot therefore proves nothing about the growing
official order. Extending a raw fixed-order prime sweep has no known transport
and is not a responsible large compute request. CR-002 instead asks for a
compressed, coverage-proved official-order simultaneous-gap and
canonical-span certificate.

Replay the pinned summary with

```text
tools/ramguard tiny -- python3 experiments/prize_resolution/rate_half_list_order64_primary_gap_check.py
```
