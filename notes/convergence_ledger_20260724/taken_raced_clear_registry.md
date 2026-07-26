# TASK A5 — TAKEN/RACED/CLEAR REGISTRY (overlap adjudicator)

Sources: upstream read-only at `origin/main = b13de811` via `git show`; `gh` read-only on `przchojecki/rs-mca`. **Part 2 was rebuilt 2026-07-26 from a FULL per-author sweep (1,099 PRs, 11 authors; open queue #1087–#1106), superseding the original open-queue-derived map** — see the box in Part 2. Other parts still rest on the original sweep (open queue #1087–#1105; closed through #1040+). Our docs `notes/lane_l_crosswalk_20260724/lnl_findings.md`, `notes/upstream_pr_proposals_20260720/upr_proposals.md`, `notes/correspondence/UPSTREAM_IMPORT_LEDGER.md`.

## PART 1 — OURS ALREADY IN HIS TREE (grep-complete inventory, `AllenGrahamHart` + `rs-mca-prize-dag` sweep)

**Current-wave integrations (the five, confirmed + file-resolved):**

1. **#1010 four-pair audit** → `experimental/notes/audits/audit_four_pair_crossing_exact_replay.md` + `experimental/scripts/verify_four_pair_crossing_exact_replay.py`. Status AUDIT/EXPERIMENTAL. Integrated in wave 1009–1046 (agents-log 2026-07-22). Pins our mirror `rs-mca-prize-dag@b8a169ac` and the exact exponent convention (list `p^(m-K)` vs MCA `p^(m-K-1)`).
2. **#1013 quotient-cell calibration** → `experimental/notes/audits/audit_quotient_cell_prefix_fiber_and_split_pencil_census.md` + `verify_quotient_cell_prefix_fiber_floor.py`. AUDIT/calibration ("enters no proof"); pinned `@8a7ec132`; positioned as companion to his `rowsharp_q_external_calibration.md` — it partially services his §0.5 falsifiability objects (super-poly prefix fiber exists one cell over, in the quotient cell).
3. **#1019 pruned-Q packet** → `experimental/notes/audits/rowsharp_q_pruned_toy_packet.md` + json + verifier. AUDIT/calibration; explicitly answers agents.md Good-first-PR #1 (`prob:row-sharp-q` toy row).
4. **#1050 WCL register** → `experimental/notes/wcl_slot_contributor_requests.md` + `experimental/scripts/verify_wcl_slot_decomposition.py` (commit 71f64349, wave 1047–1069). Status CONTRIBUTOR REQUEST/EXPERIMENTAL; pinned `@b959fe8f`; framed as contributor-marketplace serving OUR dli lane — the consumption channel back to us is established precedent.
5. **#1051 cyclic floor** → commit **78e67c40** "Integrate rate-half cyclic list floor", `Co-authored-by: AllenGrahamHart` git trailer, +213 lines into `experimental/experiments.tex` (new section "Direct Lane L Result: a Rate-Half Cyclic List Floor", status PROVED/DIRECT_LIST). Took: general quotient-rotation theorem + the c=2^33 specialization at agreement 1116691496959 + q_0 Pocklington + full Lane-L packet block. Did NOT take: interleaved-arity clause, CR5 margin criterion + extremality ledger, residual-band propagation, historical c=2^22 instantiation, our two Python scripts ("deliberately not imported"). Now cited in agents.md Lane L text itself (lines 77, 178).

**Additional finds (older, from the grep — pre-dating the five):**

6. **Finite-track packets** (commit 486c8fb3, 2026-07-10): `notes/roadmaps/finite_prize_kernel_basis.md` (ROADMAP: seven reds / three kernels), `notes/thresholds/cap25_finite_census_necessary_hypotheses.md` (PROVED counterexample families), `cap25_finite_deep_regime_exactness.md` (cyclotomic rigidity), `cap25_finite_signed_census_frame.md` (four theorems) — all sourced "the fork's finite-track campaign", all marked "safe to park until the finite pivot".
7. **imgfib crosswalk audit** (commit 2633895a, 2026-07-15): `notes/l1/l1_imgfib_crosswalk_audit.md` + `data/certificates/l1-imgfib-crosswalk-audit/certificate.json`.
8. **cor:abf(iii)** in `proximity_prize_results_v4.tex`: the general MCA→list conversion on the quadratic staircase is recorded, credited to ChoThresholds26 (his own paper) — the indirect route is TAKEN at the results-of-record level.
9. **Deep history**: 34 `AllenGrahamHart` mentions in agents-log spanning the PR #101–#419 era (M1/L1 material: `m1_boundary_off_external_anchor_audit.md`, width-one closure, high-agreement compiler, etc.) plus data jsons (`cap25_v13_route_d_barrier_map*.json`, `full_agreement_orientation_saturation.json`, `pr-triage-2026-06-26.json`). All merged and provenance-logged; historical, no live overlap risk.

## PART 2 — OCCUPIED-TERRITORY BOUNDARY MAP

> **REBUILT 2026-07-26, per-author (queue r2 Q3).** The original Part 2 was
> derived from the *open-PR queue*, so it mapped only whoever happened to be
> active that week and **missed two substantial contributors entirely** —
> LegaSage (121 PRs) and latifkasuli (27, the corridor owner) — while describing
> holmbuar without noting he is the repo's principal formalizer. Two of the three
> lanes the Convergence Ledger wanted to push into therefore read falsely CLEAR.
> Rebuilt from a full sweep: **1,099 PRs, 11 authors**, `gh` read-only at
> `origin/main = b13de811`. Rule going forward: **derive lanes from per-author
> history, never from the open queue** — the queue shows this week, not the map.

| author | PRs | open | window | lane |
|---|---:|---:|---|---|
| **holmbuar** | 370 | 15 | 06-29 → 07-25 | M31 flatness/Hahn, rate-half list refinement, synthesis audits — **and 55 Lean PRs: the principal formalizer** |
| **AllenGrahamHart** (us) | 256 | 1 | 06-17 → 07-26 | our lane; see Part 1 |
| **DannyExperiments** | 152 | 0 | 06-17 → 07-23 | M31 base/extension mechanisms, syndrome-line locals, descent/locator machinery |
| **scottdhughes** | 135 | 3 | 06-17 → 07-25 | M31 LIST rank-kill, KoalaBear rank-nine; 6 Lean PRs |
| **LegaSage** | 121 | 0 | **07-04 → 07-10 only** | thresholds / C9 payment reduction, Sidon + max-fiber, first-match atlas, entropy-frontiers, kernel-checked audits; **29 Lean PRs** |
| **latifkasuli** | 27 | 0 | 06-17 → 07-19 | **the corridor imports (#275 = `Corridor26`)**; a `formalize:` census-reduction program (CircleCode / ECFFT / cs25_cap_v12 skeletons proved false-as-written + repaired, machine-checked counterexamples); KoalaBear/Paving replay audits |
| **avdeevvadim** | 25 | 0 | 06-21 → 07-22 | thresholds: selected-owner, dense-band/dense-shell, singleton-MASTER factorization, row-sharp bridges |
| **maelcar** | 9 | 0 | 07-14 → 07-21 | finite Chebyshev / D128 packets: block-free, quadratic descent, quartic-line, typed pair-resource |
| **manifoldcontrol** | 2 | 0 | 07-06 → 07-13 | Lean toy-case kernel certificates (`experimental/lean/rsmca_certificates`) |
| **JoseBrox** | 1 | 0 | 06-29 | L3 quotient-profile scanner audit |
| **alejandrozu** | 1 | 0 | 06-18 | Paper A finite verification crosswalk |

**Consequences for our lanes (2026-07-26):**

- **The Lean lane is not greenfield and is not ours.** 447 `.lean` files in-tree;
  ~92 Lean-titled PRs — holmbuar 55, LegaSage 29, scottdhughes 6, manifoldcontrol
  2, **us 2** (#16 starter, #207 tier-one gate arithmetic). Registry rule (1)
  ("never race an open Lean-certified PR") should be read as covering the whole
  lane. Independently moot for now: Lean is deferred behind the informal proof
  (user decision, ledger §6).
- **The corridor is latifkasuli's.** E-1 is an *addendum* to #275 filling the
  printed `thm:corridor` remark (v4:294), and must cite #275 and claim no
  machinery novelty. Currently unraced — no open corridor PR — but that is a
  scoop-exposure clock, not a licence.
- **Dormancy is not vacancy.** LegaSage has been silent since 07-10 and
  latifkasuli since 07-19; both hold large, coherent programs. Absence from the
  open queue means nothing about ownership.
- **Our own in-flight item:** **#1106** (draft, opened 2026-07-26)
  "K3: add column-far fixed-union ray route cut". Not opened by the Opus 5 worker
  — treat as another agent's in-flight work; do not duplicate K3 route-cut
  material without checking it first.

**holmbuar — three concurrent programs, the busiest contributor (15 open PRs):**
- *M31 flatness/Hahn C1 program* (open #1087, #1089, #1093–#1096, #1098, #1102–#1104): boundary = M31 fixed-G Hahn/Delsarte LP relaxations on the adjacent pairs (5413,72860)/(840822,908269) — exact optimum 20737821 unconditional cap, conditional 16777214/16032481 under named hypotheses; flatness conjecture C1 + T8/T16/T32 census shards + boundary route cuts; canonical-remainder barrier; depth-32 shell and ragged-collision counterexamples. Also Lane M M31 at 2^-100, agreement 1116023 (#1104, #1102, #1088-adjacent).
- *Rate-half list refinement series* (open #1097, #1099, #1101 — ALL parasitic on our integrated floor, all Lean-certified, PROVED-labelled): boundary = OUR row (F_q, k=2^40, n=2^41) at agreement 1116691496959 — refined constant (C(255,129)+C(127,64))/256, upper/lower bracket floor(C(n,k)/C(a,k)), s=0 boundary scale + the 33-scale dyadic census + packing obstruction P_pair. **Anything at this agreement that is a constant, bracket, or scale claim is his until triage.**
- *Synthesis audits*: #1090 (v4 citation audit; predecessor #1081 was REJECTED, #1071 accepted).

**scottdhughes — M31 LIST rank-kill campaign (exact scope from PR bodies):** rank ≤5 excluded and rank-6 boundary branch closed (#1064–#1066); rank-seven cumulative-effective-deficit frontier advanced Q=26,193 → **29,554** (#1088) → **147,594** (#1092); residual localized to the unique `Q=147595, k=4981` class with the named terminal `HIGH_PAIRWISE_MASTER_LOCATOR_OVERLAP` (specializing `CROSS_COFACTOR_INTERLACED_H_AND_DEEP_FIBER_INCIDENCE`), pairwise-gcd threshold `deg gcd(G_i,G_j) >= 16903` (#1105, stacked on #1092). Explicit non-claims: rank ≥8 untreated, no Grande Finale atom assignment, LIST row not closed. Second holding: KoalaBear M1 rank-nine slack ledger (#989–#995, #1076–#1079 route-cut chain) = the §0.4 KoalaBear safe side. **Boundary = rank-stratified M31 LIST branches + KoalaBear rank-nine; the CLEAR gap inside his own program is rank ≥8 and the named overlap terminal — but he is actively heading there.**

**DannyExperiments:** M31 base/extension mechanisms and syndrome-line local theorems — #993 scalar-descent equivalence (quartic→prime field at agreement 1,116,023), #1067 pole-tolerant scalar-locator localization, #1069 base-field coordinate-span confinement, #1023 Pade–Forney full-packet, #1038 full-layer-42, #1021 masked saturation, #990/#981 O5c deep-regime counterexamples, #972–#988 affine-prefix obstructions. Boundary = M31 descent/locator/syndrome machinery + O5c repairs.

**avdeevvadim:** thresholds lane, low cadence — #1063 singleton-MASTER factorization/source-entry route cuts; historical selected-owner/dense-shell/dense-band program (#716–#905). Boundary = threshold source-entry and owner-leakage structure.

**maelcar:** finite Chebyshev/D128 theorem packets (#1015–#1018): block-free, quadratic-descent, quartic-line, typed-pair-resource lanes.

## PART 3 — DOES HE CONSUME CONDITIONAL MATERIAL? YES, WITH STRICT DISCIPLINE

Direct evidence: integration waves carry statuses `PROVED LOCAL / CONDITIONAL / CONJECTURAL / COUNTEREXAMPLE / ROUTE_CUT / AUDIT / EXPERIMENTAL` per packet; accepted conditional examples include #1054 "conditional tangent-rooted Q-shell cap", the C7–C9 conditional compiler structure, the conditional CS25 M31 bridge, and the entire `Conjectures_and_Barriers` ePrint (CONJECTURAL). The v4 synthesis itself "cleanly separates … conditional packets" as a first-class category. The binding constraints, from observed accept/reject decisions:
- **Accepted** conditional packets carry named hypotheses PLUS positive content (a local payment, route cut, or counterexample) and a workboard binding.
- **Rejected**: #1084 ("competing conjectural closure skeleton without a live-compiler payment or route cut"); #1081 (terminal verdict contradicting its own recorded defects; missing workboard binding; inadequate primality/tamper-exit contracts). Also `git diff --check` failures are cited grounds.
- **Never promoted**: conditional material stays in `experimental/`, never enters tex theorem rows or moves endpoints/scores until closed ("do not treat these local discharges as row payments until bound to the active first-match partition").
- **Replay burden is ours**: every wave states "no Python, Sage, Lean, or TeX build was run" — static review only, so verifiers must be airtight before submission.

Implication for exports: our CONDITIONAL nodes (e.g., 36-strong conditional orbit) ARE exportable, but only packaged as named-hypothesis local packets with route-cut/payment content and a deterministic verifier — never as closure claims.

## PART 4 — ATTRIBUTION TEMPLATE (observed mechanics, to be replicated)

1. **Git**: maintainer authors the squashed integration commit; contributor gets a standard GitHub `Co-authored-by: AllenGrahamHart <216503854+AllenGrahamHart@users.noreply.github.com>` trailer (78e67c40).
2. **agents-log**: one consolidated wave entry naming contributor + PR numbers; model credited explicitly ("AllenGrahamHart with Claude Fable 5 (#1050)"). PR-local log fragments, agents.md rewrites, `PR_BODY.md`, and workflow files are systematically NOT imported — don't bother polishing them.
3. **Packet header** (our accepted format, now house style): Status line → "Agent/model: Claude Fable 5 acting for AllenGrahamHart" → Artifact (stdlib-only, fail-closed, exact-integer verifier with mutation controls) → "Cross-repo source (SHA-pinned, read-only): github.com/AllenGrahamHart/rs-mca-prize-dag@<sha>" → local source commit / upstream target commit pair → honest-scope/non-claims section.
4. **tex-level**: "integrates the mathematical content of AllenGrahamHart's PR #1051", source commit pinned; scripts dropped (tex self-contained).
5. **Norm to adopt**: contributors self-audit overlap in the PR body ("The open-PR audit through #1104 found no duplicate" — #1105). Our PRs should carry the same clause, citing this registry.

## PART 5 — THE VERDICT REGISTRY

**TAKEN (do not re-propose; cite as anchors instead):** rate-half cyclic quotient-rotation floor (78e67c40 → experiments.tex + agents.md Lane L); indirect staircase MCA→list conversion in general form (v4 cor:abf(iii), ChoThresholds26); §0.4 four-pair margin replay (#1010); quotient-cell §0.5 calibration + scroll-branch-empty census (#1013); pruned-Q toy (#1019); WCL register (#1050); finite-track kernel-basis + three cap25_finite packets (486c8fb3); imgfib crosswalk audit (2633895a).

**RACED (live open PRs occupy the object — stand down until triage):** any constant refinement, bracket, or dyadic-scale claim at agreement 1116691496959 (holmbuar #1097/#1099/#1101, Lean-certified); M31 fixed-G Hahn caps and complementarity (holmbuar #1089/#1098/#1103); M31 LIST rank-7 residual incl. the `Q=147595` head and the overlap terminal (scottdhughes #1088/#1092/#1105); KoalaBear §0.4 safe side / rank-nine (scottdhughes); M31 Mersenne safe-side descent + syndrome-line machinery (DannyExperiments); M31 flatness T-census (holmbuar #1093–#1096).

**CLEAR (open, unclaimed by anyone):**
- *Interleaved transport + band propagation addendum* to the integrated floor (lnl RANK 1: agreements [2^40+1, 2^40+2^34−1], same bound by L_1 monotonicity + diagonal-repetition transport + proved collapse L ≤ floor(L(q−1)/(q−L))). No open PR states either clause. Low value; bundle-only, after #1097/#1099/#1101 triage.
- *The n=2^41 two-sided a_RH threshold family* (upr RANK 2: `a_RH(q)=n−floor(q/2^128)+1`, 2^128<q<2^166.5, wave-10 audited). Still touched by NO open PR — the holmbuar trio sits at the cyclic-floor agreement, not the far-CA staircase. Best live RESULT export; must carry the quadruple-mismatch fence vs §0.4 verbatim.
- *13-chamber budget-3 split-pencil census as LEAD* (remainder of #1013's calibration; 0/13 closed — lead-grade only).
- *Lane L's actual open ask*: an unconditional post-Johnson UPPER bound on a declared family — nobody has it, our machinery can't reach it ((n−k)/2 < Johnson radius at rate 1/2); new-mathematics territory, flagged as such.
- *WCL slot answers flowing back*: the register is integrated; his contributors solving slots and us consuming results is a sanctioned, unoccupied channel.

**DEAD (recorded to prevent zombie proposals):** budget-1/2 exact crossings at 3n/4 (below Johnson); indirect conversion of `rate_half_quadratic_exact_range` to lists (inside Johnson by 254578446957 agreements AND generalized upstream); historical σ*=8,592,912,738 band and fixed-tail floor (superseded); multiplicative-amplification census (raced + wrong format); Johnson safe anchor (at, not beyond); corridor chain list_safe (conditional-on-conditional, no in-tree integers); anything phrased as an MCA numerator sold as a list bound; imgfib full-petal re-pose (#750 precedent); `paving_rf3_double_prime` (it is HIS result, imported by us).

**Standing boundary rules distilled:** (1) never race an open Lean-certified PR; (2) the maintainer rejects conjectural skeletons without payment/route-cut content — conditional exports need named hypotheses + a verifier + workboard binding; (3) integration strips scripts/logs — the tex/note body must be self-contained; (4) every export pins our mirror SHA and the upstream target commit, uses the "Claude Fable 5 acting for AllenGrahamHart" header, and includes an explicit non-claims section; (5) include a self-run open-PR overlap audit clause in every PR body.

Key file paths (ours): `/home/u2470931/smooth-read-solomin/prize/notes/lane_l_crosswalk_20260724/lnl_findings.md`, `/home/u2470931/smooth-read-solomin/prize/notes/upstream_pr_proposals_20260720/upr_proposals.md`, `/home/u2470931/smooth-read-solomin/prize/notes/correspondence/UPSTREAM_IMPORT_LEDGER.md`. Upstream anchors: `experimental/agents-log.md` (wave entries 2026-07-22/23/24), `experimental/experiments.tex` (integrated floor section), `experimental/notes/audits/` (our three audit packets), `experimental/notes/wcl_slot_contributor_requests.md`, commits 78e67c40 / 71f64349 / 486c8fb3 / 2633895a.