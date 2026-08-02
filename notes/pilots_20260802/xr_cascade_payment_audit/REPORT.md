# Pilot report: pencil-cascade payment audit (Opus 5 subagent, 2026-08-02)

Coordinator note: subagent's final report, persisted verbatim by Fable
(HTML entities restored). Coordinator verification and adopted posture:
FABLE_AUDIT.md alongside. Evidence: CITATIONS.json, f17_cascade_check.py,
ceiling_arith.py in this directory.

---

# VERDICT

**UNSOURCED — and worse than unsourced: the payment claim's own strengthening is REFUTED in-tree, on a witness that satisfies `xr_pencil_cascade`'s hypothesis exactly.**

`xr_pencil_cascade` proves **forcing + cascade** (interpolation, two-slope inversion, the off-core upgrade map). Everything after the em-dash — "the pair is a TANGENT-PENCIL pair — **paid**" — is a **classification into a stratum whose price was never proved to cover this shape**. Specifically:

- **(a) T2/P2 does not fire.** The predicate is single-slope agreement `A0 > A`; the cascade's own upgrade map lands every upgraded slope at agreement **exactly `A`**. The cited source says so in the same sentence that proves the cascade.
- **(b) The coordinate-injection column does not cover it as stated.** Its hypothesis is `|T| <= n-A` (core `>= A`); a core-exactly-`A-1` cascade has `|T| <= n-A+1`, one notch outside. The injection *mechanism* extends (its proof never uses the hypothesis), but the extension is unbanked and yields exactly `n-A+1` — it **saturates the entire `B_tan` slot with zero slack, on all six official rows** (measured ratio 1.0000). And its explicit NONCLAIM leaves every non-pencil live slope of the same pair unpaid.
- **(c) No other banked column charges it.** `B_quot` is periodicity; the residual `R_post` target (`F5-OS`) is itself quantified at **cores `<= A-2`**, so the `A-1` tier sits in *neither* `B_tan` *nor* `R_post`. The only other source for `B_tan <= n-A+1` is (i) the **moving-root tangent FLOOR**, which is a *lower* bound (a construction, `LD_sw >= n-A+1`) — the cascade family *is* that construction — and (ii) the closed form `r+1` proved only under the deep hypothesis `3r <= n-k`, which **fails on all six candidates** (verified).
- **(d) Purely definitional.** "Paid" = membership in RK **clause (i)**'s paid taxonomy — and `rigidity_kernel` is status **CONJECTURE**.

`xr_pencil_cascade`'s PROVED status covers **forcing + cascade only**. Scope-narrowing candidate, same genre as the strip item-3 over-claim — the decision is the coordinator's.

---

# EVIDENCE CHAIN

### Step 1 — the node has no proof and no verifier; its own ledger scopes PROVED to the algebra

`critical/nodes/xr_pencil_cascade/proof.md:6-13` is the **entire** in-tree proof:

> `## Source` / `Vendored from the working record; primary artifact(s):` / `- experimental/notes/roadmaps/e27_exceptional_pair_census.md` / `## Ledger` / `PROVED (W1, PR #10, 70/70 replayed): the forcing lemma at core >= k+t-1 with the cascade, scale-free, E27-calibrated.`

`notes/` is **empty**; there is **no `verify.py`**; no verifier anywhere in the repo references the cascade. The ledger sentence itself names only "the forcing lemma ... with the cascade" — **not** the payment.

### Step 2 — the sole cited source proves the algebra and explicitly disclaims the charging

Upstream read-only source `/home/u2470931/smooth-read-solomin/rs-mca/experimental/notes/roadmaps/e27_exceptional_pair_census.md:154-162`:
> "**(b) The cascade (proved, elementary).** ... If `|T| = A-1`, EVERY point `p` off `T` with `v(p) != b(p)` upgrades exactly one slope `z_p = (a(p)-u(p))/(v(p)-b(p))` **to full agreement `A` on `T + {p}`**. So a core of size `A-1` forces multiplicity `~ n - |T|`; a core `>= A` forces all 97 slopes; a core `<= A-2` forces nothing"

`...:210-211` — E27's own caveat:
> ""Unpaid" is **not netted against the asymptotic ledgers here**; the census classifies raw alignments with chance-normalization instead."

`...:229-232` — the replay battery: S5/S6b/S6c verify constructed classification, forcing stratum, cascade replication. **What the 70/70 replay verified: the forcing/cascade algebra and census statistics. It verified no charging — E27 says so in its caveat section.**

`...:187-191` — what "paid" actually meant upstream: membership in the FACE 4 forcing chain into **clause (i)** — and `rigidity_kernel` (dag.json) is status **CONJECTURE**; clause (i) is the PAID TAXONOMY with "no positive in-branch definition".

### Step 3 — (a) T2/P2 provably does not fire on the cascade tier

`stratification_partition_thm/proof.md:85`: `P2(u,v) := EXISTS Z0, codeword c : agreement(u + Z0 v, c) = A0 > A (tangent)`; `proof.md:45-48`: "T2 tangent overlap ... `A0 > A` -> TANGENT-PAID ... price B_tan [PROVED-cited #147 range]."

E27's cascade map delivers agreement **exactly `A`**, never `> A`: at core `A-1`, a slope needs **two** cooperating off-core points to exceed `A`, and the cascade produces exactly one per point. The multiplicity upgrade does **not** imply single-slope over-agreement anywhere. (Core `>= A` does fire T2 — but core `>= A` between two exact-`A` selected supports means the supports coincide, forcing a joint `A`-support explanation, i.e. the **nongeneric** branch. The T2-firing case is precisely the case that never reaches the generic branch.)

### Step 4 — (b) the injection column: right mechanism, wrong slot, explicit nonclaim

`xr_true_tangent_coordinate_injection/statement.md:9-23` (PROVED): hypothesis `|T| <= n-A`; conclusion `# such slopes <= |T| <= n-A`. `proof.md:23-25` — the NONCLAIM: "The argument does **not** assert that an explaining codeword different from `c_0+z c_1` is tangent-paid. Those are precisely the support-mismatch slopes **retained by the consumer**." `claim_contract.md:8`: "**Bound:** at most `|T|<=n-A`, **stronger than the consumer's `n-A+1` slot**."

The injection's *argument* is hypothesis-free (`proof.md:3-21` uses only "a nonzero affine function of `z` has at most one finite root"), so it extends to `|T| = n-A+1`. But: (i) that extension is **nowhere banked**; (ii) it consumes the whole slot, destroying exactly the strictness the claim contract advertises; (iii) it is **per-pencil**, and nothing bounds the number of forced pencils per pair (Step 6 shows two).

### Step 5 — (c) the `n-A+1` number's real provenance: a LOWER bound, plus a deep-regime-only upper bound

`critical/nodes/staircase/statement.md:3-9` — the only in-tree definition of `B_tan` — is a sketch-tagged stub pointing upstream (confirmed by `notes/wave24_integration_20260727/STATEMENT_REMEDIATION.md:22-26`).

Upstream, `#147`'s proved content is a **floor**: `rs-mca/experimental/notes/audits/audit_prize_gate_unconditional_via_tangent.md:24-30`: "The proved **moving-root tangent floor** ... `LD_sw(C, a) >= n - a + 1`" — and its construction ("fixes a locator for `a-1` points ... and moves one root") **is the cascade family itself** (confirmed `qx11_topcore_globalness.md:206-210`).

The matching **upper** bound is deep-regime-only: `rs-mca/experimental/notes/thresholds/upaid_ledger_partial.md:63-64`: "Tangent closed form `r+1` under `3r <= n-k` on small rows; **range-fail when outside**." Measured (`ceiling_arith.py`): `3j <= n-k` is **False on all six candidates**. **Every official row is outside the range where the tangent upper bound is proved.**

### Step 6 — the in-tree REFUTATION already covers this exact shape, on a *stronger* hypothesis

`background/nodes/xr_nondeep_tangent_supportwise_payment/statement.md:3-18` — **status REFUTED**: joint explanation on **at least `A`** coordinates does NOT imply all support-wise bad slopes fit in `n-A+1` without the deep hypothesis. The cascade's hypothesis (core `>= A-1`) is **weaker**, its conclusion (pair-level tangent payment) the **same**. A weaker hypothesis cannot yield an already-refuted conclusion.

**Machine-checked replay** (`f17_cascade_check.py`, ramguard tiny; `RS[F_17, mu_8, k=2]`, `A=3`, `u=(0,0,0,0,0,0,1,1)`, `v=(0,0,0,0,0,0,1,2)`):

| fact | value |
|---|---|
| bad slopes | `1, 2, 4, 8, 9, 13, 15, 16` — **8**, vs slot `n-A+1 = 6` |
| distinct-slope selected-support pairs with core `>= A-1 = 2` | **20** — the cascade hypothesis fires |
| cascade multiplicity prediction `~ n-core` | `6`; **observed 8** — the prediction *undercounts* (assumes one pencil) |
| forced pencils on this one pair | **two or more** (multiple pencils each with `|T| = 6 = n-A+1`) |
| total tangent charge | exceeds `n-A+1 = 6` |

Two independent readings, both fatal to "paid": (1) a single core-`(A-1)` cascade saturates the whole `B_tan` slot — `|T| <= n-(A-1) = n-A+1`, saturation ratio **1.0000 on all six official rows**, zero room for the genuine T2 mass the same column must pay; (2) a pair can carry several forced pencils, and the slot is per-`|T|`, not per-pair — nothing banked bounds the pencil count.

*Honest scoping:* this row is the REFUTED node's toy (`n=8, k=2, t=1`) and that node's own claim contract says no clean-rate candidate is falsified by it. The finding is "the payment is unsourced, and its natural form is refuted where the deep hypothesis fails — which is every official row", not "the official rows are falsified".

### Step 7 — the `A-1` tier is in neither ledger column

`xr_strip_classification_rungs/statement.md:10`: "the tangent strip costs at most `n-A+1`". `F5_SKELETON.md:360-365`: F5-OS quantified at pairwise cores **`<= A-2`**. So `R_post` is `<= A-2` and `B_tan` covers (at best, via an unbanked one-line extension) one pencil's worth. **The `core = A-1` tier is charged by neither.** The archived band node said so: "every band pair is either charged or **upgraded toward the cascade threshold**" — the cascade threshold was *assumed* to be where charging happens, and that assumption was never discharged.

---

# WHAT THE HONEST CEILING BECOMES

**`A-1`, not "unbounded up to `A`"** — and it is **sourced without `xr_pencil_cascade`**.

Derivation (one line, from banked pieces only): the bridge selects **exact-`A`** supports. Two distinct-slope selected supports with core `= A` are the *same* set `S`, `|S| = A >= k`; the strip node's forcing algebra (PROVED, 88-check replay) then produces a codeword pair explaining `(u,v)` on all of `S` — **an `A`-support explanation**, so the pair is nongeneric and never enters the generic branch. Hence **in the globally generic branch, pairwise cores are `<= A-1` unconditionally**, by definition of the branch plus already-PROVED algebra.

The loss is exactly one notch, `A-2 -> A-1`. Effect on the two band-repair routes:

**Route W (widen P-A1 + demote + open a band column): SURVIVES, at a measured price.** (`ceiling_arith.py`, exact integers)
- The widened predicate becomes `core in [k, A-1]`, and the ceiling is *sourced* — no longer hostage to `xr_pencil_cascade`.
- Line cap `L(A-1)/L(A-2) = 2.00 exactly on all six rows` (RowC 1/4: 382 -> 764; prize 1/4: 8.20e11 -> 1.64e12).
- PSP is unaffected (already re-priced at `kappa <= A-1`; its `11,11,10` prize ranks stand).
- One extra casualty: the collapsed-face exclusion needs `k+2 > kappa`; at `kappa = A-1` it needs `h < 3` and dies on **6/6** (was 5/6). Already fatal; conclusion unchanged.
- Two extra edits: `F5_SKELETON.md:363` ("cores <= A-2") and `xr_smallcore_spread_count`'s dag statement ("cores < k+t-1") must both move to `A-1`, or the `A-1` tier stays outside `R_post` even after the bridge routes it into P-A1.

**Route T (graded tangent band charge): materially harder, and it now trips its own re-surgery trigger.**
- Route T must charge `[k+1, A-1]`, not `[k+1, A-2]` — the cascade tier is the *hardest* row of the ledger it has to build.
- The target column is already saturated (ratio 1.0000, six/six) and multi-pencil pairs exceed it. Route T **forces** `B_tan > n-A+1` — precisely re-surgery trigger 4 in `xr_smallcore_spread_count/conditional.md:69`.
- Whatever it builds cannot be the nondeep `r+1` form (REFUTED).
- The `13n^3` headroom is in the *residual* column, not the tangent column; re-baselining `B_tan` upward re-opens the six-row consumption arithmetic (69 checks).

**Net: this audit tilts the fork toward Route W.** Route W's ceiling is now independently sourced; Route T's target column is provably full.

# DOUBLE-COUNTING

- Current wording: no double-count, but a *gap* — the `A-1` tier is counted **zero** times (unsafe direction).
- Route W at `kappa = A-1`: benign double-count (both subtractions from `B*` in an already-verified gate with `29n^3` room against a `16n^3` reserve; over-counting is conservative).
- Route T: genuine double-count risk — if band pairs are charged to `B_tan` and the generic-branch predicates are not re-scoped in the same change, the same slopes appear on both sides while `B_tan` grows past its printed slot.

---

# CONSUMER TABLE

Edges (dag.json, 4718 enumerated): one out-edge `req -> xr_clean_residual_any_gate`; one in-edge `ev <- v13_bc_split_pencil_normal_form` (itself CONJECTURE — the node's only evidence supplier is unproved).

| Consumer | What it consumes | Effect |
|---|---|---|
| **`xr_clean_residual_any_gate`** (`conditional.md:16`: "The proved `xr_pencil_cascade` **removes** the large-core pencil regime.") | a *removal* of the whole `core >= A-1` regime before `R_post` | **Directly weakened.** Classified, not removed. Its "remaining unproved contribution is precisely the small-core spread remainder" (`conditional.md:23-24`) is false as written — the `A-1` tier is a second unproved contribution. |
| **`xr_strip_classification_rungs`** (via BAND_OVERCLAIM_FLAG note) | the flag note's residual claim "removal/charge PROVED only at `r >= A-1`" | **That repair text is itself now unsourced.** Amend: forcing PROVED for all cores `>= k+1`; NO core-based charge is proved at any threshold; the generic-branch ceiling `A-1` comes from genericity + forcing, not a payment. Arithmetic (69) and replay (88) untouched. |
| **`xr_tangent_support_mismatch_bridge`** (via FLAG_ADJUDICATION note) | the `A-1` anchor; the fork gate | **R2 unaffected** (routing-only, needs no ceiling). Fork gate answered: Route T's charge does NOT fit inside `B_tan <= n-A+1`. |
| **`xr_highcore_collision_count`** (P-A1, via WIDENING_COST_PASS note) | the `A-2` ceiling for the widened obligation | **Ceiling moves to `A-1`; the widening survives.** Line caps x2; PSP unchanged; collapsed-face loses its last row. Sourcing improves. |
| **`xr_smallcore_spread_count`** | the `<= A-2` scope of the residual target | **Scope hole**: the `A-1` tier is outside F5-OS AND outside `B_tan`. Under Route W both quantifiers move to `A-1` in the same change. Trigger 4 fires under Route T. |
| **`xr_lowcore_spread_heart`** (P-B) | nothing core-ceiling-dependent | Unchanged, verbatim. |
| **`notes/pilots_20260802/p_a1_widening_cost`** | REPORT.md:116 "Cascade ceiling verified ... genuinely independent" | **That sentence is now wrong** — independent of item 3, but not *sourced*. Its own caveat 1 called this correctly. All Group A/B/C classifications survive; only `kappa` moves `A-2 -> A-1`. |
| **`notes/kernel_basis/WP7_WORSTWORD_VERDICT.md:8-13`** | "Face 4 = two proved arithmetic bookends" | **The second bookend is half-proved** (forcing/cascade real; payment not). Face 4's open residue is larger than stated. |
| **`archive/.../xr_partial_tangent_band`** (cut) | "upgraded toward the cascade threshold" as a terminal sink | Confirms the diagnosis: the cut node's ladder terminated in an assumed-paid boundary condition. |

---

# OPEN QUESTIONS

1. **Is the one-line injection extension worth banking?** Restating `xr_true_tangent_coordinate_injection` as "`# recovered-line slopes <= |T|`, hence `<= n-A+1` whenever the forced core is `>= A-1`" is a genuine small theorem (the proof is hypothesis-free) that would make the *recovered-line half* of the cascade charge sourced. Still leaves zero slot slack and the multi-pencil overflow.
2. **How many forced pencils can one received pair carry?** Nothing banked bounds it; the MDS bound permits >= 2 at all six rows and the F_17 witness realizes 2. A per-pair pencil-count lemma is the missing piece for ANY pair-level tangent payment — and it is the same object as the k-packing lemma the widening pass proposed.
3. **Is the `A-1` tier populated at official scale?** Arithmetic exact (saturation six/six), realizability at toy scale (F_17, E27's F_97); population at official `A` established nowhere. The gap argument is scale-free; the "concrete exposure" framing is not.
4. **`t=2`/`h` sensitivity:** at `t=2` the tier `[k+1, A-1]` is a single value — every banked measurement of the cascade tier is at a row where the tier is a single point or empty (same genre as the cost pass's empty-band catch).
5. **The "multiplicity ~n-core" clause needs "per forced pencil" scoping** — the F_17 replay shows observed multiplicity (8) exceeding `n-core` (6) because the formula assumes one pencil.
6. **Provenance not closed:** "W1, PR #10, 70/70 replayed" has no in-repo artifact (no battery, no verifier, no log); the upstream `#147` package resolves to a `.tex` read only through the audit note citing it. Anyone re-grading this node should pull both artifacts directly.
