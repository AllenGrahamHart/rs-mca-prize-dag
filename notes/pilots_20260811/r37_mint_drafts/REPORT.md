All ten verifiers pass and write scope is clean. Here is the full report.

---

# REPORT — r37_mint_drafts (round 37, THE MINT WAVE, DRAFTED)

## VERDICT

**10 of 10 packages COMPLETE. 10/10 verify.py PASS, 0 FAIL**, all run under `tools/ramguard` from the repo root in a final end-to-end sweep.

| # | package | verify.py | profile | assigned status (PROPOSAL) |
|---|---|---|---|---|
| 1 | `statement_u` | **PASS** | tiny | TARGET (PROVED parts separated) |
| 2 | `l2_par_parametrization` | **PASS** | local | PROVED (+ one status split) |
| 3 | `l2_nonempty_theorem` | **PASS** | local | PROVED |
| 4 | `hr_dictionary_common_support` | **PASS** | local | PROVED + POSED (split advised) |
| 5 | `negation_closure_excess_fence` | **PASS** | local | PROVED |
| 6 | `la_eq_and_geometry_counterexamples` | **PASS** | local | PROVED + POSED |
| 7 | `share3_luroth_template` | **PASS** | local | POSED (mixed) |
| 8 | `outm_identity_degm` | **PASS** | tiny | POSED |
| 9 | `type2_ledger_scope_fence` | **PASS** | tiny | PROVED |
| 10 | `sat3_ledger_corrections` | **PASS** | tiny | HEURISTIC/RECORD |

Every package carries `statement.md` + `node.json` + passing `verify.py`; eight also carry `proof.md`. Packages 8 and 10 deliberately have none (POSED/HEURISTIC — a proof.md would overstate them).

## MISSES FIRST

**MISS 1 — anchor 1 was read PARTIALLY, exactly as pre-registered and never repaired.** I read A1:3186-3967 and A1:4270-4645 but **never A1:3967-4269** (Cycles 146-157). Nothing in the ten items traced there, but I cannot claim to have subtracted the drafts against that window. `critical/nodes/rate_half_band_crossing_location/statement.md:3962-4269` is unaudited by me.

**MISS 2 — my package-count prior was badly under-confident.** I registered 7/10 with P(10) = 0.15; the answer was 10/10. The registered P(all pass first run) = 0.12 was closer: **6 of 10 passed first run**. Of the four that did not, **three failures were my own bugs** (a print format; an inverted `r > R/2` inequality; a test point that included the bracket's excluded endpoint) and one was a genuine source defect I had encoded as an assertion (D8).

**MISS 3 — the verifiers replay statements; they do not re-run experiments.** Not verified anywhere: the (RES) converse; (LA-PADE)/(LA-DEG); the `h_r = 2rho` leg; the full `T = 95..98` census; the eleven other (L2) witnesses; the (D-F) `24x24` inversion; the `-1952 m^2` and `-61.3` bit figures; every DFS ceiling. **A PASS means the transcribed statement is self-consistent and matches banked constants — not that the original experiment was right.** This was zero-power declaration 2 and it held.

**MISS 4 — the packages are four files, not the exemplar's twelve.** The format exemplar carries `audit.md`, `certificate.json`, `claim_contract.md`, `dependency_subdag.md`, `provenance.md`, `result.md` and `verify_audit.py` as well. I drafted only the four the brief mandated. **Wiring will require the remaining seven per node**, including the independent `verify_audit.py` second code path that the exemplar uses to avoid single-implementation risk.

**MISS 5 — the `a*` projective convention is my inference.** It reproduces the banked `13`, which is evidence, not proof that it is the pilot's convention. Package 3 asserts it; if the coordinator rules the other way, that assertion flips (D1).

**MISS 6 — zero power over duplication.** My greps were negative for the new formulations, but package 6 turned up an already-banked family by reading, not by grepping (D12). There may be more.

## MANIFEST SUMMARY

Full detail in `notes/pilots_20260811/r37_mint_drafts/MANIFEST.md` (D2 deliverable): per package, source line refs, status rationale, what could not be verified, and suggested wiring.

Substantive results the verifiers establish, beyond transcription:

- **Package 2** rebuilds the banked `q=97`, `T=2` witness from `(f,g,h,k,L)` alone and re-certifies it end to end, and settles the "two conditions imply the third" claim **exhaustively over `F_13^4`**: exactly `144 = (q-1)^2` exception tuples, all of the form `f(ell)=g(ell)=0`, confirming the addendum's parenthetical under its natural reading.
- **Package 6** produces an H1+H2 exhibit with the **exact banked support profile** `[7,7,2,2,2,2,2,1,1]`, `T=9`, max pair-intersection `1`, nullity `1` — and makes the solve explicit: prescribing the five merged slope values turns the merge conditions **linear**, giving `10` equations on `9` unknowns, i.e. the addendum's "one scalar condition". It also verifies the generalized fence at a **fresh `m = 3`** (`60x48`, rank `42`, nullity `6 = 2m`).
- **Package 5** verifies the row-collapse mechanism **directly** on all `1158` covering even locators, and shows the bad set equals the covering set **as a set**, not merely in count.
- **Package 7** scans **every** constant-norm class at `q=193` exhaustively: max **31** collinear split cubics, **9152** lines at `>= 8`.
- **Cross-package:** `2r > R` at razor is ONE inequality carrying THREE fences — the type-2 vacuity (9), the razor row's `r > R/2` (5), and hence the necessity of an independent pigeonhole cap in Statement U (1). Recommend wiring as a cluster.

## DISCREPANCY (D3)

Twelve items in the addenda resisted precise statement.

**D1 — `a*` has no stated convention.** `A1:3583-3586` records `a* = 13 = 7m-1` on 5 of 6 witnesses and `12` on one. On the published `q=97` witness, `13` reproduces **only** under the projective reading (members read as degree-`rho` forms on `P^1`, roots at infinity counted); the affine reading gives `12` on the *same* object, because the leading coefficient `22+62z+z^2` vanishes at two parameters. **The round-35 F1 sentence is convention-sensitive.** Fix the convention before any F1/(NEWCAP) pricing.

**D2 — (RES) is stated as an "iff" but only half of it is hand-checked.** `A1:4363-4364` gives `det M(B) = 0 iff gcd(...) != 1` with a `1200/1200` two-field measurement. The coordinator hand-check list at `A1:4349-4355` does **not** include it. Forward direction is a one-liner; the converse is measured. Package 2 carries it as PROVED forward / MEASURED backward.

**D3 — the negation-closure count is stated without its hypothesis.** `A1:4465` gives `count = C(m-1, r/2-1)`. The general law is `C(m - off, r/2 - off)` with `off = m-(r+1)`; `C(m-1, r/2-1)` is its **`off = 1` face**. It fails at H4/H6/H7/H8 (`off = 2,2,2,3`), where the banked covering counts are `165/715/3003/1365` — all reproduced by the general form, none by the banked one. Not present anywhere in the repo (greps clean).

**D4 — locator count vs slope count are conflated.** At H3 the `330` bad even **locators** carry only **329 distinct slopes** (`f4_results.txt:10-11`). Only the slope count enters `T`. MISS-2 guard fired as registered.

**D5 — "the official row's own shape (`r <= R/2`)" is ambiguous and, at the crossing offset, false.** `A1:4496-4500` scopes the proved bound `B_ca^far(n-r) <= r+1` to `r <= R/2`. But at `a = k+2^34` the razor row has `r = 63*2^34 > 2^39 = R/2`. So the proved bound covers **neither** the exhibits **nor** the crossing offset — which is coherent only if "the official row's own shape" denotes an evaluation point outside the open bracket. The text does not disambiguate, and this is load-bearing: it is *why* Statement U needs its own pigeonhole cap.

**D6 — a missing closed form.** The corrected 2-sharing demand row `8, 25, 47` (`A1:3741-3745`) has a printed derivation **only** at `m=4` (`25 = 36+4-15`). Residuals over `3m(m-1)-rho` are `1, 4, 6` at `m=3,4,5`; no rule in the source generates them. The `m=5` value `47` is unreconstructible.

**D7 — two quantities inside one parenthesis.** `A1:3744-3746` reads "`D_max(m) = 4m-8`, LINEAR, for `m >= 7` (11 at `m=4`)". The hand-checked formula `(8m-9)-(4m-1)` gives `D_max(4) = 8`; the `11` is the **separate** calibration `D(3,3)` from `A1:4513`.

**D8 — an off-by-one.** `A1:4560-4562`: "required cross-coincidence `>= ~m-5`, VACUOUS for `m <= 6`, BINDING from `m = 7`". Literally, `m-5 = 1 > 0` at `m = 6`. The `~` makes the constant soft, so the **crossover at `m = 7`** is the load-bearing claim and the constant is not.

**D9 — BLOCKING: the first-moment gate's expression is never printed.** `A1:3846-3856` and `A1:4391-4392` give only calibrated values (`+13.75` at `q=17`, `-0.94` at `q=97`, `~ -1952 m^2` at official scale, `-61.3` at `q=97` after the dim-18 sharpening). **These are not mutually reconstructible**: a pure power law through the two `m=1` points needs exponent `5.85`, and `-0.94 - 2 log2 97 = -14.1`, not `-61.3`. Package 10's verifier deliberately refuses to recompute the bits. **Recover the formula from the pilot before this gate is re-priced or cited** — it is one of the four instruments the board leans on.

**D10 — opposite sign conventions in adjacent rows.** The locator-layer bookkeeping (`-5` at `m=2`, `+7` at `m=1`, `A1:3435-3436`) is sign-inverted relative to the TCAP ledger (`+3..+5` at `m=2`, `-9..-7` at `m=1`). "Agree in verdict" is true only after flipping. **The rows must never be added.**

**D11 — BLOCKING symbol collision, still unresolved.** `deg_H` names both the (DEG-m) quantity and the bipartite non-incidence degree in the PROVED `a1_core_one_active_partition_incidence_reconstruction`, inside the same `rate_half` family (`A1:3767-3771`). A rename must precede wiring package 8.

**D12 — duplication risk.** The `Z^m - X^{2m}` generalized fence is **already banked** in the coordinator addendum of `background/nodes/rate_half_layer_a_saturation_count_route_fence/statement.md:73-89` (nullity `2m`, `m = 2,3,4,6`, five fields). Package 6 must **cite, not re-claim**; its independent contribution is the `m=3` replay and the explicit H1+H2 solve. Related wiring gap: **neither fence node cites (RIC3)**, though `A1:4318-4321` records all three as faces of one mechanism.

## COMPLIANCE

**Compute law: CLEAN. 25 interpreter invocations, all via `tools/ramguard`, zero bare `python3` for any purpose** — no file patching, no probes, no heredocs. Profiles: `tiny` (256M/60s) for the four pure-arithmetic verifiers, `local` (1G/5min) for the six with linear algebra or enumeration; `RAMGUARD_TIMEOUT` set explicitly on every call (60/120/300/420s). Stdlib only, no Modal, no network, no git, no subagents.

**Write discipline: CLEAN.** All writes through Write/Edit. No `sed -i`, `awk -i`, `perl -i`, `tee`, or shell redirection onto any file.

**Results files: N/A by design.** No verifier writes a results file; each prints one `*_PASS` line to stdout and exits non-zero on failure. **No results-producing run was piped through `head`** — the final sweep captured output in a shell variable and printed it only on failure.

**Imported-script rule: OBSERVED, strictly.** Zero imports. I used the anti-import pattern the round-36 close recommends: **helpers duplicated into every file**. I *read* `r35_l2_gate/d1_structure.py`, `r36_hrlow/f1_family.py`, `f3_probe.py` and `f4_close.py` to learn the models — and confirmed each writes a results file at module scope (e.g. `d1_structure.py:277-279` opens its results path in `"w"` mode), which is exactly why none was imported or executed.

**Write scope: CLEAN.** A `find -newermt` sweep over the whole repo shows **zero** modified files outside `notes/pilots_20260811/r37_mint_drafts/`. No `dag/`, `nodes/`, `critical/`, `background/` or `tools/` edit; no git; no path containing `prize-codex-`; no scratch files outside my directory or in `/tmp`.

**Quarantine: OBSERVED.** `notes/pilots_20260802/CAMPAIGN_LEDGER.md` never opened. The three sibling round-37 directories (`r37_third_solve`, `r37_urand`, `r37_share3_gap`) never read; the parent was `ls`-ed once, which listed their names — names I already had from CONSTRAINTS, and no content was accessed. Every recursive grep carried the full `--exclude-dir` set **and** `--exclude=dag.json`; `dag.json` was never opened.

**Ordering: OBSERVED.** The `## Pilot registrations` section was appended to `PREREG.md` after the two anchors and **before** any other read, grep, `ls`, or interpreter invocation. Two anchor-scoped commands preceded it — the `## Round-3` header grep that PREREG itself instructs, and an `ls` of the exemplar's own directory, which PREREG defines as part of anchor 2. **Disclosed rather than assumed harmless.**

**CATCH-24A:** own-repo greps run before every novelty claim, including hyphenated and infixed variants (`constant-norm` / `constant norm` / `constant-normalized`; `C(m-off` / `r/2-off`; `roots at infinity`). The `constant-normalized` hits are a different object — the same trap round-36 bank 4 already documented and deflated.

**Zero-power declarations all held.** No status was assigned above what the source's own audit language supports; where in doubt I took the weaker (packages 7, 8, 10). The MISS-2 guard fired once for real (D4) and its pre-registered sample-quantities were all kept out of universal claims — in particular the `31`/`9152` constant-norm figures are labelled RAW-line counts, explicitly *not* superseding the source's structurally-verified `12/9/9`.
