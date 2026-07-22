# L1 balanced mixed-petal growth census

## Decision

Roadmap round N10 is complete for the chart family and scales below.  The
registered super-polynomial-growth falsifier did not fire.  This is numerical
evidence only: it neither proves a polynomial bound nor changes
`l1_mixed_petal_amplification` from `TARGET`.

## Object

For the house rate-half chart over a multiplicative subgroup, the census
enumerates every candidate support satisfying all of:

```text
agreement >= k+1,
core defect d >= 2(t-2),
at least one partially met two-point petal.
```

It interpolates the unique degree-`<k` polynomial from `k` candidate points
and retains the candidate only when its **complete** agreement set is exactly
that support.  A codeword is therefore counted once, rather than through all
of its agreement sub-supports.  The floor restriction implies at most three
selected core points and at most three omitted petal points, giving the exact
candidate totals printed below.

Two scalar schedules were tested: consecutive petal labels and powers of
five.  The fields are the smallest convenient prime fields for these scales;
the change from `F_97` to `F_193` is part of the scope and prevents treating
the table as one nested-field family.

## Results

| `n,k,p` | labels | candidates | retained | agreement histogram | core-count histogram |
|---|---|---:|---:|---|---|
| `16,8,97` | consecutive | 5,096 | 43 | `9:43` | `2:6, 3:37` |
| `16,8,97` | powers of 5 | 5,096 | 33 | `9:33` | `1:1, 2:8, 3:24` |
| `32,16,97` | consecutive | 386,640 | 2,879 | `17:2871, 18:8` | `2:93, 3:2786` |
| `32,16,97` | powers of 5 | 386,640 | 2,857 | `17:2850, 18:7` | `1:3, 2:98, 3:2756` |
| `64,32,193` | consecutive | 27,152,032 | 109,391 | `33:109329, 34:62` | `2:987, 3:108404` |
| `64,32,193` | powers of 5 | 27,152,032 | 108,600 | `33:108547, 34:53` | `1:6, 2:1001, 3:107593` |

The consecutive doubling ratios are `66.9535` and `37.9962`, with effective
base-two exponents `6.0651` and `5.2478`.  The powers-of-five ratios are
`86.5758` and `38.0119`, with exponents `6.4359` and `5.2484`.  The falling
second ratio resists, rather than supports, the pre-registered
super-polynomial trend on these charts.  Three points cannot distinguish a
polynomial law from a delayed escape, and this family is not universal over
received words.

## Execution record

- source:
  `experiments/prize_resolution/l1_balanced_mixed_growth_census_modal.py`
- final source SHA-256:
  `08ff22fa18be71ff4bb8ef7f6322d0b0fdc7d79933b2ef802256c8aff1c96cc8`
- pilot and complete `n<=32` run:
  `ap-8dNe0YK0DFiWy9h0DehmIR`
- first `n=64` run:
  `ap-zu0wucMs6lAqoRmPL41CV1`
- failed consecutive shards from that run: `5,6,30`; all other shards and
  the complete powers-of-five census finished
- exact retry of only those three shards:
  `ap-jOUf3ceh1L741L9N3qarLS`

The `n=16` consecutive run reproduced the banked catch-176 count `43` before
larger outputs were accepted.  The first `n=64` invocation correctly returned
`INCOMPLETE`, preserving the three timeout shard IDs.  The final consecutive
total is the first-run partial `99,105` plus retry total `10,286`.

The two complete `n=64` modes consumed about `998.04` aggregate worker
seconds at one requested physical CPU and 1 GiB.  At the Modal function rates
published on 2026-07-21, the CPU-plus-memory charge is approximately `$0.016`,
excluding minor image-build overhead and rounding.  No other paid run was
launched in this round.

## Next scale

Do not launch `n=128` on the remaining credit.  The same complete generator
has exactly `1,821,304,128` candidates per scalar schedule.  Scaling the
measured implementation by candidate count and the quadratic interpolation
cost predicts roughly `37` CPU-hours per schedule, or about `74` CPU-hours
for both.  At current function rates this is approximately `$4.1` before
overhead.  The contributor request and its required checker semantics are
recorded as `L1-N10-128` in `notes/PRIZE_COMPUTE_REQUESTS.md`.

