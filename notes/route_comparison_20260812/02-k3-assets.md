# K3 route inventory — banked assets and conditional structure

All paths below are under `/home/u2470931/smooth-read-solomin/prize/` (abbreviated `PRIZE`); node files under `background/nodes/`, cycles under `notes/work_cycles/roadmap_r3/`.

## 1. What would flow if SEM-QBC + Rec_2_4 existed, and through which nodes

The single choke point is `rate_half_kb_active_balanced_core_component_bridge` (CONDITIONAL). Its node.json statement conditions on exactly the two missing pieces: "a concrete source-bound compiler for the active balanced-core certificate and a same-record realization of each compiled witness as an actual Q=6,s=6,u=2 endpoint component" — i.e., every Z_BC slope assigned once, same received line, to component type (2,4,2) or (2,8,1) (SOURCE-STATED). Cycle 19 discharged the compiler half: the `bcCertified` predicate is now instantiated by the active shifted-lattice certificate (K=1048577, omega=981104, w=67471, d1>=w+1), lexicographic minimization giving unit fibers (`19-active-bc-semantic-gap-20260810.md:41-49`); the remaining target is the same-record Q6 endpoint realization (`:50-52`). Per the independent-review addendum, upstream #1159 isolates SEM-QBC as the first missing bridge *before* Rec_2_4 (`rate_half_kb_m2_r4_k3_independent_review/statement.md:34-37`) — so both are needed, in that order (SOURCE-STATED).

With the bridge live, the conditional chain fires in this order (all `gate: all`, from each node.json `requires`):

1. **`rate_half_kb_m2_r4_coordinate_positive_complete_payment`** (CONDITIONAL) — requires the bridge + the eleven-route payment; outputs U_positive = U_remaining. It consumes the banked zeros: 433-1a→O0b proved empty and 433-1b→O0a proved empty at raw-system level (its node.json statement).
2. **`rate_half_kb_m2_r4_k3_orientation_assembly`** (CONDITIONAL) — requires bridge + positive + source-line + source-cover + trivial-stabilizer payments; outputs U_geometry = U_source_line + U_source_cover + U_trivial, negative branch proved empty (`statement.md:6-28`); explicitly "No slope-to-component or multiplicity assertion is inferred merely from the component-level trichotomy" (`conditional.md:20-22`).
3. **`rate_half_kb_m2_r4_k3_allocation_inequality`** (CONDITIONAL) — requires positive payment + orientation assembly + `rate_half_kb_v4_balanced_core_allocation_definition`; prints U_positive, U_geometry, U_K3 = U_positive + U_geometry, U_K3_allocation and proves U_K3 <= U_K3_allocation by exact integer arithmetic (`statement.md:7-22`).
4. **`rate_half_kb_m2_r4_k3_distinct_slope_budget_ledger`** (CONDITIONAL) — the terminal ledger: U_K3 = U_positive + U_geometry within allocation, with the proved saturated c2(1,1,2), c2(2,0,2) and negative-coordinate exclusions contributing zero (node.json:8).

Banked raw assets that convert into these payments: the 433-1b→O0a raw workboard PROVED empty — 15 role cells, 9 disjoint owner blocks `[0]|[1,2]|[3,6]|[4,7]|[5,8]|[9,10]|[11]|[12,13]|[14]`, 1,575 labels, 25,200 signed systems, plus the global product-rank-drop branch (`..._433_1b_raw_workboard_complete_exclusion/statement.md:1-20`); cell5 and cell11 complete 105/105-label exclusions as its cell owners (both `statement.md`); the c2(1,1,2) saturated packet as one proved zero subcase (`18-...md:43-44`). Each raw node self-limits: "does not identify raw labels with distinct affine slopes... does not prove exhaustive balanced-core routing, genuine-pencil hypotheses, exact line multiplicities, independent review, K3, or a Prize result" (raw workboard `statement.md:18-20`) — the bridge + chain is precisely what converts them (MY-INFERENCE from the requires-wiring).

## 2. What remains conditional EVEN WITH the bridge

Five TARGET leaves sit inside the chain (statuses from node.json):

- **Eleven-route payment** (`rate_half_kb_m2_r4_coordinate_positive_remaining_route_payment`, TARGET): 442-0a→O0b/O1b/O1d, 442-1b→O0a/O0b, 433-0→O0a/O0b/O1b/O1c/O1d, 433-1b→O0b, outputting U_remaining. Cycle 17 banked strict partial evidence on 433-1b→O0b — repeated-BC cells 3/6 closed for both signs (840 systems x 4), split-BC product-rank-drop closed (10,080 cases empty) — leaving an exact residual of 408 common rows / 42,840 labels in three blocks (`17-...md:92-116, 155-169`), explicitly "does not promote that critical node" (`17-...md:100-102`).
- **Source-line payment** (TARGET): rows (1,0,4), (0,1,4), near-aligned (0,0,6), and the exceptional unsaturated (1,1,2) orbit KBDM-10 (`18-...md:40-44`; node.json).
- **Source-cover payment** (TARGET): new workboard over both proved V4 passports.
- **Trivial-stabilizer (2,8,1) payment** (TARGET): U_trivial.
- **Allocation definition** (`rate_half_kb_v4_balanced_core_allocation_definition`, TARGET): must prove exact U_Q and U_new sibling bounds, or an equivalent certified three-way allocation, then define U_K3_allocation by exact subtraction from B* = 274980728111395087 after U_paid = 981104. The integer 274980728110413983 = B* − 981104 "is jointly owned by U_Q, U_BC, and U_new; it is not U_K3_allocation" (`18-...md:46-53`; allocation node `statement.md:21-22` allows it only "unless the sibling U_Q and U_new cells are proved zero"). The derived joint floor **U_Q + U_BC + U_new >= 57197049262** "remains conditional on the recorded owner ruling and does not isolate U_BC" (`18-...md:54-55`, SOURCE-STATED). Why it cannot isolate U_BC (MY-INFERENCE): it is a *lower* bound on a three-cell *sum*, while the allocation inequality needs a per-cell *upper* allowance for U_BC; without exact sibling atoms, any split of the joint reserve among the three cells is consistent with the floor.
- **Independent review** (TARGET): a reviewer outside every producing implementation replaying the whole load-bearing sub-DAG (`independent_review/statement.md:1-15`).

## 3. External replay status

Two outside replays exist (scottdhughes on upstream rs-mca), both matching our verdicts exactly, both PARTIAL:

- **PR #1153** (2026-08-09): the six residual xi=3 cell-5 pairing representatives, exact over F_2130706433, zero terminal solutions/witnesses, public-DAG pin `28b3bc8a`; its RED verdict was provenance-only (fetch-window pin `3fa2987`), resolved 2026-08-10, no mathematical objection (`cell5_complete_exclusion/source_evidence.md:5-19`).
- **PR #1157** (2026-08-10): full raw 433-1b→O0a exclusion — 15 cells, 1,575 labels, 25,200 systems, zero survivors — at pin `8df0903391a2`, also reconstructing the thirteen-route table with the two raw-empty routes at `distinct_affine_slope_payment = null` (`raw_workboard.../source_evidence.md:9-19`).
- **Cell 11 has NO external replay addendum** (`cell11_complete_exclusion/source_evidence.md` is internal-only); upstream #1154's "yellow compact tower" for cell 11 is weaker and non-conflicting (`16-...md:41-45`).
- The review node stays TARGET: the replays "do not cover the complete load-bearing K3 sub-DAG" and accumulate only as evidence (`independent_review/statement.md:39-41`).

## 4. The two unsound shortcuts cycle 18 removed

(`18-k3-bridge-and-allocation-refactor-20260810.md:57-61`, SOURCE-STATED)

1. **Component classification treated as a slope bridge.** The proved order-two trichotomy (coordinate / diagonal source-line / biquadratic source-cover, plus separate (2,8,1)) "has no slope-domain conclusion" (`:19-22`). Forbidden: inferring any active-slope ownership, exhaustiveness, or multiplicity from component-level algebra alone — the bridge must supply the slope-to-component assignment (codified in orientation `conditional.md:20-22` and the cycle-19 independence audit: 256 Boolean assignments all satisfy the partition algebra while 31 have nonempty Z_BC with empty endpoint set, `19-...md:18-26`).
2. **The joint reserve treated as a K3-only budget.** 274980728110413983 was a false U_K3_allocation placeholder. Forbidden: running the K3 allocation comparison against the joint reserve, or any allocation "imported from a different row, cell, or partition" (allocation node.json:8), until the sibling U_Q/U_new atoms or a certified three-way allocation exist.

Net effect: even a proved SEM-QBC + Rec_2_4 bridge yields the K3 ledger only after four payment TARGETs plus the allocation-definition TARGET close; the banked 25,200-system, cell-5/11, and cells-3/6+split-rank-drop closures then convert with zero re-derivation.