The harness refused the `REPORT.md` write (expected per the brief). Returning the full report verbatim, with the one compliance line corrected to reflect the refused write.

---

# REPORT — rh_haboeck_seam (round 32, ADVERSARIAL)

**Verdict: NO KILL on the mathematics. The wave-57 Haboeck import chain is CERTIFIED on object identity, convention, rounding, arithmetic, and field scope.** Every attack in the brief was run; each is logged below with what would have killed it. Four real defects were found, all *outside* the mathematics: one substantive scope-transport gap (F1), two stale-text items one of which is now literally false (F2, F3), and one mis-rounded printed constant propagated to four files (F4). Plus three lower-severity items (F5-F7) and one notation hazard (F8).

My pre-registered prior was P(at least one real seam) = 0.72 with 0.50 of the seam mass on OBJECT identity. The object seam is **dead**; the mass that paid out landed on a class I had not registered at all — *transport scope*, i.e. the supplier proving strictly more than the consumer records. Registering that miss explicitly: my R2 ranking was wrong about where this import would leak.

---

## MISSES FIRST — what I attacked and could not break

**M-A. CATCH-24C, the prime suspect (D1). DEAD, by my own pre-registered falsifier (a).** I expected `E_m` to exclude a class of pair-explained slopes that `B_mca` counts. It does not: the exclusion is word-for-word the repository's own definition of MCA badness. Both sides, quoted:

Import side — `background/nodes/haboeck_quadratic_johnson_mca_import/statement.md:20-28`:
```
For every received pair `f_0,f_1:D->F_q`, let `E_m(f_0,f_1)` be the set of
finite affine slopes `z in F_q` for which there is a support `A subseteq D`
with

    |A| >= (1-gamma_m)n,
    (f_0+z f_1)|_A in C|_A,
    but (f_0,f_1)|_A not in C^2|_A.
```

Repo side — `background/nodes/rate_half_arbitrary_line_syndrome_router/statement.md:10-17`:
```
...received pair with syndromes `(s_0,s_1)`. A finite slope `gamma` is
support-wise MCA-bad at agreement at least `a` if and only if there is a set
`E` with `|E|<=r` such that

    s_0+gamma s_1 in V_E,
    not (s_0 in V_E and s_1 in V_E).                     (SL1)
```

`s_0 in V_E` is exactly `f_0|_{D\E} in C|_{D\E}`, so `not (s_0 in V_E and s_1 in V_E)` is exactly `(f_0,f_1)|_A not in C^2|_A` with `A = D\E`. The two exclusions are the same predicate, existentially quantified over the same support in the same conjunction. **There is no pair-explained class that `E_m` drops and `B_mca` keeps.** What would have killed it: a `B_mca` defined as an unrestricted bad-slope count, or the two conditions quantified over *different* supports on the two sides.

**M-B. Same-support quantifier.** Both texts put the closeness test and the non-containment test on one and the same `A`. The import's own audit says so in terms (`.../haboeck_quadratic_johnson_mca_import/audit.md:7`: "The noncontainment test and the close-codeword test use the same support."), and it is true of `(SL1)` as written. What would have killed it: `E_m` testing non-containment globally while `B_mca` tested it on the witness support (or vice versa) — that mismatch changes the counted set in both directions.

**M-C. Support-size direction.** `B_mca(a)` counts slopes bad at agreement *at least* `a` (`background/nodes/mca_quadratic_prize_rows/statement.md:9-10`: "let `B_C(a)` be the maximum number of support-wise MCA-bad finite slopes at agreement at least `a`"). Since `a_m = ceil((1-gamma_m)n) >= (1-gamma_m)n`, every slope counted by `B_mca(a_m)` has a witness support of size `>= a_m >= (1-gamma_m)n` and is therefore in `E_m`. The inclusion runs the safe way. What would have killed it: `a_m` defined as the *floor* of the threshold, or `B_mca` counting at agreement *exactly* `a`.

**M-D. Max-over-pairs vs for-every-pair.** `B_mca` is a maximum over received pairs; `(HJ1)` is stated "For every received pair". A per-pair bound bounds the max. What would have killed it: `(HJ1)` stated for a *typical* or *random* pair — the round-27 FLOOR v2 max-vs-mean death.

**M-E. Finite vs infinite slope.** All three texts are finite-slope: the import ("finite affine slopes `z in F_q`", statement.md:21), the router ("A finite slope `gamma`", statement.md:10), the endpoint node ("Under the finite-slope support-wise MCA convention", `background/nodes/mca_full_agreement_endpoint/statement.md:8`). The import's audit item 2 rules out a `q+1` projective denominator. What would have killed it: a projective slope set on one side, silently adding the `z=oo` member.

**M-F. D2, the convention correction. Correct, and load-bearing at the last unit.** `background/nodes/haboeck_quadratic_johnson_mca_import/proof.md:10-14`:
```
Haboeck writes `RS[F_q,D,d]` for polynomials of degree at most `d`, with
dimension `d+1` and reduced rate `rho=d/n`. The repository writes
`RS[F,D,K]` for polynomials of degree less than `K`, with dimension `K`.
Therefore `d=K-1`, proving `(HJ2)` with no inequality or conservative rate
replacement.
```
I verified the repository half of that sentence independently rather than taking it: the official row's code is `C=RS[F,D,k]` (`background/nodes/mca_quadratic_prize_rows/statement.md:9`) and the `deg < k` reading is used throughout the repo's own proofs (e.g. `background/nodes/xr_ov_slope_free_reduction/proof.md:23-24`: "a non-zero `deg < k` polynomial ... has at most `k-1` roots"). So `d = k-1`, `rho=(k-1)/n`. **This check mattered**: I ran the counterfactual, and under `rho=k/n` the banked `a_9` and `a_95` would each be too small by exactly 1, i.e. genuinely unsafe —
```
m=9 : a_m would be 1641330047988, banked 1641330047987  -> banked SAFE? False
m=95: a_m would be 1563128173125, banked 1563128173124  -> banked SAFE? False
```
(`notes/pilots_20260810/rh_haboeck_seam/rederive.py`). The asymmetry is worth recording: in `Q_m` the `(k-1)` choice is *conservative* (the wrong convention would only have made `Q_m` too large, which is safe), while in `a_m` it is *load-bearing* and unsafe-if-wrong. The correction cycle 41 claims was applied is real and complete. What would have killed it: any repo-side use of `deg <= k` at the official row.

**M-G. Rounding directions (D2, second half). Both safe.** `Q_m` is a floor of a real upper bound on an integer count — safe (an integer `<= x` is `<= floor(x)`). `a_m` is a ceiling of a real agreement threshold — safe (an integer support meeting the real threshold has size `>= ceil` of it). The node's verifier does not merely compute them, it asserts the two adjacent squared inequalities that *characterise* floor and ceil (`background/nodes/rate_half_haboeck_quadratic_johnson_safe_bracket/verify.py:23-32`), so a wrong-direction idiom could not pass. No third rounding exists in the chain, and no floating-point value enters any assertion — `log2` appears only inside the final `print`. What would have killed it: a ceiling on `Q_m`, a floor on `a_m`, or a float `sqrt` inside a comparison near a tie.

**M-H. D3, the ladder arithmetic. Every banked integer reproduces exactly.** I re-derived `m = 3..96` from `(HJ1)`/`gamma_m` alone, never from the consumer's closed forms `N_m/D` or `(2m a)^2`, using exact `Fraction` arithmetic and `math.isqrt`, with an independently written ceil-sqrt (`notes/pilots_20260810/rh_haboeck_seam/rederive.py`). Results:

| landmark | banked | re-derived | match |
|---|---|---|---|
| `a_8` | 1652128271987 | 1652128271987 | yes (`> 3n/4`) |
| `a_9` | 1641330047987 | 1641330047987 | yes (`< 3n/4`) |
| `Q_9` | 31838208335176550182206428283836 | same | yes |
| `Q_94` | 306835809425699384690368974701937497457 | same | yes |
| `a_94` | 1563215236073 | same | yes |
| `Q_95` | 330298791207625937408605578064099942258 | same | yes |
| `a_95` | 1563128173124 | same | yes |
| `n-a_95` | 635895082428 | same | yes |
| `Q_96` | — | 355283122119774852268896123596088746233 | `> 2^128-1` |

and independently: `m=9` is the first `m` with `a_m < 3n/4`; `m=95` is the largest with `Q_m <= 2^128-1`; `Q_m` nondecreasing and `a_m` nonincreasing on `3..96`; `(Q_94*2^128)^10 < 2^2559` and `(Q_95*2^128)^10 > 2^2559`, i.e. `Q_94*2^128 < 2^255.9 < Q_95*2^128 < 2^256` — which is exactly what makes "every razor row gets `m=94`, upgrading to `m=95` at the printed threshold" true and non-vacuous. I also confirmed the consumer's closed forms agree with `(HJ1)` for every `m` in `3..96` (`CLOSED_FORM_AGREES_WITH_HJ1 True`), so `(RHJ1)`/`(RHJ2)` are faithful transcriptions and not re-derivations with a slip. What would have killed it: any single integer off, or `Q_m` nonmonotone across the `95/96` cap boundary.

**M-I. Beyond-Johnson check.** `a_95 = 1563128173124 > floor(sqrt(n(k-1))) = 1554944255987`, and `a_m` decreases to that limit but never reaches it, so the scope line "does not cross the Johnson radius" holds for every affordable `m`. `gamma_m > 0` for all `m` in `3..96`.

**M-J. D3, the field/e-axis and O6.** The import is field-general and domain-general as written (`F_q`, arbitrary evaluation set); nothing in the chain assumes `F_q` has no proper subfield, so **O6 is not tripped** — and it would not be even if it applied, since O6 fences far-CA *upper* bounds and this is a direct MCA bound. The consumer node's own pose is `q=p^e` with `e in {1,...,6}` (`critical/nodes/rate_half_band_crossing_location/node.json:9`) and the bracket's inputs are "an admissible field order `q<2^256`" (`.../rate_half_haboeck_quadratic_johnson_safe_bracket/claim_contract.md:8`) with no primality, smoothness, or `e`-restriction — so all six strata are covered. What would have killed it: any `q` prime, `q` large-enough-relative-to-something, or no-subfield hypothesis appearing in the import or the specialization.

**M-K. D4, the BCHKS25 boundary. No leak.** `BCHKS` appears in exactly three places outside the two Haboeck nodes: `background/nodes/xr_band_key_lemma_pencil_mass/statement.md:95` (a remark that MC "routes around those unconditionally"), `background/nodes/paving_rf3_double_prime_koalabear_safe_rows/upstream_ordinary_audit.md:63` and `.../upstream_bridge.md:66` (an ECCC artifact hash pin and a Claim A.2 correction). None uses the linear-in-`n` MCA refinement. Every occurrence of "linear refinement"/"linear-in-`n`" in `critical/` and `background/` is inside the two Haboeck nodes and is an explicit *exclusion*. What would have killed it: any downstream numerator computed with the linear formula.

**M-L. The second consumer's `CA <= MCA` step. VALID.** I found a second consumer of the import that the brief did not name — `background/nodes/l1_fpc5_shifted_johnson_grs_shell_cap` (its `node.json` `requires` the import). Its `proof.md:48-50` performs an object transport of exactly the T5 death shape:
```
...Every CA-bad slope is MCA-bad: CA-farness rules
out any common explaining support, which is precisely enough for the
support-wise MCA event. Thus the CA numerator of `C` is also at most `Q_m`.
```
This is sound, and I checked it rather than assuming it. `epsilon_ca` is by construction a *far-branch* quantity — the conversion node states it (`background/nodes/rs_deep_point_list_to_ca_conversion/statement.md:47-48`: "It uses ordinary lists for `C+` and support-wise finite-slope CA for `C`") and, decisively, its proof *establishes the farness of the specific pair it uses* rather than assuming it (`.../rs_deep_point_list_to_ca_conversion/proof.md:32-42`: "The received pair in `(1)` is CA-far on every such support. Indeed, if a polynomial `G` of degree below `K` agreed with `g_alpha` on more than `K` points, then `(X-alpha)G(X)+1` would have degree at most `K`, more than `K` roots, and value `1` at `alpha`, a contradiction."). Because `g_alpha` alone is unexplainable on any support of size `> K`, and `(DP1)` forces `A >= K+1`, every witness support has the pair not jointly contained — so the same `A` serves the MCA event. **What would have killed it**: `epsilon_ca` defined as a max over *all* pairs rather than far pairs. In that case a pair with a common explaining support could carry many combination-close slopes that are pair-explained and therefore *not* in `E_m`, and the transport would be a bound on a subset dressed as a bound on the whole — the exact D1 failure, one node over. It does not happen. The direction is also correctly fenced by the node's own audit (`.../l1_fpc5_shifted_johnson_grs_shell_cap/audit.md:9`: "MCA supplies CA only in the direction `CA<=MCA`"), and the repo's fence bars only the *opposite* direction (`background/nodes/rate_half_unique_decoding_ca_mca_scope_fence/statement.md:14-24`: the CA-to-MCA transfer has gate `2r<=n-k`, i.e. `a>=3n/4`). The Haboeck route is direct-MCA and legitimately operates below `3n/4`.

**M-M. The retired premise-weakening surgery is not re-run.** The round-28 correction on the consumer node (`critical/nodes/rate_half_band_crossing_location/statement.md:140-146`) holds that "HD1 is an upper bracket END at 3n/4 and B_mca is nonincreasing, so it bounds nothing below 3n/4", and retires as unsound the reading that a bracket end discharges `mca_safe`'s bar. The Haboeck bracket is the same species — a safe-side end with no adjacent-unsafe witness — and the chain says so in three places rather than quietly claiming a flip (`.../safe_bracket/statement.md:69-70`; `.../safe_bracket/audit.md:6`; `critical/.../statement.md:763-765` "This is a real bracket movement but no status flip"). What would have killed it: any claim that `mca_safe`'s consumer bar moved.

**M-N. `3n/4` staleness sweep, negative branch.** Most repo occurrences of `3n/4` are in `critical/nodes/rate_half_list_adjacent_crossing` and are the *ordinary LIST* object (`a_L`, `L_1`), which the import explicitly does not bound (`.../haboeck_quadratic_johnson_mca_import/claim_contract.md:11`: "no ordinary LIST bound"). Those are correctly untouched. Only the two MCA-side occurrences below are stale.

---

## FINDINGS

### F1 — SCOPE-TRANSPORT GAP (the finding of the round). Supplier proves a 23-bit staircase; consumer records two steps of it.

`rate_half_band_crossing_location`'s obligation, after the same-day quantifier widening, is **all** admissible `2^167 < q < 2^256` (`critical/nodes/rate_half_band_crossing_location/node.json:9`). The Haboeck supply becomes available at `q >= Q_9*2^128`, i.e. `log2 q ~ 232.6505` — the bracket node says so itself (`background/nodes/rate_half_haboeck_quadratic_johnson_safe_bracket/statement.md:37-38`: "Thus `(RHJ4)` applies whenever `q>=Q_9*2^128`"). But `(RHJ7)` is stated only "throughout the razor slice" (`.../statement.md:60-65`), and the consumer records only the `m=94`/`m=95` members — in the addendum (`critical/.../statement.md:743-760`) and in the shard (`critical/.../node.json:9`: "On razor rows the proved direct-MCA Haboeck bounds give upper endpoints a_94 ... and ... a_95").

So the window `log2 q` in `[232.6505, 255.9)` — roughly 23.25 bits of the node's own obligation — carries **86 proved bracket steps (`m = 9..94`) that neither node states**. The staircase, computed exactly (`notes/pilots_20260810/rh_haboeck_seam/staircase.py`):

| `m` | `log2` of `q`-threshold | `a_m` | gain vs `3n/4` |
|---:|---:|---:|---:|
| 9 | 232.650530 | 1641330047987 | 7,937,393,677 |
| 20 | 240.417902 | 1593817862387 | 55,449,579,277 |
| 40 | 247.535963 | 1573574783987 | 75,692,657,677 |
| 60 | 251.463130 | 1568006769587 | 81,260,672,077 |
| 80 | 254.135118 | 1565216767187 | 84,050,674,477 |
| 93 | 255.743299 | 1563304171342 | 85,963,270,322 |
| 94 | 255.850734 | 1563215236073 | 86,052,205,591 (banked) |

This is not a mathematical error: a bracket top of `3n/4` in that window is *true*, just not the best proved. It is an under-transport of the node's own banked content, and it is the shape the campaign cares about — the supplier proved it, the verifier loops `m = 3..96` (`.../safe_bracket/verify.py:37`), and the consumer records two rows of the table. **Recommended (AUDIT-AND-DRAFT, coordinator-gated):** extend `(RHJ7)` and the consumer addendum to the general form "for admissible `q`, `a_RH(q) <= a_{m(q)}` where `m(q) = max{m : Q_m*2^128 <= q}`", with the printed `m=9` entry point and the `m=94/95` razor rows as its named corollaries.

*Novelty subtraction:* I grepped `notes/` for the constant `232.65`, `Q_9`, and every `Haboeck` mention. The two hits (`notes/PRIZE_RESOLUTION_ROADMAP.md:25543` and `notes/work_cycles/roadmap_r3/41-rate-half-haboeck-johnson-bracket-20260810.md:13`) both repeat "available from `log2(q)>=232.650531`" and then jump straight to the razor rows — i.e. the cycle note has the same gap and does not record it. No prior art found in readable scope.

### F2 — a now-FALSE exhaustive claim in a critical node, made false by wave 57 the same day.

`critical/nodes/adjacency_closing/conditional.md:109-113`:
```
Rate-`1/2` rows at the official `n = 2^41, k = 2^40` with `q` in
`[2^167, 2^255.9]` are therefore inside this node's quantifier and located by
nothing: the only proved bracket tops there are `n` (full agreement, every
admissible `q`) and `3n/4` (`q >= 2^169`), and a bracket top is not an
adjacent certificate.
```
"the only proved bracket tops there are `n` ... and `3n/4`" is an exhaustive claim, and it is now false: on the upper 23 bits of that very interval, `a_9 .. a_93` are also proved bracket tops. The sentence sits inside a block that is subsequently marked RESOLVED (line 123), so it is narrative rather than load-bearing — but it is a false present-tense statement about what is proved, in a critical node, introduced by the same day's landing. Minimal fix: append "(superseded above `q ~ 2^232.651` by the Haboeck staircase — see `rate_half_haboeck_quadratic_johnson_safe_bracket`)".

### F3 — stale headline bracket on the consumer node itself.

Two places in `critical/nodes/rate_half_band_crossing_location/statement.md` print the old top with no forward pointer to the addendum 670 lines below:

line 64-65 (inside the same-day QUANTIFIER WIDENING block):
```
and (2^167+2^129, 2^255.9] carries the same bracket
[k+2^34, 3n/4 for q >= 2^169, n below] with no located crossing.
```
line 69-72 (the node's headline pose):
```
B_mca(a_RH) <= B*(q) = floor(q/2^128) < B_mca(a_RH - 1),
a_RH in [k + 2^34, 3n/4]          (the PROVED bracket).
```
Same defect class as F2 — under-statement rather than falsity, since a weaker bracket is still a bracket — but "(the PROVED bracket)" now names something weaker than the node proves, and it is the line a consumer reads first. This is the "F1 stale reduction" pattern the brief flagged, and it grew within the same wave rather than one or two rounds later.

### F4 — a printed constant that disagrees with its own verifier, propagated to four files.

`background/nodes/rate_half_haboeck_quadratic_johnson_safe_bracket/statement.md:37-38`:
```
Thus `(RHJ4)` applies whenever `q>=Q_9*2^128`, approximately
`log2(q)>=232.650531`.
```
The node's own verifier prints `log2_q_first=232.650530093386`. My two independent routes agree with the verifier and not with the statement: a fixed-point binary logarithm validated to 15 digits against `log2(3)`, `log2(10)`, `log2(7)`, and a logarithm-free integer bracket `X^200000` vs powers of two giving `232.6505300 <= log2(Q_9*2^128) < 232.6505350` (`notes/pilots_20260810/rh_haboeck_seam/logcheck.py`). Correctly rounded to six decimals the value is **232.650530**, not 232.650531.

Direction: **safe**. The exact criterion `q >= Q_9*2^128` is stated first and is exact; an over-large printed threshold only ever under-applies `(RHJ4)`. Severity: cosmetic. But it is a statement/verifier disagreement that a passing verifier cannot catch — the verifier *prints* the number, it does not assert the statement's string — and it has already propagated to `.../safe_bracket/node.json:8`, `notes/PRIZE_RESOLUTION_ROADMAP.md:25543`, and `notes/work_cycles/roadmap_r3/41-rate-half-haboeck-johnson-bracket-20260810.md:13`.

### F5 — double edge with conflicting kinds (hygiene; NOT novel, do not price as a wave-57 regression).

The import→bracket edge is declared from **both** ends with **different kinds**: `haboeck_quadratic_johnson_mca_import/node.json:32-36` declares `evidence_for -> rate_half_haboeck_quadratic_johnson_safe_bracket` (kind `ev`), while `.../safe_bracket/node.json:26-30` declares `requires <- import` (kind `req`). `tools/dag_manifest.py:102-137` expands both with no de-duplication and no kind-conflict check, so `dag.json` carries two edges for one dependency; `tools/verify_prize_dag.py` has no duplicate-edge check. The two nodes' prose disagrees accordingly (`import/dependency_subdag.md:6` prints `--ev-->`, `safe_bracket/dependency_subdag.md:4` prints `--req-->`).

*Novelty subtraction (own-repo grep first, per hard law 5):* I scanned all 2,195 `node.json` shards (`notes/pilots_20260810/rh_haboeck_seam/edge_scan.py`, never opening `dag.json`). Result: **16 doubled ordered pairs out of 6,434**, all with conflicting kinds, 14 of them in the pre-existing `kb_m2_r4` cluster. So this is a standing repo pattern (~0.25%), not a wave-57 defect. Consequence is benign — the `req` edge is present so refutation propagation still works and the extra `ev` edge is inert. Reported as a class-level hygiene item worth a compile-time check, not as a catch against this wave.

### F6 — D4: the pinned "proof audit" names a different theorem, and is out of repo. ZERO POWER.

`background/nodes/haboeck_quadratic_johnson_mca_import/provenance.md:9-12`:
```
- **Upstream audit pin:** `przchojecki/rs-mca` commit
  `93fba1be3f3299b0ba4708d88715377bbb656e45`, file
  `experimental/notes/audits/audit_bchks25_thm46_conditional_johnson_import.md`,
  blob `ef064597a820165804848cb976d61abcb8067c3d`.
```
The node's `closure` is "published theorem import with statement and proof audit" (`statement.md:4`) and `proof.md:19-20` says "The pinned upstream audit checked the deferred BCIKS steps, the inseparable branch, and the same-support endpoint." But the pinned file is named for **BCHKS25 Theorem 4.6, a *conditional* Johnson import** — the very object this node explicitly excludes (`statement.md:48-51`, `audit.md:9-10`). The two are compatible (one audit can delimit the conditional refinement from the proved quadratic core, which is what `provenance.md:14-16` asserts), but the naming is the shape a misattributed audit takes, and the file is not in this repo. `experimental/` does not exist here; the vendored literature directory referenced elsewhere (`.../paving_rf3.../upstream_ordinary_audit.md:64-66`, `experimental/literature/proximity-gaps-mca/`, gitignored) is likewise absent. **I have zero power on this offline and did not guess.**

### F7 — D4: no ledger row for the wave's only external-publication import.

`notes/correspondence/UPSTREAM_IMPORT_LEDGER.md` has 27 rows and covers the Haboeck import's same-day sibling (the deep-point list-to-CA conversion, line 12), which even names Haboeck in its claim cell ("composition with Haboeck and the exact FPC5 shells"). There is **no row for `haboeck_quadratic_johnson_mca_import` itself** — grepping `notes/` for the node id and for the pinned audit filename returns nothing at all. The ledger's stated law concerns v13-raw material, so its letter does not compel a row for an external preprint; but this is the only import in the wave whose proof lives entirely outside the repo, and it is the one the ledger's "claim / explicit nonclaim" columns would serve best.

### F8 — notation hazard (no error present).

`C^2` in `(f_0,f_1)|_A not in C^2|_A` must be read as the Cartesian square `C x C`, and the pair notation forces that reading. In the coding literature `C^2` very commonly denotes the Schur/square code, and this chain sits next to genuine Schur-square material. No misreading has occurred anywhere in the chain; flagged only because an import statement is the place such a collision would first bite.

### F9 — hostile extension available (not a defect).

The import is row-general but the bracket is specialized only at `n=2^41, k=2^40`. Under the descriptor family (`n=2^s, k=2^(s-1)`, `s=1..41`) the same specialization is mechanical for every `s`. This is precisely the round-29 ROW-SIZE SCOPE pattern already flagged one lane over on the LIST side (`critical/nodes/rate_half_list_adjacent_crossing/statement_addenda/16-round29-row-size-scope.md:1-9`). Since `rate_half_band_crossing_location`'s own pose is fixed at the official row, this is an opportunity rather than a quantifier gap — but it is cheap and it is the natural companion to F1.

---

## ATTACK LOG (every attack run, with what-would-have-killed)

| # | attack | result | what would have killed |
|---|---|---|---|
| A1 | `E_m` exclusion vs `B_mca` exclusion, both sides quoted | MISS (M-A) | unrestricted `B_mca` count, or no matching exclusion |
| A2 | same-support quantifier on both sides | MISS (M-B) | global-vs-witness support mismatch |
| A3 | `>= a` vs `>= (1-gamma_m)n` inclusion direction | MISS (M-C) | floor on `a_m`, or `B_mca` at exact agreement |
| A4 | max-over-pairs vs for-every-pair | MISS (M-D) | a typical/random-pair hypothesis in `(HJ1)` |
| A5 | finite vs projective slope set | MISS (M-E) | `z=oo` on one side only |
| A6 | repo RS convention `deg<K` verified independently | MISS (M-F) | any `deg<=k` reading at the official row |
| A7 | `rho=k/n` counterfactual recomputation | MISS (M-F) | banked `a_m` safe under both — it is not, so the check had teeth |
| A8 | floor/ceil safe-direction audit | MISS (M-G) | reversed rounding, or a float inside an assertion |
| A9 | full ladder `m=3..96` re-derived from `(HJ1)` alone | MISS (M-H) | one integer off |
| A10 | closed forms `(RHJ1)`/`(RHJ2)` vs `(HJ1)` for all `m` | MISS (M-H) | a transcription slip in `N_m/D` |
| A11 | razor thresholds `Q_94*2^128 < 2^255.9 < Q_95*2^128 < 2^256` | MISS (M-H) | `m=94` unaffordable on some razor row |
| A12 | `m=96` infeasibility against `B* <= 2^128-1` | MISS (M-H) | `Q_96 <= 2^128-1` |
| A13 | `Q_m` monotone across the cap boundary | MISS (M-H) | nonmonotone `Q_m` making "largest affordable" ill-defined |
| A14 | Johnson-radius non-crossing for every affordable `m` | MISS (M-I) | `a_m <= sqrt(n(k-1))` |
| A15 | field generality / O6 / `e in {1..6}` | MISS (M-J) | a no-subfield, primality, or smoothness premise |
| A16 | BCHKS25 linear-refinement leak sweep | MISS (M-K) | any downstream numerator using the linear formula |
| A17 | second consumer's `CA <= MCA` transport | MISS (M-L) | `epsilon_ca` as an all-pairs max |
| A18 | `K` vs `K+1` in the shell cap | MISS (M-L) | Haboeck applied to `C+` while `Q_m` used `C`'s rate |
| A19 | CA-to-MCA fence direction | MISS (M-L) | the shell cap using the fenced direction below `3n/4` |
| A20 | round-28 retired surgery re-run? | MISS (M-M) | any claimed `mca_safe` bar movement |
| A21 | `3n/4` staleness sweep, LIST branch | MISS (M-N) | LIST nodes treated as Haboeck consumers |
| A22 | consumer-obligation vs supplier-coverage tiling | **HIT (F1)** | the addendum stating the general `m(q)` form |
| A23 | `3n/4` staleness sweep, MCA branch | **HIT (F2, F3)** | a forward pointer at the headline / a corrected sentence |
| A24 | printed constants vs verifier output | **HIT (F4)** | `232.650530` printed, or the verifier asserting the string |
| A25 | edge-type consistency, both ends | **HIT (F5)**, not novel | a compile-time dedup/conflict check |
| A26 | provenance / vendored fragment / audit pin | **HIT (F6)**, zero power | the audit file in-repo, or named for Thm 2 |
| A27 | upstream import ledger coverage | **HIT (F7)** | a ledger row for the import |
| A28 | banked verifiers replay | pass (3/3) | any assertion failure |

Verifier replay, for the record:
```
HABOECK_QUADRATIC_JOHNSON_MCA_IMPORT_PASS
RATE_HALF_HABOECK_QUADRATIC_JOHNSON_SAFE_BRACKET_PASS m_first=9
  log2_q_first=232.650530093386 m_cap=95 log2_q95=255.957039295531
  a95=1563128173124
RATE_HALF_HABOECK_QUADRATIC_JOHNSON_SAFE_BRACKET_AUDIT_PASS
```

---

## ZERO-POWER DECLARATIONS

1. **Haboeck's actual Theorem 2.** No network, and no vendored copy exists in this repo (`experimental/` is absent). I cannot check whether the source quantifies over *arbitrary* received pairs or restricts to far pairs; whether it carries a field hypothesis (characteristic, prime field, `q > n`); whether it constrains the evaluation domain; or whether the constant is `ell^7/3`. **Everything in D1 and D2 that I certified is certified as an *internal consistency* result: the import's printed event matches the repo's MCA event, and the specialization matches the import. Whether the import's printed event matches the paper is out of my reach.**
2. **The pinned upstream audit** (`audit_bchks25_thm46_conditional_johnson_import.md` @ `93fba1be`, blob `ef064597...`) is not in this repo. The claim "statement and proof audit" rests on it entirely.
3. **Citation reconciliation.** `audit.md:11-13` says the source's Claim 5.7 citation is version-sensitive and reconciled upstream with BCIKS20 Claim 5.6/(5.10). Unverifiable offline.
4. **Quarantine-induced blindness.** I did not read `notes/pilots_20260802/CAMPAIGN_LEDGER.md` or the three sibling round-32 directories. I additionally self-tightened to read *no* `pilots_20260810` directory other than my own, to remove any ambiguity about which are round-32 siblings. All novelty claims (F1, F4, F7) are therefore relative to everything else readable, and could be duplicated in those five places.

**Outward verification question for the coordinator (one, specific):** does `experimental/notes/audits/audit_bchks25_thm46_conditional_johnson_import.md` @ `93fba1be` actually audit **Haboeck ePrint 2025/2110 Theorem 2** — namely (i) the quantifier over received pairs (arbitrary, or far-only), (ii) any field or evaluation-domain hypothesis, and (iii) the constant `(ell^7/3)` and the exponent 7 — or does it audit only the BCHKS25 Thm 4.6 *conditional* Johnson import that this node explicitly excludes? If the latter, the import node's closure line should read "statement audit; proof by citation" and F6 becomes load-bearing rather than cosmetic.

---

## COMPLIANCE

**Interpreter invocations: 8, all under `tools/ramguard` with a literal `--`, all from the repo root, all stdlib-only** (`fractions`, `math`, `json`, `os`, `collections`). Zero bare `python3`. Breakdown, with the `RAMGUARD_TIMEOUT` documented per use:

| # | profile | `RAMGUARD_TIMEOUT` | script |
|---|---|---|---|
| 1 | `tiny` | `60s` | `notes/pilots_20260810/rh_haboeck_seam/edge_scan.py` |
| 2 | `local` | `300s` | `notes/pilots_20260810/rh_haboeck_seam/rederive.py` |
| 3 | `local` | `300s` | `notes/pilots_20260810/rh_haboeck_seam/logcheck.py` |
| 4-5 | `local` | `300s` | `notes/pilots_20260810/rh_haboeck_seam/staircase.py` (twice: head, tail) |
| 6 | `tiny` | `60s` | `background/nodes/haboeck_quadratic_johnson_mca_import/verify.py` |
| 7 | `local` | `300s` | `background/nodes/rate_half_haboeck_quadratic_johnson_safe_bracket/verify.py` |
| 8 | `local` | `300s` | `background/nodes/rate_half_haboeck_quadratic_johnson_safe_bracket/verify_audit.py` |

All 8 completed inside their ceilings; no OOM, no timeout, no Modal, no network, no git.

**RAM discipline.** File-at-a-time reads throughout; the one large statement (`critical/nodes/rate_half_band_crossing_location/statement.md`, 44 KB) was read only in bounded windows (lines 40-101, 130-157, 728-787) located by `grep -n` first. **`dag.json` was never opened or read into memory.** Honest disclosure: two early recursive greps were rooted at `.` and therefore *streamed* `dag.json`, so five of its lines appeared in grep output; every subsequent grep excluded it explicitly, and no finding depends on it. The edge scan reads only `node.json` shards.

**Write scope.** Writes confined to `notes/pilots_20260810/rh_haboeck_seam/`: an append to `PREREG.md` under "## Pilot registrations" (made after the two named anchors and before any other read), plus `edge_scan.py`, `rederive.py`, `logcheck.py`, and `staircase.py`. **The `REPORT.md` write was REFUSED by the harness** (anticipated by the brief), so this report exists only as the returned message — the coordinator must bank it. No `dag/`, `nodes/`, `critical/`, `background/`, or `tools/` file was modified; no git operation was run; no path containing `prize-codex-` was touched; no subagent was launched.

**Quarantine.** `notes/pilots_20260802/CAMPAIGN_LEDGER.md` never opened. The three named round-32 siblings (`rh_fr_algebraic`, `rh_farca_upper`, `rh_residuals_close`) never read, and excluded by pattern from every grep. Self-tightened further to read no `pilots_20260810` directory but my own; that tightening is declared as zero-power in item 4 above.

**Surgery.** None. F1-F4 and F7 are drafted as recommendations only; every one of them touches a node file and is coordinator-gated per AUDIT-AND-DRAFT.
