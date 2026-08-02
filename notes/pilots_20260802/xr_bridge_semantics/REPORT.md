# Pilot report: xr bridge adjudication (Opus 5 subagent, 2026-08-02)

Coordinator note: this file is the subagent's final report, persisted
verbatim by Fable. The coordinator's verification record and adopted
posture are in FABLE_AUDIT.md alongside. Evidence citations JSON:
CITATIONS.json in this directory.

---

# VERDICT

**Classification: (b) — genuine gap, inherited.** The coordinator's leading hypothesis is *half* right and the wrong half is load-bearing.

- Right: the strip rung's trigger **is** the ">k points" condition, not the A-support condition. The bridge's prose does conflate them.
- Wrong: that does **not** make the proof safe. The strip rung does not merely *classify* the >k event — it claims to **charge and remove** it, and that removal is what delivers the `cores <= K` premise the bridge imports. The removal is **not proved** for cores in `[K+1, A-2]`. The only proved core-based payment in the banked tree fires at core >= **A-1**, not >= K+1.

**Repair forced: R2** (`Gamma_hi = {core >= K}`), and it is forced *jointly* with widening P-A1's predicate from "shares a size-`k` core" to "shares a core of size **at least** `k`". R1 is not merely non-forced — it is **unsafe**, because it relocates the band into P-A2, whose tangent-removal step provably requires `|T| <= n-A` (an A-support explanation).

**PROVED status: SAFE, conditional on the joint edit.** The bridge is routing-only. Under R2 the generic-branch partition becomes unconditionally disjoint-and-exhaustive with **zero** reliance on any core-cap premise, so the bridge's theorem survives as a statement-level edit. As currently written it is **not** sound. The edit is not cosmetic and must land on the bridge *and* P-A1 in the same change, or the routing remains incomplete.

A second, larger finding falls out: the flag has surfaced a genuine over-claim inside a different PROVED node, `xr_strip_classification_rungs` (item 3). That is the coordinator's call, not mine.

---

# EVIDENCE CHAIN

### Step 1 — the bridge's generic branch is triggered by A-supports and imports `cores <= K` from the strip

`critical/nodes/xr_tangent_support_mismatch_bridge/statement.md:12-15`
> "If no codeword pair jointly explains `(u,v)` on an `A`-support, select one exact-`A` support-wise bad ray per live slope. The proved strip/classification rung leaves selected agreement supports with pairwise intersections at most `K`."

`.../statement.md:18-19`
> "Gamma_hi={z: some z'!=z has |S_z intersect S_z'|=K}, / Gamma_lo=Gamma\Gamma_hi."

`.../proof.md:6-9`
> "In the second case the pair is in the original globally generic scope. **The proved strip rung makes all distinct selected support intersections at most `K`.** Declaring a slope high when it participates in an intersection of size exactly `K` and low otherwise gives a disjoint exhaustive partition."

The bolded sentence is the single load-bearing step. Note that `proof.md:3` is explicit that the case split itself is on A-supports — so the conflation is **in the proof**, not only in the statement. This already rules out classification (a).

### Step 2 — the verifier proves nothing about the premise; it *assumes* it

`.../verify.py:9-14`
```python
def partition(family, cap):
    assert all(len(left & right) <= cap for left, right in combinations(family, 2))
    high = { i ... if any(i != j and len(support & other) == cap ...) }
```
and `verify.py:29` only ever calls `partition` on families already filtered by `if all(... <= cap ...)`. So the 4-million-check green on this node is **conditional on `cores <= K`** and is silent on whether it holds in the generic branch.

### Step 3 — the strip node proves the *forcing*, and asserts the *charge*

`critical/nodes/xr_strip_classification_rungs/statement.md:11-14`
> "any two live rays at distinct slopes with a common core of size at least `k+1` determine a degree-`<k` codeword pair on that core **and therefore enter the tangent/classified branch**; hence the post-strip generic remainder has pairwise cores at most `k`"

`.../proof.md:18-22`
> "On every point of `R`, subtraction gives `g=v` and then `f=u`. Thus a distinct-slope pair with `|R|>=k+1` forces the received pair to a codeword pair on more than `k` points. **This is exactly the tangent/classified event removed before the generic remainder.** Consequently the generic post-strip family has pairwise cores at most `k`."

Everything up to "forces the received pair to a codeword pair on more than `k` points" is proved algebra. The next sentence — "removed" — is asserted by fiat. Nothing in the node derives it.

### Step 4 — the tangent strip's *actual* predicate does not fire on band cores

`critical/nodes/stratification_partition_thm/proof.md:85`
> `P2(u,v)  :=  EXISTS Z0, codeword c : agreement(u + Z0 v, c) = A0 > A   (tangent)`

`.../proof.md:45-48`
> "T2 tangent overlap ... agreement(u + Z0 v, c) = A0 > A -> TANGENT-PAID; ... price B_tan [PROVED-cited #147 range]."

T2 is a **single-slope over-agreement** condition. A distinct-slope pair with core `r in [k+1, A-2]` satisfies neither T2 (every slope still has agreement exactly `A`) nor the bridge's A-support trigger (the forced pair `(f,g)` agrees on `r < A` points). It is stripped by nothing.

### Step 5 — the only proved core-based payment is at A-1

`critical/nodes/xr_pencil_cascade/statement.md:9` (PROVED)
> "If a pair (u,v) has two aligned supports (distinct slopes) whose agreement sets share a common core of size **>= k+t-1 = A-1**, then the slope pencil is FORCED on the core ... and the pair is a TANGENT-PENCIL pair — **paid**."

The dag statement of the strip node concedes this in its own parenthetical: *"(graded band, cascade at r >= A-1)"*.

### Step 6 — charging the band was explicitly OPEN WORK, on a node that was cut

`archive/retraction_xr_20260705/xr_partial_tangent_band/statement.md:9` (status CONDITIONAL; **absent from dag.json today**)
> "Distinct-slope aligned supports with core r in [k+1, A-2]: ... **The work: design the GRADED tangent ledger charging depth-d partially-forced pairs** ... so that every band pair is either charged or upgraded toward the cascade threshold."

The consumer's own re-surgery list still treats this as live — `critical/nodes/xr_smallcore_spread_count/conditional.md:66-67`:
> "3. A post-strip live cross pair with core in [k+1, A-2] surviving the tangent ledger at any scaled row (breaks the rung-2b step)."

That criterion is *incoherent* if the strip already removed all such pairs. Its existence is proof that the program does not believe the strip removes them.

### Step 7 — the banked, SHA-pinned verifier itself uses R2 semantics

`xr_strip_classification_rungs/verify.py` pins `audit_p8p9_local_20260710.py` by SHA-256 and replays it. That file:

`critical/nodes/xr_smallcore_spread_count/notes/audit_p8p9_local_20260710.py:221-226`
```python
# H1: high-core counting implication (assembly step 5)
# high-core rays: rays sharing >= k core with another DISTINCT-slope ray
hc = set()
for a, b, J in cross:
    if J >= k:
        hc.add(a); hc.add(b)
```
**`if J >= k`** — the machine-checked high-core class is `{core >= K}`, i.e. exactly R2. The bridge's `= K` is a mis-transcription of its own verifier.

`.../audit_p8p9_local_20260710.py:188, 204` — F1 checks only the forcing identity, and reports `n_forced` = **4,662 non-vacuous core->=k+1 cross pairs** in the very fixture the strip node cites (`xr_strip_classification_rungs/proof.md:34`: "including 4,662 nonvacuous forced pairs"). Those pairs exist and are not removed by anything in the replay.

`.../audit_p8p9_local_20260710.py:214` — `if t - d_ <= 0:  # tangent event; cap not claimed (charged to strip)`. The tangent event fires at `d >= t`, i.e. pair-agreement `>= k+t = A`. The A-support trigger again.

### Step 8 — the program's own conventions document is R2, and is internally inconsistent with the strip node

`critical/nodes/xr_smallcore_spread_count/notes/F5_SKELETON.md:398-402`
> "(i)  HIGH-CORE stratum (some pair of supports shares **>= k** points, i.e. cores in **[k, A-2]**) ... (ii) LOW-CORE stratum (all pairwise cores <= k-1)"

`.../F5_SKELETON.md:360-365` — F5-OS counts live slopes "with pairwise cores **<= A-2**".
`.../F5_SKELETON.md:384` — "`>= t` such points give pair-agreement `>= k+t` = a TANGENT event".

`.../F5_SKELETON.md:25-31` shows the contradiction in one place: L1(ii) says core >= k+1 is "stripped", yet L1(iii) bounds the live class by `<= k+t-2`. If (ii) were true, (iii)'s bound would be `k`. The `k+t-2` is the honest number; the "stripped" is the drift.

The consumer's top-level dag statement agrees with the skeleton, not the strip: *"aligned aperiodic supports whose agreement sets pairwise share cores **< k+t-1**"*.

### Step 9 — the configuration is realized, and the band is non-empty on all six official rows

The pilot's exhibits are **proved globally generic**, not merely assumed:
`notes/pilots_20260802/pb_split_fibre_selector/pb_split_fibre_pilot.py:320-323`
> `# global genericity: joint agreement <= deg(V - c_1) = A - m < A` / `self.req("globally_generic_by_degree", ...)`

Max joint agreement `A - m = K+1 < A`: a genuine no-A-support pair carrying a joint codeword-pair explanation on `K+1 > k` points, with selected distinct-slope cores of exactly `K+1`. Measured: P3 17/97 and P5 46/46 slopes with core >= K+1 and **never exactly K** — under the current wording those land in neither `Gamma_hi` nor legitimately in `Gamma_lo`.

Band arithmetic from the dag pin `A = k + n/scale + 1`, scales 256/256/512 (verified via `tools/ramguard tiny`):

| row | K | t=h | A | band `[K+1, A-2]` |
|---|---|---|---|---|
| RowC 1/4 | 256 | 5 | 261 | [257, 259] <- pilot instance |
| RowC 1/8 | 128 | 5 | 133 | [129, 131] |
| RowC 1/16 | 64 | 3 | 67 | [65, 65] |
| prize 1/4 | 549755813888 | 8589934593 | 558345748481 | [549755813889, 558345748479] |
| prize 1/8 | 274877906944 | 8589934593 | 283467841537 | [274877906945, 283467841535] |
| prize 1/16 | 137438953472 | 4294967297 | 141733920769 | [137438953473, 141733920767] |

Non-empty on **every** candidate — and astronomically wide on the prize rows. This is not a small-toy artifact.

### Step 10 — why R1 is unsafe, not merely unforced

R1 pushes the band `[K+1, A-1]` out of the generic branch and into the nongeneric one. The nongeneric branch's only removal step is `q_z = 0`, paid by `xr_true_tangent_coordinate_injection`, whose hypothesis is:

`critical/nodes/xr_true_tangent_coordinate_injection/statement.md:9-19`
> "`u=c_0+e_0, v=c_1+e_1, T=supp(e_0,e_1), |T|<=n-A` ... Then `# such slopes <= |T| <= n-A`."

With only a `K+1`-point explanation, `|T|` can reach `n-K-1 >> n-A`, and the node's own conclusion ("fits inside the printed `n-A+1` slot", L22-23) collapses. R1 therefore requires re-scoping P-A2's quantifier (`claim_contract.md:6`: *"per received pair having a joint `A`-support explanation"*) **and** re-proving its tangent-removal step.

Worse, that exact widening has already been refuted:
`background/nodes/xr_nondeep_tangent_supportwise_payment/statement.md:3,16-18` — **status: REFUTED**
> "This is false without a hypothesis such as the deep-regime condition `3r<=n-K`. A smooth rate-`1/4` counterexample over `F_17` has eight exact-`A` bad slopes while `r+1=6`."

### Step 11 — why R2 is forced

Set `Gamma_hi := {z : EXISTS z'!=z, |S_z intersect S_z'| >= K}`, `Gamma_lo := Gamma \ Gamma_hi`. Then:
1. The partition is disjoint and exhaustive **by construction**, with no core-cap premise — so it is immune to however the strip question is finally resolved.
2. `Gamma_lo = {z : FORALL z'!=z, |S_z intersect S_z'| <= K-1}` is *verbatim* P-B's banked predicate (`xr_lowcore_spread_heart/claim_contract.md:8`: "every selected support intersection is at most `K-1`"). P-B needs **no** edit.
3. It is already the semantics of the pinned verifier (Step 7), the conventions document (Step 8), the pilot instrument (`SELECTOR_MANIFEST.md:199-201`), and the Pro brief (`notes/pro_briefs_20260801/BRIEF_4_xr_lowcore_spread_heart.md:10-16`).

R2 is the only repair that is (i) purely statement-level, (ii) sound without new mathematics, (iii) P-B-preserving, and (iv) already what every downstream instrument computes. It is forced.

---

# DOWNSTREAM-CONSUMER TABLE

| Consumer | Edge | What it consumes | R1 | R2 | Verdict |
|---|---|---|---|---|---|
| **`xr_highcore_collision_count` (P-A1)** | `ev` out | `statement.md:7-13`: "post-strip live slopes whose selected agreement support shares a **size-`k`** core with another live member <= 8n^3" | unchanged | **must widen to "core of size >= k"** | FLAGGED — **relies on `Gamma_hi = {core = K}` exactly.** The mandatory paired edit. Note its own dag statement already banks "PROVED AROUND IT: post-strip pairwise cores <= k" — same over-claim as Step 3, must be corrected in the same pass. Cost: P-A1's true obligation becomes cores in `[k, A-2]` — which `F5_SKELETON.md:398` had already assigned to it. |
| **`xr_highcore_collision_count` (P-A2)** | `ev` out | `claim_contract.md:6`: quantifier = "per received pair having a joint `A`-support explanation" | **breaks** — quantifier must widen to ">k points", and the `\|T\| <= n-A` payment fails | unchanged | R1-fatal. Under R2, untouched. |
| **`xr_lowcore_spread_heart` (P-B)** | `ev` out | `statement.md:7-14` / `claim_contract.md:8`: intrinsic "all pairwise cores <= K-1" | scope hypothesis narrows (evidence base shrinks) | **unchanged, verbatim** | Safe under R2. Its `Gamma_lo` is already R2's `Gamma_lo`. |
| **`xr_smallcore_spread_count`** | `req` out (CONDITIONAL) | the 8+8 / 16 assembly | assembly survives but re-surgery criterion 3 (`conditional.md:66`) fires on the re-scoping | assembly unchanged; the `Gamma_hi U Gamma_lo = Gamma` step becomes unconditional | Safe under R2. Its own dag statement ("cores < k+t-1") is already R2-consistent. |
| **`xr_quotient_global_core_collision_router`** (background) | `ev` into bridge; routes *into* P-A | `statement.md:38-40`: "Every still-live generic-branch slope in `Z_collision` shares a **size-`k`** core with another live slope and is therefore in the exact class quantified by `xr_highcore_collision_count`" | **breaks** — its slopes whose full core exceeds k would fall out of the generic branch | **repaired** — its `k`-set is contained in the full core, so core >= k => in `Gamma_hi` | R2 *fixes* an existing latent inconsistency here. Under the current `= K` wording this router's routing is already wrong whenever the core exceeds k. |
| **`xr_supportwise_transverse_lineray_rank_charge`** | `ev` into bridge | support-local transversality (`statement.md:32-34`) | neutral | neutral | Core-agnostic. Unaffected. |
| **`xr_true_tangent_coordinate_injection`** | `req` into bridge | `\|T\| <= n-A` A-support hypothesis | **incompatible** | unchanged | R1-fatal (Step 10). |
| **FM3** (P-B lane, `REPORT.md:73-75`) | not yet a node | "lex-first-match forces selected supports to contain `{x_0..x_{K-1}}` ... => `Gamma_lo` empty" | **self-defeating** — the prefix mechanism produces cores >= K+1, which R1 ejects from the generic branch entirely; FM3 becomes vacuous | **directly statable** — all cores >= K => every slope in `Gamma_hi` => `Gamma_lo = EMPTY` | Under the *current* wording FM3's conclusion is literally **false** (a slope whose every core is >= K+1 sits in neither set). This is precisely why the flag blocks FM3. **R2 unblocks it; R1 kills it.** |

`xr_clean_residual_any_gate` is **not** a direct consumer — `bridge/verify.py:65` asserts that edge does not exist.

---

# OPEN QUESTIONS I COULD NOT SETTLE FROM THE BANKED SOURCES

1. **Is the strip node's over-claim a status question?** `xr_strip_classification_rungs` is PROVED and its item 3 asserts band pairs are "tangent-charged". Under R2 the bridge no longer needs that claim, so the bridge is safe — but the strip node's own statement is unsupported by T2/P2 and by `xr_pencil_cascade`. Whether that is a prose correction, a scope narrowing (restate item 3 as: *forcing* proved, charge only at `r >= A-1`), or a status flip is a coordinator/maintainer call. I did not touch it.

2. **What is P-A1's real cost under R2?** Widening from `{core = k}` to `{core in [k, A-2]}` may or may not be free against the already-banked partial payments (the sunflower/pencil cap `(n-k)/(t-d)`, the rank ledgers, the AZC arithmetic). The sunflower lemma is keyed on a common **k-set** `W`, so it plausibly covers cores >= k unchanged — but I did not verify the rank-charge and Maxwell-deficit results survive the widened predicate. That needs its own pass before the P-A1 edit is written.

3. **Does `B_tan <= n-A+1` need re-derivation?** If the coordinator instead pursues the third route — *prove* the graded tangent ledger (the archived `xr_partial_tangent_band` work) — then whether the band's charge fits inside the existing `n-A+1` column is open, and `conditional.md:68` already lists "B_tan resolved above n-A+1" as a re-surgery trigger. I found no banked bound for the band.

4. **Notational hazard, unresolved.** `K` (node `.md` files for the bridge and P-B) and `k` (dag statements, the strip node, P-A1, all verifiers) denote the same object. I confirmed this by predicate matching (P-B's `.md` "<= K-1" == dag "<= k-1"; P-A1's "size-k core" against the bridge's "= K"), not by a glossary — the repo has none that I found. Any repair edit should pin one symbol, since the flag itself is partly a transcription failure across this boundary.

5. **Pilot scale vs official rows.** The `K+1`-core exhibits are constructed at pilot scale. The *band's non-emptiness* at the official rows is exact arithmetic (table above), but whether band-core configurations are *realized* by received pairs at official `A` is not established by the pilot and is not established anywhere I could find. This weakens the "concrete counterexample" framing while leaving the proof-gap argument (Steps 3-6) untouched — that argument is scale-free.
