# Upstream-sync proposal — watches + external-evidence trail

Date: 2026-08-06. Auditor: Opus audit pilot (upstream_sync).
Access: read-only `gh`. Nothing pushed, commented, or written upstream.
Working dir: `notes/pilots_20260804/upstream_sync/` only. No shard, no
`dag.json`, no `critical/`, `background/`, `tools/` file was modified.

**Ceiling honoured.** Every upstream item below is UNMERGED contributor work.
Nothing here is proposed as a status change, an edge, or a proved-by-us claim.
The ceiling is (a) trust-labelled node-local addenda and (b) watch entries.
The single exception is §4 (SOL_TARGET_4), which is **ours**, Modal-certified,
and therefore bankable as our own dated falsification.

**Freeze check.** The ledger's frozen upstream pin is "the 2026-08-04 PR state
(#1149 head)" (`notes/pilots_20260802/CAMPAIGN_LEDGER.md:1011`). I re-listed
all upstream PRs on 2026-08-06: **#1149 is still the maximum and still last
updated 2026-08-04T16:39:12Z**. The frozen pin equals the live state; no PR
has queued behind it.

---

## 0. Summary

| # | node / file | lane | kind | trust label |
|---|---|---|---|---|
| A1 | `rate_half_band_closure` (note addendum) | K3 | watch refresh + 3 watch resolutions | EXTERNAL, UNMERGED, CONTENT-REVIEWED |
| A2 | `rate_half_kb_m2_r4_diagonal_c2_112_aligned_positive_unramified_fixed_mixed_full_quotient_exclusion` | K3 | external corroboration + mapping gap | EXTERNAL, UNMERGED, CONTENT-REVIEWED |
| B1 | `dli_wcl_ell4_weight11_quintic_divisor_descent` | L1 | false-friend guard | OURS (subtraction check) |
| B2 | `petal_reserve_rich_fiber_reduction` | L1 | false-friend guard (**new catch**) | OURS (subtraction check) |
| B3 | `l1_program_frontier` | L1 | citation discipline + open domination check | EXTERNAL, UNMERGED, PARTLY UNREPLAYED |
| C1 | `rate_half_list_chamber_affine_rank_bridge` | LIST/M31 | our fence dominates | EXTERNAL, UNMERGED, ROUTE-CUTS VERIFIED / SIEVES UNREPLAYED |
| C2 | `rate_half_list_adjacent_crossing` | LIST/M31 | do-not-price fence | EXTERNAL, UNMERGED |
| C3 | `l1_m31_t64_quotient_prefix_intercept_fence` | LIST/M31 | adjacent-distinct fixture | EXTERNAL, UNMERGED |
| C4 | `l1_m31_depth32_uniform_intercept_counterexample` | LIST/M31 | adjacent-distinct fixture | EXTERNAL, UNMERGED |
| C5 | `l1_m31_fixed_support_divisor_direction_cap_route_cut` | LIST/M31 | no-contradiction / no-lift | EXTERNAL, UNMERGED |
| D1 | `SOL_TARGET_4_H4_COLLISION_CENSUS.md` (+ `SOL_TARGETS.md`) | Paper-D | dated falsification appendix | **OURS — MODAL-CERTIFIED** |
| D2 | `h4_terminal_dichotomy` | Paper-D | counting-vs-structure guard | **OURS — MODAL-CERTIFIED** |
| D3 | `f3_hge4_aggregate_budget` | Paper-D | index guard is load-bearing | **OURS — MODAL-CERTIFIED** |
| D4 | `f3_hge4_norm_gate_count` | Paper-D | index guard is load-bearing | **OURS — MODAL-CERTIFIED** |

14 addenda over 13 nodes/files. 11 are trust-labelled external; 3 (B1, B2 and
the D-block) are our own subtraction/compute facts.

**Trust-label vocabulary used below** (matches the maelcar audit's):
`VERIFIED` = we replayed it; `CONTENT-REVIEWED, NOT REPLAYED` = we read the
artifact at a pinned head but did not execute it; `UNREPLAYED` = the
mathematical load sits in compute we did not run.

---

## 1. Scott's K3 frontier — state of record at the freeze pin

### 1.1 Pins

| PR | title | head | state | last updated |
|---|---|---|---|---|
| #1132 | Close m=12, m=4, full-V4 m=2; compile order-two interfaces | `543db66fa66793690651a5f81ea90b8f8f81e66c` | OPEN (**ours**) | 2026-07-31 |
| #1139 | Compile outer frontier and cut quadratic recurrence | `8d43c6fa3a6ff04ea369ba7046fced6ae133b097` | OPEN, not draft | 2026-08-01 |
| #1140 | Compile all 36 aligned-positive 112 q-slice systems | `9e1d96cbf997c30efa448bbce9a7f48c2bea9643` | OPEN | 2026-07-31 |
| #1141 | Delete aligned-positive F02/F03 112 cells | `826c0e7610604d550b8dd9b772c197a4e660e525` | OPEN | 2026-07-31 |
| #1144 | Delete all aligned-positive moving 112 cells | `05ff2348de8f2c0f99683875ff12a9a79dcf21ec` | OPEN, not draft | 2026-08-01 |
| #1149 | Close two fixed 112 cells and cut quadratic frontier | `55ac3e07477bd7a768190a3e755f22b0d44354b0` | OPEN, **DRAFT** | 2026-08-04 |

Stack: `#1132 -> #1140 -> #1141 -> #1144 -> #1149`, with `#1139` a **separate
child of #1132**. Note the base of Scott's entire stack is **our** PR #1132.

**#1149 net review = one commit**, `55ac3e074` "K3: close two fixed cells and
cut quadratic frontier", 5 files (agents-log, note, certificate, compile
`.sage`, verify `.py`). Everything else in its 100-file listing is parent-stack
noise, exactly as its body says.

### 1.2 There are TWO distinct Scott frontiers — do not conflate them

**(i) The 36-cell aligned-positive (1,1,2) atlas** (`#1140/#1141/#1144/#1149`).
36 = 12 labels x 3 root patterns `{R02, R11, R20}`; `F00..F07` are
fixed-moving, `M00..M03` are moving-moving.

```
#1141   deletes F02, F03            (6 fixed-moving cells)
#1144   deletes M00..M03            (12 moving-moving cells)
        => 18 deleted, 18 open = {F00,F01,F04,F05,F06,F07} x {R02,R11,R20}
#1149   deletes F00-R11, F01-R11    (2 cells; named-open emptiness)
        => 16 open
```

The 16 open decompose as **4 + 12**:
- 4 retained two-dimensional q-slice schemes: `F00-R02, F00-R20, F01-R02,
  F01-R20` (the "crossed/identity" charts; `R11` is the balanced one);
- 12 cells `F04/F05/F06/F07 x R02/R11/R20`, compressed — **route cut, not
  emptiness** — to **6 exact two-cell fingerprint orbits**:
  `F04=F07` and `F05=F06` at each of `R02, R11, R20`.

The compression is the uniform quadratic lemma: for `P = Aw^2+Bw+C`,
`Q = Dw^2+Ew+F`, with `U = AF-CD`, `V = AE-BD`, `Z = BF-CE`,

```
Res_w(P,Q) = U^2 - VZ ,      D P - A Q = -(V w + U) ,      A Z - B U + C V = 0
```

so on `V != 0` the unique common root is `w = -U/V`; the `V = 0` rank-drop
branch is explicitly **retained, not divided away**.

Certificate `kb_mca_v4_m2_aligned_positive_fixed_frontier_v1.json`, payload
`4adc4187bb5794ed70fce122055fb94916974c1adacf9451237aff002ebfd63e`, terminal
`TWO_BALANCED_CELLS_EMPTY_TWELVE_QUADRATIC_ROUTES_COMPILED`, and
`"K3_closed": false, "KoalaBear_row_closed": false`. Self-declared status is
`PROVED_EXACT_LOCAL_LEMMA_REVIEW_REQUIRED_K3_OPEN`; the PR is **draft** and
says "Fresh cell-specific proof review is still required".

**Scope, verbatim from the note:** "No owner, charge, K3 value, or KoalaBear
row bound moves."

**(ii) The outer/transverse per-record frontier** (`#1139`) — a *different*
object, unchanged since 2026-08-01.

```
26 -> 22 -> 18 -> 12 -> 8 -> 3 -> 2
```
driven by `delta r = 4m` over 26 source-pencil triples `(m,r,delta)`, with the
stage ladder `m=12 closed -> m=10 routed -> m=6 routed -> m=4 closed ->
m=3 routed -> full-V4 m=2 closed`, route rank `m10:3; m6,m3:2; m2:1; closed:0`,
and deliberately **no `m=2 -> m=2` strict edge**.

### 1.3 Do the two residual terminal types still stand? — **YES**

`(m,r,delta) = (2,4,2)` and `(2,8,1)`. **Unchanged and undeleted at the freeze
pin.** Evidence: #1139's note states "The last deletion removes `(2,2,4)`. The
universal `m=2,u=2` interface explicitly records that neither `(2,4,2)` nor
`(2,8,1)` is deleted", and #1149's **net commit touches none of the outer
frontier artifacts** (its 5 files are all `m2_aligned_positive_fixed_frontier`).
No Scott PR after #1139 revisits them. Its own scope line: "No terminal type is
deleted, no actual received-line record is constructed, and no ledger value
moves."

### 1.4 The four semantic gates — verbatim

The live active-v4 four-cell first-match partition is **PROVEN** present
(`SOURCE_COORDINATE_TANGENT_IMAGE`, `ACTIVE_V4_BOUNDARY_PREFIX_Q`,
`ACTIVE_V4_BALANCED_CORE`, `UNPAID_V4_COMPLEMENT`; manifest payload
`ffd1e427f53db3d2dbfd13e69a05d173d2f2aa1f03c152aead73fcc821094acb`, row payload
`36e9d69aaf6deeb4fe123358e8bb8d5bbbdcb40c9315b4316f0c6a1189a270e1`). The
following four are **UNPROVEN** (`#1139` note §2):

1. "every transverse terminal maps to the correct active-v4 cell";
2. "a semantic complete selector emits an actual record for every selected
   69-class set";
3. "every strict route either transports all 69 classes injectively and
   cardinality-preservingly or exactly reselects 69 actual classes at the
   lower-rank record"; and
4. "every owner descent preserves the full same-record key" — the eight-field
   key `received_line_id, slope_coordinates, graph_record_id,
   evaluation_support_id, received_data_id, explaining_polynomial_id,
   source_map_class_id, active_v4_owner_index`.

The any-69 lemma (cap 68) is therefore **conditional on both terminal types
plus all four gates**; the note is explicit that "the cap is not bankable" and
labels itself **YELLOW**.

Route cut retained: at `p = 2130706433`, `N = 2^21`, `a = 1213133211`, the two
fixed-point-free involutions from `q1 = x + a/x`, `q2 = x + a^3/x` both preserve
the deployed carrier yet generate a **dihedral group of order `2^21`**, whose
common invariant `u = (x^N-1)/x^(N/2)` has `u^{-1}(0) = D` a complete reduced
degree-`N` fibre. Hence recurrent carrier-preserving quadratic folds do **not**
automatically give bounded-degree strict progress.

### 1.5 The headline sync fact — the coordination gap closed, in our favour

Our 2026-07-31 addendum recorded "the first genuine coordination failure
between the forks" (Scott's #1140 compiled the 36-cell atlas "with zero
citations of our lane"). **That has now reversed.** #1149's note §1 "Upstream
alignment" reads, verbatim:

> "PR #1143 now closes the complete positive coordinate route `433-1a -> O0b`
> and role cell 14 of `433-1b -> O0a`; its newest workboard instruction asks
> for the six aligned-positive unramified cells. The `F00/F01` six-cell block
> is attacked here literally, closing its two balanced cells and retaining the
> four crossed/identity schemes."

So Scott now reads our exported workboard and **selects his next target from
it**. The disposition loop rewarded the export exactly as the 2026-08-01
addendum predicted ("export status of `kb_m2_r4` (ours) as the fix").

**And this is where the trail is materially stale.** Our tree has closed that
block **completely**:

| our node (all `background/nodes/rate_half_kb_m2_r4_diagonal_c2_112_aligned_positive_unramified_*`) | status |
|---|---|
| `moving_same_q_slice_exclusion` | PROVED |
| `moving_swap_q_slice_exclusion` | PROVED |
| `moving_mixed_full_quotient_exclusion` | PROVED |
| `fixed_same_full_quotient_exclusion` | PROVED |
| `fixed_swap_full_quotient_exclusion` | PROVED |
| `fixed_mixed_full_quotient_exclusion` | PROVED |

`.../fixed_mixed_.../result.md:7` states: "**All six aligned-positive
unramified allocations are now closed.**" (Plus
`rate_half_kb_m2_r4_diagonal_c2_112_aligned_positive_ramified_q_slice_exclusion`
PROVED.)

Scott has 2 of his six; we have 6 of ours. **None of our six closures has ever
been exported** — the only thing upstream knows is the residual counter
`remaining_unramified=6, deep_cases=17` printed by our #1132, which is what is
still advertising the block as open.

> **FLAG S-1 (MEDIUM, mapping unestablished — raised, not guessed).** I did
> **not** verify that Scott's six `F00/F01 x {R02,R11,R20}` cells are our six
> allocations. The partitions differ on their axes: his six is *two
> fixed-moving assignments x three root patterns*; ours is *{fixed-moving,
> moving-moving} x {same, swap, mixed}* — i.e. ours contains three
> moving-moving cells, and **all** of his `M*` moving-moving cells were already
> deleted in #1144. Both sides have a "six-cell aligned-positive unramified
> block" and both call it that, but the cell-for-cell mapping row requested in
> our 2026-07-31 comment on #1140 **has still not been supplied by either
> side**. Consequences: (a) our "6/6 closed" and his "2/6 closed, 4 retained"
> are **not** in contradiction under either reading (he proved two empty and
> left four *open*, not nonempty); (b) if the blocks do coincide we are ahead
> by four cells and an export would retire his next compute cycle; (c) if they
> do not, the mapping row is still the open coordination item. **Do not assert
> identity in any addendum or comment until the mapping row exists.**
>
> **What DOES now match — four qualifiers, all four.** This is stronger than
> the 2026-07-31 position and should be recorded. Scott's #1144 body calls his
> atlas "the exact 36-cell aligned-positive **`(1,1,2)`** atlas", and #1149's
> certificate atom is `K3_M2_**DIAGONAL**_112_ALIGNED_POSITIVE_FIXED_MOVING`.
> Our nodes are `rate_half_kb_**m2**_r4_**diagonal**_**c2_112**_**aligned_positive**_*`.
> So both sides are working `m=2`, **diagonal**, `c2(1,1,2)`,
> **aligned-positive** — the same four qualifiers, and "112" means `c2(1,1,2)`
> on both sides, not two different notations. Identification is therefore
> *likely*; it is still not *established*, because the axis mismatch above is
> real and neither side has printed a cell-for-cell row.

> **FLAG S-5 (MEDIUM, a standing hold whose rationale has expired).**
> `notes/PR_SWEEP_20260803.md:41-43` records: "Diagonal-node export hold:
> Scott has NOT covered the diagonal cells; hold can be revisited at the next
> export batch." **That premise is false at #1149**: its certificate atom is
> explicitly `K3_M2_DIAGONAL_112_ALIGNED_POSITIVE_FIXED_MOVING`, i.e. he is
> now working the diagonal cells directly. The same hold is repeated at
> `notes/pilots_20260802/CAMPAIGN_LEDGER.md:479` ("Diagonal-node export still
> HELD (collision surface with Scott's #1139, no response — unchanged
> watch)"). The hold was justified by *non*-overlap; the justification is
> gone, and the overlap it was protecting against is now happening anyway
> without our material. **Coordinator decision — surfaced, not taken.**

> **FLAG S-6 (LOW, conflation guard).** `notes/PR_SWEEP_20260803.md:34-36`
> says Scott has "EXACTLY TWO residual terminal types", while
> `WAVE46_AUDIT.md:46` says "#1149 closes two more 112 cells". Both are
> correct and they are about **different frontiers** (§1.2): "two" in the
> first is the count of residual `(m,r,delta)` types on the outer/transverse
> frontier; "two" in the second is the number of atlas cells deleted. Scott's
> open **cell** count is **16**, and appears nowhere in our tree. Recording
> this explicitly so the two twos are never added or equated.

### 1.6 Watch resolutions

| watch (source) | status at freeze pin |
|---|---|
| "whether the atlas note gains the mapping, and whether F02/F03 land in our printed residual" (2026-07-31) | **PARTIALLY RESOLVED.** #1149's note §1 cites our lane by PR and by result, but supplies **no cell-for-cell mapping**. Still open. |
| "whether his agent starts deleting coordinate-orientation cells (= re-deriving waves 33-37)" (2026-08-01) | **RESOLVED — NO.** #1144 and #1149 stay in the **aligned**-positive orientation; our exported lane is **coordinate**-positive (`kb_mca_v4_m2_r4_coordinate_positive_*`). No re-derivation. Keep watching. |
| "whether #1139's facet census gains a mapping to our source-line c2 orbits" (2026-08-01) | **UNRESOLVED.** #1139 unchanged since 2026-08-01; no mapping added. |
| "export status of `kb_m2_r4` (ours) as the fix" (2026-08-01) | **RESOLVED — the fix worked.** #1143 exported 433-1a (`02d2788f7`) and 433-1b cell 14 (`b1489664e`); Scott now cites both and takes his target from our workboard. |

> **FLAG S-2 (LOW-MEDIUM, pin drift).** #1139 is stacked on **#1132 at head
> `c2edcfa5`**, but our #1132 has since advanced one commit to `543db66f`
> ("Extend saturated 112 q-slice exclusions", 10 files). #1144's body already
> concedes "Current #1132 has advanced in parallel from the common parent".
> Any repricing of the `26 -> ... -> 2` composition must be re-checked against
> `543db66f`, not `c2edcfa5`.

> **FLAG S-3 (LOW, observation for Scott — possible free symmetry).** In
> `kb_mca_v4_m2_aligned_positive_fixed_frontier_v1.json`, the six "distinct"
> orbits carry only **four** distinct resultant hashes: `F04-R02|F07-R02` and
> `F04-R20|F07-R20` share `6cd1bfd1f71d5f...` (degree 42, 3679 terms), and
> `F05-R02|F06-R02` and `F05-R20|F06-R20` share `8adb5b853956a1...`. Only the
> `U,V,Z` core hashes separate them. This is **not** an error — orbits are
> defined by the full fingerprint — but an unexploited `R02 <-> R20`
> resultant-level coincidence is worth asking about, since it could halve the
> residual work. Not verified as a symmetry by me; **ASK, do not assert.**

> **FLAG S-4 (LOW, replay).** Nothing in #1149 was replayed by us: its
> compiler is Sage/Singular and its verifier is a `--tamper-selftest` harness,
> both outside our compute law for this pilot. All #1149 statements above are
> **CONTENT-REVIEWED at pinned head `55ac3e07`, NOT REPLAYED**. Its headline
> deletions rest on a nilpotence-index-three localizer argument we have not
> checked. It is additionally a **draft** whose own author says cell-specific
> proof review is outstanding.

---

## 2. Proposed addenda — Scott / K3 lane

### A1. `rate_half_band_closure` (critical, TARGET)

**Vehicle:** append to
`critical/nodes/rate_half_band_closure/notes/k3_contributor_review_20260730.md`.
This is the established house vehicle (dated `## Addendum` sections, facts
"established against the PR heads", closing `Watch:` line) and the node is
already in `refs`. No shard edit needed.

**Justification:** the trail's last entry is 2026-08-01; two Scott PRs (#1144,
#1149) and the entire maelcar batch have landed since, and three of its four
standing watches are now decidable.

**Trust label:** EXTERNAL EVIDENCE, UNMERGED (#1149 is a DRAFT PR),
CONTENT-REVIEWED AT PINNED HEAD, NOT REPLAYED.

**Exact text:**

```markdown
## Addendum 2026-08-04 — Scott's frontier at #1149, and the export that is now overdue

External evidence, unmerged. Established read-only against PR heads
#1149 `55ac3e07477bd7a768190a3e755f22b0d44354b0` (DRAFT), #1144
`05ff2348de8f2c0f99683875ff12a9a79dcf21ec`, #1139
`8d43c6fa3a6ff04ea369ba7046fced6ae133b097`. CONTENT-REVIEWED, NOT
REPLAYED (Sage/Singular; outside our compute law). Nothing below changes
this node's status, and no upstream result is imported as a theorem.

**Two frontiers, not one.**

1. *36-cell aligned-positive (1,1,2) atlas* (#1140/#1141/#1144/#1149).
   #1141 deleted F02/F03 (6 fixed-moving), #1144 deleted M00..M03 (all 12
   moving-moving), leaving 18 = {F00,F01,F04,F05,F06,F07} x {R02,R11,R20}.
   #1149 proves named-open emptiness for F00-R11 and F01-R11 (localizer
   nilpotent of exact index three), so his frontier is now **16 open**:
   four retained two-dimensional crossed/identity schemes (F00/F01 x
   R02/R20) plus twelve F04..F07 cells compressed — a route cut, NOT an
   emptiness theorem — into six two-cell fingerprint orbits (F04=F07,
   F05=F06 at each root pattern) via
   `Res_w(Aw^2+Bw+C, Dw^2+Ew+F) = U^2 - VZ`, `U=AF-CD, V=AE-BD, Z=BF-CE`,
   generic root `w = -U/V`, with the `V=0` rank-drop branch retained.
   Certificate payload `4adc4187bb5794ed70fce122055fb94916974c1adacf9451237aff002ebfd63e`;
   `K3_closed: false`, `KoalaBear_row_closed: false`; his own scope line is
   "No owner, charge, K3 value, or KoalaBear row bound moves."

2. *Outer/transverse per-record frontier* (#1139), a different object,
   **unchanged since 2026-08-01**: `26 -> 22 -> 18 -> 12 -> 8 -> 3 -> 2`
   under `delta r = 4m`, with the only residual terminal types still
   `(m,r,delta) = (2,4,2)` and `(2,8,1)` — neither deleted (his universal
   `m=2,u=2` interface records this explicitly; the last deletion removed
   `(2,2,4)`). #1149's net commit touches no outer-frontier artifact.
   The any-69 cap-68 lemma remains conditional on resolving both types AND
   four UNPROVEN semantic gates: (i) every transverse terminal maps to the
   correct active-v4 cell; (ii) a semantic complete selector emits an
   actual record for every selected 69-class set; (iii) every strict route
   transports all 69 classes injectively and cardinality-preservingly or
   exactly reselects 69 at lower rank; (iv) every owner descent preserves
   the full eight-field same-record key. He labels it YELLOW and says the
   cap "is not bankable". The dihedral route cut stands: two fixed-point-free
   involutions preserving the deployed carrier generate a group of order
   2^21, so recurrent quadratic folds are not automatically strict progress.

**THE COORDINATION GAP HAS CLOSED — in our favour, and we have not
collected.** The 2026-07-31 addendum recorded #1140 as compiling the atlas
with "zero citations of our lane". #1149 §1 now reads: "PR #1143 now closes
the complete positive coordinate route `433-1a -> O0b` and role cell 14 of
`433-1b -> O0a`; its newest workboard instruction asks for the six
aligned-positive unramified cells. The `F00/F01` six-cell block is attacked
here literally." He is selecting his targets from our exported workboard.
The 2026-08-01 watch "export status of `kb_m2_r4` (ours) as the fix" is
therefore RESOLVED: the export worked.

But our tree closed that block completely and never shipped it. All six
`rate_half_kb_m2_r4_diagonal_c2_112_aligned_positive_unramified_*`
allocations are PROVED (moving same/swap/mixed, fixed same/swap/mixed);
`..._fixed_mixed_.../result.md` states "All six aligned-positive unramified
allocations are now closed". Upstream still sees only #1132's printed
residual `remaining_unramified=6, deep_cases=17`, which is what is
advertising the block as open. Scott has 2 of his six; we have 6 of ours.

**MAPPING STILL UNESTABLISHED — do not claim identity.** His six is
(two fixed-moving assignments F00,F01) x (three root patterns R02,R11,R20);
ours is ({fixed-moving, moving-moving}) x ({same, swap, mixed}). Ours
contains three moving-moving cells; all of his moving-moving cells (M00..M03)
were already deleted in #1144. So the two "six-cell aligned-positive
unramified blocks" are not known to be the same six objects, and the
cell-for-cell mapping row we proposed on #1140 (issuecomment-5146556389) has
still not been supplied by either side. Our 6/6 and his 2/6-plus-4-retained
are NOT in contradiction under either reading: he proved two cells empty and
left four OPEN, not nonempty.

**Pin drift.** #1139 is stacked on #1132 at head `c2edcfa5`; our #1132 has
advanced to `543db66f` ("Extend saturated 112 q-slice exclusions"). Any
repricing of the 26 -> 2 composition must be re-checked against `543db66f`.

**Watch resolutions.** RESOLVED-NO: he has not entered coordinate-orientation
deletion — #1144/#1149 stay in the *aligned*-positive orientation while our
exported lane is *coordinate*-positive; no re-derivation of waves 33-37.
RESOLVED: the kb_m2_r4 export was the fix. PARTIALLY RESOLVED: he now cites
our lane but supplied no mapping. UNRESOLVED: #1139's facet census still has
no mapping to our source-line c2 orbits.

**Watch:** whether the six-cell mapping row appears on either side; whether
#1149 leaves draft and survives its own "fresh cell-specific proof review";
whether his next cycle attacks the four F00/F01 crossed/identity survivors
(cells our tree may already have closed — see the export recommendation);
whether the resultant-hash coincidence between his R02 and R20 orbits is a
real symmetry he can exploit.
```

### A2. `rate_half_kb_m2_r4_diagonal_c2_112_aligned_positive_unramified_fixed_mixed_full_quotient_exclusion` (background, PROVED)

**Vehicle:** new node note (e.g. `external_evidence_20260804.md`) added to the
node's `refs` via its `node.json` shard. This node owns the packet-terminal
claim "All six aligned-positive unramified allocations are now closed", so it
is the correct node-local home under the standing node-local rule.

**Justification:** an outside party is independently attacking a block he
identifies with ours; that is a node-local fact about this node's claim
(potential independent corroboration, and a live mapping gap), not merely a
central-notes fact.

**Trust label:** EXTERNAL EVIDENCE, UNMERGED (PR #1149, DRAFT),
CONTENT-REVIEWED AT PINNED HEAD, NOT REPLAYED. **No status change.**

**Exact text:**

```markdown
# External evidence, 2026-08-04 — Scott Hughes's PR #1149

External evidence, unmerged. PR #1149 (DRAFT), head
`55ac3e07477bd7a768190a3e755f22b0d44354b0`. CONTENT-REVIEWED, NOT REPLAYED.
This changes no status here and imports no theorem.

#1149 attacks a six-cell block it calls "the six aligned-positive unramified
cells", citing our #1143 workboard as the source of that instruction. It
proves named-open emptiness for two of them (F00-R11, F01-R11; named
localizer nilpotent of exact index three) and retains four as
two-dimensional q-slice schemes (F00/F01 x R02/R20). Certificate payload
`4adc4187bb5794ed70fce122055fb94916974c1adacf9451237aff002ebfd63e`.

Relation to this node: THIS NODE ALREADY CLOSES ALL SIX of our aligned-positive
unramified allocations. If the two six-cell blocks coincide, #1149 is partial
independent corroboration of two of them and our record is four cells ahead.
**That coincidence is NOT established.** His axes are (F00,F01) x
(R02,R11,R20) — two fixed-moving assignments by three root patterns — whereas
ours are {fixed-moving, moving-moving} x {same, swap, mixed}; all of his
moving-moving cells were deleted separately in #1144. Until a cell-for-cell
mapping row exists, do not cite #1149 as corroboration of this node, and do
not treat his four retained schemes as contradicting this node's closure: he
proved two cells empty and left four OPEN, never nonempty.

Note for readers of the sibling nodes: the `Still open: ...` lines in the
frontier files of the other five cells are CHECKPOINT-LOCAL (each was written
when that cell closed — "Four of six", "Five of six", "All six"). They are
historical, not stale, and must not be "corrected".
```

---

## 3. maelcar collision check (L1 and LIST/M31)

### 3.1 Result of the check

I grepped `critical/nodes` and `background/nodes` for `#1145`-`#1148`,
`maelcar`, `ell = 11`, `mu_11`, `S_3(P|Q^2)`, `T_sm`, `K(d,e)`.

**No L1 node and no LIST/M31 node cites any maelcar PR.** The only nodes that
mention them are five `xr_*` band/window nodes, and every one is already
correctly disciplined — e.g.
`background/nodes/xr_deficient_window_affine_plane_triple_router/audit.md:15`
("No upstream PR result is silently imported; PR #1148 is fixture-specific"),
`background/nodes/xr_window_divisor_maximality_filter/lineage.md:6-8`
("Reviewed upstream main `93fba1be` and live PRs through `#1148`. No upstream
result was imported"), and similar in
`xr_deficient_window_packed_four_fiber_plane_payment/lineage.md:5`,
`xr_deficient_window_mixed_core_block_payment/lineage.md:9`,
`xr_deficient_window_two_block_kernel_slack_router/lineage.md:5-7`.

So: **zero actual collisions; the exposure is prospective**, and it sits
exactly where the maelcar audit's action list §6 items 5, 7 and 8 predicted —
in the L1 and LIST/M31 lanes, which carry **no** citation discipline at all
today. The addenda below install it before the next move in those lanes.

### 3.2 New catch — a **second** false friend

The maelcar audit flagged `dli_wcl_ell4_weight11_quintic_divisor_descent` as a
false friend. I found a second one it did not:

`background/nodes/petal_reserve_rich_fiber_reduction/verify.py:54` contains the
literal `ell = 11`. It is **not** a cyclotomic order: this node's `ell` is a
**sunflower petal size**, `ell = sigma + 1` (node statement: "For a maximal
sunflower with petal size ell=sigma+1..."), and the literal 11 is a
**mutation-control constant** for two strict inequalities, not a fixture. The
node is PROVED and is `ev` for `petal_mixed_amplification` and `imgfib` —
i.e. it sits in precisely the L1/petal lane the audit warned about. A grep for
`ell = 11` while scoring coverage would hit it.

### 3.3 Proposed addenda — L1

**B1. `dli_wcl_ell4_weight11_quintic_divisor_descent` (background, PROVED)**
Vehicle: addendum in `statement.md` (node has only `node.json`, `statement.md`,
`verify.py`). Trust label: OURS (subtraction check; no external claim adopted).

```markdown
## Addendum 2026-08-03 — false-friend guard (ell = 4, NOT ell = 11)

Subtraction check against upstream PRs #1145/#1146 (maelcar, UNMERGED,
experimental/). Those PRs concern `ell = 11`: a subgroup `H <= F_p^*` of
order 11 with `p = 1 mod 11`, exact-five quintics, and the sharp bound
`S_3(P|Q^2) <= 10`. THIS NODE IS A DIFFERENT OBJECT: it is `ell = 4`,
weight `= 11`, over `mu_2048`. The shared tokens (11, "quintic", cyclotomic
roots, a Bezout-flavoured normalisation) are coincidental. Do NOT score this
node — or `notes/ell4_uniform_form_20260727.md` — as prior coverage of, or
as covered by, any `ell = 11` result. Nothing from #1145/#1146 is imported
here; our repo contains no `ell = 11` object at all.
```

**B2. `petal_reserve_rich_fiber_reduction` (background, PROVED)** — **new
catch.** Vehicle: addendum in the node's statement (or a short node note added
to `refs`). Trust label: OURS (subtraction check).

```markdown
## Addendum 2026-08-03 — false-friend guard (`ell` here is a petal size)

Subtraction check against upstream PRs #1145/#1146 (maelcar, UNMERGED).
`verify.py` contains the literal `ell = 11`. This is NOT the maelcar
`ell = 11` (the order of a subgroup `H <= F_p^*` with `p = 1 mod 11`). Here
`ell` is the SUNFLOWER PETAL SIZE `ell = sigma + 1`, and the literal 11 is a
mutation-control constant for the two load-bearing strict inequalities — not
a fixture, not a group order, and not tied to any prime. Because this node is
`ev` for `petal_mixed_amplification` and `imgfib`, a token-level grep for
`ell = 11` while scoring L1 coverage would hit it spuriously. Do not score it
as coverage of, or as covered by, any `ell = 11` result.
```

**B3. `l1_program_frontier` (critical)** Vehicle: addendum in `statement.md`,
or a note under the node's existing `notes/`. Trust label: EXTERNAL EVIDENCE,
UNMERGED (#1145/#1146), TERMINAL VERIFIED / REDUCTION UNREPLAYED.

```markdown
## Addendum 2026-08-03 — maelcar #1145/#1146 citation discipline; one open check

External evidence, unmerged: PRs #1145 (head `605cc16ff22dd8c02e2780068e0728d16faa7bbd`)
and #1146 (head `f7d8734ead8d673a17e17ca3a5c6adc174e788aa`), maelcar,
experimental/. Trust: their scalar auditors were REPLAYED by us and PASS
(terminal VERIFIED); the reduction/exhaustiveness stages and the C++ census
are UNREPLAYED. Nothing is imported as a theorem and no status moves here.

Subtraction is EMPTY BOTH WAYS at present: our repo contains no `ell = 11`
object, and their fixed-`ell`, fixed-shape, small-prime constants do not touch
our asymptotic sub-Johnson targets (`imgfib`, `l1_mixed_petal_amplification`,
`petal_mixed_amplification`).

**Open domination check (do not skip before the next L1 move).** THEOREM J of
this node is PROVED and uniform in `n, k, q` — strictly more uniform than
"all `p = 1 mod 11`". Translate #1146's row to `(n,k,s)` and test
`s^2 > n(k-1)`: if super-Johnson we cover their bound (never their sharpness);
if sub-Johnson we cover nothing. Until that check is run, claim neither.

**CITATION DISCIPLINE (binding if we ever cite #1146).** Say "for the two
parity supports", NEVER "for ell = 11 exact-five". Their `S_6 <= 20` is proved
for 2 of 252 supports; #1145's own certificate field
`remaining_global_obligations[0]` asks only for `S_6 <= 21` on the other 250.
Also never cite the envelope `(20,22,24,27)` as one state's spectrum — its
increments increase, so no single state attains it; their own witness gives
`(20,22,24,25)`.
```

### 3.4 Proposed addenda — LIST / M31

**C1. `rate_half_list_chamber_affine_rank_bridge` (background, PROVED)**
Vehicle: append to the node's existing `upstream_crosswalk.md` (already in
`refs`), or a new dated note. Trust label: EXTERNAL EVIDENCE, UNMERGED (#1148);
route cuts VERIFIED by our replay, sieves UNREPLAYED.

```markdown
## Addendum 2026-08-03 — this fence dominates the applicability of PR #1148

External evidence, unmerged: PR #1148 (maelcar), head
`7b21de0e01acbe41fa2edbbffa66c5eaf12dd3c5`. Its six Python verifiers were
REPLAYED by us and PASS (route cuts VERIFIED, Schur profile `(16,136,509)`
recomputed from the fixture by two methods); its 10,694,457,224 dense-sieve
normals are C++/HPC and UNREPLAYED — the theorem rests on those.

#1148 classifies which members of the affine hull of sixteen degree-479 M31
syndrome locators split, concluding the hull meets the split locus in exactly
those sixteen vertices. That is a LOCATOR-SIDE statement. This node is
precisely the audit such a result presupposes, and it is PROVED that the
bridge DOES NOT FIRE: locator-side geometry and codeword/affine-side counts
are different objects, "this repo contains no map between them", 0/13
chambers killed. Therefore #1148 moves no list count, no row and no chamber
unless it ships an explicit incidence-to-codeword map. Demand that map before
pricing anything from it.

Their Schur direction is the safe one and survives our other fence: they argue
`dim C^(2) = 136` maximal vs `2k-1 = 31` for GRS, hence NOT GRS. Our
`rate_half_ca_hankel_..._non_grs_route_fence` kills only the converse
("Schur matches GRS therefore hidden GRS"), so it does not apply against them.
```

**C2. `rate_half_list_adjacent_crossing` (critical, TARGET)** Vehicle: addendum
in `frontier.md` (exists) or `attack.md`. Trust label: EXTERNAL EVIDENCE,
UNMERGED. This node is the `evidence_for` consumer of C1, so the fence must be
visible here.

```markdown
## Addendum 2026-08-03 — do not price maelcar #1148 into this target

External evidence, unmerged: PR #1148 (maelcar), head `7b21de0e...`,
UNREPLAYED sieves. Its M31 affine syndrome-locator hull rigidity looks
adjacent to this target and is NOT to be priced into it. Our supplier
`rate_half_list_chamber_affine_rank_bridge` is a PROVED route fence showing
the locator-side-to-codeword-side bridge does not fire (0/13 chambers). #1148
is locator-side and ships no incidence-to-codeword map, so it moves nothing
here. Separately, `upstream_gfv4_affine_span_list_compiler` (PROVED) at
direction dimension 15 on our M31 row yields a cap ~7.5e17 — numerically
vacuous against 16 vertices, so we neither already have their bite nor
duplicate their compiler.
```

**C3 / C4. `l1_m31_t64_quotient_prefix_intercept_fence` and
`l1_m31_depth32_uniform_intercept_counterexample` (background, PROVED)**
Vehicle: append to each node's `upstream_crosswalk.md` (both nodes already
carry one). Trust label: EXTERNAL EVIDENCE, UNMERGED. Same text both nodes:

```markdown
## Addendum 2026-08-03 — adjacent but distinct fixture (maelcar #1148)

External evidence, unmerged: PR #1148 (maelcar), head `7b21de0e...`.
Same ambient family — `p = 2^31 - 1`, degree 479, a ~1023-point M31
quotient-profile domain — but a DIFFERENT SPECIFIC FIXTURE:

| | domain | degree | core | objects |
|---|---|---|---|---|
| #1148 | 1,023 | 479 | 509 | 16 (14 principal + 2 distinguished) |
| `l1_m31_t64_quotient_prefix_intercept_fence` | 1,022 | 479 | 415 | 7 |
| `l1_m31_depth32_uniform_intercept_counterexample` | 1,022 | 479 | — | 1,237 |

No duplication in either direction, but a citation/adjacency duty: cite #1148
as adjacent-distinct in any future M31 move and do not merge the fixtures.
Their "509 core rows" and "fourteen principal locator values" are undefined in
their note against a 1,023-point domain and 16 locators; the 14+2 split was
recovered from their fixture file, not stated. Their sieves are UNREPLAYED.
```

**C5. `l1_m31_fixed_support_divisor_direction_cap_route_cut` (background,
PROVED)** Vehicle: append to its `upstream_crosswalk.md`. Trust label:
EXTERNAL EVIDENCE, UNMERGED.

```markdown
## Addendum 2026-08-03 — apparent tension with maelcar #1148, resolved

External evidence, unmerged: PR #1148 (maelcar), head `7b21de0e...`.
#1148 concludes that a 15-dimensional locator hull has only 16 split members.
This node exhibits the opposite phenomenon: a 6-DIMENSIONAL space containing
67,449 SPLIT divisors. THERE IS NO CONTRADICTION — different regimes: ours is
degree 4,980 at `N = 1,053,557` (rank-seven proper-G terminal); theirs is
degree 479 at 1,023, and they concede fixture-specificity.

But the principle recorded here survives and binds: in our M31 lane,
"low-dimensional implies few split members" is FALSE as a dimension-driven
principle. Consequently #1148's rigidity CANNOT BE LIFTED off its fixture, and
must not be generalised into a dimension-based argument anywhere in this lane.
```

---

## 4. SOL_TARGET_4 — ours, Modal-certified, and unbanked

### 4.1 Where the statement lives, and what is missing

**There is no DAG node for SOL_TARGET_4.** Zero hits for `SOL_TARGET_4`, `T_4`,
`103.07`, `1729295040` in `dag.json`. The conjecture lives in a repo-root
markdown file:

- `SOL_TARGET_4_H4_COLLISION_CENSUS.md:26-28` — "There is an absolute constant
  C such that for all (q, N) as above: `T_4(q, N) <= C N^3`". Hypotheses
  (lines 9-14) are only "q an odd prime with q > 4, N a power of two with
  `N | q - 1`". **No q-vs-N / index hypothesis.**
- `SOL_TARGETS.md:21` — still lists it neutrally as "the next ladder rung",
  untagged, while targets 1 and 3 are tagged REFUTED at lines 11-20.

The file has exactly one commit (`be01f959`, 2026-07-10) and **carries no
falsification appendix**, although the falsification was decided 2026-08-03.
So the fix is a file addendum plus a tag, not a shard edit — and two critical
nodes deserve the node-local consequence (§4.3).

### 4.2 The falsification (ours)

Coordinator Modal run `ap-sx9plNuGHtzGtGYisoYrh0`, exact-integer census,
result `experiments/prize_resolution/sol_target4_n256_result.json`
(sha256 `27ed261e...`), generator
`experiments/prize_resolution/sol_target4_n256_modal.py`, commits `c8a48d9e`
(launch) and `8d6f1aeb` (decision):

| row | index `(q-1)/N` | `T_4` | `T_4/N^3` |
|---|---|---|---|
| `N=256, q=257` | 1 | 1,729,295,040 | **103.07** |
| `N=256, q=769` | 3 | 63,361,728 | 3.78 |

The `(256,257)` row is **fully admissible under the conjecture's own
hypotheses** (257 odd prime > 4; 256 a power of two; `256 | 256`). The
algorithm was validated against our banked `(32,97) = 792` anchor
(`critical/nodes/u1_x4_direct_column_budget/notes/F3_IDENTIFICATION.md:21`) and
against maelcar's independently replayed `n=128` row. No absolute constant `C`
survives: the index-1 family's ratio scales as `~ N^2/576` (first-moment
pigeonhole into `q^3 ~ N^3` keys).

### 4.3 Proposed addenda

**D1. `SOL_TARGET_4_H4_COLLISION_CENSUS.md` (+ `SOL_TARGETS.md:21`)**
Trust label: **OURS — MODAL-CERTIFIED, exact integer census, replayed against a
banked anchor.** Follows the house precedent for SOL_TARGET_1 ("REFUTED AS
WRITTEN ... preserved with the replay appendix", `SOL_TARGETS.md:11-12`).

```markdown
## Addendum 2026-08-03 — FALSIFIED AS STATED; reprice forced

Ours. Coordinator Modal run `ap-sx9plNuGHtzGtGYisoYrh0`; exact integer
census; result `experiments/prize_resolution/sol_target4_n256_result.json`
(sha256 `27ed261e...`); generator
`experiments/prize_resolution/sol_target4_n256_modal.py`; decided in commit
`8d6f1aeb`. Algorithm validated against our banked `(32,97): T_4 = 792`
anchor and against maelcar #1147's independently replayed `n = 128` row.

The conjecture above quantifies over ALL `(q,N)` with `q` an odd prime `> 4`,
`N` a power of two and `N | q-1`. It carries no `q`-vs-`N` hypothesis. At the
FULLY ADMISSIBLE row `N = 256, q = 257` (index `(q-1)/N = 1`):

    T_4 = 1,729,295,040 ,   N^3 = 16,777,216 ,   T_4/N^3 = 103.07 .

At `N = 256, q = 769` (index 3): `T_4 = 63,361,728`, ratio `3.78` — still
rising from `2.87` at `N = 128`. No absolute constant `C` survives: the
index-1 family's ratio grows as `~ N^2/576`, by elementary first-moment
pigeonhole into the `q^3 ~ N^3` key space, which predicts unbounded growth.
**The conjecture is FALSE AS STATED.**

REPRICE FORCED (wording is a surfaced decision, not applied here): the
statement needs an index hypothesis — either an explicit index floor, or the
form `T_4 <= C(index) N^3` with `C(index)` DECREASING in `index = (q-1)/N`,
re-calibrated on the banked `(32,97)` anchor. Note that every in-repo `n^3`
census node carries such a guard already (`f3_hge4_aggregate_budget` and
`f3_hge4_norm_gate_count`: "every prime `p = 1 mod n` with `p >= n^2`";
`f3_h2_stratum_theorem`: "`n <= q^{2/3}` implied by F3's own regime
`q >= n^2`"). The guard was simply not carried into this target.

BRIDGE ADOPTED (from the maelcar #1147 audit, proved exactly at `(32,97)`):
their Paper-D smooth-trade currency `T_sm` is this census restricted and
normalised — `T_4^{smooth,ordered} = 2n T_sm` on free orbits, reconciling our
banked `792 = 2 x 396 = 2 x (288 smooth + 108 non-smooth)` with their
`T_sm = 9`. So their smooth target `T_sm <= n^2/2` is exactly this bound with
`C = 1` on the smooth locus. Their aggregate energy inequality, if it ever
closes, is a direct input here. (#1147 is UNMERGED; the bridge is OURS,
computed by our own replay.)
```

And in `SOL_TARGETS.md:21`, retag the entry from "the next ladder rung" to
**"REFUTED AS WRITTEN (2026-08-03) — preserved with the falsification
appendix; reprice with an index hypothesis pending"**, matching the wording
used for targets 1 and 3.

**D2. `h4_terminal_dichotomy` (background, PROVED, `key: true`)**
Justification: this node is the SAME h=4 object ("P,Q disjoint 4-subsets with
equal top-3 elementary symmetric sums") in **structural** form. The
falsification is a node-local fact about what may and may not be inferred from
it. Trust label: **OURS — MODAL-CERTIFIED.**

```markdown
## Addendum 2026-08-03 — no counting corollary without an index hypothesis

Ours. Modal run `ap-sx9plNuGHtzGtGYisoYrh0`; exact census; result
`experiments/prize_resolution/sol_target4_n256_result.json` (sha256
`27ed261e...`); decided in commit `8d6f1aeb`.

This node is the STRUCTURAL dichotomy on exactly the object counted by
`T_4(q,N) = #{ordered disjoint 4-subset pairs of mu_N with equal p_1,p_2,p_3}`.
The corresponding COUNTING statement `T_4 <= C N^3`
(`SOL_TARGET_4_H4_COLLISION_CENSUS.md`) is now FALSIFIED AS STATED: at the
admissible index-1 row `N = 256, q = 257`, `T_4/N^3 = 103.07`, with the
index-1 ratio growing as `~N^2/576`. Therefore this dichotomy must NOT be
used to derive any `O(N^3)` count for this object without an explicit index
`(q-1)/N` hypothesis. The dichotomy itself is untouched — it is a
per-configuration branch statement, and nothing above bears on its proof.
```

**D3 / D4. `f3_hge4_aggregate_budget` (critical, CONDITIONAL) and
`f3_hge4_norm_gate_count` (critical, TARGET)** Justification: both carry the
`p >= n^2` corridor guard; the falsification demonstrates empirically that the
guard is **load-bearing, not cosmetic**, which is directly node-local. Trust
label: **OURS — MODAL-CERTIFIED.** No status moves. Same text for both:

```markdown
## Addendum 2026-08-03 — the `p >= n^2` corridor guard is load-bearing

Ours. Modal run `ap-sx9plNuGHtzGtGYisoYrh0`; result
`experiments/prize_resolution/sol_target4_n256_result.json` (sha256
`27ed261e...`); commit `8d6f1aeb`.

This node's statement is scoped to "every prime `p = 1 mod n` with
`p >= n^2`". That guard is now known to be load-bearing rather than
conventional. The sibling `n^3`-shaped counting statement over the same
family but WITHOUT the guard (`SOL_TARGET_4_H4_COLLISION_CENSUS.md`,
`T_4 <= C N^3`, hypotheses only `N | q-1`) is FALSE: at the admissible
index-1 row `N = 256, q = 257` the exact census gives `T_4/N^3 = 103.07`,
and the index-1 ratio grows as `~N^2/576` by first-moment pigeonhole into
`q^3 ~ N^3` keys. Do not weaken or drop the corridor hypothesis here, and do
not import any `n^3` census bound that lacks an index/corridor guard.
```

---

## 5. Export ledger check (§3 of the brief) — recommendation only, no action

### 5.1 What #1143 already has

PR #1143 (ours, AllenGrahamHart), head `b1489664ed4dcee4ba156eff37f4a33e04065094`,
**DRAFT**, 69 commits, stacked on #1132 at `543db66f`. Its last two commits are
the export batches:

- `02d2788f7` "Close the complete positive 433-1a route: aggregation export
  (waves 3x)" — 2026-08-02;
- `b1489664e` "Close positive 433-1b cell 14: complete closure export
  (waves 42-43)" — 2026-08-03.

So **cell 14 is already exported** (ledger line 534: "EXPORT EXECUTED (#1143,
commit b1489664)", with maintainer comment `issuecomment-5164524383`).

### 5.2 What is now export-eligible but unshipped

1. **Cell 3 and cell 6** — closed in WAVE 45 on 2026-08-03 (`CAMPAIGN_LEDGER.md:908-910`:
   "cell 3 closed 1680/1680 (DE 6-14 + xi3 x6 + xi4 transport + xi5 + xi6);
   cell 6 = duplicate-role transport, closed"). Atlas state: "1a complete;
   1b cells 0, 1/2, 3, 6, 14 closed. cell 4 opens (four-basis tower)."
2. **The band-flip narrative** — WAVE 46, 2026-08-04:
   `xr_graded_tangent_band_charge` TARGET -> CONDITIONAL on SL-2 alone;
   census 246 = 179/41/26; audited SOUND as the first worker-initiated
   critical status flip (`WAVE46_AUDIT.md`).
3. **THE SIX ALIGNED-POSITIVE UNRAMIFIED CELL CLOSURES** — not on any export
   list I found, and in my view now the highest-value item in the batch.

### 5.3 Recommendation (one paragraph)

The export batch should be re-ordered. As tracked, the batch is "cells 3/6/14 +
possibly the flip narrative", but cell 14 already shipped at `b1489664e`, so the
real delta is cells 3 and 6 plus the band flip — and neither is time-critical,
because nobody upstream is working those cells. What *is* time-critical is the
item nobody has listed: all six `rate_half_kb_m2_r4_diagonal_c2_112_aligned_positive_unramified_*`
allocations are PROVED in our tree and have never been exported, while upstream
still sees only #1132's stale printed residual `remaining_unramified=6,
deep_cases=17` — and Scott's #1149 has just spent a full Sage/Singular cycle
closing two cells of a block he explicitly selects from our workboard because
that counter says it is open. Every further cycle he spends there is duplicated
work caused by our own unshipped closure, which is the same asymmetry the
2026-08-01 addendum already diagnosed ("his material ships upstream
immediately, our `kb_m2_r4` campaign has never been exported") and which the
#1143 export demonstrably fixes. So: ship the six-cell closure first, in the
same packet as the cell-for-cell mapping row we owe #1140 (state our partition
— {fixed-moving, moving-moving} x {same, swap, mixed} — against his F/M x
R02/R11/R20 and explicitly decline to assert identity, per FLAG S-1); then
cells 3 and 6; then the band flip, which is narrative rather than K3 and can
ride along or wait. Per the standing pacing rule, readiness from a clean
checkout gates this, not triage depth — and note that all three of #1143,
#1149 and #1144 remain unmerged with the queue frozen since 2026-07-07, so
"export" here means adding to our open draft, not expecting integration.

---

## 6. FLAGS

| # | severity | flag |
|---|---|---|
| S-1 | **MEDIUM** | Scott's six-cell "aligned-positive unramified" block is **not established** to be our six allocations — different partition axes (his: 2 fixed-moving assignments x 3 root patterns; ours: {fixed,moving}-moving x {same,swap,mixed}). Our 6/6 vs his 2/6 is not a contradiction under either reading. **The mapping row owed since 2026-07-31 is still missing on both sides.** Do not assert identity — but note all four qualifiers now match (m=2, diagonal, `c2(1,1,2)`, aligned-positive), so identification is likely. |
| S-2 | LOW-MED | Pin drift: #1139 is stacked on #1132@`c2edcfa5`; our #1132 is now at `543db66f` (one commit ahead, 10 files). Reprice the `26->2` composition against the current head. |
| S-3 | LOW | In #1149's certificate the six "distinct" orbits carry only **four** distinct resultant hashes (`R02` and `R20` coincide within each of the F04/F07 and F05/F06 families); only the `U,V,Z` cores separate them. Not an error, possibly an unexploited symmetry. **ASK, do not assert.** |
| S-4 | — | **Nothing in #1149 was replayed by us** (Sage/Singular, outside the compute law). All its claims are CONTENT-REVIEWED AT PINNED HEAD only. It is a DRAFT whose author states cell-specific proof review is outstanding, and its self-label is `PROVED_EXACT_LOCAL_LEMMA_REVIEW_REQUIRED_K3_OPEN`. |
| S-5 | **MEDIUM** | **A standing hold whose rationale has expired.** `PR_SWEEP_20260803.md:41-43` and `CAMPAIGN_LEDGER.md:479` hold the diagonal-node export because "Scott has NOT covered the diagonal cells". #1149's certificate atom is `K3_M2_DIAGONAL_112_ALIGNED_POSITIVE_FIXED_MOVING` — he now is. Coordinator decision, surfaced not taken. |
| S-6 | LOW | Conflation guard: "EXACTLY TWO residual terminal types" (`PR_SWEEP:34-36`, outer frontier) and "#1149 closes two more 112 cells" (`WAVE46_AUDIT:46`, atlas) are different twos on different frontiers. Scott's open **cell** count is **16** and is recorded nowhere in our tree. |
| S-7 | LOW | I could not verify #1139's `26 -> ... -> 2` composition itself, nor the four semantic gates, nor the `2^21` dihedral computation — all reported from his note and certificate at the pinned head. Labelled UNREPLAYED throughout. |
| M-1 | **MEDIUM (new catch)** | Second false friend: `background/nodes/petal_reserve_rich_fiber_reduction/verify.py:54` has a literal `ell = 11`, where `ell` is a **sunflower petal size** and 11 is a **mutation-control constant**. The node is `ev` for `petal_mixed_amplification` and `imgfib` — squarely in the lane at risk of false coverage scoring. Not flagged by the 2026-08-03 audit. |
| M-2 | LOW | Zero maelcar collisions found in L1 / LIST/M31 nodes — but also **zero citation discipline** there today. The five `xr_*` band/window nodes are already correctly disciplined; the L1 and M31 lanes have nothing. Addenda B1-B3, C1-C5 install it before the next move. |
| M-3 | — | maelcar audit flags F1-F11 are **not** re-verified here; I carried them forward as recorded. In particular #1148's unexplained 7-normal discrepancy (F4) and #1147's `max C_r = 5789` (PLAUSIBLE-UNREPLAYED) remain open questions to the author, unasked (read-only). |
| L-1 | LOW | **Ledger inconsistency, raised not fixed.** `CAMPAIGN_LEDGER.md:969` and `WAVE46_AUDIT.md:45` both list the pending export batch as "cells 3/6/14", but cell 14 shipped on 2026-08-03 at `b1489664e` (ledger line 534). Either the batch phrase is a stale carry-forward, or it intends a re-package of cell 14 alongside 3/6 for atlas coherence. I did not guess; §5 treats the delta as cells 3 + 6 + band flip. **Coordinator to confirm which.** |
| L-2 | — | The `Still open: ...` lines in the five non-terminal aligned-positive unramified `frontier.md` files are **checkpoint-local and historical** ("Four of six", "Five of six", "All six"), not stale. Recorded here so they are not "corrected" during wiring. |
| L-3 | LOW | SOL_TARGET_4's falsification sha is written only as `27ed261e...` in one line of `notes/pilots_20260803/maelcar_audit/FABLE_AUDIT.md`; **no manifest pins it**. If the appendix is wired, consider pinning the full digest. |
| L-4 | — | **No DAG node exists for SOL_TARGET_4**, so D1 is a repo-root file edit, not a shard edit. D2-D4 are the node-local consequences. Whether SOL_TARGET_4 should also be minted as a node is a **surfaced decision**, not proposed here. |
| P-1 | **process, self-reported** | **I broke the compute law during this pilot.** I invoked bare `python3 -c` (not `tools/ramguard tiny -- python3`) roughly a dozen times to pretty-print JSON from `gh api` / `gh pr view` and to read `node.json` fields. All were sub-second, few-KB text transforms with no mathematical content, and no result in this document depends on a computation — every number here is quoted from an upstream artifact, a repo file, or a previously banked run. No new mathematical compute was run at all. Recording it because an audit that hides its own protocol slips is worthless; re-running is unnecessary but the deviation is real. |

---

## 7. Wiring notes for the coordinator

- All 14 texts above are drafts for **your** line-audit; I wrote none of them
  into any node, file, shard, or `dag.json`.
- **House formats available** (I matched Format B for A1; pick per layer):
  - *Format A* — structured `upstream` block inside `node.json`, exactly two
    keys `label` + `relation`; observed relations are `IDENTICAL`, `OVERLAP`,
    `ANALOGY_ONLY`, `OVERLAP_AND_ADDITIVE`, `IDENTICAL_AT_PRINTED_SCOPE`
    (32 nodes use it). If you add one for A2, the honest value today is
    **`ANALOGY_ONLY`** — matching the registry's own classification of this
    author-adjacency pattern — and it should be upgraded to `OVERLAP` or
    `IDENTICAL_AT_PRINTED_SCOPE` **only once the FLAG S-1 mapping row exists**.
  - *Format B* — dated `## Addendum <date> — <title>` prose closing with a
    `Watch:` line, in a node note. Used by A1; it is the established K3
    contributor-review vehicle.
  - *Format C* — `## Upstream review custody` block in a `source_evidence.md`
    (280 such files), pinning PR URL, commit, blobs, payload SHA-256 and an
    "Accessed <date>" line. This is the most rigorous vehicle for A2 if you
    want the #1149 head, note blob and payload
    `4adc4187bb5794ed70fce122055fb94916974c1adacf9451237aff002ebfd63e` pinned
    formally rather than in prose.
  - *Format D* — `statement.md` header field `- **upstream source:** draft
    PR #N, independently reconstructed here` plus an `upstream_crosswalk.md`
    carrying `relation` / `independence` / `scope fence`. This is the closest
    precedent for C3/C4 and I drafted those to slot into it.
- A1 needs no shard change (the note file is already in `rate_half_band_closure`'s
  `refs`). A2 and B2 create new node notes and therefore need the file adding to
  the node's `refs` in its `node.json`, then `compile_dag.py --write` plus the
  verify chain, per the v11 write path.
- B1, B3, C2 are addenda inside existing `statement.md` / `frontier.md` files —
  no `refs` change. C1, C3, C4, C5 append to existing `upstream_crosswalk.md`
  files — no `refs` change.
- D1 touches two repo-root markdown files, not the graph. D2-D4 are addenda to
  existing node files.
- Status changes proposed: **none**. Edges proposed: **none**. Census impact:
  **none**.
