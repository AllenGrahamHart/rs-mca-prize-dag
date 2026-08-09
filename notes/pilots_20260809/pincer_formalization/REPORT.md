# REPORT.md — pincer_formalization (round 27) — persisted verbatim by the coordinator (Fable) from the pilot's final message, task ae39f5f59adc10f37, 2026-08-09. Pilot: Opus. No edits.

All escape tests pass and the D0 arithmetic is complete. Writing the report of record.

---

# pincer_formalization — round 27 report of record

## VERDICT (first)

**D0 = BROKEN.** The "safe-side-above-sigma\* pincer machinery" is not sound, not repairable in place, and in fact **does not exist as an in-repo theorem**. Worse than absent: its *conclusion is refuted* by a PROVED in-repo node. `sigma* = 8,592,912,738` is **not a pincer constant at all** — it is `t*(255.9) − 1`, the **random-word first-moment corridor edge** computed in `background/nodes/xr_radius_arithmetic/proof.md` §2 from `E[X] = C(n,j)q^{1−t}` against the gate `B* = floor(q/2^128)`. The genuine half-distance pincer safe side that does exist in-repo lands at excess **2^39**, i.e. **63.978× higher** than the point it was attached to.

**Did the formalization land? No — and it must not.** Per the stop rule I registered (R4) I did not build D1 on the broken foundation. **CATCH-24A fired**: the "worst-word/pincer per-row crossing whose formalization is missing" **already exists in-repo**, in the same node, as `(RH-ADJ)` / `a_RH(q)` / `B_mca(a)` — banked 2026-07-17 (wave-9) and refined 2026-07-18 (wave-10), *seven days after* WP5 wrote the flag. WP5 was correct on 2026-07-10; the flag went stale on 2026-07-17 and was never retired. This is the campaign's **fourth** bookkeeping "missing theorem" — with the nuance that it was not bookkeeping *when written*.

**Did BAND-AC get posed? No — it is unstateable, and I recommend retiring it rather than restating it.** BAND-AC has exactly two readings and both fail: with `sigma_FM` = the random-word crossing it is **FALSE at the razor rows by a PROVED node**; with `sigma_FM` = the worst-word crossing it is the **tautology** `a_RH = a_RH`. There is no third reading. A non-vacuous successor pose is drafted below (§D3).

---

## Misses first

1. **My P7 monotonicity sub-prediction is a MISS.** I registered `rho(q)` as "monotone-ish decreasing in L". It is **not**: it rises 64.51 → 79.88 over L = 129 → ~161, then falls to 53.77 at L = 166.503. The window itself ([30, 80]) held and the two point predictions held; the shape claim was wrong.
2. **P8's registered constant was arithmetically wrong** (my error, disclosed in full in §Self-corrections).
3. **P1 carried a stale sub-claim**: I registered that `xr_ledger_qpower` is OPEN (from `xr_radius_arithmetic/proof.md` §6). Its `node.json` says **PROVED** (closed 2026-07-04). This does not touch the verdict — the `t*` computation is exactly correct; the problem is what `t*` *is*, not whether it is right.
4. **My D0 substance is partly a re-discovery.** `notes/kernel_basis/WAVE9_AUDIT_FINDINGS.md:211` already recorded "sigma\* was only the corridor map's MEAN-crossing estimate" on 2026-07-17. What is new here is (a) the custody miss that let it survive, (b) the quantification, (c) the CATCH-24A consequence for WP5's open item.

---

## D0 — the foundation audit

### The load-bearing steps, named

| # | Step | Status |
|---|---|---|
| L1 | `sigma* = t* − 1`, `t* = min{t : t·L ≥ log2 C(n, n−k−t) + 128}` at L = 255.9 | **SOUND** (replayed exactly, E1) |
| L2 | `E[X] = C(n,j)q^{1−t}` is a **random-word / union-bound mean over one word**, times q slopes | **SOUND but mis-typed downstream** |
| L3 | "SAFE side proved for sigma &gt; sigma\* (half-distance/pincer machinery)" — `pro_brief_razor.md:24` | **BROKEN — no such theorem** |
| L4 | "the safe side ABOVE sigma\* is proved" — `P6_RATEHALF_SIBLING.md:21` | **BROKEN — same** |
| L5 | "sigma\* provenance: generic pincer, pro_brief_razor.md" — `node.json` FLOOR v2 statement | **BROKEN — mis-attribution** |
| L6 | The band `(2^33, sigma*]`, width 2,978,146, as a *bracket* | **BROKEN — its upper endpoint is not a proved safe point** |

The failure is a **type error**: `B_mca(a)` is a **max over received words**; `E[X]` is a **mean over received words**. Comparing them and calling the result a determination is not an approximation error, it is a category error — and the repo's own moment machinery flags it: `xr_ledger_qpower/statement.md` caveat (a), *"this is the exact PAIR-CORRELATION (moment-level) ledger — the fixed-word worst-case conversion remains with the KMS/globalness branch."*

### The refutation, in exact integers

```
s*      (random-word FM last-unsafe excess, L=255.9)   =      8,592,912,738
sigma_0 (PROVED MCA-unsafe reach, wave-9)              =      8,594,128,895
2^34-1  (PROVED unsafe reach, wave-10 optimized floor) =     17,179,869,183
sigma_0 - s*   =     1,216,157        (2^34-1) - s*  =  8,586,956,445
(2^34-1) / s* =     1.999307
```

`rate_half_cyclic_simple_pole_mca_floor` (**PROVED**, uniformly for q &lt; 2^256, hence at every razor row) puts `epsilon_mca &gt; 2^-83 &gt; 2^-128` at excess `sigma_0 &gt; s*`. So **the point where the machinery claims "safe above" is strictly inside the proved-unsafe region.** Robustness: the two candidate gates for the FM crossing (cap proxy `2^(L−40)`, used by `f6a2`; prize gate `2^(L−128)`, used by `xr_radius_arithmetic`) differ by at most 1 in the crossing integer — the refutation does not depend on which is meant.

### What the real pincer actually says

`background/nodes/rate_half_half_distance_safe_bracket` (**PROVED**), (HD1):
`B_mca(3n/4) ≤ n ≤ floor(q/2^128)` for q ≥ 2^169 — excess **2^39 = 549,755,813,888**.
Ratio to the claimed safe point `s*`: **63.978×**. Ratio to the proved unsafe reach: **32×**.
The node's own `statement.md:136` and `proof.md:85-86` say it plainly: *"Neither is supplied by the deep or half-distance pincer at this near-capacity radius."*

**Exhaustive P2 grep (own-repo, CATCH-24A discipline).** The only rate-half MCA *safe upper bounds* in the repo are: `rate_half_quadratic_exact_range` (RQ1/RQ2, q &lt; 2^166.503), `rate_half_half_distance_safe_bracket` (HD1, a = 3n/4), and `rate_half_mca_sparse_layer_reduction` (a lossless *identity*, not a bound). **Nothing at, near, or below `sigma*` exists.** P2's registered falsifier did not fire.

### The custody miss (the reason round 27 inherited this)

Wave-9 recorded the correction and its import plan listed *"P6_RATEHALF_SIBLING.md + notes/pro_brief_razor.md (superseded banners)"*. **Those banners never landed.** Both files are unbannered today (`grep -c superseded` → 0/0). Consequently:
- `P6_RATEHALF_SIBLING.md:21` still reads "the safe side ABOVE sigma\* is proved";
- `pro_brief_razor.md:24` still reads "SAFE side proved for sigma &gt; sigma\* (half-distance/pincer machinery)";
- `node.json`'s FLOOR v2 statement still cites `pro_brief_razor.md` for a "generic pincer" provenance;
- WP5 (2026-07-10) consumed them in good faith, and this brief consumed WP5.

The node's *own* live front has already moved on — `attack.md` (today's file) is entirely the `(RH-ADJ)` far-CA/budget program with no band language. **Only the outward-facing/planning layer is stale.**

---

## D1 — CATCH-24A: the object already exists

The brief's Candidate A, registered before use, is
`sigma_FM^worst(q) := min{ t : max_y N(y, k+t; q) ≤ B*(q) }`.
But `max_y N(y,a;q) ≡ B_mca(a)` **by definition**. So Candidate A **is** `a_RH(q) − k`, and the object is in-repo with strictly more structure than the brief asked for:

- **(RH-ADJ)** `B_mca(a_RH(q)) ≤ B*(q) &lt; B_mca(a_RH(q)−1)` — `critical/nodes/rate_half_band_closure/statement.md:75`
- **(RH-SPLIT)** `B_mca(a) = max(B_ca^far(a), S_sparse(a))` — PROVED lossless, `rate_half_mca_sparse_layer_reduction`
- **(RQ1)** `a_RH(q) = n − floor(q/2^128) + 1` **exactly and unconditionally** for `1 ≤ B ≤ B_Q = 389,500,552,609` (q &lt; 2^166.503) — `rate_half_quadratic_exact_range`, PROVED
- **(HD2)** `k + 8,594,128,896 ≤ a_RH(q) ≤ 3n/4` for q ≥ 2^169 — PROVED; wave-10 improves the lower constant to `k + 2^34`

I built nothing. Building a new `sigma_FM` here would have manufactured a duplicate of a PROVED object.

---

## D2 — verification against the banked evidence

### The negative control: the random-word model vs proof, on official rows

`sigma_RH(q) = n − k − B*(q) + 1` (PROVED, RQ1) vs `sigma_FM^rand(q) = t*(q)`, at n = 2^41, k = 2^40:

| log2 q | B* | sigma_RH (PROVED) | sigma_FM (random-word) | rho |
|---|---|---|---|---|
| 129 | 2 | 1,099,511,627,775 | 17,043,737,078 | 64.51 |
| 140 | 4,096 | 1,099,511,623,681 | 15,704,997,239 | 70.01 |
| 150 | 4,194,304 | 1,099,507,433,473 | 14,658,275,453 | 75.01 |
| 160 | 4,294,967,296 | 1,095,216,660,481 | 13,742,346,575 | 79.70 |
| 166 | 274,877,906,944 | 824,633,720,833 | 13,245,741,196 | 62.26 |
| 166.503 | 389,500,552,609 | 710,011,075,168 | 13,205,747,724 | 53.77 |

**rho ∈ [53.77, 79.88] across all 38 determined scales.** The random-word first-moment model **undershoots the PROVED worst-word crossing by ≥ 53.8× at every determined row** — unconditionally, on the *official* rate-1/2 row shape, by theorem rather than by enumeration.

Sharpest single row (log2 q = 166): FM declares safe from agreement **1,112,757,368,972**; `(RQ1)` proves unsafe at **1,924,145,348,608**. The interval FM calls safe and proof calls unsafe is **811,387,979,636 agreements wide = 73.80% of the entire excess range.** At the proved crossing itself, FM's predicted count understates the proved `B_mca = B*` by ~1.36 × 10^14 bits.

**This is FLOOR v2's own pre-registered falsifier firing** — "exact counts deviate from the first-moment model beyond Poisson, sustained across ≥ 3 scales, EITHER direction" — in the structural-surplus direction, sustained across **38 consecutive scales**, on the official row rather than an analogue. And it fires *directly* at the razor rows too, without any scaling, via `sigma_0 &gt; s*`.

### Why the banked evidence never could have caught this

- **18/18 crossing-fidelity family**: q = 97…1153, n ≤ 64.
- **Window-law grid**: ~200 primes, 3 scales, q to 2^40.
- Every one of these rows has **q &lt; 2^128, hence `B*(q) = floor(q/2^128) = 0`** — the node's own "already-settled degenerate regime with grand threshold zero."
- All of it measures the **random-word count law**, which is **not in dispute and is not what FLOOR v2 asserts**. The failure is a **max-over-words vs mean-over-words gap, and that gap is invisible to every random-word count check ever run.** FLOOR v2's evidence base and FLOOR v2's claim are about different objects. Survivals +1…+4 are therefore not evidence for the claim they were banked against.

### The four upstream pairs (replayed exactly)

```
KoalaBear MCA   1116047   +8.978 / -22.197   PAIR OK
KoalaBear list  1116046   +9.164 / -22.011   PAIR OK
M31 MCA         1116023  +27.927 /  -3.259   PAIR OK
M31 list        1116022  +28.113 /  -3.073   PAIR OK
```

All four margins reproduce to 3 decimals. **They do not discriminate** (P9 confirmed): n = 2^21 extension rows, delta ≈ 0.468 near-capacity, KoalaBear q ≈ 2^185.9 / Mersenne q ≈ 2^123.4 — a quadruple parametrization mismatch vs n = 2^41 prime-q razor rows (independently recorded at `KB_LOG.md` §105 and as WP5's F2). Their unsafe side is upstream's theorem; **their safe side is upstream's conjecture** (`upstream_determination_datum.md:27-30`). They confirm first-moment *location arithmetic at their own rows* and are silent about ours. They are **not** support for FLOOR v2.

### Escape tests — 6/6 exact

E1 `t*` = 8,592,912,739 / 7,014,660,390 / 4,722,556,392 / 2,943,177,800 **MATCH**, `s*` = 8,592,912,738. E2 cap reach = 2^33 exactly, plateau e = 22…33 (12 scales). E3 band width 2,978,146 **MATCH**. E4 threshold 255.89999, depth@thr 8,592,916,480, just-above 8,592,912,384, open slice 0.10001 bits **MATCH**. E5 four-pair margins **MATCH**. E6 both f6a2 cells **MATCH** (255.90000002 → 8,592,912,736 / 8,592,912,738; 255.92 → 8,592,241,265 / 8,592,241,266). The banked machine checks are arithmetically flawless — the failure is entirely in what the numbers were taken to mean.

---

## D3 — BAND-AC: retire, don't restate (draft recommendation)

**BAND-AC as briefed cannot be stated.** With `sigma_FM` = random-word crossing it is refuted (above). With `sigma_FM` = worst-word crossing it reduces to `a_RH = a_RH`. The node's real conjecture of record already exists and is `(RH-ADJ)` with the wave-10 bracket.

### Exactly where the FLOOR v2 statement is wrong

1. *"the band determination equals the first-moment prediction … deficit up to the first-moment crossing, safe above"* — **FALSE at the razor rows**, by `rate_half_cyclic_simple_pole_mca_floor` (PROVED): unsafe at excess 8,594,128,895 &gt; s*, margin 1,216,157; margin 8,586,956,445 under the wave-10 constant.
2. *"the proved safe side (above sigma\* = 8,592,912,738)"* — **no such theorem**; the real one is at 2^39, 63.978× away.
3. *"sigma\* provenance: generic pincer, pro_brief_razor.md"* — **mis-attribution**; provenance is `xr_radius_arithmetic` (T\*), a random-word FM computation.
4. *"the band 2^33 &lt; sigma ≤ sigma\*, width 2,978,146"* — **wrong band**. The proved bracket at razor rows is `sigma ∈ [2^34, 2^39]`, width **532,575,944,704** = **178,828× wider (2^17.448)**, and **s\* &lt; 2^34 lies outside it entirely**.
5. *"no structural surplus and no anti-concentration failure"* — the surplus is **proved and is at least a factor 2 at the razor rows, 53.8–79.9× on the determined rows.**
6. The "Opening evidence: window law verified at every band-analogue probed campaign-wide" — **all at q &lt; 2^128 where B\* = 0**, and all measuring the mean-object, not the max-object.

### Successor pose (draft; coordinator's call, not mine to bank)

**(RH-AC) — razor-row crossing location.** For every admissible razor row (n = 2^41, k = 2^40, q prime in (2^255.9, 2^256), q ≡ 1 mod n), the exact adjacent crossing `a_RH(q)` of `(RH-ADJ)` exists and its excess satisfies `sigma_RH(q) ∈ [2^34, 2^39]` (PROVED bracket), with the **binding term being `S_sparse` alone** — `B_ca^far` is free at razor rows because `B*(q) ~ 2^128 ≫ n = 2^41`, so the Hankel layer `B_ca^far(n−r) ≤ r+1 ≤ n` discharges the far-CA half unconditionally. **The open positive content is exactly: locate `min{ a : S_sparse(a) ≤ floor(q/2^128) }`.** No random-word quantity may appear in the statement.

Two named candidate endpoints, with the campaign holding **no evidence** discriminating them — this is the honest state, not a hedge:
- **(RH-AC-lo)** `a_RH(q) = k + 2^34` — the quotient floor is tight.
- **(RH-AC-hi)** `a_RH(q) = 3n/4` — the half-distance pincer (HD1) is tight.
The determined-region ratio `rho ≈ 54–80` extrapolated to the razor rows would place `sigma_RH ≈ 60 · s* ≈ 2^38.9`, i.e. **near (RH-AC-hi)** — reported explicitly as a heuristic extrapolation across a mechanism change (far-CA-driven → sparse-driven), not as evidence.

**Pre-registered falsifiers, with power controls:**
- **F1 (high power).** Improve the quotient-remainder floor's razor-row reach beyond `2^34 − 1`. Power: the constant already moved 2^33 → 2^34 within one wave, so this is a live, cheap, repeatedly-successful attack — any success immediately refutes (RH-AC-lo) and narrows the bracket. Fires on the *unsafe* side.
- **F2 (high power).** Exhibit any received word `y` and razor row with `N(y, k+2^34; q) &gt; floor(q/2^128)`. Power: this is `S_sparse` evaluation at one agreement, the exact object of `rate_half_sparse_pinning_rigidity`'s coupled system; a single witness refutes (RH-AC-lo). Fires on the *safe* side.
- **F3 (control / anti-power).** Any further random-word or window-law count check at q &lt; 2^128. **Pre-declared to have ZERO power over (RH-AC)** — it measures the mean-object. Registering this explicitly is the guard that would have prevented FLOOR v2's four survivals from being banked as support.

**Consumer bars (CATCH-24C, quoted from the consumers' own text):**
- `critical/nodes/adjacency_closing/conditional.md:94` — needs the **complete field-dependent adjacent certificate** for the rate-1/2 row (**LOCATED** crossing). Bar: full `(RH-ADJ)`. Explicitly notes the simple-pole dependency "gives only a lower bracket: it refutes the former fixed candidate rather than certifying an adjacent crossing there."
- `critical/nodes/mca_safe/conditional.md:96-97` — needs only **the safe half**: `B_mca(a_safe) ≤ B*`. Bar: strictly weaker than adjacency; a safe point anywhere suffices. Explicitly: "The proved cyclic simple-pole theorem is an unsafe lower bracket and is not an upper input."
- `critical/nodes/list_adjacency_closing` — **no longer a consumer of this node's MCA content.** Owner moved to `rate_half_list_adjacent_crossing` (TARGET) at wave-10; the w9-C3 correction records the packet as BRACKET-GRADE for the rate-half row pending that pose. **Two live consumers of the MCA content, with different bars** (P10 confirmed).

**One consequence the coordinator should price:** because `mca_safe`'s bar is only the safe half, and HD1 *already* proves `B_mca(3n/4) ≤ B*` unconditionally for q ≥ 2^169, **`mca_safe`'s rate-1/2 bar may already be discharged at the razor rows by an existing PROVED node.** I did not chase this (out of scope after the D0 stop) and flag it as an unverified lead, not a finding. `adjacency_closing`'s bar is untouched by it — it needs adjacency, which is genuinely open.

---

## Predictions vs outcomes

| ID | Registered | Outcome |
|---|---|---|
| E1–E6 | exact values | **6/6 MATCH** |
| P1 | sigma\* = random-word FM edge, not pincer | **CONFIRMED** (sub-claim on `xr_ledger_qpower` stale — see misses) |
| P2 | no in-repo safe theorem above sigma\* | **CONFIRMED**; falsifier did not fire |
| P3 | gaps 1,216,157 and 8,586,956,445 | **CONFIRMED exactly** |
| P4 | D0 = BROKEN | **CONFIRMED** |
| P5 | object already formalized (CATCH-24A) | **CONFIRMED**, with the dating nuance |
| P6 | sigma_RH anchors 1,099,511,627,775 / 824,633,720,833 | **CONFIRMED exactly** |
| P7 | rho ∈ [30,80]; 64±6 @2^129; 62±6 @2^166; decreasing | window ✓ (53.77–79.88), points ✓ (64.51, 62.26), **shape MISS** |
| P8 | s\* outside bracket; widening 184,590 ±5% | outside ✓; **178,828 (−3.12%)**, inside window despite a bad registered constant |
| P9 | four pairs replay but don't discriminate | **CONFIRMED** |
| P10 | two live MCA consumers, different bars | **CONFIRMED** |

---

## Self-corrections (plainly)

1. **I registered a wrong constant.** P8 stated `2^39 − 2^34 = 549,738,634,304`. The correct value is **532,575,944,704**; I mis-subtracted 2^34. The derived ratio prediction 184,590 inherited the error. The measured ratio 178,828 lands inside my ±5% window **by luck, not by correctness** — the registered input was wrong.
2. **My P7 shape claim was wrong** (rho is non-monotone; peak near L ≈ 161).
3. **My P1 sub-claim was stale** (`xr_ledger_qpower` is PROVED, not OPEN).
4. **I initially framed P5 as "the fourth bookkeeping claim" without checking dates.** WP5's flag was **true when written** (2026-07-10); the formalization arrived 2026-07-17. The correct charge is a **stale flag never retired**, not a misread. I corrected the framing before writing this report.
5. **I did not run the banked Modal scripts.** `verify_floor_depth_modal.py`, `verify_q_threshold_modal.py` and `f6a2_fullscale_sweep_modal.py` require `modal`/`mpmath` (non-stdlib, and Modal is forbidden here). I re-implemented their decision cores from scratch in `esc.py` with `math.lgamma`. **This is a weaker replay than running the banked code**, and I registered the precision argument for it in advance (lgamma error ~0.02 bits vs ~256-bit-per-step decision functionals). All six checks reproduce banked values exactly, so the substitution appears sound — but it is a substitution, and I name it.
6. **I considered proposing a successor conjecture that swapped the floor's cap-proxy trigger `2^(L−40)` for the prize gate `2^(L−128)`, and dropped it** — the node's audited guard forbids reusing the list threshold `q/2^128` as an MCA surrogate ("the two triggers are different objects"). I record the near-miss rather than silently omitting it.

## Files

- `/home/u2470931/smooth-read-solomin/prize/notes/pilots_20260809/pincer_formalization/PREREG.md` — registrations appended under "## Pilot registrations" before any computation; left unmodified afterward as the audit trail.
- `/home/u2470931/smooth-read-solomin/prize/notes/pilots_20260809/pincer_formalization/esc.py` — escape tests E1–E4, E6.
- `/home/u2470931/smooth-read-solomin/prize/notes/pilots_20260809/pincer_formalization/d0d2.py` — D0 arithmetic and the D2 negative control.

Primary sources for the verdict: `critical/nodes/rate_half_band_closure/{statement.md:39-48,136; proof.md:85-86; attack.md}`, `background/nodes/xr_radius_arithmetic/proof.md:36-59`, `background/nodes/rate_half_half_distance_safe_bracket/statement.md:26`, `background/nodes/rate_half_quadratic_exact_range/statement.md:15-32`, `notes/kernel_basis/WAVE9_AUDIT_FINDINGS.md:198-217`, `notes/kernel_basis/KB_LOG.md:2755-2790`, and the two unbannered files `critical/nodes/rate_half_band_closure/P6_RATEHALF_SIBLING.md:21` and `.../notes/pro_brief_razor.md:24`.

---

## Compliance

Registrations were appended to the PREREG with Edit **before any interpreter ran**; everything preceding that edit was reading only. **QUARANTINE honored**: I never read `notes/pilots_20260802/CAMPAIGN_LEDGER.md` (two grep hits surfaced were at lines 1211 and 1363, above 4062, and I excluded the file from subsequent greps); I never read the other three round-27 pilot dirs — one `grep -l` listed their `PREREG.md` **paths only**, no content. I spawned no subagents. **COMPUTE LAW**: exactly three interpreter invocations, all via `tools/ramguard` from `/home/u2470931/smooth-read-solomin/prize` — `esc.py` (tiny), `four_pairs_exact_SCRATCH.py` (local, with `RAMGUARD_TIMEOUT=280` documented, moved to background by the harness at 120 s and completed exit 0), `d0d2.py` (tiny). **BANKED SCRIPTS**: `four_pairs_exact.py` was copied to the session scratchpad and run from the copy; no banked script was run in place or edited. **RAM discipline**: file-at-a-time reads, `dag.json` never opened or Read (it appeared only as a grep match, one line printed), no bulk loads. **DRAFT-ONLY**: all writes confined to `notes/pilots_20260809/pincer_formalization/` plus the session scratchpad; no dag/nodes/tools edits, no git, no Modal, stdlib only. **CATCH-24A** was executed before any "does not exist" claim and it fired against my own D1 mandate. **CATCH-19C**: every measured functional is named in PREREG §R0 (`FM(a;q)`, `t*`, `sigma_FM^rand`, `B_mca`, `sigma_RH`, `D(c,d;q)`, `Reach`, `W`, `rho`, `mu`). Misses are reported first and every self-correction is disclosed above.
