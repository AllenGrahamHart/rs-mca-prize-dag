## Preregistered rank-eleven affine-reflection cyclotomic census

- **decision:** compute every official cyclotomic number
  `R_c=#{x in H:c-x in H}` up to multiplicative `H`-scaling, and decide
  whether affine-reflection exception pencils can carry the complete
  triple-owner heavy-ruling mass
- **field/domain:** `p=2130706433`, `H=mu_(2^21)`, index
  `(p-1)/|H|=1016`, primitive generator `3`
- **C++ source SHA-256:**
  `a910d1f447cf2f0895a5b050a2de79de57831c7ca22679065c2cdc53b948a00b`
- **Modal dispatcher SHA-256:**
  `c402e1ac68bb5b7b6aeaa1bde24206415a8a5b6316fe7e0cf0b6eeb0cd371e95`
- **outcome-neutral checker SHA-256:**
  `e36fd9799e046160006877b8cd478a030729142e59763efeedc874fc9d417ec1`
- **coverage:** all `1016` nonzero additive constants modulo multiplicative
  domain scaling, in `93` ordered shards of at most `11` cosets
- **two implementations:** bitset membership while traversing `H` forward;
  exponent membership `y^(2^21)=1` while traversing `H` backward
- **global exact check:** scaling invariance gives
  `sum_(j=0)^1015 R_(3^j)=N-1`; reflection parity must agree with the
  presence of the fixed point `c/2`
- **envelope:** at most `93` containers, one CPU and `768 MiB` each,
  `50`-second child and `60`-second container wall; projected aggregate cost
  below `$0.50`; no local census

`PASS` requires complete paired agreement, every checker invariant, and

```text
floor(max_c R_c/2)<=5523.
```

Since there are at most `58361` first-owned heavy pair types, this inequality
bounds all affine-reflection records by at most `58361*5523=322327803`,
strictly below the triple-owner mass `322359637`. The exact returned maximum
will give the sharper payment. A complete result is promoted only through a
separate proof node that verifies the ownership and currency transport.

`ROUTE_DEAD` is a complete checked census with a larger maximum.
`INCOMPLETE` includes any timeout, missing coset, implementation disagreement,
checksum failure, parity failure, or resource breach. Every outcome retains
all completed shard rows. No critical status moves directly from this run.

The first deployment, Modal app `ap-C9iVehkrtVunsOc2U3Uo0k`, stopped before
any census function ran because the dispatcher derived the nonexistent local
path `..._modal.cpp`. The corrected dispatcher above names the pinned C++
source explicitly. This was a launch-path failure, not a mathematical shard
failure, and produced no result rows.

Launch command:

```text
tools/ramguard modal -- timeout --signal=TERM --kill-after=15s 120s \
  ~/.venvs/modal/bin/modal run \
  experiments/prize_resolution/rate_half_mca_rank11_affine_reflection_cyclotomic_census_modal.py
```

## Complete outcome and scope repair

- **status:** `COMPLETE`
- **first complete app:** `ap-m004TekD9vwl8btNU1jtr2`
- **capture replay app:** `ap-f4Sx3SasZ3EBY9ZBSS4WCC`
- **result SHA-256:**
  `a559b38b99fa6c2a59b4c15b9491f75752cdbd0ba2b4e1901dd311e91066238f`
- **paired rows:** `1016/1016`; implementation disagreements: `0`
- **exact first moment:** `sum_j R_(3^j)=2097151=N-1`
- **exact maximum:** `2308`, uniquely at coset index `74`, represented by
  `c=1177199610`
- **exact maximum nonfixed fibers:** `1154`
- **checker:** PASS; hostile mutations rejected `9/9`

The preregistered numerical predicate passes: `1154<=5523`. The proposed
aggregate conclusion does not follow from the census alone, however. The
current exception-SPI normal form may return different pencils for different
twenty-record packets from one pair type. Multiplying the fixed-pencil cap by
`58361` is authorized only after a separate packet-pencil synchronization,
bounded-multiplicity assignment, or chronology theorem. The promoted PROVED
node therefore states the exact fixed-pencil cap and leaves aggregate
transport explicit.

Subsequent PROVED anchor-exchange nodes supply that transport per first-owned
pair type. Every type with at least 29 records synchronizes or emits high
complexity; smaller types cost at most 28. The owner-safe uniform charge is
therefore

```text
58361*1154=67348594,
```

leaving `255011043` records on other synchronized pencil classes and forcing
one such type with at least `4370` records. This is a route cut, not a payment
of the residual or of high complexity.
