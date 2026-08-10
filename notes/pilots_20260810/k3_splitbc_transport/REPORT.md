REPORT — k3_splitbc_transport (round 30)

The harness blocks writing report `.md` files, so `REPORT.md` could not be created on disk; the full report text is returned below (and `DRAFT_CODEX_BRIEF.md` **is** on disk at `notes/pilots_20260810/k3_splitbc_transport/DRAFT_CODEX_BRIEF.md`, along with `PREREG.md` with my registrations and `label_orbits.py`).

---

# REPORT — k3_splitbc_transport (round 30)

Transport/quotient audit of the `433-1b -&gt; O0b` split-BC product-rank-five owner block (360 common rows, 37,800 raw outside labels), against the closed `433-1b -&gt; O0a` owner machinery. AUDIT AND DRAFT ONLY: no census, no elimination, no node edits, nothing written outside this directory.

Artifacts in this directory: `PREREG.md` (brief + my blind priors), `label_orbits.py` (the one script I ran), `DRAFT_CODEX_BRIEF.md` (D3). This report could not be written to disk (harness blocks report-file writes) and is delivered as the pilot's return text.

## Verdict in one paragraph

The transport is **sharply asymmetric and the asymmetry is not the one the cycle-17 note implies**. The *common/source* layer of the split block does not merely "share a rank-drop locus" — it is **literally the same 60 compiled algebra rows** as the closed O0a route, so every per-cell common curve/tower certificate already banked for `433-1b -&gt; O0a` is valid verbatim for all six O0b split lanes at zero cost. The *outside* layer genuinely must be rebuilt, but it is not a blank sheet: four exact transports, three of which are one-line consequences of already-PROVED O0b nodes, cut the block from 37,800 raw labels to **11,304 representative systems** (factor 3.34) before any algebra runs, and a fifth certificate that does not yet exist in this repo would take it to about **3,414** (factor 11.1). No guard-only closure is proposed anywhere, so the verdict is consistent with the PR #1155 fence rather than in tension with it.

---

# D4 — MISSES AND SEAMS (first)

## M1 — HIGH. A "universal" node that is silently route-specific, and whose misuse would delete 65% of the workload falsely

`background/nodes/rate_half_kb_m2_r4_coordinate_positive_433_1b_universal_generic_outside_label_orbit_quotient` is titled "universal 433-1b outside-label quotient" and states, with **no route qualifier**:

&gt; "In every positive deployed `433-1b` common role cell, the involutions `P=(0 1)`, `Q=(3 4)` on the seven outside records induce exact system bijections on the 105 omitted-record/residual-matching labels." — `statement.md:5-11`

and `node.json:8` repeats "For every guarded positive deployed 433-1b common role cell". But it `requires` `..._433_1b_o0a_signed_edge_atlas` (`node.json:25`) and its atlas is the O0a record list `DE, DE, -DE, DF, sigma_o EF, BF, sigma_c CF` (`proof.md:6`).

**Both generators fail on `433-1b -&gt; O0b`:**

- `P` exchanges two *identical* `DE` records. O0b's `S0` and `SBC` lanes have `de` and `-de` (`..._o0b_split_rankdrop_complete_exclusion/proof.md:12`; `..._o0b_common_repeat_cell3_outside_label_quotient/node.json:8`), which are not identical. `P` exists on O0b only in `SDE`/`SDF`.
- `Q` is the `D/E` transport `(d,e,f) -&gt; (sigma_o e, sigma_o d, f)`, and its proof needs `bf` and `sigma_c cf` to be **fixed** (`..._433_1b_universal_xi4_xi3_outside_role_transport/proof.md:17-18`), which holds only because O0a normalizes *both* colored incidences to `F` (`..._433_1b_o0a_signed_edge_atlas/statement.md:33`). O0b's colored edges are `BE` and `CF` (`..._o0b_signed_edge_atlas/statement.md:8-9`), so `d &lt;-&gt; e` sends `be -&gt; bd`, which is not a record at all.

Applying its 105-&gt;36 census to an O0b lane would falsely delete 65.7% of the labels. Its parent `..._universal_xi4_xi3_outside_role_transport` **is** correctly scoped ("For every guarded positive deployed `433-1b -&gt; O0a` common role cell", `statement.md:5`); the child dropped the `-&gt; O0a`. Recommended fix (coordinator-gated, I did not apply it): add `o0a` to the statement scope line and a one-sentence non-transport addendum naming O0b.

## M2 — MEDIUM. Quantifier slippage in the partition node's own statement

`..._433_1b_o0b_residual_owner_partition/node.json:8` says

&gt; "The six split-BC lanes contribute 6*15*4=360 **product-rank-five** common rows"

but its `proof.md:5-7` derives

&gt; "Hence the split side has `6*15*4=360` **formal** common rows. The split rank-drop parent excludes the complete rank-at-most-four branch, so every possible split survivor belongs to the rank-five principal branch."

Those are different claims. Rank-five is a *branch* condition on a locus, not a property of a row: the 16 deployed rank-drop points sit inside eight of those very rows, in cells 9 and 10 (`..._433_1b_product_rankdrop_deployed_rational_classifier/statement.md:35-38`). `statement.md:10` of the same node hedges correctly ("split BC, product rank five | 6*15*4 = 360"), so only the `node.json` sentence is loose. No count is affected.

## M3 — MEDIUM, and it is the largest single free win. A PROVED node is under-scoped by exactly the block we care about

`..._433_1b_o0b_common_repeat_cell3_outside_label_quotient` is scoped to "the 105 ... labels in a **repeated-BC cell-3** outside system" (`statement.md:4`). Its proof uses **nothing** from cell 3 and nothing from the BC repetition: it is `d -&gt; -d` acting on the outside records only (`proof.md:1-13`), and its only `requires` edge is the O0b signed-edge atlas (`node.json:24-26`).

The `S0` split lanes have the **same seven outside records** as `SBC`:

```text
S0:  be,cf,de,-de,df,-df,sigma_o ef      (split_rankdrop proof.md:12)
SBC: (BE,CF,DE+,DE-,DF+,DF-,EF)          (cell3 quotient node.json:8)
```

and the atlas proof confirms the two strata differ only on the common side plus the `EF` sign: "In `SBC`, the common-triangle invariant is precisely `sigma`; the other invariant changes only the outside `EF` record" (`..._o0b_common_vieta_minor_atlas/proof.md:10-12`). So a PROVED 105-&gt;57 quotient already covers 12,600 of the 37,800 split labels, and its statement happens to exclude them.

## M4 — LOW/MEDIUM. Cross-route dependency whose parent's stated scope is the other route

`..._433_1b_o0b_split_rankdrop_complete_exclusion/node.json:29` requires `..._433_1b_product_rankdrop_deployed_rational_classifier`, whose scope line reads "deployed-field rational points on the finite exceptional common schemes of **`433-1b -&gt; O0a`**" (`statement.md:4-5`). The licence for the cross-route use lives only in the *consumer's* prose: "The split common products are identical to the certified `O0a` split compiler, so the rank-drop rational classifier transfers exactly" (`..._split_rankdrop_complete_exclusion/proof.md:3-4`). The parent's `claim_contract.md:6` carries no route qualifier, so this is not a correctness bug, but a mechanical parent-scope check would flag it. Per the node-local notes rule, the route-independence fact belongs *in* the parent as a statement addendum.

## M5 — MEDIUM. Row-deletion asymmetry between the two blocks is a certificate gap, not a geometric fact

The repeated side deleted **160 of 240** formal rows as common-unit (`..._o0b_common_repeat_saturation_classification/proof.md:22-24`: "80 unit and 40 surviving algebra rows ... hence 160 deleted and 80 surviving formal systems"). The split side deleted **0 of 360**: no saturation classification exists for the 60 split algebra rows. So "the residual is exactly 408 rows" is an exact *ledger* count of what is not yet closed, and must not be read as "360 split rows are irreducible".

Honest downgrade of my own suggestion: the expected yield of running the split saturation is **low**, because the O0a route's split common loci are positive-dimensional in essentially every cell — `cell3_compact_curve_kernel`, `cell4_four_basis_tower_kernel`, `cell5_elliptic_common_kernel`, `cell9_global_five_relation_common_locus`, `cell11_quadratic_four_basis_common_locus`, `cell12_elliptic_four_basis_common_locus`, `cell14_quadratic_curve_structure`. The repeated side's unit rows come from the coincidence `bc = bc` in the products `(-1,b,c,sigma*bc,sigma*bc)` (`..._o0b_common_vieta_minor_atlas/statement.md:11-12`), which the split products `(-1,b,c,bc,-bc)` do not have. I therefore do **not** recommend it as a first move; I record it so nobody mistakes 360 for a lower bound.

## M6 — HIGH VALUE, MISSING CERTIFICATE. There is no 433-1b source root-sign quotient in this repo

`ls background/nodes | grep -i root_sign` returns exactly three ids, all `433-1a`-scoped: `..._433_1a_cell1_2_common_root_sign_orbit_exclusion`, `..._433_1a_cell58_complete_root_sign_orbit_exclusion`, `..._433_1a_common_root_sign_symmetry_quotient`.

The 1a quotient collapses "the 60 raw rows to exactly ten algebraically distinct matching/root-sign representatives" (`..._433_1a_common_root_sign_symmetry_quotient/statement.md:44-45`), and its cells-3..14 argument is entirely source-side: "The loop is the canonical root-`1` anchor and has `q=0`, so its deck mate represents the same loop record. Hence all four sign rows of each such cell form one exact orbit" (`.../statement.md:23-25`). In 433-1b, cells 3..14 likewise have the loop role `LA` inside a pair rather than as the singleton (cells 0, 1, 2 are the `LA`-singleton cells: `..._433_1b_cell0_complete_exclusion/statement.md:10-14`, `..._433_1b_cells1_2_complete_exclusion/statement.md:13-14`). Every split count in the DAG carries a factor of 4 for source-root signs that this quotient would remove in 12 of 15 cells.

Caveat I am registering rather than hiding: the 1a cell-0/1/2 arguments use "the two identical `AB+` roles" (`.../statement.md:27-35`), and the 433-1b split common products `(-1,b,c,bc,-bc)` are five *distinct* values (`..._433_1b_common_vieta_minor_compiler/statement.md:16-19`), so only the source-reciprocity half of that argument is available in 433-1b cells 0,1,2. The port is therefore "cells 3..14 clean, cells 0,1,2 need their own argument".

## M7 — MEDIUM. The 105-label ledger is uniform in *count* but is not one object

The factor 105 is genuinely uniform across all three residual blocks: "For each formal common row there are seven missing-record choices and fifteen matchings of the remaining six records, exactly 105 raw outside labels" (`..._o0b_residual_owner_partition/proof.md:20-22`). My blind prior R3 predicted exactly this and it holds: `37,800 = 360 x 105`, `1,680 = 16 x 105`, `3,360 = 32 x 105`.

But the *canonical orbit ledger* with SHA `70c074ad010a7c8a03c84d6eaeb6206f14b941de455301180c9aa51a03f02b91` (`..._o0b_common_repeat_cell3_outside_label_quotient/statement.md:29-30`) is tied to the record list `(BE,CF,DE+,DE-,DF+,DF-,EF)`. `S0` and `SBC` share that list; `SDE` and `SDF` do not — their records 2,3 (resp. 4,5) are equal (`experiments/prize_resolution/rate_half_kb_positive_433_1b_o0b_split_rankdrop_outside_modal.py:169-178`). Reusing that ledger on `SDE`/`SDF` would be wrong. Their correct census is 60 orbits, not 57 (section D2, C5).

## M8 — PASS. The three blocks do partition, with nothing dropped or double-counted

I checked the full route ledger and it closes exactly:

```text
formal route labels   10 lanes x 15 cells x 4 rows x 105        = 63,000
  closed: repeated common-unit rows      160 rows x 105         = 16,800
  closed: repeated cells 3/6              32 rows x 105         =  3,360
  residual                                                       42,840
```

`63,000 - 16,800 - 3,360 = 42,840`, exactly the partition total (`..._o0b_residual_owner_partition/statement.md:9-13`). Sources for the inputs: 600 formal lane/source systems (`..._o0b_common_vieta_minor_atlas/statement.md:19-24`), 160 deleted / 80 surviving repeated rows (`..._o0b_common_repeat_saturation_classification/proof.md:24`), survivor split 16 / 32 / 32 (`..._o0b_residual_owner_partition/proof.md:12-19`).

Two overlap traps I specifically checked and cleared:

- The split rank-drop closure removes **no row**. It closes a branch at 16 deployed points inside cells 9/10 rows (`..._o0b_split_rankdrop_complete_exclusion/statement.md:7-8, 16-27`), so the 360 rows correctly stay in the residual and the 10,080 excluded systems are not subtracted from 37,800. No double count.
- The repeated-side residual cells `{1,2}` and `{11,14}` are `BC1&lt;-&gt;BC2` orbit pairs; that involution "fixes three role cells and pairs the other twelve" (`..._o0b_common_repeat_saturation_classification/proof.md:18`), and the three fixed cells are `{0,3,6}` — consistent with cells 3/6 being the closed block. No cell is in two blocks.

## M9 — Answers to the pre-registered D4 questions (PREREG R4)

1. `360 + 16 + 32 = 408` is a sum of *formal* rows over disjoint lane sets (six split lanes vs four repeated lanes); disjointness is by lane, not assumed. **No hidden assumption.**
2. The 105-ledger is uniform in count, not in object. **See M7.**
3. The 16 rank-drop points are *inside* the 360 rows, at deployed points of cells 9/10 rows; they are neither a separate block nor double-counted. **See M8.**
4. The "360 common rows" of the split block and the "360 representative residual-pairing systems" of the cells-3/6 uncolored payment (`notes/work_cycles/roadmap_r3/17-positive-433-repeat-bc-20260810.md:41-42`) are **an index collision, not a relation**: the first is `6 lanes x 15 cells x 4 sign rows`, the second is `3 packets x 120 representative cases`. Worth not confusing in prose.
5. "Raw outside labels" is pre-quotient throughout, and the closed blocks were also counted pre-quotient (160 rows x 105 = 16,800). The totals are commensurable. **No miss.**

---

# D1 — THE MACHINERY MAP

## D1.1 What "the closed O0a campaign" actually is

`433-1b -&gt; O0a` is one of the two already-proved positive routes (`critical/nodes/rate_half_kb_m2_r4_coordinate_positive_remaining_route_payment/node.json:7`: "except the already proved 433-1a to O0b and 433-1b to O0a routes"). It is **entirely a split-BC route**: its defect budget is spent by the loop (1) and the multiplicity-three `DE` pair (2), so "the two `BC` records have opposite signed types" is forced (`..._433_1b_o0a_signed_edge_atlas/statement.md:20-24`, `proof.md:5-8`). There is no repeated-BC stratum in O0a at all. Hence "the closed O0a split-BC owner machinery" = the whole closed `433-1b -&gt; O0a` route, carried by the un-prefixed `..._433_1b_cell*` node family.

## D1.2 The O0a machinery, by layer

| layer | node (`background/nodes/rate_half_kb_m2_r4_coordinate_positive_...`) | mechanism |
|---|---|---|
| target atlas | `433_1b_o0a_signed_edge_atlas` | vertex sign gauge, 128 assignments -&gt; 4 orbits of size 32, invariants `(sigma_c, sigma_o)` (`statement.md:43-48, 59-61`) |
| common compiler | `433_1b_common_vieta_minor_compiler` | 15 role cells x 4 root-sign rows = 60 rows; six maximal minors `det(B,Q_i,Q_j)` (`statement.md:22-25, 47-55`) |
| rank-drop branch | `433_1b_product_rankdrop_common_exception_classifier` | localized ideal of 6 cofactors of `P` + 45 minors of `M` + Rabinowitsch; unit in cells 0,1,2,3,6; zero-dimensional in the other ten (`statement.md:39-55`) |
| rank-drop points | `433_1b_product_rankdrop_deployed_rational_classifier` | FGLM to shape position, exact factorization; 32 rows empty, 16 deployed points, all in cells 9/10 (`statement.md:10-15, 29-38`) |
| role-cell quotient | `433_1b_cells1_2/3_6/4_7/5_8/9_10/12_13_duplicate_role_*` | target `B&lt;-&gt;C`, roles `AB&lt;-&gt;AC`; e.g. cell 9 -&gt; cell 10 with `(e1,e2)-&gt;(e1,-e2)` (`cells9_10_duplicate_role_transport/statement.md:3-14`) |
| outside label quotient | `433_1b_universal_generic_outside_label_orbit_quotient` | `P` = exchange of the two identical `DE` records, `Q` = `D/E` transport; 105 -&gt; 36 orbits, profile `1:3, 2:15, 4:18` (`statement.md:5-16`) |
| outside role transport | `433_1b_universal_xi4_xi3_outside_role_transport` | `(d,e,f) -&gt; (sigma_o e, sigma_o d, f)` swaps records 3,4; fixes every role cell (`statement.md:5-12`, `proof.md:11-18, 31-34`) |
| per-cell closures | `433_1b_cell0/cells1_2/cell3/cell4/cell5/cell9/cell11/cell12/cell14_complete_exclusion` | rank-five branch, per-label: reciprocal-square / reciprocal-linear / nested-signfree / quadratic-resultant / common-F-resultant families |

Role cells: "produces exactly `5*3=15` role cells, indexed `0,...,14`" (`433_1b_raw_workboard_complete_exclusion/proof.md:5`) — a singleton role among `{LA,AB,AC,BC+,BC-}` times one of the 3 matchings of the other four (`433_1b_universal_xi4_xi3_outside_role_transport/proof.md:31-32`). The `AB&lt;-&gt;AC` involution therefore has orbits `[0] | [1,2] | [3,6] | [4,7] | [5,8] | [9,10] | [11] | [12,13] | [14]` — nine orbits, three fixed cells — which is exactly the node inventory above, and is printed as `(KBRSQ-2)` in `433_1a_common_root_sign_symmetry_quotient/statement.md:40-41`.

## D1.3 The O0b split-BC rank-five block, exactly

- Strata: `S0` (BC, DE, DF all split, defect 1), `SBC`, `SDE`, `SDF` (`..._o0b_signed_edge_atlas/statement.md:20-25`); ten target-gauge lanes `S0:2, SBC:4, SDE:2, SDF:2` (`statement.md:29-34`). Split = the six non-`SBC` lanes (`..._o0b_common_vieta_minor_atlas/proof.md:3-5`).
- Common products for all six split lanes: `(-1,b,c,bc,-bc)`, "and transport exactly to the existing split compiler" (`..._o0b_common_vieta_minor_atlas/statement.md:10-11`).
- Outside records, from the banked executable (`experiments/prize_resolution/rate_half_kb_positive_433_1b_o0b_split_rankdrop_outside_modal.py:163-188`):

```text
idx   0        1        2        3        4        5        6
S0   (b e,+) (c f,+) (d e,+) (-d e,-) (d f,+) (-d f,-) (s_o e f, s_o)
SDE  (b e,+) (c f,+) (d e,+) ( d e,+) (d f,+) (-d f,-) (s_o e f, s_o)
SDF  (b e,+) (c f,+) (d e,+) (-d e,-) (d f,+) ( d f,+) (s_o e f, s_o)
squared sums: (b+e)^2 (c+f)^2 (d+e)^2 (d-e)^2 (d+f)^2 (d-f)^2 (e+s_o f)^2
```

- Rank-five is the complement of the closed rank-&lt;=4 branch (`..._o0b_split_rankdrop_complete_exclusion/statement.md:22-27`).
- Size: `6 x 15 x 4 = 360` rows, `x 105 = 37,800` labels.

## D1.4 O0a vs O0b split: the difference table

| | `433-1b -&gt; O0a` | `433-1b -&gt; O0b` split |
|---|---|---|
| outside multigraph | `r=(0,0,2)`, `m_DE,m_DF,m_EF=(3,1,1)` (`o0a atlas statement.md:28-31`) | `r=(0,1,1)`, `m=(2,2,1)` (`o0b atlas statement.md:12-14`) |
| colored incidences | both at `F`: `B-F, C-F` (`o0a statement.md:33`) | split: `BE` and `CF` (`o0b statement.md:8-9`) |
| defect spend | loop 1 + `DE` 2+1 split = 3, `BC` forced split (`o0a proof.md:3-8`) | loop 1 + one of `BC/DE/DF` repeated = 3, four strata (`o0b proof.md:3-7`) |
| lanes | 4 orbits of size 32, `(sigma_c, sigma_o)` | 10 lanes; split = `S0` x2, `SDE` x2, `SDF` x2 |
| outside records | `de, de, -de, df, sigma_o ef, bf, sigma_c cf` | see D1.3 |
| identical record pair | yes (`de, de`) — powers `P` | only in `SDE`/`SDF` |
| `D/E` swap admissible | yes (both colored at `F`) — powers `Q` | **no** |
| `d -&gt; -d` stabilizer | no (`{de,de,-de}` is not `d`-stable) | **yes on `S0`/`SBC`** |
| common products | `(-1,b,c,bc,-bc)` | **identical** |
| role cells / sign rows | 15 / 4 | 15 / 4, same source-facet parent |
| label ledger | 105, quotient 36 | 105, quotient 57 (`S0`) or 60 (`SDE`/`SDF`) |

---

# D2 — TRANSPORT FEASIBILITY, PIECE BY PIECE

Every "transports" verdict below is either already a DAG edge, or a consequence whose only new content is a record-list comparison against the banked executable quoted in D1.3.

## C1. Common products and sums — TRANSPORTS EXACTLY, ALREADY BANKED

"The six split lanes have common products `(-1,b,c,bc,-bc)` and transport exactly to the existing split compiler" (`..._o0b_common_vieta_minor_atlas/statement.md:10-11`); "The split template is exactly the input of the proved split compiler" (`proof.md:9-10`). The same 60 compiled algebra rows serve all six O0b split lanes (`statement.md:19-24`: "180 distinct compiled algebra rows = 60 split + 120 repeated"). **Consequence the DAG does not spell out:** every per-cell O0a common-locus certificate (compact curve kernel, four-basis tower kernel, elliptic kernels, five-relation locus, quadratic four-basis) is valid verbatim as the source algebra of the O0b split block. Zero recomputation.

## C2. Product-rank-drop classifier — TRANSPORTS EXACTLY, ALREADY USED

"The split common products are identical to the certified `O0a` split compiler, so the rank-drop rational classifier transfers exactly" (`..._o0b_split_rankdrop_complete_exclusion/proof.md:3-4`), realized as the DAG edge `node.json:29`. See M4 for the scope-line seam.

## C3. Role-cell duplicate transport (`AB&lt;-&gt;AC`) — TRANSPORTS, WITH A COMPANION

In O0a the map is target `B&lt;-&gt;C` alone (`..._cells9_10_duplicate_role_transport/proof.md:3`), which works because both colored incidences are at `F`. In O0b it must be `B&lt;-&gt;C` **and** `E&lt;-&gt;F`; that composite is already PROVED for the repeated lanes (`..._o0b_common_repeat_cells3_6_full_system_transport/statement.md:6-11`: "Apply `B&lt;-&gt;C` and `E&lt;-&gt;F` ... role cell 3 maps to cell 6 ... Outside, the map exchanges `BE&lt;-&gt;CF`, `DE+&lt;-&gt;DF+`, and `DE-&lt;-&gt;DF-`, fixes `EF`, and preserves the outside-cycle sign"). Checking it on split lanes costs one line: `bc -&gt; cb = bc` and `-bc -&gt; -cb = -bc`, so `BC+` and `BC-` are fixed individually and the role permutation is exactly `(AB AC)`. On the records of D1.3 the induced permutation is `(0 1)(2 4)(3 5)`, fixing 6.

Two distinct consequences:
- **On `S0` lanes it is a self-map**, giving role-cell orbits `[0][1,2][3,6][4,7][5,8][9,10][11][12,13][14]`: 9 orbits, 15 -&gt; 9 cells.
- **On `SDE` lanes it lands on `SDF`**: applying it to `SDE`'s tuple returns `SDF`'s tuple exactly. The two `SDF` lanes are therefore entirely free.

`BC1&lt;-&gt;BC2` is **not** available on split lanes (it would need a gauge flipping the sign of `bc`, which breaks the `ab`/`ac` normalization). That is why cells 11 and 14 pair on the repeated side but stay separate here — and it is corroborated by the O0a route, which paid cell 11 and cell 14 with separate nodes and has no `cells11_14` transport.

## C4. Outside label quotient `d -&gt; -d` (105 -&gt; 57) — TRANSPORTS TO `S0`, DIES ON `SDE`/`SDF`

`S0`'s records 2,3 and 4,5 are `(d e, +)/(-d e, -)` and `(d f, +)/(-d f, -)` with squared sums `(d+e)^2/(d-e)^2` and `(d+f)^2/(d-f)^2` (modal script `:164-168, 181-188`), so `d -&gt; -d` induces exactly the banked permutation `(2 3)(4 5)` and the banked involution applies verbatim (`..._o0b_common_repeat_cell3_outside_label_quotient/proof.md:3-13`). On `SDE` it fails: `d -&gt; -d` sends `{de, de}` to `{-de, -de}`, which is not the lane's record multiset. I verified the gauge argument in general: the vertex sign gauge must fix `ab, ac` (so `a,b,c` share status), then `be` (so `e` shares it) and `cf` (so `f` shares it), leaving only the flip of `d`. Hence `S0`'s outside stabilizer is exactly `Z/2` and `SDE`/`SDF`'s is trivial.

## C5. Identical-record exchange `P` (O0a's first generator) — DIES ON `S0`, TRANSPORTS TO `SDE`/`SDF`

`P` needs two records with identical product and identical squared sum (`..._universal_generic_outside_label_orbit_quotient/proof.md:9-10`). `SDE` has exactly that at indices 2,3 and `SDF` at 4,5 (modal script `:169-178`). Census: **60 orbits, profile 1:15, 2:45**.

## C6. `D/E` transport `Q` (O0a's second generator) — FAILS, CERTIFICATE-LEVEL

`Q` is `(d,e,f) -&gt; (sigma_o e, sigma_o d, f)`, and its proof requires the `bf` and `sigma_c cf` rows to be fixed (`..._universal_xi4_xi3_outside_role_transport/proof.md:17-18`: "The `bf` and `sigma_c cf` rows are fixed"). That is available only because O0a puts both colored incidences on `F`. In O0b the colored edges are `BE` and `CF`, so `d &lt;-&gt; e` maps `be -&gt; bd`, which is not an edge of the outside graph at all. **No repair exists**: any sign gauge fixing `ab, ac` forces `e` and `f` to share status with `b, c`, and no vertex relabeling other than `(B&lt;-&gt;C, E&lt;-&gt;F)` preserves the O0b outside multigraph. This is the precise, structural reason the O0b quotient tops out at 57/60 instead of 36.

## C7. Signed-pair guard factorization — NOT USED, AND I DO NOT CHALLENGE THE FENCE

The `433-1a` signed-pair guard-factorization family (`..._433_1a_cell3/9/11/12/14_signed_pair_guard_factorization_exclusion`; e.g. `cell11`'s 42,316-term resultant reduction, `statement.md:16-49`) runs on the **1a -&gt; 1b axis**, i.e. a *different source*. My transports all run on the **1b/O0a -&gt; 1b/O0b axis**, i.e. same source, different target, and use no guard factorization anywhere.

Fence datum, taken as hard and quoted in full:

&gt; "Upstream PR #1155 supplies a useful route fence: in one source chart the `433-1a` signed-pair guard factorization does not transplant, and an exact guarded necessary signed-pair point survives. That point is not a full outside witness, but it proves that a guard-only closure is unavailable and that the residual quadratic cover must be counted or routed to an owner." — `notes/work_cycles/roadmap_r3/17-positive-433-repeat-bc-20260810.md:306-311`

**Verdict: fully consistent, no refutation attempted.** I propose no guard-only closure; the residual quadratic cover is counted (11,304 representative systems) and routed to owners. Nothing I found weakens the fence, and I found nothing that bears on it either way — see the zero-power declaration Z1.

## C8. Per-label O0a exclusion algebra — DOES NOT TRANSPORT

The O0a per-label families (`parallel_de`, `xi3_xi4`, `reciprocal_square`, `quadratic_resultant`, `common_f_resultant`) are stated over the O0a residual record set. Even where the *quotient* transports (C5), the *residual five records* differ: O0a's complement of the identical pair is `{-de, df, sigma_o ef, bf, sigma_c cf}`, `SDE`'s is `{be, cf, df, -df, sigma_o ef}`. The outside elimination must be rebuilt. This is the sense in which cycle-17's "The outside graph is not transported; it is rebuilt" (`:124-125`) is right — but it is right only about the elimination, not about the label combinatorics.

## C9. Summary of the split-lane transport verdicts

| lane (count) | `d-&gt;-d` 105-&gt;57 | identical-pair 105-&gt;60 | `B&lt;-&gt;C,E&lt;-&gt;F` | net |
|---|---|---|---|---|
| `S0` (2) | **yes** (C4) | no | self-map, 15 -&gt; 9 cells | 4,104 reps for 12,600 labels |
| `SDE` (2) | no | **yes** (C5) | maps to `SDF` | 7,200 reps for 12,600 labels |
| `SDF` (2) | no | yes (unused) | image of `SDE` | 0 reps for 12,600 labels |

---

# D3 — THE DRAFT CODEX BRIEF

The shippable draft is on disk at `notes/pilots_20260810/k3_splitbc_transport/DRAFT_CODEX_BRIEF.md` (this pilot's directory; **not** shipped to `notes/codex_briefs/` — coordinator's call). Its exact ledger, repeated here so this report stands alone:

```text
piece                       raw labels   representative systems   quotient used
SDF lanes (2)                   12,600            0               lane transport from SDE
SDE lanes (2)                   12,600        7,200               identical-pair, 120 rows x 60
S0 lanes, rho-paired cells      10,080        2,736               role transport + d-&gt;-d, 2 x 6 x 4 x 57
S0 lanes, rho-fixed {0,11,14}    2,520        1,368               d-&gt;-d only, 2 x 3 x 4 x 57
total                           37,800       11,304               factor 3.34
```

Optional extra on the three `rho`-fixed `S0` cells: the two involutions commute there and generate a Klein four-group on labels with **32 orbits (1:3, 2:7, 4:22)**, which would take the last line from 1,368 to at best 768 (total 10,704) once the induced source-root-sign action is printed.

Conditional on the missing 433-1b root-sign quotient of M6 (4 rows -&gt; 1 in cells 3..14, 4 -&gt; 2 in cells 0,1,2):

```text
SDE lanes:  2 x 18 rows x 60 = 2,160
S0 paired:  2 x  7 rows x 57 =   798
S0 fixed:   2 x  4 rows x 57 =   456
total                          3,414        factor 11.1 vs raw
```

Certificates the brief asks for, in dependency order: `S0` label quotient (reuse of an existing PROVED node, widened scope, with the falsifiable prediction that its orbit-ledger digest must equal the banked `70c074ad...`); `SDE`/`SDF` identical-record quotient; `SDE -&gt; SDF` lane transport; `S0` role transport; and, optionally and separately, the 433-1b root-sign quotient.

**Sizing caveat that must survive into any brief.** 11,304 is a *count* match to the 10,080-system split rank-drop run that completed cleanly (`..._o0b_split_rankdrop_complete_exclusion/statement.md:16-25`), but that run was over **zero-dimensional deployed points**, whereas the rank-five block sits over positive-dimensional common curves. The monolithic all-variable outside ideal is already fenced: "one pilot label for each `BC` sign hit a 300-second Modal cap" (`notes/work_cycles/roadmap_r3/17-positive-433-repeat-bc-20260810.md:205-206`, run `ap-532TAx5h3Qaw22D3ueMOVZ` at `:216`). The brief therefore prescribes the function-field generic-rank atlas plus finite-boundary replay shape, not a per-system census.

---

# Blind-prior scoring (PREREG registrations vs outcome)

| prior | registered | outcome |
|---|---|---|
| R1 common side 90-100% transportable | yes | **CORRECT and understated** — it is 100%, and stronger than predicted: the same 60 compiled algebra rows, not merely "the same geometry" |
| R1 outside side: 0% of labels closed by pure transport | yes | **CORRECT** — no O0a outside emptiness certificate closes an O0b split label |
| R1 quotient factor, point prediction 4x | yes | **CLOSE, slightly high**: certified factor is **3.34** (10,704 at best without new certificates); 11.1 only with the missing root-sign quotient |
| R2 primary: guard-factorization/target-guard failure | yes | **WRONG as the operative mechanism.** The operative failure is structural and cheaper to state: the colored incidences move from `{F,F}` to `{E,F}`, killing the `D/E` transport (C6). Guard factorization never enters my axis at all |
| R2 secondary: some O0a component transports vacuously | yes | **PARTLY CORRECT**: `P` transports vacuously to `S0` (no identical record pair there), exactly the "must not be scored as a success" case I pre-registered |
| R2 tertiary: sign-convention seam | yes | **CORRECT in a mild form**: the `B&lt;-&gt;C` map changes the `BC-` *sum* sign, so the source-root-sign row must be flipped to compensate (`cells9_10_duplicate_role_transport/proof.md:3`) |
| R3 `37,800 = 360 x 105` and uniform 105 | yes | **CORRECT** (`..._residual_owner_partition/proof.md:20-23`), with the M7 refinement that the ledger *object* is not uniform |
| R3 residue 9,000-10,000 raw labels | yes | **WRONG unit, roughly right magnitude**: the right unit is representative systems, and the answer is 11,304 (10^4, at the top of my band) |
| R3 representative systems 1,000-3,000 | yes | **TOO LOW by ~4x** without the root-sign quotient; inside the band (3,414) only with it |
| R3 not a monolithic census; function-field atlas | yes | **CORRECT**, and independently fenced by the 300s cap |
| R4.1-R4.5 pre-registered misses | yes | answered in M9; R4.2 and R4.5 produced real content, R4.1/R4.3/R4.4 cleared |

---

# Zero-power declarations

- **Z1 — the PR #1155 fence itself.** `grep -rn "1155" --include=*.md --include=*.json background/ critical/ notes/` returns **no prose hit**; every hit is a digit substring inside numeric arrays in unrelated `e1_*` result JSONs. In this repo the fence exists **only** as the cycle-17 prose at `:306-311`. I have no network and the Codex worktree is quarantined, so I have **zero power** to audit the fence's certificate. I take it as a hard datum, as instructed, and my plan is designed to be indifferent to it.
- **Z2 — novelty of the four transports.** Searches run: `ls background/nodes | grep "o0b" | grep -E "quotient|transport"` (two hits, both repeated-BC: the cell-3 label quotient and the cells-3/6 full system transport); `ls background/nodes | grep -E "433_1b.*split"` (one hit, the rank-drop exclusion); `grep -rn "S0" --include=*.md background/nodes/` (every hit is the unrelated `negative one-loop 442` lane family, not `433-1b/O0b`); `grep -rln "split-BC\|split BC" notes/` (only the roadmap, cycle-14/16/17, and this pilot dir). **Conclusion, correctly scoped:** no node in *this repo* states any of T1-T4 for the O0b split lanes. This has **no power** to establish that no such certificate exists upstream on GitHub or in the Codex worktree, both of which are unreachable to me. Note also that T1 and T3 are *not* novel mathematics — they are existing PROVED O0b nodes whose statements exclude the split lanes by wording only (M3, C3).
- **Z3 — the 433-1b root-sign quotient (M6).** `ls background/nodes | grep -i root_sign` returns three ids, all `433-1a`. Scoped claim: **no such node is banked in `background/nodes` or `critical/nodes` of this repo.** I did not and cannot check upstream. I also did **not** verify the port; I verified only that 433-1b's cell 0/1/2 vs 3..14 loop-role split matches the 1a hypothesis, and I flagged the cell-0/1/2 gap explicitly.
- **Z4 — the sign-row action of the role transport on the three fixed `S0` cells.** Not determined. I deliberately did not run it (it would be a computation over the common rows, outside an audit's remit). Every headline number therefore uses the **safe** 57-per-row count, and the Klein-four improvement is quoted only as an upper-bound-on-savings.
- **Z5 — result-shard contents.** I read only lines 155-199 of the split rank-drop modal script and no result shard bodies. I have **zero power** over any claim about what the 92,558-line raw result contains beyond what the node statements assert.

---

# Compliance

**Interpreter invocations: 1.** Exactly one, and it went through the guard: `tools/ramguard tiny -- python3 notes/pilots_20260810/k3_splitbc_transport/label_orbits.py`, run from the repo root with the literal `--`, stdlib only (`itertools`), no network, no Modal, no git. It computes nothing about the algebra: it counts orbits of record permutations on the 105 `(missing-record, matching)` labels. Two of its five cases are **validations** that reproduce banked DAG numbers exactly — 57 orbits with profile `1:9, 2:48` (matching `..._o0b_common_repeat_cell3_outside_label_quotient/statement.md:23-26`) and 36 orbits with profile `1:3, 2:15, 4:18` (matching `..._433_1b_universal_generic_outside_label_orbit_quotient/statement.md:12-16`) — which is what licenses the three new counts (60, 56, 32). No other command in this session invoked an interpreter; everything else was `ls`, `grep`, and file reads. No bare `python3` was ever run.

**Quarantine.** I did not open `notes/pilots_20260802/CAMPAIGN_LEDGER.md` at any line, and excluded it explicitly from the one `grep` that could have reached it. I did not read `notes/pilots_20260810/k3_orientation_assembly`, `k3_allocation_inequality`, or `k3_chain_seams`; one `grep -l` printed the path `notes/pilots_20260810/k3_allocation_inequality/compute_arith.py` as a filename only, and I did not open it or any other sibling file. I touched no path containing `prize-codex-`. I never opened `dag.json`; all DAG facts come from `node.json` shards, node markdown, and `ls`/`grep` over `background/nodes`. I read exactly one range of one large experiment file (lines 155-199) and no result-JSON bodies.

**Write scope.** Everything I wrote is inside `notes/pilots_20260810/k3_splitbc_transport/`: the `## Pilot registrations` block appended to my own `PREREG.md` (before any read beyond the two named anchors), `label_orbits.py`, and `DRAFT_CODEX_BRIEF.md`. `REPORT.md` was attempted in the same directory and refused by the harness's report-file rule, so it is delivered as this return text instead. No `dag/`, `nodes/`, `critical/`, `background/`, `experiments/`, or `tools/` file was created or modified. No git operation of any kind. No census and no elimination computation was run — the only arithmetic performed is the label orbit count described above, and no surgery was applied anywhere: everything in D3 is a draft awaiting the coordinator.
