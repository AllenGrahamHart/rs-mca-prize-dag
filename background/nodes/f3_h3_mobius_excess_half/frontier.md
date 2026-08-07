# Frontier

## Paid terms

- `P(1)<4n^(2/3)` by the proved one-shift Stepanov packet.
- The first `18` units of every nonidentity product fiber are paid.
- The exact remaining target is `17X_18<=300n^2`.
- The proved non-swap compiler reduces this to the sufficient aggregate
  estimate `S_ns^rich<=1200n^2`, where only targets with `P(t)>=19` are
  retained. The former full `S_ns` target is a strictly stronger envelope.
- Dyadic shifted roots are multiplicatively Sidon in characteristic zero.
  Hence every non-swap record entering `S_ns` is a finite-characteristic
  norm-gate accident, with a nonzero lifted obstruction whose norm is
  divisible by the row prime.
- Ten-representation Parseval packing proves `P(t)>=19 => p<=6^(n/4)`.
  Hence `X_18=0` on the complete large-field branch `p>6^(n/4)`.

## Evidence

The first twelve official primes at `n=8192` have `X_35=0`. On the row with
largest observed product fiber, `(n,p)=(8192,67657729)`, the maximum is `20`
and its quotient multiplicity is only `1` (Modal run
`ap-ttBP0c2JCopfqrGmGtvnI2`).

The bounded small-row fleet `ap-bHp1Epb9jC5BdW4xeXfB7l` added 7,090
exhaustive admissible rows at `64<=n<=4096`: `X_35=0` throughout, maximum
`P+2R=32`, and maximum `S_ns/n^2=3.824218750`. All 116 shards completed. The
same data are far inside the weaker current truncated target.

The exact boundary replay `ap-yTeGirrfOykwHEmzAcuamR` isolates the effect of
that truncation at `(n,p)=(8192,67657729)`: the full `S_ns=65810428` collapses
to `S_ns^rich=720`, supported on exactly two targets, while `X_18=4`. Both
rich targets have `P=20` and `R=1`. This is route-selection evidence only.
The fifth-orbit replay `ap-qQ3yscqJjP1LR8yH9nqI5y` gives
`M_5^rich=504` on the same row.

Exact FLINT shards in Modal run `ap-WgM34tE25CAe0FYz8owGUJ` recovered both
complete ten-pair rich fibers on this row. Relative to one reference pair,
the gcd of the first two collision norms is `4p` in both fibers, and remains
`4p` across all nine norms. The proved ideal sandwich therefore identifies
the generated ideal exactly as `(1-zeta)^2 P` in both cases. Reduced ordinary
resultants retain 2880- and 3455-bit non-`p` cofactors, selecting ideal-level
batching over raw resultants. This is exact route evidence, not a uniform
middle-field estimate.

The engineered Fermat-factor replay `ap-MdlzVrunPKIxHe0OyZSWmb` attacks the
norm-divisor route at two order-8192 subgroups with the low-height generator
`2`. Both certified prime rows have `max_t P(t)=5`, hence no target at the
actual cutoff `P(t)>=19` and exactly zero for `X_18`, `S_ns^rich`, and the
rich fifth-orbit moment. Details and nonclaims are in
`fermat_factor_adversary_result.md`.

## Open content

Prove the weighted bound `(WX18)` on the remaining range
`n^2<=p<=6^(n/4)`. The preferred sufficient target is
the truncated non-swap moment `S_ns^rich<=1200n^2`; the full moment's observed
constant is below `3.825`, but that full moment now serves only as an envelope.
The proved line-star identity now poses this as a directed chord-emission
moment between quotient lines. It rules out treating the task as either a
marginal energy estimate or an automatically paid target witness. The complete
`6!` symbolic fence also rules out a direct coordinate-permutation embedding
into the classical shifted-subgroup collinear-triple count; any use of that
literature now needs a new rational bridge.
The pointwise M35 route remains in
`background/nodes/f3_h3_mobius_overlap_cap35` as a stronger sufficient route,
but its generic form is close to an open constant-fiber conjecture.

The proved fifth-orbit compiler supplies a repetition-free alternative:
bounding `sum_{P(t)>=19} binom(U(t),5)R(t)` by `(34650/17)n^2` suffices.
This is a fixed six-fiber incidence moment with a constant above `2038`,
rather than a pointwise constant-intersection conjecture.

The Sidon reduction selects a fourth route: aggregate the `p`-divisible
shifted-product obstructions at one row. Its per-record norm bound alone is
not summable. Same-fiber ideal batching now proves that all collision
differences share `(1-zeta)^2 P`, and the measured boundary fibers attain that
minimal ideal after two generators. The missing input is a uniform upper
index bound or a count/weight bound for the resulting saturated ideals across
the middle-field corridor. The Fermat-factor audit rules out low-height
generation alone as the needed concentration mechanism; it does not supply
that aggregation theorem.

The cutoff-four packing probe supplies a route fence: even seven genuine
low-norm coefficient vectors coming from pairwise factor-disjoint shifted
pairs can all have squared mutual distance at least `6`. Thus the proved
`6^(n/4)` cutoff cannot be improved to `4^(n/4)` from metric packing and the
same-fiber matching property alone. A further norm gain must use the common
product congruences themselves. See `parseval_cutoff4_route_fence.md`.
