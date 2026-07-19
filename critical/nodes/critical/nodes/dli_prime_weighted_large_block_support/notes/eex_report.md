# ENDPOINT-EXC ADVERSARIAL ROUND — REPORT (round 1 for ENDPOINT-EXC)

Date: 2026-07-13. Runner: fresh-context falsification runner.
Companion files (same directory, self-contained set):
- `eex_findings.md` — the pre-registration (reads + kill lines fixed before
  any run), the incremental run log, the fired-and-retracted line's full
  audit trail, catches, findings.
- `eex_verify.py` — every check of the round, replayable (commands below).
Repo paths referenced are absolute under
`/home/u2470931/smooth-read-solomin/prize/`. Repos untouched (read-only).
Catch ledger entries issued: #162, #163.

---

## 1. THE POSED CLAIM (verbatim)

Source: `critical/nodes/dli_prime_weighted_large_block_support/notes/M3_ENDPOINT_EXCEPTION_COVERAGE.md`
(wave-4 import, Codex 5b436aa, custody-merged per #104/#120; static audit
`notes/verify_m3_endpoint_contract.py` — re-run this round: PASS 11/11).

> For an official row `R`, an endpoint-exception certificate `pi_R` must contain:
> 1. the exact row key, field presentation, generated-field normalization, and
>    primality/order certificates;
> 2. for every production level, a complete low-weight orbit ledger with a
>    checkable completeness proof, not only exhibited representatives;
> 3. exact multiplier-shadow and lift de-duplication bounds;
> 4. an independently checkable residual near-peak upper certificate for every
>    unlisted weight/frequency class;
> 5. the C2'' coset/bulk/accident ownership ledger, with the aggregate reserve
>    charged once;
> 6. an exact rational final check against the binding endpoint `2^121`.
>
> VERIFY_ENDPOINT_EXC(R,pi_R)=ACCEPT  ==>  q^{-t+H} W_cen(R) <= 2^121.
>
> for every official row R, there exists pi_R such that
> VERIFY_ENDPOINT_EXC(R,pi_R)=ACCEPT.        (ENDPOINT-EXC-COVERAGE)

Rejected certificate types (verbatim): "'No explicit construction is known,'
'the row is likely nonexceptional,' and PPT/engineering hardness are rejected
certificate types." Scope: "every official code row, not a density-one or
deployer-selected set." Nonclaim: "A1-PROD does not discharge this
obligation." The pose itself marks COVERAGE as OPEN ("posed but open";
"soundness without coverage is only a conditional checker").

## 2. THE PRE-REGISTERED ATTACK (fixed before any run; full text in
## eex_findings.md SECTION 1)

Falsifiable content of a posed contract: (T1) the soundness implication —
a certificate satisfying every posed clause at a row where exact ground
truth violates the (scaled) endpoint kills the pose; (T2) non-vacuity —
the six items must be simultaneously satisfiable by an honest certificate
at exact rows, with truth-matching verdicts on BOTH sides (fail-closed);
(T3) consistency with the banked facts the pose leans on.

Toy model = the repo's own exact conventions (A1_PROD_NORM_SIEVE.md +
modal_dli_orbit_census.py): level (n'=2N, L), admissible q = 1 mod n',
pinned omega = g^((q-1)/n') (g smallest primitive root), kernel = ternary
d != 0 with D(omega^(2l-1)) = 0 mod q for l = 1..L, W_cov = sum 2^-w over
the window [L+1, w_cov], signed-shift orbits with quantum 2N. Two
pre-registered thresholds per row: T=1 (production analog) and
T_mf = 2*MF (mean-field-scaled; pre-run amendment 1, fixed before running).

Kill lines: K1 (an abuse no posed clause blocks that certifies a false
endpoint), K2 (items conflict at an exact row / verdict-truth mismatch /
false ACCEPT), K3a (Vandermonde floor break), K3b (A1-PROD Markov band
violation), K3c (orbit-quantum break), K3d (banked census mismatch).

Cells: A (n'=16, FULL exhaustive, 34 primes x L=1,2,3, incl. the
mission-flagged 17/97), B (n'=32, MITM-exact, 73 primes x L=1,2, incl.
banked F2b row 8353), C (n'=64, Modal, the four banked exceptional rows
193 / 7937 / 110849 / 204353), the 8-abuse battery in two threshold
configs, and the A1-PROD Markov replay over 54 dyadic band cells.

## 3. PER-CELL EXACT RESULTS

### Abuse battery (q=97, n'=16, schedule L=[1,2,3]; truth = 15/8 exactly)
All 8 abuses REJECTED in both configs, each by the toy check implementing
exactly the posed clause pre-registered as its blocker:
A1 ledger truncation -> "complete...checkable completeness proof";
A2 halved orbit size -> "exact multiplier-shadow...de-duplication";
A3 residual class omitted -> "for every unlisted weight/frequency class";
A4 residual understated -> "independently checkable";
A5 reserve double-charge -> "aggregate reserve charged once";
A6 float boundary -> "exact rational final check" (demo: at T' = truth -
2^-80, binary64 WOULD accept, exact rational rejects — the clause is
load-bearing); A7 wrong-order omega -> item-1 pin/order certificates;
A8 "likely_nonexceptional" tag -> the explicit rejected-type list.
Honest cert: tight (certified total == exact truth), ACCEPT at T=4,
fail-closed REJECT at T=1 and at T=truth/2. The T=1 config is the sharp
one: truth EXCEEDS the threshold, so any under-pricing abuse escaping its
item clause would flip REJECT->ACCEPT via item 6 — none did.

### CELL A (n'=16, N=8, exhaustive over all 6560 ternary d; 102 row-cells)
Zero kill lines. Direct-vs-MITM cross-validation PASS (q=17, 97). Floor
K3a holds everywhere. Verdict == exact truth at all 102 rows x 2
thresholds. Band structure: L=1 top-3 by W_cov = q=17 (14.0625), q=97
(1.875), q=113 (1.375); at L=2 the ONLY nonzero window mass in the band is
q=17 (0.25); at L=3 the band is empty.

### CELL B (n'=32, N=16, MITM exact; 146 row-cells)
Zero kill lines. Honest certs tight, verdict == truth at 146 x 2
thresholds. REJECT(T=1) = 74 (small-q side, as mean-field predicts);
REJECT(T_mf) = 0 — W_cov tracks mean-field across the band (q=97: 404.25
vs MF 403.98; banked F2b row q=8353: 4.25 vs MF 4.69, min_w=6,
fail-closed REJECT at T=1, ACCEPT at T_mf).

### CELL C (n'=64, N=32, Modal runs ap-hL4dnQo2VwRUPdP1k8frYk and
### ap-YTnp5iwRlH6Uhhyiq8j4rU; w_cov=6)
| q | W_cov | MF | W/MF | T1 | Tmf | banked replay |
|---|---|---|---|---|---|---|
| 193 | 5978 | 5953.29 | 1.004 | REJECT | ACCEPT | w3/w4/w5 orbits 3/46/529 == banked primitive EXACTLY |
| 7937 | 334 | 144.76 | 2.31 | REJECT | REJECT | 2/8/31 == banked EXACTLY |
| 110849 | 22 | 10.37 | 2.12 | REJECT | REJECT | w<=5 orbits 4 == banked n_gens |
| 204353 | 75 | 5.62 | 13.3 | REJECT | REJECT | w<=5 orbits 10 == banked n_gens; k_indep 7 <= 10 |
Banked W_cl arithmetic replays: 5763 = 24+184+1058+4497 (q=193),
236 = 16+32+62+126 (q=7937); my w=6 totals (4712, 224) exceed banked
primitive (4497, 126) by exactly the imprimitive multiplier-shadow mass —
the object item 3 exists to price. All counts orbit-quantized (divisible
by 2N=64); quantum exactly 64 on every ledger rep. Honest certificates
instantiated all six items at all four banked exceptional rows; coverage
at T=1 is honestly answered NO there by REJECT — never by a false ACCEPT.

FIRED-AND-RETRACTED LINE (full trail in eex_findings.md RUN 5): the first
CELL C run fired the pre-registered K3d floor "w5 orbits >= banked k" at
q=204353 (6 < 7). Audit of band_census_and_clusters.json showed the banked
k_indep counts independent components across the WHOLE w<=5 window after
multiplier-dilation clustering (204353: n_gens=10 = my total w<=5 orbits
1+3+6, z_rank=9, k_indep=7 <= 10; 110849: n_gens=4 = my 4 w5-orbits). The
floor was a runner-side misread of the banked convention — retracted, NO
catch against the banked census; the corrected checks (RUN 6) all PASS and
the banked censuses replay exactly.

### A1-PROD Markov replay
54 dyadic band/threshold cells (n'=16 and 32; T in {1, 1/4, max observed}),
each an exact-integer check of #{q: W_cov >= T} <= TOTAL(w_cov)/T.
ZERO violations.

Totals: 524 certificate verifications (508 honest across 252 exact
row-cells x 2 thresholds + the battery row and fail-closed demos; 16
adversarial), 0 soundness violations, 0 verdict-truth mismatches.

## 4. OUTCOME — **SURVIVED** (round 1 for ENDPOINT-EXC)

No kill line stands. K1: not fired (8/8 abuses blocked by explicit posed
text, both configs). K2: not fired (six items simultaneously satisfiable
at 252 exact row-cells including the four banked exceptional rows and the
mission-flagged 17/97; verdicts truth-matching on both sides; fail-closed
demonstrated at engineered thresholds and at banked exceptional rows).
K3a/K3b/K3c: not fired. K3d: one line fired on a runner-side misread,
retracted by audit; corrected checks pass with EXACT banked replays.

**The F-round state becomes 1/1/1** (C2'' 1, C1' 1, ENDPOINT-EXC 1). Per
the node-pinned F-round rule, the dli amber attempt now needs ONLY:
- **M4 — the assembly verifier** (exact-rational, fail-closed; per catch
  #163 it must expose BOTH the coverage input and the C2''-instance input),
- **M5 — the 2^121 maintainer confirmation one-liner** (catch #40 re-pin;
  the head repair is banked, the maintainer's one-line confirmation is the
  outstanding item).

Honest attempt-limits (pre-registered as non-falsifiers, restated): the
round is exact at toy scale n' <= 64; the PRODUCTION coverage obligation
remains open — that is the pose's own explicit status, not a round result;
the joint/tower dimension of W_cen was exercised structurally (item-5
ownership/reserve-once) and pinned textually (catch #163), not mechanized
— the joint content is C2''s own lane (its M1 round survived 2026-07-13).

## 5. CATCHES AND FINDINGS (details in eex_findings.md SECTION 3)

- **CATCH #162** (dag.json, dli node statement, wave-4 custody merge): a
  TORN DUPLICATE of the M1 round record sits inside the wave-4 paragraph
  (resumes mid-token "==gridDP PASS"; 'F-a NOT FIRED at either depth' x2,
  "C2''s F-round count: 0 -> 1" x2). No conclusion flips. Surgery: delete
  the duplicated fragment from the wave-4 paragraph (maintainer edit).
- **CATCH #163** (M3 precision pin owed): item 5's verification semantics
  must be pinned — the C2'' ownership ledger must be VERIFIED per-row or
  consumed as a wired proved predicate; consistency-only item-5 checking
  makes the displayed unconditional soundness implication conditional on
  C2''. One-sentence surgery in M3; M4 must expose the C2''-instance as an
  input alongside coverage.
- **FINDING F-1**: cross-lane exceptional-prime transfer — the a3 lane's
  (16,3) exceptional set {7,17,97} restricted to admissible primes is
  {17,97}, which are EXACTLY the two heaviest DLI-ledger rows of the n'=16
  band (null ~0.09%). Follow-up suggested: same rank test at n'=32 vs S(h).
- **FINDING F-2**: exceptionality is weight-graded — q=193 is 1.004x
  mean-field in aggregate yet carries the F_193 low-weight structure
  (3 w3-orbits); q=204353 is 13.3x aggregate. Aggregate-only certificates
  would misclassify q=193; the posed ledger-first item order handles both.
- **FINDING F-3**: the six-item list is irredundant — each item was the
  sole item-level blocker for at least one battery abuse; deleting any one
  admits a wrong-field, under-priced, or rounding-corrupted certificate.

## 6. REPLAY

Local cells (each < 60 s under the tiny profile):
```
tools/ramguard tiny -- python3 <scratchpad>/eex_verify.py ABUSE
tools/ramguard tiny -- python3 <scratchpad>/eex_verify.py CELL_A
tools/ramguard tiny -- python3 <scratchpad>/eex_verify.py CELL_B
tools/ramguard tiny -- python3 <scratchpad>/eex_verify.py MARKOV
```
Modal cell:
```
tools/ramguard modal -- ~/.venvs/modal/bin/modal run \
  tools/modal_run_script.py --script <scratchpad>/eex_verify.py \
  --args "CELL_C"
```
Exit code 0 = no kill line; the script prints per-cell exact results and
an EEX_VERDICT line. The banked M3 static audit
(`notes/verify_m3_endpoint_contract.py`) was re-run this round: PASS 11/11.

---

> CROSS-REFERENCE (2026-07-13, wave-6): the coverage pose verified here
> was found CIRCULAR as a decomposition target (certificate item 6
> already checks the 2^121 endpoint; universal coverage implies B-WEAK —
> w6-C4 = catch #181). The posed successor decomposition routes through
> dli_wcl_zone_coverage (W_cl <= 1/32, all 34 levels) +
> dli_marginal_baseline100_coverage + dli_c2pp_joint_reserve; see
> M3_ENDPOINT_EXCEPTION_COVERAGE.md "M3 CORRECTED POSE". This round's
> execution record and the #165-repaired verifier remain the banked M4
> interface of record.
