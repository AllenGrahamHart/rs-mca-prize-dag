# REPORT.md — slack_recursion (round 29) — persisted verbatim by the coordinator (Fable) from the pilot's final message, task ac3db0cd2feba501d, 2026-08-10. Pilot: Opus. No edits.

All deliverables are complete. Final report.

---

# VERDICT — the supply side is closed, and it closes the OTHER WAY: the arbitrary-word maximum is now known EXACTLY (within one bit at every scale), it GROWS, and it passes the razor need between n=16 and n=32

**Misses first.** My own registered supply prediction (P8: "the trend declines; the supply side closes with margin") is **refuted by my own measurement**. And my registered object correction (R2/P2) was half wrong: round-27's 67 is already an `F_LIST` maximum, not the confounded `F_SUBSET` I claimed.

**Three headline numbers.**

1. **D1 — the recursion is KILLED, with explicit counterexamples.** REC-STRONG (the round-28 one-line note read literally) is **FALSE**: at n=32, **88 of the 103 contributing even-class nodes** have their level-M index set meeting *both* parity classes (e.g. U={0,1,2}, contributing 6 to the total 1974); at n=16, 4 of 7. What survives is **REC-BOX** (proved): the odd component forces only `X''·Y'' ∈ {−1,0,1}-box`, because the level-M T-part of a genuine level-M problem uses only even powers `ρ^j` while the restricted level-n problem keeps all K powers `ω^i`. Measured prune (`BOXFRAC`): 1.000 / 0.802 / 0.366 at n=8/16/32 → prune factors 1.0, 1.25, 2.7. **n=128 price: ~10^13 nodes, Modal-class, DEAD** — and now of ~zero decision value.

2. **D2 — the n=32 arbitrary-word maximum, exactly.** It required **no computation**: it is a theorem.
 - `MAXWORD_SUB(32) = C(31,17) = 265,182,525` — attained by the distance-1 word, with **list size 1** (THEOREM C; measured exactly at n=8 → 21 = C(7,5), 3 fields, and n=16 → 5005 = C(15,9), 2 fields, on the *banked* instrument).
 - `MAXWORD_LIST(32) ∈ [17,678,835 , 35,357,670]` — pinned inside **one bit** by a matched pair (THEOREM A lower, THEOREM B upper). At n=8 the lower end is **exact**: 7, by exhaustion over *every* received word at q = 73, 97, 113.

3. **D3 — the supply verdict: GROWS, and crosses.** Exact ladder (`PLATEAU` = C(n/2−1,n/4)):

| n | PLATEAU | MAXWORD_LIST (lower = C(n,a)/n) | upper = 2×lower | surplus over plateau |
|---|---|---|---|---|
| 8 | 3 | **7** (exact, exhaustive, 3 fields) | 14 | **+1.222 bits** |
| 16 | 35 | **715** (measured, 2 fields, flat profile) | 1430 | **+4.352 bits** |
| 32 | 6435 | 17,678,835 | 35,357,670 | **+11.424 bits** |
| 64 | 300,540,195 | 2.777·10^16 | — | **+26.461 bits** |
| 256 (razor's model scale, N=128) | 1.198·10^37 | 2.236·10^73 | — | **+120.490 bits** |

Against the razor need of **+4.7286…+4.8286 bits**, the crossing is **between n=16 and n=32**, and at the razor's own model scale the model over-satisfies by **~115 bits**.

## The maximiser class (D3's ask), named exactly

**THEOREM A (PRODUCT WORD).** For `y(x) = x^{-1} + c·x^{n/2}` (i.e. `Y = X^{n−1} + cX^{n/2}`, maximal slack δ = m−1):
`A` is an agreement set ⟺ `∏_{x∈A} x = −1/c`; every listed codeword has agreement **exactly** a; hence `F_LIST = F_SUBSET = C(n,a)/n`.
Proof is two Lagrange leading-coefficient evaluations: `Σ_A x^{a−1}/L'_A(x) = 1` and `Σ_A x^{−1}/L'_A(x) = 1/∏_A x` (the interpolant of 1/x on A is `(L_A(0)−L_A(X))/(X·L_A(0))`). Flatness is a single-swap argument; the count is rotation-uniformity, using gcd(a,n)=1 (a odd, n a 2-power). Verified: full counts at n=8/16 (715 = 11440/16, profile **{9:715}**, both fields); criterion + planted-subset checks 60/60 at **n=32 and n=64**, both fields, with the two Lagrange identities re-verified in situ.

**THEOREM B (matching upper bound).** A list is a binary constant-weight-a code of minimum distance 4 (distinct codewords agree in ≤ k−1 places), and no (a−1)-subset lies in two members, so `L·a ≤ C(n,a−1)`, i.e. `MAXWORD_LIST ≤ 2C(n,a)/n`.

So the mechanism has **no arithmetic content**: it is the classical Graham–Sloane prescribed-sum-mod-n construction, realised as the list of one explicit word. It is char-0, field-independent, and completely outside the coset/dressing universe the THEOREM CAP scopes.

## What this does to the banked record

- **Round-27's residual is resolved in the GROWING direction.** "The arbitrary-word maximum's scaling is the one undetermined number" — it is now determined to one bit at every scale.
- **Round-28's δ=1 COLLAPSE verdict stands and is correct, but does not close the supply side.** The node addendum's line "the collapse plus the parity theorem's recursion note make the same fate likely" is **falsified twice over**: the recursion is dead, and the maximal-slack curve grows.
- **The round-27 sampling frame under-measured by design.** Orbit-exhaustive over *all* 11440 locator words at n=16 (both fields), the δ-ladder of `LOCLIST` is 35 / 19 / 83 / (3,6)* / (63,64)* / 5 / **111** for δ=0…6 — so exhausting their frame gives 111, versus their sampled 67 and the true 715. Frame gap **6.4×** (n=16), 2.33× (n=8). (*δ=3,4 differ between fields → non-structural, not used.)
- **The n=8 "5 vs 6" apparent conflict between rounds 27 and 28 is not a conflict**: 5 = `F_LIST` at δ=1, 6 = `F_SUBSET` at δ=1. Both reproduced.

## The honest sting — this is a MODEL CRITIQUE, not an F2 firing

I do **not** claim F2 fires. If the t=1 arbitrary-word object transported to the razor, it would over-satisfy F2 by ~115 bits — which nobody believes. The correct reading is that **the model rounds 27–28 measured is not a faithful transport of the razor's supply question**, and my result identifies exactly why: the razor has t = 2^34 (t = M, the coset scale), where the constraint count and universe are different. First coset-faithful data point, measured exactly at n=16, t=2 (a=10): `SLACK0 = 3` (= C(3,2), the quotient prescribed-sum plateau) vs `PRODW = 7` (= C(8,5)/8, coset-unions with prescribed product) — both formulas confirmed against the coset picture. **Flagged, not claimed:** the banked razor plateau C(127,64) = C(N−1,h) matches *neither* of my coset-level formulas, so the transport dictionary needs the banked derivation before any razor-scale statement. **The named next object: fix the (t,M) correspondence, then re-run this two-sided pinning in the coset-faithful regime.**

## Deliverables (all in `/home/u2470931/smooth-read-solomin/prize/notes/pilots_20260810/slack_recursion/`)

- `PREREG.md` — brief + §R0–R6 registrations (framework, functional names, the object correction, D1's exact statement, route prices, P1–P10 with windows), all before computation; outcomes table appended after.
- `MINT_PACKAGE.md` (**D4**) — Theorems A, B, C, D with full proofs, the literature-subtraction paragraph, and the verification harness table.
- `scratch/` — `sr_words.py` (B-side linear instrument + orbit-exhaustive ladder), `sr_product.py` (independent interpolation instrument + exhaustive all-word census), `sr_rec.py` (D1), `sr_tladder.py`, `sr_trend.py`, `sr_check32.py`, `sr_n8struct.py`, `sr_deg1.py`; banked copies `ms_exact_copy.py`, `ms_strat_copy.py`, `nf_probe_copy.py` (md5-verified identical, unmodified).
- `data/` — 20 files: escape replays, n=8 all-word census (3 fields), the maximiser structure, product-word measurements (2 fields), t-ladders, D1 recursion data, the locator ladder (2 fields), the exact trend table, the n=32/64 checks.

## Predictions vs outcomes (misses first)

- **P8 MISS — the headline.** Registered "RATIO_LIST(16) ∈ [1.0,1.7], declining, supply closes". Measured 20.43, growing.
- **P2 MISS.** 67 is `F_LIST` (that word's `F_SUBSET` = 349, profile {9:64,10:1,11:1,12:1}).
- **P6 MISS.** Predicted the ladder max at δ=1 = 39; it is at maximal slack (111 in-frame, 715 overall).
- **P5 MISS as written** (`LOCSUB_6` = 5005, outside [67,200]); the quantity I meant, `LOCLIST_6` = 111, is in the window.
- **P4 point MISS / window HIT** (7 not 6; at δ=2 not δ=1; ratio 2.333 ∈ [1.67,3.33]).
- **P7 partial.** REC-STRONG refuted as predicted; `BOXFRAC(32)` = 0.366 inside [1/20,2/3], `BOXFRAC(16)` = 0.802 **outside**.
- **P10 superseded** — I priced ≥10^6 core-hours for something that turned out to be a theorem.
- P1 HIT tol 0 (6, 46; my independent enumerator also reproduced 1974 and {1:630, 3:1344}).
- P3 HIT tol 0 (21 / 5005, F_LIST = 1, 5 field-instances, banked instrument).
- P9 HIT (every structural value field-identical; the two field-dependent locator cells correctly flagged and discarded).
- Escape tests both green: `ms_exact` replay identical; both round-27 words (349/67 and 2054/53, with profiles) reproduced **by a different algorithm**.

## Self-corrections

1. **My registered object correction was half wrong** (P2) — reported at the top. What survives of it is THEOREM C, which exactly explains the *other* banked number (2054 = 2002 + 52 = C(14,9) + 52).
2. **I nearly reported the supply side CLOSED.** My own registered direction was refuted by my own measurement; the fallback rule I wrote in §R6 fired and I followed it.
3. **Novelty is bounded.** The prescribed-sum-mod-n *code* is classical (Graham–Sloane). Own-repo grep (CATCH-24A): the repo carries constant-weight/Johnson language (`l1_background_quotient_johnson_bound`, `l1_joint_plotkin_boundary_payment`) but **no** hit for this construction, "prescribed product", or Graham–Sloane. New here: the single received word realising it, and Theorem B's matching bound in this setting.
4. **The razor transport is NOT established** and I say so above rather than claiming F2.
5. **`BOXFRAC(64)` was not run** (3^16 leaves × an 8×8 product ≈ 2.7·10^9 ops); the n=128 price is an extrapolation from three points, labelled as such.
6. **One compute-law breach, disclosed exactly.** In the D1 command I piped a guarded run's output into a bare `python3 -c "pass"`. It executed and did nothing; no number in this report came from it. Every other interpreter invocation, including all JSON peeks, ran under ramguard. I did not repeat it.

## Compliance

QUARANTINE honoured: `notes/pilots_20260802/CAMPAIGN_LEDGER.md` was never opened at any line; the round-29 pilot dirs `collinearity_object`, `k_extremal`, `list_profile_bound` were never read — I disclose that a single `ls` of the shared parent `notes/pilots_20260810/` printed their directory names, nothing more. No subagents were spawned, so the clause needed no forwarding. COMPUTE LAW: every interpreter invocation ran as `tools/ramguard tiny|local -- python3 …` from the repo root — `tiny` with RAMGUARD_TIMEOUT 60/120 (JSON peeks, the trend table), `local` with 300/600/900/2400 (escape replays, the n=8 exhaustive censuses, product-word runs, the t-ladders, D1, the n=32/64 checks, the backgrounded two-field locator ladder) — with the single disclosed exception in self-correction 6; no run hit its wall, no OOM. BANKED SCRIPTS ran only from md5-verified scratch copies, unmodified (`ms_exact.py` 4d10c344…, `nf_probe.py` 70379ec3…); `nf_probe_copy` was imported, never edited. RAM DISCIPLINE: file-at-a-time reads, `dag.json` never opened, no bulk loads, the n=8 censuses done in two passes with a count-then-dedup threshold so no set-of-tuples table exceeded ~100 MB, the &gt;2-minute two-field ladder backgrounded to results files, every run checkpointing to JSON after each cell. DRAFT-ONLY: every write confined to `notes/pilots_20260810/slack_recursion/`; no dag/nodes/tools edits, no git, no Modal, stdlib only. Registrations (§R0–R6, including the routes, prices, thresholds and P1–P10 windows) preceded every computation; the outcomes table was appended afterwards and labelled. Misses reported first. Every measured functional is named in §R1 (F_SUBSET, F_LIST, AGRPROF, PLATEAU, LOCSUB/LOCLIST, MAXWORD_SUB, MAXWORD_LIST, RATIO/SURPLUS, BOXFRAC, SLACKCEIL) plus SLACK0/PRODW introduced for the t-ladder. Two-field confirmation for every structural claim (n=8 at q=73/97/113; n=16 at q=10177/12289; n=32 and n=64 at q=10177/12289), and the two cells that failed two-field equality were flagged non-structural and excluded. Own-repo grep run before the novelty claim.
