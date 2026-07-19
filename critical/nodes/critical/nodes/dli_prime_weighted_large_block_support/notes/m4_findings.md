# M4 build — incremental findings log

Builder: fresh-context M4 builder, 2026-07-13. Repo READ-ONLY throughout;
all artifacts in this scratchpad (`m4_` prefix). Catch ledger entering:
#163.

## Run log (incremental)

1. **Read-in.** dag.json dli node dumped (`m4_dli_node_dump.json`);
   C2PP_POSED (M-ledger, M4 definition), M3 coverage contract, C1' pose,
   M1/M2 audits + verifiers, eex report/findings/verifier (the certificate
   semantics template), A1-PROD theorem + banked 34-level table, REPOSE
   (incl. #40 addendum), DLI_CLOSE_PINNED (Lemma-1/D2/D3 + DLI-AGG <= 100 +
   round-6 excess correction), x4 REDUCTION_PACKET (the 2^121 consumer
   face), KB_LOG #108/#162/#163 entries.
2. **#162 located exactly.** Statement chars [6673, 7286), 613 chars,
   verbatim copy of [5461, 6074), torn at `MITM==gridDP PASS`; sha256
   prefix `d60593436da96d99`; deletion spec written (m4_report.md sec 2).
3. **Pre-check run** (`m4_scratch_precheck.py`, ramguard tiny): f2b
   cross-file ratios bit-identical AND recomputable bit-exactly; raw GM
   2.139 reproduces; toy battery truth 15/8 reproduces by fresh exhaustive
   enumeration (weights {4,5,6,7} x 16 vectors at L=1, q=97, n'=16; L=2,3
   empty); aggregate (41/8)^34 <= 2^100 exact (80.157 bits); A1 zone table
   pinned (L=1 full, 2..19 partial, 20..34 uncovered). DISCOVERY: the
   banked "2^(21/33) = 1.555" display is wrong in the last digit -> catch
   #164 below.
4. **Verifier built + green on first full run** (ramguard tiny, ~10 s):
   22 provenance pins, gates G1-G5, assembly A0-A6, #162 detection, 9/9
   mutation controls tripped, verdict line CONDITIONAL. Banked as
   `m4_run_out.txt` (exit_code=0 recorded in-file).
5. **Drafts banked**: `m4_amber_statement_draft.md` (statement addendum,
   conditional-close entry, M5 exact text, 6 re-surgery criteria),
   `m4_report.md`.
6. **#162 detector path test** (`m4_test_162_paths.py`, ramguard tiny,
   ALL OK): the current duplicate state matches the pinned spec; the
   post-surgery clean state passes its invariants (so the banked verifier
   stays green across the maintainer's edit); a malformed half-surgery
   state is rejected fail-closed (`M4Reject`). Temp repo copies removed
   after the run.

## CATCHES (#164+)

### CATCH #164 — the /33 allowance display "1.555" is a last-digit slip
2^(21/33) = 1.554406... which rounds to **1.554**, not 1.555. The wrong
display appears in exactly two banked texts:
- `notes/C2PP_POSED_20260710.md` (clause (ii)): "geometric-mean junction
  allowance 2^(21/33) = 1.555";
- the dag.json dli statement, the catch-#108 pin sentence: "the
  junction-allowance display is the POSED /33 form (2^(21/33) = 1.555)".
(The mission/goal texts quoting them inherit the slip.) DISPLAY-ONLY: no
conclusion flips — nothing gates on the GM-per-junction display (the
aggregate form is primary by the pose's own words; the M1 log's
bits-per-junction display "21/33 = 0.636" is CORRECT, and the pose's
survival comparison used the drift values 1.534/1.566 vs stripped refuters
2.752/2.874, which exceed EVERY variant). Provenance of the slip: probably
a carry-over from 2^(22/34) = 1.5658 -> "1.566" -> mis-adjusted. SURGERY
(maintainer, cosmetic, can ride along with the #162 edit): replace "1.555"
with "1.554" at both sites. The M4 verifier prints the catch as an [info]
line, pins the RECOMPUTED display (1.554) on its decision path, and does
NOT fail on the banked slip.

No other catches: the /34 drift in `f2b_replay_perclass_20260710.py` line
105 and in `c2pp_calibration_20260710.py` line 71 is the ALREADY-PINNED
catch #108 (display drift, no new entry owed).

## FINDINGS (positive, not catches)

### M4-F1 — the assembly has 19.84 bits of aggregate slack at tau = 2^-5
With the pinned K' = 4 and the per-level zone input tau_L = 2^-5, the
34-level aggregate uses 34*log2(41/8) = 80.157 bits of the 100-bit DLI-AGG
budget. The exact break-even uniform threshold is tau <= (2^{50/17} - 5)/4
= 0.6700...: any per-row certified W_cl <= 0.67 per level closes the
budget. Consequence for the pi_R spec: the certificates do NOT need the
aggressive 2^-5 — W_cl <= 1/4 per level (8x weaker) still leaves 12.1 bits
of slack, and even W_cl <= 1/2 (16x weaker) leaves 4.5 bits. This
materially widens the feasible region for the open coverage obligation
(the widest-gap predicate P3).

### M4-F2 — the M1 results file already carries the joint-gate fields
`m1_dli_m1_results.json` rows carry E_cond/E_uncond/ratio/stripped/bulk
at n = 64 in exactly the f2b schema, so a future M4-tightening could add a
G1' gate on the 45-row n = 64 record with zero new computation. Not added
now: the mission's gates are the f2b 8-row record + the pose-time
calibration, and gate G4 already pins the M1 verdict/flags.

### M4-F3 — the countersign mechanism gives M5/promotion a machine surface
The verdict logic accepts `status: PROVED` only with a countersign file
containing `MAINTAINER-COUNTERSIGN: <predicate> PROVED`. This turns the
F-round promotion rule ("pending maintainer review") into a checkable
artifact: the future promotion of C2'' is a one-line file, and the M4
verifier will flip its verdict only then — no prose ambiguity. The M5
endpoint confirmation got the same treatment
(`notes/M5_CONFIRMATION_2P121.md`, exact line in the draft).

### M4-F4 — the demo certificate's independence structure
The G5 demo builds pi_R from a `product`-loop enumeration and verifies
item 2 against a second, structurally different enumeration
(supports x sign patterns). At (q=97, n'=16) the two agree and reproduce
the eex-banked battery truth 15/8 with per-level split {L1: 15/8, L2: 0,
L3: 0} — consistent with the eex Cell-A band structure (q=97 is the #2
heaviest n'=16 row, finding F-1 of the eex round).

## Status after this build

- M4: **DONE** (this deliverable set; banking = maintainer copies the
  verifier + run-out into the node notes, applies the #162 deletion per
  spec, optionally the #164 cosmetic fix and the M3 one-sentence #163 pin).
- Remaining before the amber attempt: **M5 only** (the 2^121 maintainer
  one-liner; exact text in `m4_amber_statement_draft.md` sec 3).
- Re-surgery criteria pre-registered (draft sec 4).
