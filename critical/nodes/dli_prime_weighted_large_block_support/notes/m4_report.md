# M4 — the dli assembly verifier: BUILD REPORT

Date: 2026-07-13. Builder: fresh-context M4 builder (read-only on repos;
all deliverables self-contained in this scratchpad, `m4_` prefix).
Node: `critical/nodes/dli_prime_weighted_large_block_support` (CONJECTURE
B-WEAK). M-ledger source: `notes/C2PP_POSED_20260710.md`, section "Path to
predicate status". F-round state at build time: **C2'' 1 / C1' 1 /
ENDPOINT-EXC 1**. Catch ledger entering this session: #163; issued here:
**#164** (see `m4_findings.md`).

Deliverables (this directory):
- `m4_assembly_verifier.py` — the verifier (exact-rational, fail-closed).
- `m4_run_out.txt` — the banked green run: 103 lines, every check PASS,
  all 9 mutation controls TRIPPED, `exit_code=0`.
- `m4_amber_statement_draft.md` — the amber-surgery statement drafts, the
  M5 exact text, the re-surgery criteria.
- `m4_findings.md` — incremental log + catches #164+.
- `m4_scratch_precheck.py`, `m4_dli_node_dump.json` — working files.

Replay:
```
tools/ramguard tiny -- python3 <scratchpad>/m4_assembly_verifier.py
```
(< 15 s, < 256 MB; no Modal needed — every recomputation is exact and
small; the heavy censuses are consumed as banked records, not re-run.)
Exit 0 = green; exit 1 = gate/pin/assembly/mutation-control failure;
exit 2 = fail-closed input rejection.

---

## 1. What the verifier checks, step by step

### Stage 0 — the input manifest (all inputs explicit, fail-closed)
`build_inputs()` declares five blocks; `validate_inputs()` rejects (exit 2)
on ANY missing block or field:

| input | content | status consumed |
|---|---|---|
| (a) `C2PP_INSTANCE` | the joint-reserve inequality `E_U[prod rho]_reduced <= 2^R_joint * prod E_U[rho]`, `R_joint = 21` bits, 33 junctions, /33 posed convention (#108), theta = 2 | **NAMED CONDITIONAL INPUT**, 1 survived round (M1), provenance pinned to 5 banked files — never silently assumed (catch #163) |
| (b) `C1P_LEDGER` | level-scaled per-level excess `E-1 <= K' r (1+W_cl)`, `K' <= 4`, `w_max(L) = L+5` | NAMED CONDITIONAL, 1 survived round (M2) |
| (c) `ENDPOINT_EXC` | the 6-item per-row certificate rule + the COVERAGE predicate ("for every official row R exists accepted pi_R") | NAMED CONDITIONAL, 1 survived round; `coverage: OPEN` carried honestly |
| (d) `ZONES` | per-level `L = 1..34`: `N = 256L`, zone tag (covered-full / covered-partial / uncovered) that must MATCH the banked `a1_prod_norm_sieve_table.json`, and the per-row `W_cl` input `tau_L = 2^-5` (exact Fraction) whose certification source is pi_R items 2-4 — i.e. ENDPOINT-EXC content, because A1-PROD is density-only and discharges no row (the M3 audit) | input spec |
| (e) `SKELETON` | Lemma-1 exact reduction, D2/D3 identities, the `E >= 1` D3 floor, the consumer-face identity `q^{-t+H} W_cen = E_U[prod rho_j]` | PROVED-PINNED (provenance strings checked) |

### Stage 1 — provenance pins (22 checks)
Exact strings/values in the banked record: the node statement's `q^{-t+H} *
W_cen <= 2^121` and `1/1/1` and #163 sentence; the C2'' pose's `R_joint =
21 bits`, `/33` display, aggregate-form-primary; manifest==pose equality for
21 and /33; the C1' pose's `w_max(L) = L+5` and kill line; M3's soundness
display, all six item phrases, and its "expose coverage as an input"
clause; the eex report's SURVIVED + 1/1/1 + #163; REPOSE's #40 addendum;
the x4 packet's `equivalently half-band count <= 2^121`; the arithmetic pin
`21 + 100 = 121`; and the full 34-level zone-tag agreement with the banked
A1-PROD table (L=1 covered-full with `w_1 = w* = 55`; L=2..19
covered-partial; L=20..34 uncovered).

### Stage 2 — gate G1: the f2b 8-row record replays exactly
From `f2b_nested_correlation.json` + `f2b_replay_perclass_20260710.json`:
row set == the banked 8 rows {(2,97),(2,193),(2,8353),(2,32801),(3,97),
(3,193),(4,97),(4,193)}; `ratio == E_cond/E_uncond` **bit-exact** (IEEE
binary64) at all 8 rows; the two banked files bit-identical on ratios with
`replay_ok` true everywhere; raw GM reproduces the banked 2.139; the two
sparse rows' stripped mass identically zero. Any mismatch => exit 1.

### Stage 3 — gate G2: the pose-time calibration replays
The 8 pose-cited bulk values (0.998/1.010/0/0/1.033/1.066/0.760/0)
reproduce the banked bulk GM 0.967; the four accident masses 128/128/64/128
are exact multiples of the orbit quantum 32; the naive-uniform refuters
2.752/2.874 reproduce from the banked stripped ratios AND exceed the /33
allowance **exactly** (Fraction comparison `x^33 > 2^21` — no floats on the
decision path) — the three-part C2'' shape is forced, which is the pose's
survival argument.

### Stage 4 — gate G3: the C1' M2 record, full exact-rational replay
All 12 frozen rows recomputed from the M1 signed spectra + M2 primitive
counts as exact Fractions: `E-1`, `r`, `W_cl` fields match; the C1'
inequality holds at every row; the positive control fires (the no-ledger
form FAILS at (L=1, q=7937) — the repair is substantive); max
`K' = 0.246909432` exactly at the preselected accident row, `< 1/4`.

### Stage 5 — gate G4: the C2'' M1 record pins
45 rows, all n=64, depths {2,3}; theta = 2.0; `Fa_fired`/`Fc_fired` both
false; verdict `C2'' SURVIVES...`; zero sub-orbit anomaly flags; the full
Modal log banked with the survival verdict and the /33 display.

### Stage 6 — gate G5: the ENDPOINT-EXC 6-item certificate, demonstrated
A complete honest pi_R is built and verified at the exact toy row
(q=97, n'=16, schedule L=1,2,3) with fail-closed eex-round semantics:
item 1 (row key/field/pins — primality, splitting, pinned omega + order,
generated-field normalization), item 2 (complete low-weight orbit ledger,
completeness checked against an INDEPENDENT second-pass enumeration +
Vandermonde floor guard), item 3 (orbit sizes exact, quantum 2N, dedup),
item 4 (every unlisted weight class present, exact recount lower-bounds the
claimed residual, rejected certificate types refused), item 5 (every bucket
owned exactly once by coset/bulk/accident, reserve bits == the named C2''
instance's 21, reserve charged at most once, **and the c2pp_instance link
must resolve to the manifest's named C2''-instance — catch #163**), item 6
(exact-rational final check). The exact truth replays the eex-banked
battery value **15/8**; the honest certificate ACCEPTs at T=4 and the SAME
certificate REJECTs at T=1 (truth 15/8 > 1) — fail-closed in both
directions.

### Stage 7 — the assembly chain (exact inequalities on declared inputs)
- **A0** consumer-face identity pinned (`q^{-t+H} W_cen = E_U[prod rho_j]`;
  x4 packet string).
- **A1** Lemma-1 / D2 / D3 skeleton declared with the `E >= 1` floor.
- **A2** balance: `r_L = q^L / 2^{256L} < 1` for every admissible
  `q < 2^256` — exact integer inequality at L = 1, 2, 34.
- **A3/A4** per-level excess + aggregate: from C1' (`E_L <= 1 + K' r_L
  (1+W_cl_L)`), `r_L < 1`, and the zone inputs (`W_cl_L <= tau_L = 2^-5`
  per row, certified by pi_R):
  `prod_{L=1}^{34} (1 + 4(1 + 2^-5)) = (41/8)^34 <= 2^100` — exact
  rational; measured usage **80.1568 bits of 100** (slack 19.8432 bits).
- **A5** the joint reserve composes: `2^21 * (41/8)^34 <= 2^121` — exact.
- **A6** endpoint identity `21 + 100 = 121` — exact.
- Conclusion printed as CONDITIONAL on the three named predicates.

### Stage 8 — catch #162 detection (read-only)
See section 2. Presence of the torn duplicate is verified against the
pinned spec (verbatim-copy property + sha256) and reported as
deletion-owed; a HALF-deleted/malformed state fails the run; the
post-surgery clean state passes via its own invariants — the verifier stays
green across the maintainer's edit.

### Stage 9 — mutation controls (9 built-in tampers; ALL must trip)
| control | tamper | tripped by |
|---|---|---|
| MUT-1 | reserve 21 -> 22 | pin `manifest R_joint == posed 21` + assembly A6 `21+100=121` |
| MUT-2 | zone bound broken (`tau_20 = 2^30`) | A3/A4 aggregate `> 2^100` + A5 |
| MUT-2b | zone tag L=20 claims covered | zone-table agreement pin |
| MUT-3 | certificate item3 removed | fail-closed `item3:MISSING` REJECT |
| MUT-4a | C2'' honestly unproved | verdict logic returns exactly `ASSEMBLY-VERIFIED-CONDITIONAL (...)`, never PASS |
| MUT-4b | C2'' flagged PROVED, no countersign | `M4Reject: no silent upgrade` |
| MUT-5 | coverage input deleted | `M4InputReject` (exit-2 path) |
| MUT-6 | junction convention -> /34 | #108 convention pin |
| MUT-7 | item-5 c2pp link severed | `item5:c2pp_instance_unresolved (catch #163)` REJECT |

A control that does NOT trip fails the whole run (exit 1).

### Stage 10 — verdict
```
M4-VERDICT: ASSEMBLY-VERIFIED-CONDITIONAL (on C2'', C1', ENDPOINT-EXC as named predicates)
```
The amber wiring consumes exactly this line. The unconditional verdict
string exists in the code but is reachable ONLY when all three predicates
carry `status: PROVED` **and** a maintainer countersign file containing
`MAINTAINER-COUNTERSIGN: <name> PROVED`; any PROVED claim without it is a
hard reject. M5 status is displayed informationally (currently
OUTSTANDING; exact required text in `m4_amber_statement_draft.md` section 3).

---

## 2. CATCH #162 — the exact deletion spec

**Location:** `dag.json`, node `dli_prime_weighted_large_block_support`,
field `statement` (a single JSON string).

**The fragment (613 characters):** at string offsets **[6673, 7286)**
(0-indexed, current file state 2026-07-13), beginning verbatim
```
==gridDP PASS; full log banked at notes/m1_run_record_20260713.log): F-a NOT FIRED at either depth (
```
and ending verbatim (INCLUDING the trailing space)
```
...per the node-pinned F-round rule it is now PROMOTION-ELIGIBLE pending maintainer review. 
```
sha256 of the fragment: `d60593436da96d99...` (first 16 hex digits; the
verifier pins this).

**Why it is a duplicate:** the fragment is a VERBATIM copy of statement
chars [5461, 6074) — the tail of the original "M1 ROUND SURVIVED" block,
torn mid-token at `MITM==gridDP PASS` (the duplicate resumes at
`==gridDP`). Mechanical counts before surgery: `F-a NOT FIRED at either
depth` x2, `C2''s F-round count: 0 -> 1` x2, `==gridDP PASS` x2 with
`MITM==gridDP PASS` x1.

**The edit:** delete statement[6673:7286] — nothing else. The wave-4
paragraph then reads seamlessly:
```
... custody-merged per #104/#120; binding new content follows, full text in the node folder): M2 ROUND SURVIVED: the committed level-scaled C1' pose ...
```

**Post-surgery invariants (the verifier checks these automatically once the
duplicate is gone):** exactly one occurrence each of `F-a NOT FIRED at
either depth`, `C2''s F-round count: 0 -> 1`, and `==gridDP PASS` (the
surviving one inside `MITM==gridDP PASS`); the original M1 paragraph
untouched.

**Caution:** edit via a JSON-aware tool (load, mutate the string, dump) —
the statement contains escaped characters; a byte-offset edit on the raw
file is NOT offset [6673, 7286).

---

## 3. CATCH #163 — the semantics as implemented

The pinned requirement: *M4 must expose the C2''-instance as an explicit
input alongside coverage, else item-5's soundness display is secretly
conditional.* Implemented as four mutually reinforcing mechanisms:

1. **Named input block.** `C2PP_INSTANCE` is a first-class manifest input
   with id `C2PP-INSTANCE-20260710`, the posed clause text, `R_joint = 21`,
   the /33 convention, `status: CONDITIONAL`, `rounds_survived: 1`, and
   five provenance files — parallel to (not folded into) the
   `ENDPOINT_EXC` coverage input. Deleting either block is a fail-closed
   input rejection (MUT-5 demonstrates the coverage side).
2. **Item-5 linkage.** Every pi_R's item 5 must carry a `c2pp_instance`
   field resolving to that manifest id, and its `reserve_bits` must equal
   the instance's 21. A certificate whose item 5 is consistency-only
   (well-formed ledger, no link) is REJECTED with
   `item5:c2pp_instance_unresolved (catch #163)` (MUT-7). This makes the
   conditionality of "ACCEPT => endpoint" syntactically visible in every
   certificate.
3. **Verdict downgrade.** The verdict function returns the CONDITIONAL
   string whenever ANY of the three predicates is unproved (MUT-4a), and
   hard-rejects a PROVED claim lacking a maintainer countersign (MUT-4b) —
   item-5's soundness display can never silently become unconditional.
4. **M3 one-sentence surgery (owed, maintainer edit):** append to M3's
   "Certificate soundness" section: *"Item 5's verification semantics are
   pinned: the ownership ledger must either be verified per-row by exact
   joint accounting or consume C2'' as a named wired predicate;
   assumption-only item-5 content is a REJECT (catch #163)."* The M4
   verifier already implements exactly this rule, so the sentence can be
   banked together with M4.

---

## 4. The amber-surgery spec

Full drafts in `m4_amber_statement_draft.md`:
- section 1 — the statement addendum recording M4 (apply AFTER the #162
  deletion);
- section 2 — the petal-template conditional-close entry with the three
  predicates wired (P1 C2'', P2 C1', P3 ENDPOINT-EXC with coverage OPEN
  flagged as the widest gap), the green skeleton, and pins
  P-CONS/P-FIELD/P-ROWS/P-CONV;
- section 3 — **the M5 line, exact required text** (one sentence; the
  verifier greps it verbatim from
  `notes/M5_CONFIRMATION_2P121.md` and flips M5 OUTSTANDING -> CONFIRMED);
- section 4 — six pre-registered re-surgery (downgrade) criteria + the
  re-promotion rule (new round + fresh green M4 run).

The 2026-07-10 amber audit's four blockers, revisited: (1) F-round zeros —
now 1/1/1; (2) no machine-verified assembly — M4 is that artifact; (3) the
naive uniform C2'' refuted — the posed three-part form is what M4 consumes,
and gate G2 re-verifies the refuters exceed the allowance exactly; (4)
catch #40 staleness — the head repair is banked, M5 remains the
maintainer's one-liner. **After M5, the amber attempt has no open technical
item.**

---

## 5. Honest scope (what M4 does NOT do)

- It proves NO predicate: C1', C2'', ENDPOINT-EXC-COVERAGE all remain
  unproved; B-WEAK remains a conjecture with its pre-registered falsifier.
- The production coverage obligation (every official row has an accepting
  pi_R) is OPEN — the pose's own status; M4 consumes it as a named input
  and demonstrates the certificate semantics at exact toy scale (n' = 16
  demo here; the eex round exercised n' <= 64).
- `tau_L = 2^-5` is an INPUT SPEC (what each pi_R must certify per level,
  matching the A1-PROD threshold trade-off row), not a theorem; the
  aggregate closes for any uniform certified `tau <= 0.67` (19.8 bits of
  slack at 2^-5 — see finding M4-F2).
- The consumer-face identity and the banked joint measurements are
  provenance-pinned, not re-derived; the heavy censuses (M1 n=64 Modal,
  eex cells) are consumed as banked records with their own verifiers.
