REPORT — k3_allocation_inequality (round 30, 2026-08-10)

**Note on the artifact:** the harness blocked `Write` on `REPORT.md` (report/summary `.md` files must be returned as text, not written). The three working artifacts are on disk in `notes/pilots_20260810/k3_allocation_inequality/` — `PREREG.md` (with my appended blind priors), `compute_arith.py`, `verify_partition_digest.py`, `binding_schema_draft.json`. The full REPORT.md text follows verbatim; materialize it to that directory if you want it on disk.

---

# REPORT — k3_allocation_inequality (round 30, 2026-08-10)

**VERDICT: the dry run is BLOCKED, and not by one missing certificate but by three. Three of the four demanded integers cannot be printed today, and the fourth — `U_K3_allocation` — is not defined anywhere in this repository. The only honest output is an interval for the allocation, a `BLOCKED` state for both summands, and a wiring repair that must land before any future run can even be checked.**

Nothing in this report changes a node, an edge, or a status. Everything below is audit output plus two scratch scripts in this directory.

---

## MISSES FIRST

**M1 — `U_K3_allocation` IS NOT DEFINED ANYWHERE. There is no ledger row, no subtraction-table row, no manifest field, and no note that fixes it.**
The token `U_K3_allocation` occurs in exactly four files outside `dag.json`, and all four are inside the two K3 node directories that *demand* it: `critical/nodes/rate_half_kb_m2_r4_k3_allocation_inequality/node.json:7`, `.../k3_allocation_inequality/statement.md:12`, `critical/nodes/rate_half_kb_m2_r4_k3_distinct_slope_budget_ledger/statement.md:7`, `.../k3_distinct_slope_budget_ledger/conditional.md:15`.
The node's attack says "Recover the active K3 allocation directly from the pinned row manifest" (`critical/nodes/rate_half_kb_m2_r4_k3_allocation_inequality/attack.md:3`), but the pinned row manifest does not contain one. The atom that pins the row states the opposite in terms: "No value is proved here for `U_Q`, `U_BC`, or `U_new`." (`background/nodes/rate_half_kb_v4_tangent_source_atom/statement.md:69`).
My blind prior P1a (60%, allocation lives in a subtraction-table note) and P1b (25%, machine-readable manifest field) are both WRONG; P1c (15%, not pinned at all) is the outcome. See the power declaration Z1.

**M2 — THE ALLOCATION NODE HAS NO INCOMING EDGES, SO THE BINDING IT DEMANDS IS NOT REPRESENTABLE.** Its statement demands that each input be bound "to its proof certificate and manifest digest" (`critical/nodes/rate_half_kb_m2_r4_k3_allocation_inequality/node.json:7`) and its falsifier fires if "a digest or row differs" (`.../node.json:8`). But `.../node.json:14` is `"requires": []` and `.../node.json:16` is `"evidence_for": []`, and a shard-wide grep shows the only other file naming this node is the ledger that consumes it. In particular the node that actually pins the row, the partition digest, `B*`, `U_paid` and the reserve — `rate_half_kb_v4_tangent_source_atom` — has `"to": "rate_half_band_closure"` as its sole evidence edge (`background/nodes/rate_half_kb_v4_tangent_source_atom/node.json:28-31`). The manifest and the node that must cite it are not connected.

**M3 — THE UNIT SEAM IS THE REAL BLOCKER, AND IT IS UNPRICED.** The node's unit is "distinct affine slopes under the active first-match owner" (`critical/nodes/rate_half_kb_m2_r4_k3_allocation_inequality/statement.md:4`); the manifest's unit token is `DISTINCT_BAD_FINITE_SLOPES_PER_RECEIVED_LINE` (`background/nodes/rate_half_kb_v4_tangent_source_atom/partition_contract.json:69`). Every banked `m2 r4` workboard result is denominated in something else — raw labels, raw atlas cases, principal systems — and the producers say so explicitly and repeatedly:
- "This theorem does not identify raw labels with distinct affine slopes." (`background/nodes/rate_half_kb_m2_r4_coordinate_positive_433_1b_raw_workboard_complete_exclusion/statement.md:18`)
- "This is a raw-system theorem; it is not a distinct-affine-slope payment." (`notes/work_cycles/roadmap_r3/16-k3-aggregate-20260810.md:18-19`)
- "Does not cover cell 14 or convert raw systems into distinct affine slopes. / Books no K3 allocation or Prize endpoint." (`background/nodes/rate_half_kb_m2_r4_coordinate_positive_433_1b_o0b_common_repeat_cell11_uncolored_deployed_off_guard_pair_exclusion/claim_contract.md:10-11`)
- "Books no label, distinct slope, K3 allocation, or Prize endpoint." (`background/nodes/rate_half_kb_m2_r4_coordinate_positive_433_1b_o0b_common_repeat_cell11_uncolored_generic_rank_atlas/claim_contract.md:8`)
- listed as a live frontier item: "conversion from surviving raw systems to distinct affine slopes and K3 allocation" (`.../cell11_uncolored_deployed_off_guard_pair_exclusion/frontier.md:9-10`)

The falsifier's "omitted line multiplicity" clause bites exactly here: nothing banked states how many distinct affine slopes one surviving raw label contributes. This is recorded in-node already; I am confirming it, not discovering it (see the novelty subtraction).

**M4 — `U_positive` IS BLOCKED, AND IT IS BLOCKED HARDER THAN "one open node".** `U_positive = U_remaining` (`critical/nodes/rate_half_kb_m2_r4_coordinate_positive_complete_payment/node.json:8`), and `U_remaining` is the output of `rate_half_kb_m2_r4_coordinate_positive_remaining_route_payment`, whose status is `"TARGET"` (`.../remaining_route_payment/node.json:6`). That node owes a printed integer on **eleven** routes (`.../remaining_route_payment/node.json:7`, replayed exactly below), and **zero** of the eleven has a printed integer anywhere in the repo. My prior P2a put 55% on printing an exact `U_positive`; that was wrong.

**M5 — `U_sourcecover` IS BLOCKED ON THE OPEN ORIENTATION TARGET, exactly as the brief anticipated.** `rate_half_kb_m2_r4_k3_orientation_assembly` has status `"TARGET"` (`.../k3_orientation_assembly/node.json:6`) and is the sole producer of the disjoint sum (`.../k3_orientation_assembly/statement.md:14`). It cannot be bounded either: no cap on the source-cover terminal count is banked, and the node's own text requires each image to be "eliminated, paid ... or carried bijectively to a closed image" (`.../statement.md:12-13`) before any total exists. Prior P2b (20%, fully computable) is refuted.

**M6 — THE ROW KEY IS AMBIGUOUS IN THE ONLY BANKED ROW MANIFEST, AND THE FALSIFIER'S IMPORTED-ALLOCATION CLAUSE IS LIVE.** In `background/nodes/deployed_identity_prefix_owner_scope_audit/deployed_rows.json` the four deployed rows share `n` and `k` (lines 14-15, 33-34, 52-53, 71-72), and `kb_mca` and `kb_list` additionally share `p`, `extension_degree` and `B_star = 274980728111395087` (lines 17-23 vs 36-42). Verified by exact enumeration in section F of `compute_arith.py`: `B_star` alone matches 2 rows, `(n,k)` matches 4, `(n,k,p)` matches 2, and `(n,k,p,K)` matches exactly 1. **Any future binding that identifies the active row by its budget will pick up `kb_list` silently.** No prior repo note records this hazard (novelty subtraction below).

**M7 — "ALLOCATION" IS A HOMONYM INSIDE THIS VERY LANE.** In the `c2(1,1,2)` sub-campaign, `allocation` denotes a residual assignment axis with values `same/swap/mixed = R20/R02/R11` (`critical/nodes/rate_half_band_closure/notes/k3_contributor_review_20260730.md:164-165`), and it is a literal CLI argument of the banked probes (`critical/nodes/rate_half_band_closure/notes/kb_c2_112_aligned_positive_ramified_saturation.py:203`, `.../kb_c2_112_near_moving_template_probe.py:96`). A verifier that greps for "allocation" in this lane will hit dozens of unrelated matches before it hits the budget. This is a naming trap for the eventual checker, not a mathematical error.

**M8 — THE LEDGER'S "record `U_K3=0`" FALLBACK IS NOT FREELY AVAILABLE.** `critical/nodes/rate_half_kb_m2_r4_k3_distinct_slope_budget_ledger/attack.md:10-11` says "If all residual terms are eliminated, record `U_K3=0`". But the banked lower attack at the active row forces the three unpaid cells to carry at least `57197049262` between them (derivation and exact arithmetic in D2/E below). `U_K3 = 0` therefore requires proving that the entire floor falls on `U_Q` and `U_new` — and the routing of that attack family into the Grande-Finale-v4 cells is explicitly *not proved*: "A bridge from the upstream legacy first-match stack to Grande Finale v4." (`background/nodes/deployed_identity_prefix_owner_scope_audit/claim_contract.md:18`, under the "Not proved" heading at line 13).

**M9 — A SECOND IMPORT TRAP IS PRE-ARMED IN THE SAME PARAGRAPH AS `U_paid`.** "The legacy value `U_paid=422354730332` is not imported." (`background/nodes/rate_half_kb_v4_tangent_source_atom/statement.md:69-70`). Any allocation computed as `B* - 422354730332` would look plausible and be wrong.

**M10 — CAUTION, NOT A MISS: the "source-line contributes zero" leg is scoped to SATURATED packets.** The ledger asserts "The proved `c2(1,1,2)` source-line and negative-coordinate exclusions contribute zero as evidence" (`critical/nodes/rate_half_kb_m2_r4_k3_distinct_slope_budget_ledger/node.json:8`), but the source-line certificate's claim row reads "No admissible **saturated** diagonal `c2(1,1,2)` packet in the source-line branch exists" (`background/nodes/rate_half_kb_m2_r4_diagonal_c2_112_source_line_complete_exclusion/claim_contract.md:5`), whereas the orientation node promises only that "the source-line image is exactly the declared `c2(1,1,2)` source-line workboard" (`critical/nodes/rate_half_kb_m2_r4_k3_orientation_assembly/node.json:7`). The word "saturated" has to be carried across that identification or the zero is not yet earned. The negative leg has no such gap: "No negative-parity coordinate-order-two packet exists over the deployed KoalaBear field." (`background/nodes/rate_half_kb_m2_r4_coordinate_negative_complete_exclusion/statement.md:16-17`).

**M11 — ALREADY-FLAGGED, RESTATED SO IT IS NOT LOST: the K3 arm is an `n=2^21` object.** "The workboard rows are `n = 2^21` extension rows; transport to the `n = 2^41` prime razor rows is NOTE-LEVEL (the WP5 quantifier mismatch stands)." (`critical/nodes/rate_half_band_structural_surplus/statement.md:35-37`). Whatever `U_K3_allocation` eventually is, it is a budget at the deployed `n=2^21` KoalaBear row and carries no razor-row content.

---

## D1 — THE PROVENANCE MAP

### D1.0 What K3 is, in this partition

The K3 arm is the **balanced-core cell** of the frozen first-match partition. The orientation node quantifies over "every unpaid same-owner balanced-core bad-slope witness in the active KoalaBear `m2 r4` first-match residual" (`critical/nodes/rate_half_kb_m2_r4_k3_orientation_assembly/node.json:7`); the roadmap names the object "the unpaid K3 balanced-core/residual-geometry obligation" (`notes/PRIZE_RESOLUTION_ROADMAP.md:5445`). In the manifest that is the third chronology stage: `atom_id = "U_BC"`, `owner_id = "ACTIVE_V4_BALANCED_CORE"`, `paid = false`, `priority = 2` (`background/nodes/rate_half_kb_v4_tangent_source_atom/partition_contract.json:37-44`). So **K3 = `U_BC`**, and `U_K3_allocation` is an allocation to `U_BC` inside a four-cell first-match ledger.

### D1.1 The pinned row manifest and the partition manifest

| object | file:line | value |
|---|---|---|
| active row record | `background/nodes/deployed_identity_prefix_owner_scope_audit/deployed_rows.json:9-27` | `row_id=kb_mca`, `object=MCA`, `n=2097152`, `k=1048576`, `K=1048577`, `p=2130706433`, `extension_degree=6`, `security_bits=128`, `a0=1116047`, `a_plus=1116048`, `w=67471`, `B_star=274980728111395087` |
| row manifest digest | computed, `compute_arith.py` §F | `bdef9068a68dccaae0240eb87b0edce6c068497377cb65273d4f8548d36b85d1` |
| canonical `kb_mca` record digest | computed, `compute_arith.py` §F | `8f8c8965ee812457594b3ea36994306041645d805bff7452d6a1a3cfaeb38015` |
| partition manifest | `background/nodes/rate_half_kb_v4_tangent_source_atom/partition_contract.json` | architecture `GRANDE_FINALE_V4_KB_MCA_TANGENT_SOURCE_ADAPTER_V1` (line 2) |
| partition digest | `partition_contract.json:64` | `4fade91abc408264989babcff6f8f9bbd80bcec52545a5db15ac376bf17d88fc` |
| digest method | `partition_contract.json:63` | `SHA256_CANONICAL_JSON_WITHOUT_PARTITION_SHA256_AND_METHOD` |
| unit | `partition_contract.json:69` | `DISTINCT_BAD_FINITE_SLOPES_PER_RECEIVED_LINE` |
| quantifier | `partition_contract.json:65` | `UNIFORM_OVER_ALL_ADMISSIBLE_RECEIVED_LINES` |
| atom order | `partition_contract.json:3-8` | `U_paid, U_Q, U_BC, U_new` |
| unresolved cells | `partition_contract.json:70-74` | `ACTIVE_V4_BOUNDARY_PREFIX_Q`, `ACTIVE_V4_BALANCED_CORE`, `UNPAID_V4_COMPLEMENT` |
| partition manifest file digest | computed, `verify_partition_digest.py` | `1f64cf0474911faf7a33ec0c628bf1a65a472857be145f368804e6674d9b5343` |

I recomputed the partition digest from the manifest body with the declared method and it matches the manifest field and the value pinned in the atom's statement (`.../rate_half_kb_v4_tangent_source_atom/statement.md:10`): `claimed == recomputed == pinned == 4fade91a...d88fc` (script output, MATCH `True`). **Exactly one `partition_contract*.json` exists in the whole repo** and exactly one `partition_sha256` value occurs anywhere, so a *local* competing partition is not the import risk; the upstream legacy stack (M8, M9) is.

### D1.2 Which closed workboards feed `U_positive`

`U_positive = U_remaining`, with the two closed routes contributing zero (`critical/nodes/rate_half_kb_m2_r4_coordinate_positive_complete_payment/node.json:8`). The complete positive route table is `(KBPRW-4)` at `background/nodes/rate_half_kb_m2_r4_coordinate_positive_residual_loop_workboard/statement.md:56-62`; I re-derived all thirteen routes from the printed defect and loop-cap rules and they reproduce the table exactly (D2 below).

| route | status | feeding certificate | contribution to `U_positive` |
|---|---|---|---|
| `433-1a -&gt; O0b` | CLOSED, empty | `background/nodes/rate_half_kb_m2_r4_coordinate_positive_433_1a_o0b_complete_route_exclusion/statement.md:37` "The positive residual route `433-1a -&gt; O0b` is empty." | 0 |
| `433-1b -&gt; O0a` | CLOSED, empty | `background/nodes/rate_half_kb_m2_r4_coordinate_positive_433_1b_raw_workboard_complete_exclusion/statement.md:3,14-16` | 0 |
| the other **eleven** | OPEN | none | **unknown** |

Both closure certificates are `evidence_for` the positive composition node (shard read): `433_1a_o0b_complete_route_exclusion -&gt; rate_half_kb_m2_r4_coordinate_positive_complete_payment`, and `433_1b_raw_workboard_complete_exclusion -&gt; {rate_half_band_structural_surplus, rate_half_kb_m2_r4_coordinate_positive_complete_payment}`. That wiring is correct. What is missing is any producer for the eleven.

The best-developed open route is `433-1b -&gt; O0b`. Its exact residual ownership is banked: three disjoint blocks, `408` common rows, `42,840` raw outside labels (`background/nodes/rate_half_kb_m2_r4_coordinate_positive_433_1b_o0b_residual_owner_partition/statement.md:8-14`), and the node states its own limit: "This is an ownership theorem only. It does not assert that any of the 42,840 labels has a point or that the route is empty." (`.../433_1b_o0b_residual_owner_partition/statement.md:21-22`). Today's work cycle closed the repeated-BC cells 3/6 block for both `BC` signs and states its own scope: "This is strict evidence for `rate_half_kb_m2_r4_coordinate_positive_remaining_route_payment`; it does not promote that critical node" (`notes/work_cycles/roadmap_r3/17-positive-433-repeat-bc-20260810.md:99-102`). For the other ten routes there is **no label census at all**: the workboard statement warns "The table pairs common and outside orbit representatives; it is not a count of fully labeled packets." (`background/nodes/rate_half_kb_m2_r4_coordinate_positive_residual_loop_workboard/statement.md:65-67`).

### D1.3 Is `U_sourcecover` gated on the open orientation TARGET?

**Yes, and it cannot be bounded instead.** Status `"TARGET"` at `critical/nodes/rate_half_kb_m2_r4_k3_orientation_assembly/node.json:6`; sole producer of the sum at `.../node.json:7` and `.../statement.md:14`; `requires` is empty at `.../node.json:15`, i.e. nothing supplies it either. I searched for any banked cap on source-cover terminals and found none — see the zero-power declaration Z2. The brief's instruction "if so, say so and bound it instead" cannot be honoured: an honest bound needs either a terminal census or a per-line cap, and neither exists. Reporting `BLOCKED` is the correct output.

### D1.4 Which ledger/subtraction-table row defines `U_K3_allocation`

**None.** This is M1. The complete chain of what *is* pinned, in the atom's own words:

```text
|Sigma| &lt;= n-a = 981104.                                  (KB-T1)
|Z_paid| &lt;= 981104.                                       (KB-T3)
|Z_bad| &lt;= 981104 + U_Q + U_BC + U_new.                   (KB-T4)
B* = floor(|F|/2^128) = 274980728111395087,
B* - 981104 = 274980728110413983.                         (KB-T5)
```

(`background/nodes/rate_half_kb_v4_tangent_source_atom/statement.md:26,45,59,65-66`; the same integers appear at `critical/nodes/rate_half_band_closure/attack_sections/00-koalabear-owner-and-q6-ledger.md:14-16` and `background/nodes/rate_half_kb_v4_tangent_source_atom/audit.md:12`, `.../result.md:7`.)

`274980728110413983` is a **joint reserve for three cells**, not a K3 allocation. The atom then says in terms: "No value is proved here for `U_Q`, `U_BC`, or `U_new`." (`.../statement.md:69`), and the roadmap harvest entry for the same lane lists among its nonclaims "no `U_Q`, `U_BC`, `U_new`, global pencil-chart census, fixed-union aggregation, exhaustive slope payment" (`notes/PRIZE_RESOLUTION_ROADMAP.md:5448-5450`).

**Row/partition contract check (the falsifier's imported-allocation clause).** The reserve is stated for the row keyed `kb_mca` under the single frozen v4 partition, so *if* it were used it would at least be the right row and the right partition. The seam is not the row — it is the **cell**: assigning the whole reserve to `U_BC` imports budget that the same partition assigns to `U_Q` and `U_new`. Under the node's own falsifier wording ("allocation imported from a different row or partition") that is arguably in scope and arguably not; I flag it as a wording gap the coordinator should close, because it is the exact error a future run is most likely to make.

---

## D2 — WHAT IS COMPUTABLE TODAY (exact integers only)

All arithmetic below is Python `int`, replayed by `notes/pilots_20260810/k3_allocation_inequality/compute_arith.py` under `tools/ramguard local`. **56/56 internal checks PASS.** No batching was needed: every input is a small pinned literal or a manifest under 3 kB, so no checkpoint boundaries arose.

### A. Active row constants

```text
p                        = 2130706433
n                        = 2097152            (= 2^21)
k                        = 1048576            (= 2^20)
K                        = 1048577
a_plus                   = 1116048
q = p^6                  = 93571093019388561295270373781649880353786165192103559169
B_star = floor(q/2^128)  = 274980728111395087
U_paid cap = n - a_plus  = 981104
reserve = B_star - cap   = 274980728110413983
w = a_plus - K           = 67471
h = a_plus - k           = 67472
```

`B_star` and `reserve` reproduce the pinned literals exactly; `w = 67471` reproduces `deployed_rows.json:22`; `n-a_plus+1 = 981105` reproduces the published safe-set numerator.

### B. The 13-route positive residual workboard, re-derived

From `(KBPRW-1)` and `(KBPRW-3)` (`background/nodes/rate_half_kb_m2_r4_coordinate_positive_residual_loop_workboard/statement.md:16-27,42-49`) I checked, for all six outside orbits, that `sum r_i = 2`, `sum l_i + sum m_ij = 5`, `r_i + 2 l_i + sum_{j!=i} m_ij = 4` for all three `i`, and `sum l_i &lt;= 1` — **24/24 PASS**. Applying the printed rules (total defect at most three; a common loop forbids an outside loop) to the five live common skeletons reproduces `(KBPRW-4)` **exactly**:

```text
442-0a (defect 2, no common loop) -&gt; O0b, O1b, O1d           3
442-1b (defect 1, common loop)    -&gt; O0a, O0b                2
433-0  (defect 0, no common loop) -&gt; O0a, O0b, O1b, O1c, O1d 5
433-1a (defect 3, common loop)    -&gt; O0b                     1
433-1b (defect 1, common loop)    -&gt; O0a, O0b                2
                                                      total 13
```

`13 - 2 = 11` open routes, matching the eleven named obligations at `critical/nodes/rate_half_kb_m2_r4_coordinate_positive_remaining_route_payment/node.json:7` label-for-label.

### C. Closed-route censuses (exact, and unit-flagged)

```text
433-1a -&gt; O0b   60 common rows = 4+8+8+8+8+8+4+8+4          (KBPCR-2)
433-1b -&gt; O0a   15 role cells; 15*105 = 1575 raw labels;
                1575*16 = 25200 signed principal systems
```

Both PASS. **These are raw-label/system counts, not slope counts** (M3). Their contribution to `U_positive` is `0` because the routes are *empty*, which is unit-independent — that step is sound.

### D. The open `433-1b -&gt; O0b` residual (exact)

```text
split BC, product rank five    360 rows   37,800 labels   (= 6*15*4, *105)
repeated BC, cells 1/2          16 rows    1,680 labels
repeated BC, cells 11/14        32 rows    3,360 labels
total                          408 rows   42,840 labels
```

Supporting censuses re-checked: cells 3/6 per-cell census `120+120+240+240+120 = 840`; split-BC rank-drop replay `16*6*7*15 = 10,080`; cell-11 generic atlas `8*2*3*15 = 720` with rank census `248+112 = 360`; cell-11 finite boundary degree `4*4 + 4*6 = 40`. All PASS.

**These numbers are NOT convertible into `U_positive` today.** With the unproved hypothesis "each surviving raw label contributes at most one distinct affine slope", the `433-1b -&gt; O0b` route would be capped at `42,840` — I record that only to show the *scale* of the missing conversion, and it is **not importable**: `.../433_1b_o0b_residual_owner_partition/statement.md:21-22` forbids reading the 42,840 as points, and the labels-to-slopes multiplicity is exactly the open item (M3).

### E. A derived exact floor on the three unpaid cells

`deployed_rows.json:24-25` prints the identity-prefix lower attack at the active row: `attack_a0 = 138634741058327852652` and `attack_a_plus = 57198030366`, and the audit certifies that these "straddle their printed budgets in the stated lower-attack sense" (`background/nodes/deployed_identity_prefix_owner_scope_audit/claim_contract.md:5`; table at `.../statement.md:13`, reading at `.../statement.md:18-20`). Exact checks: `attack_a0 &gt; B_star` (excess `138359760330216457565`) and `attack_a_plus &lt; B_star` (`B_star - attack_a_plus = 274980670913364721`). Since the four cells are disjoint with union `Z_bad` (`background/nodes/rate_half_kb_v4_tangent_source_atom/statement.md:51-56`) and `U_paid &lt;= 981104`:

```text
U_Q + U_BC + U_new  &gt;=  57198030366 - 981104  =  57197049262.
```

**Status of this line: DERIVED, not imported.** It needs one owner ruling that `attack_a_plus` lower-bounds the same per-row bad-slope numerator that `B_star` bounds. It does **not** floor `U_BC` alone: the routing of that family into the v4 cells is explicitly unproved (`.../deployed_identity_prefix_owner_scope_audit/claim_contract.md:18`). Its one firm consequence is M8: at least one unpaid cell is nonzero, so `U_K3 = 0` cannot be recorded by default.

### F. Digests bound in this run

Recomputed SHA-256 over each file (`compute_arith.py` §F):

```text
1f64cf0474911faf7a33ec0c628bf1a65a472857be145f368804e6674d9b5343  partition_contract.json
50fa02fff88e70216ba350381e41e288d24c1344c426400d4bfefaa483a90449  tangent_source_atom/statement.md
57bba3dca290938523e49e430c9a264352291b51ca700b3361f940eb0150b390  tangent_source_atom/node.json
bdef9068a68dccaae0240eb87b0edce6c068497377cb65273d4f8548d36b85d1  deployed_rows.json
fdfe52363a1b143279e426080c8a7cf9dd79623f21f1f69f371b6794d15fef7a  residual_loop_workboard/statement.md
214291d336deb44ecaa354edccb7ef5e6ced91d2692930ac85470c777c68200c  433_1a_o0b_complete_route_exclusion/statement.md
c9e41b75dbbd083727f05a2341af19201b537f16f2820165f39d59e04ad02ca0  433_1b_raw_workboard_complete_exclusion/statement.md
a01d451b19f2c09987a5b88102edb1a39eb6e2402fe8530bce996494a7fdcaac  433_1b_o0b_residual_owner_partition/statement.md
2359e3d6f74073781179897a004ae4830472ac5ccaeffff193a7ce6cab2b17d8  source_line_complete_exclusion/statement.md
ed410d81bc93b558e8b04ae29814b5bb69ad36940b4c171b0fbeeff1c4293eae  coordinate_negative_complete_exclusion/statement.md
56be9194696cde4f8c3c861b6eeee6e14ae41b7ab3767fb1701a9f3dc3508828  k3_allocation_inequality/node.json
6d49a1b27a74e697714f29c98b18698bbb6bd4923b0590abb522515b71b41825  k3_distinct_slope_budget_ledger/node.json
96611053959ba2bb1892328133acb05edd66e337c87046f5d10f56b1a70a5666  coordinate_positive_complete_payment/node.json
af09158c4a00eda67ae6d8c38186daca80dda66189df3a4bdfb39dc824a9e035  coordinate_positive_remaining_route_payment/node.json
1e22af2bdcb2a1654a4ce5978016295b558b2d8de00da19f55a59ef2018e8e9b  k3_orientation_assembly/node.json
```

Plus the recomputed partition digest `4fade91abc408264989babcff6f8f9bbd80bcec52545a5db15ac376bf17d88fc` and the canonical `kb_mca` row-record digest `8f8c8965ee812457594b3ea36994306041645d805bff7452d6a1a3cfaeb38015`.

---

## D3 — THE DRY-RUN INEQUALITY

### The four demanded integers, today

```text
U_positive        = BLOCKED on rate_half_kb_m2_r4_coordinate_positive_remaining_route_payment (TARGET)
                    11 of 13 routes unpaid; 0 of 11 has a printed integer
U_sourcecover     = BLOCKED on rate_half_kb_m2_r4_k3_orientation_assembly (TARGET)
                    no terminal census, no cap, no bound available
U_K3              = BLOCKED (both summands blocked)
U_K3_allocation   = UNPINNED (no defining row anywhere in this repo)
U_K3 &lt;= U_K3_allocation
                  = NOT EVALUABLE
```

**An honest "blocked on certificate X" beats an estimated total, and this is that case, three times over.**

### The strongest exact statement available today

The allocation is an **interval**, not a number, and both ends are exact:

```text
0  &lt;=  U_K3_allocation  &lt;=  274980728110413983
```

- Upper end: any allocation consistent with the banked atom must satisfy `U_Q + U_BC + U_new &lt;= B_star - 981104 = 274980728110413983`, because `U_paid &lt;= 981104` is proved (KB-T3) and the four cells are disjoint with union `Z_bad` (KB-T4). Certificate: `background/nodes/rate_half_kb_v4_tangent_source_atom/statement.md:45,59,66`, digest `4fade91a...d88fc`, row `kb_mca`, digest `8f8c8965...8015`.
- The upper end is **attained by K3 only under the unproved side condition `U_Q = U_new = 0`** (`.../statement.md:69`). Substituting the reserve for `U_K3_allocation` without that proof is precisely the import error the falsifier is written to catch.
- Lower end is `0` and nothing banked improves it for `U_BC` specifically; the derived floor `U_Q + U_BC + U_new &gt;= 57197049262` (§E) constrains the sum only.

### Slack sign

**Undetermined, and I decline to guess.** My prior P3a put 70% on positive slack; the correct answer today is that the left side has no value at all, so the sign is not a fact about the mathematics — it is a fact about three missing certificates. Prior P3 is therefore scored as "not evaluable", and my pre-registered 40% on "strong enough to decide the sign at audit grade" resolves to NO.

The only slack-adjacent exact numbers I can print honestly:

```text
reserve                                    = 274980728110413983
derived floor on the three unpaid cells    =      57197049262
reserve - floor                            = 274980670913364721
```

i.e. even if the entire derived floor fell outside K3, the joint reserve remaining would be `274980670913364721`. This is a **scale reading**, not a slack: it says the budget side is enormous relative to the only banked lower attack, which in turn says the binding difficulty in this node is the *unit conversion and the missing payments*, not budget scarcity.

### What would unblock it, in dependency order

1. A labels-to-slopes conversion theorem with exact multiplicity (M3) — without this, no route integer can be stated in the node's unit at all.
2. A definition of `U_K3_allocation`: either a proof that `U_Q = U_new = 0` (which promotes the reserve to the K3 allocation exactly), or an explicit three-way split of `274980728110413983` with its own certificate.
3. Route integers for the eleven open positive routes.
4. `U_sourcecover` from the orientation assembly.
5. The four missing edges in D4/`wiring_binding`.

Items 1 and 2 are the ones nobody currently owns; 3 and 4 have owners.

---

## D4 — THE BINDING SCHEMA (DRAFT)

Full machine-readable draft: `notes/pilots_20260810/k3_allocation_inequality/binding_schema_draft.json` (parses; validated under ramguard). It is a draft in this pilot's directory only — no node, no wiring, no verifier.

Nine required blocks, each a FAIL-if-absent:

1. **`row_binding`** — pins `kb_mca` by the *separating key* `(n,k,p,K)`, not by `B_star`, plus the row-manifest digest and the canonical single-row digest. Rejects `kb_list`/`m31_*` and any budget-keyed lookup (M6).
2. **`partition_binding`** — architecture id, `partition_sha256`, digest method, `atom_order`, `owner_order`, and the explicit `k3_atom_id = "U_BC"` / `k3_owner_id = "ACTIVE_V4_BALANCED_CORE"` / `k3_priority = 2`. Rejects the upstream legacy stack and the legacy `U_paid = 422354730332` (M8, M9).
3. **`unit_binding`** — declares the manifest unit token and the node's unit phrase as two distinct strings requiring a *named equality certificate* (currently `REQUIRED_AND_ABSENT`), lists the nine forbidden units that appear in banked `m2 r4` artifacts, and carries a `labels_to_slopes_conversion` sub-record with `must_not_assume: "one label = one slope"` (M3).
4. **`summand_binding`** — one record per summand with `state in {PRINTED, BOUNDED, BLOCKED}`, a producer node id, a producer status, a value, and a certificate digest. **A `BLOCKED` summand may not be replaced by `0`, by a placeholder, or by a sibling cell's bound.** Today: `U_positive = BLOCKED`, `U_sourcecover = BLOCKED`, `U_sourceline = PRINTED_CONDITIONALLY` (with the "saturated" scope caveat of M10), `U_negative = PRINTED` at `0`.
5. **`allocation_binding`** — `state = UNPINNED`; carries the joint reserve as a *labelled non-substitute* with `owned_jointly_by = [U_Q, U_BC, U_new]` and `side_condition_status = UNPROVED`; rejects five named substitutions including the `c2(1,1,2)` `same/swap/mixed` homonym (M7).
6. **`inequality_binding`** — `EXACT_PYTHON_INT_ONLY`, explicit float/Decimal/log-scale/bit-count bans, required prints (`U_positive, U_sourcecover, U_K3, U_K3_allocation, slack, sign(slack)`), and the negative-slack policy quoted from `critical/nodes/rate_half_kb_m2_r4_k3_allocation_inequality/attack.md:9` ("Treat negative slack as a route failure, not as an invitation to renormalize the terms").
7. **`wiring_binding`** — records the M2 defect and proposes four edges (manifest atom, row manifest, positive composition, orientation assembly) into the allocation node. **Proposal only; edge ownership is coordinator-gated and this pilot made no DAG change.**

The one design decision worth surfacing: I made the schema **refuse to substitute** rather than **allow a flagged placeholder**. A flagged placeholder would let a run print a number, and the whole point of this node's falsifier is that a printed number with a bad provenance is worse than no number.

---

## ZERO-POWER AND POWER DECLARATIONS

- **Z1 (POWER: adequate).** "`U_K3_allocation` is defined nowhere in this repo." Token families searched over `*.md`, `*.json`, `*.py`, `*.txt`, `*.tex`, whole tree, excluding `dag.json`, the Codex worktree, the quarantined ledger and the sibling round-30 dirs: `U_K3_allocation` (4 files, all in the two K3 node dirs), `K3_allocation` (5, same), `k3 allocation` (0), `allocation for K3` (0), `allocation to U_BC` (0), `U_BC &lt;=` (0), `U_BC=` (0), `U_BC bound` (0), `balanced-core allocation` (0), `balanced core allocation` (0), `subtraction table`/`subtraction_table` (6 files, none in the K3 lane), `274980728110413983` (7 files, all the joint reserve). I regard this as adequate power for a negative claim.
- **Z2 (ZERO POWER).** "No cap on `U_sourcecover` exists." I searched only the `m2 r4` node families, the two K3 node dirs, and the `band_closure`/`band_structural_surplus` documents. I did **not** enumerate all 1,912 background nodes for a source-cover cap under a different name. If a source-cover cap exists under a name containing neither "sourcecover", "source-cover", nor "source cover", my search would not have found it.
- **Z3 (ZERO POWER).** "No route payment integer exists for any of the eleven open routes." I grepped the 473 `rate_half_kb_m2_r4_*` background node dirs and the six `m2 r4` critical node dirs for `slope payment`, `exact payment`, `payment of`, `pays &lt;digits&gt;`, `charge &lt;digits&gt;`, `U_remaining`, and `distinct affine slope`. Every hit was a raw-case count or an explicit non-claim. I did **not** read all 473 node directories in full, and I did not read `experiments/`, `formal/`, or `archive/`.
- **Z4 (ZERO POWER, by construction).** Anything the sibling round-30 pilots (`k3_orientation_assembly`, `k3_splitbc_transport`, `k3_chain_seams`) may have established today is invisible to me by quarantine. If any of them prints a source-cover integer or a labels-to-slopes conversion, D3's verdict changes and this report must be re-run against it. I saw three sibling filenames in `grep -l` output and opened none of them.
- **Z5 (ZERO POWER).** Upstream. I did not fetch or read any upstream PR; the upstream state quoted here is second-hand from `critical/nodes/rate_half_band_closure/notes/k3_contributor_review_20260730.md` and `notes/work_cycles/roadmap_r3/16-k3-aggregate-20260810.md`, both of which record `K3_closed: false` and "No owner, charge, K3 value, or KoalaBear row bound moves" (`k3_contributor_review_20260730.md:132-133`). `upstream_dag/` contains no `U_BC`, `balanced core`, or `K3` material at all (grep, 0 files).
- **Z6 (bound on my own arithmetic).** Every integer in D2 is either a literal read from a pinned file (cited) or a product/difference of such literals computed in Python `int`. I introduced no estimate, no rounding and no floating-point value anywhere in this report.

---

## NOVELTY SUBTRACTION (own-repo greps before any novelty claim)

Run over `critical/`, `background/`, `notes/`, root `*.md`, excluding `dag.json`, the Codex worktree, the quarantined ledger and the sibling dirs.

| claim | prior repo record? | verdict |
|---|---|---|
| M3, raw labels are not distinct affine slopes | **YES**, stated in-node at least five times (quoted above) and named as the frontier item at `.../cell11_uncolored_deployed_off_guard_pair_exclusion/frontier.md:9-10` | NOT NOVEL — I confirm and quantify it |
| M11, `n=2^21` vs `n=2^41` scope | **YES**, `critical/nodes/rate_half_band_structural_surplus/statement.md:35-37` | NOT NOVEL — restated so it is not lost |
| M4/M5, both summands gated on TARGETs | **YES**, `notes/work_cycles/roadmap_r3/16-k3-aggregate-20260810.md:35-36` names all four red leaves | NOT NOVEL — the brief anticipated it; I add the exact route accounting |
| M1, `U_K3_allocation` undefined | greps `U_K3_allocation`/`K3_allocation`/`subtraction table` → no defining occurrence | **NEW to the repo** |
| M2, allocation node has no incoming edges | greps `unwired`, `not wired`, `no incoming edge` over all shards → no record for this node | **NEW to the repo** |
| M6, `B_star` does not separate `kb_mca` from `kb_list` | greps `same B_star`, `shares B_star`, `row ambiguity`, `row confusion` → 0 hits; `kb_list` appears in 3 files, none flagging the collision | **NEW to the repo** |
| M7, `allocation` homonym in the `c2(1,1,2)` lane | the two senses coexist in-repo but no note names the collision | **NEW to the repo** (naming hazard only) |
| M8, the `U_K3 = 0` fallback is not free | greps for the derived floor `57197049262` → 0 hits outside `deployed_rows.json`'s input integer | **NEW to the repo**, and flagged DERIVED not imported |

No external/literature novelty is claimed anywhere in this report.

---

## COMPLIANCE

**Interpreter invocations: 5. All 5 under `tools/ramguard`, all with the literal `--`, all from the repo root, all stdlib-only. Zero bare `python3`.** They were: (1) `tools/ramguard tiny -- python3 notes/pilots_20260810/k3_allocation_inequality/compute_arith.py` (first version, section A only); (2) `tools/ramguard tiny -- python3 notes/pilots_20260810/k3_allocation_inequality/verify_partition_digest.py`; (3) `tools/ramguard tiny -- python3 -c ...` (six `node.json` shard statuses and their evidence edges); (4) `tools/ramguard local -- python3 notes/pilots_20260810/k3_allocation_inequality/compute_arith.py` (full run, 56/56 PASS); (5) `tools/ramguard tiny -- python3 -c ...` (parse-validate `binding_schema_draft.json`). Ramguard status: all five exited 0 with no memory or wall-clock kill; the heaviest run (4) is dominated by one `p**6` big-int power and fifteen SHA-256 file reads, far inside the 1 G / 5 min `local` profile. `verify_partition_digest.py` is a **scratch copy** of the banked `background/nodes/rate_half_kb_v4_tangent_source_atom/verify.py` with the `dag.json` read deliberately removed; the banked script itself was never executed.

**RAM discipline.** I never opened `dag.json` with `Read` and never parsed it with an interpreter. Two early recursive `grep -n` passes did stream through it and printed two very long matching lines before I added `--exclude=dag.json`; I record that honestly, and all subsequent greps carry the exclusion. All node facts in this report come from `critical/nodes/*/node.json` and `background/nodes/*/node.json` shards read one file at a time, plus targeted greps. The largest file I read in full was `critical/nodes/rate_half_band_closure/attack_sections/00-koalabear-owner-and-q6-ledger.md` (414 lines); the two multi-hundred-kilobyte notes (`PRIZE_RESOLUTION_ROADMAP.md`, `FLIP_LOG.md`) were only grepped and read by bounded line ranges (`sed -n '5420,5475p'`, `sed -n '255,290p'`), never opened whole.

**Quarantine confirmed.** `notes/pilots_20260802/CAMPAIGN_LEDGER.md` was never opened at any line — it appeared once in a `grep -l` filename list and was excluded from every grep thereafter. The three sibling round-30 directories `notes/pilots_20260810/k3_orientation_assembly`, `notes/pilots_20260810/k3_splitbc_transport`, `notes/pilots_20260810/k3_chain_seams` were never read; one of them appeared as a filename in an early `grep -l` list and all three were excluded from every subsequent grep. No path containing `prize-codex-` was read, written, or listed. No network access, no Modal, no subagents, no `git` command of any kind.

**Write scope confirmed.** I wrote exactly four files, all inside `notes/pilots_20260810/k3_allocation_inequality/`: `PREREG.md` (appended the "## Pilot registrations" section only, below the coordinator's brief, before any read beyond the two named anchors), `compute_arith.py`, `verify_partition_digest.py`, `binding_schema_draft.json`. A fifth write — `REPORT.md` — was **refused by the harness** (report `.md` files must be returned as text); its full content is this message. No `dag/`, `nodes/`, `critical/`, `background/`, `tools/`, or `orbit/` file was modified. No status flip, no edge change, no surgery of any kind — the audit-and-draft boundary held.

**Prior scoring (blind priors registered in `PREREG.md` before any further read).** P1a WRONG, P1b WRONG, **P1c RIGHT** (15% branch). P2a partly right in shape but wrong in content — I predicted `U_positive` computable and `U_sourcecover` blocked; **both are blocked**, so **P2c** (15% branch) is the outcome. P2b refuted. P3 not evaluable (the left side has no value); my 40% prior on being able to decide the sign resolves NO. P4's "some artifact already contains a floating-point comparison or renormalized owner count" (35%) — not found; **declared ZERO POWER**, I did not audit banked verifier scripts for float usage. P4's "line multiplicity recorded per-line but dropped somewhere" (30%) — refuted in a stronger direction: line multiplicity is not recorded anywhere at all, which is M3.
