# REPORT — c2pp_diag (persisted verbatim by the coordinator from the session transcript, task a72521ce78de75db3, 2026-08-07)

All artifacts are confined to the pilot directory (dag.json's mtime is 10:46, hours before this session started). Report follows.

---

# C2''/C1' MYSTERY-3 DIAGNOSIS — round 23, `c2pp_diag`

**Headline:** C2'' does not have the standing the board records. Its own falsifier of record (F-b) **fires** at every `theta` above the pinned value, inside the range the pose declares immaterial. Separately, the node's wired statement is strictly stronger than the clause both survived F-rounds tested, and the qualifier that marks the difference exists in exactly one line of one script. No status flip proposed — verdicts and artifacts only.

## Self-corrections, stated plainly

1. **The brief's premise was wrong and I registered the correction before computing** (`PREREG.md` §P0). C2'' was *not* "posed but never attacked": `conditional.md:8-10` says verbatim "*F-round state 2: rounds M1 + the 2026-07-13/14 round both survived*". The event the brief remembered is the 2026-07-07 F-round that refuted the **predecessors** C1 and C2 (`F_ROUND_CONJECTURE_FALSIFICATION.md:106-110`: "*C1-as-frozen: REFUTED (F1). C2-as-frozen: REFUTED (F2b).*"). C1'/C2'' are the successors. My round is therefore **F-round 3**, and replaying F-a/F-b/F-c would not have been an attack — so I registered a new family, F-d.
2. **Prediction PR2 refuted.** I predicted `coset_mass_share ≥ 0.90` at both high-loss rows; measured 0.4444 at (2,8353). Wrong.
3. **Prediction PR4 was mis-posed.** `coset_leakage` at (2,32801) is undefined (stripped conditional mass is exactly 0), not a number I could compare to 1.554406. I had registered the NaN branch in advance so the escape test still resolved, but the prediction as an inequality was untestable.
4. **My working hypothesis that the coset column was *the* overflow mechanism was wrong.** At (4,97) `coset_leakage` = 0.9807 &lt; 1 and the accident column carries the overflow. The mechanism is row-dependent.
5. **My own refutation rests on the same transport as the survival I attack.** Both use uniform 33× stacking. I therefore do *not* claim a kill on that basis; the honest instrument is the symmetric not-evidence clause in D5, which retires my F-d result along with F-b's survival. Only the `theta` result (below) is a kill under the node's own rules without needing a new transport judgement.

## D1 — State reconstruction (compressed)

- 2026-07-07: F-round kills both frozen conditions. C1 died on normalization ("*the flaw is the NORMALIZATION: cluster/generator mass is absolute (does not scale with iid mass)*", `F_ROUND_CONJECTURE_FALSIFICATION.md:17-19`). C2 died on measurement — `F_ROUND...md:87-92` banks raw junction ratios **4.25** at (t=2,q=8353) and **8.40** at (t=2,q=32801), "*Geometric mean 2.14 &gt; the 1.57/junction budget; the ratio GROWS with q*", with the decisive cut "*the correlation is carried by (a) the k=0 COSET class*".
- 2026-07-10: **C2'' posed** as a three-part shape — clause (i) coset routing "*budget arithmetic, never correlation*" (`C2PP_POSED_20260710.md:22-28`); clause (ii) the conjecture proper, `E_U[prod_j rho_j]_reduced &lt;= 2^R_joint * prod_j E_U[rho_j]`, `R_joint = 21` (`:35-36`); clause (iii) accidents charged once at absolute weight (`:43-49`).
- 2026-07-13: M1 and round 2 both survive; C1'-r2 is **killed** (K'=6.199), demoting the baseline arm. 2026-07-19/21: C1'-r3 minted, Decision 6 wires the conditional route.
- **Since 2026-07-13 the C2'' node has not moved**: `statement.md` and `attack.md` still carry 2026-07-13 mtimes; `node.json` moved only in the 2026-08-03 manifest refactor. It is genuinely the stalest board item.

## D2 — Consumer contract from CURRENT dag edges (not memory)

Read from `dag.json` directly. The wiring **did** change after the F-round — Decision 6 (2026-07-21) promoted the non-circular decomposition from ev to req:

```
dli_c1r3_gated_envelope_bound  --req--&gt;  dli_marginal_baseline100_coverage   (dag.json:44230-44232)
dli_wcl_zone_coverage          --req--&gt;  dli_marginal_baseline100_coverage   (dag.json:37015-37017)
dli_marginal_baseline100_coverage --req--&gt; dli_prime_weighted_large_block_support (dag.json:37025-37027)
dli_c2pp_joint_reserve         --req--&gt;  dli_prime_weighted_large_block_support (dag.json:37030-37032)
dli_prime_weighted_large_block_support --req--&gt; x4_exactlist_staircase_split  (dag.json:35285-35287)
x4_exactlist_staircase_split   --req--&gt;  tr_perleaf_list_ident               (dag.json:33975-33977)
```

Statuses: `dli_c2pp_joint_reserve` **TARGET**; `dli_prime_weighted_large_block_support`, `dli_marginal_baseline100_coverage`, `dli_wcl_zone_coverage`, `x4_exactlist_staircase_split` all **CONDITIONAL**; `dli_c1r3_gated_envelope_bound` **TARGET**.

**Quantified need.** The consumer face asks for the **unreduced** quantity: `REDUCTION_PACKET.md:51` "*prize budget q^{-t+H} W_cen &lt;= 2^122 [#40: superseded display; binding = 2^121]*", and `:62` "*equivalently half-band count &lt;= 2^121*". Decision 6 splits it 21 + 100 (`conditional.md:3-18`). So C2'' must deliver a bound on `X(R)` itself relative to `A(R)` — exactly the form the pose does not defend.

## D3 — C2'' made exact + the adversarial attack

**The gap, located to the line.** The token `_reduced` appears in the entire `critical/` + `background/` + `dag.json` corpus in exactly one C2''-bearing place:

- `m4_assembly_verifier.py:112` — declared input: `"E_U[prod_j rho_j]_reduced &lt;= 2^R_joint * prod_j E_U[rho_j] ... (coset-routed, accident-decomposed; clauses i+iii exact accounting)"`
- `m4_assembly_verifier.py:827-828` — the A5 step that uses it: `# A5: the joint reserve (C2'', named conditional):` / `#   E_U[prod rho] &lt;= 2^21 * prod E_L` — the qualifier is gone.

It is absent from `statement.md`, `node.json`, `dag.json`, and `conditional.md`. The A5 arithmetic check is `reserve * prod &lt;= endpoint` (a pure constant comparison), so none of the ten mutation controls can catch the drop.

### F-d (coset-routing neutrality) — FIRED

Positive control passed first (8/8 banked raw ratios bit-exact, 8/8 pose bulk values, GM 0.966561 → 0.967). New functionals per `PREREG` §P2.

| row | raw | κ=raw/stripped | σ (cond coset share) | σ_u (uncond) | 33·log₂raw | clause-(ii) vacuous |
|---|---|---|---|---|---|---|
| (2, 97) | 0.9983 | 1.0000 | 0.00161 | 0.00148 | −0.08 | . |
| (2, 193) | 1.0101 | 1.0004 | 0.00385 | 0.00294 | 0.48 | . |
| (2, 8353) | 4.2514 | 1.5451 | 0.44444 | 0.12227 | **68.90** | **YES** |
| (2, 32801) | 8.3989 | NaN | 1.00000 | 0.38525 | **101.32** | **YES** |
| (3, 97) | 1.0392 | 1.0056 | 0.11165 | 0.10653 | 1.83 | . |
| (3, 193) | 1.1635 | 1.0913 | 0.43750 | 0.38583 | 7.21 | . |
| (4, 97) | 2.8187 | 0.9807 | 0.09091 | 0.10653 | 49.34 | . |
| (4, 193) | 3.5663 | NaN | 1.00000 | 0.38583 | **60.54** | **YES** |

All three registered escapes fail (E-a, E-b, E-c). **F-b's scoring set drops the high-loss rows by construction**: `c2r2_local.py:93` reads `bulk_rows = [(b, ...) if b &gt; 0]`, and `bulk_ratio` is 0 at exactly those rows. Reproduced F-b's banked path (x_max 1.066159 at (3,193) → 14.523%, matching the banked 14.53%) against the unfiltered path (x_max 8.398887 → 482.460%, exact `Fraction`: `raw_max^33 &gt; 2^21`).

**F-d-C — clause (i) tested directly.** `coset_internal_ratio` ι = **1.0000 exactly at 6/6 rows** (the coset class is internally uncorrelated — clause (i) is right about that). But `coset_weight_shift` ω = 15.45, 21.80, 2.41, 9.24 at the overflow rows vs 1.09, 1.32 at controls: null states land in the coset class up to 21.8× more often. Freezing all internal means and moving only the weights (`mixture_only_ratio`) gives 3.47 / 9.91 / 1.73 / 4.27 → 26.2 to 109.2 bits at 33×. So clause (i) conflates *internal-correlation-freedom* (true) with *contribution-freedom* (false): the conditioning **selects** the coset class, and selection is correlation in the only sense `X/A` measures.

**F-d-B — clause (iii)'s "counted once".** F-b charges accident mass once (worst 0.00086 bits = 0.004% of reserve), but the accident column's own multiplicative factor at (4,97) is 3.7834 → **63.35 bits at 33×** (301.7% of reserve). On clause (iii)'s *own* q-independent window law, a 33-junction tower expects **1343.86** accidents at (2,8353) and **15.32** at (4,97): "counted once" is non-conservative at 2/8 banked rows.

### The decisive result — F-b fires at every theta above the pin

The pose states: "*theta = 2 is a pose-time convention (results insensitive for theta in [2,4] at the 8 rows)*" (`C2PP_POSED_20260710.md:93-95`). Re-running **F-b's own kill rule on F-b's own search set**, changing nothing but theta:

| theta | x_max | F-b score | % of 21-bit reserve | F-b |
|---|---|---|---|---|
| 2.0 | 1.066159 (3,193) | 3.0508 bits | 14.53% | does not fire |
| 2.5 | 2.238705 (2,8353) | 38.3683 bits | **182.71%** | **FIRES** |
| 3.0 | 2.238705 | 38.3683 bits | **182.71%** | **FIRES** |
| 4.0 | 2.238705 | 38.3683 bits | **182.71%** | **FIRES** |

Spread 35.3 bits across a range the pose calls immaterial. Mechanism: at (2,8353) the theta=2 cut calls three classes accidents, with class ratios **6.6204** (k=7), **2.2414** (k=12), **2.1429** (k=14). The last two clear theta=2 by 0.24 and 0.14. Any theta &gt; 2.2414 returns both to BULK, where they are charged 33× at 2.2387/junction instead of once at 0.0003 bits. **The 85% margin is produced by that classification, not by the tower.**

**What the attack could not reach** (registered in advance, `PREREG` §P6): no official-row inference — every reading is n=32, t ≤ 4, and the only transport used is the packet's own pinned `x**33`. It does not show clause (ii) is *false* (vacuous is not false). It does not settle whether the packet's exact staircase account may legitimately move coset mass onto the `A(R)` side; it shows only that `A(R)` **as defined** (`prod_j E_U[rho_j]`, unconditional) does not contain it.

## D4 — Cross-lane matrix

| Family | Current node(s) | Verdict |
|---|---|---|
| Ternary suppression (ES / master threshold) | `background/nodes/es_ternary_suppression_instruments`, `tern_master_threshold`, `dli_c1_ternary_relation_norm_sandwich` | **FAILS** — emptiness predicates on ternary vectors, not a measure ratio; C2'' is not among the three enumerated instances and THEOREM PT forbids a monotone statement spanning the τ regimes; official rows sit in ES's own proved gap (`es_...:60-62`) |
| Ternary suppression, **dli-lane variant** (the only wired one) | `dli_norm_gate_forward_and_ofold` (LN2), `dli_official_support_forcing` (OS-2/OS-3), `dli_norm_gate_splitting_law`, `dli_norm_gate_energy_ceiling` — 3 `ev` edges into C2'', minted 2026-08-02/03 | **APPLIES (partial)** — kills states in `X(R)` exactly and **uniformly across all 33 junctions** (`rho_0 = 0`); the only banked instrument with the required all-junction reach. Stops at its own line: "*Not a bound on states with \|S_0\| &gt;= 4 ... exactly the open territory (count bounds, not max-norm bounds)*" (`dli_official_support_forcing/statement.md:98-101`) |
| Constant-weight / prescribed-sum (**U2**) | `rate_half_list_adjacent_crossing/statement_addenda/14-round22-u2-accident-cap.md`; `pilots_20260807/bb_nu_transport/PROOFS.md:149-157` | **FAILS** — cardinality cap on prescribed-sum subsets of `Z/2L`, priced against `B*` on the crossing lane, different accident notion, 42.6 bits lossy against a 21-bit reserve; and `esg_lane_rescope` formally **unwires** the dli lane from that balance family |
| Z-2 moments | `f2_z1_mass_knife_edge` (Z-2 at `:35-38`) | **FAILS** — as a supply it closes only at `p &lt;= 8.30` vs official `log2 p &gt;= 39`; its DLI gift lands on `dli_wcl_newton_short_window_exclusion`, and WCL is scope-excluded from C2''. The round-22 R-locality floor is anti-transport and **corroborates** the pessimism |
| WCL slot certificates | 10 `dli_wcl_slot_*_emptiness` (1 PROVED / 9 TARGET), `dli_wcl_zone_coverage` | **FAILS by explicit exclusion** — `dli_wcl_zone_coverage/statement.md:26-28`: "*No C1' inequality, C2'' joint reserve, residual near-peak bound, or final endpoint check is part of this statement.*" They feed the **(P2)** 100-bit denominator arm, not the **(P1)** joint-reserve arm. Closing all ten would make C2'' the sole remaining unproved predicate — a scheduling fact, not progress |

**Has the standing changed since the F-round? Yes, twice — and neither is recorded in `node.json`.**

1. **2026-08-01, Pro's adversarial audit** (`notes/pro_briefs_20260801/responses/BRIEF2_ADVERSARIAL_AUDIT_SUMMARY.md:40-43`): "*The C2R2 "14.53% of reserve" margin is NOT evidence about the true joint ratio — it stacks one-junction proxies... Empirical support for the measured proxy only.*" With the 32-wise trap (`:16-22`): at the admissible gate prime `q = 3*2^41+1`, "*the 33 moment-curve forms on F_q^32 are 32-wise independent — every proper subtower exactly iid — yet the full product is q &gt; 2^21, via a unique circuit supported on ALL 33 junctions.*" This is my not-evidence clause, reached independently and earlier.
2. **2026-08-02, `c2pp_nullity_structure`**: the designated replacement route (NUL0–NUL4) was built, validated 42/42, and **retired by its own pre-registered kill line**. It found the same split I did from the other side — `REPORT.md:11`: "*the joint excess `R` is carried by the `delta = 0` stratum*", and `:67` "*L9 the joint excess is carried by delta=0 (91% at (32,4,97))*" — i.e. **noncoset at exactly the row where my `coset_leakage` &lt; 1**.

## D5 — The re-pose of record (draft at `notes/pilots_20260807/c2pp_diag/REPOSE_C2PP_R3_DRAFT.md`)

**C2''-r3 (aggregate, non-uniform, transport-explicit).** For every official prize row `R`, over the actual 33 junctions of the official 34-level schedule:

```
sum_{j=1}^{33} log2( E_U[ rho_j | state_{&lt;j} null ] / E_U[ rho_j ] )  &lt;=  21.
```

Equivalently the unreduced `X(R) &lt;= 2^21 A(R)` the consumer needs, stated as a genuine sum. No per-junction bound, and **no clause licenses discarding a column before the sum is taken.**

**Binding not-evidence clause (symmetric — the load-bearing repair).** A single-junction measurement multiplied by 33 is **not** evidence for C2''-r3 **and not** evidence against it. This retires, together, round 2's 85% margin and this pilot's 482% F-d reading — same arithmetic, different columns of the same banked rows. The pose already disclaims the uniform form for the *claim* (`statement.md:22-23`); this makes the disclaimer binding on the *evidence*, which is what was missing.

**Pre-registered falsifier.** (G-a) a measurement of the junction sum over `|J| &gt;= 8` **consecutive** junctions of a **single** tower with a separately justified `J → 33` transport, exceeding 21 bits; or (G-b) `sum_j log2(omega_j)` growing without bound in q over `&gt;= 8` consecutive junctions at `&gt;= 3` q-scales. Uniform stacking is excluded on both sides.

**Mandatory pin if any three-part form is kept:** `theta` must become an operative constant (like P-CONS/P-FIELD) with a verdict-stability requirement over its declared range. C2''-r3 avoids this by taking no decomposition.

**Cost of the next decisive test.** The pose's own honest-gaps line names it: "*No multi-junction joint measurement beyond t=4/n=32*" (`C2PP_POSED_20260710.md:92-93`). Every banked C2'' number — M1's, round 2's, mine — is a shallow-tower reading transported to 33 junctions by convention. The instrument that carries `&gt;= 8` consecutive junctions of one tower does not exist in the repo. The 32-wise trap sets the bar higher still: any instrument with reach `k &lt; 33` is defeatable by construction at an admissible gate prime. **Until such an instrument exists, C2'' is neither supported nor refuted by any banked number — it is unmeasured at its own quantifier depth.**

## Predictions vs outcomes

| | registered | outcome |
|---|---|---|
| PR1 | bulk ∈ {0,NaN} while raw &gt; 1.5544 at (2,8353),(2,32801) | **CONFIRMED** |
| PR2 | σ ≥ 0.90 at both | **REFUTED** — 0.4444 at (2,8353) |
| PR3 | κ(2,8353) = 1.544 ± 0.02 | **CONFIRMED** — 1.5451 |
| PR4 | κ(2,32801) &gt; 1.5544 | **UNTESTABLE as posed** — NaN (stripped mass = 0); stronger fact obtained (σ=1.000 vs σ_u=0.385) |
| PR5 | raw at (4,97),(4,193) = 2.82 / 3.57 | **CONFIRMED** — 2.8187 / 3.5663 |
| PR6 | F-b's x_max = 1.0662 comes from (3,193) | **CONFIRMED** — 1.066159 at n32 (t=3,q=193), 14.523% |
| PR7 | F-d yields a structural finding, not a kill under the node's own rules | **CONFIRMED for F-d** — but the unregistered theta follow-up *is* a kill under F-b's own rule |

## Catches for the coordinator (I edited nothing)

- **C-1** `_reduced` dropped between `m4_assembly_verifier.py:112` and `:827-828`; absent from `statement.md`, `node.json`, `dag.json`, `conditional.md`. The wired claim is stronger than the defended one.
- **C-2** `c2r2_local.py:93` `if b &gt; 0` filter drops the high-loss rows from F-b's scoring set by construction.
- **C-3** `theta` insensitivity claim (`C2PP_POSED_20260710.md:93-95`) refuted on its own 8 rows; F-b fires at theta ∈ {2.5, 3.0, 4.0}.
- **C-4** F-c's rare-window restriction `lam_window &lt;= 1/2` (`c2r2_falsifiers.md:107-108`) excludes the classes carrying `lam = 40.72` at (2,8353) — so all three falsifiers exclude the high-loss cells, by three different mechanisms.
- **C-5** `node.json:8` cites the c2r2 packet at `background/nodes/dli_c2pp_joint_reserve/notes/c2r2_fround2_20260713/`; that path does not exist (packet is under `critical/`).
- **C-6** `m4_assembly_verifier.py:122` `"rounds_survived": 1` — stale, should be 2.
- **C-7** `node.json:8` still presents the 14.53%/85% margin as live evidence after Pro's 2026-08-01 retroactive demotion.
- **C-8** The FD schema takes as its first instance "*the c2pp bulk identity (worst case 1.0662, monotone-decreasing slope)*" (`notes/roadmap/sections/03-unifying-lemmas.md:519-524`) — the selection-biased number. `07-tracks.md:1913` already gates the schema on this adjudication.

The risk register anticipated this outcome: "*c2pp reserve break | round 3 breaks the 2^21 reserve (round 2 used 14.53%) | Decision 6 reversed; B-WEAK-direct re-pose from mechanism data*" (`notes/roadmap/sections/05-risk-register.md:6`).

**Artifacts** (all in `notes/pilots_20260807/c2pp_diag/`, all reproducible under `tools/ramguard`, stdlib only): `PREREG.md` (registrations appended before computing), `fd_coset_routing_attack.py`, `fdb_accident_multiplicity.py`, `fdc_coset_mechanism.py`, `fdd_theta_fragility.py`, their four `*_results.json`, and `REPOSE_C2PP_R3_DRAFT.md`. Nothing outside the pilot directory was written.
