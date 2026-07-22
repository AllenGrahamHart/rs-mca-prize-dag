All numbers below re-verified against `dag.json` at 550f176b before merging (req-closure of `prize` = 279 nodes: 221 PROVED / 35 CONDITIONAL / 23 TARGET; the 23 targets are exactly the 22 red-leaf ids named below + `submission_quality_paper_dossier`; alt edges into the closure confirmed: `rigidity_kernel → gap1_noneq_mass`, `rigidity_kernel → xr_clean_residual_any_gate`, `route_noslack → mca_safe` [REFUTED], `lattice_cone_certificate → certified_valueset_lower` [PROVED, spent]).

# THE GAP MATRIX — what stands between master 550f176b and full resolution of both problems

## 0. Basis, counts, and conflicts between the reports (flagged, not papered over)

Three different node-count measures are in circulation and all are correct for their own scope — do not mix them:
- **Critical surface** (board facts, A2): 208 PROVED / 33 CONDITIONAL / 22 open red leaves.
- **Req-closure of `prize`** (A1, re-verified by me from `dag.json`): 279 nodes = 221/35/23; the closure is strictly larger than the critical surface (16 extra nodes) and its 23rd target is the dossier artifact, exempt from the red-leaf law under RIPE staging.
- **`critical/nodes/` folder census**: 254 dirs (201/32/21) — folders lag the DAG; the DAG is authority.

**Conflict 1 (substantive — resolve in A6's favor).** A1's one-liner for `rate_half_band_closure` ("undetermined band ... equals the first-moment prediction", σ\* = 8,592,912,738) is **stale**: the fixed-crossing-at-σ\* pose was killed in wave-9 (the cyclic count is s-independent; σ₀ = 8,594,128,895 > σ\*+1 is also unsafe; `critical/nodes/rate_half_band_closure/refutation.md`). The residual of record (wave-10 audited) is A6's: (i) the two budget values {2³⁹, 2³⁹+1} where the proved staircase a_RH(q) = n − ⌊q/2¹²⁸⌋ + 1 does not decide the crossing on 2¹²⁸ < q < 2¹⁶⁷, and (ii) the beyond-2¹⁶⁷ regime where a_RH is only bracketed in [k+2³⁴, 3n/4 or n].

**Conflict 2 (cosmetic).** A1's leaf enumeration runs 1–23 with **no leaf 18**; there are exactly 22 red leaves. Node ids, not A1's ordinals, are used below.

**Conflict 3 (scope mismatch).** A2 lists a "Hankel band" among stalled red families. There is **no Hankel leaf** among the 22; the Hankel work is interior machinery of the K5 lane (the far-CA layer inside the band-closure determination). Velocity claims about it do not bear on the leaf count.

**Conflict 4 (RESOLVED 2026-07-21).** The proved
`f1_pole_same_rate_scope_router` checks the actual F1 construction:
`C_K=RS[K,D,kappa]` expands to `C_B^e` with the same `D,kappa`, and every
tower step changes only the coefficient field. Therefore the
`ext_lift ← f1_pole_list_threshold_location ← list_adjacency_closing`
import is rate preserving. Clean ambient rates use clean base-list
thresholds; rate-half adjacency enters only for an ambient rate-half row.
On the current 21-red surface the clean-rate milestone has 19 mathematical
leaves, excluding the two rate-half leaves. The old 20-of-22 count below is
historical drafting arithmetic.

**Refinement, not conflict.** WCL slot (2,7) cost: A2's $6,000–14,300 blind estimate and A6's ~$1,900–5,300 after a GMP/FLINT gcd swap are the same fact at two engineering stages; either way it is CR-004 external-request-only, and it additionally carries an unfixed soundness gap (Norm(u)-saturation's weight-4 exclusion unpaid at order 1024).

---

## 1. The true bottleneck set

**Wired bottlenecks — on every route through our DAG, no alt of any kind, no upstream substitute:**

| Node | Feeds | Why unavoidable |
|---|---|---|
| `l1_mixed_petal_amplification` | BOTH grands (list spine via `imgfib`; MCA via the `ext_lift ← f1_pole_list_threshold_location ← list_adjacency_closing` coupling) | No alt; parent floors already weakened to the minimum consumers accept |
| `ww_row_envelope_clause` | BOTH grands (same coupling) | Same; mean forms proved insufficient, sup form is forced |
| `rate_half_list_adjacent_crossing` | BOTH grands | Sole supply for the rate-1/2 list crossing (B\* ≥ 3 branches) |
| `rate_half_band_closure` | `mca_safe` (rate-1/2 instance) + `adjacency_closing` | Intentionally isolated; its only historical alt (`route_noslack`) is REFUTED; terminal risk of the program |
| `submission_quality_paper_dossier` | `packaging` → `prize` | Artifact-closure by definition |

There is **no MCA-only resolution**: the F1 pole pricing imports the base-row list threshold, so the three list-side leaves are load-bearing for `mca_grand` too.

**Shared mathematical bottlenecks — both sides considered.** The joint program has exactly one deep object and two hard atoms that neither tree can currently reach:
1. **The balance line** — his row-sharp Q atom (`def:q-row-atom`, GF v3 input 1) ≡ our F6/K5 `rate_half_band_closure` at our coordinates (REGIME_MAP proves same object, disjoint regimes: his crossings at Δ = +21…+67 bits of 2.09M, his theorems deep above balance). His own memo: per-term character/monodromy methods fall ≈ 2.4·10⁷ bits short at band depth ~6.7·10⁴; the M31 list row allows only ≤ 8.4152× overhead. Our side: the witness-hunt THEOREM CAP (char-0 supply plateau C(127,64) = 2^123.17 vs need 2^127.90–2^128.00, a 4.73–4.83-bit deficit across all 2,978,146 band cells). Neither side closes this within days; he says so explicitly, our cap theorem says so for us.
2. **The deep Sidon/Fourier payment** — his input 3 ≡ our F2 summit (`f2_growing_order_myerson`). Both trees have fenced every classical route (his: entropy demoted to guide; ours: no-go #9 — the analytic lane is vacuous at official fields, n ≪ √q).
3. **Sup-form anti-concentration** — `xr_lowcore_spread_heart` (P-B) on our side; his first-match atlas residual is converging on the same cells. Unlike 1–2, this one is bypassable (RK alt, or a direct `xr_smallcore_spread_count` floor proof), so it is a hard atom but not a strict bottleneck.

The bits-level bottom line: full resolution requires the four wired bottleneck leaves + closing either the 15-leaf strip subtree + XR pair **or** the RK conjecture — and nothing upstream will do any of that for us (his "not within days, by his own quantified admissions" list covers row-sharp Q, deep Sidon/Fourier, exact extension multiplicities, and all four summed certificates).

---

## 2. Per-family gap matrix

Format: **Residual | Grade | Evidence | Upstream overlap (will he close it? duplication?) | Banked machinery that applies**.

### 2.1 DLI lane — 12 leaves (`dli_c1r3_gated_envelope_bound`, `dli_c2pp_joint_reserve`, `dli_wcl_slot_{1_5,1_6,1_7,1_8,2_7,2_8,2_9,4_9,4_10,4_11}_emptiness`)
Amber of record (Decision 6): `dli_prime_weighted_large_block_support` CONDITIONAL on C2″ + baseline(C1′-r3 + WCL-ZONE-ext); B-WEAK 2¹²¹ headroom chain (E_j ≤ 41/8, 41³⁴ < 2²⁰² unchanged by the L+5→L+7 window widening). Sole exit: one req edge into `x4_exactlist_staircase_split` (19 of whose 22 reqs are proved). Widest family by leaf count (12/22), narrowest by interface.
- **c1r3**: E−1 ≤ 4r(1+W_ext) on rows with v₂(q−1) ≥ 41, w_max = L+7; twice-survived (complete 1.95·10⁹ census, worst K′ = 1.401644, 2.85× margin, envelope saturating [1.33, 1.40]; killer row 918552577 repriced 3.000058 → 1.333359 by its w6 orbit — the extension working exactly as designed). Pinned worst-row rationals 1058880560632659/1033540934303744 and 35507502101438673/25332747971067904. Grade: **compute-watch with a proof-shaped endgame** (nothing structural forces the 4-allowance). Next: gated-L=2 round-3 lever (time-rule-sized).
- **c2pp**: X(R) ≤ 2²¹·A(R), no factorization asserted; two F-rounds survived, round 2 = 14.53% of the 21-bit reserve (~85% margin), clause-(ii) bulk empirically ≡ 1 (< 10⁻³), signal = exact coset column + orbit-quantized accidents. Grade: **proof-shaped-tractable** — pose the "bulk = 1 + accident column" identity as a lemma; round 3 (F-a t=4 + 40-row F-c) pre-registered.
- **10 WCL slots**: finite zero-event statements; precedent closes (2,5) via norm-gcd (1,514 orbits, 168 Pocklington primes) and (2,6) via recursive-norm certificate (404,740 orbits, 443 prime roots, both max v₂ = 18 ≪ 41). Shape splits: **(1,5) compute** (46.44% done, 1,066,688 rows banked, $45–60 to finish, two known repairs: re-shard aggregation + ECM tail); **(1,6)–(1,8) compute-in-principle** (unpriced); **(2,7)–(2,9) proof-shaped as posed** (94,652,815-orbit census = 233.9× the (2,6) job, CR-004 no-go, plus the Norm(u) soundness gap); **(4,9)–(4,11) proof-shaped** (never sized; route = CR-004 unit-ideal endpoint certificates).
- **Upstream**: no analogue — this is our own band-depth flatness machinery on the shared balance-line frontier. He will not close it; no duplication. His head-depth row-sharp-Q witness lists (w ≤ 21–22 KB, w ≤ 10–11 M31) are calibration data.
- **Machinery**: Proth in-gate censuses + Burnside orbit model (94,652,815 predicted, validated ×3); w ≤ 7 accident-orbit repricing ledger; vendored (1,5) streaming/checkpoint stack; norm-gcd/Pocklington + recursive-norm templates; CR-004 unit-ideal idea (start: the three-variable (1,5) ideal — a land there retires Job A's $50 AND converts every slot from census to certificate).

### 2.2 F2 — `f2_growing_order_myerson` (1 leaf)
- **Residual**: Myerson at growing subgroup order (tower needs f ~ p^0.77+); honest form = 2^{o(n)} parity alignment of ε_c = (−1)^{K+U} against exp(S_c), one step past Borda–Munsch–Shparlinski 2024. Tolerance 2^{1.05e12}; per-condition extras ≤ 2¹⁵. 30 PROVED satellites, 12 no-gos; measured deviations 45–105 nats vs a 10-nat budget for the absolute route.
- **Grade**: **wall-adjacent — THE wall.** Cascade if closed: flips `f2_conditional_close` + `u2c_giant_tnull_dichotomy` (2 ambers), x4's second req.
- **Upstream**: ≡ his deep Sidon/Fourier atom (GF `thm:v3-package`(iii)). He will NOT close it; both programs are stalled at the same atom — not duplication, a shared wall. Coordination = exchange fences (our no-go #9 and signed-cancellation probes; his shallow-Fourier rigorous range + entropy demotion).
- **Machinery**: brief v4 handoff (`PRO_FLOOR_2_F2_SUMMIT_V4.md`); only in-house surface = the j: 0→1, n = 2²⁵, q = p² parity model theatre.

### 2.3 F3-h3 — `f3_h3_dsp8_correlation_bound` (1 leaf; C36 amber `f3_h3_mobius_excess_half` with `f3_h3_official_order_template_survivor` as ev reserve)
- **Residual**: an unconditional bound on 10K₂₅⁰+17K₂₅ᴬ (menu: DSP8 / DSP8-U 160(10K⁰+17Kᴬ) ≤ 76599n² / a JDP corner / 680M₂₁ ≤ 76599n² / any one of 5 accident-depth rectangles). Sharpest fact: F-round 1 survived **vacuously** over 48,544 rows — richness saturates at P = 20; a **max-P ≤ 24 theorem** (currently sampled only) makes DSP8 vacuously true and closes C36′. Parity supersession landed (w18-C1 ratified: allowance 234697/48960, endpoint (36,1)). Two method fences: nodal Stepanov (one-poly floor 2^{5/3} vs G = 4K), F_769 decoration discount.
- **Grade**: **proof-shaped-tractable** (best single-leaf cascade on the board: flips 3 ambers → `f3_h3_direct_floor_conditional_close`, R₃ < n³ exact). Survivor reserve: compute-shaped (CR-001, (36,1) row, 73,602 resultants; reserve-first close = forced re-wire).
- **Upstream**: none. He will not close it; no duplication.
- **Machinery**: coupled-ideal sieve / collision-norm templates (broad scans now vacuous by construction); accident-depth rectangle compiler; Modal time-rule screens.

### 2.4 F3-hge4 — `f3_hge4_norm_gate_count` (1 leaf, ERT4′′′′)
- **Residual**: per level m = 2^r ≥ 16, p ≡ 1 mod m, p > m²: Σ_{h=4}^{m/4−1} E_h^prim(m,p) ≤ (21/2)m², plus the deeper free/swap zones (swap dies only to h ~ (m/4)(1−2/s)). Width window proved down twice (2m/7 → m/4−1, cyclotomic quarter-width exclusion; Vandermonde-defect cubically sharpened, d to 2,677,220,820 at m = 2⁴¹). Fan-in 0→22 in three waves — highest derivative on the board.
- **Grade**: **proof-shaped-tractable** — empirical deep-aggregate mass is literally 0 on every scanned cell; what's missing is an aggregation lemma (per-level bounds must average O(m)), not a phenomenon.
- **Upstream**: his **Q ⇒ SP** pillar (row-sharp Q discharges the primitive shift-pair ledger) is adjacent to our SP_h^prim ≤ 7000n·max(1,B_h) adapter — a vendoring lead, not a closure: Q itself is his hardest atom.
- **Machinery**: amortized free/swap pairing over the lower quarter; complete n=32 full-corridor row census as pre-registered falsifier bed; the DSP8 moment compiler (untried transport). **Standing hazards pinned in-statement**: catch #99 (A5 re-open clause kills the gate — shallow mass crosses 14n³ near h~12 without the F-4 minimality pin) and catch #100 (two of five strips undefined in-repo; any KILL claim must define them first).

### 2.5 XR pair — `xr_highcore_collision_count` (P-A), `xr_lowcore_spread_heart` (P-B) (2 leaves)
- **Residual**: P-A has two exact clauses. P-A1 is the generic coherent GRS4 split-pencil census + rank-2 chart first-match audit + (u ≤ 60, v ≤ 7) pairs, within 8n³/pair; first-open selector ranks are **5,5,5 (RowC) / 17,17,15 (prize)**. P-A2 is the former combined nongeneric mismatch count within 16n³; support-local LineRay payment leaves first-open ranks **5,4,4,4,4,4**, and its full-zero descent has caps 169/169/255/254/254/510. P-B retains its generic low-core `8n^3` scope, same rank frontier, sup-over-pairs quantifier, and evidence only at FM = Θ(1)..107. The bridge is PROVED as the exact generic `(P-A1+P-B)` / nongeneric `P-A2` case split. P-A has **no umbrella verify.py** (its clause verifiers are separate) — harness gap.
- **Boolean-energy reduction:** every P-B oriented-difference fiber with `t>=K` has multiplicity one; only `h+1<=t<=K-1` can repeat. Full-side puncturing turns each repeated fiber into two smaller generic RS-line instances and pays `t=K-1,K-2` per fiber. Cross-difference aggregation remains open. This is not CAP25's local locator-SPI currency and not a slope count.
- **Grade**: P-A tractable, **P-B proof-shaped-hard** (no averaging can meet a sup; named surface = `f2_effective_energy_dichotomy` transport).
- **Upstream**: **the one real duplication-risk zone.** His first-match atlas (GF input 2) and the scottdhughes M31 route-cut wave (#999–#1008: ADE wall, Chebyshev separator, Plücker defect window, rank-46 Forney frame, padding bridge) are converging on the same residual cells as our xr emptiness slots; A3 flags "first-match atlas completion on one M31 row" as the first genuine closure risk/opportunity in either tree. Action: vendor his cut library into our chart/atlas coordinates BEFORE running our own census, and keep our paused M5 singular pivot packet (his towards-prize §8 ask) in the exchange.
- **Machinery**: covering-free AZC (margin 0.5005%, w8-C9 re-run obligation), rank-five suite, triple-implementation strip ledger, GRS4 census (named, bounded, unrun).

### 2.6 List L1 — `l1_mixed_petal_amplification` (1 leaf)
- **Residual** (post wave-15 31-rung ladder): four branches red — (1) growing-p; (2) balanced sub-Johnson strip with e, a, c all unbounded; (3) growing signed layout/core polarity; (4) canonical first-match supply for non-intrinsic charts — with a PROVED obstruction on the natural route (`l1_cross_quotient_split_descent_obstruction`: explicit F₂₃ cell, nonsquare discriminant, kills naive cross-quotient descent). Known mass small (43 mixed vs 10 full-petal at (16,8,97)); **stalled: zero movement waves 16–18**.
- **Grade**: **proof-shaped-hard** (barrier theorem on the route; three unbounded parameters; this is where the 2026-07-05 induction died).
- **Upstream**: residue of his `ass:locator` (our #750 correction posted); his planted lower count feeds `imgfib` as ev; his open "arbitrary-word list-interior theorem" is the nearest atom but does not substitute. He will not close it.
- **Machinery**: cheap pre-registered growth-law measurement of the balanced strip (arms a falsifier OR licenses floor-band-emptiness à la clause (P)); branch (4) is the constructive parallel lane; one guarded survivor atom LS6.

### 2.7 List WW — `ww_row_envelope_clause` (1 leaf, W3/R1′)
- **Residual**: per official row, per received word U (SUP form, never averaged — mean form dead: adversarial layout-sup 2.417× median = 1.263 bits > the 0.9-bit line; q^σ normalization refuted by the 24/24 census): Σ_c N_chal^o(U,c) ≤ B_chal(U) with B\* = ⌊q_line/2¹²⁸⌋, minimum-#493 branch baked in, per-row independently checkable certificates (R2 binding verbatim).
- **Grade**: **proof-shaped-tractable — and the only red that has never absorbed a falsification round.** Headroom 27.0/60.6+ bits; outer cap B < 1.5.
- **Upstream**: his |B|-normalization guard is an ev edge here; otherwise ours alone.
- **Machinery**: the never-run F-round-1 official-convention cell sweep (bg ≤ 1, σ ≥ 1; Modal, time-rule sized) — the single cheapest information purchase on the board; then the banked codimension-drop vs new-component dichotomy with the sweep's worst cells as test bed.

### 2.8 K5 MCA — `rate_half_band_closure` (1 leaf)
- **Residual** (of record, per Conflict 1): (i) the {2³⁹, 2³⁹+1} budget seam of the otherwise-complete 2¹²⁸ < q < 2¹⁶⁷ determination; (ii) the beyond-2¹⁶⁷ bracket [k+2³⁴, 3n/4 or n], theorem-capped (4.73–4.83-bit supply deficit across all 2,978,146 band cells; seven mechanisms triaged dead; only unfenced flank = non-polynomial received words, uncensused).
- **Grade**: seam **tractable**; bracket **wall-adjacent** (the "cancellation" barrier flavor; terminal program risk).
- **Upstream**: same object as his row-sharp Q, **zero regime overlap, zero contradiction** (REGIME_MAP). He is provably far away (2.4·10⁷-bit character shortfall). Our four-pair replay (#1010) and his cor:prize-window-compiler (which consumed and superseded our n=2⁴¹ determinations at all four rates, M_ρ(2⁴¹) = 389,500,552,609) are deliberate, audit-valuable duplication.
- **Machinery**: the seam is a uniform Hankel split-pencil theorem, with exact binomial ladder (#115) available only for final adjacent-row arithmetic; hardened-floor evidence (+1..+4 survivals, 18/18 crossing fidelity, Poisson anti-concentration); sporadic escape hatch priced ~2^−5.2/razor row. Next: the seam first through the branch-exact attack contract and CR-003 algebraic routers, then a dedicated non-polynomial-word census. A finite no-hit analogue is not a seam proof.

### 2.9 K5 list — `rate_half_list_adjacent_crossing` (1 leaf)
- **Residual**: B\* ∈ {1,2} COMPLETE (all-arity, a_L = 3n/4). B\* ≥ 3: bracket [k+2³⁴, a_IJ] byte-identical for four waves; witness route reduced to **exactly 13 chambers** (9 split-unit Grassmann-line, degrees {3,4,5,6,8} + 4 balanced scrolls; rank-deficient branch EMPTY), **0/13 closed, 13/13 reduced** (Stepanov cap #Y_a ≤ 355,106,851 < 2²⁹ on all official fields; one-antipodal ladder; harmonic census 0/4,495,441). Nonclaim intact.
- **Grade**: **proof-shaped-tractable, strategically low-yield** (a full 13-chamber close moves the safe endpoint exactly one step and does not collapse the bracket).
- **Upstream**: his M31 scalar-descent (#993) vendored as ev (`list_support_distance_scalar_descent`); his M31 list row is the binding case of his hardest atom — he needs exact extremality at 3.1 bits and cannot reach it either.
- **Machinery**: port the WCL norm-gcd/Pocklington template to the degree-3 chamber (unique cubic candidate at the maximal row already pinned: 7 | 5·2⁴¹+1); candidate unified gate: chamber emptiness at v₂(q−1) ≥ 41.

### 2.10 Artifact — `submission_quality_paper_dossier` + `packaging` amber
- **Residual**: clerical by definition (total certified f(C) compiler, clean-checkout replay, provenance, empty nonclaim ledger). Maintainer signal: **target Paper D's certificate grammar directly**, GF v3's six-input checklist is the promoted frame. Standing engineering debt: KB #107 lightweight-cert verify.py fix; xr_highcore verify.py gap.
- **Next**: the Paper-D/GF-v3 grammar crosswalk (which of his (F1)–(F4) obligations our compiler already emits, which need adapters — his `four_row_exact_completion_compiler_v1.json` schema landed in 18cfc199 and is the diff target).

**Meta-datum spanning the original A2 window**: four waves, +195 nodes, +709 edges, zero red closures. The current scope-contraction pass subsequently closes the standalone XR mismatch bridge without proving a numerical predicate; its combined count is preserved verbatim as P-A2. The gap between "residual named and finite" and "residual closed" remains the program's dominant cost.

---

## 3. Minimal win set analysis

**Wired minimum (the only unconditional answer):** the current req-leaf set printed by `tools/verify_prize_dag.py`, plus the dossier artifact. The critical surface is pure AND (req-only; gates normalized 2026-07-06). The historical sketch set {R2, zone-(b), S0} has fully dissolved (S0 PROVED; zone-(b) normalized away; R2 compiled into the XR pair).

**Cheapest strict sub-goals, in ascending cost:**
1. **`list_grand` alone = 3 leaves**: {`l1_mixed_petal_amplification`, `ww_row_envelope_clause`, `rate_half_list_adjacent_crossing`} — flips 8 ambers, closes one grand outright, and unlocks `ext_lift` for the MCA side for free. Note the grade mix: one tractable-never-tested (ww), one tractable-low-yield-13-chambers (leaf 20 — the bracket suffices only if the chambers close or the crossing is otherwise located), one hard (l1).
2. **Clean-rate milestone (M2/M3-grade)**: every current mathematical leaf
   except the two rate-half leaves; Conflict-4 is resolved by the same-rate F1
   pole router.
3. **Full resolution**: the complete validator-printed req-leaf set plus the
   dossier.

**Alternatives (route surgery, mathematically legitimate):**
- **RK shortcut** (`rigidity_kernel`, CONJECTURE, alt edges verified into `gap1_noneq_mass` and `xr_clean_residual_any_gate`): collapses the win set to **{RK, l1_mixed_petal, ww_row_envelope, rate_half_band_closure, rate_half_list_adjacent_crossing} + dossier** by pruning the 15 strip-side leaves and XR pair. Only recorded single-statement prune; schema-broad and unproved. All other alts dead or spent (`route_noslack` REFUTED, `conj_f` already PROVED, `lattice_cone_certificate` already consumed).
- **Direct floor-conjecture proofs** (the five 2026-07-07 floor re-poses): a direct proof of `dli_prime_weighted_large_block_support` (B-WEAK) prunes all 12 DLI leaves; of `u1_x4_direct_column_budget` prunes both F3 leaves; of `u2c_giant_tnull_dichotomy` prunes the F2 leaf; of `xr_smallcore_spread_count` prunes P-A + P-B (the scope bridge is already proved); of `worst_word_challenger_pricing` prunes ww. These are status-flip surgery under DAG law but honest bypasses mathematically.
- **Within-route cheap closes ranked by cascade**: DSP8 via the max-P ≤ 24 richness lemma (flips 3 ambers), F2 Myerson (2 ambers — but it's the wall), XR pair jointly, DLI dozen jointly (4 ambers through x4's slot, with `gap1_product_model` above already half-proved, #212 in flight).

**Irreducible core under every wiring**: {l1, ww, leaf-20 crossing, band-closure} + dossier appear in every sufficient set, including the RK world. Those four are where scarce proof effort has no substitute.

---

## 4. Risk register — what can DEMOTE, and the price

| Trigger (pre-registered) | Fires when | Immediate demotion | Cost |
|---|---|---|---|
| **c1r3 amber-2 watch** (K′_r3 ≥ 2; literal-4 kill at ≥ 4; iid-excess trend) | Round-3 census (octave-31 — needs compute-law amendment for 4 rows; gated L=2; full-ledger lever) finds K′ ≥ 2 (current worst 1.401644, 2.85× margin) | `dli_c1r3_gated_envelope_bound` dies → `dli_marginal_baseline100_coverage` → dli back to RED | Third envelope pose dead in a row (r2 T-KILLed at q = 63361, K′ = 6.199); only exits become the per-orbit mass theorem or B-WEAK direct/RK; entire strip subtree re-stalls behind x4 |
| **C2″ F-round 3** (F-a third-depth t = 4; 40+-row F-c census) | Bulk ratio or accident charge breaks the 2²¹ reserve (round 2 used 14.53%) | `dli_c2pp_joint_reserve` refuted → dli RED | C-series moves to a fourth pose; Decision 6 reversed; the coset-column + quantized-accident mechanism data survives as the re-pose seed |
| **Any WCL slot falsifier** (one admissible row + one vanishing polynomial, per slot) | Most exposed: (1,5) remaining 53.56% of Job A; extended slots (1,7)(1,8)(2,8)(2,9)(4,10)(4,11) are least-evidenced (minted by the window widening, never scanned) | That slot refuted → `dli_wcl_zone_coverage` fails at that ℓ → baseline A(R) ≤ (41/8)³⁴ < 2¹⁰⁰ dies → dli RED | Severity depends on measured mass: a single thin accident might be absorbable by a budget re-pose (41/8 has 2²⁰² vs 2¹⁰⁰ slack in the chain); a structural family kills the zone decomposition outright |
| **C36 satellite falsifier**: any official row with P ≥ 21 | DSP8 round-2 coupled-ideal/collision-norm scans | Kills the max-P ≤ 24 vacuous-close route (does NOT refute DSP8 itself unless P ≥ 25 mass appears) | Lose the cheap close; fall back to the 5-rectangle exclusions or the CR-001 (36,1) survivor row (reserve-first close forces a re-wire) |
| **Catch #99 A5 re-open clause** (HGE4) | Any challenge to F-4 minimality pinning | The un-pinned shallow mass crosses 14n³ near h ~ 12 → `f3_hge4_norm_gate_count` false-as-posed | F3-hge4 re-architecture; `u1_x4_direct_column_budget` loses its second leg. Companion tripwire: catch #100 — any KILL claim must first define the two undefined strips |
| **w8-C9 AZC obligation** (XR) | Any re-pin of (h, R, 8n³) without re-running the covering-free AZC (margin 0.5005%) | Unsound close of the RowC-1/16 line-free sub-case | Process tripwire; margin is razor-thin, so a constant drift can silently flip it |
| **P-A/P-B floor falsifiers** (transported sustained overshoot; FM-band-consistent counts explicitly do NOT refute) | GRS4 census or rank-2 audit surfaces overshoot | `xr_smallcore_spread_count` floor demotes | `r2_clean_rates` chain stalls; RK alt becomes the only aperiodic route |
| **WW F-round 1** (never run) | The cell sweep finds a word violating the sup allocation | R1′ demotes before ever being amber | Cheapest possible time to learn this; the 27+ bit headroom suggests survival, but the sup form is untested — this is why the sweep should run FIRST |
| **L1 growth-law round** | Balanced-strip mixed mass trends above n^B | Branch (2) gets a live falsifier | Confirms proof-shaped-hard grade; pushes weight to branch (4) constructive lane / floor-band-emptiness argument |
| **Non-polynomial word hunt** (K5 bracket) | A supply witness outside the fiber reduction | The F6 band floor demotes | Terminal-risk event for the program's safe-side strategy; no fallback is recorded |
| **Packaging w10-C1** | Grammar drift vs Paper D / GF v3 while waves land; three auto-discharge attempts already refused | — | Endgame scramble instead of a diff; mitigated by the crosswalk in §2.10 |
| **Custody-class process risks** | w18-C1-style negative-marker supersessions; GC-vulnerable dangling checkpoint commits (the Pilot-A 8,300× surprise) | — | Now systematized (maintainer ratification path; checkpoint rescue), but each recurrence costs a queue-walk |

Portfolio note: **12 of 22 leaves and 3 of the 5 named demotion triggers sit in one lane (dli)**. The lane's single-edge interface into x4 caps the wiring damage, but a dli demotion is the single event that most re-opens the board — which is exactly why B-WEAK-direct and RK retain option value even while the 12-leaf route is live.

---

## 5. Convergence plan inputs

**Vendor FROM upstream (he has it; we should import, not re-derive):**
1. The **M31 first-match route-cut library** (#999–#1008: ADE wall, Chebyshev separator, Plücker defect window, rank-46 Forney frame, padding bridge) → translate into our xr chart/atlas coordinates before running the GRS4 census — this is the one active duplication-risk zone (§2.5).
2. `four_row_exact_completion_compiler_v1.json` + candidate schema (18cfc199) → the packaging grammar crosswalk target (§2.10).
3. The **Q ⇒ SP discharge compiler** → candidate transport for HGE4's SP_h^prim adapter routes.
4. His **negative library as fences**: `prop:proper-q-gap`, `prop:q-moment-order-floor` (Johnson packing / fixed low moments cannot close row-sharp Q), the `kb_rowsharp_route_d_*_no_go` Lean packages, `prop:bc-not-q` — import as route-cuts on our K5/dli lanes so we never spend on his proved-dead routes.
5. His head-depth **row-sharp-Q witness lists** (w ≤ 21–22 KB, w ≤ 10–11 M31, Weil range) as calibration rows for dli/WCL.
6. The **latifkasuli Lean falsity-certificate pattern** for machine-checking our floor falsifiers (matches our pre-registered-falsifier governance exactly).
7. Already vendored, keep current: scalar_descent (#993 → `list_support_distance_scalar_descent` ev), prefix rigidity, second-moment shift-pair identity, saturation identity, |B|-normalization guard, moving-root BC theorem (all replayed/ev on our board).

**Feed TO upstream (we have it; he needs it):**
1. **PR #1010** (four-pair exact replay = the audit half of his F4 obligation) and **PR #1013** (quotient-cell super-polynomial prefix fiber + budget-3 split-pencil census = direct SS0.5 falsifier-boundary calibration; proves his primitivity hypothesis is load-bearing) — both open; his triage pattern is ~24h, chase them.
2. The **near-rational support-wise counterexample** (exact rate-half μ₈ ⊂ F₁₇) refuting a v13.2 dichotomy corollary — a live correction to his promoted cap authority; surfacing it is obligatory under our own correspondence hygiene and buys standing.
3. The **f1 extension classification lane** (`f1_classification`/`f1_case_pole`/`ext_lift`) — his agents.md F1 target ("extension-line MCA theorem or counterexample") is literally our lane; feed the classification skeleton so his input 5 (exact extension/quotient multiplicity payments) builds on it rather than in parallel.
4. The **M5 singular-bucket pivot packet** (PR #172 lineage) — his towards-prize §8 ask, still paused on our side.
5. **Fences he lacks**: the F₂₃ cross-quotient descent obstruction + Linnik-floor no-gos (bearing on his `ass:locator` residue, #750 thread); our Stepanov cap #Y_a < 2²⁹ + one-antipodal ladder (bearing on his open arbitrary-word list-interior atom); F2 no-go #9 (analytic lane vacuous at official fields) for his Sidon/Fourier bookkeeping.
6. Continued **finite determinations** — his thresholds paper already consumed our n = 2⁴¹ rate-half rows at all four rates; the determination pipeline is our proven export channel.

**Only we can (or will) do:**
- The **four wired bottleneck leaves** (l1, ww, both rate-half leaves): no upstream analogue closes any of them, and his own quantified admissions rule out his four summed certificates near-term (M31 rows need exact extremality at 3.1–3.3 bits that no tool in either tree reaches).
- The **adversarial floor discipline**: 7 hardened floors, 21 attack families, 0 deaths, pre-registered falsifiers and demotion criteria — his tree has no equivalent governance layer; it is what makes our ambers creditable.
- **Counterexample production and independent exact replay** (his ev-integration commits state no local replay is ever run — our replays are the only verification his structural theorems get).
- The **dli band-depth flatness machinery** (the entire 12-leaf finite decomposition, censuses, and certificates) — our sole-custody route onto the shared balance line from below.
- **Compute-certificate custody** (checkpoint rescue, coverage-certificate screens, the TIME RULE) — the Pilot-A incident shows nobody else preserves this state.

**Division-of-labor verdict**: he owns the unsafe-side exact frontier, asymptotic formalism, Lean statement layer, and publication (including pay-per-bit partial-credit positioning — Paper D's ε_mca > 2^−86 is 42 bits above target); we own floors, falsifiers, counterexamples, replays, f1, and the list side. The shared frontier is one object — the balance line — and on it, expect his tree to keep shrinking-and-hardening without closing, with the single near-term collision point being first-match atlas completion on an M31 row, where the vendoring in item 1 above converts a race into a merge.
