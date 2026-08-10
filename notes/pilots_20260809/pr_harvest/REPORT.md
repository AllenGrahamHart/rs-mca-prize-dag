# REPORT — pr_harvest (persisted verbatim by the coordinator, task a30336f9f48d586d5, 2026-08-09)

## Report — PR re-harvest vs the current board (round 25a)

Registrations appended to `notes/pilots_20260809/pr_harvest/PREREG.md` (sections R0–R7) **before any `python3` ran**; the append used the `Edit` tool, no interpreter involved. Artifacts: `jcheck.py/.txt`, `mystery7_calibration.py/.txt`, `fixture1148.py/.txt`, `replay/1146/`, `replay/1148/` — all inside the pilot dir.

---

### 0. Framing correction, registered in advance (R0)

The brief calls audit items #6 and #8 "NEVER RUN". **Item #6 was already run on 2026-08-07** and banked at `critical/nodes/l1_program_frontier/statement.md:24-43` ("Domination check resolved (2026-08-07)… Theorem J does not cover #1145/#1146"). I registered this before computing, then re-scoped: (#6-a) audit that resolution independently; (#6-b) run the test the board change actually opened — the **defect-side** functional, which is a different functional and had never been applied.

---

### 1. D1 item #6 — THE THEOREM-J CHECK, executed

**The dictionary is not assumed — it is derived from their own note.** `git show pr1145:experimental/notes/l1/l1_exact_five_onset_and_six_fibre_terminal.md:87-88` excludes `p = 23, 67` because they "have fewer than eleven quotient labels, so they cannot realize the `tau = 5, m = 6` RS geometry". `|Q| = (p-1)/11` is 2, 6, 18, 38 at 23, 67, 199, 419 — the exclusion is **exactly** `|Q| &gt;= m + tau = 11`, which proves `n = (m+tau)·ell`. With core `= m` fibres and the background-free list threshold `agreement = N - d + h &gt;= s ⟺ h &gt;= d + g`, we get `k-1 = N = m·ell` and `s = N + g = (m+1)·ell`. (PROVED-replayed.)

**(#6-a) Theorem J MISSES — all ten rows, exactly** (`jcheck.txt`, part 1). Closed form `s² − n(k−1) = ell²(1 − m(tau−2))`:

| (tau,m) | n | k−1 | s | clause 1: 2s−(n+k−1) | clause 2: s²−n(k−1) |
|---|---|---|---|---|---|
| (6,8) | 154 | 88 | 99 | −44 | **−3751** |
| (6,9) | 165 | 99 | 110 | −44 | **−4235** |
| (6,10) | 176 | 110 | 121 | −44 | **−4719** |
| (7,9) | 176 | 99 | 110 | −55 | **−5324** |
| (7,10) | 187 | 110 | 121 | −55 | **−5929** |
| (8,10) | 198 | 110 | 121 | −66 | **−7139** |

Clause 1 reduces to `tau &lt; 2`, so it fails on every row (all have `tau &gt;= 5`). Enlarging `n` past the minimal support domain only worsens clause 2. **This CONFIRMS the banked 08-07 addendum by independent re-derivation (MATCHED), and extends it** to the four `tau = 5` rows the addendum never enumerated: `(5,6) −2057`, `(5,7) −2420`, `(5,8) −2783`, `(5,9) −3146`. **Verdict: Theorem J neither dominates nor partially dominates — it MISSES.**

**(#6-b) THE NEW TEST — the defect-side sieve, which the board change legalized.** `l1_fixed_support_defect_johnson_bound/statement.md:84-98` (round-24) makes `(JB3)`/`(JB4)` legal at every `t`. Its `h` is the **petal agreement**, and their `S_tau` is exactly the **envelope of `h`** — machine-confirmed from their own auditor: `replay/1146/experimental/scripts/audit_p04cw_parity_uniform_S6_theorem.py:194`, `even_s6 = sum((even + [0]*6)[:6])`, i.e. `S_h` = sum of the `h` largest fibre values. So the crosswalk is `h &lt;= S_tau`, `g = ell = 11` (background-free), `r_J = 2d − h`, `J = d² − N·r_J`.

- **The mechanism (a corollary of OUR own PROVED node, one line, and NOT previously written down — own-repo grep run per hard law 5: only `statement.md:35` and `proof.md:36` state clause 1 abstractly):** `h &gt;= d+g` and `r_J = 2d−h &lt;= d−g`, so **`d &lt; g ⟹ r_J &lt; 0 ⟹ |Z| &lt;= 1`**. Field-independent, `ell`-uniform, every chart.
- **On their `tau = 6` rows** (the row carrying #1146's headline `S_6 &lt;= 20`): their envelope forces `d &lt;= S_6 − 11 = 9 &lt; 11`, hence `r_J &lt; 0` for **every** admissible defect, hence `|Z| &lt;= 1` — outright per-pattern uniqueness on all three certified `tau=6` rows. (PROVED-replayed arithmetic; see caveat below.)
- **`tau = 7`:** uniqueness for `d &lt;= 10`; at `d = 11, h = 22` → `r_J = 0`, `J = 121`, `(JB4)` gives `|Z| &lt;= 99·11/121 = 9` at `m=9` and `&lt;= 10` at `m=10`.
- **`tau = 8`:** uniqueness for `d &lt;= 10`; `d=12,h=23` → `r_J=1, J=34`, `|Z| &lt;= 605/17 = 35`; `d=12,h=24` → `|Z| &lt;= 9`; `d=13,h=24` → `J = 169−220 = −51`, **vacuous**.
- **Unconditionally** (their theorem *not* used, only the quintic fibre cap `h &lt;= 5·tau`): at `(6,8)` the sieve is live for `d &lt;= 16` and vacuous for `d ∈ {17,18,19}`. **So the entire content of `S_6 &lt;= 20`, expressed in our currency, is: it deletes the `d ∈ [11,19]` tail where our functional is weak-or-vacuous, leaving only `d &lt;= 9` where our node already gives uniqueness.**

**Verdict (#6): NOT domination in either direction — exact complementarity, newly visible only because of the board change.** Theorem J gives nothing (sub-Johnson). The newly-legalized defect-side functional gives *more* than #1146 on the low-defect range (uniqueness, not just an envelope) and *nothing* on the high-defect tail, which is precisely what #1146 removes. Composed, the two give per-pattern uniqueness on the whole `tau=6` family.

**Caveat, stated plainly (CANDIDATE at the chart level).** The arithmetic above is exact and replayed; the identification of their coset-sunflower members with `(JB1)`'s `(F, W)` pairs is a **candidate** chart mapping — I did not verify `deg W &lt;= d` or the labelling from their certificates. The one hypothesis I *registered as the likely failure*, primitivity, **transfers**: their note line 34 says "Exact pointwise reconstruction gives **primitive**, divisibility-minimal listed anchors for tau = 6,7,8." My registered P2e is falsified (see §7).

---

### 2. D1 item #8 — THE BRIDGE STATUS, executed

**Answer: NO — and the situation is now strictly worse for pricing #1148 than the 08-03 audit recorded.**

1. **No successor exists.** Repo-wide grep for `locator-to-codeword` / `incidence-to-codeword` returns exactly three live sites, all pre-existing: `background/nodes/rate_half_list_chamber_affine_rank_bridge/upstream_crosswalk.md:24`, `critical/nodes/rate_half_list_adjacent_crossing/frontier.md:141` and `:223`. No node id in `dag.json` supplies such a map (grep of `"id": "…locator…"` → 9 nodes, none of them a bridge). (MATCHED.)
2. **The bridge is now a PROVED NEGATIVE, not merely "does not fire".** `node.json` statement: *"the rank-flat expression is strictly greater than four … Hence its integer cap is at least four in all thirteen chambers and the harvested compiler cannot prove the predecessor cap three."* Plus an independent coarse fence (`verify_compiler_cannot_bite.py`) reaching integer cap **six**. So even if #1148 shipped the missing map, the compiler it would feed **cannot reach the required cap 3**. (NOT-OUR-LANE-still, now for two independent reasons.)
3. **What the bridge must supply, stated exactly** (this is the answer the action item asked for): a map from split degree-479 locators in the flat to the *codewords* whose error support they carry, delivering a **two-sided interval for `d_s`** — not a floor. The 2026-07-26 forced correction on `statement.md` proves the cap is **non-monotone** in `d_s` (it *rises* from 8 at `d_3 = R+3` to 21 at `d_3 = n`), so a lower bound on the top generalized weight makes the bound *worse*. A locator-side classification supplies neither side of that interval.

---

### 3. D2 — the re-triage matrix (prior verdicts stand unless a NAMED change re-opens)

Board objects: **B1** mystery 7 · **B2** the J-sieve legal at every t via (JB3) · **B3** red-3 rows posable, `dim V = e+1` · **B4** constant-weight cluster (mystery 2+4) · **B5** Z-CEILING / THEOREM RC · **B6** family-uniform falsification at N′=256.

| PR | B1 | B2 | B3 | B4 | B5 | B6 |
|---|---|---|---|---|---|---|
| **#1145** | NOT-OUR-LANE-still | *newly-relevant* — supplies the `S_tau` envelope that caps `d` | NOT-OUR-LANE-still (their "anchor rank 4 / no rank drops" is a *coefficient-space* rigidity, not an `(F,W)` slice; same genre, different object) | NOT-OUR-LANE-still | NOT-OUR-LANE-still | NOT-OUR-LANE-still |
| **#1146** | NOT-OUR-LANE-still | **APPLIES (partial, complementary)** — §1 | NOT-OUR-LANE-still | NOT-OUR-LANE-still | NOT-OUR-LANE-still | NOT-OUR-LANE-still |
| **#1147** | NOT-OUR-LANE-still | NOT-OUR-LANE-still | NOT-OUR-LANE-still | NOT-OUR-LANE-still | NOT-OUR-LANE-still | NOT-OUR-LANE-still |
| **#1148** | **NEWLY-RELEVANT-SINCE (B1)** — §4 HC-1 | NOT-OUR-LANE-still | NOT-OUR-LANE-still | NOT-OUR-LANE-still | NOT-OUR-LANE-still | NOT-OUR-LANE-still |

**FAILS-BECAUSE, recorded:** `#1148 × LIST/M31 pricing` re-opened by B1 and re-closed for pricing purposes by the bridge fence's *proved-negative* upgrade (§2.2). It re-opens only as an **instrument calibration**, never as a chamber or list movement.

**#1147 / SOL_TARGET_4:** no B1–B6 change touches it. Prior verdict superseded on 08-03, not by me: `SOL_TARGET_4_H4_COLLISION_CENSUS.md:48-88` records the conjecture **FALSIFIED AS STATED** (`N=256, q=257`: `T_4 = 1,729,295,040`, `T_4/N³ = 103.07`; `N=256, q=769`: ratio 3.78), and the `T_4^{smooth,ordered} = 2n·T_sm` bridge **adopted**. The one item still outstanding is the **reprice wording** — still "a surfaced decision, not applied here".

---

### 4. D3 — harvest candidates, with import shape and verification cost

**HC-1 (from #1148 × B1) — the mystery-7 instrument calibration. Highest value in this pilot.**
Mystery 7's instrument is the anticode formula `binom(n,r)/binom(j,r)`, and `f_global_packing_step/statement.md:24-27` names its own failure mode: *"Merely assuming `r&lt;j` is insufficient. The full-space case `r=j` is a known counterexample."* I measured `r` at both exhibited M31 flats, straight from #1148's fixture using their own parse (`fixture1148.txt`):

- **Theirs:** 16 branches of size 35 inside `|U| = 514`; locator degree `514 − 35 = 479`; `|U| + |core| = 514 + 509 = 1023`. **Pairwise root-set intersections: min 444, max 446** out of degree 479 → `r/j = 0.931`.
- **Ours** (`l1_m31_fixed_support_divisor_direction_cap_route_cut`, PROVED): `J_a = R(X−a)` all share `|R0| = 4979` of 4980 roots → `r/j = 0.9998`.

So **both exhibited flats sit right at the instrument's own known-counterexample end `r → j`**, and the valid anticode ceiling at #1148's flat is `C(1023,447)/C(479,447)`, i.e. **2^840.2 against a truth of 16 — vacuous by 2^836**. Mystery 7's wall is therefore *not* "the exponent grows with the dimension"; it is that the flats of interest consist of locators sharing almost all their roots.

**The lead that falls out (CANDIDATE, and the reason this is worth importing):** change to **symmetric-difference coordinates**. In the complement, their 16 branches are 35-subsets of a 514-set pairwise meeting in `&lt;= 2`, and the *same* anticode instrument gives `C(514,3)/C(35,3) = 3437` vs truth 16 — **2^7.75 loose instead of 2^836 vacuous**. At our own fixture the same move is **exact**: `m − (t−1) = 72428 − 4979 = 67449`, the node's own count, looseness 2^0. Own-repo subtraction run: complement coordinates appear once, at `background/nodes/l1_cofactor_prefix_pade_graph_normal_form/lineage.md:5`, and never against the packing instrument.
*Import shape:* an **instrument-calibration statement addendum** on `background/nodes/l1_rootfree_rational_q_projective_packing` (the instrument owner) + a node-local note on `l1_m31_fixed_support_divisor_direction_cap_route_cut` + one line in the roadmap r5 mystery-7 record. **Not** a new PROVED node, **not** an edge to any red.
*Verification before adoption:* (a) their synthesis + Schur verifiers — **DONE, PROVED-replayed** (§6); (b) the overlap measurement — **DONE**, pure set arithmetic from the fixture, no trust in their sieves; (c) **the gap that must be stated in the addendum:** the "exactly the sixteen" upper truth rests on their **UNREPLAYED** 10.69e9-normal C++ sieves, and the complement structure is a property of the 16 *vertices* — an arbitrary split member of the hull need not have its roots inside `U`. So the lead is a coordinate-change *proposal*, not a bound.

**HC-2 (from #1146 × B2) — the `S_tau ↔ h` crosswalk.** *Import shape:* node-local statement addendum on `l1_fixed_support_defect_johnson_bound` (per the standing node-local-notes rule) + a citation line on `l1_program_frontier` replacing "possible partial domination — open check" with the executed verdict. *Verification cost:* zero beyond this pilot — exact integer arithmetic (replayed) plus their auditor (replayed PASS). *Citation discipline already binding on the node applies verbatim:* "for the two parity supports", never "for ell=11 exact-five".

**HC-3 (ours, exposed by the comparison) — the corollary `d &lt; g ⟹ |Z| &lt;= 1`.** One line from clause 1 plus the node's own threshold; not currently written anywhere. *Import shape:* a clause in the same addendum, labelled OURS. *Cost:* nil.

**HC-4 — outstanding, not a harvest:** the SOL_TARGET_4 reprice wording (index hypothesis) is still unapplied; and **FLAG F4 is confirmed still live by my replay** — the shipped `SP01zxab_full_affine_hull_synthesis.json` carries `dense_primary_normals = 10694457224` vs `dense_audit_normals = 10694457231`, **difference exactly 7**, with their own verifier still declining to compare them. Ask maelcar.

**Bonus, free:** audit **FLAG F5 is now RESOLVED** from the fixture — the "1,023-point fixture domain" is `U` (514 branch roots) ⊔ `core` (509 evaluation points), degree `= |U| − 35 = 479`, and the "fourteen plus two pencil" is visible as the degenerate parameter pairs at indices **5 → (1,0)** and **11 → (2,0)**.

---

### 5. D4 — queue scan #1121–#1143

Established live via authenticated `gh pr list --repo przchojecki/rs-mca` (33 open PRs, #1121–#1152; **all 23 numbers in range present, no gaps guessed**), corroborated against `notes/PR_SWEEP_20260803.md:30-47`, `notes/wave24_integration_20260727/WAVE33_AUDIT.md:44-47`, `WAVE37_AUDIT.md:93-127`, `WAVE42_AUDIT.md:48`, `notes/roadmap/sections/12-r3-2-board-revision.md:83,166`.

**Genuine new matches: 0** — the registered expected answer (P6), reported as-is. Two false friends disarmed rather than counted: **#1121's "J-zero"** is the Mersenne-HNF role value `J_* = 0`, not B2's Johnson functional; **#1122's "ternary"** is a ternary secant/circuit variety in the KoalaBear equality-wall surface, not B5's ternary kernel. Closest call **#1124 × B1** carries the 67449-direction counterfixture — but it is *our* PR exporting a node we already hold, so B1 makes **our node** load-bearing (that is HC-1), not the queue entry. Records gap stated, not papered over: **#1133, #1134** are identified and open but have no by-number absorption record in our notes; **#1135–#1137** are on record as *import pending*. Nothing in the range was replayed; the C++/HPC loads there stay **UNREPLAYED**.

---

### 6. Replays executed (house import law) and loads listed-not-run

**PROVED-replayed by me, this session, all via `tools/ramguard local -- python3` from repo root:**
- `#1146 audit_p04cw_parity_uniform_S6_theorem.py` → `PASS_P04CW_INDEPENDENT_PARITY_UNIFORM_S6_AUDIT`, `line_states=252 five_states=241 unique_scalar_profiles=483` (matches AUDIT.md:23 exactly). Its `:283` asserts `maximum == artifact[...] == 10` and `:281` asserts `even_s6 &lt;= 20` per state — the constant I compared against is genuinely recomputed, not read.
- `#1148 C_verify_SP01zxab_full_affine_hull_synthesis.py` → `PASS_EXACT_FULL_AFFINE_HULL_RIGIDITY`; `affine_dimension = 15`, `vertex_count = 16`, `split_affine_hull_members = exactly_the_sixteen_vertices`.
- `#1148 A_verify_SP01zxaa_Schur_power_profile.py` → `PASS_MAXIMAL_SQUARE_AND_FULL_AMBIENT_CUBE`; profile `(16, 136, 509)`, `GRS_square_dimension_if_applicable = 31`. Hand-checks re-confirmed: `136 = C(17,2)` (maximal), `2^16−1 = 65535`, `Σ_{s=9}^{16}C(16,s) = 26333`, `C(16,8) = 12870`.

**UNREPLAYED, listed not run** (compute law): all #1148 partition sieves (10,694,457,224 normals, C++/HPC); #1145's `p04cu` C++ spectrum census; #1146's SymPy `derive_*` exhaustiveness stages; #1147's `max C_r = 5789`; SOL_TARGET_4's decisive rows (already settled on 08-03 by a coordinator Modal run, not by me).

---

### 7. Self-corrections, stated plainly

1. **P2e falsified.** I registered primitivity (`gcd(F,W)=1`) as the hypothesis most likely to fail transfer. It transfers — their own note asserts primitive anchors at `tau = 6,7,8`. The residual transfer risk is elsewhere (`deg W &lt;= d` and the labelling), and I have downgraded that part to CANDIDATE rather than claiming the mapping.
2. **P2a/P2b/P2c were all wrong, because I mis-set `h`.** I registered `h = tau·ell` (full petals). `h` is the petal **agreement**, capped by `S_tau`, which is far smaller. My predicted crossovers `d* = 44 / 41.84 / 40.43` and "worst bound `|Z| &lt;= 22` at `d=43`" are **void**. The corrected picture (uniqueness at `tau=6`) is *stronger* than what I predicted, which is not a defence — the registered numbers were wrong.
3. **P4e was wrong against information already in my own brief.** I registered #1147/SOL_TARGET_4 as "unchanged and still open, decisive row still not run". The brief itself says items 1–3 were executed, and `SOL_TARGET_4_H4_COLLISION_CENSUS.md:48-88` shows the conjecture falsified as stated on 08-03 with `(256,257)` and `(256,769)` both run. Careless registration.
4. **My own first calibration was invalid and I corrected it mid-pilot.** `mystery7_calibration.py` priced the instrument dimension-driven (`2^12.59` loose at their flat, `2^3.27` at ours, ≈0.93 bits per projective dimension). Then `fixture1148.py` **measured** the overlaps (446/479 and 4979/4980) and showed (PC3)'s hypothesis fails at *both* fixtures by factors of 30 and 300. Those looseness figures are therefore **not valid bounds**; the file now carries a SUPERSEDED banner and the valid numbers live in `fixture1148.txt`. The corrected finding is sharper than the wrong one, but the wrong one was published first and is retained with its correction.
5. **A refinement, not a correction, to the 08-03 audit:** it wrote "ours is degree 4,980 at `N = 1,053,557`". Both numbers are right in their own places — `N = 1053557` is the ambient row (`l1_m31_rank7_dense_top_decorated_shift_pair_router/statement.md:14`), while the packing-relevant point count is the fixed support `m = 72428`. The calibration uses 72428.

---

### 8. Compliance

No status flip, no closure claim, nothing adopted into `dag.json`. All writes confined to `notes/pilots_20260809/pr_harvest/`; PR files read one at a time with `git -C ../rs-mca show pr114X:&lt;path&gt;`; no checkout, no bulk directory read, `dag.json` only grepped. Every `python3` via `tools/ramguard tiny|local -- python3` from the prize repo root, including every JSON peek. Stdlib only; no Modal; no git writes. `notes/pilots_20260802/CAMPAIGN_LEDGER.md` not read (it shows a recent mtime from another session — not mine). The quarantine clause and all rules were passed **verbatim** to the single subagent dispatched (the D4 queue scan), which replayed nothing and asserted nothing as PROVED.
