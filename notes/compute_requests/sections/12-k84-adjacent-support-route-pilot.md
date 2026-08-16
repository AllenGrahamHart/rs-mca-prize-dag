## Preregistered K'=84 adjacent-support route pilot

- **decision:** determine whether the first new row already breaks the
  proved K'=83 adjacent-support router, and identify the exact first
  obstruction if it does
- **scope:** `ordinary`, exact offsets `1`, `2`, `7`, and the new terminal
  offset `73`, in both primary and independent implementations
- **primary wrapper SHA-256:**
  `a3f55cf0627f63b9786d3f44f526bb44c62d223152424099f1039df04d272a20`
- **audit wrapper SHA-256:**
  `a9a323316bcbef966ad97ca3e24f66220aa41baf8d5115e7ca3f3205e3e37249`
- **hash-pinned K'=83 code archive SHA-256:**
  `327c677b870233b5b43609203a45c12ca478a719da3b9391c61860d9ddbe6b49`
- **dependency archive SHA-256:**
  `5ee5d10a20f1e47b1e5400d10177e33bafdc83c0e9b516d6d12dfe0fad93aaf8`
- **batch runner SHA-256:**
  `bbe9f1100d8d6add611794e24e02d57ab0f57903a15195a944e6fe640ca98922`
- **envelope:** ten remote containers, one CPU and 1 GB each, 645-second
  child wall; projected cost below `$0.20`
- **local safety:** one RAM-guarded Modal client; no local enumeration

The wrappers change only the row parameters to `K'=84`, `q=74`,
`m'=67556`, and `n'=1048660`. The theorem and router sources imported by
the wrappers are the unchanged hash-pinned K'=83 implementations. The five
lanes are route-locating, not an exhaustive row certificate.

```text
PASS:       both implementations agree and all five lanes are safe;
            analyze the active templates symbolically before authorizing
            any remaining-lane wave
FAIL:       both implementations agree on an unsafe lane; retain its exact
            branch as the next analytic wall and do not launch broadly
INCOMPLETE: any timeout, missing lane, or implementation disagreement;
            retain no mathematical conclusion
```

No outcome of this pilot promotes `K'=84` or changes a DAG status.

**Outcome:** `PASS` as a route-locating pilot, with no row promotion.
Modal app `ap-Srv9CDnQL721xYGzAUZoR6` completed all ten jobs without a
timeout at 58--62 MB peak RSS. The raw capture SHA-256 is
`4024f6ad84c050540bfa3c32088e4768a3ca5abf798f95bc8624d054178f9ff4`.
Primary and audit agree exactly on every maximum:

```text
ordinary:  41388798786059119503097492734939028640066114130
           margin 44581160171407926086602515730765812413619
offset 1:  41388509655129434578015936172698056050247199551
           margin 333712089856333007643164756703355631328198
offset 2:  41387937303860893532474667943101838831996305858
           margin 906063358397378548911394352920573882221891
offset 7:  41388695386454290912259500164616925968496091874
           margin 147980764999998764079172837833437382435875
offset 73:   207313827489437078117773167012308731551794440
           margin 41181529539729853832905806170442450674326733309
```

The new leading branch is

```text
s2=74/s3=55/s4=45/s5=37/ordinary-single/
c6d3/c7d2/c8d1/c9d0/raw-safe.
```

Thus the adjacent-support router has not failed at the first new row, but
the maximizer changed from K'=83's offset-two/full-fallback template to an
ordinary single-support-three template. Analyze this branch and the
unsampled-offset domination problem symbolically before any full K'=84
wave.

## Preregistered one-sided raw-template scan

- **decision:** determine whether the new ordinary one-sided support-2/3
  envelope has a short stable family of active defect templates, and
  whether its exact ceiling margin crosses near the K'=84 frontier
- **interval:** every integer `K'=83..128`
- **script SHA-256:**
  `7946d6aa8174768494322aaae67b2472f351dd42fc2d9e82d07c698a23de84f1`
- **scope:** exact raw maximum over both one-sided branches, all
  support-4/5 Pareto vectors, and all support-6/9 Pareto vectors
- **envelope:** one remote CPU, 1 GB, 645-second wall; projected cost below
  `$0.02`

```text
CROSS:      report the first negative margin as the next raw analytic wall
STABLE:     extract the finitely many active affine defect templates and
            prove their binomial/floor margins on maximal intervals
PROLIFERATE: stop the scan route if active templates do not compress;
             do not replace proof by longer row enumeration
INCOMPLETE: retain no conclusion after timeout or malformed output
```

This scan ignores geometry-required cells and cannot close any row.

**Outcome:** `INCOMPLETE`, and the scan exposed a wrong endpoint rather
than a ceiling crossing. Modal app `ap-Rzy1Aw2D71418NHszc7XLf` reached its
645-second child wall at 61 MB peak RSS after printing complete rows
`K'=83..105`; the raw capture SHA-256 is
`20add11719a44044c14fe93d44a31ee3cc6068b6fac1e351b9a9fe9cf2a09787`.
All 23 completed rows have the same parity family

```text
source=3,
M3=floor(q/2),
s2=q,
s3=s4=s5=ceil(q/2),
c6d2/c7d1/c8d1/c9d0.
```

Its *raw* premium already exceeds the ceiling at `K'=83`; for example at
`K'=84` it is
`46986000759234275253755854037693521002636288520`, with margin
`-5597157392014984342732274700238761596757760771`. This is not a
counterexample to the adjacent-support route. The family lies in the
geometry-required support-three cell, where the theorem mandates the
single-completion carrier `(u,g)=(M3+2,8)`. The scan omitted exactly that
charge. Consequently no first-crossing or interval-stability conclusion is
retained, and extending this raw scan would test the wrong quantity.

The useful route information is the compressed parity family itself. The
next preregistered object must be its **post-charge** adjacent-support
premium, compared with the raw-safe ordinary leader and the other charged
families. A row or interval can be promoted only after that charged envelope
is bounded analytically and independently replayed.

## Preregistered support-three post-charge parity evaluation

- **decision:** identify the active adjacent-pair charge and exact margin of
  the isolated parity family after its mandatory single-completion carrier
- **interval:** every integer `K'=83..128`; this is 46 evaluations of one
  explicit template, not a frontier enumeration
- **script SHA-256:**
  `74f621ef2c8609c0a296d999a5a161fbad0811c3bfa5fcb3f11d3f5ec9e9c9e2`
- **template:** `q=K'-10`, `M3=floor(q/2)`,
  `s2=q`, `s3=s4=s5=ceil(q/2)`, high branch
  `c6d2/c7d1/c8d1/c9d0`, carrier `(M3+2,8)`
- **envelope:** one remote CPU, 1 GB, 120-second child wall; projected cost
  below `$0.01`

```text
STABLE:     one adjacent-charge choice per parity; extract and prove the
            corresponding exact floor/binomial inequalities
SWITCH:     finitely many charge changes; split the symbolic interval there
UNSAFE:     a negative post-charge margin is a genuine route obstruction
INCOMPLETE: retain no mathematical conclusion
```

This evaluation can reject or simplify the proposed symbolic route. It
cannot establish domination over the remaining K'=84 lane families and
cannot promote a row by itself.

Two setup-only launches preceded the hash above. App
`ap-QTHBoe6Q240zH2Vm65f0TS` used a stale dependency archive and failed
before its first row because that archive predates the all-adjacent router.
App `ap-tlQ731qAm1fuxQFA3G8VZ6` used the correct archive but timed out after
270 seconds because the script enumerated complete support-4/5 and
support-6/9 Pareto frontiers merely to retrieve named vectors; the generic
runner buffered stdout, so it returned no partial rows. Neither launch
produced mathematical evidence. The hash-pinned revision constructs those
same named vectors directly from `exact_cross_caps` and `source_options`.

**Outcome:** `SWITCH`, with a stable pricing choice and a genuine later
route obstruction. App `ap-rhsmO9Z7XoNV3I6u1ihRay` completed all 46 rows at
59 MB peak RSS. The raw capture SHA-256 is
`61a0884cc7d996512e6576c303b3746213db0c66122dce5cf29c28c94f665214`.
Every row selects the disjoint adjacent-pair charge `A45+A67`.

At the target row `K'=84`, the post-charge premium is
`30754765486431054133282031534055508984798589537`, safely below the exact
ceiling by `10634077880788236777741547803399250421079938212`. Thus the raw
support-three parity wall isolated above is not the K'=84 obstruction. The
same formula remains safe through `K'=110`, then first fails at `K'=111`
for odd `q` and `K'=112` for even `q`:

```text
K'=109: margin  509212654944121696349789160479105006945656208
K'=110: margin  296412497742911062432803390572960247010652784
K'=111: margin -289287180359720419070152831788781417392816816
K'=112: margin -502245759142497481996161240413431098141610146
```

The crossing limits this particular carrier formula; it does not falsify
the row theorem or affect K'=84. For K'=84 the full pilot's raw-safe
ordinary leader remains much larger than this charged family. The immediate
analytic task is therefore to prove the `A45+A67` reduction for the parity
cell and then establish domination over all other K'=84 ordinary and offset
families, without extending this formula past its observed crossing.

## Authorized K'=84 primary route-location wave

- **decision:** find the exact maximum and any unsafe lane among the complete
  partition `ordinary, offset1, ..., offset73`
- **primary wrapper SHA-256:**
  `a3f55cf0627f63b9786d3f44f526bb44c62d223152424099f1039df04d272a20`
- **hash-pinned K'=83 code archive SHA-256:**
  `327c677b870233b5b43609203a45c12ca478a719da3b9391c61860d9ddbe6b49`
- **dependency archive SHA-256:**
  `5ee5d10a20f1e47b1e5400d10177e33bafdc83c0e9b516d6d12dfe0fad93aaf8`
- **batch runner SHA-256:**
  `bbe9f1100d8d6add611794e24e02d57ab0f57903a15195a944e6fe640ca98922`
- **envelope:** 74 remote containers, one CPU and 1 GB each, 645-second
  child wall; projected aggregate cost below `$1`

The parity evaluation has discharged the raw-wall ambiguity that blocked a
broad launch: its mandatory carrier is safe by more than `10^43` at K'=84.
This wave remains route-locating because it uses only the primary
implementation. It does not promote K'=84 even if every lane passes.

```text
PASS:       all 74 lanes complete and are safe; retain the exact maximum and
            authorize an independent replay of the active/near-active lanes
FAIL:       retain each exact unsafe lane as an analytic obstruction
INCOMPLETE: any timeout or missing lane; retain partial route information
```

**Outcome:** `PASS` as a complete primary route-location wave. App
`ap-1oAXY3d5xqakObFjYF0Ck6` completed all 74 lanes at 58--62 MB peak RSS;
the raw capture SHA-256 is
`884e7bc9ee9c78b49e1324bb3c11ca0ca3d6044114f2bc88dd4cee196b2c916a`.
The wave evaluated 15,651,063 source units, 109,557,441 raw rows, and
268,721,026 geometry rows. The exact global primary maximum is

```text
ordinary:
s2=74/s3=55/s4=45/s5=37/ordinary-single/
c6d3/c7d2/c8d1/c9d0/raw-safe
premium 41388798786059119503097492734939028640066114130
margin     44581160171407926086602515730765812413619
```

The two nearest offset lanes are offset 15, with margin
`53789790696241039676955645542199668046166`, and offset 23, with margin
`55884925238948819300051499174416861077550`. Every lane is safe, but this
primary-only result does not promote K'=84.

## Authorized K'=84 independent completion wave

- **decision:** independently replay the same complete 74-lane partition
  and test exact agreement of coverage keys, maxima, and margins
- **audit wrapper SHA-256:**
  `a9a323316bcbef966ad97ca3e24f66220aa41baf8d5115e7ca3f3205e3e37249`
- **archives and batch runner:** unchanged from the primary wave above
- **envelope:** 74 remote containers, one CPU and 1 GB each, 645-second
  child wall; projected aggregate cost below `$1`

```text
PASS:       all audit lanes complete, are safe, and agree exactly with the
            primary coverage and frontier; mint and verify a K'=84 node
FAIL:       retain every disagreement or unsafe lane; do not promote
INCOMPLETE: retain no row-closure conclusion
```

Unlike a near-active-only audit, this full replay can satisfy the existing
K'=83 node's audit bar for the new row and is therefore closure-directed.

**Outcome:** `PASS`. App `ap-CE1YUXVUmNXrwze1lDP6Wn` completed all 74
independent lanes at 59--62 MB peak RSS; the raw capture SHA-256 is
`11420a74fbebe5f63d717e633c9914c9089c3fb92546051e267c03b60ee1a850`.
For every lane, primary and audit agree exactly on source units, raw rows,
raw-safe units, expanded units, maximum, margin, and active branch after
normalizing the terminal label `raw-safe`/`raw`. The audit evaluated
520,900,317 labelled geometry rows, at least the primary's 268,721,026.
Both implementations therefore return the same ordinary global maximum and
the same positive margin printed above.

This completes the empirical frontier replay required for K'=84. Promotion
still requires a compact merger certificate, exact positive component-gap
arithmetic, a source-hash contract, independent static verification, and
the ordinary DAG gates.

## Preregistered K'=84 compact merger

- **decision:** accept the two full captures only if all 148 jobs are
  present, successful, memory-bounded, and lane-wise identical on the
  independently implemented coverage/frontier keys
- **script SHA-256:**
  `11ef8d98a1cc07db73f4f6e6a17ebb975210a475cf08a8eaa525c4a5ea2a415a`
- **primary capture SHA-256:**
  `884e7bc9ee9c78b49e1324bb3c11ca0ca3d6044114f2bc88dd4cee196b2c916a`
- **audit capture SHA-256:**
  `11420a74fbebe5f63d717e633c9914c9089c3fb92546051e267c03b60ee1a850`
- **envelope:** one remote parser job; expected peak below 128 MB and cost
  below `$0.01`

The merger additionally asserts the exact ordinary maximizer and margin,
the offset source-unit formula `(74-offset)*5625`, the broader audit
geometry count, and normalized primary/audit branch-label equality. A
failure blocks node creation.

**Outcome:** `PASS`. App `ap-UwcGaJZm4Wst0Ozq1NMRIp` completed at 72 MB
peak RSS. The merger capture SHA-256 is
`abc5638fba58fee000c0e8552ea449c4f8058713da3b784a989bf454235633a8`.
It certified 148 jobs, 74 lanes, 15,651,063 source units, 109,557,441 raw
rows, both input hashes, the two geometry totals, and the printed global
maximum and margin.

## Preregistered K'=84 component payment

- **decision:** substitute the merger-certified premium into the exact
  rank-nine ledger and require a positive integral component gap
- **script SHA-256:**
  `391232fc91db032d2599c18e47ad5f9368cf3b9650ede0634972ad118f941207`
- **input premium:**
  `41388798786059119503097492734939028640066114130`
- **envelope:** one remote exact-integer job; expected peak below 128 MB and
  cost below `$0.01`

The script independently reconstructs the row marks, kernel capacity, safe
ceiling, full-rank capacity, required incidence, and final gap from the
hash-pinned rank-nine ledger. A nonpositive gap blocks promotion.

**Outcome:** `PASS`. App `ap-H3we0j1uIdfDebkyKPSRbR` completed at 58 MB
peak RSS; the capture SHA-256 is
`58b8a3077d2dc80444b91a9b0057f6ad47a9fd07a0bce0456904522cc4d054c5`.
The exact total capacity is
`920610888896792835227342245208088849044544034113385622333558298`
against required incidence
`920611111786972543926647666320421141253960527393538734334971880`,
leaving positive gap
`222890179708699305421112332292209416493280153112001413582`.
Together with the merger certificate and the proved analytic dependencies,
this authorizes a K'=84 `PROVED` node; no larger row is authorized.
