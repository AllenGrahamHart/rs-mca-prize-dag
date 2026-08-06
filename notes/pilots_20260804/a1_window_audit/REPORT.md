(RECOVERED 2026-08-06: this pilot's final-message report was never persisted at bank time — a systematic coordinator defect caught by the round-16 es_boundary_adversary pilot. Recovered VERBATIM from the session transcript by task-id; the opening sanity line matches the ledger's bank entry. The FABLE_AUDIT.md in this dir remains the audit of record.)

Sanity check clean: 7/7 controls PASS on re-run, `git status` shows only my untracked pilot dir — no node edits, no tracked file touched. REPORT.md writes are harness-blocked, so the full report is below.

---

# A1 — audit of the C1'-r3 window extension +5 → +7

**Verdict: LOSSY.** The minimal sound window is **W = 5** — a full rollback. `W = 7` overshoots the minimum by exactly **+2**, costing **six slot obligations** (4 → 10), which are precisely the six routeless leaves.

Files: `/home/u2470931/smooth-read-solomin/prize/notes/pilots_20260804/a1_window_audit/PREREG.md` (prediction, written before reconstruction) and `.../verify_window_width.py` (exact-rational verifier, **7/7 controls PASS** under `tools/ramguard tiny`).

## 1. There is no inequality that forces 7

The complete justification lives in one file, `critical/nodes/dli_prime_weighted_large_block_support/notes/c1r3_program_20260719/c1r3_pose.md:113-129`:

&gt; The r2 forensics (catch c1r2-C5) showed the `w &lt;= L+5` window underprices even the in-window shadow… **L+7 is chosen because: (i) it strictly contains every window probed in the kill packet; (ii) it is finitely enumerable exactly; (iii) at official aspect it stays Newton-finite: for every scheduled level `ell &gt;= 8`, `L+7 &lt;= 2L`**

Reason (i) is provenance, not derivation — the kill packet probed an *absolute* `w &lt;= 7`, itself inherited from the 2026-07-10 calibration that enumerated `w = 3..7` at `L = 2` (`F_ROUND_CONJECTURE_FALSIFICATION.md:23-32`). The r2 pose then reverse-engineered `L+5` to reproduce that same absolute 7 at `L = 2` (`C1PRIME_LEVEL_SCALED_POSE.md:18-36`: *"its old row had `L=2` and enumerated weights `3..7`"*). So **`L+7` re-reads a level-scaled window off an absolute number that already meant `L+5`** — the same numeral used twice under two semantics. Reason (ii) holds at any W. Reason (iii), the only inequality in the whole derivation, is a **ceiling** (`L+W &lt;= 2L`), not a floor.

## 2. The demand side does not bind — the zone budget is irrelevant to W

Official mass law `512·ell·2^-w` (`wcl_audit_findings.md:236`), threshold 1/32. The ten slots have masses 16, 8, 4, 2 / 8, 4, 2 / 4, 2, 1 — every one breaches 1/32 by 32×–512×. A cell first becomes mass-safe at `w &gt;= 15/16/17` for `ell = 1/2/4`, i.e. **W &gt;= 14, 14, 13 — five units past the Newton cap of 8**. The budget can never truncate a tail; the width is set purely by the supply side. Slot count is exactly **3 per unit of W**: W=4→1, W=5→4, W=6→7, W=7→10, W=8→13.

## 3. The margin/slot curve (new — never computed before)

Recomputed over the complete two-round gated census from banked per-row `(w7,w8)` counts (`c1r3_results.md:66-100`) and round-2 ledgers (`c1r3b_results.md:83-89`):

| W | slots | worst K' (exact) | ≈ | at q | vs kill line 4 | vs amber-2 line |
|---|---|---|---|---|---|---|
| 4 | 1 | 1500029/500000 | 3.000058 | 918552577 | 1.333× | **−33.3% TRIPS** |
| **5** | **4** | **108759/62500** | **1.740144** | 290455553 | **2.299×** | **+14.9%** |
| 6 | 7 | 1500029/1000000 | 1.500029 | 918552577 | 2.667× | +33.3% |
| 7 | 10 | 350411/250000 | 1.401644 | 377487361 | 2.854× | +42.7% |
| 8 | 13 | 350411/250000 | 1.401644 | 377487361 | 2.854× | +42.7% |

Marginal price: `+0→+5` = 0.315 K'-units/slot; `+5→+6` = 0.080; **`+6→+7` = 0.033**; `+7→+8` = **0.000**.

Three consequences: (a) **W=7 sits at the flat end of a curve nobody plotted** — the next step buys literally zero; (b) **1.401644 is a hard floor for every W**, because the row binding at W=7 has `W_ext = 0` (`c1r3b_results.md:85`) and carries no orbit any window can price; (c) all three pre-registered round-2 kill lines survive at W=5, and KILL-IIDX condition (a) fails *more cleanly* at W=5 (terminal increasing run 1) than at the banked W=7 (run 2).

## 4. THE BINDING INEQUALITY (why 5, not 4)

q = 918552577 is the unique in-gate `w&lt;=6` accident carrier below 2^32 (`c1r3_results.md:60-62`, complete scan of all 401 gated Proth primes). Exact `env = 46233153981711603/15410754991685632 = 3.000057687`; orbit profile `w2..8 = {0,0,0,0,1,0,1}` — one w6 (mass 1) and one w8 (mass 1/4). The amber-2 line requires

```
env/(1 + W_ext) &lt; 2   ⟺   W_ext &gt; env/2 − 1 = 0.500028844
```

The **only** orbit at that row exceeding 0.500029 is the w6 (the w8 supplies 1/4). Pricing w6 needs `6 &lt;= L+W` at `L=1`, i.e. **W &gt;= 5**. At W=4 the w6 is unpriced, `K' = 3.000058 &gt;= 2`, amber-2 fires. **W_min = 5 exactly; everything above is slack.**

## 5. Why the overshoot happened — a dated cause

`c1r3_report.md:106-112` offered the rollback and gave one reason to refuse it: *"the 4 would-be-amber rows repriced by w7/w8, finding c1r3-C6, argues for L+7."* Those four rows are at 1.230, 1.036, 1.222, 1.123 — **all in [1,2), ambers only under the `K' &gt;= 1` line**. But the same round-1 findings file, one catch earlier (`c1r3_findings.md:37-48`), had already condemned that line: *"the K'&gt;=1 watch line … sits ON the bulk asymptote and will trip forever as q → 2^N regardless of accident structure. Round 2 should re-arm amber at K'&gt;=2."* Round 2 did exactly that and confirmed it out of sample. **The sole argument for L+7 was denominated in an instrument the same document set had already declared broken and that was retired one round later.** Under the surviving line, all four are non-events at W=5.

## 6. A2 pre-check — the `W_ext = 0` overkill gap

Solving the assembly exactly: `(1 + 4(1+W_ext))^34 &lt; 2^100` ⟺ **`W_ext &lt; 0.670093374`**, versus the wired `1/32 = 0.03125`.

&gt; **A2 GAP = 21.443× unused zone budget = 1.2112 bits of product slack** (19.8432 → 21.0544 bits), and the ten-slot route delivers `W_ext = 0`, i.e. infinite overkill against a predicate already 21.4× tighter than needed.

**But the gap is sterile.** Two checks: the allowance ceiling is **6 in both cases** (`1+A &lt; 2^(100/34) = 7.680196` → `A &lt; 6.680`), so 1.2112 bits buys zero allowance units; and at the true tolerance the only mass-safe cell in the whole `W&lt;=8` board is `(4,12)`, which doesn't exist at W=7 — **the overkill retires ZERO slots**. Recommend re-scoping A2 from "re-pose to buy slack" to "re-pose to stop overclaiming", de-prioritised behind A1.

## 7. Proposal (surfaced, not applied — no node edits)

Roll the ledger window back to `w_max(L) = L+5`. Consumer arithmetic is **bit-identical** (`E_j &lt;= 41/8`, `41^34 &lt; 2^202`, 19.8432 bits slack, allowance ceiling 6 — control C7). `dli_wcl_zone_coverage` reverts to the four-slot equivalence, which *un-supersedes* the pre-extension text still sitting in `statement.md:9-18`. Board: 10 leaves / 8 routeless → **4 leaves / 1 closable now** via CR-W5-ELL1 + 3 small classifiers.

Honest costs: worst-case margin 2.854× → 2.299×, amber-2 headroom 42.7% → 14.9% (watch-line, not kill-line); the C1-ZERO extractor must produce a shorter relation — real but **unpriced, and currently unpaid-for, since no engine has been selected** (`BRIEF1_DOSSIER_AUDIT.md:78-80`); and W=5 must be treated as a **re-posed** conjecture with a replayed census, not an inherited one. Hedge option W=6 (7 slots, still 5 routeless) gets most of the cost and little of the benefit — not recommended.

## 8. Flags

- **[A1-F1]** `c1r3_pose.md:117` cites c1r2-C5 as the reason to widen; c1r2-C5's own conclusion (`c1r2_findings.md:49-51`) is *"no small fixed window `w_max` rescues the '4-allowance'"* — it argues **against** widening. Inverted citation, load-bearing for the choice.
- **[A1-F2]** `gap_matrix.md:62` calls the 918552577 repricing *"the extension working exactly as designed"*; the orbit doing the work is a **w6** = `L+5` orbit, **inside the pre-extension window**. The pre-extension window performs **90.0%** of the repricing at that row.
- **[A1-F3]** The `7` in `L+7` and the `7` in the `w=3..7` calibration are the same numeral with different semantics; the absolute 7 already *is* `L+5` at its calibration row.
- **[A1-F4]** `KB_LOG.md:2668` surfaced *"adopt the L+7 window … vs seek an intermediate window"*. No intermediate was ever computed, in any file. §3 is the first pricing, 18 days later.
- **[A1-F5]** The banked "minimum breach 32× at (4,11)" is measured against the wired 1/32; against the assembly's true tolerance it is **1.4923×**. True headroom is 49%, not 3100%.
- **[A1-F6]** `dli_wcl_newton_short_window_exclusion/statement.md` still shows the six-slot residual in its main table with a correction appended. A W=5 rollback makes the *main table* correct and the correction stale — invert the fix.

## 9. Prediction scoring

Verdict class (LOSSY) **right**; specific `W_min = 6` **wrong** (answer 5 — I under-rated full rollback at 0.25); P1 (pigeonhole/Minkowski doubling step) **wrong** — I assumed a derivation existed; P3 (budget never binds; width is supply-side only) **right and now quantified**; P4 (A2 = 2 allowance units) **wrong on framing** — the overkill buys zero allowance units.

result: A1 verdict LOSSY — the C1'-r3 window +7 is a +2 overshoot with no derivation behind it; minimal sound width is W=5 (binding inequality `W_ext &gt; env/2 − 1 = 0.500029` at the single accident row q=918552577, satisfiable only by its w6 orbit), taking the board from 10 leaves/8 routeless to 4 leaves/1 closable at identical consumer arithmetic and a 2.854×→2.299× census-margin cost; A2 gap quantified at 21.443× / 1.2112 bits and shown sterile (retires zero slots, buys zero allowance units); 7/7 controls PASS, 6 flags, no node edits.