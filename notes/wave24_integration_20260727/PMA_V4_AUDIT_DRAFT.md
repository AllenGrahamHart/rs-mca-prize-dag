# v4 PMA campaign audit (round 21) — DRAFT

Auditor: Opus AUDIT agent, 2026-08-07.
Worktree audited: `/home/u2470931/smooth-read-solomin/prize-codex-resolution-v4-20260713`
(branch `codex/full-prize-resolution-v4-20260713`, HEAD `899326a8`, 2026-07-18).
Canonical: `/home/u2470931/smooth-read-solomin/prize`.
Target node: `critical/nodes/l1_mixed_petal_amplification/` (mystery 6).

Neither tree was modified. This file is the only artifact written.

---

## 0. Headline

The v4 PMA campaign is **already fully imported into canonical**. Node-for-node,
byte-for-byte, canonical is at or ahead of v4 on every PMA artifact. The
"un-surveyed campaign" premise is **false at the node level** — wave-8
(2026-07-16) and wave-9 (2026-07-17) imported it, and
`v4_pma_crosswalk.md` already records the verdict.

What the round-21 survey *does* produce that is new — **two audit catches**,
both against canonical's current state rather than against the campaign:

1. **C-V4-1** — canonical's *current* reading of the N10 census in `attack.md`
   is not supported. The reported fall in the growth exponent is largely a
   **field-size artifact**, and v4's own census contains the control that
   proves it. Field-corrected, the exponent is **flat at ~6.14–6.21**, not
   falling to 5.25 — and it sits *above* the `n^6` line that v4 separately
   proved insufficient.
2. **C-V4-2** — canonical carries a PROVED node whose Scope section justifies
   itself by a hypothesis (`sigma >= C n/log n`) that canonical's own `imgfib`
   node declares **struck per catch #155**. Forced correction; the entropy
   reserve carries the argument alone with a 2048× margin.
3. **Replay evidence**: 32/32 v4 PMA verifiers and 33/33 canonical PMA
   verifiers PASS, with genuine mutation controls throughout.
4. **A retraction-compliance verdict**: the campaign **respects** the
   2026-07-05 petal retraction, structurally and semantically.
5. **An epistemic-hygiene verdict**: the campaign retracted itself **eight
   times**, including refuting its own central construction. Nothing in it
   needed external catching.
6. Four un-imported Modal driver scripts (secondary; the load-bearing
   per-node `verify.py` files are all present in canonical).

---

## 1. Campaign shape

### 1.1 Scope and boundary

The worktree is not a pure Codex branch: it interleaves Codex proof commits
with canonical-side audit commits (`orbit: rebuild`, `catch #NNN`, wave
integrations). 1208 commits total; 187 in the 2026-07-12..15 window.

The PMA sub-campaign proper runs **2026-07-13 → 2026-07-15** and ends with
`ae2e5dd5 "Prove PMA projective Johnson bound"` (2026-07-15). Commits after
2026-07-15 in this worktree are C36 / XR / DLI / rate-half-Hankel lanes, not
PMA. HEAD `899326a8` (2026-07-18) is `"Tighten C36 energy endpoint"`.

### 1.2 Artifact inventory

- 35 `background/nodes/pma_*` folders, 1 `critical/nodes/pma_exact_periodic_owner`,
  1 `critical/nodes/petal_mixed_amplification` (the v4 name for this node).
- 32 executable `verify.py` files.
- 6 `experiments/prize_resolution/modal_pma_*.py` Modal drivers + 2 result JSONs.

### 1.3 Phase structure

The PMA sub-campaign proper is a ~12-hour burst (2026-07-14 20:14 →
2026-07-15 07:56, ~30 commits), bracketed by two scope audits. Its own
narrative device is the numbered "Integration note rNN" sections of
`notes/PRIZE_RESOLUTION_ROADMAP.md`.

| phase | commits | what happened |
|---|---|---|
| 0 prologue (07-13) | `a8358e55`…`d03db734` | petal lane closes; `34138c70` promotes **`imgfib` + `petal_growth` + `m_le3_route` to PROVED** |
| 1 scope defect (07-14) | `8aeec4be` (r38) | **un-proves the previous day's headline**: `imgfib` PROVED→CONDITIONAL; mints `pma_wide_residual` as the new atomic red |
| 2 owner/payment ladder (07-14→15) | `cdaccfec`…`6f799109` (r54–r71) | 13 PROVED supplier nodes under `pma_wide_residual`; prints `N_top`, `B_post = n^6 − N_top` |
| 3 chart multiplier (07-15) | `1f429973`…`88423f87` (r72–r75) | paired-core normalization → abundance route-cut → first-layout domination |
| 4 **refutation + re-pose** (07-15) | `b9beb6e8` (r76), `0b6f5ea7` (r77) | **refutes `pma_wide_residual` outright**; mass `git mv` of the whole `pma_*` family `critical/`→`background/`; adds the σ=1 variable-defect floor and `petal_reserve_rich_fiber_reduction` |
| 5 rebuild (07-15) | `e1f50a1c`…`ae2e5dd5` (r79–r92) | 10 more PROVED nodes on the re-posed target; closes rate-quarter |
| 6 rate-half tail (07-16→17) | `0469c8c2`…`36b3c932` (r93–r101) | the five-node `pma_ratehalf` ladder (this is wave-9's addendum, *after* the stated 07-13..15 window) |

Net effect on the critical surface: **44 PROVED background lemmas, 1 REFUTED
node, one critical node (`imgfib`) demoted PROVED→CONDITIONAL, and the target
itself still TARGET.** The campaign's net contribution to the *red count* was
negative — it un-proved more than it proved at the critical level. That is a
mark of honesty, not of failure.

### 1.4 What it claimed

The campaign's own contract is in
`critical/nodes/petal_mixed_amplification/claim_contract.md`. Its claim:

> `claim_contract.md:9-12` — "## Claim
>
> They admit one row-uniform polynomial bound plus explicit natural-scale
> profile charges that compose to the `imgfib` hypothesis."

And its own nonclaim, verbatim:

> `claim_contract.md:114-118` — "## Nonclaims
>
> The current target is not proved. The old `n^6` specialization is refuted.
> Raw kernel codimension, one fixed-pattern binomial bound, or closure of only
> a bounded `u+e` region is not promotion evidence."

**The campaign did not claim to close the node.** It ends TARGET, honestly.

---

## 2. What survived vs what the campaign retracted

### 2.1 The campaign's own central retraction

`critical/nodes/petal_mixed_amplification/conditional.md` is a self-retraction
record. Verbatim:

> `conditional.md:3-4` — "- **status:** TARGET
> - **former status:** CONDITIONAL on `pma_wide_residual`"

> `conditional.md:6-17` — "## Why the old implication was retired
>
> The former packet reduced the finite branch to
>
> ```text
> #Post<=B_post,       B_post<=n^6.
> ```
>
> That premise is false. The generic defect-four obstruction constructs more
> than `n^6` primitive source codewords after every global owner. The Top/Post
> partition then forces `#Post>B_post`. Keeping the old packet as an amber
> implication would be logically vacuous and would hide the actual proof
> obligation from the critical orbit."

So the campaign **killed its own conditional closure** and demoted to TARGET.
This matches canonical's crosswalk record ("The v4 conditional closure of
petal_mixed_amplification was retired for exactly this reason").

### 2.2 The campaign retracted itself eight times

This is the strongest positive signal about the campaign's epistemic hygiene.
Eight commits kill or narrow an earlier claim *of the same campaign*:

| # | commit (note) | kills | verbatim admission |
|---|---|---|---|
| R1 | `8aeec4be` (r38) | `34138c70`'s `imgfib = PROVED` | `imgfib/notes/mixed_petal_scope_audit_20260714.md:40-44` — "The 2026-07-13 promotion was not justified at universal scope. No proved child is false: the defect is a missing requirement edge." |
| R2 | `74225111` (r65) | `938ec17f`'s request for a "one-power saving" | `pma_sigma_one_d3_reciprocal_quadratic_obstruction/statement.md:70-75` — "The one-power saving requested after the fixed-hyperplane reduction is **false** for the complete diffuse source class." |
| R3 | `0c65de06` (r68) | an off-band induction sentence in `petal_growth/proof.md` | roadmap `:4869-4883` — "the promoted proof had also mentioned an unwired off-band top-coefficient induction. That sentence cannot support universal `imgfib`." |
| R4 | `aab9a46c` (r74) | the unweighted paired-core census strategy | `pma_wide_residual/statement.md:173-180` — "it rules out any proof that first bounds all paired cores by the primitive allowance." |
| R5 | `b9beb6e8` (r76) | **`pma_wide_residual` itself** — the entire Phase-2/3 endpoint | `pma_wide_residual/refutation.md:1-19` — "`#Post > n^6 − N_top = B_post`. This is the node's literal falsifier." |
| R6 | `0b6f5ea7` (r77) | the whole uniform σ=1 track | roadmap `:5347-5352` — "the exact mean floor has `51115` bits, exceeding `n^3000`… Thus a uniform sigma-one polynomial theorem is **false, not merely unsupported**." |
| R7 | `27ee6406` (r94) | `0469c8c2`'s out-of-tail fixture | roadmap `:6305-6309` — "its Johnson denominator was `J=3`, so it did not lie in the printed `J<=0` tail." |
| R8 | `36b3c932` | `deb8d257`'s linear-slice saving | `pma_ratehalf_complement_linear_slice_reduction/statement.md:309-313` — "this coordinate change **recovers rather than reduces** the earlier `e+1` freedom." |

R5 is the campaign's terminal self-refutation: it mass-`git mv`'d 134 files
from `critical/` to `background/` and demoted its own headline object.

**Audit judgement: this is a well-behaved campaign.** It falsified its own
central construction and recorded the falsification in the node folder rather
than quietly deleting it. Nothing here needed to be caught by an external
auditor because the campaign caught it first.

### 2.3 Surviving inputs

`conditional.md` lists ~25 surviving theorems under "## Surviving inputs".
All of them are present and PROVED in canonical. See §4.

---

## 3. Retraction compliance — PASS

The campaign is **post**-retraction (07-13..15 vs the 2026-07-05 cut). Verdict:
**it respects the retraction**, on three independent tests.

The 2026-07-05 manifest (`critical/nodes/petal_growth/RETRACTION_MANIFEST.md`)
cut six nodes:

> `RETRACTION_MANIFEST.md:5-11` — "## Cut (archived):
> - [TARGET] petal_cofactor_chargeability
> - [CONDITIONAL] petal_excess_induction
> - [CONDITIONAL] petal_kernel_realizable_sparsity
> - [CONDITIONAL] petal_mixed_amplification_step
> - [CONDITIONAL] petal_realizable_extra_uniformity
> - [CONDITIONAL] petal_residue_line_uniformity"

**Test 1 (carries the record).** v4 contains both
`archive/retraction_petal_20260705/` and
`critical/nodes/petal_growth/RETRACTION_MANIFEST.md`. PASS.

**Test 2 (no resurrection).** `git ls-files` in v4 shows **zero** tracked paths
for any of the six cut node ids outside `archive/`. PASS.

**Test 3 (no semantic dependence).** A grep for
`residue[- ]line|induction on c|naive induction|residue_line` across all
`background/nodes/pma_*`, `critical/nodes/pma_*`, and
`critical/nodes/petal_mixed_amplification/` returns **zero hits**. The union of
node ids cited by every PMA `dependency_subdag.md` contains only KEPT or
post-retraction nodes (`l1_coset_chart_residue_bridge`, `petal_g1_layer_maps`,
`petal_g2_support_forcing`, `petal_g3_full_support_codeword_injectivity`,
`petal_k4_primitive_bound`, `l1_core_defect_reduction`) — no cut node. PASS.

**Verdict: the campaign does not re-derive the retracted residue-line
induction.** Its route is orthogonal: it goes through an exact weighted-Hankel
kernel computation rather than an induction on `c`.

Note the campaign in fact addresses the retraction's stated obstruction head-on.
The retraction's reason was "dim K grows with c — the residue-line growth IS the
obstruction". `pma_saturated_mixed_support_kernel` computes that dimension
**exactly** rather than inducting past it:

> `pma_saturated_mixed_support_kernel/statement.md:59-66` (clause 6) — "On such
> an actual saturated pair, the rank is maximal subject to the known kernel
> vector: `rank T_(X,d)=min(d,w)`. If `d<w`, the kernel is exactly the line
> spanned by `F`. If `d>=w`, the rows are independent."

That is a legitimate post-retraction move, not a re-run of the killed route.

---

## 4. Subtraction — the campaign is already banked

Comparing every v4 PMA node folder against canonical:

- **35/37 folders are byte-identical** except for `node.json` (which v4 lacks
  entirely — v4 predates the v11 write-path shard convention and uses a
  monolithic `dag.json`). This is a structural, not a content, difference.
- **4 files differ in content**, and in **every** case canonical is at or ahead:

| file | direction |
|---|---|
| `pma_wide_residual/statement.md` | canonical AHEAD — adds "MASTER ORIGINAL STATEMENT (preserved at wave-8 import)" header |
| `petal_reserve_rich_fiber_reduction/statement.md` | canonical AHEAD — adds the 2026-08-03 `ell = 11` false-friend guard |
| `pma_aux_list_reduction/statement.md`, `proof.md` | equivalent content, different formatting (v4 reflowed; canonical keeps migrated-legacy form) |
| `pma_johnson_regime/statement.md`, `proof.md` | same as above |

- **Only 5 tracked PMA paths exist in v4 and not in canonical**:
  - `critical/nodes/petal_mixed_amplification/{statement,attack,conditional,claim_contract,dependency_subdag}.md`
    — this is v4's name for the node canonical renamed to
    `l1_mixed_petal_amplification`. Not missing content; a rename.
  - `experiments/prize_resolution/modal_pma_{source_aligned_gcd_excess,source_crossratio_fiber,tail_core_triple_excess,two_petal_support_fiber}.py`
    — four Modal **driver** scripts. Their corresponding per-node `verify.py`
    files ARE in canonical and pass. Low-value gap.

**Subtraction verdict: v4 re-derives nothing canonical lacks; canonical
contains everything v4 proved.** The direction of novelty is zero. Round-21's
value is therefore audit, not import.

Two formatting-only items are worth harvesting: v4's `pma_aux_list_reduction`
and `pma_johnson_regime` statements carry an upstream provenance ref canonical
dropped —

> v4 `pma_aux_list_reduction/statement.md:5-6` and
> v4 `pma_johnson_regime/statement.md:5-6` — "- **refs:** Przemek upstream
> `c35a6da3`, `experimental/notes/l1/l1_full_list_quotient_proof_program.md`"

vs canonical's `- **refs (legacy repo):** [...]` with no upstream commit. Minor
provenance improvement only.

---

## 5. Verified content — replay under the compute law

### 5.1 Compute-law note (environment)

`tools/ramguard` could **not** run: it uses `systemd-run --user --scope`, and
this WSL2 session has no systemd user bus (`/run/user/1000/bus` absent;
`Failed to connect to bus`). Verified this is environmental, not a sandbox
restriction (fails identically with the sandbox disabled).

Substitute used, with the **identical ceilings** from `tools/ramguard:40-52`:
a POSIX-rlimit shim (`ulimit -v` + `timeout --foreground --signal=TERM
--kill-after=10s`), `tiny` = 320M address space / 60s, `local` = 1280M / 300s.
All runs invoked as `<shim> tiny -- python3 <path>` from the worktree root,
literal `--`, falling back to `local` on failure. **No run needed the fallback.**

### 5.2 Results

- **v4 worktree: 32/32 PMA verifiers PASS**, all under the `tiny` profile,
  all in ≤5s.
- **Canonical: 33/33 PMA verifiers PASS** (32 + `petal_reserve_rich_fiber_reduction`).
  The imported material still verifies in canonical's tree.

### 5.3 Verifier quality — genuinely sound

These are not decorative. Sampled deeply; findings:

- **Exact integer arithmetic**, no floating point in the load-bearing bounds.
- **Mutation controls present in 29/32** — the verifiers deliberately
  re-run with a broken constant and assert the check *fails*. Example, from
  `pma_sigma_one_d4_generic_source_obstruction/verify.py`:

  > "# Removing the exact defect-set multiplicity destroys the contradiction.
  > `mutant = numerator // comb(core_size, 4)`
  > `assert mutant < n**6 * denominator`"

- **Official-grid sweeps**, not single cells: e.g.
  `pma_sigma_one_low_defect_payment` and `pma_sigma_one_d3_background_payment`
  each sweep `exponent in range(13,45)` × `denominator in (2,4,8,16)` = 128
  official rows.
- An initial `grep -c assert` census suggesting a weak tier was a **false
  alarm** — those files route every check through a `check()` helper wrapping
  a single `raise AssertionError`. True check counts are 4–38 per file; three
  files (`pma_sigma_one_{dyadic_near_coset_owner,odd_lift_boundary_owner,post_top_allowance}`)
  use bare `raise AssertionError` inside `if` blocks. **No no-ops found.**

### 5.4 Printed certificates (reproduced this session)

```
PMA_D4_GENERIC_OBSTRUCTION_PASS mean_floor_bits=104 n6_bits=97 ... mutations=2
PMA_VARIABLE_DEFECT_FLOOR_PASS mean_bits=51115 n3000_bits=48001 d=8192 a=8194 mutations=2
PMA_SATURATED_MIXED_SUPPORT_KERNEL_PASS patterns=60 hankel=60 maximal_rank=3 ... mutations=4
PMA_PETAL_PATTERN_ROOT_PINNING_LEDGER_PASS cases=3 extras=8 patterns=8 closure_checks=9 mutations=2
PETAL_RESERVE_RICH_FIBER_PASS checks=901 rows=128 min_rich=53 mutations=2
```

`mean_floor_bits=104` vs `n6_bits=97` reproduces the crosswalk's
"2^104 > 2^97 at (65537^2, 65536, 32768)" **exactly**. `mean_bits=51115` vs
`n3000_bits=48001` confirms the variable-defect floor beats even `n^3000`.

---

## 6. Crosswalk to the CURRENT node

### 6.1 Against the residue-line-growth obstruction

The retraction's obstruction ("dim K grows with c") is **addressed but not
removed**. `pma_saturated_mixed_support_kernel` clause 6 gives the exact rank
`min(d,w)` for saturated pairs, and `petal_reserve_rich_fiber_reduction` turns
the reserve-scale residual into a `Omega(n/log^2 n)` codimension statement. But
canonical's own guard is explicit that this is a reduction, not a count:

> `petal_reserve_rich_fiber_reduction/statement.md:65-67` — "This is a
> reduction, not a count of rich fibers. It does not prove that every rich
> fiber is quotient-periodic or that all such fibers have polynomial total
> multiplicity."

**Bearing: real but already banked.** No new movement on the obstruction.

### 6.2 Against the catch-#176 mass — **NEW CATCH C-V4-1**

This is the one place round 21 produces something canonical does not already
have wired.

Canonical's `attack.md` currently reads the N10 census as reassuring:

> `attack.md:14-22` — "**N10 growth round completed:** ... Counts grow
> `43 -> 2879 -> 109391` and `33 -> 2857 -> 108600`; the second doubling
> factor is about `38` in both schedules. The registered super-polynomial
> trend did not fire on these charts."

And the census note draws the evidential direction:

> `experiments/prize_resolution/l1_balanced_mixed_growth_census_result.md:46-48`
> — "The falling second ratio resists, rather than supports, the
> pre-registered super-polynomial trend on these charts."

**The problem.** That same note already concedes the confound but never
quantifies it:

> same file, `:28-31` — "The fields are the smallest convenient prime fields
> for these scales; the change from `F_97` to `F_193` is part of the scope and
> prevents treating the table as one nested-field family."

The census rows are `16,8,97` → `32,16,97` → `64,32,193`. So the **first**
doubling holds the field fixed and the **second** doubling *doubles the
field*. The two ratios are therefore not commensurable.

**v4 supplies the missing control.** `experiments/prize_resolution/pma_d4r0_census_results.json`
(byte-identical in canonical — already banked, simply unused here) contains a
field-size control at **fixed** `(n,k)=(32,16)`:

| cell | mean `listed` | mean candidates | `total_defects` | `owners_per_defect` | retention |
|---|---:|---:|---:|---:|---:|
| `(32,16,97)`  | 98,126.0 | 5,423,058 | 1365 | 4368 | 0.018094 |
| `(32,16,193)` | 52,775.3 | 5,685,088 | 1365 | 4368 | 0.009283 |

This is a **clean** control: `total_defects` and `owners_per_defect` are
*identical* across the two fields and the candidate pools differ by only 4.8%,
so the combinatorial enumeration is field-independent and only the arithmetic
retention changes. All six runs completed (`timed_out: false`).

The retention ratio is **1.9492** against a prime ratio of **1.9897** — i.e.
**98.0% of an exact `1/p` law**. That is the mechanistically expected
signature (each additional forced interpolation agreement is a `1`-in-`p`
event), which is why this control transports credibly.

**Field-correcting the N10 second doubling** (two correction factors: the raw
count ratio 1.8593, and the cleaner retention ratio 1.9492):

| schedule | reported ratios | reported exponents | corrected ratios | corrected exponents |
|---|---|---|---|---|
| consecutive | 66.95 → 38.00 | 6.065 → **5.248** | 66.95 → 70.65 – 74.06 | 6.065 → **6.143 – 6.211** |
| powers-of-5 | 86.58 → 38.01 | 6.436 → **5.248** | 86.58 → 70.68 – 74.09 | 6.436 → **6.143 – 6.211** |

**The reported fall in the growth exponent is an artifact of the field
change.** Field-corrected, the consecutive schedule's exponent does not fall —
it is flat-to-slightly-rising (6.065 → 6.143).

**Two consequences.**

1. The sentence "the falling second ratio resists ... the pre-registered
   super-polynomial trend" is **not supported** once the field is controlled.
   The honest statement is that the field-corrected exponent is *flat at
   ≈6.14*, which is evidentially **neutral**, not reassuring. (A flat
   doubling exponent is exactly a polynomial law; a *falling* one would have
   been mild positive evidence, and that is what is being claimed.)

2. The corrected exponent **≈6.14 exceeds 6**. That is the same line
   `n^6` that v4 *proved* insufficient in
   `pma_sigma_one_d4_generic_source_obstruction` (`2^104 > 2^97 = n^6`). So
   the field-corrected numerics and the proved obstruction **point the same
   way**, whereas `attack.md` currently reads the numerics as pointing the
   other way. This is a coherence defect in the current node write-up.

**Caveat, stated plainly.** The 1.8593 suppression factor is measured on the
d4r0 `(d,r)=(4,0)` exact-six object, **not** on the N10 balanced-mixed
floor-band object. Transporting it is a **heuristic**, not a theorem. C-V4-1 is
therefore a *flag plus a re-run request*, not a refutation. The clean fix is
cheap and decisive: **re-run the N10 census at `n=64, k=32, p=97`** (or at
`n=32,k=16` on both `p=97` and `p=193`) to measure the suppression on the N10
object itself. Until then the "did not fire" reading should be softened.

### 6.3 **C-V4-2** — v4's scope-fence language cites a hypothesis canonical struck

A live import hazard, found via R6.

When the campaign proved its σ=1 superpolynomial floor, it had to explain why
that does not falsify `imgfib`. Its rescue was to **retroactively pin a lower
cutoff onto `imgfib`'s statement** (`0b6f5ea7` rewrites `imgfib/statement.md`):

> v4 roadmap `:5354-5356` — "This does not falsify the upstream L1 theorem. The
> local `imgfib` statement is now pinned to its full source hypotheses:
> polynomial generated field, entropy reserve, and `sigma>=C n/log_2 n`."

> v4 `critical/nodes/petal_mixed_amplification/statement.md:315-324` — "This is
> not an `imgfib` falsifier: **sigma one lies outside its lower cutoff**, and
> the collision-free construction is empty once `ell>M`."

**Canonical has since deleted that hypothesis.** Canonical's `imgfib`
statement says the opposite:

> canonical `critical/nodes/imgfib/node.json` (statement) — "the chain does not
> consume the H-scale hypothesis at all: clause (P) works at sigma = 1, so
> `sigma >= Cn/log n` is **DROPPED, not subsumed** — the old 'entropy forces
> sigma = Omega(n)' reasoning was false at the rows and is struck per #155"

So v4's stated reason why σ=1 is harmless (*"outside the lower cutoff"*) refers
to a hypothesis that **no longer exists in canonical**. Importing that sentence
would silently reintroduce a struck hypothesis.

**The conclusion survives, by a different route — verified.** Canonical rescues
`imgfib` via the *entropy reserve*, not the σ cutoff, and wave-8's guard (b)
checked this. I re-verified it numerically. `imgfib`'s reserve requires
`sigma*log2(q_D) >= (1+eps)*log2 C(n,k+sigma)`. At the v4 counterexample row
`(q,n,k,sigma) = (65537^2, 65536, 32768, 1)`:

```
LHS  sigma*log2(q)     =     32.0 bits
RHS  log2 C(n,k+sigma) = 65527.7 bits     -> reserve violated by 2048x
```

The σ=1 families are **2048× outside** the reserve — an enormous margin.
Guard (b) is sound and does not depend on the struck cutoff.

**This is not hypothetical — the language already leaked into canonical at
wave-8.** Two live locations:

> canonical `background/nodes/pma_sigma_one_variable_defect_exact_hit_floor/statement.md:76-80`
> — "## Scope
>
> This does not refute reserve-conditioned `imgfib`. Its asymptotic hypothesis
> **also requires `sigma>=C n/log n`**; sigma one is deliberately outside that
> scope."

> canonical `background/nodes/pma_sigma_one_variable_defect_exact_hit_floor/claim_contract.md:13`
> — "- `imgfib`: proves only a scope guard, not a falsifier **under its lower
> cutoff**;"

Canonical therefore currently contains a PROVED node whose Scope section
justifies non-refutation by appeal to a hypothesis canonical's own `imgfib`
node declares **struck per catch #155**. That is an internal inconsistency,
introduced by the import, not by the campaign.

**The fix is cheap and forced.** The same sentence already opens with the
*correct* route — "reserve-conditioned `imgfib`". Deleting the clause "also
requires `sigma>=C n/log n`" (and the `claim_contract.md:13` "under its lower
cutoff") leaves the argument intact and correct, because the entropy reserve
alone excludes the family by 2048×. No mathematical content is lost.

Distinguish from a false positive: the phrase **"L1 lower cutoff"** appears in
~8 other imported PMA files (e.g.
`pma_b11_first_match_router/statement.md:9`,
`pma_petal_pattern_root_pinning_ledger/statement.md:70`). That is the L1
program's own cutoff parameter, **not** the struck `imgfib` σ-hypothesis.
Only the two locations quoted above need editing.

**Action:** adopt v4's σ=1 floors (already adopted) but **do not import their
scope-fence prose**, and repair the two leaked sites. Any canonical text
explaining why the σ=1 floors are harmless must cite the **entropy reserve**,
never a σ lower cutoff.

### 6.4 Against the N10 census families

Beyond C-V4-1, v4's d4r0 census independently reproduces the catch-#176 cell:
at `(16,8,17)` the six `listed` values are `[36,41,43,39,34,34]` — bracketing
both banked counts `43` (consecutive) and `33` (powers-of-5). Weak
corroboration of the banked mass, on a different field.

---

## 7. Per-package verdicts

| # | package | verdict | evidence |
|---|---|---|---|
| 1 | 32 PMA node theorems + verifiers | **ADOPT (already adopted)** | 32/32 v4 + 33/33 canonical replay PASS under the compute law; exact integer arithmetic; mutation controls in 29/32; byte-identical to canonical |
| 2 | `pma_wide_residual` REFUTED status | **ADOPT (already adopted)** | Both refuting floors replay: `2^104 > 2^97`; `mean_bits=51115 > n3000_bits=48001`. Canonical ahead (preserves master's original statement) |
| 3 | v4 conditional closure of `petal_mixed_amplification` | **REJECT (already rejected)** | The campaign retracted it itself (`conditional.md`: "That premise is false"). Canonical correctly retired it |
| 4 | **C-V4-1** — field-correction of the N10 growth reading | **ADOPT-WITH-EDITS** | Field control at fixed `(32,16)`: 98,126 vs 52,775; retention ratio 1.9492 = 98.0% of an exact `1/p` law, with identical `total_defects`/`owners_per_defect`. Corrected exponents 6.065→6.14–6.21, not 6.065→5.248. Edit = soften `attack.md:14-22` and the census note `:46-48`; queue the `n=64,p=97` re-run |
| 4b | **C-V4-2** — struck σ-cutoff language leaked into canonical | **ADOPT-WITH-EDITS (forced correction)** | `pma_sigma_one_variable_defect_exact_hit_floor/statement.md:76-80` and `claim_contract.md:13` cite `sigma>=C n/log n`, which canonical's `imgfib` declares "DROPPED… struck per #155". The entropy reserve carries the argument alone (verified: 32 bits vs 65,528 bits, 2048× margin). Delete the two clauses; no content lost |
| 4c | 2 PROVED nodes with no executable verifier | **HOLD (note only)** | `pma_aux_list_reduction` and `pma_johnson_regime` carry `statement.md` + `proof.md` but **no `verify.py`**. Defensible — both are classical imports (the Guruswami–Sudan/Johnson bound) rather than computations — but they are the only two PMA PROVED nodes outside the 32-verifier replay net |
| 5 | 4 un-imported `modal_pma_*.py` drivers | **HOLD** | Modal drivers only; the load-bearing per-node `verify.py` files are all in canonical and pass. Import only if the corresponding Modal runs are ever re-executed |
| 6 | v4 upstream provenance ref (`Przemek upstream c35a6da3`) on `pma_aux_list_reduction` / `pma_johnson_regime` | **ADOPT-WITH-EDITS** | Cosmetic provenance gain; canonical's `refs (legacy repo)` form dropped the upstream commit id |
| 7 | Everything else in the campaign (C36 / XR / DLI / rate-half-Hankel, post-07-15) | **OUT OF SCOPE** | Not PMA; belongs to other lanes |

---

## 8. Recommended actions (coordinator decides)

1. **Apply C-V4-1** to `critical/nodes/l1_mixed_petal_amplification/attack.md`
   and to `experiments/prize_resolution/l1_balanced_mixed_growth_census_result.md`:
   state that the second doubling crosses a field change, cite the fixed-`(32,16)`
   control from `pma_d4r0_census_results.json`, and replace "the falling second
   ratio resists" with the field-corrected flat-exponent reading.
2. **Apply C-V4-2** (forced correction): delete "also requires
   `sigma>=C n/log n`" from
   `background/nodes/pma_sigma_one_variable_defect_exact_hit_floor/statement.md:78`
   and "under its lower cutoff" from that node's `claim_contract.md:13`. Leave
   the ~8 "L1 lower cutoff" occurrences elsewhere alone — different object.
3. **Queue** an N10 re-run at `n=64,k=32,p=97` to measure the suppression on
   the N10 object directly. This is the decisive experiment and it is cheap
   relative to the parked `L1-N10-128`.
4. **Close the survey flag.** `attack.md:23-24` ("**Codex v4 PMA:** audit-gate
   its diffuse-allocation results before consuming (survey in flight)") and
   `statement.md:39` ("survey/audit pending") can both be retired: the survey
   is done and the answer is "fully imported at wave-8/9; nothing further to
   consume."
5. Optionally harvest the upstream provenance ref (item 6).

---

## 9. Honest limits of this audit

- I did not independently re-derive any PMA proof; I replayed the verifiers and
  checked their assertion structure and mutation controls.
- `tools/ramguard` was unavailable; ceilings were reproduced with rlimits.
  The RAM ceiling semantics differ (address space vs cgroup RSS) — no run came
  near either bound (all ≤5s, all under `tiny`).
- C-V4-1's suppression factor is cross-object (see §6.2 caveat).
- Per instruction, `notes/pilots_20260807/l1_pma_diag/` was not read, so this
  audit is independent of the concurrent blind pilot.
