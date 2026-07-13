# M4A — packet audit of the dli M4 assembly-verifier packet: incremental findings log

Auditor: fresh-context PACKET AUDITOR (M4A), 2026-07-13. Repo READ-ONLY
throughout (verified byte-identical to baseline at close; one stray
`__pycache__` .pyc created by my own importlib load was removed — see N-3).
Packet under audit: `critical/nodes/dli_prime_weighted_large_block_support/notes/`
{m4_assembly_verifier.py, m4_run_out.txt, m4_report.md,
m4_amber_statement_draft.md, m4_findings.md, m4_test_162_paths.py}.
Catch ledger entering: #164. Issued here: **#165, #166, #167** (see below
and m4a_report.md).

All scratch under this scratchpad, `m4a_` prefix:
- `m4a_arith.py` — exact re-derivations (assembly arithmetic, #162 span,
  #164, refuters, M4-F1 slack claims).
- `m4a_tamper_driver.py` — shadow-repo harness: baseline + 5 gate tampers
  + 2 fresh mutations + 5 #163 attacks + M5 flip tests + independent
  third-pass battery truth. 15/15 OK.
- `m4a_baseline_hashes_node.txt` / `m4a_final_hashes3.txt` — byte-untouched
  proof (diff clean, 95 files incl. dag.json and the x4 packet).
- `m4a_replay_out.txt` — fresh verifier run transcript.

## Run log (incremental)

1. **Read-in.** All six packet files read in full; reference docs read:
   C2PP_POSED_20260710.md, C1PRIME_LEVEL_SCALED_POSE.md,
   M3_ENDPOINT_EXCEPTION_COVERAGE.md, M1/M2 result audits, eex_report.md
   (secs 4-5), REPOSE_B_WEAK.md addendum (#40), x4 REDUCTION_PACKET.md
   line 39, eex_verify.py (item-5 code), tools/verify_prize_dag.py
   (leaf-conditional + red-leaf laws, lines 78-101).
2. **Arithmetic re-derived exactly** (`m4a_arith.py`, ramguard tiny):
   - per-level factor 1 + 4(1 + 2^-5) = 41/8 exactly;
   - (41/8)^34 <= 2^100 exact (integer form 41^34 <= 2^202 True);
     log2(41/8) = 2.357552004..., 34x = **80.156768...** bits -> the
     mission's "34 x 2.3576 = 80.16" and the packet's "80.1568 of 100,
     slack 19.8432" both CONFIRMED; minimal whole-bit budget is 2^81
     (19 whole bits spare);
   - reserve composition 2^21 * (41/8)^34 <= 2^121 exact (integer form
     2^21 * 41^34 <= 2^223 True); 21 + 100 = 121;
   - M4-F1 claims replayed: tau* = (2^{50/17}-5)/4 = 0.67009...;
     tau = 1/4 -> 87.889 bits (slack 12.11); tau = 1/2 -> 95.450 bits
     (slack 4.55) — the findings' 12.1 / 4.5 figures CONFIRMED;
   - refuter exactness: 2.752^33 (48.20 bits) and 2.874^33 (50.26 bits)
     both > 2^21; boundary sanity 1.5544^33 < 2^21 — the G2 comparison is
     genuinely discriminating, not vacuous.
3. **#164 recomputed** (mission item 7): 2^(21/33) = **1.554406281770...**
   -> 3 dp display **1.554**; the banked "1.555" is wrong in the last
   digit at exactly the two sites the packet names (pose clause (ii),
   dag statement #108 pin sentence). 2^(22/34) = 1.565972 -> "1.566"
   supports the packet's carry-over provenance hypothesis. Packet's #164
   text CONFIRMED as stated, display-only.
4. **#162 verified against live dag.json** (mission item 5): statement len
   8950; frag = stmt[6673:7286], 613 chars; starts/ends exactly per spec
   (incl. trailing space); sha256[:16] = d60593436da96d99 MATCH; frag ==
   stmt[5461:6074] verbatim (the torn duplicate); '==gridDP PASS' at
   offsets {5461, 6673} only; pre-counts 2/2/2 (MITM x1) -> post-deletion
   1/1/1 (MITM x1); original block retained; JSON round-trip valid; seam
   reads "...full text in the node folder): M2 ROUND SURVIVED: ..." —
   sense preserved. The three-state detector test (m4_test_162_paths.py)
   replayed from a scratch copy: ALL OK (duplicate-detected / clean-passes
   / malformed-M4Reject).
5. **Verifier replayed** (ramguard tiny, exit 0, ~10 s): output
   byte-identical to banked m4_run_out.txt except the builder-appended
   final `exit_code=0` line. 22 provenance pins counted and cross-read
   against their source files (all substring targets exist where claimed).
6. **Gate non-vacuousness proved by tamper** (mission item 2;
   `m4a_tamper_driver.py`, shadow copy of exactly the 19 files the
   verifier reads, verifier re-pointed at the shadow; live repo untouched):
   - T1 f2b: ratio at (2,97) +1e-9 -> G1 bit-exact + cross-file checks
     FAIL, exit 1;
   - T2 calibration: stripped refuter at (2,8353) 2.7515->1.5 -> G2
     display + exact-exceedance checks FAIL, exit 1;
   - T3 M2 replay: E_minus_1 numerator +1 at (1,193) -> G3 12-row exact
     replay FAILS, exit 1;
   - T4 (bonus): m1 Fa_fired->true -> G4 FAILS;
   - T5 (bonus): banked A1-PROD table w_1(20) None->60 -> zone-agreement
     pin FAILS.
   Banked originals byte-untouched (hash diff clean before and after).
7. **9 mutation controls audited by code-path read** (mission item 3):
   each trips for the RIGHT reason — MUT-1 via the manifest==posed-21 pin
   AND the A6 identity (note: A5 alone would NOT catch 22 since
   2^22*2^80.16 < 2^121 — A6 is the load-bearing check, correctly
   conjoined); MUT-2 via the A3/A4 exact aggregate; MUT-2b via the
   zone-table pin; MUT-3 via fail-closed item-missing REJECT; MUT-4a is a
   semantics invariant (verdict == exact CONDITIONAL string); MUT-4b via
   M4Reject no-silent-upgrade; MUT-5 via M4InputReject schema; MUT-6 via
   the /33 pin; MUT-7 via the #163 item-5 link REJECT. run_out details
   confirm targeted checks, not crashes. `run_stage` treats any crash as
   a trip — acceptable (fail-closed), and no control in fact trips via
   crash.
8. **2 fresh mutations added** (mission item 3): FRESH-MUT-A item-2 orbit
   deleted at L=1 -> REJECT `item2:L1:ledger_incomplete_or_spurious`
   (the independent second-pass enumeration catches it); FRESH-MUT-B
   item-4 residual under-claim (U 16/64 -> 8/64 at L=1,w=6) -> REJECT
   `item4:L1w6:residual_bound_false`. Both trip for the right reason.
9. **#163 four-way attacked** (mission item 4): X1 wrong instance id
   ("C2PP-INSTANCE-20260709") -> REJECT with the #163 tag; X3 countersign
   line naming the WRONG predicate -> M4Reject; X4 status OPEN -> verdict
   stays exactly CONDITIONAL; X5 correct id but reserve_bits=22 -> REJECT.
   X2/X2b/X2c produced **CATCH #166** (below). Item-5 linkage, named
   input block, conditional downgrade all sound as implemented.
10. **G5 truth independently re-derived** (third method, meet-in-the-middle
    over half-supports, structurally different from BOTH in-verifier
    enumerations): total 15/8, per-level {L1: 15/8, L2: 0, L3: 0} —
    matches the banked battery value and the packet's M4-F4.
11. **M5 wiring tested**: shadow M5 file with the exact draft line ->
    "M5: CONFIRMED"; near-miss (2^122) -> stays OUTSTANDING; draft sec-3
    code block == verifier M5_REQUIRED_LINE **byte-exact**; line content
    consistent with the REPOSE catch-#40 addendum (2^122->2^121, reserve
    22->21).
12. **Amber draft wiring vs the house law** (mission item 6): see
    m4a_report.md sec 4 — primary path (statement addendum, node stays
    TARGET) never triggers the leaf-conditional law; the optional route
    badge, IF instantiated as a dag node with status CONDITIONAL, MUST get
    req in-edges from three posed predicate nodes (caveat E-1). The six
    re-surgery criteria each checked triggerable/machine-observable.
    Current dag state confirmed: dli node status TARGET, in-edges 3x ev
    only (red-leaf-law clean); tools/verify_prize_dag.py passes today.
13. **CATCH #165 found and exhibited** — see below. Also verified the same
    code shape exists in the eex template (eex_verify.py:296-299) and that
    the eex abuse battery A5 only tested DOUBLE-charging, never a single
    oversized credit — the hole is inherited, untested in both rounds.

## CATCHES (#165+)

### CATCH #165 — item-5 reserve-credit path is FAIL-OPEN (magnitude and
### justification unbounded) — the one required repair
`verify_certificate` enforces `len(reserve_credits) <= 1` but never bounds
a credit's magnitude nor ties it to coset/accident-owned mass; each credit
is subtracted from the certified total before the item-6 endpoint check.
**Exhibit (run against the banked verifier, unmodified):** the honest demo
certificate at (q=97, n'=16), truth 15/8, ALL buckets owned "bulk", plus
`reserve_credits = [[1,1]]`, threshold T=1: verdict **ACCEPT**, certified
total 7/8, zero checks fired — while the exact truth 15/8 > 1. This is the
exact "assumption-only item-5 content" that catch #163's owed M3 sentence
says must be a REJECT, so m4_report.md sec 3 item 4's claim "The M4
verifier already implements exactly this rule" is FALSE on the credit
path. Provenance: inherited verbatim from eex_verify.py lines 296-299;
the eex A5 abuse (`[[1,4],[1,4]]`) tested only the charged-once count.
No banked conclusion flips (every banked G5/eex verification used
`reserve_credits: []`, and ENDPOINT-EXC coverage is OPEN anyway), but the
fail-closed claim in the amber addendum draft and the M3 #163 sentence
cannot be banked over a known fail-open path. **REPAIR R1 (required
before the amber surgery):** in `verify_certificate`, tether credits —
accumulate the exact per-bucket mass (already enumerated) for buckets
owned "coset"/"accident" and fire
`item5:reserve_credit_exceeds_nonbulk_owned_mass (catch #165)` whenever
`sum(credits) > that mass` (in the demo, all-bulk ownership => any
nonzero credit REJECTs); add mutation control MUT-8 = the exhibit above
(must trip); re-run and re-bank m4_run_out.txt (now 10 controls); extend
the owed M3 one-sentence pin with "...and any reserve credit must be
covered exactly by the mass of buckets owned coset/accident (catch #165)".

### CATCH #166 — the countersign gate needs hardening before any real
### PROVED flip (latent; does not affect the banked verdict)
Three weaknesses, each demonstrated in the shadow harness:
(a) **no identity/instance binding** — the required line names the
predicate ("C2''"), not the instance id, and any file containing it
validates: three one-line forged files flipped the verdict to
ASSEMBLY-VERIFIED-UNCONDITIONAL (X2b);
(b) **no path containment** — `REPO / tok["path"]` with an absolute
tok path resolves OUTSIDE the repo (Python Path-join semantics), so a
countersign can live anywhere on disk (X2c);
(c) **quote fragility** — any future repo document QUOTING the magic line
verbatim becomes a valid countersign target. Current state verified clean:
grep finds ZERO literal occurrences of "MAINTAINER-COUNTERSIGN: <name>
PROVED" for any of the three predicates anywhere in the repo (the m4
packet itself carefully uses placeholders).
Threat model honesty: the manifest statuses/tokens are hardcoded in the
banked verifier, so exploiting (a)-(c) requires repo write access, which
in this house IS maintainer authority — hence latent, not a soundness
break of the banked packet. **Hardening (owed at promotion time):** bind
the instance id in the line (e.g. "MAINTAINER-COUNTERSIGN:
C2PP-INSTANCE-20260710 PROVED"), require the file under
`notes/COUNTERSIGN_<id>.md`, and require
`(REPO/tok.path).resolve().is_relative_to(REPO.resolve())`. Standing
hygiene rule: never quote a live countersign line verbatim in any repo
document.

### CATCH #167 — the banked transcript goes stale across the owed
### surgeries (pre-register the delta or re-bank)
m4_run_out.txt pins the PRE-surgery transcript. After the maintainer's
#162 deletion and M5 file, a fresh green run differs at exactly three
lines: the `[PASS] catch #162: torn duplicate matches...` +
`[info] ...deletion OWED...` pair becomes the single
`[PASS] catch #162: statement CLEAN (post-surgery invariants hold)`, and
`[info] M5: OUTSTANDING...` becomes `[info] M5: CONFIRMED (maintainer
one-liner present)` (both destination lines verified live in the shadow
harness). Anyone diffing a fresh run against the banked transcript would
see a spurious mismatch. Rule: re-bank m4_run_out.txt immediately after
the surgery (mandatory anyway under R1, which changes the control count
to 10), or bank this pre-registered three-line delta beside it.

## NITS (unnumbered; promote at maintainer's discretion)

- **N-1**: m4_test_162_paths.py writes `m4_tmp_repo_{clean,malformed}/`
  into ITS OWN parent directory and does not remove them — executed
  in-place at notes/ it would write inside the repo. Run it only from a
  scratch copy (this audit did; ALL OK).
- **N-2**: the verifier docstring attributes its expanded M4 definition
  ("pinned K-prime, w_max(L), W_cl inputs per zone, R_joint = 21 ...,
  with the f2b + calibration replays as gates") to C2PP_POSED
  'Path to predicate status', which actually reads only "M4 the assembly
  verifier (exact-rational)"; the expansion matches the eex report's M4
  bar (eex_report.md sec 4) and the mission spec — fix the attribution
  or cite both sources. Content faithful; provenance string loose.
- **N-3**: importlib-loading the banked verifier writes
  `notes/__pycache__/m4_assembly_verifier.cpython-312.pyc` (bytecode
  cache). This audit created and then removed one; final state
  byte-identical to baseline. Future auditors: set
  `sys.dont_write_bytecode = True` or load from a copy.

## POSITIVE FINDINGS (confirmations, not catches)

- The packet's M4-F1 slack analysis is exactly right (tau* = 0.6700...,
  12.1 / 4.5 bit slacks at 1/4 and 1/2).
- The banked run transcript replays byte-identically today (modulo the
  appended exit-code line) — full determinism.
- The C1'-inequality replay (G3) uses genuinely independent
  reconstruction (E from M1 signed spectra, W_cl from M2 primitive
  counts, all Fractions), and its positive control is real: the
  no-ledger form fails at (1,7937) as claimed.
- The pose-time G2 bulk values are pinned against the full 8-value pose
  string (the primary substring, including both refuter-row zeros,
  matches — not just the truncated fallback).
- The dli node today is a clean red leaf (TARGET, ev-only in-edges), so
  the packet's amber design starts from a law-compliant state.

## Status after this audit

- VERDICT: **SOUND-WITH-REPAIRS** — exactly one required repair (R1,
  catch #165) plus execution caveats E-1..E-3; full spec and the
  post-repair amber execution order in `m4a_report.md`.
- Catch ledger after this audit: **#167**.
