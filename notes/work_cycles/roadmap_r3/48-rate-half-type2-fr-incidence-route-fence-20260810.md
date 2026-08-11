### 2026-08-10 rate-half type-2 FR incidence route fence

Round 31 reduced the strict-`A=3` non-minimum type-2 count to a factor
`9/4` over the target and named `(FR)`: upgrade the saturation-forced mean
`|S_gamma intersect W|~2m` to a uniform maximum of the same order.

A preregistered route test now proves that the incidence inputs used by
`(NEWCAP)` cannot supply that upgrade. The quartic cyclotomic difference
family over `F_257` gives a power-of-two-scale system at `m=64` with

```text
N=1024, rho=255, T=257, a=447,
sum_x(64-d_x)=1,
min pair union=447,
min |S_gamma\W|=66,
```

but `max |S_gamma intersect W|=189`, exceeding `2m=128` by `61=m-3`.
The block system is proved analytically; a fixed 1024-bit `W` certificate is
replayed by two independent implementations. Three bounded Modal runs used
one CPU and 256 MB each and found both registered scales on their first
trials.

This is a route fence, not a Hankel-pencil counterexample. The critical node
stays `TARGET` and the official residual remains `9/4`. The next positive
type-2 attack must use the generalized locator polynomials `f_gamma`, the
common syndrome pencil, or the apolar Hankel equations. Support cardinality,
pairwise overlap, saturation, and MDS distance alone are exhausted.

Burn-down: starting pins local `8710af111`, canonical `48a7de3c2`, upstream
`main@93fba1be`; result `NARROWED`; one PROVED route-fence node added, no
critical status or crossing bracket changed, no assumption added, and Modal
spend was negligible. Open upstream PR #1125's determinant atlas was already
harvested locally; #1157 is a KoalaBear route cut with zero prize-ledger
movement. The next route-deciding action is algebraic type-2 support control
or a pivot to another critical leaf if no exact polynomial inequality appears.

Supersession (cycle 51): the `~2m` target above was the Round-31 pilot's
provisional calibration. Exact floor-aware arithmetic at `a=7m-1` shows
that the printed capacity route requires outside spend `9m/4+1`,
equivalently clean intersection at most `7m/4-2`, on the official row. See
`rate_half_type2_fr_exact_spend_calibration`. The incidence witness violates
this stronger target as well.
