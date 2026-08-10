REPORT — k3_chain_seams (round 30, ADVERSARIAL)

The harness blocks subagents from writing report files, so `REPORT.md` could not be created on disk — the coordinator should save the text below to `notes/pilots_20260810/k3_chain_seams/REPORT.md`. The four analysis scripts and the PREREG registrations *were* written to the pilot directory as directed.

**Headline: the chain does not hold together as written — 12 findings, 3 HIGH, one of them a NEW seam on an axis nobody has flagged (`q prime` vs `q = p^e`), with a razor-slice counterexample row exhibited by exact integer arithmetic.**

---

# REPORT — k3_chain_seams (round 30, ADVERSARIAL)

Mandate: try to BREAK the K3 conditional chain. Verdict up front: **the chain does not hold together as written.** Five separate seams, two of them in live proof text rather than history. The chain's *arithmetic* foot is clean and I could not break it; the chain's *quantifiers and scopes* are not clean.

MISSES FIRST, as required.

---

## 0. MISSES

**M1 — my headline prior was wrong in direction.** I registered (PREREG R3) `p ~ 0.6` on "no statement-level row bridge exists", with "a disclaimer rather than a usable hypothesis" at `p ~ 0.25`. The truth is the second branch, and much stronger than I framed it: the bridge is not missing and not merely disclaimed — it is **adjudicated dead by a dated in-repo verdict** (`notes/kernel_basis/WP5_RATEHALF_VERDICT.md:4-16`, 2026-07-10), and that verdict is quoted **verbatim inside the parent's own machine-readable shard** (`critical/nodes/rate_half_band_closure/node.json:9`, the `WP5 KERNEL-BASIS VERDICT` clause). I went looking for an absent text. The text was present, load-bearing, and the 2026-08-09 decomposition crossed it anyway. Looking for a hole was the wrong instinct; the finding was a contradiction, not a gap.

**M2 — the worst defect I found was on none of my four ranked candidates.** PREREG R2 ranked: (1) row bridge, (2) structural_surplus→band_closure scope, (3) the ledger's three-way gate, (4) complete_payment's "complete" vs "remaining". The single most serious thing in this report is **F1** — the parent's live conditional proof asserting a reduction that its own child has marked FALSE — and I did not anticipate that failure mode at all. My ranking was organised around *row scope*, and the worst seam was *staleness across a same-day correction*.

**M3 — compute miss, self-inflicted, cost one full ramguard wall.** My first exhibit script tested the razor-slice window with `math.log2`. For `q = p^2` with `p` just under `2^128`, `q` differs from `2^256` by about `2^170`, i.e. by `2^-86` relatively — far below float resolution — so `math.log2(q)` returned **exactly 256.0** for every candidate and the strict `&lt; 256.0` test rejected all of them. The loop ran until `tools/ramguard local` killed it at its 5-minute wall, and because the script was not `-u` the output was lost entirely (the task file contained only `ramguard: local profile reached its 5m wall limit`). I found it only by isolating and timing the loop. Fixed by replacing the float predicate with exact integer comparison against `floor(2^255.9) = iroot(2^2559, 10)`. This is a real methodological miss and it is embarrassing in this specific campaign: the node I was auditing (`critical/nodes/rate_half_kb_m2_r4_k3_allocation_inequality/statement.md:6-7`) literally instructs "Print, **without floating point**". I used floating point on a 256-bit exactness question. Recorded, not buried.

**M4 — ZERO POWER on the route compiler's own residual.** I reproduced (KBPRW-2), (KBPRW-3) and (KBPRW-4) exhaustively (§5, attack A5b), but the step *above* them — "the global positive loop cap and defect budget reduce **the parent's ten common orbits** to exactly five live orbits" (`background/nodes/rate_half_kb_m2_r4_coordinate_positive_residual_loop_workboard/statement.md:12-14`) — I took on citation. The parent's ten orbits are not derived in that file and I did not chase them. If the 13-route partition is wrong, it is wrong there, and my scan had **no power** over it.

**M5 — ZERO POWER on the mathematics.** Nothing in this report evaluates whether the KoalaBear algebraic geometry is correct. I audited quantifiers, row scopes, edge wiring, and integer bookkeeping. A chain can be seam-free in all four and still be false; a chain can also be mathematically perfect and still carry every seam below.

**M6 — novelty subtraction, partial anticipation of F3.** CATCH-24A grep turned up `notes/pilots_20260810/mca_safe_rewire/PREREG.md:176-181` (round-28 pilot, prior round, readable), which **pre-registers the question** underlying my F3: *"P8 (deployed extension rows, n = 2^21). I predict mca_safe's quantifier does NOT include the n = 2^21 deployed rows — they are K3's rows — 55%"*. So the question was asked before me. I read those lines to subtract properly. What I could **not** find is any banked *verdict*: the round-28 outcome text on the parent (`critical/nodes/rate_half_band_closure/statement.md:462-498`) reports the `a_safe`/HD1 result and two D4 precision fixes and says nothing about P8. My contribution on F3 is therefore the **verdict and its consequences**, not the question.

---

## 1. D1 — THE CHAIN, QUOTED (both sides of every link)

### LINK 1 — `rate_half_band_closure` ⇐ {structural_surplus, crossing_location}

**Parent consumes (gate `all`):**

- `critical/nodes/rate_half_band_closure/node.json:231` — `"gate": "all"`; `node.json:237-245` — `requires` from `rate_half_band_structural_surplus` and `rate_half_band_crossing_location`.
- `critical/nodes/rate_half_band_closure/conditional.md:9-11` — *"`rate_half_band_structural_surplus` — the K3/workboard arm: the enumerated structural-supply cap at the deployed rows"*.
- `critical/nodes/rate_half_band_closure/conditional.md:19-22` (Claim) — *"Conditional on the two children, the rowwise adjacent certificate of (RH-ADJ) holds at every admissible razor row with the crossing located, and the enumerated arm certifies the absence of unaccounted structural supply at the deployed rows."*
- `critical/nodes/rate_half_band_closure/conditional.md:26-27` — *"The two children partition the node's open content exactly as the round-27 rebuild established it."*

**Child 1 supplies:**

- `critical/nodes/rate_half_band_structural_surplus/statement.md:11-13` — *"Conditional on the exact `m=2,r=4` K3 distinct-slope budget ledger and fresh independent review, the deployed-row structural-supply arm has no unaccounted surplus."*
- `.../statement.md:35-38` (Scope) — *"The workboard rows are n = 2^21 extension rows; transport to the n = 2^41 prime razor rows is NOTE-LEVEL (the WP5 quantifier mismatch stands). This child feeds the parent as the enumerated structural-surplus arm, **not as razor-row coverage**."*
- `.../conditional.md:21-23` — *"no unaccounted structural supply remains at the deployed rows. The conclusion does not transport this result to the prime razor rows."*
- `.../node.json:9` — *"Scope remains the n=2^21 extension-field deployed rows; no transport to n=2^41 prime razor rows is claimed."*

**Child 2 supplies:**

- `critical/nodes/rate_half_band_crossing_location/statement.md:11-15` — *"At every admissible row with n = 2^41, k = 2^40, **q prime, q = 1 mod n, 2^167 &lt; q &lt; 2^256** … locate the exact adjacent crossing a_RH(q) of (RH-ADJ)"*.

**Verdict on link 1: SEAM (three distinct ones — F1, F2/F3, F6).** Child 1's stated conclusion is scoped to `n = 2^21` and explicitly disclaims razor-row coverage; the parent's own round-29 flag (`statement.md:502-509`) says *"this node is posed AT n = 2^41, k = 2^40 ONLY … Rate-1/2 rows with s &lt; 41 are OUTSIDE this node"*. So a gate-`all` premise of the node states content the node's own scope flag places outside it. The parent's restatement of child 1 is scope-faithful — but the *partition* claim at `conditional.md:26-27` is not, and the far-CA sentence at `conditional.md:29-31` is false. Details in §2.

### LINK 2 — `structural_surplus` ⇐ {ledger, independent_review}

**Parent consumes:**

- `critical/nodes/rate_half_band_structural_surplus/conditional.md:8-11` — the ledger *"prints and proves the **active same-owner distinct-affine-slope total**, including the eleven residual positive routes and source-cover assembly, and fits the active K3 allocation."*
- `.../conditional.md:12-13` — independent review *"supplies fresh mathematical and custody review of **the complete load-bearing sub-DAG**."*
- `.../conditional.md:20-22` — *"Their conjunction therefore proves that no unaccounted structural supply remains at **the deployed rows**."*

**Ledger supplies:**

- `critical/nodes/rate_half_kb_m2_r4_k3_distinct_slope_budget_ledger/statement.md:3-8` — *"Conditional on the three wired premises, **the active row** and first-match manifest have the literal finite ledger `U_K3 = U_positive + U_sourcecover &lt;= U_K3_allocation`."*

**Independent review supplies:**

- `critical/nodes/rate_half_kb_m2_r4_k3_independent_review/statement.md:3-6` — *"Fresh independent review must cover **the final load-bearing K3 sub-DAG** at pinned commits."*
- `.../node.json:8` — enumerates exactly four certificate families: *"the load-bearing c112, coordinate-route, orientation-assembly, and distinct-slope composition certificates"*.

**Verdict on link 2: TWO SEAMS (F5, F11).** (a) Every premise in the subtree below is pinned to **one** row — `ledger/statement.md:3` "the active row"; `allocation_inequality/statement.md:16` "the exact active KoalaBear `m=2,r=4` **row**"; `orientation_assembly/node.json:8` "the active KoalaBear m2 r4 first-match residual"; `remaining_route_payment/statement.md:21` "the active first-match ledger" — while the conclusion is stated over "the deployed **rows**" (plural), twice. (b) The parent asks for review of the *complete* load-bearing sub-DAG; the child's shard promises review of *four named families*.

### LINK 3 — ledger ⇐ {complete_payment, orientation_assembly, allocation_inequality}

**Parent consumes:** `ledger/node.json:18-22` (`requires`, all three); `ledger/statement.md:22-25` names the same three; `ledger/conditional.md:3-15` uses `U_positive` from premise 1, `U_sourcecover` + exhaustiveness/disjointness from premise 2, and the printed comparison from premise 3, plus *"The source-line and negative coordinate values are zero by the two proved evidence theorems."*

**Children supply:** `complete_payment/statement.md:9-13` — *"the positive coordinate orientation has the literal bound `U_positive = U_remaining`"*; `orientation_assembly/statement.md:3-14` — *"Prove an active-first-match, same-owner partition of every residual KoalaBear `m=2,r=4` **balanced-core** bad slope into: source-line | coordinate | source-cover … The theorem must print their disjoint total `U_sourcecover`."*; `allocation_inequality/statement.md:6-14` — the five printed integers and `U_K3 &lt;= U_K3_allocation`.

**The two "proved evidence" theorems are real and correctly wired** (verified, §5 attack A5): `rate_half_kb_m2_r4_diagonal_c2_112_source_line_complete_exclusion` and `rate_half_kb_m2_r4_coordinate_negative_complete_exclusion` are both **PROVED**, both carry `evidence_for → ...k3_distinct_slope_budget_ledger`.

**Verdict on link 3: ONE LOW-SEVERITY QUALIFIER DROP (F12), otherwise clean.** The partition composes: `U_K3 = U_sourceline(0) + U_coordinate (= U_negative(0) + U_positive) + U_sourcecover`. The one gap is that premise 2 quantifies over **balanced-core** bad slopes and neither the ledger's statement nor its shard carries that qualifier forward. See F12 — I believe this is constitutive rather than material, and I say why.

### LINK 4 — `complete_payment` ⇐ `remaining_route_payment`

**Parent consumes:** `complete_payment/conditional.md:3-8` — *"The workboard theorem proves that its 13 printed routes are exhaustive. … The remaining-route premise names and pays the other eleven with exact total `U_remaining`. These sets are disjoint and have size `1+1+11=13`."*

**Child supplies:** `remaining_route_payment/statement.md:11-24` — the eleven routes listed literally, plus the discipline conditions.

**Verdict on link 4: NO SEAM, and the attack had power.** Machine-checked in §5 (attack A5c): 11 distinct + 2 distinct, zero overlap, 13 total, and the enumeration matches a **second, PROVED** source verbatim (`...coordinate_positive_residual_loop_workboard/statement.md:56-62`, (KBPRW-4)). This is the cleanest link in the chain.

---

## 2. THE FIVE SEAMS

### F1 — HIGH. The parent's live conditional proof asserts a reduction its own child has marked FALSE.

`critical/nodes/rate_half_band_closure/conditional.md:27-31`:

&gt; "Child 2 supplies the located crossing: B_mca(a_RH) &lt;= B* &lt; B_mca(a_RH - 1) with a_RH pinned — **the far-CA half is discharged unconditionally at razor rows by the Hankel layer (B* &gt;&gt; n)**, and the child's content is **the S_sparse localization**."

`critical/nodes/rate_half_band_crossing_location/statement.md:45-51`, on the child's own identically-worded paragraph:

&gt; "**[THIS PARAGRAPH IS FALSE — round-28 P0 correction below, coordinator-verified from primary text: the Hankel layer's scope is r &lt; 2^39, i.e. a &gt; 3n/4 ONLY; on the open bracket [k+2^34, 3n/4) the far-CA term is not discharged and is in fact BINDING (the PROVED simple-pole floor's pair is column-far, payload B_ca^far(k+2^34-1) &gt;= 2^216 vs B* = 2^128). The open content is the FAR-CA crossing.]**"

and `.../statement.md:235-249`:

&gt; "**P0 (FORCED CORRECTION, coordinator-verified from primary text): the 'binding term is S_sparse alone' reduction — inherited from the round-27 (RH-AC) draft — is FALSE on the entire open bracket [k+2^34, 3n/4).** … **THE OPEN CONTENT OF RH-AC IS THE FAR-CA CROSSING on [k+2^34, 3n/4); S_sparse is dominated.** Own-repo grep: nothing in-repo carried this correction before."

**The correction landed on the child only.** Three parent texts still carry the refuted reduction:

1. `rate_half_band_closure/conditional.md:29-31` — quoted above. This is **live proof text**, not history, and it was **edited on 2026-08-10** (the mca_safe parenthetical at `conditional.md:35-41` is dated that day) — i.e. someone had this file open the same day the P0 correction landed and left the false sentence in place.
2. `rate_half_band_closure/statement.md:229-231` — *"the binding term is S_sparse alone (B_ca^far is free at razor rows since B* ~ 2^128 &gt;&gt; n, discharged by the Hankel layer); open content = min{a : S_sparse(a) &lt;= floor(q/2^128)}"*. Under the append-only convention this block is history and may stand — **but no later addendum corrects it**: I grepped `statement.md` for `ssparse_endpoints`/`P0`/`far-CA crossing` and the only later blocks are the round-28 `mca_safe_rewire` addendum (462) and the round-29 `k_extremal` flag (500).
3. `rate_half_band_closure/node.json:9`, DECOMPOSED clause — *"… rate_half_band_crossing_location (RH-AC: locate a_RH within the PROVED bracket [k+2^34, 3n/4]; **S_sparse is the binding term**; falsifiers F1/F2 …)"*. This is the shard that compiles into dag.json, the site and the artifact.

**Is it unsound?** Not in the implication direction: child 2's *obligation* is the full located crossing `B_mca(a_RH) &lt;= B* &lt; B_mca(a_RH-1)` and `B_mca = max(B_ca^far, S_sparse)` (`statement.md:124`, (RH-SPLIT)), so the child still owes both halves. The parent's error is in *describing what remains* — it understates the child's burden and mis-aims the parent's own falsifiers, which are written in the dominated term: `rate_half_band_closure/statement.md:237` — *"F2 exhibit **S_sparse**(k+2^34) &gt; B* at one row (fires safe)"*. A falsifier pointed at a dominated quantity cannot fire. **Blast radius:** anyone reading the parent to decide what child 2 must deliver gets the wrong object, and the parent's F1/F2 no longer protect the node.

### F2 — HIGH. The decomposition crosses an adjudicated no-transport verdict that the parent itself quotes.

`notes/kernel_basis/WP5_RATEHALF_VERDICT.md:4-21`:

&gt; "VERDICT: NO conditional close on K3. Two independent fatal points: (F1) SIDE MISMATCH … (F2) QUANTIFIER MISMATCH: K3 quantifies over the four deployed n = 2^21 rows (q ~ 2^186 extension fields, 31-bit prefix charges); razor rows are n = 2^41, 256-bit PRIME q … **No transport lemma exists; the ledger itself grades the bridge NOTE-LEVEL.** POSITIVE (ev-grade only): … **an ev-edge upgrade, not an amber.**"

The same verdict is carried verbatim in the parent's shard (`rate_half_band_closure/node.json:9`, `WP5 KERNEL-BASIS VERDICT` clause). Eight days later the same shard says (`node.json:9`, DECOMPOSED clause):

&gt; "DECOMPOSED (2026-08-09 …): this node is now **CONDITIONAL (gate all)** on its two children — **rate_half_band_structural_surplus (the K3/workboard arm** …)"

**"ev-grade only, not an amber" and "CONDITIONAL gate all on the K3 arm" are in the same field of the same file.** Honest subtraction, both ways:

- WP5's (F1) has partly gone **stale**: it argued the node's open content was purely deficit-side, and after the round-27 re-pose the open content is a *located crossing*, which has an upper-bound half. I do not claim (F1) still stands.
- WP5's (F2) is **untouched** by the re-pose, and the child agrees with it in its own text: *"the WP5 quantifier mismatch stands"* (`structural_surplus/statement.md:36-37`).

**D2 answer.** There is **no statement-level row bridge**. What exists is the opposite: a dated verdict of no-bridge, a child that repeats it, and a PROVED governing rule — `background/nodes/official_row_primes_pinning/statement.md:12-19` (status PROVED):

&gt; "a prize-facing certificate must be either: **uniform over the complete admissible family**; or **explicitly scoped only to the exact exhibit field it names**. A stand-in or named exhibit does not certify the universal family **without a proved transport theorem**."

Under that rule the K3 arm is legitimate *as an exhibit-scoped certificate* — and it does declare its exhibit (`F_(2130706433^6)`, `n = 2^21`). The defect is not the child. **The defect is that an exhibit-scoped certificate was wired as a gate-`all` req-premise of a family-scoped razor-row node.**

On the brief's "family territory" question: under POSE 3 (`notes/BAND_LANE_DEFINITIONS.md:198-208`, adopted 2026-08-10) the rate-half lane *is* the per-s family `n = 2^s, k = 2^(s-1), s = 1..41`, so an `s = 21` instance **is** family territory — but the *parent* was flagged the same day as `s = 41` **only** (`rate_half_band_closure/statement.md:502-509`: *"Rate-1/2 rows with s &lt; 41 are OUTSIDE this node"*). Both rulings are dated 2026-08-10 and they collide precisely at this node. And the arithmetic is stricter than either: the K3 row is not merely a different `s`, it is a row the parent's own quality gate rejects — `rate_half_band_closure/QUALITY.md:76` (**gate 1**): *"Row scope: `n=2^41`, `k=2^40`, `2^128&lt;q&lt;2^256`, and `n|(q-1)`"*, closing with *"The node stays TARGET until one printed `a_RH(q)` satisfies every gate."* Machine-verified (§5, attack A1): the KoalaBear row has `v_2(p^6 - 1) = 25`, so `2^41 ∤ q-1` — the K3 row **cannot** be an `n = 2^41` row at all, not even in principle.

### F3 — HIGH (structural). Child 1 serves no consumer bar, yet gate `all` makes it a blocker.

Every consumer bar of this node is served by **child 2 alone**:

- `rate_half_band_crossing_location/statement.md:93-111` (Consumer bars, round-27 verified): *"`adjacency_closing`: needs the LOCATED crossing … **The full pose serves it.** `mca_safe`: needs the safe half AT THE LOCATED INDEX — the SAME moving bar… `list_adjacency_closing`: no longer consumes this content."*
- `rate_half_band_closure/statement.md:307-313`: *"ONLY adjacency_closing has an open band lower-bound clause… mca_safe: upper half only. list_adjacency_closing: lower half ALREADY DISCHARGED…"*
- `critical/nodes/mca_grand/conditional.md:34-40`; `mca_safe/conditional.md:44-46`; `adjacency_closing/statement.md:9` — all consume the located crossing, none consumes an enumerated supply cap at `n = 2^21`.

So child 1 discharges **no** consumer obligation of this node. Under `"gate": "all"` it is nonetheless a hard blocker: `band_closure` cannot flip until a 20+-wave KoalaBear algebraic-geometry campaign at a different row completes. This is not unsoundness — a conjunction with a spare conjunct is *harder* to prove, never falsely green — but the consequences are real and asymmetric:

1. **Schedule hostage.** `band_closure → {adjacency_closing, mca_safe}` (verified, §5 A5) `→ mca_grand`. The prize spine is gated on a premise no consumer consumes.
2. **Read-forward risk.** When child 1 flips PROVED, the parent's Claim sentence conjoins an `s = 21` supply cap with an `s = 41` located crossing in one sentence (`conditional.md:19-22`). A reader who takes the sentence as a unit takes a razor-row structural-supply claim that nobody proved and that the child explicitly disclaims.

The honest repair shape (**not applied — AUDIT-AND-DRAFT**): either demote child 1's edge from req to ev, consistent with WP5's *"an ev-edge upgrade, not an amber"*, or keep it and state in the parent that child 1 is an exhibit-scoped rider with no consumer bar. Coordinator's call.

### F4 — MEDIUM-HIGH. **NEW SEAM**, on an axis nobody has flagged: `q prime` vs `q = p^e`.

Child 2 — the *only* child that owns a located crossing — poses at **`q prime`**:

`rate_half_band_crossing_location/statement.md:11-12`: *"At every admissible row with n = 2^41, k = 2^40, **q prime, q = 1 mod n, 2^167 &lt; q &lt; 2^256**"*.

The consumers do not:

- `critical/nodes/adjacency_closing/statement.md:9`: *"**For each admissible row**: the proved safe agreement a and proved unsafe agreement a-1 are ADJACENT"*.
- `critical/nodes/mca_grand/statement.md:9`: *"**For each admissible C**: exhibit adjacent a with `B_C(a-1) &gt; floor(q_line/2^128) &gt;= B_C(a)`"*.

And "admissible" is defined with `e` free:

- `notes/BAND_LANE_DEFINITIONS.md:159-161` (item 13): *"'admissible row' (the descriptor family — **`q = p^e`**, `n = 2^s`, `k = rho*n` under `q &lt; 2^256`, `k &lt;= 2^40`, `n | q-1`; s free)"*.
- `background/nodes/official_row_primes_pinning/proof.md:27-30` — the pinned prize fragments are *"assuming |F| is sufficiently large"*, *"for every choice of F, L, and k"*, *"k &lt;= 2^40"*, *"|F| &lt; 2^256"* — quantifiers over fields, not over primes.

The parent's live quantifier after the round-29 flag is *"every admissible rate-1/2 row AT n=2^41, k=2^40 — the live quantifier is over q, not the row size"* (`statement.md:503-505`). Nothing there restricts `q` to primes. The sub-`2^167` range is covered for **every admissible q** (`statement.md:162`: *"THE CROSSING IS DETERMINED for every admissible `2^128 &lt; q &lt; 2^167`"*). Above `2^167`, the only location-owning child says `q prime`.

**Therefore: rows with `n = 2^41`, `k = 2^40`, `q = p^e` (`e &gt;= 2`), `n | q-1`, `2^167 &lt; q &lt; 2^256` are inside the parent's quantifier and located by nothing.** This is the *same shape* as the E7 SCOPE SEAM that the 2026-08-10 widening was declared to resolve (`crossing_location/statement.md:17-30`; `adjacency_closing/conditional.md:123-128`) — the widening moved the **q-range** endpoint and left the **primality** restriction untouched.

**Exhibited, not argued** (§5 attack A4, exact integer arithmetic):

```text
p = 340282366920938463463374556854233333761      (prime, MR-20)
q = p^2                                          (so q is NOT prime)
q.bit_length() = 256      q &lt; 2^256              True
q &gt; floor(2^255.9)                               True   &lt;- INSIDE THE RAZOR SLICE
v_2(q-1) = 42   -&gt;  n = 2^41 divides q-1         True
k = 2^40, rate 1/2, k &lt;= 2^40                    True
B* = floor(q/2^128) = 340282366920938463463374506276698456066   (128 bits)
```

This row satisfies every clause of `QUALITY.md:76` gate 1 and every clause of the item-13 descriptor, sits in the **razor slice itself**, and is outside child 2's pose. A second exhibit at `q = p^2 ~ 2^201` is in the script output.

**Novelty subtraction (CATCH-24A), done before claiming:** `grep -rn "q prime\|prime q\|extension field\|extension-field\|non-prime\|composite q"` over the six band-chain node directories returns exactly three lines: `crossing_location/statement.md:11` and `:18` (the pose itself), and `rate_half_band_closure/notes/pro_brief_razor.md:17` (*"q prime in (2^255.9, 2^256)"*, the razor brief). **No line anywhere flags the exclusion.** The round-29 `k_extremal` work is on the **s**-axis only — its four flags are row-size flags (`notes/pilots_20260810/k_extremal/DRAFT_SCOPE_FLAGS.md:10-73`) and its band decomposition is `s`-banded (`:198-207`); `grep` for `prime` in that file returns only two `(p,e,s,rho)` descriptor mentions with no `e`-axis verdict. This seam is on the **e**-axis and is, as far as in-repo text goes, new.

**Honest caveat on severity.** If the campaign intends the razor slice to be prime-only by fiat, the fix is one sentence somewhere — but it must be *written*, and under `official_row_primes_pinning` (PROVED) an unwritten restriction makes the certificate neither family-uniform nor exhibit-scoped, which is exactly the state that node exists to forbid.

### F5 — MEDIUM. Singular "active row" → plural "deployed rows" across link 2.

Premises, all singular: `ledger/statement.md:3` *"the active row and first-match manifest"*; `allocation_inequality/statement.md:16` *"the exact active KoalaBear `m=2,r=4` row"*; `orientation_assembly/node.json:8` *"the active KoalaBear m2 r4 first-match residual"*.

Conclusions, plural: `structural_surplus/statement.md:35` *"The workboard **rows** are n = 2^21 extension rows"*; `.../conditional.md:21-22` *"at the deployed **rows**"*; `band_closure/conditional.md:22` *"at the deployed **rows**"*.

The only in-repo enumeration of "the deployed rows at n = 2^21" counts **four**, and two of them are a different field: `WP5_RATEHALF_VERDICT.md:11-12` *"K3 quantifies over the four deployed n = 2^21 rows"*; `rate_half_band_closure/notes/upstream_determination_datum.md:22-25,35-36` — *"KB MCA 1116047/1116048 …, M31 MCA 1116023/1116024 …"* and *"Caveat for reuse: **the M31 rows are extra-official** (circle domain, ε* = 2^−100, q = p'^4); the KoalaBear rows are official-shaped."*

Every node in the K3 chain carries the `kb_` prefix and `p = 2130706433`. **Nothing in the chain touches the M31 row**, which has a different prime, a different `ε*`, and a different domain. So either the plural is a typo for the single active KB row — in which case the conclusion should say so — or it is an unproved widening across link 2. One-line fix either way; flagged, not applied.

---

## 3. THE SHARD-LEVEL DEFECTS (machine-readable text, i.e. what compiles)

### F6 — MEDIUM. The parent's Claim was never widened when child 2 was.

Child 2's pose was widened 2026-08-10 from razor-only to `2^167 &lt; q &lt; 2^256`, and the E7 flag was declared *"RESOLVED by this widening, same day, **recorded on both nodes**"* (`crossing_location/statement.md:17-30`). The two nodes are `crossing_location` and `adjacency_closing` (`adjacency_closing/conditional.md:123-128`). **The node in between was not updated.** `rate_half_band_closure/conditional.md:13-15` still reads *"the located adjacent crossing a_RH(q) at every admissible **razor row**"*, and the Claim at `:19-22` still concludes *"at every admissible **razor row**"*. So the parent's stated conclusion is razor-only while its child now owns `(2^167, 2^256)` and its consumer quantifies over all admissible rows. The widened coverage exists in the child and in the consumer and is invisible in the node that sits between them.

### F7 — MEDIUM. A retired-as-unsound claim is still asserted in the parent's shard.

`rate_half_band_closure/node.json:9`, DECOMPOSED clause: *"the consumers are unchanged … **mca_safe's own inequality is HD1-dischargeable at q &gt;= 2^169**, premise-weakening a named follow-up"*.

Retired twice, in the same node's other files: `conditional.md:35-41` — *"the named premise-weakening follow-up onto HD1 is **RETIRED AS UNSOUND** — HD1 is an upper bracket END at 3n/4, and B_mca is nonincreasing, so it bounds nothing at the crossing"*; `statement.md:465-480` — *"**THE FLAGGED LEAD IS REFUTED** … The premise-weakening surgery is retired; mca_safe keeps this node as a premise."*

No later clause in the shard's statement field retracts it (the only later clause is the ROW-SIZE SCOPE block). This is a **live false sentence in the field that compiles into dag.json, the site and the artifact.**

### F8 — MEDIUM. The parent's machine-readable falsifier is the retired FLOOR v2 falsifier; the razor-row surplus direction now has no owner.

`rate_half_band_closure/node.json:11`:

&gt; "Pre-registered (v2): scaled rate-1/2 band-analogue rows with exact counts deviating from the first-moment determination beyond Poisson, sustained across &gt;= 3 scales (either direction: **structural surplus or anti-concentration failure**). Mechanism failures do NOT count."

But the round-27 forced correction fired that falsifier and killed both of its directions: `notes/band_decomposition_plan_20260809.md:65-74` — *"D0 = BROKEN … **FLOOR v2's own falsifier FIRED** (structural-surplus direction, by theorem). **BAND-AC is unstateable** (false in the random-word reading, tautological in the worst-word reading)."* And the shard's own DECOMPOSED clause says *"The **retired** FLOOR v2 two-directional falsifier splits per child (surplus direction → child 1, **re-scoped**; the location content → child 2's F1/F2)"*.

Follow the split: the surplus direction went to child 1 and was **re-scoped to deployed rows** (`structural_surplus/statement.md:40-45`, heading *"Falsifier (inherited, surplus direction, **re-scoped**)"*, body *"A **deployed-row** supply object outside the assembled classes…"*). Child 2's falsifiers are location falsifiers at one index (`crossing_location/statement.md:83-91`: F1 pushes the quotient floor; F2 is `N(y, k+2^34; q) &gt; B*` at the single index `k+2^34`; F3 is the zero-power declaration). **Net: no falsifier anywhere covers a structural surplus at razor rows away from `a = k+2^34`,** and the parent's own falsifier field still names the retired object. A node can flip green without the surplus direction ever having been testable.

### F9 — LOW-MEDIUM. The evidence migration the plan directed did not happen: 418 of ~422 edges never moved.

`notes/band_decomposition_plan_20260809.md:17-21` specified child 1 as the node that *"Consumes the kb_m2_r4 workboard (**existing ev edges migrate here** as the req-side once K3's labels-to-slopes conversion is audited)"*.

Measured (§5 attack A5, full shard scan, 2150 shards):

```text
rate_half_band_closure  ev-in total            : 555
   of which rate_half_kb_*  (KoalaBear n=2^21) : 418   (417 PROVED, 1 REFUTED)
   other                                       : 137
rate_half_band_structural_surplus  ev-in total :   4
```

So **~1%** of the KoalaBear evidence reached the child that was created to hold it, and the razor-row parent still carries **75.3%** of its evidence base from `s = 21` rows that its own round-29 flag places outside it. (Individual background nodes still declare `consumer: rate_half_band_closure` directly — e.g. `.../coordinate_positive_residual_loop_workboard/statement.md:10`.) The labels-to-slopes gate on the migration was never satisfied either; it was **superseded**: `notes/work_cycles/roadmap_r3/16-k3-aggregate-20260810.md:24-26` — *"The old generic labels-to-slopes placeholder has therefore been replaced by this critical sub-DAG"* — while `structural_surplus/node.json:10` still lists *"a labels-to-slopes conversion that changes any cell verdict"* as a live falsifier.

### F10 — LOW. The ledger→structural_surplus edge is double-wired (req + ev), uniquely across the band chain.

`ledger/node.json:24-26` declares `evidence_for → rate_half_band_structural_surplus` while `structural_surplus/node.json:21-24` declares `requires ← ledger`. The full-repo scan found **16** ordered pairs carrying both edge types out of 3913 req / 2400 ev; **15 of the 16 are internal to the KoalaBear workboard subtree**, and this is the only one crossing into the band chain — i.e. a residue of the ev→req promotion, not a convention. Effect: the same node counts twice in any evidence-weight or orbit view.

### F11 — LOW. Independent-review scope: "complete sub-DAG" vs four named families.

`structural_surplus/conditional.md:12-13` asks for review of *"the **complete** load-bearing sub-DAG"*; `independent_review/node.json:8` promises *"the load-bearing **c112, coordinate-route, orientation-assembly, and distinct-slope composition** certificates"*. The negative-coordinate complete exclusion (a five-branch PROVED subtree the ledger uses as a zero) and the raw `433-1b/O0a` workboard (15 cells / 1,575 labels / 25,200 signed systems) are not named; "coordinate-route" is ambiguous between them and the positive routes. Custody risk worth recording alongside it: `independent_review/statement.md:8-9` keeps the node TARGET *"until the review record names the reviewer, commits, commands, verdicts"*, and `node.json:8` adds *"Review of similarly named experimental packets or **self-review by the producing implementation is insufficient**"* — while the existing K3 review (`rate_half_band_closure/notes/k3_contributor_review_20260730.md:1-13`) is us replaying Scott Hughes's verifier and vice versa. Whoever signs the eventual record has to be outside both producers.

### F12 — LOW. The `balanced-core` qualifier is in the premise and gone from the conclusion.

`orientation_assembly/statement.md:3-4` quantifies over *"every residual KoalaBear `m=2,r=4` **balanced-core** bad slope"*; `structural_surplus/statement.md:28` also says *"exhaustive same-owner **balanced-core** routing"*. The ledger's own statement and shard carry no such qualifier. **I believe this is constitutive, not material** — `background/nodes/rate_half_kb_v4_tangent_source_atom/statement.md:48` treats balanced-core as one of the *"frozen Q and balanced-core predicates"* applied to *"the successive residuals"*, i.e. the residual class is defined by it. But I could not find one sentence saying so at the K3 stage, and a qualifier present in a premise and absent from the conclusion is exactly the shape the brief asks me to flag. One clarifying clause in the ledger closes it.

---

## 4. D3 — CONSUMERS' CONSUMERS (CATCH-24C)

**Question: is "located" ever weakened to "exists" or "bounded" along the decomposition + K3 chain? Answer: NO. The located quantifier survives intact.** Quoted on every rung:

- `critical/nodes/mca_grand/statement.md:9` — *"For each admissible C: **exhibit adjacent a** with `B_C(a-1) &gt; floor(q_line/2^128) &gt;= B_C(a)`, all conventions printed."*
- `critical/nodes/mca_grand/conditional.md:34-40` — *"`mca_safe` supplies the safe-side inequality **at the certified agreement index `a`**. `mca_unsafe` supplies the unsafe witness inequality at the lower agreement index `a - 1` — **THE SAME `a`** (round-28 quantifier audit, 2026-08-10: `a` is `a_safe`, **the located crossing**, and both premises are stated at it; **a safe point at a bracket end is not a legal instantiation**)."*
- `critical/nodes/mca_safe/statement.md:9` — *"`B_C(a_safe) &lt;= B*`"*, with `a_safe` unbound in its own prose and bound by its consumers (`crossing_location/statement.md:97-109`).
- `critical/nodes/adjacency_closing/statement.md:9` — *"For each admissible row: the **proved** safe agreement a and **proved** unsafe agreement a-1 are ADJACENT"*.
- `critical/nodes/rate_half_band_closure/conditional.md:19-21` — *"the rowwise adjacent certificate of (RH-ADJ) holds at every admissible razor row **with the crossing located**"*.
- `critical/nodes/rate_half_band_crossing_location/statement.md:14-15, 93-97` — *"**locate** the exact adjacent crossing a_RH(q)"*; *"needs the LOCATED crossing (adjacent certified indices — the moving bar). The full pose serves it."*

The round-28 audit already hardened the one place where weakening was attempted (the HD1 premise-weakening onto `mca_safe`) and retired it as unsound in both directions (`crossing_location/statement.md:98-109`, with the reductio: a free `a_safe` would be discharged at `a = n` by the PROVED `mca_full_agreement_endpoint`). I attacked this axis and **found nothing**; the attack had power (a single "bounded"/"exists" in any of the six clauses above would have been a kill).

**But the K3 arm is not on this axis at all.** `structural_surplus` supplies a *cap* ("no unaccounted surplus"), never a *location* — which is fine as an extra conjunct, and is exactly what makes F3 bite: no consumer clause anywhere requests it.

**The live D3 exposure is F4, not weakening**: the consumers' "each admissible row / each admissible C" is a **wider** quantifier than the located chain delivers, on the `e`-axis, and the round-29 `s`-axis flag on the parent (`statement.md:502-512`, *"FLAGGED, not resolved"*) plus this new `e`-axis gap means `adjacency_closing`'s and `mca_grand`'s for-each-admissible-row quantifier currently has **two** live uncovered directions where it believes it has none.

---

## 5. D4 — ATTACK LOG

Format: what I did / what would have counted as a kill / what happened.

**A1 — Row-bridge attack (D2).** Traced every row pin from `band_closure` down to the four K3 leaves; grepped `2130706433`, `deployed row`, `razor`, `K3`, `row-sharp` across `critical/`, `background/`, `notes/`; reconstructed the KB row from the node's own printed arithmetic and checked it against the parent's quality gate. *Kill = a stated, usable transport hypothesis with matching conventions on both endpoints (which would have made my prior R3 wrong and the chain sound).* **Result: no bridge; an adjudicated anti-bridge (F2).** Machine-verified from `attack_sections/00-koalabear-owner-and-q6-ledger.md:10-16`: `U_paid = n - a = 981104` with `a = 1116048` gives `n = 2097152 = 2^21` exactly; and `B* = floor(p^6/2^128) = 274980728111395087` reproduces the node's printed `B* - U_paid = 274980728110413983` **digit-exactly** (`274980728110413983 + 981104 = 274980728111395087`). `v_2(p^6 - 1) = 25`, so the KB row is not an `n = 2^41` row under any reading.

**A2 — Paraphrase-gap attack, link by link.** Read both sides of all four links and compared quantifier by quantifier (§1). *Kill = any clause the parent consumes that the child does not state.* **Result: F1 (the parent asserts a reduction the child marked FALSE), F5 (singular→plural row), F6 (razor-only Claim vs widened child), F11 (review scope), F12 (balanced-core qualifier drop).** Link 4 clean.

**A3 — Quantifier-weakening attack (D3).** Traced "located" through `mca_grand → adjacency_closing/mca_safe → band_closure → crossing_location`. *Kill = one "exists"/"bounded"/"for some a" in place of the located index.* **Result: NO KILL — the located quantifier survives every rung** (§4). Reported as a clean result *because the attack could have fired*, not as an assumption.

**A4 — Admissibility-axis attack (the new one).** Compared child 2's pose against the item-13 descriptor and the PROVED `official_row_primes_pinning`, then tried to *construct* a row in the gap. *Kill (against me) = no such row exists, or some text restricts razor rows to prime q.* **Result: SEAM (F4).** Rows exist in abundance; exhibited two, one inside the razor slice, all range decisions by exact integer comparison against `floor(2^255.9) = iroot(2^2559, 10)`. Script: `notes/pilots_20260810/k3_chain_seams/exhibit_extension_rows.py`. Own-repo grep before claiming novelty: three `q prime` hits total in the band chain, none flagging the exclusion; `k_extremal` is `s`-axis only.

**A5 — Owner/partition/edge attack.** Full scan of all 2150 node.json shards for req/ev edge structure. *Kill = a chain premise with no inbound wiring, a req edge into a node that does not exist, or a double-wired promotion residue.* **Result: F9 (418/422 evidence edges never migrated) and F10 (the one cross-lane double-wire).** Also confirmed positively: `band_closure req-out = {adjacency_closing, mca_safe}`, the two "proved evidence" zero theorems are genuinely PROVED and wired, and every K3 leaf is a true leaf (`requires: []`). Script: `notes/pilots_20260810/k3_chain_seams/dup_edge_scan.py`.

**A5b — Root-arithmetic attack (link 4's foundation).** Exhaustively re-derived (KBPRW-2)/(KBPRW-3)/(KBPRW-4) from the stated equations rather than trusting the printed tables. *Kill = a seventh outside orbit, a wrong orbit size, or a route table not reproducible from "total defect &lt;= 3 + a common loop forbids an outside loop".* **Result: NO KILL, and the attack had real power** — 6 orbits found, 6 claimed, zero missing, zero spurious; all six printed orbit sizes (3/3/3/6/6/3) reproduced; all five route rows reproduced exactly; 13 routes total; and the "five live orbits / seven labeled skeletons" bookkeeping is consistent. Script: `notes/pilots_20260810/k3_chain_seams/kbprw_reproduce.py`.

**A5c — Route partition attack.** Transcribed the eleven + two routes from the statements and checked disjointness and the count against a second PROVED source. *Kill = an overlap, a miscount, or a route in one text and not the other.* **Result: NO KILL** — 11 + 2 = 13, no overlap, matches (KBPRW-4) verbatim. Script: `notes/pilots_20260810/k3_chain_seams/route_partition_check.py`.

**A6 — Chronology-gap attack.** Compared the decomposition plan (2026-08-09) against what was executed, and the round-28 corrections (2026-08-10) against what propagated. *Kill = a design gate declared before surgery and never satisfied, or a correction that stopped short of a node that repeats the corrected claim.* **Result: both fired.** The plan's child 1 was *"no structural surplus above sigma_FM at the band radii"* (`band_decomposition_plan_20260809.md:17-18`) — a band-radii object referenced to a shared model node — and D0 = BROKEN destroyed `sigma_FM` (*"there is no sigma_FM model node to build"*, `:73-74`). The revised design then called the K3 arm *"(i) the K3/workboard arm (**unchanged** — the structural enumeration)"* (`:79-80`), but "unchanged" was not available: the executed child is a `n = 2^21` KoalaBear workboard cap, a different object from the dead band-radii one. That substitution is where F2/F3 enter. And F1/F7 are the propagation failures: two 2026-08-10 corrections reached the child and the consumer and skipped the parent in between.

**A7 — Falsifier-coverage attack.** Followed the FLOOR v2 falsifier split to see who owns each direction after the decomposition. *Kill = a direction with no owner.* **Result: F8** — the razor-row surplus direction is owned by nobody, and the parent's shard falsifier is still the retired object.

**ZERO-POWER DECLARATIONS (explicit, per PREREG R4).**

- **The route compiler's own residual.** No power over the reduction from "the parent's ten common orbits" to the five live ones (M4). My A5b scan starts *below* that line.
- **All K3 mathematics.** No power over any algebraic-geometry claim: genuine-pencil hypotheses, exact line multiplicities, ray compilers, the genus-two model, the torus reductions. I did not attempt them and nothing in this report should be read as evidence about them.
- **Whether `q` should be prime at razor rows.** F4 establishes that the restriction is *unstated*, not that it is *wrong*. I have no power over the campaign's intent; that is a coordinator/rules question.
- **Whether "deployed rows" (plural, F5) is a typo or a widening.** The text supports both readings; I cannot discriminate from in-repo text.
- **Upstream state.** I read no `prize-codex-` path and made no upstream comparison; every upstream fact quoted here is a quotation of our own in-repo record of it.
- **`balanced-core` (F12).** Weak power — I found supporting but not decisive evidence that the qualifier is constitutive, and I have declined to convert "I found no counter-text" into "there is no gap".

---

## 6. SUMMARY TABLE

| # | Severity | Seam | Live text? |
|---|---|---|---|
| F1 | HIGH | Parent's conditional proof asserts the S_sparse/far-CA reduction its child marked FALSE | **yes** — `conditional.md:29-31`, shard, statement |
| F2 | HIGH | Gate-`all` req wiring crosses the WP5 no-transport verdict quoted in the same shard field | **yes** — `node.json:9` |
| F3 | HIGH | Child 1 serves no consumer bar yet blocks the whole spine under gate `all` | **yes** — structural |
| F4 | MED-HIGH | **NEW**: `q prime` in the only location-owning child vs `q = p^e` admissibility; razor-slice row exhibited | **yes** — `crossing_location/statement.md:11` |
| F5 | MED | Singular "active row" premises → plural "deployed rows" conclusion | **yes** |
| F6 | MED | Parent's Claim never widened when child 2 was (razor-only) | **yes** |
| F7 | MED | Retired-as-unsound HD1 clause still asserted in the parent's shard | **yes** |
| F8 | MED | Razor-row surplus falsifier has no owner; shard falsifier is the retired FLOOR v2 one | **yes** |
| F9 | LOW-MED | 418 of ~422 KoalaBear ev edges never migrated to the child created for them | **yes** |
| F10 | LOW | ledger→structural_surplus double-wired req+ev (unique in the band chain) | **yes** |
| F11 | LOW | Review scope: "complete sub-DAG" vs four named families; producer-custody risk | **yes** |
| F12 | LOW | `balanced-core` qualifier dropped between premise and conclusion | **yes** |

**Clean (attacks with power, no kill):** link 4 route partition; (KBPRW-2/3/4) full reproduction incl. orbit sizes; the ledger's internal partition algebra; the located-index quantifier through all six consumer clauses; the two "proved evidence" zero theorems (genuinely PROVED and correctly wired).

**Nothing surfaced here is applied.** AUDIT-AND-DRAFT: no node, shard, edge, or status was touched.

---

## 7. COMPLIANCE

**Interpreter invocations: 11. All 11 went through `tools/ramguard`, all with the literal `--`, all launched from the repo root, all stdlib-only. Zero bare `python3` invocations.** Breakdown — `tiny` (256M/60s) ×7: shard-field print for `band_closure`; status/edge check of the three zero-contribution theorems; `c2_112` node listing; a timing micro-test of the prime search; the isolated razor-slice loop (**hit its 60s wall — the diagnostic that exposed M3**); `route_partition_check.py`; `kbprw_reproduce.py`. `local` (1G/5min) ×4: `exhibit_extension_rows.py` v1 (**hit its 5m wall, output lost to buffering — M3**); `dup_edge_scan.py`; the `band_closure` evidence-edge histogram; `exhibit_extension_rows.py` v2 (corrected, completed). **Two ramguard wall-hits, both disclosed above and both mine, not the tool's.** No Modal, no network, no git, no `sudo`, no sandbox override.

**RAM discipline.** `dag.json` was never opened — every graph fact in this report comes from `node.json` shards read one at a time (the scan script holds only edge tuples and `del`s each parsed object) or from `grep`. File-at-a-time reads throughout; the two large files in the chain (`band_closure/statement.md`, 512 lines; `crossing_location/statement.md`, 490 lines) were read in bounded windows after grepping for their section offsets, never whole. No bulk loads.

**Quarantine confirmed.** `notes/pilots_20260802/CAMPAIGN_LEDGER.md` was never opened at any line — it was excluded by an explicit `grep -v pilots_20260802` filter on every recursive grep in this session. The three quarantined round-30 sibling directories (`k3_orientation_assembly`, `k3_allocation_inequality`, `k3_splitbc_transport`) were never read; their **names** appear in one `ls` of the parent directory and nothing further. No path containing `prize-codex-` was read or written.

**Two disclosed reads outside the anchors, both permitted, both declared.** (i) `notes/pilots_20260810/k_extremal/DRAFT_SCOPE_FLAGS.md` — a prior-round (29) pilot dir, not quarantined, and cited by the node's own round-29 flag as the owner of the `s`-axis hole; read to perform the F4 novelty subtraction. (ii) `notes/pilots_20260810/mca_safe_rewire/PREREG.md:165-199` — a prior-round (28) pilot dir, not quarantined; a CATCH-24A grep hit showed it pre-registers the question behind F3, so I read the surrounding lines to subtract properly rather than claim priority I do not have (see M6). I had already appended my blind priors before either read.

**Write scope confirmed.** Everything I wrote lives inside `notes/pilots_20260810/k3_chain_seams/`: the `## Pilot registrations` block appended to `PREREG.md` (as the brief directs), `exhibit_extension_rows.py`, `dup_edge_scan.py`, `route_partition_check.py`, `kbprw_reproduce.py`. **`REPORT.md` itself could not be written — the harness blocks subagents from creating report files — so its full text is delivered in this message and needs to be saved to `notes/pilots_20260810/k3_chain_seams/REPORT.md` by the coordinator.** No `dag/`, `nodes/`, `critical/`, `background/` or `tools/` file was modified. No git operation of any kind was run. All four scripts are fresh, written in this directory; no banked script was executed in place.

**Blind-prior discipline.** Registrations were appended to `PREREG.md` after reading only the two named anchors and before any other read, as required. Scored: **R1** (P = 0.75 of at least one real seam) — HIT, and under-confident. **R2** (ranked weakest links) — MISS on rank 1 vs the actual worst (M2); the row bridge did turn out to be a seam, but not the severest one. **R3** (row-bridge status) — MISS in direction (M1); I predicted absence, the truth is documented contradiction. **R4** (zero-power pre-commitment) — honoured; six zero-power declarations recorded in §5, none converted into a "no seam" claim.
