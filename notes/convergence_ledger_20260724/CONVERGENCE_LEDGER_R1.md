# Convergence Ledger r1 — the co-finish program (2026-07-24)

> **PROCEDURE POINTER:** This dated ranked inventory is executed under
> `notes/JOINT_PRIZE_RESOLUTION_PROTOCOL.md`. In particular, local
> mathematical status and upstream acceptance are separate axes; the joint
> key is required for co-completion, not for recognizing a complete local
> proof as `PROVED`.

Basis: ours @ prize master 8a820bdb; upstream @ origin/main b13de811 (read-only). Sources merged: Plan B1 (export+mining, fact-checked, one fatal correction applied), Plan B2 (harvest+joint-graph, six material corrections applied), Critique C3 (all additions C3-1..C3-14 and risks R1–R7 adopted). Every claim below carries the evidence grade its fact-check assigned; nothing fatal-flagged survives.

**Baseline of record — CORRECTED 2026-07-26 (Q0 + E1 and unsafe-crossing false-green audits), machine-pinned by `tools/verify_orbit_census.py`.** The two orbit definitions remain unchanged. The E1 audits removed invalid named-exhibit transport; the unsafe audit then replaced that route-local leaf on the live orbit with the exact universal row-instantiation target. The current counts below supersede the earlier snapshots.

| name | root | closure | census |
|---|---|---|---|
| **MATH ORBIT** | {`mca_grand`, `list_grand`} | req-ancestry + alt-closure | **242 = 180 PROVED / 38 CONDITIONAL / 24 TARGET** |
| **SUBMISSION ORBIT** | `prize` | same | **257 = 192 / 40 / 25** |

The submission orbit is a strict superset: math orbit **+ a 15-node packaging spine** (12 PROVED — `bridge_ledger`, `compiler`, `dossier_partial`, `envelope`, `half_johnson_ca`, `harness`, `ld_bridge`, `ldsw_ld_separation`, `lean_existing`, `lean_tier1`, `mca_from_ca_reduction`, `pinned_row`; 2 CONDITIONAL — `prize` and `packaging` themselves; 1 TARGET — `submission_quality_paper_dossier`). **257 − 242 = 15 is definitional, not drift.**

The math orbit is what `orbit/critical_dag.json`, the radial SVG, the published site, `verify_prize_dag.py`'s partition law, and `verify_critical_harness_coverage.py` all measure; its 24 TARGETs are the roadmap's mathematical leaves. The submission orbit is this ledger's baseline and has 25 TARGETs, the 24 math leaves plus the dossier. **Burn-down of mathematics is measured on the math orbit; the all-green end state is the submission orbit, which owns the dossier leaf.** Every count below must now say which orbit it means.

Upstream terminal open inputs per GF `thm:audited-status` (:7530): **(S)** `prob:mca-spread-routing`, **(A)** `prob:large-owner`, **(E)** `prob:mca-exception-routing`, **list-completion**.

---

## 0. The strategic frame, restated as policy

1. **The DAG is the guiding map — and it must be shared.** The critical DAG remains our single source of truth, and a `critical_orbit_snapshot.md` (nodes, status, req edges, his-label crosswalk column, who's-on-it board) is regenerated per wave and travels **with real packets** — never as a standalone PR (his stop rules class label-maps and schema acceptance as non-progress).
2. **Definition of DONE (all-green, submission orbit):** 25 TARGETs closed (24 math leaves + the dossier) **and** his four terminal inputs closed. The conditional conjunct remains redundant on our side: all 38 mathematical CONDITIONALs discharge by pure gate propagation from the 24 TARGETs (`tools/verify_conditional_propagation.py`, `assumption_dedup.md`), and the other 2 (`prize`, `packaging`) are packaging spine nodes that discharge the same way. So **DONE = the 24 mathematical leaves + the dossier + his four inputs**. No plan item counts as convergence unless it moves that ledger.
3. **Proactive feed + harvest is a cadence, not an episode:** a standing per-session upstream-delta sweep (pin-advance → triage into refutation / harvest / ledger lanes) replaces one-shot harvest lists, which go stale in ten days against his multi-wave weeks.
4. **The progress metric is joint:** every wave reports bits of remaining delta\*-bracket moved, jointly over both trees (roadmap §9). A wave that moves zero joint bits is exchange, not convergence — and two full cycles at zero triggers the self-kill (§7, R7).
5. **The DAG is the Lean module graph:** node → module, namespace = node id, req edge → import, ev edge → no import, gate:all → explicit hypotheses until discharged.

**Burn-down honesty (C3-1):** the exports in §1 close zero of our reds by construction (outbound); the harvests in §4 are almost all ev-wired. Their convergence value is: his four-input checklist coverage, the shared map, the conditional-dedup, the two seam-cleans (E-4/M-1), and the milestone that unlocks O-2. Each item below states what it closes, routes, or merely evidences.

---

## 1. EXPORT NOW — the ranked immediate pipeline

Pacing baseline (pending §7 ratification): ≤2 open PRs, never same lane; airtight stdlib-only fail-closed verifiers with mutation controls; house header, mirror-SHA pin, non-claims section, submission-day A5 registry re-audit on every packet.

**E-1. Literal corridor prime (week 1, effort S; single owner — the B2 Part-3 duplicate is struck).** Fills his printed TODO (v4 `thm:corridor` remark, verified verbatim). Spec, with the load-bearing correction: mint prime q = c·2^41+1, 2^255.9 < q < 2^256, **constrained to floor(q·2⁻¹²⁸) = B\* exactly** — the packet's printed budget; the admissible band has width 2^128, so try several certified large-prime cofactor structures (~10³ candidates, trivial under ramguard tiny). Attach the Pocklington certificate; replay all six GKL24/Hab25 corridor comparisons at exact budget, reproducing the three printed safe radii 1092724518963 / 1415997755216 / 1644686143216 digit-exactly, plus adjacent-failure checks. If the B\* mint fails, fall back to pre-verifying pass/fail equivalence at all six edges ± one grid step before the word "digit-exact" appears anywhere (edges are sharp to 0.01–0.05 bits). Fences: "pins the denominator; strengthens no bound"; **no machinery-novelty claim** — his Paving Proth certificates and the integrated E1 250-bit exhibit are the format anchors. Scoop-exposed (public printed ask): front of queue for that reason. Carries the Lean pilot (§6).

**E-2. Proth-row independent replay audit (week 1, alongside E-1, different lane; effort S).** Fills v4 submission-package item (3) verbatim (:700). Source `mca_quadratic_prize_rows` (PROVED, 32,654-instance verifier in-node). **Precondition:** refresh the stale crosswalk pins (9262f63c-era manuscript labels → v4 labels @ b13de811). The theorem is HIS; we confirm, close nothing. This is the deliberate down-payment on O-2, and per §6 we run the replays ourselves — which simultaneously fixes the S5 status-discipline problem.

**E-3. WCL first-installment theorems (promoted — no serialization).** The register is a negotiated no-triage-cost channel; C3-12 promotes it out of the E-1/E-2 queue. Per-cell packets in his certificate-dir format for the five (2,5)/(2,6)/weight-3/weight-4/Newton-window cells, each stated as the register's printed predicate verbatim. Preconditions from A2: Norm(u) order-1024 fix, gcd benchmark, (1,5) stage-0 repairs. Fully consistent with KB #124's NOT-NOW on the theorem-PR route — this is the register channel.

**E-4. Rate-half exact-threshold remnant (week 2–3; effort M).** Re-cut of `upr_draft_2` with the mandatory subtraction table vs `cor:target`/`thm:official`; our determined-family half is stated as **concordance, not novelty**; fix the claim-(i) self-subtraction. Claims: seam reduction on B_Q < B ≤ 2^39+1; the q ≥ 2^169 bracket; the MDS counterexample fence. The 40-node far-CA Hankel layer stays "on request" (terminal is TARGET — stop-rule violation if exported). M-1's seam close (§3) cleans this packet's honest-residual clause before it ships. Race re-check day-of.

**E-5. L1 m=4,h=3 official emptiness (week 3–4; effort M).** Verified absent upstream; direct hit on agents.md M1's printed gap ("not exhaustive row bounds"). Row-dictionary section mandatory: claim nothing about his n=2^21 deployed rows.

**E-6. Petal clause-(P) closure (week 4+; heaviest fences, last deliberately).** Three-node PROVED chain on the installed 7-cert base; #750 cited by number up front; mixed-petal gap (catch #212) and CONDITIONAL `imgfib` parent declared; bankable-cell progress only, never an L1 closure.

**X-1. Cross-tree identification certificates (C3-8; new, week 2).** The two machine-verified identification chains, **scoped exactly**: F2 ↔ U_Q/K2 via `f2_zero_prefix_q_equivalence` (zero-prefix, level j < char q — the pruned-vs-raw gap named); L1 exact-shell ↔ locator-prefix Q fiber at e=0 only. Stated in his labels, fenced "identifies objects; strengthens no bound." Until this lands, he does not know the walls are shared.

**X-2. Balance-line pincer ledger (C3-10a; week 3).** Exactly which of the 2,978,146 band cells each side's bound covers (our 123.17 bits from below; his ~1.66M-bit packing overhead from above), joint residual stated as a co-owned open problem. Zero overlap, zero contradiction — the observation itself is the export. Also partial-credit posture insurance (roadmap §8).

---

## 2. CONDITIONAL OFFERS

Contract (binding, from his accept/reject record — #1084/#1081 rejected, #1054 accepted): named hypotheses + positive content (payment, route-cut, or counterexample) + workboard binding + deterministic verifier; lives in `experimental/`, never moves endpoints.

- **O-1. C36 conditional proposition** (`f3_h3_mobius_excess_half` ⇐ DSP8), drafted after three integrations land: one displayed inequality, DSP8 leaves as named hypotheses, 7,090-row evidence, falsifier printed. First-paragraph fence: his deployed rows are extension fields, our corridor is prime fields. Offered as *input toward* the GF Sidon/Q ⇒ SP ledger, never as paying it.
- **O-2. Dossier co-ownership** — raised at the E-1 landing (plausibly the first milestone-grade joint artifact), as a proposal, not a PR: we supply the independent adversarial replay lane; co-signed integer certificates; double-keyed flips. The bilateral **attribution ledger** (C3-13) attaches to this same message. Freeze-date/posture stays the maintainer's call.
- **O-3. P-A1/P-A2 scope-contraction methods note** — gated on the grammar crosswalk; no symbol reuse before it.
- **O-4. dli B-WEAK — register channel only.** KB #124's NOT-NOW on the theorem route stands; register update marks the four cheapest cells TESTED-WITH-POWER, "survival evidence, not census subtraction, rough-odd-part blind spot disclosed." The C1′ REFUTED disclosure travels with any dli statement — our self-refutations presented as the credibility asset they are.
- **O-5. F-round pre-registration discipline** exports through O-2 as the proposed joint falsification standard.

---

## 3. THE MINING PROGRAM — standing production lines

**Standing rule (from the fatal fix): every M-1 mint runs a subtraction check against v4 §"Exact affine-line staircases" + `thm:official` before drafting.** The struck E1 (rate-1/4 adjacent family) is the cautionary instance: his `thm:quadratic` + `cor:target` + `thm:official` already print it in strictly wider generality; shipping it would have been exactly the zombie-proposal our own §7 fences exist to prevent.

- **M-1 (TOP): the rate-half seam {2^39, 2^39+1}** via the pre-armed uniform Hankel split-pencil bound (`rate_half_band_closure/attack.md`, roadmap ~:784). One session. The one mining item genuinely beyond `thm:official` (B ≤ 2^39−2), extending the determined window to ~(2^39+2)·2^128 — and it cleans our own node's honest-residual clause feeding E-4. Falsifier: a split-pencil instance violating the uniform bound at either seam budget. Rate-1/8, 1/16 analogues follow **only after** passing the subtraction rule; list counterparts only in the two-sided sharpness/unsafe direction (his `thm:high-ledger`(ii) already gives Λ_μ = 1 for r ≤ ⌊R/2⌋ for every μ).
- **M-2: engineered-prime exclusion censuses** (~15 banked instances). A1 = E-1 above. A2 (bounded-weight relation exclusion on his declared q₀ = 3·2^41+1 coset) — rigidity, not constants; timing-gated on holmbuar triage per the lnl zero-new-race rule. A3: Burnside orbit-completeness certificates as a service, mutation-controlled.
- **M-3: U2 chart-carried quotient descent** — the Lean-kernelized descent master lemma against his `firstocc_general`/`firstocc_nodup_mem` modules (his named high-value genre); K₂-invariance dyadic collapse; margin-one sharpness (falsifier already constructive).
- **M-4 (new, C3-10b): restrict his packing-overhead machinery to our 2,978,146 band cells.** Question: does the ceiling, band-restricted, lose fewer than 1.66M bits — can upper-side technology be transported through the pincer to shave the 4.73–4.83-bit deficit? Nobody on either side has recorded trying. Pre-registered falsifier: an exact band cell where the restricted overhead still exceeds the unrestricted per-cell rate. Evidence-grade: exploratory; no consumer promised.

**Cadence:** mining feeds from the per-session upstream-delta sweep (§0.3), not from episodic surveys. On hold: 13-chamber census as theorems (0/13 — leads only), dli-internal repricing, sampling-as-theorems.

---

## 4. HARVEST NOW — ranked imports with DAG surgeries

House law: independent reconstruction + exact-integer replay before any vendored supplier reads PROVED. Every surgery = node ops + one UPSTREAM_IMPORT_LEDGER row with immutable provenance + nonclaims. **Every ev-wire below names its ev→req promotion test** (the C3 defect fix — without one, harvests decorate reds forever).

**Same-day fence notes (S1, forced-corrections territory, no status changes):**
- **R1 (EXECUTED 2026-07-26)** depth-32 shell counterexample imported as `l1_m31_depth32_uniform_intercept_counterexample`. Two independent local algorithms reconstruct all quotient labels and the explicit `1225+12=1237` support packet, so the uniform in-band cap `1233` is false at deficiency `192`. The local L1 route is recalibrated, not closed or killed: intercept at least `1237` still leaves `1767799` arithmetic reserve, but no replacement upper bound, received-word realization, or first-match projection is proved.
- **R2** ten-minute audit that no petal/imgfib note assumes the refuted half-slice flatness; bank the audit line.
- **R3** moment-blindness (orders ≤ 990/991) as route-cut citation in `u2_per_row_certifier` — advisory only.
- **R4** Q-moment order floor (≥ 641,593) onto `f2_growing_order_myerson` — **with the τ=1 hypothesis and the three named escapes verbatim in the fence text**; registered on the F2 ladder as "route-cut for fixed raw moments at full mass" only; **the ladder change is surfaced, not silent**.
- **R5** singleton-MASTER: ledger line only.

**Positive harvests, ranked:**

- **H1 (EXECUTED 2026-07-26): affine-span / fixed-union list compilers → the 13-chamber bottleneck.** `upstream_gfv4_affine_span_list_compiler` and `upstream_gfv4_fixed_union_johnson` independently reconstruct and replay `thm:affine-span-list`, `thm:rank-flat-list`, `thm:fixed-union-ray`, `thm:single-mds-circuit-ray`, and `thm:fixed-union-list-johnson` at `b13de811`. The new `rate_half_list_budget_three_affine_rank_rigidity` closes the apparent rank-two equality case: for `d>=3`, every four-word predecessor witness has codeword affine rank three. Chamber audit result: **0/13 chambers killed** because the nine Grassmann lines and four scrolls describe locator geometry, not affine codeword rank. The next promotion test is an explicit incidence-to-codeword bridge; until then all H1 links to the red crossing remain `ev`. Any future chamber kill remains maintainer-surface before the DAG count changes.
- **E-7 (OPENED 2026-07-26): XR generic MDS ray bound → upstream K3.** Draft PR [#1106](https://github.com/przchojecki/rs-mca/pull/1106) exports `xr_generic_mds_kernel_ray_bound` as the column-far fixed-union compiler. The exact KoalaBear specialization pays each retained chart through nullity nine, with two independent upstream replays and a genericity-deletion counterexample. Impact is `ROUTE_CUT`: no chart aggregation, sparse payment, endpoint movement, critical status flip, or prize closure is claimed.
- **H2: exact sparsification identity** (S4; ev into `mca_safe`, `packaging`; trivial toy-row replay). Promotion: when the f(C) compiler consumes the Γ-restricted form; any resulting `mca_safe` amber resolution is **maintainer-surface**.
- **H3: Danny three-way ev fan** (S6; pole localization + coordinate-span/secant into `xr_lowcore_spread_heart`, `l1_mixed_petal_amplification`, `f3_h3_dsp8_correlation_bound`) — the strongest wiring evidence in either plan; **citation pins corrected to v4.tex, not GF**. Promotion per node: exact replay instantiated at the node's own row.
- **H4: v4 solved-row inventory** (S5, **merged with Lean Phase-0(b)**): mint `upstream_v4_proth/f17/corridor` nodes **only after our own ramguard exact-integer endpoint replays** (cheap: 506/507, [0,6/512), four Proth rows) — or at CONDITIONAL/statement-import until the replay lands. Calibration ev only; never promotes.
- **H5: GF Part III Sidon/Fourier chain** (S7; ev into the F2 summit, petal, `imgfib`) with his own :4055 remark **printed in the node statement**: prize rows are outside the proved shallow range. Promotion requires extending (PF)+(MA) past shallow — i.e., Wall-1 movement; no in-plan promotion exists, and saying so is the fence.
- **H6/H7:** low-rate staircases + window compilers (rate-1/2 portion SUBSUMED by our wave-10 layer — do not re-vendor) and the separating-field regime (S8). Promotion: F(r)-positivity replay per rate / adjacency-template instantiation.
- **Method transplant:** the M31 rank-kill discipline — technique yes, object no (scottdhughes territory RACED).

**Infrastructure:** S9 refresh the verifiably stale `upstream_dag/dag.json` (ab7721e5-era, retired v3 skeleton) to the v4 terminal set {S, A, E, list-completion} + live workboard. S10: `verify_prize_dag.py` pass + artifact + public-site refresh per standing rule, every batch.

**Maintainer-surface register:** chamber kills (S3); any req promotion of H1; `mca_safe` amber resolution; the F2-ladder R4 registration; crosswalk adoption; the ownership-split proposal; all outbound PRs.

---

## 5. THE JOINT GRAPH

**Correspondence artifact** — `notes/correspondence/JOINT_CROSSWALK.json`, our tree, single source of truth. Row: `{our_node, his_object{label,file,line}, relation, chain, owner, status_ours, status_his, lean, provenance{our_sha,his_sha}, nonclaims[]}`. **Scoping fix applied:** relation IDENTICAL means *identical-at-scoped-instance* — the F2 row carries chain `f2_zero_prefix_q_equivalence` with scope "zero-prefix, level j < char q" and the pruned-vs-raw gap named in-row; the L1 row is scoped e=0; anything wider is OVERLAP. The Q ↔ `rate_half_band_closure` row is ANALOGY_ONLY with the WP5 "structurally incapable" fence, chain=null, never silently promotable. Validator `tools/verify_crosswalk.py`: every node exists in dag.json; IDENTICAL ⇒ non-null chain; ANALOGY_ONLY ⇒ chain=null + fence citation; JOINT ⇒ both keys named. **Delivery of the mirrored copy upstream is gated on maintainer surface + Przemek's opt-in** (e.g. acceptance into his item (3)); until then it lives in our tree only. Built once, it is simultaneously our joint spine and his dossier's "formal correspondence files."

**Coverage checklists (C3-2), standing in the snapshot:** a 4-row table over his terminal inputs — list-completion ↔ H1 (real route), (S) ↔ H3/XR (ev only), **(A) and (E): no route this cycle — his-side objects, we feed ev only** — and a 25-row table over our submission-orbit TARGETs; every uncovered row carries an explicit "no route — reason," never silence.

**Conditional dedup (C3-3) — OUR HALF CLOSED 2026-07-26 WITH A NEGATIVE.** `assumption_dedup.md` is written and the answer is that **there is no assumption set of ours to dedup**: the 38 mathematical CONDITIONALs carry **zero independent work** and all 38 discharge by pure gate propagation once the 24 TARGETs close (fixpoint in 8 rounds; 0 off-orbit blockers; all 12 open nodes named in their prose but not wired audited and found explicitly fenced as non-consumed, historical, or parenthetical). Pinned fail-closed by `tools/verify_conditional_propagation.py`. **The remaining mathematics is exactly the 24 TARGETs.** What survives of C3-3 is only the joint half: mapping our 24 against his six GF inputs.

**Ownership split (re-count before packaging; current submission orbit = 24 math leaves + dossier):** HE closes (A), (E), K1, K5, Lane-M rows, M31 Lane-L uppers. WE close the **12-leaf in-orbit DLI block** (13 counting the off-orbit factorization leaf), the two certificate leaves (`integer_code_distance_cert`, `u2_per_row_certifier`), the universal unsafe payload `unsafe_crossing_family_instantiation`, the F3 pair, `rate_half_band_closure`, and lane-adjacent list leaves under the crosswalk fences. E1 and its two named-field certificate leaves are route evidence, not universal proof obligations. JOINT, double-key: the F2 wall, the L1 pair, (S) ↔ XR, list-completion assembly, the dossier ↔ his item (3).

**Double-key rule:** any flip on an IDENTICAL or JOINT row needs (a) our key — exact-integer verifier PASS in-tree; (b) his key — bankability contract satisfied (workboard item, partition digest, quantifier, unit). One-sided proofs sit at CONDITIONAL with the missing key named. Hash-green ≠ execution-green.

**Co-finish mechanics:** harvest pass per upstream wave audit; snapshot regenerated per wave with the who's-on-it board; outbound only in his packet grammar naming live workboard items. The endgame sentence, honestly conditioned: one co-signed proof of the F2 identification's target — **once the scoped zero-prefix chain is extended to the pruned K2 atom** — discharges his `U_Q` atom and our summit red together, collapses the L1 pair via chain #2, and the 40 submission-orbit CONDITIONALs then discharge by gate propagation; the resulting all-green DAG, carrying the crosswalk and the node-keyed Lean modules, IS the joint proof's dependency graph.

---

## 6. THE LEAN PLAN — phased, his-priority-aligned

> **STANDING USER DECISION, 2026-07-26 — LEAN IS DEFERRED BEHIND THE INFORMAL PROOF.**
> *"Prefer to push the proof frontier informally for now — focus on formalising
> results later"* / *"we will focus on lean only after there is a full informal
> proof, this will prevent us formalising results which end up not making it or
> being tweaked."* Formalization follows a **complete, stable informal proof** —
> never runs ahead of one. Rationale is churn: a node whose statement is still
> moving (the rate-half poses have been re-scoped in waves 8, 9 and 10 alone)
> would be formalized against a statement that then changes, and the sunk Lean
> work is lost. Everything in this section below — the C3-5 pilot, Phase 0(a)/(b),
> Phase 1, and the C3-6 `lean_ready` audit — is therefore **PAUSED**, not
> cancelled, and does not gate any export.
>
> Two independent findings support the same call (measured 2026-07-26 at
> `origin/main` b13de811, `gh` read-only):
> 1. **The Lean lane upstream is densely occupied, not greenfield.** 447 `.lean`
>    files in-tree; ~92 Lean-titled PRs — **holmbuar 55, LegaSage 29,
>    scottdhughes 6, manifoldcontrol 2, us 2** (#16 starter, #207 tier-one gate
>    arithmetic). §6 was written as if nodes→modules were an opening move; it is
>    not, and a volume promise there would have been racing two established
>    formalizers. Registry rule (1) — never race an open Lean-certified PR —
>    applies to the whole lane, not just holmbuar's rate-half trio.
> 2. **C3-5's pilot object sits in a third contributor's packet.** The corridor
>    certificates are latifkasuli's #275 (merged 2026-07-05, cited in v4 as
>    `Corridor26`); the Pocklington/Proth format anchors are his own e1 and
>    Paving packets. A pilot there would have been an addendum to someone else's
>    work, credited accordingly — fine as a courtesy export, worthless as a
>    "cheapest end-to-end test of OUR nodes→modules mapping."
>
> **A5 REGISTRY DEFECT (same measurement, fix owed in Part 2):** the
> occupied-territory boundary map omits **LegaSage entirely (121 PRs, 29 of them
> Lean, thresholds/C9 lane)** and **latifkasuli entirely (27 PRs: the corridor
> imports #275, the `formalize:` census program, CircleCode/ECFFT/cap25 skeleton
> repairs)**, and describes holmbuar without mentioning that he is the repo's
> principal formalizer. Two of the three lanes the ledger wanted to push into
> were unmapped. Re-derive Part 2 from a per-author sweep, not from the open-PR
> queue alone — the queue only shows the two contributors who happen to be active
> this week.

Constraints on record: his priority order (agents.md §7: (i) proved local theorems in live atoms, (ii) first-match/add-back kernels, (iii) endpoint/integer conversion, (iv) row certificates + counterexample correspondence); banned: stubs, axiomatized global conjectures, end-to-end GF while inputs are open.

- **Pilot (C3-5, rides E-1/E-2, week 1–2):** Lean 4 verification of the Pocklington/Proth certificates + exact `floor(q·2⁻¹²⁸)` endpoint conversion — squarely his genres (iii)/(iv), reuses his in-repo toolchain, cheapest end-to-end test of nodes→modules on content both sides have blessed.
- **Phase 0 (~free):** `lean` column in the crosswalk; adopt `firstocc_general`/`firstocc_nodup_mem` as the shared first-match base with correspondence entries for our U2 objects; **(b)** replicate our Tier-1 F17 endpoint pattern for the four Proth rows — merged with S5, discharging its status-discipline problem and starting his priority (iii) on his own solved rows. Track-B cap ~10% effort holds.
- **Readiness audit (C3-6):** classify the 202 PROVED submission-orbit nodes (190 of them mathematical) `lean_ready` vs prose-level. The former `127/86` measure predates the E1 regressions and must be recomputed before any volume promise.
- **Conventions note (C3-7), agreed with Przemek before volume:** namespace scheme, statement-freezing rule (DAG statement text is the spec; Lean statement diffs are catches), double-key extended to "builds-green ≠ statement-matched."
- **Phase 1:** the verifier-backed nodes as `decide`/Nat-kernel certificates, ordered (ii)→(iii)→census anchors; a module lands in the same commit as its node's surgery.
- **Phase 2 — explicitly gated (material fix):** co-signed per-terminal packages (F2, S, A, E, list-completion) with open inputs as declared hypotheses go upstream **only after the maintainer surfaces the co-sign proposal and Przemek opts in**; until then they live in our tree and are never framed as progress-claiming PRs (cf. the #1084 rejection).
- **Phase 3:** hypotheses discharged in place as inputs fall; `mca_grand`/`list_grand` close as builds. Hard nodes formalized only where a live certificate imports them.

---

## 7. Governance, risk register, and what NOT to do

**Governance:**
- **First outbound note = pacing ratification (C3-11):** keep the 2-PR cap OR batched waves with the standing snapshot between waves — the maintainer flagged this for ratification; we do not default it.
- **Stall rule (C3-12):** wave untriaged > 10 days → consolidate the next wave into one omnibus packet, stage upstream-ready packets under `notes/outbound_ready/`, route what fits through pre-authorized channels (E-3's register lane is already promoted for exactly this).
- **Attribution (C3-13):** bilateral per-node/theorem ledger, appended per wave, co-signed — proposed at the E-1 landing, inside O-2.
- **Defect custody (C3-14):** agreed cross-repo rollback paragraph (who fixes, which repo, how DAG + register roll back jointly), citing the double-key rule; the forced-corrections authority covers our repo only.

**Risk register (triggers → mitigations):** **R1** triage stall → the stall rule + staging. **R2** contributor scoop — the corridor prime is a public printed ask; rank exports by his-need × readiness × scoop-exposure; per-session poll of his open-PR queue vs our in-flight items (upgraded from submission-day-only). **R3** correspondence drift → CI script resolving every cited label at its pinned SHA, failing on movement; every harvest replays its weld at the current pin ("a stale source pin is a failed provenance gate" — his rule, adopted inbound). **R4** concurrent-close race → the who's-on-it board; now guaranteed-relevant once X-1 lands. **R5** v5 rewrite → every subtraction pin-relative, stated so. **R6** single-maintainer bus factor → stdlib-deterministic verifiers + attested execution transcripts to widen his bottleneck. **R7 self-kill:** two full export+harvest cycles with zero joint-bracket-bit movement → the exchange strategy has failed its own falsifier; revert effort to direct red-closure grind and take the submission-posture decision. Every other program we run has a termination condition; this one now does too.

**What NOT to do (carried in full from B1 §4; condensed):** TAKEN items cited as anchors, never re-proposed (cyclic floor, cor:abf(iii), #1010/#1013/#1019/#1050, kernel-basis packets, imgfib audit, baseline cert sets). RACED: anything at agreement 1116691496959 (holmbuar trio — never race a Lean-certified open PR), M31 Hahn/flatness/rank-7, KoalaBear rank-nine, Danny descent machinery, threshold owner-leakage. DEAD: sub-Johnson crossings, superseded σ\* band, Johnson safe anchor, corridor-chain list_safe, MCA numerators sold as list bounds, #750-form imgfib re-poses, **and now M-1's struck rate-1/4 family**. HOLD: far-CA Hankel chain (TARGET terminal — stop-rule), DSP8 standalone, XR floors, Lane-L addenda until triage. Carried fences on every packet: §0.4 quadruple-mismatch verbatim where rate-half appears; prime-vs-extension stated first on F3/C36; conditional statements print falsifier + F-round record; C1′ REFUTED travels with dli.

---

## 8. The walls, honestly

**Wall 1 — his input 3 == our F2 summit (`f2_growing_order_myerson`).** What this program does: exports the scoped identification certificate (X-1) so both sides know the wall is shared; imports the strongest route material the F2 campaign has ever had (H5, shallow-range-fenced) and the τ=1-scoped route-cut (R4); and gives the only recorded route onto the wall a named slot — **run the DSP8 Sidon-strip harness; if the residual lands ≤ 24, trigger the roadmap §10 joint-brief authorization ask** (C3-9; owner: us; precondition: harness green). What it does not do: pay any constant, extend (PF)+(MA) past the shallow range, or close the zero-prefix→pruned-atom gap. The wall stands; the program makes it *jointly* attackable instead of privately attacked twice in incompatible formulations.

**Wall 2 — the balance line (123.17 bits from below vs 127.90+ needed across 2,978,146 band cells; his ~1.66M-bit overhead from above).** Previously silently skipped; no longer. The program ledgers it (X-2, the pincer export — regime complementarity is itself the highest-value observation on this front and doubles as partial-credit insurance), mines it once (M-4, the band-restricted overhead question, pre-registered falsifier, exploratory grade), and otherwise **defers it explicitly**: no item in this ledger closes the 4.73–4.83-bit deficit, and at rate-1/2 "finish together" is impossible until something does. Deferral is a recorded decision here, not an omission.

**The bottom line, stated against our own metric:** executed perfectly, r1 closes at most two of our reds directly (the M-1 seam feeding `rate_half_band_closure`'s residual; any S3 chamber kill), evidences ~ten more, discharges zero conditionals by itself, and covers two of his four inputs with real routes. Its actual product is the machinery of convergence — the shared map, the deduped hypothesis set, the double-keyed crosswalk, the Lean pipeline, and the governance that lets two trees finish one proof. Whether that machinery moves joint bracket-bits is measured per wave, and R7 says what happens if it does not.
