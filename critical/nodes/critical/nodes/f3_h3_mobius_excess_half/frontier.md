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
- At each fixed order, every remaining rich row prime belongs to the finite
  union of divisors of collision norms `Norm(beta_E-beta_F)` with
  `||v_E-v_F||^2<=6`. Galois/exchange orbit reduction is exact.
- In fact every rich fiber contains two such collisions with one common
  center among vectors of squared norm at most three. After removing the
  universal `(1-zeta)^2` factor, the row prime divides their two-generator
  ideal norm, which divides the gcd of the two normalized principal norms.
  This ideal-star union supersedes the single-norm candidate union for future
  computation.
- For every split candidate prime, divisibility of an ideal-star norm is
  equivalent to three shifted products coinciding at one degree-one prime.
  Odd dilation makes one fixed primitive root sufficient for the complete
  star union, so the final sieve needs neither ideal normal forms nor all
  primes above `p`.
- Squared-distance-two collision obstructions are dyadic binomials with
  2-power norm. They cannot occur in an odd row-prime fiber. The seven-vector
  packing graph consequently has at least six low edges, and official
  candidate generation only needs the distance-four and distance-six classes.
- Distance four is now split exactly. If an endpoint is not antipodal, a
  genuine same-fiber edge must have a cross signed-monomial overlap. After
  relabeling, `uv=-y` and the collision equation becomes
  `ux(1-y)=u^2-y`, so `x` is determined by `(u,y)`. The antipodal sublane is
  equally explicit: `x^2=u+v-uv`, with square-subgroup membership determining
  its unordered pair. The two lanes give the global bound
  `N_4<=(3n^2+n)/2`, so at most `floor((3n^2+n)/12)` rich targets have no
  distance-six edge. Joint quotient pricing remains open.
- More sharply, the selected rich-fiber graph satisfies
  `2N_4+N_6>=11`. A weighted handshake gives a center of incident weight at
  least four, and its two-to-four normalized collisions generate an ideal
  whose norm contains the row prime. The complete candidate sieve should use
  this weighted-degree condition instead of the older two-leaf condition.
  On the complete toy principal-prime lists it leaves `4/103` and `67/2,127`
  primes at orders `32` and `64`.
- The rich excess itself strengthens the ideal: `e=P-18` supplies at least
  `7+ceil(e/2)` small vectors and center degree
  `L(7+ceil(e/2))`. Weight four is confined to the possible boundary profiles
  `(P,D)=(19,1),(20,2)`; excess `>=3` forces weight six and excess `>=7`
  forces weight eight. Quotient-weighted counting of these degree strata is
  still open.
- Total quotient mass yields five exact budget/degree interfaces. The selected
  one pays `P<=32` and leaves only `P>=33`, where center weight is at least
  twelve and the residual numerator budget is
  `300n^2-238(n-1)(n-2)`. Cutoffs `E=2,6,10` give the fallback degree
  thresholds `6,8,10` with larger budgets.
- On this tail, excess is at most `16/83` of the complete centroid edge
  weight. C36' therefore reduces to a low-distance edge–quotient moment of
  conservatively less than `18.92n^2`. Canonical elimination realizes the
  distance-six term as a four-variable/two-membership rational incidence and
  each distance-four lane as a three-variable/two-membership incidence. The
  required estimate remains open.
- More sharply, orienting one valid cross-overlap per generic distance-four
  edge gives indegree at most one, so the generic graph has at most as many
  edges as vertices. With the unique possible antipodal representation this
  combines with the norm-one antipodal centroid saving to force
  `P-18<=(8/21)N_6` on the selected tail. The current endpoint is
  therefore only the distance-six incidence moment
  `M_6,33<(651/68)n^2` in its exact integer form; the distance-four term is
  retired from this route.
- Splitting by the unique possible antipodal representation improves the
  antipodal-free ratio to `P-18<=(16/53)N_6`. The antipodal moment keeps the
  uniform `8/21` ratio but gains a third exact subgroup-membership test
  through `t=1-x^2`. The refined endpoint is
  `136(42M_6,33^0+53M_6,33^A)<=1113(300n^2-238(n-1)(n-2))`.
- Analytic incidence work may instead use the proved `E=6` or `E=10` Pareto
  interfaces. Their conservative weighted allowances are `24.75n^2` on
  `P>=25` with antipodal weight `17/10`, and `(715/34)n^2` on `P>=29` with
  antipodal weight `11/8`. Fixed-order candidate generation still uses
  `E=14`, whose center-degree-twelve sieve supplies stronger compression.
- The `E=6` support-overlap strata are paid by exact quotient mass. Two cubic
  one-parameter covers bound overlapping generic edges by six per target, and
  the antipodal vertex contributes at most two more. The preferred analytic
  endpoint is now the disjoint-support moment
  `D_6,25^0+(17/10)D_6,25^A<=(223/20)n^2`.
- Raw orbit enumeration is not sparse: a restricted `n=8192` family already
  has at least `530,590,075` such orbits. A practical factor certificate needs
  an algebraic norm-template compression or a stronger collision selector.

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

For the ideal-star selector, the same two fibers are especially clean: the
reference pair is at squared distance six from all nine other pairs, and the
first two normalized collisions generate `P` itself. Thus the rooted-star
ideal norm is exactly `p` on both known rich fibers. Uniform saturation is not
claimed.

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

The fixed-order ideal-star route and its preprocessing gate are recorded as
`CR-001` in `notes/PRIZE_COMPUTE_REQUESTS.md`. Incomplete orbit or factor
sweeps remain evidence only.

A bounded template pilot (`ap-J4kT8st6P45yWvWZtc2Xgi`) shows that equality of
exact norms is not enough compression. The complete `n=32` census merged
`5,216` orbits to `227` norms, but the first `5,000` `n=64` orbits already
produced `2,567` norms. This is route evidence, not a growth theorem; it
selects a stronger collision selector or symbolic template invariant before
any larger fleet. The proved ideal-star router now supplies that stronger
selector. A complete rational-gcd screen then removed no relevant primes
(`103 -> 103` at `n=32`, `2,127 -> 2,127` at `n=64`), while exact common
prime-ideal alignment compressed the same lists to `18` and `162`. The latter
is the selected sieve. Both toy orders had empty `P>=19` loci. Official-scale
candidate generation remains algebraic, not a larger raw fleet.

The complete norm-class pilot `ap-nFVftE3yG19HwOwPvjIehP` confirms the
2-primary theorem and rejects its extension to distance four. Relevant odd
factors by distance are `0,4,103` at `n=32` and `0,67,2127` at `n=64` for
distances `2,4,6`. Distance four is a smaller four-term lane, but distance six
remains the dominant candidate-generator problem. No larger raw census is
selected.

The unfiltered exact row `(n,p)=(32,1153)` contains six antipodal
distance-six edge–quotient records, and the direct and three-membership routed
counts agree. This checks the refined router's posedness; no target on that
row reaches the selected `P>=33` tail.
