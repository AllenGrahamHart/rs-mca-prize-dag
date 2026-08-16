## K'=83 support-5/6 carrier-frontier diagnostic (INCOMPLETE)

- **target:** repair the claimed first wall at
  `rate_half_mca_rank11_k83_pairwise_atlas_triple_carrier_wall`
- **source start:** `714cd8458`; uncommitted experimental router and analytic
  theorem nodes were used after that pin
- **script:**
  `experiments/prize_resolution/rate_half_mca_rank11_k83_stratified56_lane_probe.py`
- **envelope:** one CPU and 1 GB per lane; measured peak RSS `60--61 MB`
- **status effect:** diagnostic only; no DAG promotion from this campaign

The first complete plain-frontier replay found two cells above the exact
premium ceiling `41364814251146263394918185689469529403097578120`:

```text
ordinary:       48823218479219528366674899867061323445817347365
  s2=44/s3=37/U23/s4=37/s5=37/c6F/c7F/c8F/c9F
carrier32:      47607497915597011275062723646851407786954935075
  s2=44/s3=43/s4=37/s5=37/c6F/c7F/c8F/c9F
```

The old offset-lane reruns completed lanes one through five. Lane one was
safe at `39633799344485339625076021189757227349617183809`. Lanes two
through five were unsafe only on cells deliberately left `plain` by the
K'=72-era implementation. Their maxima were respectively

```text
48783905667574087508920103887361714400981382257
48348402162021094645514147182990352368730621550
47912801724652164241916586247137000096365503413
47477104341394433057921308982733002380752506610.
```

The offset-six app timed out after 590 seconds and emitted no useful partial
certificate. The six old-lane apps in that launch wave were
`ap-QpukROdm56bYlGNaN50zKk`, `ap-oE2Y2Yks4BKveY5jEzw2fn`,
`ap-mHzkJ85vvxFSuNRik3YcHe`, `ap-j8ZR9KC0lmNegQziNNCEu6`,
`ap-byMLjB7ltmGiZYr6A8OAdT`, and `ap-FTO4glZYB671vfDc4JBmH2`.

The proof audit showed that these plain cells are covered by the already
proved full-completion pairwise-carrier atlas; the executable router had
only instantiated the subcases needed through K'=82. Corrected exploratory
apps `ap-2Y2o1UE58RDlmWcVzdCvnV`, `ap-0Ai6Bt9c5t4C8HCs7KwXbw`,
`ap-eLJZBZf17FWTVGjbDHtGrM`, `ap-X4Ln2LrAh3sev1ArEGT117`,
`ap-MIig66IDp5uszg7YiJsPA2`, `ap-ajWzfmdFDI28d1wsBvzsaq`, and
`ap-wIUyDQhqglQ3ZCHTA2u2eB` were all manually aborted when aggregate wall
time crossed the protocol limit. They emitted no retained result.

This campaign violated the intended preregistration order and did not have
resumable checkpoints. Do not cite it as a computational proof or rerun the
broad Cartesian product. A future replay must first Pareto-compress the
geometry signatures, emit deterministic per-lane checkpoints, and stop with
explicit `PASS`, `FAIL`, or `INCOMPLETE` output inside a five-minute aggregate
and `$1` campaign envelope. The analytic outputs that survive independently
are the adjacent-flat circuit coupling and its fixed-union support-5/6
corollary; both have proof-based node-local audits.

## Preregistered K'=83 threshold-pruned complete frontier replay

- **mathematical decision:** determine whether the proved pairwise-carrier
  atlas plus the proved fixed-union support-5/6 coupling closes the complete
  K'=83 rank-nine component frontier
- **lanes:** `ordinary`, `carrier32`, and exact offsets `1..6`; together these
  partition every support-2/3 position emitted by the proved finite router
- **primary:**
  `rate_half_mca_rank11_k83_threshold_frontier_replay.py`, SHA-256
  `e9cfef842bada08b53f1fb63d764f674b0f7a9374b5d8aff9f6c80ffad7847dd`
- **independent implementation:**
  `rate_half_mca_rank11_k83_threshold_frontier_audit.py`, SHA-256
  `2a196bcdca9c6155398df3bf7d0326b4461e394b8dd1a2294ab3c7cf3b0aff49`
- **formula source:** K'=83 stratified router SHA-256
  `069999aee001ee12cc0bfcaf2f8032594b4bef608163584ca06c452ae58e25d4`
- **dependency archive:** `/tmp/k72-deps.tar.gz`, SHA-256
  `5ee5d10a20f1e47b1e5400d10177e33bafdc83c0e9b516d6d12dfe0fad93aaf8`
- **code archive:** `/tmp/k83-threshold-frontier-code.tar.gz`, SHA-256
  `bcf3bfa31f91bdad88614f873e20ed27b4148dcc3f8597bf6b2e2c886db949f0`
- **runner:** `tools/modal_run_script_checkpointed.py`, SHA-256
  `8b387d5efaf7d4bfd434e98ac922324899bf8aa7d611ef4599757289eee07edf`

The threshold proof is exact: if the uncharged premium of one geometry unit
is already at most the ceiling, every fixed-union and joint charge can only
lower it, so the complete alternative product need not be expanded. Every
raw-unsafe unit is expanded through all exhaustive `T/A/F` alternatives.
Each lane flushes a complete checkpoint with source-unit, raw-row,
raw-safe-unit, expanded-unit, and geometry-row counts before the next lane.
The checkpointed runner returns these records even after a hard timeout.

Pilot: the nine diagnosed maximizers replay locally under RAMguard in 3.5
seconds at the previously measured 61 MB dependency footprint. Campaign
ceiling: two parallel one-CPU-equivalent/1 GB containers, 285-second child
hard stop, under five minutes observed wall and under `$1` conservative cost.

```text
PASS: primary and audit both cover 8/8 lanes, agree on the exact maximum,
      and place it at or below the ceiling; mint a K'=83 payment node.
FAIL: preserve the exact leading branch as the next analytic wall.
INCOMPLETE: retain complete lane checkpoints as evidence only; no promotion.
```

**Outcome:** `INCOMPLETE`. Primary app `ap-MoCjCkKzQdsFoaDpSgySte`
and independent app `ap-y3fYR39AKHhomN0R79gHTf` both reached the 285-second
child wall at 60 MB while processing the first combined ordinary lane. Each
returned only its `START` record, so no coverage or status claim is retained.
The failure is computational granularity, not mathematical evidence.

## Preregistered K'=83 offset-7 sharding pilot

The finite router decomposes the failed ordinary lane into a true plain
residue and offsets `7..36`. The revised primary SHA-256 is
`692218a499f84739a1e6ce671cadf184da279b53085431d7485989dffa82170d`;
the revised independent SHA-256 is
`e10ac6915fdf611d0703cbf6d1c57c71e7e9e1b14177cd1bb62b5a856c274a23`;
and the code archive `/tmp/k83-threshold-frontier-sharded-code.tar.gz` has
SHA-256 `6bfaf2ac8292645e39f50d4f0b2dbfb20266d477667aee423f87c084b3f1dc56`.
All other pinned sources and the checkpointed runner are unchanged.

Pilot exactly one lane, `offset7`, in primary and independent containers.
This lane has 32 support-2/3 source rows and 5,476 exact support-4/5 rows.
Both implementations flush progress every 1,000 source units and a complete
coverage record on success. Hard wall remains 285 seconds per child; campaign
wall is five minutes and conservative cost is below `$0.05`.

```text
PASS: exact maxima and coverage counts agree; use measured expansion and wall
      time to authorize or reject the 38-lane parallel campaign.
FAIL: retain the exact offset-7 wall.
INCOMPLETE: use progress counts to redesign the per-unit geometry optimizer;
            do not launch the 38-lane campaign.
```

**Pilot outcome:** `PASS`. Primary app `ap-jmgm9FhgNcjwq96l2zR3gJ`
and independent app `ap-l9ISWe18boAySpaly1diZi` agree on:

```text
source units:       175232
raw rows:           1226624
raw-safe units:     167536
expanded units:       7696
maximum: 41364700171905693710376221140276840019247232410
margin:     114079240569684541964549192689383850345710
active:  s2=47/s3=40/s4=32/s5=47/c6F/c7F/c8F/c9F/raw-safe
```

Primary deduplication evaluated 3,898,321 geometry rows; the independent
all-label implementation evaluated 3,945,508. Both returned the same exact
maximum. Peak RSS was 60 MB and observed wall was well below two minutes.

## Authorized K'=83 38-lane parallel completion wave

Launch primary and independent containers for each disjoint lane

```text
ordinary, carrier32, offset1, ..., offset36.
```

The 76-container peak is below the account limit of 100. Every child has the
same 285-second hard wall and periodic checkpoints as the pilot. Using the
offset-7 measured work as a conservative per-lane upper for the smaller
offsets and the published Modal CPU/memory unit scale, projected total cost
is below `$1`; observed campaign wall remains below five minutes because the
lanes run in parallel. Source hashes, archive hashes, theorem versions, and
PASS/FAIL/INCOMPLETE effects are exactly those of the offset-7 pilot.

To protect WSL RAM, the wave uses one local Modal client and remote
`starmap`, not 76 resident local clients. The batch runner is
`tools/modal_run_script_checkpointed_batch.py`, SHA-256
`9ca25d723d6ec0d616e334cc3fbd7354a0ef0752b1986f331e655dea5db59043`.
It allocates one CPU and 1 GB per remote child, returns each child's flushed
stdout independently, and emits a final expected/completed/failures ledger.

The wave is proof-usable only if all 38 primary lanes and all 38 independent
lanes complete, lane maxima agree pairwise, and the global maximum is at most
the exact ceiling. Any missing or disagreeing lane makes the wave
`INCOMPLETE`; no partial prefix promotes K'=83.

**Wave outcome:** `INCOMPLETE`, with exact route information. Batch app
`ap-FCVIzeLq0GH1yjqXU9SPha` completed all 76 jobs at 58--60 MB. Exactly two
jobs returned mathematical `FAIL`, namely primary and audit `ordinary`; no
job timed out. The other 37 lane pairs returned `PASS`. Raw batch SHA-256 is
`87bbe929745cd26acfe445bade74517325d79befe99b97da10ac08cdbbf84922`.

Both implementations agree on the ordinary wall:

```text
defects:  (73,37,37,37)
maxima:   (0,36,36,36)
high:     c6d3/c7d2/c8d1/c9d0
premium:  46067025990627744112258469425635158852400659940
deficit:   4702211739481480717340283736165629449303081820
```

The cell has an unconditional support-three completion carrier of size 38
and eight-dimensional annihilator. A focused exact replay applies that
`(38,8)` fixed-union charge plus the proved support-4/5 and support-5/6
couplings and obtains premium
`34180322136602231166354248419499424949751610015`, safely below the ceiling
by `7184492114544032228563937269970104453345968105`.

The same audit found a second completeness issue: pre-charge Pareto
compression of support-2/3 vectors cannot preserve offset-dependent carrier
provenance. Therefore the former lanes through offset 36 are evidence only.
The corrected exact partition is one ordinary lane plus offsets `1..72`,
with every exact defect pair retained before geometry.

## Preregistered exact-router repair pilot

- **primary SHA-256:**
  `bd55cb64beff7a2acc119030fed42968c8b251247131213cdc15d446aa5b7f55`
- **independent SHA-256:**
  `7022c625a3039b2aae96306e69ea1c1c09416a5498081978667ce5ea12c0868f`
- **code archive:** `/tmp/k83-threshold-frontier-exact-code.tar.gz`, SHA-256
  `f7af236d6886d1ad7681bd39e72306b3c25a91d26e6b1d3f54c8c0937bc979ac`
- **pilot lanes:** repaired `ordinary` and exact `offset7`, primary plus audit

The repaired ordinary router retains every positive single support-two or
support-three carrier before Pareto compression, while positive
`M3-M2=offset` rows are partitioned exactly for all offsets `1..72`.
The four pilot children use one CPU, 1 GB, periodic checkpoints, and the
285-second hard wall. Conservative campaign cost is below `$0.10`.

```text
PASS: both implementations agree and both lanes are safe; authorize two
      <=66-container exact-offset waves for offsets 1..72.
FAIL: retain the exact repaired wall.
INCOMPLETE: refine the failing lane only; no broad rerun.
```

**Pilot outcome:** `FAIL`, with a narrower exact wall. Modal batch app
`ap-IyNq9TiXnzgFvRFLmwRYqB` completed all four jobs at 57--60 MB without a
timeout. Primary and audit agree that exact offset 7 is safe, but the repaired
ordinary lane has

```text
defects:  (55,55,37,37)
maxima:   (18,18,36,36)
high:     c6F/c7F/c8F/c9F
premium:  44127003119745923941522954461412336564614624900
deficit:   2762188868599660546604768771942807161517046780
```

The broad exact-offset waves remain unauthorized until this cell is paid.

## Preregistered K'=83 adjacent-high fixed-union probe

The ordinary wall already has exhaustive support-2/3 alternatives
`T23=(u,g)=(39,7)` and `A23=(38,8)`. The generic adjacent-flat circuit
coupling applies not only to supports 5/6 but to every adjacent support pair
`d/(d+1)` with `g>=d+1`. The targeted script evaluates the exact wall under
all disjoint matchings of the available pairs `4/5,5/6,6/7,7/8`; overlapping
pairs are never charged simultaneously.

- **script:**
  `experiments/prize_resolution/rate_half_mca_rank11_k83_adjacent_high_support_probe.py`
- **scope:** one container, one CPU, 1 GB, 285-second child wall
- **expected cost:** below `$0.01`

```text
SAFE: both exhaustive T23/A23 alternatives are below the ceiling; generalize
      the adjacent-support fixed-union theorem and repair the exact router.
WALL: at least one exhaustive alternative remains unpaid; preserve it as the
      next analytic wall.
INCOMPLETE: retain no mathematical conclusion.
```

**Outcome:** `SAFE`. Modal app `ap-ltflETo1CTk9D8ndmZOGnD` used 63 MB and
returned in under one minute. The script SHA-256 is
`999c5a815285d4e989b4a176ec332526d9e266208e4e11fd91f5a10a76c892c3`.
Both routes select the support-disjoint pairs 4/5 and 6/7:

```text
T23 (39,7): premium 28580257237466146031071834658493035776688499195
             margin 12784557013680117363846351030976493626409078925
A23 (38,8): premium 28138384063262743811603676163266039013680815843
             margin 13226430187883519583314509526203490389416762277
```

## Preregistered adjacent-router exact pilot

The generic theorem has now been minted as
`rate_half_mca_sparse_circuit_fixed_union_adjacent_support_coupling`. The
primary and independent routers retain fixed-union provenance through
Pareto compression and optimize only over support-disjoint adjacent pairs.

- **primary SHA-256:**
  `1c19b328e667feb49b44c6e70744a37237c3a0dae8f09e55595108f31e9bf9b7`
- **independent SHA-256:**
  `77dabfcfa552f7a1c5939f110b5142742bacd5df3c71947b1d8090030b24a7bf`
- **archive:** `/tmp/k83-threshold-frontier-adjacent-code.tar.gz`, SHA-256
  `327c677b870233b5b43609203a45c12ca478a719da3b9391c61860d9ddbe6b49`
- **lanes:** exact `ordinary` and `offset7`, primary plus audit
- **envelope:** four one-CPU, 1 GB containers; 285-second child wall; below
  `$0.10` conservative cost

```text
PASS: both implementations agree on complete safe lanes; authorize the two
      exact offset waves.
FAIL: preserve the exact maximizing branch as the next analytic wall.
INCOMPLETE: reduce computational granularity without making a coverage claim.
```

**Outcome:** `PASS`. Batch app `ap-Qr5dCpKMRHiLusDi0QczQU` completed all
four jobs at 63 MB without timeout. The raw output SHA-256 is
`73d8348274b25911e7d0b13a404b2adb57ff24d022043be1b7d6ebed7548cb25`.
Primary and audit agree exactly:

```text
ordinary:  maximum 41363991498791696492883838631369698521229319916
           margin      822752354566902034347058099830881868258204
offset 7:  maximum 41364734718541076704831964436177797049983165655
           margin       79532605186690086221253291732353114412465
```

## Authorized adjacent-router exact offset waves

The remaining exact partition is offsets `1..72`. Run primary and audit for
offsets `1..36` in wave A and `37..72` in wave B. Each wave has 72 containers,
below the account limit of 100. Source, archive, dependency, runner, memory,
and timeout hashes are exactly those of the passing adjacent-router pilot.
The duplicated offset-7 pilot is intentionally rerun inside wave A so each
wave output is a self-contained interval certificate.

Conservative cost remains below `$1` across both waves based on the measured
pilot. A wave is proof-usable only if all 72 jobs complete, every primary and
audit lane pair agrees on coverage, maximum, and margin, and every margin is
positive. Any missing lane makes the K'=83 payment `INCOMPLETE`.

**Wave-A checkpoint:** the local Modal client was mistakenly launched under
RAMguard's five-minute `local` profile. It returned 64/72 remote checkpoints
before the local wall: all 36 primary lanes and 27 audit lanes were safe;
`audit:offset19` alone reached the 285-second child wall after 265,000 of
295,704 units, and audit offsets 20--28 were not returned. The partial output
SHA-256 is `dc2e285843645a3d5f0fa3e96dd2bab0a7b63ceffcf790db025405546dcf69f0`.
These complete per-lane checkpoints remain proof-usable after a successful
repair supplies every missing lane.

## Authorized wave-A audit repair

Rerun only audit offsets `19..28`. The mathematical source and archive are
unchanged. The batch runner now accepts one audit implementation, gives each
remote child a 645-second hard wall, and is itself launched under RAMguard's
12-hour `modal` profile. Its SHA-256 is
`bbe9f1100d8d6add611794e24e02d57ab0f57903a15195a944e6fe640ca98922`.
The ten-container repair remains below `$0.20` conservative cost. The longer
wall changes no theorem or search space; periodic checkpoints and the 1 GB
memory cap remain unchanged.

**Wave-B outcome:** `PASS`. Batch app `ap-cEUnaW2ssU1ObLbSSllkVv`
completed all 72 primary/audit jobs for offsets 37--72 without failure or
timeout. The raw output SHA-256 is
`e7714f76c755f4908c56bd55c551e2e0c6e39d025b00dad997fa81e9e36bb3e6`.
Its maximum occurs at offset 37:

```text
premium: 41347932347360629348777920971056540502170790055
margin:     16881903785634046140264718412988900926788065
```

**Wave-A repair outcome:** `PASS`. Batch app
`ap-DTDRrKPV8NvHxqZC4Q9ULg` completed all ten audit offsets 19--28 under
the extended wall with no failure or timeout. The raw output SHA-256 is
`b4adf54a2d0f776a40cd8698f1950be1875b9f709a581cabd85ab17b5e50930b`.

**Exact merger outcome:** `PASS`. The compact checker consumed the pilot,
partial wave A, wave-A repair, and wave B. It found all 146 required jobs
covering exactly `ordinary + offsets 1..72`; all primary/audit coverage keys
and maxima agree and all margins are positive. Its final certificate is

```text
lanes:                 73
jobs:                 146
global lane:          offset2
global maximum:       41364793335621487128860475977676014245181683050
minimum margin:           20915524776266057709711793515157915895070
primary geometry rows: 203167790
audit geometry rows:   393886640
```

The checker SHA-256 is
`c694c40dff948cff07d3fe8a0775047ae09ae2517063a2b654dc2a1cd713ad44`.
This authorizes a `PROVED` K'=83 payment node; no later row is claimed.
