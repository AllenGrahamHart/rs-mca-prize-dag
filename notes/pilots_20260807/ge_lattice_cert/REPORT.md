# REPORT — ge_lattice_cert (persisted verbatim by the coordinator from the session transcript, task a759a36be53e0f16e, 2026-08-07)

All work complete. Here is my report.

---

# ROUND 23 — THE DIM-64 LATTICE CERTIFICATION RUN

**Headline (two results, one of them a correction to the machinery I was told to reuse):**

1. **`e1_folded_no_vector_certificate_128_payload` is CERTIFIED EMPTY by a complete enumeration** — 2,061,127,954 Fincke–Pohst nodes, at the literal pinned field/root, with a fail-closed control that passed at the same dimension and determinant. This is the first complete (not BKZ-inconclusive) transcript for that cell.
2. **CATCH-23A: round-22's `d4_cone.py` enumerator is NOT fail-closed.** It under-reports witnesses on 3 of its 6 published rows. Round-22's *verdicts* survive; three banked *constants* do not. Since round 23's entire mandate is emptiness certification, this had to be fixed before anything else was trusted.

All work is in `/home/u2470931/smooth-read-solomin/prize/notes/pilots_20260807/ge_lattice_cert/`. No writes outside it; `dag.json`, `nodes/`, `tools/` untouched; no git writes, no Modal, stdlib only, every `python3` via `tools/ramguard`. Registrations were appended to `PREREG.md` before any computation (post-hoc amendments are separately flagged in `PREREG.md` §P9).

---

## 1. CATCH-23A — the reused machinery is unsound as an emptiness certifier

`notes/pilots_20260807/ge_floor_falsifier/d4_cone.py:116-118` computes the per-level Fincke–Pohst half-width as an **integer**:

```
hi = 0
while Fraction((hi + 1) ** 2) &lt;= lim:   hi += 1
```

then scans `x_i ∈ [ceil(-c - hi), floor(-c + hi)]` (`:119-124`). The true window is `|x_i + c| ≤ sqrt(lim)` with **c rational**, so the interval is truncated by `sqrt(lim) − floor(sqrt(lim))` on each side. At `(h=4, p=137)` the four levels lose 0.109–0.232 per side, and valid lattice points fall outside.

Adjudicated by exhaustive box sweep (`catch_d4cone.py`, ground truth):

| cell | round-22 published | **brute force** | mine |
|---|---|---|---|
| h=4, p=137, 2ℓ'=8 | 2 | **8** | 8 |
| h=4, p=401 | 0 | 0 | 0 |
| h=8, p=12289, 2ℓ'=6 | 0 | 0 | 0 |
| h=8, p=12289, 2ℓ'=16 | **6** | **16** | 16 |
| h=8, p=463249, 2ℓ'=16 | 2 | **16** | 16 |
| h=8, p=463457 | 0 | 0 | 0 |

**Structural confirmation, independent of any recomputation** (`symmetry.py`): Λ_p is an ideal, so every witness set is closed under the negacyclic shift σ and under −1. The true sets are single full ⟨σ,−1⟩-orbits of size exactly 2h (8, 16, 16). **Round-22's reported sets are not σ-closed** — its own output was already detectably incomplete.

**What moves:**
- `critical/nodes/lattice_cone_certificate/statement.md:35-40` banks *"there are 6 non-cyclotomic kernel witnesses"* at p=12289 full radius. The true count is **16**.
- Round-22 `REPORT.md`'s D4 witness column `(2,0,0,6,2,0)` should read `(8,0,0,16,16,0)`; its FPCOST column was measured on a truncated tree, so the "model over-predicts by 2–3×" calibration is calibrated against under-counts.

**What does NOT move:** all three EMPTY verdicts are genuinely empty (confirmed by brute force *and* by my complete enumeration), and D3/TIGHTEMPTY came from `sweep.py` (exhaustive box sweep), not `d4_cone.py`. Round-22's headline conclusions stand. But a "0 witnesses" answer from that tool was never a proof of emptiness — which is exactly what this round was asked to produce.

---

## 2. D1 — THE ROW LIST (with file:line)

**The spec pins a FAMILY, not a finite list** — `background/nodes/official_row_primes_pinning/statement.md:8-10`:
&gt; `The grand challenges quantify over every admissible choice of F, L, and k, subject to the printed bounds and sufficiently-large-field proviso. They do not specify a hidden finite list of official row primes.`

Admissibility (`.../proof.md:27-30`): `k &lt;= 2^40`, `|F| &lt; 2^256`.

**PINNED (R1)** — a node makes the literal certificate its own payload:

| cell | p | root | N' | box | provenance |
|---|---|---|---|---|---|
| **E1-128** | `9046256971666468693477907086899377594122279777450959829708209533531277 23009` (2^249.000) | ρ₁₂₈ = `44026618583012229486255209887871781979482135870287517619879801663372 9926114` | 128 | {−2..2}^64, no support restriction | `e1_pocklington_250bit_exhibit_field/statement.md:11-12` and `:23-24`; `e1_folded_no_vector_certificate_128_payload/statement.md:9-16`; restated at `e1_folded_certificate_cell_128_payload/statement.md:14-15,25` |
| E1-256 | same p | ρ₂₅₆ (`:26-27`) | 256 | {−2..2}^128 | `e1_folded_no_vector_certificate_256_payload/statement.md:8-16` |

**DEPLOYED (R2)** — the four Proth prize rows, `background/nodes/mca_quadratic_prize_rows/statement.md:31-34`, verified exactly (`facts.py`): all prime, all `p ≡ 1 mod 128` (in fact mod 2^92…2^97), all with an exact order-128 root, all `B = floor(p/2^128)` matching the printed table.

| rate | n | p | bits | v₂(p−1) | bits below 253^32 |
|---|---|---|---|---|---|
| 1/2 | 2^41 | `132540169958804033333249306710494641010898987122689` = 26766274163673319604503·2^92+1 | 167 | 92 | 88.95 |
| 1/4 | 2^42 | `411940680852499481698306614369841346700408394874881` | 169 | 93 | 87.32 |
| 1/8 | 2^43 | `979947269755402568812854322316630667196565607677953` | 170 | 95 | 86.07 |
| 1/16 | 2^44 | `2121285573237585848299875619011192262679065433997313` | 171 | 97 | 84.95 |

These are **not** a side-quest: `critical/nodes/integer_code_distance_cert/status_ruling.md:17-19` places them squarely in this route's residue —
&gt; `The order-128 branch with p&gt;253^32 is now paid analytically by integer_code_distance_high_field_folded_box_exclusion. The four pinned Proth prize exhibits have 167--171-bit primes and are below its threshold.`

**PRICED-NOT-RUN (R3)** — the six deployed clean-anchor rows. `background/nodes/qfloor_clean_anchor_norm_threshold_route_cut/statement.md:9-13` fixes (rate, N', ℓ'): 1/4→(256,65), 1/8→(256,33), 1/16→(512,33); *"The table is identical at RowC and prize scale"* (`:15`). No prime is pinned, only intervals: `I_C=[2^250, 2^250+2^128−1]` and `I_P=[B_P·2^128, …]`, `B_P=317494674775468773183020924238786383963` (`e1_pair_feasible_prime_field_reduction/proof.md:20-24, 38-43`). **Notation trap** (`notes/roadmap/sections/07-tracks.md:200-202`): here `N=256,512` are *quotient orders*, so the folded dimensions are **128 and 256**, not 64.

**EXHIBIT** — the corridor literal prime `q = 2^41·P_AUX·S_MULT+1` (`critical/nodes/corridor_ledger/verify_corridor_literal_prime.py:22-26`), 256 bits, `q ≡ 1 mod 1024`, `q &gt; 253^32` — already free by the PROVED high-field theorem, so I ran it as an independent check *of* that theorem.

---

## 3. D2 — VALIDATION GATES (all PASS before any dim-64 result)

- **G1** (`gates.py`) — verdicts match round-22 on all six boundary cells; witness **sets** equal exhaustive brute force; DETCHECK/MEMBERCHECK pass. (Restated per amendment A2 after CATCH-23A: brute force adjudicates, not round-22's counts.)
- **G2** — C-4 anchor replayed verbatim: 576 cyclotomic (= 288 up to sign), **0** non-cyclotomic.
- **G3** — enumerator vs exhaustive box sweep at all six cells, both verdicts: identical sets.
- **G4** — for every reported cell: `|det B| = p` exactly and every basis row in Λ_p.
- **G5** — `PLANT-C` fail-closed control: 8/8 at h=4,8; **and at full dimension** (`PLANT-64`: h=64, det = p = 2^249, R=16, same code path) the planted box vector was **FOUND** — 61,514,718 nodes, exactly {v, −v}. Reproducible from the registered seed alone with zero library imports (`witness_repro.py`).
- **G6** (added, amendment A1) — shard equivalence: 6 cells × 5 (nshard, sdepth) configurations, **sum of shard FPNODES = single-process FPNODES exactly** and **union of FPFOUND = single-process FPFOUND exactly**, 30/30 PASS.

---

## 4. D3 — THE RUN

Machinery: exact integer LLL (Cohen 2.6.7 integral Gram–Schmidt, δ escalated 3/4 → 99/100) + a **scaled-integer** Fincke–Pohst with an explicit fail-closed rounding lemma (S = 2^128; runtime assertions q[i] ≥ 2^48, |x| ≤ 2^40, ‖b*ᵢ‖² ≤ 2^80 bound the total deviation by 2^−32 &lt; 1, so the enumeration is a provable **superset**; every leaf is re-checked in exact integers, so no false positives). Checkpointed to `state/` with a 235 s self-imposed soft wall under the 300 s `ramguard local` wall — I never raised `RAMGUARD_TIMEOUT`.

| cell | log₂p | RHF | FPEST | **FPNODES measured** | CPU-s | verdict |
|---|---|---|---|---|---|---|
| **E1-128** (pinned) | 249.000 | 1.02363 | 2^30.88 | **2,061,127,954** = 2^30.941 | 23,080 | **CERTIFIED EMPTY** |
| CORRIDOR-128 | 255.900 | 1.01977 | 2^25.10 | 37,383,728 = 2^25.156 | 289 | CERTIFIED EMPTY |
| CORRIDOR-128-CONJ (root ρ³) | 255.900 | 1.02123 | 2^24.27 | 20,978,542 = 2^24.322 | 140 | CERTIFIED EMPTY |
| PLANT-64 (control) | 249.000 | 0.99681 | 2^25.82 | 61,514,718 | 392 | **NONEMPTY(2) = {v,−v}** ✔ |

E1-128 detail: LLLSWAPS 13,912 in 1.6 s; ‖b₀‖²=4172; min over the reduced basis ‖bᵢ‖² = 2736 ≫ R²=256; GH λ₁ = 28.711; 12 shards, 12/12 finished, **1 distinct basis across all shard certificates**. Independently re-verified by `verify_cert.py` (retypes the literal constants, re-derives ρ's order, checks membership, and recomputes |det B| = p by a separate Bareiss determinant — hence L(B) = Λ_p since index = p/p = 1): **ALL STRUCTURAL CHECKS PASS**.

The CORRIDOR pair is a genuine cross-check: `integer_code_distance_high_field_folded_box_exclusion` (PROVED, `statement.md:14-25`) predicts EMPTY there, and two independent enumerations at two Galois-conjugate roots and two different bases both returned EMPTY. Root-independence is also proved outright (`symmetry.py`): τ_s: x↦x^s is a **signed permutation** of Z^h, so it preserves the box and maps Λ_{p,ρ} to Λ_{p,ρ^{s⁻¹}} — the verdict is the same for every primitive 128th root. Verified computationally over all primitive roots at h=4,8 and on 2400 random vectors at h=4,8,64.

### Radius-graded certificates at the four LITERAL deployed prize primes

The archimedean norm bound gives |Norm(w)| ≤ ‖w‖₁^64, so the **free radius is exactly L = 6 at all four Proth rows** (6^64 = 2^165.44 &lt; p ≤ 7^64) — precisely the C-4 anchor's radius. Everything below is beyond what any norm bound can give:

| row | log₂p | L=20 (10 swaps) | **L=24 (12 swaps)** |
|---|---|---|---|
| 1/2 | 166.503 | EMPTY, 33,194,432 | **EMPTY, 195,584,948** |
| 1/4 | 168.139 | EMPTY, 11,154,282 | **EMPTY, 58,961,000** |
| 1/8 | 169.389 | EMPTY, 111,066,284 | **EMPTY, 699,304,056** |
| 1/16 | 170.503 | EMPTY, 66,531,196 | **EMPTY, 426,841,390** |

(plus row 1/2 at L=6, 12, 16.) All four verify standalone. **L = 24 is 12 swaps — the radius named verbatim** in `critical/nodes/lattice_cone_certificate/statement.md:13`: *"weight-graded MITM (provable radius extension 7 -&gt; ~12 swaps per row)"*.

---

## 5. D4 — THE HONEST LEDGER

**Certified (complete enumerations, all controls passed):** E1-128 full box; corridor prime + conjugate; four deployed Proth rows at support ≤ 24.

**Attempted, not finished (exact state, no extrapolated verdict):** `PROTH-1over2` at **full radius** — 190,889,984 nodes, DFS at level 36, 1172 s, then stopped. That is 2^27.5 of a projected 2^59.99. Also an abandoned 246,022,144-node unsharded E1-128 partial (superseded by the fresh sharded run, not merged into it).

**Out of reach, with exact prices** (`FPPRICE`, round-22's GSA model):

| row | h | 2ℓ' | LLL | BKZ-45 | BKZ-90 | CLASSHEUR |
|---|---|---|---|---|---|---|
| PROTH 1/2 … 1/16, full box | 64 | 128 | 2^62.6 … 2^60.4 | 2^45.0 … 2^42.7 | 2^40.3 … 2^38.0 | 2^−17.9 … 2^−21.9 |
| RowC-1/4, prize-1/4 | 128 | 130 | 2^199.3 / 2^196.2 | — | 2^109 / 2^105 | **2^39.0 / 2^33.1** |
| RowC-1/8, prize-1/8 | 128 | 66 | 2^167.2 / 2^164.3 | — | 2^75.3 / 2^72.6 | 2^−32.7 / 2^−38.6 |
| RowC-1/16, prize-1/16 | 256 | 66 | 2^652 / 2^649 | — | 2^284 / 2^281 | **2^35.3 / 2^29.4** |
| E1-256 | 128 | 256 | 2^235 | — | 2^152 | **2^48.2** |

Three findings in that table:

- **PRICE-CLIFF (new).** Round-22 reclassified per-row N'=128 certification as *"laptop-scale, not Modal-scale"* (`lattice_cone_certificate/statement.md:41-49`, at `log2 p ~ 250`). That holds only above ≈ **242 bits** with LLL (`FPPRICE` crosses 2^30 at log₂p = 241.8, 2^40 at 214.5). At the four rows the status ruling itself names (167–171 bits) the *same cell* costs **2^60–2^63 with LLL and still 2^38–2^40 with BKZ-90**. The reclassification is correct at the exhibit prime and false at the deployed ones.
- **GS-FLOOR OBSTRUCTION (new, `gsfloor.py`).** The cheapest conceivable certificate is λ₁ ≥ minᵢ‖b*ᵢ‖. Since Πᵢ‖b*ᵢ‖ = p, minᵢ‖b*ᵢ‖ ≤ p^{1/h} for **every** basis, so this works only if p &gt; (2√h)^h — which equals `(4h)^{h/2}` **exactly**, i.e. the AM-GM norm ceiling. Verified identical at h = 4…256. At h=64 both equal **2^256**, which is exactly the spec's own field cap `|F| &lt; 2^256`. Hence **no admissible N'=128 prize row admits a Gram-Schmidt/λ₁-floor certificate for any basis whatsoever**; better reduction can make the enumeration cheaper but can never replace it. (The PROVED 253^32 branch beats both by 0.544 bits — that sliver is the entire free region.)
- **Four of six deployed clean-anchor rows are EXPECTED NONEMPTY.** PRO_W3 banks ~2^48 for the N'=256 *full* box (`PRO_W3_e1_density.md:26-27`); I reproduce 2^48.2 at the literal pinned prime and claim **no novelty** there. The extension is to the six anchors at their *declared* support bounds: rate-1/4 (2ℓ'=130) and rate-1/16 (h=256) stay expected-nonempty (2^29–2^39), while **rate-1/8 flips to expected-EMPTY** (2^−33/2^−39). So `e1_folded_certificate_manifest_payload`, which demands *"zero nonzero non-cyclotomic folded vectors in each certificate"* (`statement.md:13`), cannot close at its N'=256 entry even in principle.

**What per-row certificates do NOT close.** `critical/nodes/integer_code_distance_cert/statement.md:16-18`:
&gt; `There is no hidden finite registry of official row primes. Closure must therefore be either uniform over every admissible row assigned to this route, or explicitly exhibit-scoped with every downstream claim narrowed to the same field.`

and `status_ruling.md:11-15`:
&gt; `The node may return to PROVED only after a family-uniform theorem covers all rows assigned to this route, or after a literal exhibit certificate is banked with a deterministic checker and every consumer is formally narrowed to that same exhibit.`

My E1-128 run supplies the *literal exhibit certificate with a deterministic checker* half, at the exact pinned field/root. It supplies **none** of: the family-uniform theorem; the narrowing of consumers; the exact cell cardinality vs `B*` (the value-set side, entirely outside my scope). **I make no status flip and no closure claim.**

---

## 6. Registered predictions vs outcomes

| | prediction | outcome |
|---|---|---|
| Q1 | E1-128 certifies EMPTY | **CONFIRMED** (2,061,127,954 nodes, complete) |
| Q2 | FPNODES ∈ [2^14, 2^27.4] | **FALSIFIED** — 2^30.941. Round-22's 2^27.4 assumed δ=1.0219 *and* log₂p=250; the pinned prime is 2^249.000 and my exact integer LLL realises δ=1.02363. The GSA model at the realised δ gives 2^29.81; the measured-profile estimator gives 2^30.88 |
| Q3 | Proth rows EMPTY, ≥2^15 costlier, maybe out of reach | cost **CONFIRMED** (2^29.5 costlier, not 2^15); out-of-reach **CONFIRMED**; EMPTY **CONFIRMED only up to support ≤ 24**, UNRESOLVED at full radius |
| Q4 | all six anchors GHRATIO&gt;1, rate-1/4 CLASSHEUR≫1, all out of reach | **CONFIRMED** (1.050–1.521), plus the unpredicted rate-1/8 flip |
| Q5 | no witness at any h=64 prize/pinned cell | **CONFIRMED** — P6 did not trigger; the only h=64 witnesses were the control's planted pair |
| Q6 | RHF ∈ [1.018, 1.030] | **CONFIRMED** (1.01863–1.02363) |

The measured-profile estimator `FPEST` matched every completed cell to ≤ 0.06 bits (25.10/25.156, 24.27/24.322, 25.82/25.874, 30.88/30.941) — a better-calibrated instrument than the GSA idealisation.

---

## 7. Self-corrections, stated plainly

1. **G1 as registered was wrong and I changed it under evidence** (amendment A2): my pipeline does *not* reproduce round-22's witness counts, because those counts are wrong. I re-gated on brute force. Disclosed in `PREREG.md` §P9, not only here.
2. **Q2 falsified**: I predicted my run would come in *under* the banked price and it came in 3.5 bits over.
3. **Sharding was not pre-registered.** I added it mid-run for parallelism and added gate G6 to justify it. G6 initially **FAILED** (4 of 30 configs) because level 0 is processed by a batched interval intersection inside the level-1 step and so cannot itself be a shard frontier; fixed by forcing `flev ≥ 1`, then 30/30 PASS.
4. **A real concurrency bug, caught fail-closed.** Twelve shards starting a *fresh* cell all ran LLL and raced on one `.tmp` file; two crashed. `merge_shards.py` correctly refused a verdict. Fixed two ways (per-PID temp names; LLL completed single-process before shards launch) and I added a check that all shards enumerated an identical basis. **E1-128 was not affected** — its LLL finished 25 minutes before sharding began, and I verified the merged certificate's basis is byte-identical to the LLL state and to all 12 shard certificates.
5. **Work discarded**: a 246M-node unsharded E1-128 partial (superseded, not merged) and a deep-insertion LLL experiment that reached FPEST 2^29.43 and is **not used** for any reported certificate.
6. **A behaviour-preserving optimisation mid-run** (Python loop → C-level map/sum for the FP centre); gates re-run and returned identical node counts and witness sets.
7. **Prior art subtracted before any claim**: λ₁ &gt; 16 at N'=128 is banked (`PRO_W3_e1_density.md:49`) — I claim only the complete transcript, which the repo itself rules is the missing piece. The ~2^48 N'=256 figure is banked — I reproduce it. The CATCH-1-corrected class heuristic is round-22's — my 2^−100.4 is that figure at the literal pinned prime (round-22 used log₂p=250; it is 249.000).
8. **Quarantine held absolutely.** `notes/pilots_20260802/CAMPAIGN_LEDGER.md` was never opened at all; `cw_shared_target`, `fpc5_diag`, `c2pp_diag` never read. One subagent was dispatched (row-registry search) and carried the quarantine clause verbatim. `sys.dont_write_bytecode` kept round-22's directory untouched (its `__pycache__` mtime is unchanged at 08:05).

**Files** (all under `notes/pilots_20260807/ge_lattice_cert/`): `PREREG.md` (registrations + amendments), `latlib.py`, `cells.py`, `runcell.py`, `gates.py`, `shardtest.py`, `catch_d4cone.py`, `symmetry.py`, `price.py`, `graded.py`, `graded_results.py`, `gsfloor.py`, `facts.py`, `estimate.py`, `summary.py`, `merge_shards.py`, `verify_cert.py`, `witness_repro.py`, `improve.py` (unused), `drive.sh`, `drive_shards.sh`, and `state/` (reduced bases, checkpoints, merged certificates).
