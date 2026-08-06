# WAVE-47 AUDIT DRAFT — WCL certificate stream + remainder (non-F2)

- **auditor:** Opus AUDIT agent (wave-47), 2026-08-06
- **worktree audited:** `/home/u2470931/smooth-read-solomin/prize-codex-resolution-v11-20260803`
  branch `codex/full-prize-resolution-v11-20260803`, HEAD `48fc9efcf`
- **range:** `88238fd0..48fc9efcf` (last integrated pin -> Codex HEAD)
- **canonical:** `/home/u2470931/smooth-read-solomin/prize` at `59cb2f627`
  (Round-20 LAUNCH), rulings commit `85c9d1536`
- **scope:** everything EXCEPT the F2 node stream (sibling auditor owns F2)
- **compute law:** every replay below run from the WORKTREE root as
  `tools/ramguard tiny|local -- python3 ...` (literal `--`)

STATUS: IN PROGRESS — sections filled as the audit proceeds.

---

## 1. THE WCL CERTIFICATE STREAM

### 1.1 Commit inventory (in range, WCL-labelled)

Certificate/CADO chain (newest last):

```
b8ba0287e Preregister bounded WCL weight-five hard tails
f019577b9 Route sole WCL weight-five hard tail
54c0bc179 Record sole external WCL weight-five factor request
e2dc5b301 Preregister independent WCL factor vocabulary audit
341e503b8 Record null WCL audit attempt
a8bde7da8 Reprice WCL vocabulary inventory
bafa61fc0 Bank independent WCL factor vocabulary audit
7b95ec740 Preregister independent WCL batch replay pilot
57de5b61b Bank independent WCL batch replay pilot
8a381b2d5 Preregister full independent WCL easy replay
36bbcfb62 Bank full independent WCL easy replay
f88d727ba Preregister independent WCL hard-tail certificate
bf3b97291 Fix WCL tail certificate packet custody
05ba8c9e3 Bank independent WCL hard-tail certificate
25a23a401 Preregister bounded CADO run for WCL tail 191
6ffb48334 Fix CADO tail workdir invocation
e9e463d03 Fix WCL tail CADO CPU portability
75cd3a630 Fix official CADO runtime dependencies
010125a5c Bank final WCL tail factorization
db36b047e Certify final WCL hard-tail factors
e7ec67fa0 Prove WCL slot 1,5 emptiness
37f94d019 Preregister WCL 1,6 unit-lift pilot
3d2fd0588 Fence expanded WCL 1,6 certificate route
```

Artifacts live in `notes/pilots_20260806/wcl15_finish/` (30 files) and
`notes/pilots_20260806/wcl16_delta6/` (4 files), plus in-repo primary packets
under `experiments/prize_resolution/`.

### 1.2 REPLAY A — tail-191 factor certificate: **PASS 20/20**

Artifact: `notes/pilots_20260806/wcl15_finish/tail191_factor_cert.json`
Prereg: `notes/pilots_20260806/wcl15_finish/TAIL191_FACTOR_CERT_PREREG.md`

This is the *only* result in the wave that rests on heavy external compute
(CADO-NFS general number field sieve, 16 CPU / 80s, app
`ap-gyFwY6AxmBrU0NioPlsJ5C`).  I did **not** replay the sieve.  I did not need
to: a factorization is a self-certifying object, and the certificate carries
its own factors verbatim.  I re-derived every claim from scratch with my own
arithmetic and my own primality test (16 fixed Miller-Rabin bases + strong
Lucas = BPSW), trusting neither CADO nor Codex's FLINT checker:

```
[PASS] C1  norm string in cert == norm in preregs/EXTERNAL_REQUEST
[PASS] C2  norm_bits 269 == recomputed bit length
[PASS] C3  product of the two claimed factors == the norm (exact)
[PASS] C5.0/C5.1 both factors prime (independent BPSW)
[PASS] C6.*  bit lengths 112, 158 as claimed
[PASS] C7.*  v_2(p-1) = 9, 12 as claimed
[PASS] C9.*  official gate (p<2^256 AND v_2(p-1)>=41) FALSE for both
[PASS] C13 in-repo CADO packet SHA-256 == cert.source_sha256
           c093d5e05aea1e2b2851042e550f89cf44f093c8b1714c80780efd27b72ec608
[PASS] C14 both factors appear verbatim in the CADO source packet
```

The split, for the record (`tail191_factor_cert.json:9,16`):

```
648504938724625892617537595827566622528651020454874372151735040370465231483079169
  = 2618025003265620701077592958097921
  * 247707694890502006805474333259382717013127180289
```

**Verdict: the CADO dependency is NOT a trust dependency.**  Heavy compute was
used only to *find* the split; the split is verified locally in milliseconds.
This is exactly the right shape for an unreplayable-compute result.

### 1.3 REPLAY B — 193-tail independent certificate: **PASS 17/17**

Artifact: `notes/pilots_20260806/wcl15_finish/tail_independent_cert.json`
Primary packet (IN REPO, 195 KB):
`experiments/prize_resolution/dli_wcl_weight5_recursive_norm_tail_factor_only_result.json`

I did not run Codex's checker (`tail_independent_cert_modal.py`, needs Modal +
python-flint).  I re-implemented every check from scratch against the in-repo
packet:

```
[PASS] T1  in-repo packet SHA-256 == cert.source_sha256 (026fbd0d...ac0f4b)
[PASS] T5  recomputed manifest digest == aa7fa74e...bf1ab8
[PASS] T7  factor_results has exactly 194 entries
[PASS] T8  193 tails COMPLETE; exact product check + 400 independent BPSW
           primality proofs, ZERO composites
[PASS] T9  sole residual is tail 191, status PARTIAL, FACTOR_TIMEOUT_300S
[PASS] T11 recomputed distinct primes == 399
[PASS] T12 recomputed prime digest == 4180c683...00cbb
[PASS] T13 recomputed max v_2(p-1) == 17
[PASS] T14 NO official-gate prime among the 399
[PASS] T17 certificate_digest reproduces from the certificate body
```

Codex's checker (`tail_independent_cert_modal.py:47-215`) is **fail-closed**:
every custody deviation raises `AssertionError` rather than degrading to a
partial.  I read it line by line; there is no branch that can emit
`status: COMPLETE_193_PENDING_191` on a mismatch.

**Verdict: ADOPT.**  This package is proof-grade and locally auditable.

### 1.4 REPLAY C — the node verifier: **PASS, 5/5 tamper controls**

```
tools/ramguard local -- python3 critical/nodes/dli_wcl_slot_1_5_emptiness/verify.py
  -> WCL15_CERTIFICATE_PASS rows=2296920 easy=2296726 tails=194 max_v2=30 tamper_rejected=0
tools/ramguard local -- python3 critical/nodes/dli_wcl_slot_1_5_emptiness/verify.py --tamper-selftest
  -> WCL15_CERTIFICATE_PASS ... tamper_rejected=5
```

CATCH W-1 (minor, presentational).  The tamper self-test is **opt-in**.  The
bare invocation prints `tamper_rejected=0`, which reads like "zero hostile
mutations were rejected" when it actually means "no mutation was attempted".
`proof.md:131-132` correctly documents the `--tamper-selftest` form, so the
node is fine; but any harness that calls `verify.py` without the flag banks a
weaker check than the proof advertises.  Recommend making the self-test the
default (or renaming the field `tamper_selftest=skipped`).

I confirmed all four pinned packet SHA-256s match on disk, and that the five
hostile mutations (row count, missing batch, empty residual list, depth 41,
injected gate factor) are each rejected.

### 1.5 CATCH W-2 (**the significant one**): the class count 2,296,920 was the wave's only unverified trust root — and it is CORRECT

`proof.md:24-40` derives completeness of the census from a "finite completeness
router": the weight-4 normalized section supplies every reduced 4-set, each
5-set is reached by a legal extension, then canonical keys de-duplicate.  The
output is asserted as

> `2,296,920 affine-Galois classes, representative SHA-256
> 9ac0ca650e704a13514180fe2d8bcea94943c771f125b3942888a6aba8c87f00.`
> — `critical/nodes/dli_wcl_slot_1_5_emptiness/proof.md:32-36`

**No replay in the wave re-derives that number.**  The full easy replay
(`full_batch_replay_modal.py:207-231`) *reads* the representative file and
only checks its pinned hash; the representative file itself lives on the Modal
volume and is not in the repo.  So the entire PROVED status rested on a paper
surjectivity argument plus an unreproduced enumeration.

I closed that gap independently.  The object is exactly: 5-subsets of `Z/512`
pairwise distinct mod 256 (the encoding is confirmed at
`full_batch_replay_modal.py:218-223`, and the reducedness test is the
`antipodal collision` assertion at line 219), modulo
`G = {x -> ax+b : a odd mod 512, b in Z/512}`, `|G| = 131072`
(`proof.md:17-19`).  Burnside's lemma, computed from scratch with no reference
to Codex's generator:

```
|G| = 131072
Fix(identity)  = 281905569792   (= C(256,5)*2^5, cross-checked)
sum_g |Fix(g)| = 301061898240
remainder      = 0
INDEPENDENT ORBIT COUNT = 2296920
CODEX CLAIMED COUNT     = 2296920      -> MATCH
```

This is a strong corroboration in **both** directions at once: had the
extension argument missed orbits the census would be short of 2,296,920; had
de-duplication been imperfect it would exceed it.  Hitting the true orbit
count exactly means the census is both complete and irredundant, *provided*
its 2,296,920 keys are pairwise inequivalent — which is now the only residual
of the completeness router, and is a cheap sort/canonicalize check rather than
a paper argument.

I also re-derived the mathematical reduction in `proof.md:42-66` and find it
sound: `X^256+1 = Phi_512`; `2^41 | q-1` gives an order-512 root in `F_q`; a
shared root forces `q | Res(Phi_512, P)`; the affine action sends
`P -> X^b P(X^a)` with `a` odd, which permutes the primitive 512th roots and
so preserves the absolute norm.  The nonvanishing argument (a vanishing sum of
2-power roots of unity decomposes into antipodal pairs, so an odd-size reduced
set cannot vanish) is correct.

### 1.6 What still rests on unreplayed heavy compute

Honest accounting of the trust surface:

| claim | in-repo data? | independently replayed here? |
|---|---|---|
| tail-191 split (CADO-NFS, 16 CPU) | yes, factors verbatim | YES — full, from scratch |
| 193 hard tails (194-row manifest) | yes, 195 KB packet | YES — full, from scratch |
| class count 2,296,920 | no (Modal volume) | YES — independently, by Burnside |
| easy census: 2,296,726 rows, 6,177,403 primality checks, 6,528,119 factor records, max `v_2(p-1)=30` | **NO** — summaries + digests only | **NO** |

The easy stage is the one genuinely unreplayable item.  Its replay
(`full_batch_replay_modal.py`) is nevertheless well-built: it recomputes each
norm by a **different algorithm** than the primary run (direct FLINT
`resultant` against `X^256+1`, line 224, versus the primary's recursive
`f(X)=f_0(X^2)+X f_1(X^2)` identity), re-proves every shard prime with
`fmpz_is_prime` (line 202), re-divides each norm to remainder 1 (lines
249-262), and reconstructs the primary's candidate and factor digests (lines
230, 270).  Every deviation raises `AssertionError`.  It is fail-closed and
methodologically independent — but 17,865 worker-seconds of it are attested
only by a 53 KB summary.

**This is not a defect to fix; it is a residual to state.**  Recommend the
node's statement or proof carry one sentence naming the easy stage as
volume-resident.

### 1.7 wcl16_delta6 — the (1,6) route fence

`notes/pilots_20260806/wcl16_delta6/` (PREREG, REPORT, pricing script and
result) prices the expanded `(1,6)` slot.  Commit message is "Fence expanded
WCL 1,6 certificate route".  Reviewed as a **pricing/fencing** artifact only —
it claims no status change.  See section 4 for the DAG-effect confirmation.

---

## 2. CRITICAL NODE EDITS OUTSIDE F2 — CLOBBER ANALYSIS

Three nodes in scope: `rate_half_list_adjacent_crossing`,
`rate_half_band_closure`, `l1_mixed_petal_amplification`.

### 2.1 What Codex actually did

Commit `11d100f4c` "Decompose oversized critical node documents" (**not in
canonical**) introduced a *new* sectioned-document mechanism for critical node
documents: a long `statement.md` / `attack.md` becomes a ~35-line index stub
plus a `statement_sections/` or `attack_sections/` directory holding the
original text split into packets, with a `document.json` manifest pinning the
pre-refactor byte stream.  Four documents were decomposed into 36 packets:

```
critical/nodes/l1_mixed_petal_amplification/attack.md          (940 lines)
critical/nodes/l1_mixed_petal_amplification/statement.md      (1356 lines)
critical/nodes/rate_half_band_closure/attack.md               (3950 lines)
critical/nodes/rate_half_list_adjacent_crossing/statement.md  (4059 lines)
```

Replay of the lossless-decomposition verifier:

```
tools/ramguard local -- python3 tools/refactor_critical_node_documents.py
  -> {"documents": 4, "packets": 36, "status": "PASS"}
tools/ramguard local -- python3 tools/verify_sectioned_critical_node_documents.py
  -> {"documents": 4, "packets": 36, "status": "PASS"}
```

`node.json` for all three nodes is **unchanged except for added `refs`**
entries pointing at the new `document.json` files.  **No status changed, no
edge changed.**  Verified by direct diff against canonical.

### 2.2 CATCH W-3 (**the clobber**): canonical's mint-4 addendum was paraphrased, not preserved

I checked both diff directions, per the wave-45 lesson.  Three of the four
decompositions start from **exactly canonical's current bytes**:

```
l1_mixed_petal_amplification/attack.md    pinned 6b128721... == canonical 6b128721...  (940 lines)
l1_mixed_petal_amplification/statement.md pinned b584bf55... == canonical b584bf55... (1356 lines)
rate_half_band_closure/attack.md          pinned 26f1d1c5... == canonical 26f1d1c5... (3950 lines)
```

The fourth **diverges**:

```
rate_half_list_adjacent_crossing/statement.md
  pinned pre-refactor : ce6bc78cb6f9135a596c9e0caa5fadf923f77447430b834e0b33911e65d23cf1 (4059 lines)
  canonical current   : c017b7120241ed0af1471e13462e1b1ef0e6423705095ebb3c0e684d262e02b7 (4075 lines)
```

The 16-line delta is canonical's MINT-4 addendum, added by canonical commit
`207d49732` — which memory records as carrying **user-delegated coordinator
rulings**.  Canonical text, verbatim
(`critical/nodes/rate_half_list_adjacent_crossing/statement.md:4060-4075`):

```
## Addendum (2026-08-06, mint-4, round 18 — DSA scope note)

THEOREM DSA (background/nodes/crossing_dsa_refutation, witness
verified at n = 2^41) proves non-structural window members EXIST at
admissible tower rows (p^{delta_a} < 2^{L-2}; 10 of 19 admissible
pairs at w = 2^34). Consequence for THIS node: the (ES)-route to
the count bound is DEAD at those rows; the gamma-shell population
of the accidents (hence this node's budget question there) is
RE-OPENED, not decided. At e = 1 prime rows DSA provably cannot
apply (B* >= 3 forces log2 p >= 129.585 > 126) and the heuristic
ternary re-pricing gives a 53-61 bit margin. Whether tower rows are
in the official family is a MAINTAINER question that decides the
scope of this obligation. Unconditional positive coverage at
w > 2^37.3131 (256-bit p) via THEOREM CS
(es_ternary_suppression_instruments).
```

Sequence of events: `11d100f4c` (the refactor) is **not** a descendant of
`207d49732` — I verified `git merge-base --is-ancestor 207d49732 11d100f4c`
returns false.  Codex refactored first; canonical's addendum then arrived via
merge `a5e3b98df`; and Codex resolved that merge by **rewriting** the
addendum into a new separate file
`critical/nodes/rate_half_list_adjacent_crossing/statement_addenda/12-round18-dsa-scope.md`.

The rewrite is **semantically faithful** — I checked claim by claim: THEOREM
DSA, the `p^delta_a < 2^(L-2)` condition, 10-of-19 at `w=2^34`, the (ES) route
dead, gamma-shell re-opened, `e=1` prime rows excluded because `B*>=3` forces
`log2 p >= 129.585 > 126`, the 53-61 bit heuristic margin, the maintainer
scope question, and CS coverage at `w > 2^37.3131` are all present.  But the
wording is Codex's, not canonical's: normalized-text similarity is **0.37**,
and neither text contains the other.

**This is a text clobber, not a content clobber.**  Adopting Codex's tree
as-is would replace a ratified coordinator-ruling wording with a paraphrase,
and would move it out of `statement.md` into a separate addenda file.

**Adoptable without loss:** take the decomposition (it is verified lossless),
but restore canonical's 16 lines **verbatim** as
`statement_addenda/12-round18-dsa-scope.md`, replacing Codex's paraphrase, and
re-pin `document.json`'s `pre_refactor_sha256` to canonical's
`c017b712...` / 4075 lines.  Nothing else in the package needs editing.

### 2.3 CATCH W-4: two competing sectioned-document mechanisms now exist

Canonical already ships `tools/sectioned_document.py` with schema
`sectioned-document-v1` (plus `compile_sectioned_documents.py`,
`migrate_sectioned_documents.py`, `verify_sectioned_documents.py`).  Codex
added a **parallel** mechanism — `tools/refactor_critical_node_documents.py`
and `tools/verify_sectioned_critical_node_documents.py` — with a *different*
schema, `sectioned-critical-node-document-v1`
(`tools/refactor_critical_node_documents.py:321`).  Canonical currently has no
`*_sections` directory under `critical/nodes/` at all.

This is a genuine design choice, not a forced correction: adopting it commits
the project to two sectioning schemas.  **Surface to the coordinator rather
than auto-apply.**  Note the memory rule "node.json shards = DAG source;
dag.json/roadmap/compute-requests compiled, never hand-edited" — the new
mechanism makes `statement.md` a *compiled index* for these four documents,
which is a write-path change for critical node documents specifically.

### 2.4 CATCH W-5 (**pre-existing canonical red**): `rate_half_list_adjacent_crossing/verify.py` FAILS in BOTH trees

This is not caused by Codex, but the audit found it and it should not be lost.

```
WORKTREE : status FAIL, exit 1, 223/224 checks pass, failing = brackets_are_evidence
CANONICAL: status FAIL, exit 1,          failing = brackets_are_evidence
```

(Canonical's was run read-only, in place, with no writes.)

Cause: `verify.py` asserts the node's incoming evidence-edge list **by exact
enumeration**, and both trees' graphs have grown past their verifier.
Reconstructing incoming edges from the `node.json` shards (the DAG source of
record):

```
CANONICAL  actual incoming 118, verify.py expects 111 -> 7 unexpected:
   es_ternary_suppression_instruments
   l1_m31_rank7_dense_top_decorated_shift_pair_router
   l1_m31_rank7_zero_excess_two_block_incidence_router
   rate_half_list_budget_three_common_mismatch_zero
   rate_half_list_chamber_affine_rank_bridge
   rate_half_list_cyclic_budget_staircase
   rate_half_m31_adjacent_quotient_rotation_product_spectrum

WORKTREE   actual incoming 119, verify.py expects 117 -> 2 unexpected:
   es_ternary_suppression_instruments
   rate_half_crossing_ideal_galois_multiplicity_exclusion
```

So **Codex's version is strictly better**: it repairs six of canonical's seven
stale expectations (those six suppliers exist in both trees and are
pre-existing — none is new in this wave).  It still misses two:
`es_ternary_suppression_instruments`, which reached Codex only via the merge of
canonical's MINT-4 and was never wired into the consumer's verifier; and
`rate_half_crossing_ideal_galois_multiplicity_exclusion`, Codex's own new node
(section 2.5) whose evidence edge was added without updating the consumer.

**Adoptable with a forced correction:** take Codex's verify.py, then add the
two remaining constants so the node goes green.  That is a mechanical
completion of an enumeration, not a mathematical choice.  Recommend the
coordinator also ask why a *node-count-sensitive* enumeration is asserted by
hand — this check will keep going red on every supplier mint.

### 2.5 New background supplier: `rate_half_crossing_ideal_galois_multiplicity_exclusion`

New in this range (commit `99a55c51b`), absent from canonical, `status:
PROVED`, `closure: proof`.  Both its verifiers replay clean:

```
tools/ramguard local -- python3 background/nodes/.../verify.py
  -> ..._PASS norm_checks=816 divisibility_checks=1104 first_excluded=170752922588 dag=2/2   (exit 0)
tools/ramguard local -- python3 background/nodes/.../verify_audit.py
  -> AUDIT_..._PASS boundary=2/2 tower=65/65 failed_run_preserved=1 tamper=1                 (exit 0)
```

CATCH W-6 (minor, mechanical).  Its two `evidence_for` entries carry **no
`order` field**, unlike every other edge I inspected in this wave:

```json
"evidence_for": [
  { "to": "rate_half_list_adjacent_crossing" },
  { "to": "u2c_giant_tnull_dichotomy" }
]
```

Worth confirming against the compile step before adoption.  Note its second
edge lands on `u2c_giant_tnull_dichotomy`, which is the sibling auditor's F2/u2c
lane — flagging the cross-lane edge, not adjudicating it.

### 2.6 The weight-4 supplier was PROMOTED background -> critical

Commit `e7ec67fa0` **moved** `dli_wcl_weight4_ambient_exclusion` from
`background/nodes/` to `critical/nodes/`.  Canonical still has it under
`background/`; the worktree no longer has a background copy.  The node's
content is byte-identical apart from its six self-referential `refs` paths
being rewritten `background/... -> critical/...`; status was **already**
`PROVED` before the move.

This is a graph-shape decision (it changes the critical/background census
split, and makes the node a `requires` supplier of the newly-PROVED
`dli_wcl_slot_1_5_emptiness` at `order 5018`).  **Surface, do not auto-apply.**
It is mathematically inert but it re-prices the board's node counts.

---

## 3. ROADMAP / COMPUTE-REQUEST / work_cycles CHANGES

### 3.1 Write path — Codex respected it

`notes/PRIZE_RESOLUTION_ROADMAP.md` and `notes/PRIZE_COMPUTE_REQUESTS.md` are
**compiled**, not authored: `tools/compile_sectioned_documents.py:19-21` names
exactly two manifests, `notes/roadmap/document.json` (17 sections) and
`notes/compute_requests/document.json` (10 sections).  Sources are the shards
under `notes/roadmap/sections/` and `notes/work_cycles/roadmap_r3/`.  I ran
the check in the worktree:

```
tools/ramguard local -- python3 tools/compile_sectioned_documents.py --check
  SECTIONED_DOCUMENT_PASS notes/PRIZE_RESOLUTION_ROADMAP.md sections=17 bytes=949062
  SECTIONED_DOCUMENT_PASS notes/PRIZE_COMPUTE_REQUESTS.md   sections=10 bytes=618032
```

Compiled twins are in sync with the shards.  **Review the shards, not the
top-level files.**  Note there is no generation banner in either compiled
file — worth adding, since nothing on the page warns an editor off.

### 3.2 What was added

One new roadmap shard, `notes/work_cycles/roadmap_r3/15-prize-resolution-20260806.md`
(607 lines at the pin, 14 `###` subsections), absent from canonical.  In my
lane the load-bearing ones are the `(1,5)` squared-root router fence, the
complete easy census, and the `(1,6)` expanded-certificate fence.

Compute requests, all hanging off existing CR-004 (no new top-level CR number):
- `notes/compute_requests/sections/04-cr004-wcl.md:4` — the 2026-08-06
  finish-inventory authorization, ~155 lines chaining ~15 Modal apps with app
  ids, SHA-256s and cost ceilings inline.
- `...:98` — `CR-004-W15-TAIL191-NFS`, the external factoring request, opened
  and retired in the same bullet (consistent with `EXTERNAL_REQUEST.md:3`
  "**Status: RETIRED 2026-08-06.**").
- `...:558` — `CR-004-W16-DELTA`, expanded rational certificate pricing;
  declines a 185,569,028-class census priced at ~36,000 CPU-hours / ~$6.6k.
- `notes/compute_requests/sections/09-k3-and-positive-433.md:1163` — the XR
  fiber-rigidity boundary fixture.

### 3.3 Board repricing (verified directly from dag.json)

```
worktree AT PIN 48fc9efcf : nodes=1838 edges=5115
   PROVED 1622  REFUTED 31  CONDITIONAL 60  TARGET 77  CONJECTURE 15  WALL 7  PROVABLE 26
canonical      f4143ab2f  : nodes=1824 edges=5084
   PROVED 1610  REFUTED 28  CONDITIONAL 61  TARGET 77  CONJECTURE 15  WALL 7  PROVABLE 26
```

Three status conflicts between the trees:

```
dli_wcl_slot_1_5_emptiness : canonical TARGET      -> worktree PROVED   [MY LANE]
f2_admissible_object       : canonical PROVED      -> worktree REFUTED  [sibling]
f2_conditional_close       : canonical CONDITIONAL -> worktree TARGET   [sibling]
```

Only the first is mine.  The roadmap states the repricing explicitly
(`notes/work_cycles/roadmap_r3/15-prize-resolution-20260806.md:131,135-137`):

```
is now PROVED. The WCL zone residual drops from ten slots to nine.
...
node: dli_wcl_slot_1_5_emptiness [PROVED]
result: complete 2,296,920-class norm census and all 194 tails certified
DAG status delta: one TARGET promoted to PROVED; WCL-zone residual 10 -> 9
```

The `TARGET` count does not move (77 in both), because the slot was a TARGET
that became PROVED while other targets were minted.  The zone-coverage node's
own text was updated consistently in three places
(`dli_wcl_zone_coverage/statement.md`, `conditional.md`,
`official_terminal_attack.md`), each naming the residual nine cells.  That is
correct node-local bookkeeping per the node-local-notes rule.

### 3.4 CATCH W-7: Codex's work predates the SCOPE AND READING RULINGS, and one addendum is now stale

Codex's branch at the pin descends from canonical only up to `fed71a06b`.  It
had **not** seen `a37290e55`, `23083a6ea`, `85c9d1536` (THE SCOPE AND READING
RULINGS) or `59cb2f627`.  (Post-pin, Codex's live HEAD `a16df47ef` has since
merged canonical, but that is wave-48 territory.)

For the WCL stream this is harmless — the rulings are about the F2/(ES)/gamma-shell
lane and do not touch the `(1,5)` census.  **But it bites the addendum in
section 2.2.**  Canonical's own verbatim text, and Codex's paraphrase of it,
both say:

> "Whether tower rows are in the official family is a MAINTAINER question that
> decides the scope of this obligation."

Canonical commit `85c9d1536` has since **answered** that question:

> "**Non-generating and tower rows ARE in the challenge family.**"
> — `85c9d1536`, coordinator ruling, spec-derived

So when the coordinator restores canonical's 16 lines verbatim (section 2.2),
they should be aware the restored text is itself stale: the DSA consequence
for this node — "(ES)-route DEAD at those rows; the gamma-shell population
RE-OPENED" — is now **unconditionally live**, not contingent on a maintainer
answer.  That sharpens `rate_half_list_adjacent_crossing`'s obligation rather
than softening it.  Recommend a follow-on addendum applying the ruling, which
is a coordinator call, not a forced correction.

---

## 4. CODEX'S NEW PILOT DIRECTORIES (notes/pilots_2026080x/)

Worktree-only dirs (canonical does not have them): `pilots_20260804/fiber_rigidity`
and `pilots_20260806/{cs_transport, wcl15_finish, wcl16_delta6, f2_minus_branch,
f2_newton_distance, f2_route_repair, f2_weighted_prefix_l2}`.  The four `f2_*`
are the sibling auditor's; named only.

Canonical also has four pilot dirs the worktree lacks (`crossing_gap`,
`f2_repose`, `gamma_shell`, `tail_count`) — Codex is simply behind canonical
there; no conflict.

**Status-change claims, checked:**

- `pilots_20260804/fiber_rigidity` — exact `q=193,n=64,k=4,d=13,h=18` fixture,
  all 635,376 anchors x 194 slopes, plus a constructor-free checker rejecting
  12 hostile mutations.  Claims **no** status change, explicitly:
  `REPORT.md:7` "- **DAG effect:** none"; `REPORT.md:97-99` "This packet is a
  **route fence**, not a critical-node falsification.  Keep
  `xr_band_forced_commonroot_syzygy_count` at its current status."  Clean and
  correctly self-scoped (preregistered at `PREREG.md:118-123`).
- `pilots_20260806/cs_transport` — **does** mint a status: the PROVED node
  `rate_half_crossing_ideal_galois_multiplicity_exclusion` (section 2.5).  The
  prereg gates it correctly (`AUDIT_PREREG.md:63` "no consumer target changes
  status merely from this supplier"), and no consumer flipped.  I replayed
  both of its verifiers: PASS, exit 0.  This packet also preserves three
  failed launches and a self-caught off-by-one before rerun — good discipline.
- `pilots_20260806/wcl16_delta6` — `REPORT.md:6`
  "- **mathematical status:** no change; `(1,6)` remains `TARGET`".
- `pilots_20260806/wcl15_finish` — **every** sub-packet disclaims promotion,
  e.g. `TAIL_CERT_PREREG.md:64` "No node promotion occurs until tail 191 is
  completely factored and independently certified";
  `TAIL191_FACTOR_CERT_PREREG.md:33` "this certificate alone does not change
  DAG status"; `INVENTORY_REPORT.md:5` "- **DAG effect:** none".  The
  promotion is asserted only at the node/roadmap layer (`e7ec67fa0`), which is
  the right place.  Pilot hygiene here is exemplary.

---

## 5. VERDICTS

| # | package | verdict |
|---|---|---|
| 1 | WCL tail-191 CADO factorization + FLINT certificate | **ADOPT** — replayed 20/20 from scratch |
| 2 | WCL 193-hard-tail independent certificate | **ADOPT** — replayed 17/17 from scratch |
| 3 | WCL easy census + full batch replay + vocabulary audit | **ADOPT-WITH-EDITS** — method sound and fail-closed, but volume-resident; state the residual in the node |
| 4 | `dli_wcl_slot_1_5_emptiness` TARGET -> PROVED | **ADOPT-WITH-EDITS** — proof sound, class count independently confirmed; make the tamper self-test default; name the volume-resident easy stage |
| 5 | `dli_wcl_zone_coverage` 10 -> 9 residual bookkeeping | **ADOPT** — consistent across all three node documents |
| 6 | `dli_wcl_weight4_ambient_exclusion` background -> critical | **HOLD** — mathematically inert, but a graph-shape/census decision for the coordinator |
| 7 | wcl16_delta6 `(1,6)` route fence | **ADOPT** — pricing only, no status claim |
| 8 | Critical-node document decomposition (4 docs, 36 packets) | **ADOPT-WITH-EDITS** — lossless for 3 of 4; restore canonical's addendum verbatim on the 4th |
| 9 | New sectioning schema `sectioned-critical-node-document-v1` | **HOLD** — commits the project to a second sectioning mechanism |
| 10 | `rate_half_list_adjacent_crossing/verify.py` update | **ADOPT-WITH-EDITS** — strictly better than canonical's, but still red; add the two missing constants |
| 11 | `rate_half_crossing_ideal_galois_multiplicity_exclusion` (new PROVED background node) | **ADOPT** — both verifiers replay clean; confirm the missing `order` fields |
| 12 | Roadmap shard 15 + CR-004 additions | **ADOPT** — compiled twins verified in sync |
| 13 | `pilots_20260804/fiber_rigidity` | **ADOPT** — correctly self-scoped, no status claim |

## 6. CATCHES

- **W-1** tamper self-test is opt-in; bare `verify.py` prints `tamper_rejected=0`, which reads as a passed control but is a skipped one.
- **W-2** the class count 2,296,920 was the wave's only unverified trust root — **independently confirmed correct** by Burnside (orbit count exact, remainder 0).
- **W-3** canonical's mint-4 DSA addendum (ratified coordinator wording) was **paraphrased**, not preserved — similarity 0.37, neither text contains the other. Content faithful; wording clobbered.
- **W-4** two competing sectioned-document schemas now exist.
- **W-5** `rate_half_list_adjacent_crossing/verify.py` **FAILS in BOTH trees** (exit 1, `brackets_are_evidence`) — a pre-existing canonical red, not caused by Codex; Codex's version fixes 6 of the 7 stale entries.
- **W-6** the new node's `evidence_for` edges carry no `order` field.
- **W-7** Codex's work predates `85c9d1536`; the restored addendum's "MAINTAINER question" has since been ruled, making it stale on arrival.

## 7. HONEST RESIDUALS

1. The easy census (2,296,726 rows, 6,177,403 primality checks, 17,865 worker-seconds) is **not** reproducible from this repo. It is attested by a 53 KB summary plus digests.
2. The census's **pairwise-inequivalence** is the only surviving piece of the completeness router that my Burnside count does not settle. It is now a cheap sort/canonicalize check rather than a paper argument — worth doing.
3. I did not run the CADO factorization, the Modal replays, or any remote job. Every replay above is local, under `tools/ramguard`, from the worktree root.
4. F2 nodes and the `f2_admissible_object` PROVED -> REFUTED conflict are out of scope here — the sibling auditor owns them.

