
#### CR-E1-E34-Q16-SURVIVORS: close the three unobstructed profiles

**Status:** COMPLETE WITH PARTIAL PASS. Two profiles close; `(2,8)` returns an
exact quotient obstruction.

The pilot obstructions occur only in `(6,7)`, `(9,4,1)`, and `(12,1,2)`.
Exhaust the remaining profiles `(2,8)`, `(5,5,1)`, and `(14,1,0,1)` in both
the odd order-128 and divided-odd order-64 chambers. Their exact aggregate
coverage is 42,413,558 allocations. Use sixteen shards per cell: 96 tasks,
one CPU and 256 MiB each, at most 100 concurrent containers, a 120-second
function cap, and a 110-second subprocess cap. This is one task wave with a
conservative wall ceiling below three minutes and dollar ceiling below
`$0.25`. The corrected launcher records per-worker duration and checkpoints
after each return.

`PASS` requires all six maxima at most 1947 and closes these three abstract
`V=68` profiles by the cubic-Hermite certificate and the existing outer-`4Z`
norm exclusion. `FAIL` emits the exact profile/order allocation above 1947
for support-specific coupling. `INCOMPLETE` changes no status. The independent
checker must reproduce every maximum and the exact 42,413,558 allocation
coverage before any theorem node is promoted. Do not include the three known
obstructed profiles in this run.

Modal app `ap-zx5C3lSHLdaYAZE2Ic0tZA` completed all 96 tasks and all
42,413,558 allocations in 29.84 seconds of client-observed wall time. Worker
durations range from 0.052 to 16.259 seconds and total 334.664 CPU-seconds.
The independent checker gives exact maxima

```text
(2,8):          2052 / 2008
(5,5,1):        1880 / 1828
(14,1,0,1):     1922 / 1922
```

where each pair is order 128 / order 64. Hence `(5,5,1)` and `(14,1,0,1)`
pass the 1947 threshold and are proof-closed. The `(2,8)` profile returns the
declared `FAIL` with exact allocations in the packet. Its largest order-128
quotient components are `(300,264,240,240)`, totaling 2052; replacing the
inner cubic by the proved cap 174 still leaves 1986. The order-64 obstruction
falls to 1942 under that replacement. Continue only with a chamber-exhaustive
inner-layer refinement for `(2,8)`; do not rerun the two closed profiles.

The launcher's terminal progress dictionary originally retained the last
returned shard rather than the maximum shard. The compact result packet was
unaffected, the independent checker found the correct maxima above, and the
summary source is repaired. No theorem relies on the incorrect terminal
print.

#### CR-E1-E34-P2-COUPLED: profile-(2,8) chamber close

**Status:** COMPLETE PASS. Profile `(2,8)` is closed.

Run two exhaustive pieces in one 64-container wave. The refined quotient
piece covers all 531,517 order-128 and 277,957 order-64 allocations, applying
the proved `R(B,B,B)<=174` cap in the order-64 and even-inner chambers and
reporting the order-128 inner-`4Z` split. The exact support piece covers all
`binom(15,8)*1232=7,927,920` weighted supports in the remaining
`B subset 4Z` chamber. Its outer supplement has two positive representatives,
at least one odd, and is disjoint from the eight inner representatives.

Use 16 shards at each quotient order and 32 support shards, one CPU and
256 MiB per task, at most 64 concurrent containers, 120 seconds per function,
and 110 seconds per subprocess. The conservative campaign wall ceiling is
below three minutes and the cost ceiling is below `$0.20`. The launcher
checkpoints every result and records worker durations. The independent checker
recounts both quotient universes, all 7,927,920 supports, every quotient
candidate, both source hashes, and every exact support maximum.

`PASS` requires the order-64 global refined cap, order-128 outside-inner-`4Z`
cap, and exact inner-`4Z` support cap all to be at most 1947. It closes the
profile `(2,8)` at `V=68`. `FAIL` returns an exact quotient allocation or
weighted support in the surviving chamber. `INCOMPLETE` changes no status.
Do not broaden the campaign to any other profile.

Modal app `ap-8xzV3fZniv8jms4V2EI19N` completed all 64 tasks in 22.02
seconds of client-observed wall time. Worker durations range from 0.031 to
0.673 seconds and total 17.624 seconds. The independent checker reconstructed
all 809,474 quotient allocations and 7,927,920 exact supports, obtaining

```text
order-64 refined quotient maximum          1942,
order-128 outside-inner-4Z maximum         1942,
order-128 inner-4Z exact support maximum   1536.
```

This is the declared `PASS`: profile `(2,8)` is excluded at `V=68`. The
result is consumed by `e1_n256_s16_e34_three_profile_reduction`. No rerun or
extension is authorized.

#### CR-E1-E34-QUARTER: normalized quarter-template close

**Status:** COMPLETE PASS. The quarter heavy-position template is closed; no
rerun or extension is authorized.

The heavy-template theorem normalizes the branch to `H={0,32,64}`, opposite
outer heavy signs, no light at `96`, 124 possible light positions, two middle
heavy signs, and sixteen light-sign patterns. The exact universe is
`binom(124,4)*32=300,200,032` vectors.

The primary implementation groups unordered signed chords. The independent
audit forms `F(X)F(X^-1)` directly in `Z[X]/(X^128+1)`. Each uses 121 shards,
one CPU and 256 MiB per task, 60-second function caps, at most 100 containers,
and partial packet writes. `PASS` requires exact shard coverage, shardwise
agreement on all counts and maxima, and `M_3<=1947` on every full-conductor
profile-`(6,7)` vector.

Modal apps `ap-kLTKBwJM3lNWUZA3hul5w7` and
`ap-XXTZkD7kcupvXULmbp2GKZ` completed in under 30 client-observed seconds
each, using 45.781851 and 52.691880 aggregate worker-seconds. They agree on

```text
E=34 vectors                       1,514,544,
profile-(6,7) vectors              1,181,056,
full-conductor profile vectors     1,031,680,
maximum full-conductor M_3              1188.
```

The combined conservative cost ceiling was `$0.15`; actual worker usage was
98.473731 CPU-seconds. The exact maximum is 759 below the cubic threshold, so
`e1_n256_s16_e34_quarter_template_exclusion` closes the branch.

#### CR-E1-E34-NONQUARTER-DIAMETER: exact weld-chamber decision

**Status:** COMPLETE PASS. The nonquarter-diameter template is closed; no
rerun or extension is authorized.

The proved weld reduction gives 31 normalized heavy triples
`H={0,64,t}`, `1<=t<=31`, and exactly 915,125 admissible light supports per
triple. With four residual heavy-sign choices and sixteen light-sign choices,
the complete chamber has 1,815,608,000 signed vectors.

The primary implementation groups 21 unordered signed chords. The independent
audit forms `F(X)F(X^-1)` directly in `Z[X]/(X^128+1)` and reconstructs weld
eligibility from circular distances. Each uses 31 one-CPU, 256 MiB tasks with
60-second function caps, at most 31 containers, and a partial packet write
after every return. Abort the campaign after five client-observed minutes or
any task timeout. The conservative combined cost ceiling is `$0.90`; do not
rerun or extend without a new route decision.

`PASS` requires exact coverage, 915,125 supports per `t`, shardwise agreement
of every count and maximum, and replay of retained witnesses. If the maximum
full-conductor profile-`(6,7)` moment is at most 1947, the inherited exact
cubic certificate closes the branch. Otherwise the packet must retain exact
extremizers and the branch remains open at the first failing `t`/sign class.

Modal apps `ap-EfGZditRQm7eDLLLWpNiSA` and
`ap-MQpKibQl8PBqzuhB5DKf2m` completed all 31 tasks without retries, using
271.301709 and 339.920267 aggregate worker-seconds. The two implementations
agree shardwise on

```text
light supports                       28,368,875,
normalized signed vectors         1,815,608,000,
E=34 vectors                           1,518,816,
profile-(6,7) vectors                  1,044,528,
full-conductor profile vectors          899,456,
maximum full-conductor M_3                  1560.
```

The combined 611.221976 worker-seconds remain below the declared conservative
`$0.90` ceiling. Since `1560<1947`, the inherited cubic certificate closes
the complete nonquarter-diameter branch.

#### CR-E1-E34-PROGRESSION: five-orbit exact chamber decision

**Status:** COMPLETE PASS. The progression template is closed; no rerun or
extension is authorized.

The proved progression reduction leaves 62 heavy-step forms, opposite outer
heavy signs, and 1,195,965 welded supports per form. Odd cyclotomic
automorphisms preserve every load-bearing invariant and reduce the complete
decision to representatives `t=1,2,4,8,16`, containing 191,354,400 signed
vectors in total.

The primary implementation groups unordered signed chords. The independent
audit forms the ordered negacyclic product and reconstructs the singleton weld
from circular distances. Each uses five one-CPU, 256 MiB tasks with 60-second
caps, at most five containers, and partial packet writes. Abort on any timeout
or incomplete shard. The combined conservative cost ceiling is `$0.20`; no
rerun or extension is authorized without a new route decision.

`PASS` requires exact five-shard coverage, 1,195,965 supports per
representative, shardwise agreement of all fields, replay of retained
witnesses, and exact weighting by orbit multiplicities `32,16,8,4,2`. A
maximum `M_3<=1947` closes all 62 progression forms by unit transport;
otherwise retain the first exact failing representative and keep the branch
open.

Modal apps `ap-i5ZUL3DXjsMVeoSd2KwzT4` and
`ap-x6NGO4WBkgu0GbaGBpeQim` completed all five tasks without retries, using
29.943997 and 50.977832 aggregate worker-seconds. They agree shardwise. The
five representatives contain

```text
supports              5,979,825,
signed vectors       191,354,400,
E=34 vectors             603,832,
profile-(6,7) vectors    404,212,
full-conductor vectors   329,776.
```

Exact orbit weighting gives 3,131,008 full-conductor profile vectors over all
62 forms. The maximum is `M_3=1722`, attained in the odd-step orbit. The
combined 80.921829 worker-seconds remain below the `$0.20` ceiling. Since
`1722<1947`, unit transport and the inherited cubic certificate close the
complete progression branch.

#### CR-E1-E34-GENERIC-ORBITS: affine three-weld route classifier

**Status:** COMPLETE PASS. The route classifier is banked; no rerun is
authorized.

Before any generic-vector census, classify all 325,376 generic heavy triples
under translations and odd cyclotomic units. The primary implementation maps
every triple to a canonical form. The independent audit generates full affine
orbits and removes them from the exact triple set. For each representative,
both compute the three heavy-light weld sets, all intersections, and the exact
four-light support count by inclusion-exclusion.

Run two one-CPU, 256 MiB tasks with 60-second caps and at most two containers.
Abort on any timeout or disagreement. The conservative cost ceiling is
`$0.05`. This campaign is route classification only: it may promote a proved
normal-form reduction, but it cannot exclude the generic template without a
separate signed profile/moment certificate.

Modal app `ap-RX2pnnmJRiFhsRSBEJS6To` completed both implementations in
1.110289 aggregate worker-seconds. They agree exactly: the 325,376 generic
heavy triples form 57 affine odd-unit orbits. The three-weld ledgers have
exactly three shapes:

```text
rows  weld sizes  pair intersections  triple  union  supports
 52    4,4,4           1,1,1             0      9     66,405
  4    3,4,4           2,1,1             0      7     72,486
  1    3,4,3           2,1,2             0      5     58,325.
```

After four heavy-sign and sixteen light-sign choices, the exact representative
chamber has 243,285,056 signed vectors. The campaign cost is below `$0.05`.
This closes route classification only; profile and moment remain unpaid.

#### CR-E1-E34-GENERIC-CENSUS: final affine-orbit chamber decision

**Status:** COMPLETE PASS. The generic template and E34 endpoint are closed;
no rerun or extension is authorized.

The proved generic affine-weld reduction leaves exactly 57 representatives,
58,325 to 72,486 supports per representative, and 243,285,056 normalized
signed vectors. The primary implementation groups unordered signed chords.
The independent audit uses ordered negacyclic multiplication and independently
reconstructs weld membership from circular distances.

Run 57 tasks per implementation with one CPU, 256 MiB, 60-second caps, and at
most 45 containers per app so concurrent usage cannot exceed 90 containers.
Write a partial packet after every return and abort on any timeout or mismatch.
The combined conservative cost ceiling is `$0.20`; no rerun or extension is
authorized without a new route decision.

`PASS` requires exact agreement with the orbit packet's support count, all 57
shards, shardwise count/max agreement, and retained-witness replay. A maximum
`M_3<=1947` closes the generic branch and therefore the full `E=34` endpoint;
otherwise retain the first failing orbit and keep E34 open.

Modal apps `ap-XpmKEOhClEfy8STvFbMH9y` and
`ap-GUW2NuOkVnhQDU4jUvepbZ` completed all 57 tasks without retries, using
34.471246 and 50.538048 aggregate worker-seconds. They agree shardwise on

```text
light supports                         3,801,329,
normalized signed vectors            243,285,056,
E=34 vectors                              793,742,
profile-(6,7) vectors                     505,466,
full-conductor profile vectors            418,464,
maximum full-conductor M_3                    1770.
```

The maximum occurs in orbit 14, represented by `H={0,1,19}`. The combined
85.009294 worker-seconds remain below the `$0.20` ceiling. Since `1770<1947`,
the inherited cubic certificate closes the generic template. Together with
the quarter, nonquarter-diameter, and progression exclusions, this closes the
complete `E=34`, `V=68` endpoint.

#### CR-E1-V36-WITNESS-NORM: full-conductor falsifier decision

**Status:** COMPLETE NO-HIT. No rerun is authorized for this witness.

The proved proper-conductor packet contains a full-conductor folded-`(3,4,0)`
vector at `V=36`. Compute its resultant with `x^128+1`, divide by the exact
2-adic valuation, and test the odd part for primality independently in FLINT
and PARI. A prime odd part in `(2^250,2^256)` is an immediate candidate
collision row and triggers exact pair-feasibility replay; a composite or
undersized odd part kills this particular falsifier without supporting a
universal exclusion.

Run one one-CPU, 256 MiB Modal task with a 60-second hard timeout and no
retries. The source prints a complete or explicit incomplete packet and both
engine outputs must agree. Conservative cost is below `$0.02`. App ID and
measured worker time are recorded after the single launch; no rerun is
authorized without a changed witness or a failed infrastructure launch.

Modal app `ap-w5NVLM6qks58oQP9KHXi9G` completed in `0.063751`
worker-seconds. FLINT and PARI agree on the 249-bit norm

```text
713716409960669519192598736974780038395771519667874695041952783752312355842.
```

Its valuation is one. The 248-bit odd part is prime and congruent to one
modulo 256, but is below `2^250`, so this exact vector cannot collide on the
pair-feasible branch. The compact packet is
`e1_v36_full_conductor_witness_norm_result.json`; its deterministic arithmetic
and source-hash checker is `e1_v36_full_conductor_witness_norm_check.py`.

#### CR-E1-E26-TOP-MASK-PILOT: actual-vector falsifier search

**Status:** COMPLETE NO-HIT. This bounded pilot is superseded by the complete
four-profile census below; no rerun is authorized.

The exact E26 odd-mask relaxation leaves every light mask alive, but ranks the
two cheap profiles `(4,1,2)` and `(6,1,0,1)` by attainable `M_3`. Census the
top 16 normalized light representatives for each profile, retaining the 32
highest-`M_3` full-conductor vectors per task for exact norm follow-up. The
pilot covers exactly `32*binom(124,3)*64=635,133,952` signed vectors; it makes no
claim about the other 1,202 masks.

Run 32 one-CPU, 256 MiB tasks with 60-second hard timeouts and at most 32
containers. The launcher writes a partial result after each return, checks
every actual maximum against the exact relaxation maximum, and aborts on any
timeout or malformed row. Conservative total cost is below `$0.10` and total
wall time below five minutes. A retained odd prime norm part above `2^250`
triggers independent collision replay; no hit only retires this ranked pilot.

Modal app `ap-L2vmgKMlAx8lsHkCxmzySB` completed all 32 tasks without retry,
covering exactly 635,133,952 vectors in `68.453854` aggregate worker-seconds.
It found 614 profile vectors, 560 above `M_3=228`, and 44 full-conductor
exceptions on seven masks. Their maximum full-conductor third moment is 624.
Modal app `ap-sSRw4M4r3Lo3CFYJzKwm74` completed dual FLINT/PARI norm and
primality evaluation of all 44 retained vectors. The engines agree on 22
distinct norms. The 247-bit maximum is

```text
206300578845256388660989325009715100926350250639065957504774519402224202242.
```

Six odd parts are prime, but none reaches the pair-feasible floor `2^250`, so
the pilot finds no collision row. The complete census and norm packet below
now covers the other 1,202 masks as well.

#### CR-E1-E26-FOUR-PROFILE-CENSUS: complete six-odd endpoint decision

**Status:** COMPLETE PASS. The four profiles and the full `V=52` endpoint are
closed; no rerun is authorized.

The proved six-odd atlas has exactly 1,234 odd masks and one affine light orbit
per mask. For every representative, choose all heavy triples from the other
124 positions and all 64 relative sign vectors. One pass therefore covers
exactly `1,234*binom(124,3)*64=24,492,353,024` vectors and classifies all four
live profiles simultaneously. The production engine uses folded signed
chords; the audit engine independently forms the direct negacyclic product.
Retain every full-conductor vector above `M_3=228` for dual exact norms.

Run the engines sequentially, each with 1,234 one-CPU, 256 MiB tasks, 60-second
task caps, and at most 100 containers. Checkpoint every 16 returns and abort
on timeout, malformed output, or row disagreement. The 32-mask pilot measured
`68.453854` worker-seconds for 635,133,952 vectors, projecting about 2,640
worker-seconds per engine. Conservative combined cost is below `$0.50` and
wall time below five minutes. A prime odd norm part above `2^250` triggers
collision replay; otherwise exact norms below threshold close the endpoint.

Infrastructure launch `ap-Jq5ilys1UDMuhHb04wAVdk` failed during worker module
import because local path resolution assumed the checkout directory depth.
It completed `0/1,234` production and `0/1,234` audit tasks and supplies no
mathematical evidence. One import-safe retry was authorized under the stated
budget; no computational retry was authorized.

Import-safe Modal app `ap-w01euXu1uuSZMynixEsU9m` completed all 1,234
production and all 1,234 audit tasks. Modal transparently restarted two
preempted containers on the same inputs. The two independent engines agree
row by row after 24,492,353,024 vectors each:

```text
profile       vectors   M_3>228   full conductor   max M_3   full max
(6,5)          51,562      48,918           32,096       1074       1062
(5,3,1)        23,884      23,232           12,632        942        942
(4,1,2)         1,614       1,590              408        870        690
(6,1,0,1)       1,788         874              272        606        606
total          78,848      74,614           45,408
```

The production and audit engines used `2707.686703` and `5063.911652`
aggregate worker-seconds. The proper-conductor theorem removes the
`74,614-45,408=29,206` imprimitive exceptions.

Modal app `ap-B13nYXtQQsbfCqFKDPTeUr` computed every remaining norm in FLINT
and PARI in 46 batches. The engines agree entry by entry on 45,408 vectors and
20,636 distinct norms. Their common maximum is

```text
1139098407599461804511111865916270680930143333943822578584573946997885235216
```

and satisfies `N_max<2^250<2*N_max`. No norm reaches `2^250`; hence no
pair-feasible collision survives, all four profiles are excluded, and the
live positive even frontier advances to `V<=50`.

#### CR-E1-E25-ROUTER: exact last-live-majorant route decision

**Status:** COMPLETE PASS. The exact router is banked; no rerun is authorized.

At `N=256`, folded profile `(3,4,0)`, and `V=50` (`E=25`), derive the exact
positive-half L1 bound, enumerate every compatible integer magnitude profile,
certify the cubic-Hermite sign change at `M_3=13/14`, apply diameter parity,
and price the surviving profiles against the already-proved one-diameter
light atlas. This is a router only and must not claim any profile exclusion.

Run one one-CPU, 256 MiB Modal task with a 60-second hard timeout. The local
launcher must write the complete JSON packet, and the prepared independent
checker must reconstruct the profile ledger, the exact rational sign change,
the atlas usage, and the direct-census floor. Conservative cost is below
`$0.01`. A large surviving router or a cutoff below all attainable moments is
a route boundary, not authorization for an undifferentiated norm campaign.

Infrastructure app `ap-0xK5g91qR7LZzevi5tScu5` failed while importing the
remote module because checkout-depth path resolution ran at module scope. It
completed no computation and supplies no mathematical evidence. The one
authorized import-safe retry follows; no further retry is authorized.

Import-safe app `ap-Bmu0kinryPMCm1zYI5CWas` completed the single task. The
independent checker confirms `L<=15`, 12 energy profiles, the exact
`M_3=13/14` sign change, and nine parity survivors: five with one odd class
and four with five odd classes. They occupy 111 proved affine light templates,
giving a direct floor of 2,203,120,896 vectors per engine. The router excludes
no profile by itself.

#### CR-E1-E25-NINE-PROFILE-CENSUS: exact actual-vector route decision

**Status:** COMPLETE PASS. The bounded primitive remainder authorizes the
dual exact-norm pass below; no census rerun is authorized.

Run the exact E25 router's 111 affine templates through folded-chord and
direct-negacyclic engines. Each engine covers
`111*binom(124,3)*64=2,203,120,896` signed vectors. Record exact per-profile
counts, minimum and maximum `M_3`, conductor counts, and every vector above
the cutoff `M_3=13`. This decides whether exact norms remain a bounded route;
it does not itself prove an exclusion.

Run 111 one-CPU, 256 MiB tasks per engine, sequential engine passes, 60-second
task caps, and at most 100 containers. Checkpoint every 16 returns and preserve
partial rows on failure. The prepared checker replays every retained vector
and compares the two engines row by row. The identical E29 router size and
measured E26 throughput put conservative cost below `$0.15` and wall time
below five minutes. If the retained primitive set is too large for a bounded
dual norm pass, stop and seek an algebraic filter instead.

Modal app `ap-GPkfA9swDimrWIrdVL3u7Z` completed all 111 production and all 111
audit rows without retry. Folded-chord and direct-negacyclic engines agree
exactly after 2,203,120,896 vectors each:

```text
profile       vectors   M_3>13   full conductor   min/max full M_3
(5,5)          12,156     12,156            6,944          60/900
(1,6)          11,884     11,628            6,888           0/720
(4,3,1)         5,526      5,526            2,868         120/696
(0,4,1)           416        352               32           0/276
(3,1,2)           632        632              116         120/480
(5,1,0,1)         238        238               56          96/384
(1,2,0,1)         812        748               80           0/240
(0,0,1,1)          16          0                0             --
(0,0,0,0,1)         6          0                0             --
total           31,686     31,280           16,984
```

The complete dual pass used `250.331735` aggregate production worker-seconds;
the audit summary agrees exactly. The proper-conductor theorem removes the
other `31,280-16,984=14,296` cubic exceptions. Since only 16,984 primitive
vectors remain, exact dual norms are bounded and cheaper than the completed
E26 norm packet.

#### CR-E1-E25-NINE-PROFILE-NORMS: exact endpoint decision

**Status:** COMPLETE PASS. The nine profiles and `V=50` endpoint are closed;
no rerun is authorized.

Compute `Res(g,x^128+1)` for all 16,984 full-conductor E25 vectors above
`M_3=13`, in 17 batches of at most 1,000. Compare FLINT and PARI entry by
entry, record profile maxima, and independently test every odd part in the
pair-feasible interval `(2^250,2^256)` for primality. A prime eligible odd
part becomes an explicit collision-row candidate requiring exact replay; if
all norms are below `2^250`, the nine profiles and the `V=50` endpoint close.

Run one-CPU, 256 MiB tasks with 60-second hard caps and at most 100 containers.
Checkpoint every four batches and preserve partial output on failure. The
prepared checker binds the census and source hashes, compares both norm
ledgers, reconstructs all profile maxima and candidate records, and checks
coverage. Based on the completed 45,408-vector E26 packet, conservative cost
is below `$0.10` and wall time below two minutes.

Modal app `ap-P7nLJ3MSSHmUrHb9P2RSoX` completed all 17 FLINT and all 17 PARI
batches without retry. The systems agree entry by entry on 16,984 vectors and
3,727 distinct norms. Their common maximum is

```text
689346143769176281255733260656192958605975198224651023251426809106119000068
```

and satisfies `2*N_max<2^250<3*N_max`. No norm reaches `2^250`; there are no
eligible odd parts and no candidate collision rows. All nine E25 profiles are
excluded and the live positive even frontier advances to `V<=48`.

#### CR-E1-E17-ROUTER: exact cutoff-free V=34 route decision

**Status:** COMPLETE PASS. The exact router is banked; no rerun is authorized.

At `N=256`, folded profile `(3,4,0)`, and `V=34` (`E=17`), derive the exact
positive-half L1 bound, enumerate every compatible integer magnitude profile,
apply the one-diameter parity constraint, and price the surviving odd profiles
against the already-proved one/three/five-odd light atlas. This is a router
only: it closes no profile and changes no DAG status.

Run one one-CPU, 256 MiB Modal task with a 60-second hard timeout. The launcher
writes a complete deterministic JSON packet. The prepared independent checker
reconstructs the slack minima, magnitude profiles, layer caps, parity split,
matching ledger, atlas use, and direct-census floor without importing the
primary implementations. Conservative wall time is below one minute and cost
below `$0.01`.

PASS records the exact finite router and permits a separately priced actual-
vector census only if the workload and expected retained residue are bounded.
FAIL falsifies the proposed E17 routing specialization and returns the route
to analytic derivation. INCOMPLETE is evidence only and authorizes no retry
without a repaired source or explicit new route decision.

Infrastructure app `ap-KqmsjnSeuKSHccRguoGspV` mounted only the entry file,
failed during worker import of a local helper, and was explicitly aborted. It
completed no mathematical task and supplies no evidence. The self-contained
repair below is the single authorized retry; no second retry is authorized.

Self-contained app `ap-c8VmO1f95T4RM21QCIoMbA` completed the single task. The
independent checker reconstructs `L<=11`, six profiles, rejection of the
nine-odd profile `(8,0,1)`, and five surviving profiles: three one-odd and two
five-odd. They occupy 111 proved affine templates, giving a direct floor of
`2,203,120,896` vectors per engine. The router excludes no surviving profile.

#### CR-E1-E17-FIVE-PROFILE-CENSUS: exact actual-vector route decision

**Status:** COMPLETE PASS. The primitive residue is banked; no rerun is authorized.

Run the exact E17 router's 111 one/five-odd affine templates through two
independent engines. The primary engine uses folded oriented chords; the audit
engine directly multiplies in `Z[x]/(x^128+1)`. Each covers
`111*binom(124,3)*64=2,203,120,896` vectors. Record exact profile and conductor
counts and retain every full-conductor vector for a separately priced norm
decision. This census alone proves no endpoint exclusion.

Use at most 100 one-CPU, 256 MiB workers with 60-second task caps, checkpoint
every 16 returns, and abort on timeout, malformed output, or row disagreement.
The completed same-size E21/E25 campaigns put conservative wall time below
five minutes and cost below `$0.15`. The prepared checker reconstructs every
retained vector by direct negacyclic multiplication and checks source hashes,
atlas coverage, conductor, profiles, engine equality, and one hostile mutation.

PASS authorizes an exact norm campaign only if the retained primitive set is
small enough to keep its own conservative cost below `$0.10`. FAIL returns to
the engine or atlas derivation. INCOMPLETE retains partial rows as evidence
only and authorizes no automatic retry.

Modal app `ap-wX3VHEQgXjopXqefRieIpQ` completed all 154 rows without retry.
The folded-chord and direct-negacyclic engines agree exactly after
`3,056,582,144` vectors each:

```text
profile       actual   full conductor   proper conductor
(4,3)            530              162                368
(0,4)              0                0                  0
(3,1,1)          158               16                142
(0,0,0,1)          0                0                  0
total             688              178                510
```

The dual pass used `959.740393` aggregate worker-seconds. The independent
checker replays all 178 retained vectors exactly. Exhaustive emptiness removes
two profiles, and the proper-conductor theorem removes another 510 vectors.
The 178-vector primitive residue authorizes the bounded norm decision below.

#### CR-E1-E16-FOUR-PROFILE-NORMS: exact endpoint decision

**Status:** AUTHORIZED, not yet launched.

Compute `abs(Res(g,x^128+1))` for all 178 full-conductor E16 vectors in one
FLINT batch and one independently evaluated PARI/GP batch. Strip the exact
2-adic valuation before applying the row-prime cutoff. Whole-norm size is
diagnostic only.

Use one CPU and 256 MiB per engine with 60-second hard caps and at most two
containers. Preserve partial packets on failure. Conservative cost is below
`$0.01` and wall time below one minute. The prepared checker binds the census
and source hashes, compares all 178 norms entry by entry, reconstructs 2-adic
valuations and profile maxima, enforces the odd-part cutoff, and mutates one
engine ledger.

PASS with every odd part below `2^250` closes all four routed profiles and
V=32. Any odd-part hit requires exact factor/divisibility replay and does not
close the endpoint. INCOMPLETE supplies no status change and authorizes no
automatic retry.

Modal app `ap-nuzv6imnkUH0ElJlCLyKRy` completed all 111 rows without retry.
The folded-chord and direct-negacyclic engines agree exactly after
`2,203,120,896` vectors each:

```text
profile       actual   full conductor   proper conductor
(5,3)            608              196                412
(1,4)          1,152              272                880
(4,1,1)          188               20                168
(0,2,1)           92                0                 92
(1,0,0,1)         10                0                 10
total           2,050              488              1,562
```

The dual pass used `651.957882` aggregate worker-seconds. The independent
checker replays all 488 retained vectors exactly. The proper-conductor theorem
removes the other 1,562 vectors; the 488-vector primitive residue authorizes
the bounded norm decision below.

#### CR-E1-E17-FIVE-PROFILE-NORMS: exact endpoint decision

**Status:** COMPLETE PASS. The five profiles and V=34 are closed; no rerun is authorized.

Compute `abs(Res(g,x^128+1))` for all 488 full-conductor E17 vectors in one
FLINT batch and one independently evaluated PARI/GP batch. Strip the exact
2-adic valuation before applying the row-prime cutoff: because every
admissible row prime is odd and exceeds `2^250`, an odd part below `2^250`
cannot vanish modulo that prime. Whole-norm size alone is diagnostic only.

Use one CPU and 256 MiB per engine with 60-second hard caps and at most two
containers. Preserve partial packets on failure. Conservative cost is below
`$0.01` and wall time below one minute. The prepared checker binds the census
and source hashes, compares all 488 norms entry by entry, reconstructs 2-adic
valuations and profile maxima, enforces the odd-part cutoff, and mutates one
engine ledger.

PASS with every odd part below `2^250` closes all five profiles and V=34.
Any odd-part hit becomes a candidate requiring exact factor/divisibility
replay and does not close the endpoint. INCOMPLETE supplies no status change
and authorizes no automatic retry.

Modal app `ap-YS86fN9k5a8svWi6zF2boU` completed one FLINT and one PARI batch.
The systems agree entry by entry on all 488 vectors and 108 distinct norms.
The whole-norm maximum is

```text
2816861446662266258222239103326104068711609833031798890850684996153986296836
```

and 16 whole norms reach `2^250`. Their exact 2-adic reductions have maximum
odd part

```text
744372174442013450465816409476894770650462784978029532566873973061928116737
```

with `2*odd_max<2^250<3*odd_max`. There are zero odd-part threshold hits.
The independent checker reproduces every norm, valuation, profile maximum,
threshold count, and maximizing index and rejects one mutated engine ledger.
All five E17 profiles and the V=34 endpoint are therefore closed; the live
positive even frontier advances to `V<=32`.

#### CR-E1-E16-ROUTER: exact cutoff-free V=32 route decision

**Status:** COMPLETE PASS. The router is proved; no rerun is authorized.

At `N=256`, folded profile `(3,4,0)`, and `V=32` (`E=16`), derive the exact
positive-half L1 bound, enumerate every compatible integer magnitude profile,
apply the zero/two-light-diameter parity constraint, and price the surviving
even profiles against the already-proved zero/two/four/six-odd light atlas.
This is a router only and changes no DAG status.

Run one one-CPU, 256 MiB Modal task with a 60-second hard timeout. The launcher
writes a complete deterministic JSON packet. The prepared independent checker
reconstructs the slack minima, magnitude profiles, layer caps, parity split,
matching ledgers, atlas use, and direct-census floor without importing the
primary implementations. Conservative wall time is below one minute and cost
below `$0.01`.

PASS records the exact finite router and permits a separately priced census
only if its workload is already calibrated below `$0.20`. FAIL returns to the
analytic derivation. INCOMPLETE is evidence only and authorizes no automatic
retry.

Modal app `ap-UNOcTGZLQStD1pUQnlIcQG` completed the single task. The
independent checker reconstructs `L<=10`, five energy profiles, rejection of
the eight-odd profile `(7,0,1)`, and four surviving profiles: two zero-odd and
two four-odd. They occupy 154 proved affine templates, giving a direct floor
of `3,056,582,144` vectors per engine. The router excludes no survivor.

#### CR-E1-E16-FOUR-PROFILE-CENSUS: exact actual-vector route decision

**Status:** COMPLETE PASS. The census is source-pinned; no rerun is authorized.

Run the exact E16 router's 154 zero/four-odd affine templates through two
independent engines. The primary engine uses folded oriented chords; the audit
engine directly multiplies in `Z[x]/(x^128+1)`. Each covers
`154*binom(124,3)*64=3,056,582,144` vectors. Record exact profile and conductor
counts and retain every full-conductor vector for a separately priced norm
decision. This census alone proves no endpoint exclusion.

Use at most 100 one-CPU, 256 MiB workers with 60-second task caps, checkpoint
every 16 returns, and abort on timeout, malformed output, or row disagreement.
The completed same-size E20 campaign puts conservative wall time below five
minutes and cost below `$0.15`. The prepared checker reconstructs every
retained vector by direct negacyclic multiplication and checks source hashes,
atlas coverage, conductor, profiles, engine equality, and one hostile mutation.

PASS authorizes an exact norm campaign only if the retained primitive set is
small enough to keep its own conservative cost below `$0.10`. FAIL returns to
the engine or atlas derivation. INCOMPLETE retains partial rows as evidence
only and authorizes no automatic retry.

Modal app `ap-wX3VHEQgXjopXqefRieIpQ` completed all 154 templates. The two
engines agree row by row after `3,056,582,144` vectors each. In profile order
`(4,3),(0,4),(3,1,1),(0,0,0,1)`, actual counts are `[530,0,158,0]`,
full-conductor counts are `[162,0,16,0]`, and proper-conductor counts are
`[368,0,142,0]`. Thus 688 actual vectors reduce to 178 retained
full-conductor representatives; both zero-odd routed profiles are exactly
empty. Aggregate dual worker time was 959.740 seconds. The independent
checker reproduces every retained vector and rejects one mutated row.

#### CR-E1-E16-FOUR-PROFILE-NORMS: exact endpoint decision

**Status:** COMPLETE PASS. The four profiles and V=32 are closed; no rerun is authorized.

Compute `abs(Res(g,x^128+1))` for all 178 full-conductor E16 vectors in one
FLINT engine and one PARI/GP engine. Record exact powers of two and odd parts,
because the pair-feasible row prime is odd and exceeds `2^250`. The campaign
uses two one-CPU, 256 MiB Modal tasks and is priced below `$0.01`.

PASS requires exact engine agreement, positive norms, and every odd part below
`2^250`. FAIL produces a candidate norm witness. INCOMPLETE is evidence only
and authorizes no automatic retry.

Modal app `ap-NKEaivIgiXPWHEwHeBgkkM` completed both engines. They agree on all
178 vectors and 78 distinct norms. The exact whole-norm maximum is

```text
3310692535087337739109785704249356622971820103039851493935549506897278325762
```

and ten whole norms reach `2^250`. Their exact 2-adic reductions have maximum
odd part

```text
1655346267543668869554892852124678311485910051519925746967774753448639162881
```

with `odd_max<2^250<2*odd_max`. There are zero odd-part threshold hits. The
independent checker reproduces every norm, valuation, profile maximum,
threshold count, and maximizing index and rejects one mutated engine ledger.
All four E16 profiles and the V=32 endpoint are therefore closed; the live
positive even frontier advances to `V<=30`.

#### CR-E1-E15-ROUTER: exact cutoff-free V=30 route decision

**Status:** COMPLETE PASS. The router is source-pinned; no rerun is authorized.

At `N=256`, folded profile `(3,4,0)`, and `V=30` (`E=15`), derive the exact
positive-half L1 bound, enumerate every compatible integer magnitude profile,
apply the one-light-diameter parity constraint, and price the surviving odd
profiles against the already-proved one/three/five-odd light atlas. This is a
router only and changes no DAG status.

Run one one-CPU, 256 MiB Modal task with a 60-second hard timeout. The launcher
writes a complete deterministic JSON packet. The prepared independent checker
reconstructs the slack minima, magnitude profiles, layer caps, parity split,
matching ledger, atlas use, and direct-census floor without importing the
primary implementations. Conservative wall time is below one minute and cost
below `$0.01`.

PASS records the exact finite router and permits a separately priced census
only if its workload is calibrated below `$0.20`. FAIL returns to the analytic
derivation. INCOMPLETE is evidence only and authorizes no automatic retry.

Modal app `ap-4uZGK1UWEjeAnhVm6de5UE` completed the single task. The
independent checker reconstructs `L<=9`, three energy profiles, rejection of
the seven-odd profile `(6,0,1)`, and the two surviving three-odd profiles
`(3,3)` and `(2,1,1)`. They occupy eight proved affine templates, giving a
direct floor of `158,783,488` vectors per engine. The router excludes no
survivor.

#### CR-E1-E15-TWO-PROFILE-CENSUS: exact actual-vector route decision

**Status:** COMPLETE PASS. The census is source-pinned; no rerun is authorized.

Run the exact E15 router's eight three-odd affine templates through two
independent engines. The primary engine uses folded oriented chords; the audit
engine directly multiplies in `Z[x]/(x^128+1)`. Each covers
`8*binom(124,3)*64=158,783,488` vectors. Record exact profile and conductor
counts and retain every full-conductor vector for a separately priced norm
decision. This census alone proves no endpoint exclusion.

Use eight one-CPU, 256 MiB workers with 60-second task caps and checkpoint
after every return. The completed same-size E19 campaign puts conservative
wall time below two minutes and cost below `$0.03`. The prepared checker
reconstructs every retained vector by direct negacyclic multiplication and
checks source hashes, atlas coverage, conductor, profiles, engine equality,
and one hostile mutation.

PASS authorizes an exact norm campaign only if the retained primitive set is
small enough to keep its own conservative cost below `$0.10`. FAIL returns to
the engine or atlas derivation. INCOMPLETE retains partial rows as evidence
only and authorizes no automatic retry.

Modal app `ap-xIQLyhRtHtlRxbQkOIS7Yp` completed all eight templates. The two
engines agree row by row after `158,783,488` vectors each. In profile order
`(3,3),(2,1,1)`, actual counts are `[258,36]`, full-conductor counts are
`[64,0]`, and proper-conductor counts are `[194,36]`. Thus 294 actual vectors
reduce to 64 retained full-conductor representatives; the second profile is
entirely proper-conductor. Aggregate dual worker time was 52.945 seconds. The
independent checker reproduces every retained vector and rejects one mutation.

#### CR-E1-E15-TWO-PROFILE-NORMS: exact endpoint decision

**Status:** COMPLETE PASS. Both profiles and V=30 are closed; no rerun is authorized.

Compute `abs(Res(g,x^128+1))` for all 64 full-conductor E15 vectors in one
FLINT engine and one PARI/GP engine. Record exact powers of two and odd parts,
because the pair-feasible row prime is odd and exceeds `2^250`. Use two
one-CPU, 256 MiB Modal tasks with 60-second caps. The E16 calibration puts
conservative cost below `$0.01`.

PASS requires exact engine agreement, positive norms, and every odd part below
`2^250`. FAIL produces a candidate norm witness. INCOMPLETE is evidence only
and authorizes no automatic retry.

Modal app `ap-4c65PlujVH2D5kNI12Bcac` completed both engines. They agree on
all 64 vectors and 28 distinct norms. The exact whole-norm maximum is

```text
3003171528471974836716922425205211633163258783488230570091067301168069285892
```

and 32 whole norms reach `2^250`. Their exact 2-adic reductions have maximum
odd part

```text
1263041506267492322130816623667822529962454800313964008196082776100356004097
```

with `odd_max<2^250<2*odd_max`. There are zero odd-part threshold hits. The
independent checker reproduces every norm, valuation, profile maximum,
threshold count, and maximizing index and rejects one mutated engine ledger.
Both E15 profiles and the V=30 endpoint are therefore closed; the live
positive even frontier advances to `V<=28`.

#### CR-E1-E14-ROUTER: exact cutoff-free V=28 route decision

**Status:** COMPLETE PASS. The router is source-pinned; no rerun is authorized.

At `N=256`, folded profile `(3,4,0)`, and `V=28` (`E=14`), derive the exact
positive-half L1 bound, enumerate every compatible integer magnitude profile,
apply the zero/two-light-diameter parity constraint, and price the surviving
even profiles against the already-proved zero/two/four/six-odd light atlas.
This is a router only and changes no DAG status.

Run one one-CPU, 256 MiB Modal task with a 60-second hard timeout. The launcher
writes a complete deterministic JSON packet. The prepared independent checker
reconstructs the slack minima, magnitude profiles, layer caps, parity split,
matching ledgers, atlas use, and direct-census floor without importing the
primary implementations. Conservative wall time is below one minute and cost
below `$0.01`.

PASS records the exact finite router and permits a separately priced census
only if its workload is calibrated below `$0.20`. FAIL returns to the analytic
derivation. INCOMPLETE is evidence only and authorizes no automatic retry.

Modal app `ap-rxPXBVj2USK33LIXWpg4Lo` completed the single task. The
independent checker reconstructs `L<=10` and four energy profiles. All four
survive parity: two have two odd classes and two have six. They occupy 1,321
proved affine templates, giving a direct floor of `26,219,123,456` vectors per
engine. The router excludes no survivor.

#### CR-E1-E14-FOUR-PROFILE-CENSUS: exact actual-vector route decision

**Status:** COMPLETE PASS. The census is source-pinned; no rerun is authorized.

Run the exact E14 router's 1,321 two/six-odd affine templates through two
independent engines. The primary engine uses folded oriented chords; the audit
engine directly multiplies in `Z[x]/(x^128+1)`. Each covers
`1321*binom(124,3)*64=26,219,123,456` vectors. Record exact profile and
conductor counts and retain every full-conductor vector for a separately
priced norm decision. This census alone proves no endpoint exclusion.

Use at most 100 one-CPU, 256 MiB workers with 60-second task caps, checkpoint
every 16 returns, and abort on timeout, malformed output, or row disagreement.
The completed identical-size E18 campaign puts conservative wall time below
five minutes and cost below `$0.15`. The prepared checker reconstructs every
retained vector by direct negacyclic multiplication and checks source hashes,
atlas coverage, conductor, profiles, engine equality, and one hostile mutation.

PASS authorizes an exact norm campaign only if the retained primitive set is
small enough to keep its own conservative cost below `$0.10`. FAIL returns to
the engine or atlas derivation. INCOMPLETE retains partial rows as evidence
only and authorizes no automatic retry.

Infrastructure app `ap-C2U6Lugoj5XbrqQWnS2rLs` failed while importing the
worker module because the repository path was evaluated inside the remote
container. It completed zero of 1,321 tasks, ran neither census engine, and
supplies no mathematical evidence. The path guard was repaired before the one
authorized clean rerun.

Modal app `ap-rQOuJb9DVQwka46OLEj4Er` completed all 1,321 templates. The two
engines agree row by row after `26,219,123,456` vectors each. In profile order
`(6,2),(2,3),(5,0,1),(1,1,1)`, actual counts are `[982,714,100,40]`,
full-conductor counts are `[540,184,8,4]`, and proper-conductor counts are
`[442,530,92,36]`. Thus 1,836 actual vectors reduce to 736 retained
full-conductor representatives. Aggregate dual worker time was 7,636.622
seconds. The independent checker reproduces every retained vector and rejects
one mutation.

#### CR-E1-E14-FOUR-PROFILE-NORMS: exact endpoint decision

**Status:** COMPLETE ROUTE REPAIR PASS. The norm ledger and exception audit are
source-pinned; no rerun is authorized.

Compute `abs(Res(g,x^128+1))` for all 736 full-conductor E14 vectors in one
FLINT engine and one PARI/GP engine. Record exact powers of two and odd parts,
because the pair-feasible row prime is odd and exceeds `2^250`. Use at most
eight one-CPU, 256 MiB Modal tasks with 60-second caps and batches of 200. The
completed E18 norm campaign puts conservative cost below `$0.03`.

The original PASS criterion required exact engine agreement, positive norms,
and every odd part below `2^250`. Failure produces candidate norm witnesses;
INCOMPLETE is evidence only and authorizes no automatic retry.

Modal app `ap-A7rhyHWVrOpGoAZM9bOuSs` completed four FLINT and four PARI
batches. The engines agree on all 736 positive norms, with 262 distinct
values. The whole-norm maximum is

```text
5848948255836721605243059534285585250067895734911016890819011517212606236162,
```

and 152 whole norms reach `2^250`. The maximum odd part is

```text
2924474127918360802621529767142792625033947867455508445409505758606303118081.
```

The original below-threshold shortcut therefore FAILS: six vectors have odd
part at least `2^250`. They comprise three distinct integers, all below
`2^251`, and supply the complete downstream candidate packet.

#### CR-E1-E14-LARGE-ODD-CANDIDATES: exact threshold-exception decision

**Status:** COMPLETE PASS. The classifier is source-pinned; no rerun is
authorized.

For an exceptional odd part `R_odd<2^251`, any pair-feasible prime divisor
`p>2^250` would force `R_odd=p`. Modal app
`ap-JtCD7equumzMV4qV44ziGe` ran independent PARI `isprime` and FLINT
`is_prime` classifiers on all six exceptions. The engines agree: there are
three distinct odd parts, all three are composite, and there are zero eligible
prime candidates. All three happen to be `1 mod 256`, so congruence alone does
not pay them. The independent checker reconstructs every vector, norm,
valuation, threshold, residue, and one hostile mutation. This exact repair
closes all four E14 profiles and the `V=28` endpoint; the live frontier is
`V<=26`.

#### CR-E1-E13-ROUTER: exact cutoff-free V=26 route decision

**Status:** COMPLETE PASS. The router is source-pinned; no rerun is authorized.

At `N=256`, folded profile `(3,4,0)`, and `V=26` (`E=13`), derive the exact
positive-half L1 bound, enumerate every compatible magnitude profile, apply
the one-light-diameter parity constraint, and price the survivors against the
proved one/three/five-odd atlas. This router changes no DAG status by itself.

Run one one-CPU, 256 MiB Modal task with a 60-second hard timeout. PASS requires
the independently structured checker to reproduce every slack minimum,
profile, matching ledger, atlas count, and exact direct-vector floor. FAIL
records a deterministic route inconsistency. INCOMPLETE is evidence only and
authorizes no automatic retry. Expected cost is below `$0.01`.

Modal app `ap-i2oKjwTWqN24exJmrNCPtQ` completed the single task. The independent
checker reconstructs `L<=9` and four profiles: `(5,2)`, `(1,3)`, `(4,0,1)`,
and `(0,1,1)`. Two have one odd class and two have five; no profile is rejected.
They occupy 111 proved affine templates, giving a direct floor of
`2,203,120,896` vectors per engine. The router excludes no survivor.

#### CR-E1-E13-FOUR-PROFILE-CENSUS: exact actual-vector route decision

**Status:** COMPLETE PASS. The census is source-pinned; no rerun is authorized.

Run the 111 one/five-odd affine templates through independent folded-chord and
direct-negacyclic engines. Each engine covers
`111*binom(124,3)*64=2,203,120,896` vectors. Record exact profile and conductor
counts and retain every full-conductor vector for a separately priced norm
decision. The census alone proves no endpoint exclusion.

Use at most 100 one-CPU, 256 MiB workers with 60-second task caps and checkpoint
every 16 returns. The completed identical-size E17 campaign calibrates cost
below `$0.15`. PASS requires row-by-row engine equality and independent replay
of every retained vector. FAIL returns to the engine or atlas derivation.
INCOMPLETE preserves partial rows and authorizes no automatic retry.

Modal app `ap-AhqC0lLGj9BYMLmRpKa1mj` completed all 111 templates. The engines
agree after `2,203,120,896` vectors each. In profile order
`(5,2),(1,3),(4,0,1),(0,1,1)`, actual counts are `[418,252,104,46]`,
full-conductor counts are `[112,0,16,8]`, and proper-conductor counts are
`[306,252,88,38]`. Thus 820 actual vectors reduce to 136 retained
full-conductor representatives. Aggregate dual worker time was 613.766
seconds. The independent checker reproduces every retained vector and rejects
one mutation.

#### CR-E1-E13-FOUR-PROFILE-NORMS: exact endpoint decision

**Status:** COMPLETE LEDGER PASS. Four threshold exceptions remain; no norm
rerun is authorized.

Compute exact cyclotomic norms for all 136 retained vectors in independent
FLINT and PARI engines. Record exact 2-adic valuations and odd parts without
assuming a below-threshold outcome. One batch per engine, 256 MiB per worker,
and a 60-second cap put conservative cost below `$0.01`. PASS means exact
engine agreement and a complete ledger. Any odd part at least `2^250` becomes
an explicit downstream prime candidate; it does not fail the ledger or close
the endpoint. INCOMPLETE authorizes no automatic retry.

Modal app `ap-cXvEeUhd1ym0Ep1InsluxC` completed one FLINT and one PARI batch.
The engines agree on all 136 positive norms, with 36 distinct values. The
whole-norm maximum is

```text
4937981356753691307652038461254907642619144628263052811320856547919621259264,
```

and 112 whole norms reach `2^250`. The maximum odd part is

```text
2099233185140600860850973089797376067771315496789913419840767568645748406017.
```

Four vectors have odd part in `[2^250,2^251)`. The below-threshold shortcut is
therefore false, and these four exact vectors form the complete candidate
packet for the next decision.

#### CR-E1-E13-LARGE-ODD-CANDIDATES: exact threshold-exception decision

**Status:** COMPLETE PASS. The classifier is source-pinned; no rerun is
authorized.

Run independent PARI and FLINT primality classifiers on all four exceptions.
Because every exception is below `2^251`, a pair-feasible divisor above
`2^250` must equal the whole odd part. Record primality and residue modulo 256
for every vector. Two 256 MiB workers with 60-second caps cost below `$0.01`.
PASS means exact engine agreement and a complete classification ledger; an
eligible prime is a genuine surviving collision candidate rather than a
checker failure.

Modal app `ap-a4p98JmkMEXvNaIRL7bXzV` completed both classifiers. The four
exceptions comprise two distinct odd parts. Both are composite, all four
values are `1 mod 256`, and there are zero eligible prime candidates. The
independent checker reconstructs every vector, norm, valuation, threshold,
residue, and one hostile mutation. This closes all four E13 profiles and the
`V=26` endpoint; the live frontier advances to `V<=24`.

#### CR-E1-PROFILE-36-M32-PRIMARY: exact cofactor-32 direct census

**Status:** COMPLETE PRIMARY AND AUDIT PASS. All authoritative packets are
source-pinned; no rerun is authorized unless a pinned source changes.

At `N=256`, profile `(3,6,S=18)`, and cofactor `m=32`, enumerate the complete
19,840-orbit multiplicity-five atlas. The exact product ledger contracts 1,834
`(E,q,L)` records to 474 live records through `E=60`; the direct engine then
uses the proved parity-radius filter, exact autocorrelation energy, and
Arb-audited 48-bit fixed-root intervals. Retain every high-side witness.

The calibrated one-CPU benchmark covers one orbit at every parity weight
`q=3,...,15`, agrees exactly with the pre-optimization engine on every count,
and projects about 10.5 worker-hours. Run 1,240 batches of at most 16 orbits,
at most 100 one-CPU 256 MiB containers, with 60-second hard task caps and an
atomic partial packet after every return. The conservative cost is about
`$0.50` and below the `$1` authorization. No task is retried automatically.
PASS requires exact atlas coverage, all structural count identities, agreement
between the long-double screen and rigorous intervals, zero unresolved
intervals, and one retained state per high-side interval. INCOMPLETE or FAIL
preserves the packet as evidence and authorizes no retry. A separate,
independently structured exact audit is required before theorem promotion.

Modal app `ap-blU0kVG1XoQdz0XWxgLKwz` completed all 1,240 primary shards and
all 19,840 affine orbits in 42,561.764 one-CPU worker seconds. It covered
5,857,561,600 unique heavy-position triples, 187,441,971,200 singleton-sign
distance tests, and 679,384,891,200 exact heavy-sign tests. Of 239,131,808
product-live vectors, rigorous intervals place 239,131,588 below the complete
`32p` interval and 220 above; none is unresolved, and all 220 high-side states
are retained. The screen and rigorous intervals agree on every live vector.

The complete audit traverses positions and singleton signs in reverse order,
constructs its chord columns separately, and directly rebuilds every
low-energy autocorrelation. Its 13-row benchmark agrees exactly with both the
primary engine and an independent reverse hash-block pilot at every parity
weight. Run batches of at most 12 orbits with the same one-CPU, 256 MiB,
60-second, 100-container, atomic-checkpoint, and no-retry constraints. Its
projected cost is about `$0.58`, below the `$1` authorization. PASS requires
exact equality with every proof-relevant primary total and complete energy
ledgers; only then may the cofactor-32 theorem node be promoted.

Modal app `ap-JcLLKV4WPUIDrn8rhERbNh` completed all 1,654 audit shards and
all 19,840 affine orbits in 44,023.162 one-CPU worker seconds. It independently
reproduces all primary totals, including 84,923,111,400 radius triples,
339,892,636 directly rebuilt low-energy autocorrelations, and the exact
239,131,588/220/0 interval split. The source-pinned node verifier replayed the
complete packet and all 220 high-side lower intervals on Modal app
`ap-RltPJOCiFf2VhH1gYQMtdw`. This promotes
`e1_prize_n256_s18_profile_36_m32_exclusion` to `PROVED`.

#### CR-E1-PROFILE-36-M64: exact two-atlas cofactor exclusion

**Status:** COMPLETE PASS. All authoritative packets are source-pinned; no
rerun is authorized unless a pinned source changes.

At `N=256`, profile `(3,6,S=18)`, and cofactor `m=64`, an exact product ledger
contracts `E=2,...,65` to 255 `(E,q,L)` chambers through `E=46`. A primitive
atlas normalizes an odd-separated singleton pair in `Z/128`; a separate
all-one-parity atlas divides to exact multiplicity three in `Z/64` and then
lifts. This two-atlas split was required after audit caught that the initial
primitive-only normalization was incomplete.

The final direct-triple and reverse hash-block engines cover 12736 affine
orbits, 407552 singleton-sign assignments, 10179448632 unique radius triples,
and 81435589056 exact heavy-sign tests. Arb-audited fixed-root intervals place
7191424 product-live vectors below the complete `64p` interval and 142 above;
none is unresolved. All 142 high-side states are retained.

Authoritative Modal apps:

```text
product ledger:             ap-vGLCNU73MLJj9RDeI3qeG2
primitive atlas:            ap-jsMfCK4V0ZOgCMYLHX8R7R
fixed-root generation/audit: ap-LWtv7vAuj73JwMclHhmQee
primitive primary:          ap-Ku7oS4IA5YTB6bMTAD68xf
primitive audit:            ap-8NxLniYGvXr1XY60JB2Rbb
primitive high witnesses:   ap-dMbnhlT62Afo9s0CXj7S3I
all-one-parity atlas:       ap-AZqE2K0OIwaJ72JJ8NC3JR
all-one-parity primary:     ap-8bHvHbIdNO7uEIZAXHJFzz
all-one-parity audit:       ap-GXPXxEWBsDAcVHfNG5iY7a
all-one-parity witnesses:   ap-gXAQR7y8tv1kbCbNclOHe0
```

Every worker had a hard timeout at or below 300 seconds. The campaign used at
most 96 containers concurrently, remained within the sub-dollar authorization,
and performed no scientific computation on the WSL host.

#### CR-E1-PROFILE-36-M16-TWO-DIVISIONS: exact branch exclusion

**Status:** COMPLETE PRIMARY AND AUDIT PASS. No rerun is authorized unless a
pinned source changes.

At `N=256`, profile `(3,6,S=18)`, and cofactor `m=16`, the complete support
atlas splits into primitive multiplicity four in `Z/128` (39,936 affine
orbits), once-divided multiplicity two in `Z/64` (9,080), and twice-divided
multiplicity one in `Z/32` (903). A 41-representative Modal benchmark covers
every realized `(branch,q)` class. Its measured weighted projections are
121.464, 26.819, and 2.077 one-CPU hours respectively. Only the twice-divided
branch is authorized for a complete census; the other two are deferred.

Run the 903 twice-divided orbits in batches of at most three, using at most 100
one-CPU, 256 MiB containers with 60-second hard task caps and no automatic
retry. Write an atomic partial packet after every return and retain every
high-side witness. The calibrated cost is about `$0.10`, comfortably below
the `$1` authorization. PASS requires complete atlas coverage, every structural
count identity, exact agreement between the long-double screen and rigorous
48-bit fixed-root intervals, zero unresolved intervals, and one retained state
per high-side interval. A separately structured reverse-direct audit must
reproduce every proof-relevant total before theorem promotion.

Modal app `ap-ozjw9RBwmTg6BmHBmn0HSf` completed and atomically recorded the
first three-orbit shard before the local `tiny` RAMGuard wall clock interrupted
the client. Source-matched resumable app `ap-1xutdz21Bfop112ugKr65k` preserved
that shard and completed the remaining 300. The aggregate covers all 903
affine orbits in 7,723.486 one-CPU worker seconds. It covered
266,601,720 unique heavy-position triples, 8,531,255,040 singleton-sign
distance tests, and 59,378,994,368 exact heavy-sign tests. Of 205,513,652
product-live vectors, rigorous intervals place 205,486,644 below the complete
`16p` interval and 27,008 above; none is unresolved, and all high-side states
are retained. The screen and rigorous intervals agree on every live vector.

Run the separately structured reverse-direct engine in batches of at most
three under the same 100-container, one-CPU, 256 MiB, 60-second, atomic
checkpoint, and no-retry constraints. The primary runtime projects another
roughly `$0.10`. PASS requires exact equality with every proof-relevant primary
total and complete live/above energy ledgers.

Modal app `ap-kmhgYnrF7vWYttQXorFm0w` completed all 301 reverse-direct audit
shards. It independently reconstructs all 497,496,976 low-energy vectors and
reproduces every primary total, including the exact 205,486,644/27,008/0
interval split and complete live/above energy ledgers. This promotes only the
twice-divided support subnode; the two larger m16 branches remain open.

One source-pinned node-verifier replay is authorized on Modal with one CPU,
at most 2 GiB, and a 290-second hard task cap. It must reconstruct the complete
quotient atlas, product partition, both census ledgers, and all 27,008 retained
high-side interval witnesses. Expected cost is below `$0.01`; no broad verifier
suite or scientific rerun is authorized.

Modal app `ap-IVF9ra2KWJyhXPplppzymj` passed the one source-pinned verifier in
9.817 seconds. It reconstructs all 903 quotient orbits, all 3,685 product
records, both complete census ledgers, and every retained high-side lower
interval, and catches a hostile witness-metadata mutation.

Two targeted structural replays are authorized for the global DAG validator
and critical-harness coverage checker. Each uses one short Modal task and no
scientific enumeration; combined expected cost is below `$0.01`.

Modal apps `ap-ygaLDQODvhgXc1CG3DtGR5` and
`ap-xysNDmOuY80dHYl5tXXXAS` passed the global DAG validator and critical
harness coverage checker respectively. No structural or registration gap was
introduced by the new branch theorem.

#### CR-E1-PROFILE-36-M16-LARGER-BRANCHES: deferred exact censuses

**Status:** ONCE-DIVIDED COMPLETE; PRIMITIVE PRIMARY COMPLETE; REVERSE AUDIT
PARTIAL. No relaunch is authorized while the Modal workspace is disabled.

The initial once-divided and primitive m16 branches projected to 26.819 and
121.464 one-CPU hours from complete parity-class benchmarks. The contraction,
primary, and audit history for both branches is recorded below. The primitive
reverse audit may resume only from its source-pinned atomic checkpoint after
the external Modal workspace is re-enabled.

One 15-representative optimization benchmark is authorized for the
once-divided branch. It removes the non-proof long-double diagnostic and skips
heavy triples whose three positions are even: together with the even singleton
support, those vectors are polynomials in `X^2`, so their degree-128
cyclotomic norm is a square and cannot equal `16p`. Use at most 15 one-CPU,
256 MiB, 60-second Modal tasks. Expected cost is below `$0.01`; the benchmark
does not authorize a complete census.

Modal apps `ap-uS90mwAgnXkmFsSjw4xxgc` and
`ap-Jwda0y53bpMXMNp0GjPBNp` completed the no-diagnostic/even-square and
rigorous early-cap benchmarks. Weighted projections fall from 26.819 to
19.529 and then 16.779 one-CPU hours. Modal app
`ap-bJ1BO3Mz3ciVx7Cnry7tUj` records the final projection. Every representative
retains the same fixed below/above/unresolved classification as the full
interval engine.

The once-divided primary census is now authorized. Run 2,270 batches of at
most four orbits, with four independent subprocesses in each four-CPU,
512 MiB Modal container, at most 100 containers, 60-second task caps, atomic
checkpoints, no script-level retries, and all high-side witnesses retained.
The calibrated 60,404 CPU-second projection costs about `$0.8`; four-way
container concurrency projects below five minutes wall time. PASS requires
all 9,080 affine orbits, the exact even-square omission count, all structural
identities, and zero unresolved fixed intervals. It authorizes no theorem
promotion without a separate reverse-direct audit.

Modal app `ap-6xxI9MGrLIK1n5crnIT6c3` completed that primary census. All
9,080 orbits passed in 2,270 four-way batches, with maximum task wall time
11.249 seconds. The exact totals are 2,680,779,200 raw triples,
76,819,415,040 post-square-omission sign-distance tests, 73,175,732,492
radius matches, 585,405,859,936 exact sign tests, 6,762,240,640 low-energy
vectors, and 1,816,625,504 product-live vectors. The fixed-root interval
classified 1,816,625,308 below and 196 above, retained all 196 high-side
witnesses, and left zero unresolved.

One 15-representative reverse-direct benchmark is authorized. It must use the
independent reverse enumeration, the original full fixed-root interval, and
the same exact square-norm omission. It must reproduce every primary count on
one orbit for each represented odd-chord weight before projecting the full
audit cost. This benchmark alone does not authorize the complete audit.

Modal app `ap-vysGPqGNw3Uo1bZm9osv0L` completed the reverse benchmark. All 15
odd-chord classes reproduce every corresponding primary count exactly. Modal
app `ap-mt8xdOni6TjNwFU6qkqBqE` projects 68,410.34 CPU seconds, or 19.003 CPU
hours, for all 9,080 orbits. This is approximately a sub-`$1` campaign at the
same rates as the completed primary, so one complete reverse-direct audit is
authorized: 2,270 four-orbit batches, four independent subprocesses per
four-CPU, 512 MiB container, at most 100 containers, 60-second task caps,
atomic partial output, and no script-level retries. PASS requires an exact
per-orbit match to the primary as well as the independent aggregate ledger.

Modal app `ap-HxT2OzXtS2r4jcKWzNH2a4` completed that audit. All 2,270 batches
and all 9,080 per-orbit comparisons passed. The reverse engine independently
reproduces 73,175,732,492 radius matches, 585,405,859,936 exact sign tests,
6,762,240,640 low-energy vectors, 1,816,625,504 product-live vectors, the
1,816,625,308/196 below-above split, and zero unresolved intervals. The
maximum four-worker task wall time was 13.321 seconds. This closes the
once-divided branch subject to the source-pinned node verifier; no additional
campaign under this request is authorized.

One primitive-branch optimization benchmark is authorized, with no complete
census implied. The primitive singleton support contains an odd position, so
the Galois involution `F(X) -> F(-X)` acts freely on the 32 normalized
singleton-sign patterns and permits 16 exact representatives. A second exact
optimization rounds each already-certified upper squared root factor upward
to a 16-bit dyadic mantissa and multiplies those upper bounds before invoking
the full interval. Benchmark one orbit in each of the 13 primitive odd-chord
classes, using at most 13 one-CPU, 256 MiB, 60-second Modal tasks. PASS
requires the full fixed-side ledger to be exactly half of the pre-involution
baseline in every class. Project cost before requesting further compute.

Modal apps `ap-csIUQ1ujheUPmHOCYAAirx` and
`ap-mE0wTipjjrqrejyw5lx958` completed that benchmark and projection. Every
class matches exactly. The weighted primary projection falls from 121.464 to
29.148 CPU hours (104,931.54 CPU seconds), but a complete primary plus audit
would still consume nearly all remaining credit, so neither is authorized.

One further 13-class benchmark is authorized at the same sub-`$0.01` scale.
Replace the 63-lag, eight-sign energy loop by its exact seven-coefficient
Walsh expansion, precomputing cross-vector dot products and replaying all 63
lags only for energy survivors to recover `L`. Retain the sign involution and
dyadic norm cap. PASS again requires exact half-baseline counts in every
class; project the cost before any larger request.

Modal apps `ap-o0Osge7eWPzD7RYeOZou0l` and
`ap-su7TzkrKQXDkLWG9g84C82` completed the fast-energy benchmark and weighted
projection. All 13 classes again match exactly. The full primitive primary now
projects to 25,008.33 CPU seconds, or 6.947 CPU hours, about `$0.33` at the
observed rate. One complete primary is authorized: 1,248 batches of at most
32 orbits, four independent subprocesses per four-CPU, 512 MiB container,
at most 100 containers, 60-second task caps, atomic checkpoints at bounded
intervals, no script-level retries, and all high-side representatives
retained. PASS requires all 39,936 affine orbits, exactly 16 sign-involution
representatives per heavy triple, exact Walsh/direct-energy agreement on
every low-energy survivor, structural count identities, and zero unresolved
fixed intervals. It does not authorize theorem promotion without an
independent reverse benchmark and audit decision.

Modal app `ap-tkhXMEdMpCXgm2LWUnXkEZ` completed the primitive primary. All
1,248 batches and 39,936 affine orbits passed in 22,736.06 worker seconds;
the maximum 32-orbit task wall time was 8.131 seconds. The exact
sign-involution ledger has 188,651,274,240 distance tests,
184,336,208,507 radius matches, 1,474,689,668,056 exact sign tests,
29,756,245,802 low-energy representatives, and 5,651,872,006 product-live
representatives. Certified intervals place 5,651,870,997 below and 1,009
above, retain all 1,009 high-side representatives, and leave zero unresolved.

One 13-class reverse benchmark is authorized. It must scan singleton signs
before descending heavy triples, construct its own chord columns, use an
independently inserted exact Walsh ledger, directly reconstruct every
low-energy survivor, and use the original complete fixed-root interval with
no primary dyadic cap. Use at most 13 one-CPU, 256 MiB, 60-second tasks. PASS
requires exact per-orbit agreement with the completed primary before a full
reverse cost projection is considered.

Modal apps `ap-cgOZPizDCrJE0YmFfdCkoh` and
`ap-dlfsihBSP21uvIM2RSslOr` completed the reverse benchmark and projection.
Every class agrees exactly, but the original full interval projects to
99,462.95 CPU seconds (27.629 CPU hours), above the automatic sub-`$1`
threshold; the complete audit is not authorized.

One final 13-class reverse optimization benchmark is authorized. Before the
full interval, independently compute and multiply all 64 certified integer
upper squared-root factors exactly (not with the primary's dyadic mantissas).
Strict-below products stop there; every residual still receives the original
full lower/upper interval. Use the same 13 one-CPU, 256 MiB, 60-second caps.
PASS requires exact agreement in all classes and a fresh cost projection.

Modal apps `ap-ATxdGYMJ3NJBvayKTp20Hc` and
`ap-AmrikHigBcehbCZ8jxlKb3` completed the exact-upper benchmark and
projection. Every class agrees exactly. The complete audit projects to
54,032.49 CPU seconds (15.009 CPU hours), about `$0.7`, so one full reverse
audit is authorized: 1,248 batches of at most 32 orbits, four independent
subprocesses per four-CPU, 512 MiB container, at most 100 containers,
60-second task caps, bounded atomic checkpoints, and no script-level retries.
PASS requires all 39,936 per-orbit primary comparisons, the complete
independent aggregate and energy ledgers, and zero unresolved intervals.

Modal app `ap-bvisSxyx7641bXRImfOwy8` reached batch 768 before Modal returned
`workspace ... is disabled` and terminated the campaign. The atomic packet is
valid and incomplete: 24,576 of 39,936 orbits and 768 of 1,248 batches pass
exact per-orbit comparison, with 3,477,665,782 product-live representatives,
3,477,665,087 below, 695 above, and zero unresolved. It records 35,110.54
worker seconds. Exactly 480 batches / 15,360 orbits remain. The resumable
launcher will skip the completed prefix; expected remaining compute is about
20,000--25,000 CPU seconds. Do not relaunch until the workspace is enabled and
the user confirms available credit. The primitive node remains unpromoted.

#### CR-E1-PROFILE-36-M16-GENERIC-THIRD-MOMENT: quantified no-go

**Status:** COMPLETE NEGATIVE ROUTE TEST. No rerun is authorized.

A generic layer-set third-moment/Hermite relaxation searched every integer
contact pair `1<=a<b<=144` against all live m16 product chambers. It excludes
only 7 of 436 distinct `(E,L)` pairs and leaves 949 of 967 live `(E,q,L)`
records, still through `E=89`. This generic relaxation is too weak to justify
further compute; any useful moment argument must exploit support-specific
structure rather than only the universal layer-set bound.

#### CR-E1-PROFILE-36-LOW-DYADIC-ORBIT-LEDGER: aggregate-first successor

**Status:** PROOF-ONLY PREFLIGHT COMPLETE; NO COMPUTE AUTHORIZED. The Modal
workspace is over its spend limit.

The remaining pure cofactors are `m=2,4,8`; candidate `m=16` awaits completion
of its independent reverse audit. Exact Hasse and Burnside packets give the
support interfaces

```text
m=2: 331359 primitive mu1 support orbits in Z/128
m=4: 159216 primitive mu2 orbits plus 18383 quotient mu1 orbits
m=8: 79360 primitive mu3 orbits; the affine support action is free
```

These counts do not authorize a radius census. The aggregate target should
count **full coefficient orbits with primitive-root incidence**, not support
orbits and not support-normalized vector rows. For a pure-dyadic collision
`Norm(F)=2^mu p`, `v_p(Norm)=1`, so exactly one primitive root is a simple
zero. Its signed translation slice contains exactly 256 oriented dictionary
vectors. The profile-only coarse allowance is therefore 367 full collision
orbits; orbit 368 fails.

Any future campaign must emit atomic partial packets and preserve, per full
coefficient-orbit representative:

```text
cofactor and exact 2-adic valuation;
canonical singleton and heavy supports plus all signs;
full affine canonical key, not only a singleton-support key;
exact norm interval and any row-prime candidate;
number of primitive-root incidences modulo that candidate prime;
translation stabilizer check and restored oriented-vector debit;
profile weight and cumulative exact weighted debit.
```

PASS may be either zero survivors or a certified weighted ledger within the
pair budget. Before any launch, first replay the tiny Hasse/Burnside/debit
verifiers and build a product/modular contraction. A generic census over all
588318 low-cofactor support orbits and broad energy windows is out of scope;
record it only as an external contributor request if no analytic contraction
is found.

#### CR-E1-PROFILE-36-CHARACTER-ELLIPSOID: certified sparse-associate preflight

**Status:** PREFLIGHT COMPLETE; GENERIC ENUMERATION REJECTED.

The proved `e1_conductor256_character_diagonal_exponent_router` replaces an
unbounded rank-63 unit search by one finite character-diagonal exponent
region for each fixed cofactor. A certified tiny implementation has completed
steps 1--2 below. Any future implementation must begin at step 3:

```text
1. DONE: certify outward intervals for all 63 nontrivial Fourier eigenvalues;
2. DONE: derive the conservative integer coordinate and Euclidean envelopes;
3. implement a **sparse-first** circular-unit multiplication and inversion
   recurrence in
   Z[X]/(X^128+1);
4. apply the cofactor boxes 1006,503,251,125 before the anchor product;
5. retain only exact profile-(3,6,S=18) products;
6. print a branch-and-bound node count, peak-RAM estimate, and dollar ceiling.
```

A floating-point FFT may guide subdivision but cannot accept or reject a
vector. Every boundary comparison uses directed intervals, and every
retained vector is replayed by exact ring arithmetic. The completed
preflight gives `|xi_t|<=7`, `sum xi_t^2<=101`, exactly
`16616854517524950208619690062355423946568371` coarse zero-sum vectors, and
at least `38,482,585,013,041` explicit vectors inside the weighted ellipsoid.
The subsequent inverse-kernel theorem sharpens the live body to
`|xi_t|<=3`, `sum|xi_t|<=60` while retaining the Euclidean bound.
Therefore coordinate-, Euclidean-, and ellipsoid-first enumeration are all
rejected; no fleet request should merely scale them up. A new request becomes
admissible only after an algebraic sparse-product/inverse recurrence has a
conservative state count under the limits, or after a small pilot establishes
early pruning independent of floating point. PASS of
the eventual enumeration requires a complete torsion-orbit count across
`mu=1,2,3,4` and comparison with `367`; it still does not pay lower-weight
profiles. No Modal credit is allocated by this entry.

#### CR-E1-CONDUCTOR256-L1-SVP-PROBE: route-deciding height pilot

**Status:** READY BUT BLOCKED BY WORKSPACE SPEND LIMIT. This is an exploratory
floating-point MILP, not a proof certificate and not a DAG promotion input.

The common-prime associate router gives `||lambda(u)||_1<77.202` for any two
live collisions in one cofactor. The certified spectrum and inverse-kernel
contraction bound the unique zero-sum exponent vector by
`-3<=xi_t<=3` and `sum|xi_t|<=60`. The launcher

```text
experiments/prize_resolution/e1_conductor256_l1_svp_modal.py
```

minimizes the actual 64-coordinate log `L1` norm subject to those integer
and aggregate bounds. It fixes cyclic and sign symmetry by putting a positive
largest-absolute coordinate at index zero. One two-CPU, 2-GiB container is
capped at 280 seconds; HiGHS is capped at 240 seconds and prints the incumbent,
dual bound, gap, node count, and a 70-decimal recomputation before shutdown.
The projected charge is cents, not dollars.

The proved Schinzel-height collapse now pays cofactors `4,8,16` without this
probe, so its only live E1 payoff is the residual cofactor-`2` family.

The first launch attempt on 2026-07-29 started no container and incurred no
compute. Modal returned

```text
Workspace ac-WIsI8fedhlHGSBu0g8EiyG has exceeded its spend limit
```

for the sole configured profile `allengrahamhart`. Do not bypass that account
control. Relaunch only after the workspace is enabled.

Route interpretation:

- an incumbent below `77.202` refutes the proposed torsion-only height shortcut;
  replay its integer exponent exactly in `Z[X]/(X^128+1)` and apply the sparse
  profile and inverse-coefficient filters;
- an optimum above `77.202` would collapse every fixed-cofactor associate family
  to one torsion orbit, but the floating solver result alone proves nothing;
- promotion after an above-threshold result requires a rational outer
  approximation and an independently checkable exact branch/LP, SAT, or
  lattice-cover certificate.

No fleet expansion is authorized. A single completed pilot decides whether the
proof-producing certificate is worth engineering.
