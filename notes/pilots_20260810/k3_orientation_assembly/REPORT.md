REPORT — k3_orientation_assembly (round 30)

The harness blocked writing `REPORT.md` to disk (subagent report-file policy), so the full artifact text is returned verbatim below — please persist it to `notes/pilots_20260810/k3_orientation_assembly/REPORT.md`. Two files were written inside my scope: the appended `## Pilot registrations` block in `PREREG.md`, and `replay_orientation_images.py`.

**Headline:** the routing theorem is not buildable today. Its domain is a set of bad slopes (`Z_BC`) and its codomain is a set of geometric workboard cells, and the map between them is explicitly disclaimed in-repo ("The endpoint parameter line is not the evaluation carrier"). Two of the three named images exist; the third — source-cover — does not exist as an object at all, so `U_sourcecover` has no domain to sum over. Offsetting that: the orientation trichotomy itself is already a theorem (`delta=|S|` forces three order-two subgroups; transpose transport merges two; the source-subfield dichotomy splits the third), so a conditional draft with one named hypothesis is writable now.

---

# REPORT — k3_orientation_assembly (round 30)

Pilot: `rate_half_kb_m2_r4_k3_orientation_assembly` (TARGET, critical).
Date: 2026-08-10. Grade attempted: AUDIT-AND-DRAFT. No surgery applied.

---

## 0. MISSES FIRST — what I could not do

**M1. I did not build a provable routing theorem, and I now believe one cannot be built today.** The node's domain is a set of *bad slopes* (`Z_BC`, an arithmetic object over the deployed KoalaBear row) and its codomain is a set of *combinatorial workboard cells* (packets of an algebraic correspondence curve). The map between them does not exist in this repo, is not merely unproved but explicitly disclaimed, and is disclaimed by the very node that supplies the geometry: `background/nodes/rate_half_kb_decomposition_source_pencil_compiler/statement.md:48` — "The endpoint parameter line is not the evaluation carrier." The same fence is repeated at `critical/nodes/rate_half_band_closure/attack_sections/00-koalabear-owner-and-q6-ledger.md:77` — "The parameter line and carrier remain distinct." Everything below is therefore an audit plus a *conditional* draft whose top hypothesis is that missing bridge. I POSE it; I do not claim it.

**M2. I could not compute `U_sourcecover`, not even as a bound.** There is no source-cover object in this repo at `m=2,r=4` to sum over (§D4). I name the exact missing certificate instead.

**M3. I could not verify the node's own image-exactness clause; I believe it is false as written.** The statement says "The source-line image is exactly the declared `c2(1,1,2)` source-line workboard" (`critical/nodes/rate_half_kb_m2_r4_k3_orientation_assembly/node.json:7`). The declared workboard covers the *saturated* `(a,b,c)=(1,1,2)` row only; three further live diagonal rows and one exceptional orbit have no workboard at all (§D1.4, §D3-O3). This is a finding about the node text, not about the upstream mathematics.

**M4. I did not read the sibling round-30 dirs, and I did not re-derive `U_positive`.** `U_positive` belongs to the two coordinate-payment nodes, which are separately owned; I treated it as a symbol.

**M5. One quarantine leak, self-reported.** An early repo-wide `grep -rn` for `U_K3|U_sourcecover|U_positive|U_remaining` matched and printed approximately fifteen lines from `notes/pilots_20260810/k3_allocation_inequality/PREREG.md`, a quarantined sibling dir. I did not open the file, and no content from those lines is used anywhere in this report or in any conclusion. Every subsequent grep carried `grep -v 'pilots_20260810/k3_'`. Full disclosure in §Compliance.

**M6. Scope I did not audit.** I did not re-audit the eleven open positive routes, Codex's wave-55+ raw-workboard work, or the `n=2^21` → `n=2^41` transport (the WP5 quantifier mismatch, `notes/kernel_basis/WP5_RATEHALF_VERDICT.md:12-18`, restated in-node at `critical/nodes/rate_half_band_structural_surplus/statement.md:35-37`: "The workboard rows are n = 2^21 extension rows; transport to the / n = 2^41 prime razor rows is NOTE-LEVEL"). That fence sits *above* this node and is unaffected by anything here.

**M7. `REPORT.md` could not be written to disk.** The harness blocked the write under its subagent report-file policy. The artifact is returned verbatim to the coordinator instead; the two in-scope files that *were* written are the `PREREG.md` registrations block and `replay_orientation_images.py`.

---

## D1 — THE OBJECT MAP

### D1.1 The active row and partition contract

The active first-match manifest is the partition contract of the PROVED `rate_half_kb_v4_tangent_source_atom`. It is the only `partition_contract*.json` in the repo (`find . -name 'partition_contract*.json'` → one hit).

| field | value | file:line |
|---|---|---|
| architecture | `GRANDE_FINALE_V4_KB_MCA_TANGENT_SOURCE_ADAPTER_V1` | `background/nodes/rate_half_kb_v4_tangent_source_atom/partition_contract.json:2` |
| partition digest | `4fade91abc408264989babcff6f8f9bbd80bcec52545a5db15ac376bf17d88fc` | `.../partition_contract.json:64` |
| deployed row | `p=2130706433`, `F=F_(p^6)`, `n=2097152`, `k=1048576`, `a=1116048` | `background/nodes/rate_half_kb_v4_tangent_source_atom/statement.md:16` |
| unit | `DISTINCT_BAD_FINITE_SLOPES_PER_RECEIVED_LINE` | `.../partition_contract.json:69` |
| chronology | `U_paid` → `U_Q` → `U_BC` → `U_new`, `first_match: true` | `.../partition_contract.json:54`, owner order at `:57-62` |
| this node's cell | `ACTIVE_V4_BALANCED_CORE`, priority 2, `paid: false` | `.../partition_contract.json:38-43` |

The digest is independently pinned outside the node at `notes/roadmap/sections/07-tracks.md:1699-1700` and `notes/PRIZE_RESOLUTION_ROADMAP.md:2454-2455`.

The witness set is defined literally at `background/nodes/rate_half_kb_v4_tangent_source_atom/proof.md:25-30`:

```text
Z_paid = Z intersect T,
R_1    = Z \ Z_paid,
Z_Q    = R_1 intersect Q,
R_2    = R_1 \ Z_Q,
Z_BC   = R_2 intersect BC,
Z_new  = R_2 \ Z_BC.
```

So **W := Z_BC** — the "unpaid same-owner balanced-core bad-slope witnesses" of the node statement — is exactly the third first-match cell. `|Z_bad| &lt;= 981104 + U_Q + U_BC + U_new` (`background/nodes/rate_half_kb_v4_tangent_source_atom/statement.md:59`), and "No value is proved here for `U_Q`, `U_BC`, or `U_new`" (`:67-68`).

**FINDING D1-a (dangling contract target).** The contract's `"residual_passes_to": "experimental/grande_finale.tex#part:rank-atoms"` (`.../partition_contract.json:66`) points at a path that does not exist in this repo — there is no `experimental/` directory (top-level dirs are `archive background critical experiments formal graph notes orbit tools upstream_dag`). The residual's own onward destination is therefore upstream-only. This matters for D3-O1: the contract itself does not name an in-repo object that receives `Z_BC`.

### D1.2 Image 2 — the signed coordinate workboards (BOTH EXIST)

*Negative.* PROVED `rate_half_kb_m2_r4_coordinate_negative_loop_budget_gate`, five pair-multiplicity skeletons at `background/nodes/rate_half_kb_m2_r4_coordinate_negative_loop_budget_gate/statement.md:18-23` (label `(KBNL-2)`), obtained from the parent's seven injective skeletons `(KBCV-6)` by `ell_K&lt;=2` (`:14`, label `(KBNL-1)`). The orientation is then PROVED empty: "No negative-parity coordinate-order-two packet exists over the deployed / KoalaBear field" (`background/nodes/rate_half_kb_m2_r4_coordinate_negative_complete_exclusion/statement.md:16-17`), five rows `(KBNX-1)` at `:19-28` deleted respectively by `(KBNX-2)` at `:31-35`.

*Positive.* PROVED `rate_half_kb_m2_r4_coordinate_positive_residual_loop_workboard`: ten parent common orbits → five live orbits / seven labelled skeletons (`.../statement.md:16-28`, label `(KBPRW-1)`), six outside orbits `(KBPRW-3)` at `:41-48`, and thirteen necessary routes `(KBPRW-4)` at `:55-61`; "Thus thirteen representative route records remain" (`:64`). Two are closed, eleven open (`critical/nodes/rate_half_kb_m2_r4_coordinate_positive_remaining_route_payment/statement.md:3-19`).

**I replayed all three censuses independently** (script `notes/pilots_20260810/k3_orientation_assembly/replay_orientation_images.py`, stdlib only, run under `tools/ramguard local`). All PASS:

```text
B1  common orbit count                     10   (parent's ten)
B4  orbit sizes and defects match (KBPRW-1) exact
B5  live common orbits  {442-0a,442-1b,433-0,433-1a,433-1b}
B6  labelled live skeletons                 7
B7  outside orbit count                     6
B8  outside sizes/defects match (KBPRW-3)  exact
B9  necessary route records                13
B10 route table equals (KBPRW-4)           exact
C1  injective skeleton orbits (KBCV-6)      7
C2  negative skeletons after ell_K&lt;=2       5
C3  negative set equals printed (KBNL-2)   exact
```

Two reconstructions were needed and are recorded because they are not printed in-repo: the degree law `deg_i = 2 l_i + sum_{j!=i} m_ij`, and the defect law `defect = #loops + sum_{i&lt;j} 2*max(m_ij-2, 0)`. The defect law reproduces **all sixteen** printed defect entries of `(KBPRW-1)` and `(KBPRW-3)` exactly, which is strong evidence it is the intended one. The positive workboard's "loop cap" is exactly "at most one common loop" (it and only it deletes `442-2, 442-3, 433-2, 433-3`); the negative gate's `ell_K&lt;=2` is strictly weaker.

**FINDING D1-b (the two coordinate workboards are not the same list).** My replay prints:

```text
positive-only live skeletons: 433-1a, 442-0a
negative-only live skeletons: 433-2,  442-2
shared skeletons:             433-0, 433-1b, 442-1b
```

The "signed negative/positive coordinate workboards" of the node statement are therefore two *different* five-element skeleton lists whose union is seven skeletons, overlapping in three. Disjointness of the coordinate image is supplied by the parity split, **not** by the skeleton label. Any routing proof that treats "the coordinate image" as one workboard indexed by skeleton will double-count `433-0, 433-1b, 442-1b`. I have not seen this stated anywhere in-repo (own-repo grep for `442-2`/`433-2` in the positive/negative node pair returns only their own censuses).

### D1.3 Image 1 — the declared c2(1,1,2) source-line workboard (EXISTS, PARTIAL)

The declared object is `(KBS2-4)` of PROVED `rate_half_kb_m2_r4_diagonal_c2_112_saturated_defect_classifier`: "96 labeled packets in 12 matching-preserving orbits" (`.../statement.md:49`), cut down from "exactly `1,560` labeled pairs" in `123` orbits (`:38-42`). It is PROVED empty by `rate_half_kb_m2_r4_diagonal_c2_112_source_line_complete_exclusion` ("Hence the complete saturated source-line `c2(1,1,2)` branch is excluded.", `.../statement.md:33`).

Its census contract is explicit that this is one branch of one row: `.../claim_contract.md:11` — "nonclaim | coordinate and source-cover branches, universal packet assembly, `rate_half_band_closure`, and both Prize theorems remain open"; and `.../statement.md:35-36` — "Coordinate/source-cover branches and later packet/source-row assembly also / remain open."

### D1.4 FINDING D1-c — the source-line image is NOT exactly that workboard

The diagonal orientation has a five-row mixing census, PROVED at `background/nodes/rate_half_kb_m2_r4_diagonal_facet_mixing_obstruction/statement.md:42-46`:

```text
(a,b,c) in {
  (2,0,2), (1,1,2),
  (1,0,4), (0,1,4),
  (0,0,6)
}.                                                       (KBDM-3)
```

I replayed this from first principles (block A of my script): over all `10395` fixed-point-free involutions on the twelve source labels, with `I={0..5}`, `K={0..4}`, `xi=5`, the realised `(a,b,c)` set is **exactly** those five rows, `c in {2,4,6}`, and `|I cap tau(I)| = 6-c` holds identically — i.e. `(KBDM-2)` and `(KBDM-3)` both replay PASS. The labelled multiplicities, which I do not find printed anywhere in-repo, are

```text
(2,0,2): 1350   (1,1,2): 2700   (1,0,4): 3600   (0,1,4): 1800   (0,0,6): 720
partition-preserving tau deleted by (KBDM-1): 225      (total 10395)
```

(CATCH-24A caveat: the integer `2700` also appears at `background/nodes/rate_half_kb_m2_r4_diagonal_c2_112_source_line_colored_quotient_compiler/source_evidence.md:24` as "all `2700` aligned and `900` near-saturated" cases. That is a different object; I make no claim that the coincidence is meaningful and I claim no novelty for the number itself.)

Status of the five rows:

| row | status | evidence |
|---|---|---|
| `(2,0,2)` | DELETED entirely | `rate_half_kb_m2_r4_diagonal_c2_202_defect_exclusion`; "four rows remain" at `critical/nodes/rate_half_band_closure/attack_sections/08-diagonal-whole-fiber-program.md:181` |
| `(1,1,2)` saturated, source-line branch | DELETED (this is the declared workboard) | `(KBS2-4)` + source-line complete exclusion |
| `(1,1,2)` exceptional unsaturated orbit `(KBDM-10)` | **OPEN, no workboard** | `.../diagonal_facet_mixing_obstruction/statement.md:125`; "it must retain that exceptional `(1,1,2)` orbit" at `attack_sections/08-...:139`; "keep `(KBDM-10)` separate" at `:197` |
| `(1,0,4)` | **OPEN, no workboard, no node** | see below |
| `(0,1,4)` | **OPEN, no workboard, no node** | see below |
| `(0,0,6)` near-aligned survivor | **OPEN, no workboard** (aligned subcase deleted) | `(KBDM-5)-(KBDM-7)`; `attack_sections/08-...:103-120` |

Own-repo search for `(1,0,4)`/`(0,1,4)`/`(0,0,6)` treatment: `ls background/nodes | grep kb_m2_r4_diagonal` returns 34 nodes, of which **every** row-specific one is `c2_112_*` or `c2_202_*`; and `grep -rn '(1,0,4)|(0,1,4)|c2_104|c2_014|c2_006'` across `background/`, `critical/` and `notes/` returns only the census printings themselves (`facet_mixing_obstruction/statement.md:44`, `attack_sections/08-...:89`, `notes/PRIZE_RESOLUTION_ROADMAP.md:11159`, `:11243`) plus unrelated `m4`/`F3` hits.

**Conclusion D1-c.** The node's clause "The source-line image is exactly the declared `c2(1,1,2)` source-line workboard" is *false* as a description of the diagonal source-line branch, unless a separate theorem deletes rows `(1,0,4)`, `(0,1,4)`, `(0,0,6)` and orbit `(KBDM-10)`. No such theorem is in the repo. The node text needs either that theorem or an explicit scope restriction to the saturated `(1,1,2)` row.

### D1.5 FINDING D1-d — the source-cover image does not exist

"Source-cover" is branch 2 of the PROVED source-subfield dichotomy: `background/nodes/rate_half_kb_m2_r4_diagonal_source_subfield_dichotomy/statement.md:52` — "2. **Biquadratic source cover.** If `K_1!=K(X)`, then `E/F` is Galois with group `V4`" — with genus and passport data `g in {0,1}, #Fix(mu)=2-2g` `(KBDS-6)` at `:58` and the two tame passports `(KBDS-7)` at `:62-65`. Its result card is explicit: "Neither branch is yet excluded." (`.../result.md:6-7`).

There is **no source-cover workboard, census, cell list, chart list, or terminal enumeration for `m=2,r=4` anywhere in this repo.** Searches performed (CATCH-24A):

- `ls background/nodes critical/nodes | grep -i 'source_cover|sourcecover'` → exactly one hit, `rate_half_kb_m2_r2_dihedral_residual_source_cover_twist_classifier`, whose scope is the `m2 **r2**` dihedral row (`.../statement.md:1,4`), i.e. the already-deleted `(2,2,4)` type — **not this row**.
- `grep -rli 'biquadratic'` over `background/ critical/` → 5 node families, all of which mention it only as an out-of-scope disclaimer, e.g. `background/nodes/rate_half_kb_m2_r4_diagonal_c2_square_fiber_linear_cut/audit.md:14-15` ("No part of the proof applies to the biquadratic source-cover branch or the exceptional unsaturated `(1,1,2)` orbit") and `background/nodes/rate_half_kb_m2_r4_diagonal_c2_202_ramified_defect_exclusion/audit.md:4-5`.
- `ls background/nodes | grep kb_m2_r4 | grep -i 'v4|cover|genus'` → nine hits, none a source-cover object.

The only forward-facing instruction is the dichotomy's own frontier (`.../frontier.md:5-7`): "In the biquadratic branch, classify the rational and elliptic `V4` passports against the six-pole source data and the twelve whole-fiber quartics."

**ZERO-POWER DECLARATION Z1.** My search for a source-cover object was a token search over node ids (`source_cover`, `sourcecover`, `cover`, `v4`, `genus`, `biquadratic`) plus a prose grep over `background/`, `critical/`, `notes/`. If such an object were banked under a name sharing none of those tokens, I would have missed it. I did *not* stream the compiled `dag.json` (forbidden) and did not read the Codex worktree (forbidden). Treat "no source-cover object exists" as *high-confidence but token-limited*.

### D1.6 Object map, assembled

```text
witness cell            Z_BC = R_2 cap BC          (proof.md:29, digest 4fade91a)
        |
        |  [O1: NO PROVED BRIDGE — parameter line != carrier]
        v
actual (m,r,delta) type  {(2,4,2), (2,8,1)}        (m3 router result.md:7-8,
        |                                           section 06 line 47-48)
        |  [O2: (2,8,1) has no orientation]
        v
(2,4,2) stabilizer S     three order-two subgroups  (outer_recurrence_router
        |                                            statement.md:33-35)
    +---+--------------------------+
    |                              |
 &lt;tau x 1&gt; / &lt;1 x tau&gt;          &lt;tau x tau&gt;
 = COORDINATE                   = DIAGONAL
    |                              |
  parity +/-                  source-subfield dichotomy (KBDS)
    |   \                       /                  \
    |    \                     /                    \
 positive negative      SOURCE-LINE lift        SOURCE-COVER (biquadratic)
 13 routes  5 skels      5 rows (KBDM-3)         2 passports (KBDS-7)
 (KBPRW-4)  (KBNL-2)     1 row's saturated       *** NO OBJECT ***
 11 open    PROVED       branch closed;
            EMPTY        3 rows + (KBDM-10) open
```

---

## D2 — WITNESS CLASSIFICATION

### D2.0 The honest layer-0 answer

**There is no declared sub-typing of `Z_BC` itself.** The partition contract gives one predicate, `BAD_SLOPE_NOT_EARLIER_AND_HAS_ACTIVE_V4_BALANCED_CORE_CERTIFICATE` (`partition_contract.json:41`), and nothing refines it. Grep for `U_BC`/`Z_BC` across the repo returns nine files, all of which either define the cell or disclaim any value for it (e.g. `background/nodes/rate_half_kb_q6_u2_complete_source_conic_exclusion/statement.md:30-31` — "It supplies no distinct-slope count, owner, `U_Q`, `U_BC`, `U_new` ...").

**ZERO-POWER DECLARATION Z2.** Any statement of mine of the form "the witness types are exactly ..." is therefore a statement about *component* types, obtained by assuming the missing bridge O1. Stated as a fact about slopes it would be a search-shaped hole. I decline to make it.

### D2.1 The classification that does exist (component-level)

Assume O1. Then the live classification is a five-level tree, every level of which is backed by a PROVED node:

**Level 1 — transverse type.** `delta*r=4m, delta&lt;=m^2, r&lt;=60/m-1`, 26 types (`background/nodes/rate_half_kb_source_pencil_rank_transverse_compiler/statement.md:23-38`), reduced by the degree routers to three (`background/nodes/rate_half_kb_m3_primitive_outer_degree2_router/result.md:7-8`: "The independent transverse frontier drops from eight types to three: / `(m,r,delta)=(2,2,4),(2,4,2),(2,8,1)`"), then `(2,2,4)` deleted, leaving two: "The live `m=2` frontier is now exactly the order-two stabilizer type / `(r,delta)=(4,2)` and the trivial-stabilizer type `(8,1)`" (`critical/nodes/rate_half_band_closure/attack_sections/06-full-v4-source-facet-close.md:47-48`).

**Level 2 — stabilizer.** `background/nodes/rate_half_kb_m2_v4_outer_recurrence_router/statement.md:33-35`:

```text
(r,delta)=(2,4): S=V4;
(r,delta)=(4,2): S is one of the three order-two subgroups;
(r,delta)=(8,1): S=1.
```

**Level 3a — coordinate parity.** `&lt;tau x 1&gt;` and `&lt;1 x tau&gt;` merge under `rate_half_kb_m2_r4_coordinate_transpose_transport` `(KBTT-2)` (`.../statement.md:22-27`); parity is forced to be exactly one of two coefficient forms (dimension 8 or 7) by `rate_half_kb_m2_r4_coordinate_coefficient_normal_form`, quoted at `critical/nodes/rate_half_band_closure/attack_sections/08-diagonal-whole-fiber-program.md:596-605`.

**Level 3b — diagonal source-subfield.** `(KBDS)` dichotomy, exhaustive by construction ("Exactly one of the following holds", `.../source_subfield_dichotomy/statement.md:21`).

**Level 4 — diagonal mixing row.** `(KBDM-3)`, replayed exhaustive above.

**Level 5 — saturation.** saturated vs `(KBDM-10)` (`.../diagonal_facet_mixing_obstruction/statement.md:121-125`).

### D2.2 Type → orientation → quantity at risk

Four preserved quantities, per the node statement (`critical/nodes/rate_half_kb_m2_r4_k3_orientation_assembly/node.json:7`): **(i)** received-line owner, **(ii)** support reconstruction, **(iii)** affine slope, **(iv)** chronology.

| # | witness type | must route to | quantities at risk | why |
|---|---|---|---|---|
| T1 | `(2,4,2)`, `S=&lt;tau x 1&gt;`, positive parity | coordinate-positive workboard, one of 13 routes | (iii), (iv) | routes are counted in *labelled packets/systems*, never in slopes: "This theorem does not identify raw labels with distinct affine slopes." (`background/nodes/rate_half_kb_m2_r4_coordinate_positive_433_1b_raw_workboard_complete_exclusion/statement.md:18`); the 2026-08-10 aggregate repeats it: "This is a raw-system theorem; / it is not a distinct-affine-slope payment." (`notes/work_cycles/roadmap_r3/16-k3-aggregate-20260810.md:18-19`) |
| T2 | `(2,4,2)`, `S=&lt;1 x tau&gt;`, either parity | coordinate workboard **after transposition** | **(i), (iv)** | "Geometric route equivalence does not transport an owner or payment / without a separate chronology theorem." (`background/nodes/rate_half_kb_m2_r4_coordinate_transpose_transport/audit.md:13-14`); also "The original and primed source forms are not identified" (`.../statement.md:50-51`) |
| T3 | `(2,4,2)`, `S=&lt;tau x 1&gt;`, negative parity | coordinate-negative workboard | none once landed | image is PROVED empty (`coordinate_negative_complete_exclusion/statement.md:16-17`); risk is entirely in *landing* |
| T4 | `(2,4,2)`, diagonal, source-line lift, `(1,1,2)` saturated | declared `c2(1,1,2)` workboard, `(KBS2-4)` | none once landed | PROVED empty |
| T5 | `(2,4,2)`, diagonal, source-line lift, `(1,1,2)` exceptional `(KBDM-10)` | **nothing declared** | **(ii)** | no reconstruction target exists; the only in-repo instruction is "keep `(KBDM-10)` separate" (`attack_sections/08-...:197`) |
| T6 | `(2,4,2)`, diagonal, source-line lift, rows `(1,0,4)`,`(0,1,4)`,`(0,0,6)` | **nothing declared** | **(ii)** | no workboard; no exclusion node |
| T7 | `(2,4,2)`, diagonal, biquadratic source cover, any row, genus-0 passport | **source-cover image — nothing declared** | **(i),(ii),(iii),(iv)** | §D1.5 |
| T8 | same, genus-1 passport | **source-cover image — nothing declared** | **(i),(ii),(iii),(iv)** | §D1.5 |
| T9 | `(2,8,1)` trivial stabilizer | **no orientation at all** | all four, vacuously | "The trivial-stabilizer type also remains open." (`attack_sections/07-coordinate-order-two-signature.md:45`); its only theorem is the universal facet census, whose frontier says "Do not impose unproved involution symmetry on the trivial row." (`background/nodes/rate_half_kb_m2_u2_universal_source_facet_census/frontier.md:6-7`) |

T1–T8 are inside the node's own `m2 r4` scope. T9 is outside the node's name but inside the K3 arm's ledger, and this is the sharpest structural consequence of the audit (see O2).

---

## D3 — THE DRAFT ROUTING THEOREM

Stated as a conditional skeleton. Every gap is a named obstruction with a pre-registered falsifier. **POSE, not claim.**

### D3.0 Notation

`W = Z_BC` (D1.1). For `z in W` let `Gamma(z)` denote the actual irreducible bidegree-`(4,4)` component of the endpoint self-correspondence `f(T)=f(W)` that the balanced-core certificate of `z` produces — *this object is exactly what O1 says does not yet exist.* Write `Orient(Gamma) in {SL, CO, SC}` for source-line, coordinate, source-cover.

### D3.1 The map

```text
route(z) :=  CO   if Gamma(z) has stabilizer &lt;tau x 1&gt; or &lt;1 x tau&gt;;
             SL   if stabilizer &lt;tau x tau&gt; and K_1 = K(X);
             SC   if stabilizer &lt;tau x tau&gt; and K_1 != K(X).
```

Priority is not needed: the three branches are already mutually exclusive by Levels 2 and 3b of D2.1. This is the single genuinely good news of the audit: **the trichotomy is a theorem, not a construction.**

### D3.2 Lemma spine

**Lemma R2 (orientation trichotomy). PROVED, assemblable today.** For every actual `(2,4,2)` component exactly one of `SL, CO, SC` holds. *Proof.* `delta = |S|` and `(r,delta)=(4,2)` gives `|S|=2`, so `S` is one of the three order-two subgroups of `V4` (`rate_half_kb_m2_v4_outer_recurrence_router/statement.md:26-35`). If `S` is `&lt;tau x 1&gt;` or `&lt;1 x tau&gt;` set `CO`; the transpose transport `(KBTT-1)` makes these one geometric route (`coordinate_transpose_transport/statement.md:19-27`). If `S=&lt;tau x tau&gt;`, the source-subfield dichotomy is an exclusive alternative (`source_subfield_dichotomy/statement.md:21`, `:23`, `:52`), giving `SL` or `SC`. QED. — *This lemma needs no new mathematics; it needs writing down.*

**Lemma R3 (coordinate parity split). PROVED.** Every `CO` packet is positive- or negative-parity, by the two forced coefficient forms (dimensions 8 and 7) of `rate_half_kb_m2_r4_coordinate_coefficient_normal_form` (`attack_sections/08-...:592-611`), and the two workboards `(KBPRW-4)`/`(KBNL-2)` receive them.

**Lemma R4 (diagonal row split). PROVED.** Every diagonal packet lies in one `(KBDM-3)` row; `(2,0,2)` is empty. Replayed by me (block A).

**Lemma R5 (coordinate image exactness).** *POSE.* The coordinate image is the pair of workboards, and the two lists differ (FINDING D1-b). Needs a disjointness clause keyed on parity, not on skeleton name. *Falsifier:* an assembly that counts skeleton `433-0`, `433-1b` or `442-1b` once when both parities are live.

**Lemma R6 (source-line image exactness).** *POSE — currently FALSE as written.* See O3.

**Lemma R7 (source-cover terminal trichotomy).** *POSE — vacuous today.* See O4.

**Lemma P1–P4 (preservation of owner / support / slope / chronology).** *POSE. All four are open.* Own-repo grep for `chronology` across `background/nodes/rate_half_kb_m2_r4*/**.md` returns **exactly one file**, `coordinate_transpose_transport/audit.md`, and there it is a *disclaimer* (`:13-14`). Grep for `preserv.*owner|owner.*preserv` across `background/nodes/rate_half_kb_m2_r4*` and `critical/nodes/rate_half_kb_m2_r4*` returns **two hits, both in TARGET nodes asking for it**: `critical/nodes/rate_half_kb_m2_r4_k3_independent_review/review_protocol.md:8` and `critical/nodes/rate_half_kb_m2_r4_k3_orientation_assembly/attack.md:10`. **No background node anywhere in the `m2 r4` family asserts any of the four preservation properties.** *ZERO-POWER DECLARATION Z3:* this is a token grep. A node asserting preservation in different vocabulary ("the first-match owner is unchanged under this transport") would be missed. I searched `chronology`, `owner`, `preserv`. Confidence: high, not certain.

### D3.3 The eight named obstructions

**O1 — THE BRIDGE (fatal, top of the tree).** No proved map `Z_BC -&gt; {actual (2,4,2) or (2,8,1) components}`. Evidence: `rate_half_kb_decomposition_source_pencil_compiler/statement.md:48-51` ("The endpoint parameter line is not the evaluation carrier. The conditional / carrier classification supplies no parameter-to-carrier bridge, witness-data / descent, owner, charge, cap `68`, `u=2` close, adjacent certificate, or row / close."); repeated at `attack_sections/00-...:73-77`. The roadmap treats it as a *promotion test*, not a theorem: "prove / a source-bound transport into one frozen first-match cell" (`notes/PRIZE_RESOLUTION_ROADMAP.md:5451-5452`). *Pre-registered falsifier:* exhibit a bad slope in `Z_BC` for which no `(2,4,2)`/`(2,8,1)` component exists, or two distinct components for one slope with different orientations — either kills single-valuedness of `route`. *What would close it:* a same-record parameter-to-carrier bridge for the order-`2^21` carrier, the object conditionally classified at `decomposition_source_pencil_compiler/statement.md:37-41`.

**O2 — THE FOURTH CLASS `(2,8,1)`.** The live transverse frontier is two types, not one. The node's three orientations cover `(2,4,2)` only. *Pre-registered falsifier:* a balanced-core witness whose component is trivial-stabilizer — this satisfies the node's own falsifier clause "A balanced-core bad slope outside the three orientations" (`.../k3_orientation_assembly/node.json:8`) while violating nothing upstream. *Two honest repairs:* (a) prove `(2,8,1)` empty, or (b) restrict the node to `(2,4,2)` **and** add a fourth term to the K3 ledger. Note that (b) changes `U_K3 = U_positive + U_sourcecover` (`critical/nodes/rate_half_kb_m2_r4_k3_distinct_slope_budget_ledger/statement.md:7`) into a three-term identity, so it is a coordinator-gated edit, not a pin correction. I did not make it.

**O3 — SOURCE-LINE IMAGE INEXACT.** Rows `(1,0,4)`, `(0,1,4)`, `(0,0,6)` near-aligned, and orbit `(KBDM-10)` have no declared image (FINDING D1-c). *Pre-registered falsifier:* a `(1,0,4)` source-line packet — it is combinatorially admissible (my replay finds 3600 labelled `tau` in that row), and nothing in-repo excludes it.

**O4 — SOURCE-COVER IMAGE ABSENT.** No object; `U_sourcecover` has no domain to sum over (FINDING D1-d). *Pre-registered falsifier:* trivially satisfied today — the theorem's "every source-cover image is either proved empty, mapped bijectively ..., or paid" quantifies over an undefined set. A vacuous-truth reading is not admissible because the node must also *print* `U_sourcecover`.

**O5 — UNIT MISMATCH (labels vs distinct affine slopes).** Every workboard is denominated in labelled packets / signed principal systems; the ledger unit is `DISTINCT_BAD_FINITE_SLOPES_PER_RECEIVED_LINE` (`partition_contract.json:69`). No conversion theorem exists; the raw workboard node says so in terms (`.../433_1b_raw_workboard_complete_exclusion/statement.md:18-20`: "does not identify raw labels with distinct affine slopes. It / does not prove exhaustive balanced-core routing, ..."). *Pre-registered falsifier:* two distinct workboard labels carrying the same affine slope (over-count), or one label carrying two slopes (under-count).

**O6 — PRESERVATION UNSTATED.** Lemma P1–P4 above; zero background support (Z3). *Pre-registered falsifier:* a route whose payment is charged to a different received line than the witness's.

**O7 — TRANSPOSE MERGE IS NOT OWNER-SAFE.** `&lt;1 x tau&gt;` components are routed through `theta`, which is proved to be a *geometric* equivalence only: "Geometric route equivalence does not transport an owner or payment without a separate chronology theorem" (`coordinate_transpose_transport/audit.md:13-14`). For an *emptiness* theorem this is harmless; for a *counting* theorem it is not, because `Gamma` and `Gamma^tr` are distinct components. *Pre-registered falsifier:* a `&lt;1 x tau&gt;` witness and its transpose both charged to the coordinate image, doubling `U_positive`.

**O8 — CHRONOLOGY IS PARTITION-LEVEL, NOT ROW-LEVEL.** The first-match chronology is defined on the four owner cells (`partition_contract.json:9-53`), while the "add-back chronology" the node must preserve is an ordering *inside* the routing. Nothing defines the latter. *Pre-registered falsifier:* two routings of the same residual that agree setwise but give different `U_sourcecover` because the add-back order differs.

Obstruction count: **8** (my pre-registered point estimate was 5, interval 3–8; landed at the upper edge — see §Priors).

### D3.4 What IS provable today (the salvageable core)

I recommend the node be re-posed as the conjunction of a PROVED spine and one named hypothesis:

&gt; **Draft Theorem (conditional orientation assembly).** Assume (H-bridge): every `z in Z_BC` determines a unique actual transverse component `Gamma(z)` of the deployed KoalaBear `Q=6,s=6,u=2` residual, with the received-line owner and affine slope of `z` carried along. Then `Gamma(z)` has type `(2,4,2)` or `(2,8,1)`; and on `(2,4,2)` the map `route` of D3.1 is total, single-valued and exhaustive, with images `CO` = the two signed coordinate workboards `(KBPRW-4)`/`(KBNL-2)`, `SL` = the diagonal source-line branch stratified by `(KBDM-3)`, and `SC` = the biquadratic branch stratified by `(KBDS-7)`. The negative-coordinate image and the saturated `(1,1,2)` source-line image are empty. No integer is produced.

Every clause of that statement is a PROVED in-repo node (R2, R3, R4 above) plus (H-bridge). It is a real, writable, audit-grade deliverable — and it is strictly weaker than the current node text, because it does **not** claim image-exactness (O3), does **not** produce `U_sourcecover` (O4), does **not** cover `(2,8,1)` (O2), and does **not** preserve owner / support / slope / chronology (O6, O7, O8). Whether to re-pose the node that way is a coordinator decision; I have not touched the node.

---

## D4 — `U_sourcecover`

### D4.1 What the integer must be

Exactly: the disjoint sum, in the unit `DISTINCT_BAD_FINITE_SLOPES_PER_RECEIVED_LINE` (`partition_contract.json:69`), of the exact distinct-affine-slope payments assigned to those source-cover terminal cells that are neither proved empty nor carried bijectively into the source-line or coordinate image — under the active manifest, active row `a=1116048`, digest `4fade91abc408264989babcff6f8f9bbd80bcec52545a5db15ac376bf17d88fc`, and the frozen owner order. It then enters `U_K3 = U_positive + U_sourcecover` (`critical/nodes/rate_half_kb_m2_r4_k3_distinct_slope_budget_ledger/statement.md:7`).

### D4.2 It is NOT computable today

Three independent blocks, any one of which suffices:

1. **No domain.** There is no source-cover terminal cell list (§D1.5). A sum over an unenumerated set is not an integer.
2. **No unit conversion.** Even a complete cell list would give labelled packets, not distinct affine slopes (O5).
3. **No bridge.** Even a slope-denominated payment would be uncharged without O1.

I therefore did **not** pre-register a value. I record the natural target for falsifiability: **if** the biquadratic branch is proved empty in all four live `(KBDM-3)` rows and both `(KBDS-7)` passports, **then** `U_sourcecover = 0` — which is what the ledger's own attack anticipates ("If all residual terms are eliminated, record `U_K3=0`; do not assume zero / before the route and source-cover compilers establish it", `critical/nodes/rate_half_kb_m2_r4_k3_distinct_slope_budget_ledger/attack.md:10-11`). I assign no probability to that outcome here; my pre-registered prior was 0.4 and I have found no evidence bearing on it either way — an honest zero-power outcome (**Z4**).

### D4.3 The exact missing certificate

**One certificate, four rows, two passports.** Name it, say, `rate_half_kb_m2_r4_diagonal_biquadratic_source_cover_workboard`:

&gt; For each live diagonal mixing row `(a,b,c) in {(1,1,2), (1,0,4), (0,1,4), (0,0,6)}` and each tame passport of `(KBDS-7)` (`g=0: eta, eta', mu` and `g=1: eta, eta, eta', eta'`), enumerate the admissible complete-source packets of the non-lifting branch against the six-pole source data and the twelve whole-fiber quartics, exactly as instructed at `background/nodes/rate_half_kb_m2_r4_diagonal_source_subfield_dichotomy/frontier.md:5-7`. Print a finite terminal-cell list with orbit counts, in the style of `(KBS2-4)` and `(KBPRW-4)`.

Downstream of it, two further certificates are needed before `U_sourcecover` is an integer: the unit-conversion theorem (O5) and the bridge (O1). `U_K3_allocation` is separately undefined — grep for the token `U_K3_allocation` across `--include=*.md --include=*.py` returns only the two node statements that *ask* for it (`critical/nodes/rate_half_kb_m2_r4_k3_allocation_inequality/statement.md:12` and `.../k3_distinct_slope_budget_ledger/statement.md:7`) — but that is the sibling node's obligation, not mine.

---

## Prior scorecard (registered blind in PREREG.md before any further read)

| prior | registered | outcome |
|---|---|---|
| P0 shape: priority split | predicted priority-ordered | **wrong in a good way** — the trichotomy is *already exclusive* (Lemma R2), no priority needed |
| P0 (b) exhaustiveness is enumeration-backed | predicted yes | **wrong** — it is group-theoretic (`delta=|S|`), not enumerative |
| P0 (c) image-exactness is where the work is | predicted yes | **right** (O3, O4) |
| P0 (d) chronology bites hardest | predicted yes | **half right** — chronology is open (O8), but the *bridge* (O1) dominates it |
| P1 obstruction count 5 (interval 3–8) | 5 | **8** — upper edge of my interval |
| P2 full theorem already banked | 0.15 | **no** (grep for "orientation assembly" finds only the TARGET nodes and the roadmap) |
| P2 exhaustiveness half already banked | 0.55 | **yes, and stronger than expected** — R2+R3+R4 are all PROVED |
| P2 ≥1 preservation property already proved | 0.65 | **no** — zero of four (Z3) |
| P3 all three objects exist under recognisable names | 0.55 | **no** — two of three exist; the third does not exist at all |
| P3 quotable digest | 0.7 | **yes** — `4fade91a...` |
| P4 `U_sourcecover` computable today | 0.35 | **no** |
| P4 I end by naming a missing certificate | 0.6 | **yes** (§D4.3) |
| P4 I can print an exact bound | 0.75 | **no** — not even a bound; the domain is undefined |
| P5 zero-power warning would be needed | registered | **used four times** (Z1–Z4) |

---

## Novelty statement (CATCH-24A)

Nothing in this report is claimed as new mathematics. Three items I believe are new *as assembled statements*, each with the own-repo grep that failed to find prior art:

1. **The two coordinate workboards are different skeleton lists** (FINDING D1-b, three shared / two+two exclusive). Prior-art grep: the positive and negative nodes each print only their own census; no file compares them (`grep -rn '442-2|433-2'` over the `m2_r4_coordinate_*` families returns only the censuses).
2. **The per-row labelled `tau` multiplicities of `(KBDM-3)`** (`1350/2700/3600/1800/720`, `225` deleted, total `10395`). Prior-art grep for those integers over `background/nodes/rate_half_kb*` and `critical/nodes/rate_half*` returns only an unrelated `10395` in a binomial list (`source_pencil_rank_transverse_compiler/proof.md:16`) and the unrelated `2700/900` at `c2_112_source_line_colored_quotient_compiler/source_evidence.md:24`.
3. **The reconstructed defect law** `defect = #loops + 2*sum max(m-2,0)`, which reproduces all sixteen printed defect entries. Prior-art grep for `defect` inside the positive/negative workboard nodes finds the *values* but never the *formula*.

Everything else — O1 through O8, the five-row diagonal frontier, the live `(2,8,1)` type, the raw-vs-slope unit gap — is already recorded in-repo in the places I cite, mostly as disclaimers in `nonclaim` blocks and `frontier.md` files. This report's contribution there is *assembly*: it is the first place they are collected against one node's obligations.

---

## Compliance

**Interpreter invocations: 2. Both `tools/ramguard local -- python3 ...`, literal `--`, from the repo root. Zero bare `python3`. Zero `tiny` invocations were needed (no JSON peeks required an interpreter; all JSON I touched was read with `Read`/`grep` at file scale).** Both invocations ran the single script `notes/pilots_20260810/k3_orientation_assembly/replay_orientation_images.py` (stdlib only: `itertools`; no imports beyond it; no network, no Modal, no git). First run exposed two modelling errors in my own orbit-counting (over-counted 14 orbits vs the printed 10, and orbit sizes 3x); I corrected the model — at most one loop per vertex, and orbits taken inside the ordered degree profile — and the second run is `FAILURES: none` across all 17 checks. Peak footprint was trivial (a 10395-element involution enumeration); ramguard reported no ceiling event on either run.

**RAM discipline.** `dag.json` was never opened; all node facts came from `critical/nodes/*/node.json` and `background/nodes/*/*.md` shards, read one file at a time, with `grep -n`/`sed -n` windows on the four large files I needed (`notes/PRIZE_RESOLUTION_ROADMAP.md`, `notes/roadmap/sections/*`, `notes/work_cycles/roadmap_r3/16-*.md`, the `attack_sections/*`). No bulk loads. Note: three greps used `--include=*.json .` at repo root and therefore *matched* lines inside `dag.json`; I filtered those lines out with `grep -v '^dag.json'`/`grep -v '^./dag.json'` and did not read them. Two `dag.json` statement lines did scroll past in one early grep before I added the filter; they were duplicates of node-shard statements I had already read, and nothing in this report depends on them.

**Quarantine.** `notes/pilots_20260802/CAMPAIGN_LEDGER.md` was never opened at any line and was excluded from every recursive grep from the first one onward. The sibling round-30 dirs `k3_allocation_inequality`, `k3_splitbc_transport`, `k3_chain_seams` were never opened. **One leak, already flagged as M5:** a single early `grep -rn` printed roughly fifteen matched lines from `notes/pilots_20260810/k3_allocation_inequality/PREREG.md` into my context before I added the `grep -v 'pilots_20260810/k3_'` filter. I did not open the file, I did not read beyond the matched lines that the tool printed, and no statement, number, prior, or conclusion in this report derives from them — in particular my own P4 priors were registered before that grep ran, and §D4 rests entirely on the node shards and the source-subfield dichotomy. No path containing `prize-codex-` was read, listed, or matched (all greps ran with `grep -v 'prize-codex-'`, and `ls -d */` confirms no such directory exists in this checkout).

**Write scope.** I attempted to write exactly three files, all inside `notes/pilots_20260810/k3_orientation_assembly/`: the appended `## Pilot registrations` section of `PREREG.md` (registered after the two anchors and before any further read, with the interpreter count at 0 stated in-line), `replay_orientation_images.py`, and `REPORT.md`. The first two succeeded; the third was refused by the harness under its subagent report-file policy, so this report is delivered as text for the coordinator to persist. No `dag/`, `nodes/`, `critical/`, `background/`, or `tools/` file was created or modified. No git operation of any kind was run. No subagent was launched.
