# E1 N=256 E=34 route boundary

This report records an exact preflight and route decision. It is not a proof
node and changes no DAG status.

For `V=68`, put `E=34`. Parity in the relaxed slack recurrence makes the L1
ceiling increase again:

```text
L=21: slack 16, minimum energy 38 > 34,
L=20: slack 20, minimum energy 34.
```

Thus `L<=20`. There are 24 integer magnitude profiles. The rational cubic at
contacts 14 and 57 has positive exact margin at `M_3=1947` and negative exact
margin at 1948. Its boundary log forms are

```text
M_3=1947: (74945/79507, 4562/79507, -17729/1475502),
M_3=1948: (74947/79507, 4560/79507, -2943/245917).
```

Six profiles exceed the threshold:

```text
2428  (6,7),
2264  (9,4,1),
2252  (2,8),
2124  (12,1,2),
2084  (5,5,1),
1956  (14,1,0,1).
```

This is the boundary of the cheap one-exception quotient descent. Unlike
`E=35`, several three- and four-layer profiles miss by hundreds, so an
outer-only quotient census cannot decide the slice. At this checkpoint no new
Modal campaign was authorized: a return first had to derive a common
nested-layer compiler for all six profiles, with a proved completeness router
and a sub-`$1` pilot, or replace the cubic by a stronger analytic certificate.

## Nested-layer compiler

The common compiler is now implemented in
`e34_nested_quotient_census.cpp`. For an exact magnitude profile
`(n_1,...,n_r)`, it allocates the `n_j` positive distance representatives
among the nine negation-orbit categories modulo 16. The resulting nested
layers are

```text
X_i={d: |A_d|>=i},       1<=i<=r.
```

For every unordered layer triple it applies the proved target-fiber quotient
bound in each of the three orientations and multiplies by the exact ordered
triple multiplicity. Nested two-point layers coincide and have zero cubic
Schur count. Requiring an odd outer category handles the live order-128
chamber; applying the same compiler with the order-64 capacities handles the
outer-even but not outer-`4Z` chamber after division by two. The inherited
small-field norm theorem excludes the remaining outer-`4Z` chamber. These
cases are exhaustive, so a complete census with maximum at most 1947 would
close `V=68`.

The independent checker
`e34_nested_quotient_census_check.py` recomputes every displayed objective
and, for a complete packet, recounts each of the twelve profile/order state
spaces by a separate dynamic program. Their aggregate size is 228,097,120
exact allocations. The launcher checkpoints after every returned shard and
retains explicit failed-task records.

The registered pilot `CR-E1-E34-NESTED-Q16-PILOT` runs one deterministic
outer shard out of 128 for each of the twelve cells. It is a route decision,
not theorem evidence. Any returned objective at least 1948 kills the bare
mod-16 nested quotient route with an exact allocation. If all twelve pilot
maxima are at most 1947, the measured worker times determine whether the
complete 16-shard-per-cell campaign remains within the five-minute and
sub-`$1` laws. No full campaign is authorized before that timing audit.

## Pilot outcome and route cut

Modal app `ap-Ec22WlisgFjRNPFuigxlEy` returned all twelve pilot tasks in
18.91 seconds of client-observed app wall time. The independently replayed
maxima were

```text
profile             order 128    order 64
(6,7)                     2132        2154
(9,4,1)                   1990        2016
(2,8)                     1716        1616
(12,1,2)                  1990        1706
(5,5,1)                   1698        1716
(14,1,0,1)                1620        1726
```

Thus five sampled cells already exceed 1947. Their exact magnitude-by-
quotient allocations are stored in
`e34_nested_quotient_pilot_result.json`; the checker reconstructs every
nested layer and objective directly. These are obstructions to this upper-
bound compiler, not autocorrelation vectors and not counterexamples to the
`V=68` exclusion.

The all-profile 228,097,120-allocation campaign is retired. A direct weighted-fiber
recombination was also evaluated on every displayed obstruction and gives
bounds between 2036 and 2174 on the five failing cells, so it does not repair
the route. The next positive theorem must use information erased by the
mod-16 allocation: simultaneous chord-origin realizability across all layer
triples, a finer support-specific coupling for the failing profiles, or a
stronger analytic norm majorant. Do not run the complete quotient census.

The launcher did not record individual worker durations, so the app is not a
timing certificate for a future full campaign. No theorem depends on timing
or sampled coverage here, and the exact route obstructions replay locally;
there is no reason to spend credit rerunning the retired pilot solely to add
timings.

The obstruction is profile-selective. The three unobstructed profiles

```text
(2,8),       (5,5,1),       (14,1,0,1)
```

occupy exactly 42,413,558 allocations across the two live quotient chambers,
and every pilot maximum is at most 1726. Campaign
`CR-E1-E34-Q16-SURVIVORS` is separately authorized to exhaust only these six
cells in sixteen shards each. It is not the retired all-profile campaign. A
complete maximum at most 1947 closes all three profiles; a larger maximum
returns an exact allocation and leaves only that profile for support-specific
coupling. The other three profiles are not run: their next compiler is the
41-signature `L=20` chord-origin classification.

Modal app `ap-zx5C3lSHLdaYAZE2Ic0tZA` completed all 96 tasks and all
42,413,558 allocations in 29.84 seconds of client-observed wall time. Worker
durations range from 0.052 to 16.259 seconds and sum to 334.664 CPU-seconds.
The independently reconstructed maxima are

```text
profile             order 128    order 64
(2,8)                     2052        2008
(5,5,1)                   1880        1828
(14,1,0,1)                1922        1922
```

Thus the campaign proves the latter two profiles below 1947. The `(2,8)`
profile returns the registered `FAIL`: its order-128 obstruction has quotient
components `(300,264,240,240)`, totaling 2052, while its order-64 obstruction
totals 2008. The terminal launcher print used the last returned shard rather
than the maximum shard; that presentation bug is repaired in source, and no
claim uses it. The complete packet and independent checker give the displayed
maxima.

The abstract `V=68` frontier is now four profiles:

```text
(6,7),       (9,4,1),       (2,8),       (12,1,2).
```

For `(2,8)`, the existing exact `R(B,B,B)<=174` theorem lowers the displayed
order-64 obstruction to 1942, but lowers the order-128 obstruction only to
1986. Its next route is therefore a chamber-exhaustive inner-layer refinement,
not the retired six-profile census.

## Profile `(2,8)` coupled campaign

Campaign `CR-E1-E34-P2-COUPLED` combines two exhaustive compilers. The first
replays all 809,474 profile-`(2,8)` quotient allocations and applies
`R(B,B,B)<=174` exactly when the inner layer is in the divided order-64
scope. It separately reports the order-128 chambers `B subset 4Z` and
`B not subset 4Z`. The second enumerates the remaining inner-`4Z` chamber at
support level. There are `binom(15,8)=6435` inner layers and exactly 1,232
admissible two-pair outer supplements per layer, for 7,927,920 weighted
supports.

The campaign closes `(2,8)` exactly if

```text
order-64 refined quotient maximum       <=1947,
order-128 outside-inner-4Z maximum      <=1947,
order-128 exact inner-4Z support maximum<=1947.
```

The sources are `e34_profile2_refined_quotient_census.cpp` and
`e34_profile2_inner4_support_census.cpp`; one independent checker reconstructs
both quotient objectives, both coverage counts, and every displayed support
maximum. The 64 one-CPU, 256-MiB tasks form one wave with 120-second hard
function caps, a campaign wall ceiling below three minutes, and a conservative
cost ceiling below `$0.20`. `FAIL` returns the exact surviving chamber;
`INCOMPLETE` changes no status.

Modal app `ap-8xzV3fZniv8jms4V2EI19N` completed all 64 tasks in 22.02
seconds of client-observed wall time and 17.624 aggregate worker-seconds. The
independent checker gives

```text
order-64 refined quotient maximum          1942,
order-128 outside-inner-4Z maximum         1942,
order-128 inner-4Z exact support maximum   1536.
```

All three values are below 1947, so `(2,8)` is closed. Combined with the
selective campaign, the complete `V=68` residual is now exactly
`(6,7),(9,4,1),(12,1,2)`, all with `L=20`. This reduction is promoted as
`e1_n256_s16_e34_three_profile_reduction`.

## Parity reduction

No further census is needed to compare these three profiles. The coefficient
profile has exactly six unit-product chords, namely the six edges among the
four light positions. Modulo two, every autocorrelation coefficient is the
number of unit chords in its distance class. The candidate profiles have 6,
10, and 14 odd coefficients respectively, so only `(6,7)` can occur.

Equality forces the six unit chords into six distinct non-diameter classes.
Thus the light positions form a circular Sidon set, and diameter square mass
is restricted to `0,4,8,12,16,20`. The corresponding signed equal-chord cross
sums are `-34,-32,-30,-28,-26,-24`. This proof is promoted as
`e1_n256_s16_e34_parity_profile_reduction`; the 41 relaxed signatures now
describe heavy-chord collisions around one profile rather than three.
