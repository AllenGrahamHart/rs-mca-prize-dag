# Upstream open-PR survey — przchojecki/rs-mca

Snapshot: 2026-07-19 ~16:00 UTC. Read-only reconnaissance (gh CLI + local upstream clone; no writes, no comments).

## 1. Roster

- **72 open PRs**, number range #882–#979. **Zero drafts, zero labels.**
- Authors: **holmbuar 43**, **scottdhughes (Scott Hughes) 15**, **DannyExperiments (Danny) 13**, **avdeevvadim (Vadim Avdeev) 1**. manifoldcontrol: none open right now.
- Age: 19 PRs <24h, 48 PRs 24–48h, 5 PRs 2–7d, **none older than ~50h** (oldest = #882, 2026-07-17 12:50). The backlog is effectively a two-day rolling window.
- **Integration cadence (Przemek):** close-and-integrate "wave" commits on main, 1–3/day. Recent: `999b8f3a` + `6c4ebb35` (07-19, "Integrate follow-up experimental audits" / "reviewed experimental PR packets"), `3404d21b` (07-18), `c4856fa6` (07-17, **Paving package replaced with v9.2**), `06b2a6fb`/`48115af6`/`a5750192` (07-17). The missing block **#951–#975 (25 PRs) was integrated same-day on 07-19** — triage latency is roughly 24–48h.
- Contributor conventions have converged: SHA-pinned stacked dependencies ("integrate #915 first", "replay only commit X onto main"), stdlib fail-closed verifiers + tamper suites, Lean no-sorry packages, explicit "Risk-limits"/"Boundary" non-claim blocks. Every packet checked disclaims "no MCA threshold, no Proximity Prize claim."

## 2. Lane clusters (all 72)

| Lane | PRs | Count |
|---|---|---|
| **M1 / KoalaBear rank-nine ledger** (scottdhughes) | 883, 886, 887, 889, 895, 896, 898, 899, 901, 906, 907, 908, 909, 940, 950 | 15 |
| **Route-D** (holmbuar; first-match / add-back / marked-incidence no-go mapping) | 910, 913, 918, 920, 923, 927, 928, 931, 932, 934, 937, 939, 942, 943, 945, 948 | 16 |
| **Lean formalization** (holmbuar) | 912, 916, 921, 926, 933, 938, 941, 944, 947, 977 | 10 |
| **Audit** (holmbuar; audits of other open PRs) | 884, 911, 914, 915, 919, 922, 925, 929, 936, 946, 978 | 11 |
| **Dense-shell / thresholds** (#827's successor lane) | 885, 900, 917 (holmbuar), 905 (avdeevvadim), 924 (Danny) | 5 |
| **Paving-paper-direct** | 882, 893 (holmbuar) | 2 |
| **Experimental** (Danny: fixed-26/27 resultants, affine-prefix, rank-16) | 890, 891, 892, 894, 902, 903, 904, 930, 935, 949, 976, 979 | 12 |
| **C3 semantic atlas** | 888 | 1 |

Keyword-scrub notes: "dli" hits were all substring noise ("stdlib"); "C36" hits were commit-SHA fragments. No open PR touches rate-half/2^167, C36/DSP8, WCL slots, dli, XR/GRS4 split-pencil, myerson, row-envelope, or rigidity_kernel.

## 3. Topical reads (body + files)

### #905 avdeevvadim — "thresholds: prove uniform dense-shell transfer shape"
Proves the uniform dense-shell transfer-shape lemma (TS1 pair-1 envelope 1.086, TS2 pair-2 1.663, TS3 child-share floor 7/6) for the shifted-Chebyshev cascade at every depth, via a positive two-state three-level cone A = K − (241/500)I plus curvature induction (C=1289/500) and a Riccati log-derivative envelope; certified with 448-bit Arb balls, degree-320 Chebyshev–Lobatto interpolation. Discharges **INV-TAIL**, making the existing |K| ≤ 1 dense-shell master and class-sign conclusions **unconditional at every depth B**; general decorated |K| ≥ 2 remains conjectural. **Assessment: IMPORT-CANDIDATE LEAD** (thresholds lane; direct successor to the #827 shell-band structure). Caveat from audit #911: the 448-bit Arb continuum certificate was NOT independently replayed (python-flint unavailable in audit env); the five scalar gates were re-derived in stdlib interval arithmetic (PASS), and a 10/10 SHA256SUMS mismatch table is on record.

### #900 + #885 holmbuar — Dense-shell PROP-TAIL / INV-TAIL closure
#885: #880's INV-TAIL (three floors, j ≥ 49) reduces to a single scalar (PROP-TAIL — directional sibling proportionality on the census window); PROVED reductions + certified grids j ≤ 60, CONDITIONAL on PROP-TAIL. **Corrects two banked share-floor constants: gamma_req at certified caps is 1.1011, not 1.036.** #900: discharges PROP-TAIL (rho_prop@i<17(n) ≤ 1.02560749) as a certified-census theorem; SIB-BAND, LAM-BOX, C'-CAP all discharged(-conditional); status CONDITIONAL with exactly **two computed inputs left: (FOLD) and (FLOOR-PERSIST)**, zero monitored-only literals; adds CERT-BIND hash-binding after a stale-cert class bit them twice. **Assessment: IMPORT-CANDIDATE LEAD** — the product-profile emission program (#816→#858→#880→#885→#900) is converging on an unconditional single-shell/dense-band statement; two leaves from closure.

### #893 holmbuar — "Prove Paving v9.2 RF3'' global-degree retained-factor bridge"
PROVED, against immutable Paving v9.2 (which just replaced v9.1 on main, c4856fa6): audits the retained-factor source chain, proves the standalone RF3'' global-degree bridge (corrected nonlinear recurrence, linear-factor lift, content/leading-coefficient guards, all four exact RF3'' ceilings); 286,067-check verifier, 16/16 tamper rejections; Lean certifies arithmetic kernels, algebraic-function-field theorem kept as explicit unasserted target. Notes **a future manuscript version must state RF3''** (i.e. v9.2's RF3/RF3' prose is known-insufficient as printed). **Assessment: FYI / paving-watch lead** — tells us where the paving paper's factor-retention row actually stands.

### #882 holmbuar — "Formalize atlas coverage and payment interfaces"
Lean (grande_finale package, 8087 jobs): typed prefix, exact-card witness, retained-occupancy, and **boundary-payment bridges**; connects actual first-match slope cells to the exact FC1 incidence/moment floor; corrects C3 scope to the proved subgroup-coset census. Interface formalization only — no payment is paid. **Assessment: FYI** — this is the typed scaffolding into which a future payment/first-match proof would slot; oldest open PR (07-17).

### #937 holmbuar — "Route-D: expose marked-key global add-back obstruction"
Proves the fixed-literal-G full-beta one-scalar cap via Newton coefficient reduction; two counterexample families (exact F17 raw Rule-2: printed key shape omitting G does not imply a field-sized cap before named filters; F101 primitive inhomogeneous: beta cannot be omitted); **states the correctly quantified global weighted add-back theorem and direct injection target**. Does not execute the undefined named first-match projectors. **Assessment: FYI / lead on the profile add-back input** — the add-back statement is now correctly quantified with its obstruction map drawn; companion #942 gives the F23 marked-core key add-back floor.

### #909 scottdhughes — "M1: bank tangent first-match owner"
Promotes one fixed-SP3 tangent image to a global-once **first-match owner** per received pair, removes its slope set before later owners, restarts the complete selector ladder; exact KoalaBear ledger movement (U_paid 2602502999 → 2603484103; rebuilt T_18014, E_max); the naive `old_T − j` value is refuted (off by 173957). Explicitly does NOT prove determinant-weighted nonzero-pencil incidence, complete rank-nine payment, U_Q, U_A, profile comparison, or lower reserve. **Assessment: FYI (M1 = Codex's branch)** — real positive movement on first-match *ownership* inside M1's ledger, but the exhaustion/payment obligations stay open.

### #977 holmbuar — "Lean: prove complete-fiber subset packing"
Machine-checks a generic fixed-size subset-packing theorem and the full arbitrary-field **equation-(2) wrapper for the fixed-e received-list polynomial family**: powerImage H c as Q_c, completeFiberSet on canonicalSupport as E_c(P), h = floor((K−1)/c), using the proved completeFiberIntersection bound; numerator is exactly N_c = |Q_c|. Boundary: does NOT prove the |Q_c| = n/c normalization, equation (3), the residual 1792-profile cap, GRS/syndrome transport, or list results. Successor of the closed #765 circle-code complete-fiber chain. **Assessment: IMPORT-CANDIDATE LEAD for the l1 lane** — this is the fiber-counting machinery adjacent to our imgfib/rich-fiber vocabulary, now with a Lean-verified core; if eq-(3) + normalization land later, worth a faithfulness read against our crosswalk rows.

### #978 holmbuar — "Audit primitive top-seam marked incidences"
Theorem-shaped audit of the primitive shift-pair top seam e = w+1 in normal form A−B = c ≠ 0 over F_17*: the complete target-fibre seam holds 32 ordered marked triples (not just the four-mate rooted star), projecting to 4 MCA slopes {2,5,8,11}; a fixed (z,A,B) fixture admits three distinct common cores, **refuting uniqueness** (but not subexponential determinacy); verdict **OPEN GAP** — refutes counting shortcuts, claims no asymptotic marked-incidence payment. **Assessment: FYI** — first-match survivor accounting is harder than the shortcut versions; feeds Route-D's obstruction map.

### (brief) #898/#899 scottdhughes — rank-nine rich-pencil
"Rich-pencil" here is a KoalaBear/M1 compiler object (E_20 = Σ_L beta_L(J_L − 20) over rich graph lines; GF(2^37)/GF(67^2) controls), NOT our l1 rich-fiber or XR split-pencil. Live terminal: UNPAID_SOURCE_BOUND_RICH_PENCIL_AGGREGATE. **FYI (Codex-relevant).**

## 4. Q3 — paving paper's four missing inputs

**Nobody claims any of the four.** Every occurrence of "direct Sidon payment", "residual ray compiler", "complete profile-envelope comparison" in open PRs is inside Risk-limits *disclaimers* or next-step lists (#933, #938, #941, #947: "supply image-scale MI/MA or a direct Sidon payment; compile a residual ray; compare the complete profile envelope; establish lower reserve"). But the ecosystem is actively circling two of them:
- **first-match profile exhaustion**: Route-D is mapping its obstruction boundary (no-gos #927 F31 root compiler, #931, #934, #939; audit #978), while M1 banks partial ownership (#909). The "named first-match projectors" are still explicitly undefined (#937's scope note).
- **profile add-back**: #937 states the correctly quantified global weighted add-back theorem + two omission counterexamples; #942 the F23 add-back floor.
- **image-normalized Sidon payment**: untouched (disclaimers only).
- **ray compiler**: untouched (one mention, a disclaimer in #938).
Plus infrastructure: #882 formalizes the payment/atlas interfaces in Lean; #893 fixes the paving factor-retention bridge (RF3'').

## 5. Q4 — our results upstream

**No open PR mentions AllenGrahamHart, prize-dag, imgfib, mixed-petal, or our crosswalk.** Search across all repo PRs/issues confirms the only crosswalk items are our closed #750 and their closed audit #757 ("L1 imgfib crosswalk — mixed-petal gap open", last touched 07-15) — both already banked on our side. #765's "crosswalk" is their own tex↔draft crosswalk (cs25_cap_v12.tex vs thresholds draft), unrelated. Our #174 is CLOSED (07-02, known). **Nothing CONSUMES-OURS or CONTRADICTS-OURS in the open set.**

## 6. Q5 — #827 single-shell failing band

CLOSED 2026-07-16 (not merged) = **closed-integrated**: all its files are on upstream/main (experimental/scripts/verify_shell_mass_spectral_law.py, the Lean package, certificate, thresholds note). Its claims stand: exact digit-shell decomposition on the base-3 chart; all-dense shell {s3 = B} is the first single shell to fail alone at exactly B = 12; the shell is non-hierarchy-measurable but digit-product structured; its own opening conjecture (middle shells negligible) was self-contradicted in range, asymptotic left OPEN. **Implication:** the successor lane is the currently hottest thresholds thread — #885 → #900 (PROP-TAIL, two leaves from unconditional) and #905 (INV-TAIL discharged, |K| ≤ 1 unconditional pending audit), with an active audit-repair cycle (#914 found the P7 pair-2 bound false as stated → repaired in #917; #911 flags the unreplayed Arb continuum cert). The "product-profile emission" program #827 named is now the explicit spine (#816→#858→#880→#885→#900).

## 7. WATCH list

| PR | Why watch |
|---|---|
| #905 + #911 | INV-TAIL discharge; watch whether Przemek requires an independent Arb replay before integrating |
| #900 (+#885) | PROP-TAIL: only (FOLD) + (FLOOR-PERSIST) left; closure would make the dense-shell |K|≤1 dichotomy fully unconditional |
| #893 | RF3'' bridge — predicts a Paving v9.3 manuscript revision; tells us the printed RF3/RF3' rows are insufficient |
| #977 | complete-fiber Lean eq-(2); if eq-(3)/normalization follow, do a faithfulness read vs our L1 crosswalk rows |
| #937 / #942 | add-back input: quantified theorem + obstruction map; closest live motion to a paving missing input |
| #909 → | M1 first-match ladder ("next open obligation" queued); Codex-side relevance |
| #978 | top-seam incidence audit — first-match survivor counting refutations |
| #882 | payment-interface Lean scaffolding — where a future payment proof will land |
| #914 → #917 | the audit-repair cycle pattern (class-charge claims falsified then repaired) — calibrates how much to trust unaudited packets |
| #935 | Danny's fixed27 cubic source-projection point — carries frozen external-Pro audit SHAs (new provenance pattern) |

## 8. Ecosystem shape (summary)

Four active contributors, ~35 PRs/day throughput, near-zero backlog (>48h ≈ empty), maintainer integrating in daily close-and-integrate waves (25 PRs swept today). The center of mass has shifted from L1/L2 frontier work to (a) the dense-shell/thresholds endgame descending from #827, (b) Route-D's systematic no-go mapping of the first-match/add-back territory around the paving paper's missing inputs, (c) M1's KoalaBear rank-nine ledger (Scott Hughes, 15 PRs), and (d) heavy Lean formalization + peer-audit culture (holmbuar auditing everyone, including counterexamples to peers' claims). No open PR approaches the MCA threshold / prize claims themselves — all packets explicitly fence that off.
