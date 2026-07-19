# M4A — AUDIT REPORT: the dli M4 assembly-verifier packet

Auditor: fresh-context PACKET AUDITOR, 2026-07-13. Repo READ-ONLY
(byte-identical to baseline at close; hash proofs
`m4a_baseline_hashes_node.txt` / `m4a_final_hashes3.txt`, 95 files incl.
dag.json and the x4 packet). Packet:
`critical/nodes/dli_prime_weighted_large_block_support/notes/`
{m4_assembly_verifier.py, m4_run_out.txt, m4_report.md,
m4_amber_statement_draft.md, m4_findings.md, m4_test_162_paths.py} — all
six byte-identical to the builder's scratchpad copies (hashes matched).
Incremental log + full catch texts: `m4a_findings.md` (this directory).
Catch ledger entering #164; issued here **#165 #166 #167**; ledger now
**#167**.

---

## VERDICT: **SOUND-WITH-REPAIRS**

The assembly arithmetic, all 22 provenance pins, gates G1-G4, the #162
deletion spec, the #163 four-way implementation, the #164 figure, the M5
wiring, and the amber draft's predicate/criteria structure are all
verified sound — most by independent exact re-derivation or by live
tamper/attack. **One repair is REQUIRED before the amber surgery executes
(R1, catch #165):** the G5 toy VERIFY_ENDPOINT_EXC's item-5 reserve-credit
path is fail-open (exhibit: the honest all-bulk demo certificate plus a
single untethered credit `[[1,1]]` ACCEPTs at T=1 while the exact truth is
15/8 > 1; zero checks fire). This contradicts (i) the packet's "fail-closed
in both directions" characterization of the certificate semantics and
(ii) the owed M3 #163 sentence's claim that "The M4 verifier already
implements exactly this rule" — an untethered credit IS assumption-only
item-5 content, and it is not rejected. The hole is inherited verbatim
from the eex template (eex_verify.py:296-299; the eex A5 abuse only tested
double-charging). No banked conclusion flips (every banked verification
used empty credits; coverage is OPEN regardless), so this is repairable,
not verdict-invalidating. With R1 applied, MUT-8 added, and m4_run_out.txt
re-banked green, **the amber surgery may execute from the draft** per the
execution order in section 5.

Two further catches are non-blocking: #166 (countersign-gate hardening
owed at promotion time — instance binding, path containment, quote
hygiene; latent because the manifest is hardcoded honest) and #167
(the banked transcript's pre-registered three-line delta across the #162
deletion + M5 landing; re-bank after surgery). Nits N-1..N-3 in
m4a_findings.md.

---

## 1. Link-by-link table

| # | link | what the packet claims | independent check performed | result |
|---|------|------------------------|------------------------------|--------|
| L1 | per-level factor | E_L <= 1 + K'(1+tau) = 41/8 with K'=4, tau=2^-5 | exact Fraction re-derivation | PASS (41/8 exact) |
| L2 | A3/A4 aggregate | (41/8)^34 <= 2^100 | exact integer form 41^34 <= 2^202; Decimal 60-digit bits | PASS; 34xlog2(41/8) = 34x2.357552 = **80.156768** bits (mission's 80.16 confirmed); slack 19.8432; min whole-bit budget 2^81 |
| L3 | A5 reserve composition | 2^21 * (41/8)^34 <= 2^121 | exact integer form 2^21*41^34 <= 2^223 | PASS |
| L4 | A6 endpoint identity | 21 + 100 = 121 | trivial exact | PASS |
| L5 | A2 balance | r_L = q^L/2^{256L} < 1, q < 2^256 | (2^256-1)^L < 2^{256L} — holds for each L independently; verifier samples L=1,2,34 | PASS (claim true for all 34 L) |
| L6 | K' <= 4 encoded | manifest pin + G3 12-row exact-rational C1' replay | code read + full replay + T3 tamper | PASS; max K' = 0.246909432 at (1,7937) matches the M2 audit; positive control (no-ledger fails there) real |
| L7 | w_max(L) = L+5 encoded | G3 requires weights == [L+1..L+5]; pose pin | code read (`row["weights"] != list(range(L+1, L+6))` fails the row) | PASS |
| L8 | W_cl zone inputs | tau_L = 2^-5 all 34 levels, tags == banked A1-PROD table, certified_by = pi_R items 2-4 | code read; MUT-2 (manifest tamper) + T5 (banked-table tamper) both trip | PASS; honestly an INPUT SPEC, zone tags density-only (M3-consistent) |
| L9 | R_joint = 21 at /33 | pins (manifest==posed 21, /33, #108) + G2 exponent-33 exceedance | X^33 > 2^21 exact for 2.752 (48.2 bits) and 2.874 (50.3 bits); boundary 1.5544^33 < 2^21 — discriminating | PASS |
| L10 | gate G1 (f2b 8-row) | bit-exact ratio replay, cross-file identity, GM 2.139, sparse zeros | full replay byte-identical to banked run_out; **T1 tamper (+1e-9 on one ratio) -> exit 1** | PASS, NON-VACUOUS |
| L11 | gate G2 (calibration) | bulk GM 0.967 from the 8 pose-cited values, accident quanta, refuters exact | pose primary substring carries all 8 values; **T2 tamper (2.7515->1.5) -> exit 1** | PASS, NON-VACUOUS |
| L12 | gate G3 (C1' M2) | 12 rows exact-rational from M1 spectra + M2 primitives | **T3 tamper (E-1 numerator +1) -> exit 1** | PASS, NON-VACUOUS |
| L13 | gate G4 (C2'' M1 pins) | 45 rows n=64, theta 2.0, flags false, verdict, /33 log | T4 tamper (Fa_fired->true) -> G4 fails | PASS, NON-VACUOUS |
| L14 | gate G5 (eex demo) | truth 15/8; ACCEPT@T=4 / REJECT@T=1 fail-closed | independent THIRD enumeration (MITM over half-supports): 15/8, per-level {15/8,0,0}; demonstrated pair sound; **credit path fail-open — CATCH #165** | PASS with REPAIR R1 |
| L15 | catch #162 spec | delete stmt[6673:7286), 613 chars, sha d60593436da96d99, verbatim copy of [5461:6074) | all re-verified on live dag.json; pre-counts 2/2/2 -> post 1/1/1 + MITM retained; JSON round-trip valid; seam sense preserved; 3-state detector test replayed ALL OK from scratch copy | PASS |
| L16 | catch #163 four-way | named input / item-5 link / downgrade / countersign | attacks X1 (wrong id) REJECT, X3 (wrong-name countersign) M4Reject, X4 (OPEN) stays CONDITIONAL, X5 (reserve 22) REJECT; X2b/X2c -> **CATCH #166 hardening** | PASS (hardening owed at promotion) |
| L17 | 9 mutation controls | all trip | each code path read: trips for the RIGHT reason (details m4a_findings.md item 7; note MUT-1 is correctly caught by A6, not A5); run_out details show targeted checks, not crashes | PASS |
| L18 | fresh mutations (audit-added) | — | FRESH-MUT-A item-2 orbit deleted -> `item2:L1:ledger_incomplete_or_spurious`; FRESH-MUT-B item-4 U 16/64->8/64 -> `item4:L1w6:residual_bound_false` | BOTH TRIP correctly |
| L19 | M5 wiring | exact-line grep flips OUTSTANDING->CONFIRMED | shadow test: exact line flips; 2^122 near-miss does NOT; draft sec-3 block == verifier constant **byte-exact**; consistent with REPOSE #40 addendum (2^122->2^121, 22->21 bits) | PASS |
| L20 | catch #164 figure | 2^(21/33) = 1.554, banked 1.555 wrong | recomputed: **1.554406281770** -> 1.554; 2^(22/34) = 1.566 (provenance hypothesis plausible); display-only confirmed (no pin gates on the banked digit) | PASS |
| L21 | amber draft: predicates + law | three predicates wired; node keeps TARGET | see section 4 (house-law analysis); dag today: dli TARGET, ev-only in-edges; verify_prize_dag.py passes | PASS with caveat E-1 |
| L22 | amber draft: 6 re-surgery criteria | pre-registered downgrades | each checked triggerable/machine-observable (1: F-round symmetric; 2: MUT-1 shows fail-closed; 3: pin A0/x4 string breaks; 4: P3 death; 5: G2/G4 fail; 6: verifier rejects) | PASS |
| L23 | verifier replay determinism | banked run_out is the green run | fresh run byte-identical modulo the appended `exit_code=0` line | PASS |
| L24 | packet integrity | notes copies == builder copies | sha256 all six pairs identical | PASS |

## 2. Catches issued (full texts in m4a_findings.md)

- **CATCH #165** (REQUIRED REPAIR R1): item-5 reserve-credit fail-open.
  Exhibit: honest all-bulk demo cert + `reserve_credits=[[1,1]]` at T=1 ->
  ACCEPT with certified total 7/8 while truth 15/8 > 1, zero checks fired.
  Fix: tether `sum(credits)` to the exact mass of buckets owned
  coset/accident (all-bulk => any credit REJECTs); add MUT-8 = the
  exhibit; re-bank run_out (10 controls); extend the owed M3 sentence.
  Inherited from eex_verify.py:296-299 (eex A5 only tested double-charge).
- **CATCH #166** (latent, promotion-time): countersign gate — no
  instance-id binding (three forged one-line files reach UNCONDITIONAL),
  no path containment (absolute tok path escapes REPO), quote fragility
  (any doc quoting the line verbatim validates; current repo verified to
  contain ZERO such literals). Hardening spec in m4a_findings.md.
- **CATCH #167** (operational): the banked m4_run_out.txt goes stale
  across the #162 deletion + M5 landing — pre-registered three-line delta
  (`statement CLEAN` replaces the duplicate-PASS + deletion-owed pair;
  `M5: CONFIRMED` replaces OUTSTANDING; both destination lines verified
  live); re-bank after surgery (mandatory anyway under R1).
- Nits N-1 (m4_test_162_paths.py writes tmp repos into its parent dir —
  never run in-place at notes/), N-2 (docstring's M-ledger attribution is
  loose; the expanded M4 bar is actually eex_report.md sec 4), N-3
  (importlib loads write notes/__pycache__ bytecode; use
  dont_write_bytecode).

## 3. Mission checklist coverage

1. Arithmetic: (41/8)^34 <= 2^100 exact, 80.156768 bits (34 x 2.357552);
   2^21 composition to 2^121 exact; every A-step and gate inequality read
   against the M-ledger items (K' <= 4, w_max = L+5, W_cl zones,
   R_joint = 21 @ /33) — all encoded where claimed. DONE (L1-L9).
2. Gates non-vacuous by tamper (T1/T2/T3 mandated + T4/T5 bonus), banked
   originals byte-untouched (hash-diff proof). DONE.
3. 9 controls trip for the right reasons (code-path read) + 2 fresh
   auditor mutations, both trip. DONE.
4. #163 four-way attacked (5 attacks); implementation sound; #166 issued
   for the countersign hardening. DONE.
5. #162 span verified exactly against live dag.json (sha, verbatim-copy,
   counts, JSON validity, sense); detector 3-state test replayed. DONE.
6. Amber draft: predicate wiring vs the house law (sec 4), 6 criteria
   checked, M5 text byte-exact and #40-consistent. DONE.
7. #164 recomputed: 1.554406... -> 1.554. CONFIRMED. DONE.

## 4. The amber draft vs the house leaf-conditional law (exact statement)

The law (tools/verify_prize_dag.py:91-101): any dag node with
`status == CONDITIONAL` must have >= 1 incoming req/alt edge, else FAIL
("wire the conditions as nodes or demote to TARGET"). The red-leaf law
(lines 78-89): a TARGET/CONJECTURE must keep ev/ref-only in-edges.

How the draft satisfies this:
- **Primary path (sec 1, statement addendum):** the B-WEAK node KEEPS
  status TARGET (verified live: status TARGET, in-edges 3x ev). No node
  acquires status CONDITIONAL, so the leaf-conditional law never
  triggers; the three hypotheses are wired at the ARTIFACT level — named
  manifest inputs of the machine verifier whose CONDITIONAL verdict
  string names them, with provenance files cited in the addendum text.
  This is law-compliant as-is.
- **Optional path (sec 2, route badge):** IF the maintainer instantiates
  the badge as a dag node with status CONDITIONAL, the law REQUIRES
  creating the three predicates as posed nodes (TARGET red leaves,
  statements from C2PP_POSED / C1PRIME pose / M3) with req edges INTO the
  badge node — the draft names P1/P2/P3 with file refs but does not spell
  out the node+edge creation step (**caveat E-1**). Also do NOT wire req
  edges into the still-TARGET dli node itself — that violates the
  red-leaf law; the badge node is the req consumer.

The six re-surgery criteria (draft sec 4): each is triggerable and
machine-observable or procedurally pinned — (1) F-round symmetry;
(2) endpoint re-pin => verifier fails closed (MUT-1 demonstrates);
(3) consumer-face change => pin A0/x4-string breaks automatically;
(4) coverage refuted => P3 dies; (5) /33 or theta revision => G2/G4 fail
(theta==2.0 and the /33 exponent are pinned); (6) silent upgrade =>
M4Reject, bypass = custody incident. Sound as pre-registered.

M5 (draft sec 3): the required line is byte-exact with the verifier
constant and states exactly the catch-#40 re-pin content (operative
endpoint 2^121, joint reserve 21 bits, 2^122 displays superseded) —
consistent with the REPOSE addendum. The flip was live-tested in both
directions (exact line -> CONFIRMED; 2^122 near-miss -> OUTSTANDING).

## 5. Amber-surgery EXECUTION ORDER (valid once R1 is applied)

0. **R1 (blocking, catch #165):** patch `verify_certificate` in
   notes/m4_assembly_verifier.py — tether reserve credits to
   coset/accident-owned exact mass; add MUT-8 (honest cert +
   `[[1,1]]` credit at T=1 must REJECT); run
   `tools/ramguard tiny -- python3 notes/m4_assembly_verifier.py`;
   confirm exit 0 with 10/10 controls; re-bank m4_run_out.txt. Update the
   draft addendum's "Nine mutation controls" -> "Ten" (and add "untethered
   reserve credit" to its parenthetical list).
1. **#162 deletion (FIRST dag edit; JSON-aware, never byte-offset on the
   raw file):** load dag.json; s = node.statement; pre-check
   `len(s) == 8950` and `sha256(s[6673:7286])[:16] == "d60593436da96d99"`;
   set `statement = s[:6673] + s[7286:]`; dump with the house JSON
   convention. Post-checks: the three invariant counts go 2/2/2 -> 1/1/1
   with "MITM==gridDP PASS" retained; `tools/verify_prize_dag.py` green;
   the M4 verifier now prints "[PASS] catch #162: statement CLEAN".
2. **Statement addendum (sec 1 of the draft), appended AFTER the
   deletion** (same JSON-aware tool). Verified safe: the addendum contains
   none of the #162 invariant strings and none of the statement pins'
   targets change. (Mechanically, append-then-delete would also work —
   the span [6673,7286) precedes the append point — but keep the draft's
   order.)
3. **Optional #164 cosmetic ride-along:** "1.555" -> "1.554" in
   C2PP_POSED_20260710.md clause (ii) and in the statement's #108 pin
   sentence. Verified safe: no verifier pin depends on the banked digit
   (the pose pin requires only "2^(21/33)"; the info line simply stops
   printing).
4. **M3 one-sentence #163 pin** appended to "Certificate soundness",
   extended per R1: "...assumption-only item-5 content is a REJECT
   (catch #163), and any reserve credit must be covered exactly by the
   mass of buckets owned coset/accident (catch #165)." Verified safe: all
   three M3 pins are substring checks unaffected by an append.
5. **M5:** create notes/M5_CONFIRMATION_2P121.md containing the exact
   draft sec-3 line (byte-exact; the verifier greps it verbatim). The
   verifier flips to "M5: CONFIRMED".
6. **Final green run + re-bank** m4_run_out.txt (per catch #167 the
   transcript legitimately differs from today's at the #162 and M5 lines
   and the new MUT-8 line). The amber wiring consumes exactly
   `M4-VERDICT: ASSEMBLY-VERIFIED-CONDITIONAL (on C2'', C1', ENDPOINT-EXC
   as named predicates)`.
7. **Amber surfacing:** statement-addendum-only (law-clean as-is), or the
   route badge as a dag node — then FIRST create the three posed predicate
   nodes + req edges into the badge (caveat E-1), re-run
   verify_prize_dag.py, and keep the dli node's in-edges ev-only.
8. Standing rule: refresh the artifact + publish the site after the DAG
   update.

## 6. Honest scope of this audit

- I did not re-run the heavy censuses (M1 n=64 Modal, eex cells); they
  enter as banked records exactly as the packet declares, and their own
  verifiers/audits are prior art (M1_RESULT_AUDIT, M2 audit, eex round).
- The three predicates remain unproved; nothing here upgrades them — this
  audit checked the ASSEMBLY packet, and its conditional verdict survives
  every attack except the one repaired path (#165).
- All tamper work ran against a shadow copy under the scratchpad; the
  live repo is byte-identical to its pre-audit state (hash-diff proof
  banked).
