# ENDPOINT-EXC adversarial round — findings log (incremental, content-ordered)

Runner: fresh-context falsification runner, 2026-07-13.
Repos READ-ONLY. All compute wrapped in tools/ramguard (tiny local / modal via
tools/modal_run_script.py). Catch ledger enters at #161.

---

## SECTION 0 — the posed claim (extracted BEFORE attack design)

Source of the pose (wave-4 import, Codex 5b436aa custody-merged per #104/#120):
`/home/u2470931/smooth-read-solomin/prize/critical/nodes/dli_prime_weighted_large_block_support/notes/M3_ENDPOINT_EXCEPTION_COVERAGE.md`
Static contract audit: `notes/verify_m3_endpoint_contract.py` (same dir).
DAG head paragraph (dli node, wave-4): "M3 AUDIT: ENDPOINT-EXC is truth-apt
only as universal per-row certificate coverage; A1 density and engineering
hardness do not discharge it. Coverage is posed and OPEN. M4 may compile only
a fail-closed implication with this coverage exposed as an input; no route
surgery is justified."

The pose, verbatim (the six certificate items):

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

Soundness (verbatim): `VERIFY_ENDPOINT_EXC(R,pi_R)=ACCEPT ==> q^{-t+H} W_cen(R) <= 2^121.`
Coverage (verbatim): `for every official row R, there exists pi_R such that
VERIFY_ENDPOINT_EXC(R,pi_R)=ACCEPT. (ENDPOINT-EXC-COVERAGE)`
Rejected certificate types (verbatim): "'No explicit construction is known,'
'the row is likely nonexceptional,' and PPT/engineering hardness are rejected
certificate types." Scope: "every official code row, not a density-one or
deployer-selected set". Nonclaim: "A1-PROD does not discharge this obligation."
Status in the pose itself: coverage "is therefore posed but open"; soundness
without coverage "is only a conditional checker".

WHAT IS FALSIFIABLE in a posed contract (fixed before any run):
- (T1) the SOUNDNESS IMPLICATION: the 6-item list, satisfied literally, must
  arithmetically entail the endpoint inequality. A certificate that satisfies
  every posed clause at a row where exact ground truth violates the (scaled)
  endpoint = falsifier.
- (T2) NON-VACUITY: at exact rows (including banked exceptional/accident rows)
  an honest, complete certificate must be constructible and the verifier's
  verdict must match exact ground truth on BOTH sides (ACCEPT at good rows,
  REJECT at rows over the threshold — fail-closed). If the six items conflict
  at some exact row even with full enumeration in hand, the contract is
  vacuous = falsifier.
- (T3) CONSISTENCY with the banked facts the pose leans on: the Vandermonde
  floor (no kernel vectors of weight <= L), the A1-PROD band Markov count,
  the 2N orbit-quantum convention, the banked orbit censuses at q=193/7937.
NOT falsifiers (the pose says these itself): production-scale coverage being
open; A1-PROD being density-only; the 2^121 constant's maintainer status (M5).

## SECTION 1 — pre-registered attack design (fixed BEFORE any run)

Toy model = the repo's own exact conventions (A1_PROD_NORM_SIEVE.md +
modal_dli_orbit_census.py): level (n'=2N, L), admissible prime q = 1 mod n',
pinned omega = g^((q-1)/n') with g the SMALLEST primitive root; kernel
K_q = {ternary d in {-1,0,1}^N, d != 0 : D(omega^(2l-1)) = 0 mod q, l=1..L};
W_cov(q) = sum over d in K_q, L+1 <= w(d) <= w_cov, of 2^-w(d) (elementwise);
orbit = signed-shift class under t (t^N = -1), claimed quantum 2N.
Toy endpoint analog: threshold T=1 (the A1-PROD production threshold analog).
The toy round tests the CONTRACT'S LOGIC (item composition => inequality,
fail-closed behavior, clause coverage of abuses); the production constant
2^121 is M5's item, not this round's.

### Attack axis 1 (T1): the ABUSE BATTERY — 8 adversarial certificates
Each abuse mutates an honest certificate. Scored TWO ways: (i) TEXT AUDIT —
which posed clause, quoted, blocks it; if NO clause blocks it and the mutated
certificate still satisfies every posed clause while ground truth violates
the threshold, KILL LINE K1 fires. (ii) MECHANIZED — the faithful toy
verifier must REJECT it (and must ACCEPT the honest certificate).
- A1 ledger truncation: drop one orbit from the item-2 ledger, keep the
  completeness claim.
- A2 dedup abuse: report a listed orbit's size as N instead of the true 2N
  (under-prices the shadow mass by half).
- A3 residual-class omission: omit one weight class from item 4's residual
  certificates.
- A4 residual understatement: submit a FALSE (too small) residual upper
  bound U_w with a well-formed proof tag.
- A5 reserve double-charge: subtract the aggregate reserve allowance in two
  different buckets of the item-5 ownership ledger.
- A6 float boundary: perform item 6's final check in binary64 at an
  engineered boundary where float says <= and exact rational says >.
- A7 field/order pin abuse: present omega of order n'/2 (or a mismatched
  evaluation-field declaration) so every count is taken in the wrong field
  (catch-#13 beta-clause shape).
- A8 rejected-type smuggling: price a residual class with proof type
  "likely_nonexceptional" / "ppt_hardness".
KILL LINE K1: any abuse that (a) no posed clause blocks (text), AND (b) leads
to ACCEPT with ground truth > threshold. => FALSIFIER FIRED.

### Attack axis 2 (T2): coverage/vacuity instantiation at exact rows,
### INCLUDING banked exceptional primes
- CELL A (n'=16, N=8; FULL exhaustive ground truth over all 3^8-1 = 6560
  ternary d; w_cov = 8): band q = 1 mod 16, q <= 2000; L in {1,2,3}.
  Includes the mission-flagged pair q=17, q=97 (the (16,3) exceptional set
  from the a3/dichotomy lane is banked as {7,17,97} in
  background/nodes/a3_good_reduction_lemma/statement.md — 7 is inadmissible
  here (7 != 1 mod 16); test whether 17/97 are exceptional for THIS object).
- CELL B (n'=32, N=16; exact ground truth via grouped meet-in-middle on
  halves 3^8; w_cov = 8): band q = 1 mod 32, q <= 10000; L in {1,2}.
- CELL C (n'=64, N=32; w_cov = 6; grouped MITM with half-weight <= 6,
  686,401 half-vectors; orbit ledger by direct enumeration w <= 4; Modal):
  the four banked exceptional/accident rows q=193 (banked: 3 primitive w=3
  orbits, W_cl = 5763/1), q=7937 (banked: 2 primitive w=3 orbits, M2's
  worst K' = 0.246909432, M1's V_orbits=2), q=110849 (banked k=4 cluster),
  q=204353 (banked k=7 cluster, the F-round's worst row).
At every cell row: construct the HONEST certificate (completeness realized
by exhaustive re-enumeration — legitimate at toy scale; at production scale
this is exactly the open obligation, per the pose itself), run the verifier,
compare with independently computed exact ground truth.
FAIL-CLOSED demonstration: at rows/thresholds where exact W_cov > T the
verifier must REJECT every certificate including the honest one.
KILL LINE K2: at >= 1 exact admissible row the six items cannot be satisfied
simultaneously by the honest full-enumeration certificate (items conflict),
OR an honest ACCEPT occurs at a row with ground truth > T, OR a REJECT
occurs at a row with ground truth <= T whose certificate is honest and
complete. => FALSIFIER FIRED.

### Attack axis 3 (T3): banked-fact cross-checks (exact)
- K3a Vandermonde floor: at every tested row and level, the minimum kernel
  weight must be >= L+1. Any kernel vector of weight <= L => FALSIFIER
  (breaks the pose's ledger scoping AND banked A1 material).
- K3b A1-PROD Markov band replay at toy scale: on dyadic bands, exact count
  of admissible q with W_cov >= T must be <= TOTAL(w_cov)/T
  (TOTAL = sum C(N,w) * D_cap(w), D_cap exact). Any violation => FALSIFIER
  against the banked theorem.
- K3c orbit quantum: every nonzero orbit size must be EXACTLY 2N (the
  Z[t]/(t^N+1)-is-a-domain argument, n' a power of two; mechanically
  verified on every ledger rep). A nontrivial stabilizer => catch against
  the banked quantum convention + item-3 certificates that assume it.
- K3d census replay: my total w=3 orbit counts at q=193/7937 (N=32, L=1)
  must EQUAL the banked primitive counts 3 and 2 (weight-3 kernel orbits
  are automatically primitive: the only lower-weight vanishers would have
  weight 2, and weight-2 vanishers are impossible — omega has exact order
  n' on reduced exponents). w=4 totals must be >= banked primitive counts
  (46 and 8). Cluster rows: total w=5 orbit count >= banked k (4 and 7).
  Mismatch below these floors => catch.

### Pre-registered reads (before any run)
- R1: the abuse battery — EXPECT all 8 blocked by explicit posed text (the
  pose looks well-armored; each clause names its abuse). If so, axis 1
  survives and the finding is "clause coverage complete for the battery".
- R2: CELL A/B bands — EXPECT typical rows W_cov << 1 (ACCEPT at T=1), with
  heavy rows possible at tiny q; EXPECT q=17 (N=8) plausibly heavy (tiny q,
  dense kernel). Whether 17/97 are exceptional HERE is genuinely open —
  either answer is a banked result cell.
- R3: CELL C — EXPECT q=193 and q=7937 to carry their banked w=3 orbits
  exactly (K3d); EXPECT the cluster rows' W_cov(w<=6) to be dominated by
  their banked w=5 clusters (~2 per orbit at 64*2^-5); q=204353 with k=7
  may well EXCEED T=1 => the fail-closed REJECT demonstration on a BANKED
  row (coverage honestly failing at an exceptional row is the pose working,
  not a falsifier — the pose never claims coverage holds).
- R4: item-5 reading pin (TEXT finding, fixed now): the pose's item 5
  admits two readings — (R-verify) the ownership ledger VERIFIES the joint
  accounting per-row (unconditional soundness, high coverage cost), vs
  (R-assume) the ledger ASSUMES C2''s 21-bit reserve (soundness then
  conditional on C2'', contradicting the unconditional soundness
  implication as posed). The toy verifier implements R-verify; the round
  pins R-verify as the only reading under which the posed soundness
  implication is true as stated. If any banked text asserts R-assume
  together with unconditional soundness, that is a catch.

### Kill lines (all pre-registered above): K1, K2, K3a, K3b, K3c(=catch), K3d(=catch).

### PRE-RUN AMENDMENT 1 (design parameter, fixed BEFORE the first run)
At toy q the T=1 threshold analog sits BELOW the mean-field window mass
(exact mean-field MF(q,L) = sum_{w=L+1}^{w_cov} C(N,w)/q; at N=16, band
q <= 10^4, MF is 4..400 — every CELL B row would sit on the REJECT side).
To exercise the verdict/truth-match kill line K2 on BOTH sides at every
cell, each row is scored at TWO pre-registered thresholds: T = 1 (the
A1-PROD production analog) AND T_mf = 2*MF(q,L) (mean-field-scaled).
The abuse battery likewise runs in two configs: T = 1 (at the battery row
the truth exceeds T — the dangerous flip-risk configuration where an
under-pricing abuse could flip REJECT->ACCEPT; the item-level clauses must
catch it) and T = 4 (honest-ACCEPT baseline configuration). No reads are
changed; this is threshold placement only.

---

## SECTION 2 — run log and results (appended in content order below)

### RUN 1 — ABUSE battery (ramguard tiny, q=97 n'=16 schedule L=[1,2,3])
Honest cert: tight (certified total == exact ground truth 15/8 = 1.875),
ACCEPT at T=4, fail-closed REJECT at T=1 and at T=truth/2.
ALL 8 abuses REJECTED in BOTH configs, each caught by the toy check
implementing exactly the posed clause pre-registered as its blocker:
  A1 ledger truncation      -> item2:ledger_incomplete_or_spurious
  A2 dedup halved orbit     -> item3:orbit_size_not_exact
  A3 residual class omitted -> item4:unlisted_class_missing
  A4 residual understated   -> item4:residual_bound_false
  A5 reserve double charge  -> item5:reserve_charged_more_than_once
  A6 float boundary         -> item6:not_exact_rational
     (boundary demo: at T' = truth - 2^-80, binary64 WOULD accept,
      exact rational rejects — the "exact rational" clause is load-bearing)
  A7 wrong-order omega      -> item1:omega_pin + item1:omega_order
  A8 rejected-type smuggle  -> item4:rejected_certificate_type
TEXT AUDIT: every battery abuse is blocked by explicit posed text; no abuse
found that satisfies all six clauses while breaking the endpoint. K1 axis:
NOT FIRED. Note the sharp config: at T=1 the truth EXCEEDS the threshold, so
any under-pricing abuse that escaped its item clause would have flipped
REJECT->ACCEPT through item 6 — none did.

### RUN 2 — CELL A (ramguard tiny; n'=16, N=8, FULL exhaustive; 34 primes
### x L=1,2,3 = 102 rows; w_led=5, w_cov=8; both thresholds)
- Cross-validation direct-enumeration == MITM at q=17, 97: PASS.
- K3a floor: min kernel weight >= L+1 at every row (q=17 L=1: min_w=3).
- K2: verdict == exact truth at ALL 102 rows x 2 thresholds; honest certs
  tight everywhere; ZERO kill lines.
- EXCEPTIONAL-PRIME CROSS-LANE FINDING: at L=1 the band's top-3 by W_cov are
  q=17 (14.0625), q=97 (1.875), q=113 (1.375); at L=2 the ONLY nonzero
  window mass in the whole band is q=17 (0.25); at L=3 the whole band is 0.
  The a3/dichotomy-lane exceptional set at (16,3) is banked as {7,17,97}
  (background/nodes/a3_good_reduction_lemma/statement.md); its admissible
  members (q = 1 mod 16) are EXACTLY {17, 97} — which are EXACTLY the two
  heaviest DLI-object rows of the band (top-2 of 34; null probability
  ~1/(34*33) ~ 0.09%). Cross-lane exceptional structure TRANSFERS at n'=16.
  (Finding, not a falsifier; see catch section.)

### RUN 3 — CELL B (ramguard tiny; n'=32, N=16, MITM exact; 73 primes x
### L=1,2 = 146 rows; w_led=4, w_cov=8; both thresholds)
- ZERO kill lines; honest certs tight and verdict==truth at all 146 rows x 2
  thresholds. REJECT(T=1)=74 (small q side, as mean-field predicts),
  REJECT(Tmf=2*MF)=0 — W_cov tracks mean-field tightly across the band
  (e.g. q=97: 404.25 vs MF 403.98; q=8353: 4.25 vs MF 4.69).
- Banked F2b row q=8353: W_cov=4.25 (min_w=6), fail-closed REJECT at T=1,
  ACCEPT at Tmf — certificate instantiable, verdict truthful, both sides.

### RUN 4 — A1-PROD Markov band replay (ramguard tiny)
54 dyadic band/threshold cells (n'=16 bands 2^4..2^10 x L=1,2; n'=32 bands
2^5..2^13 x L=1), each an exact-integer check of
#{q in band: W_cov >= T} <= TOTAL(w_cov)/T at T in {1, 1/4, max observed}.
ZERO violations. K3b: NOT FIRED.

### RUN 5 — CELL C first run (Modal; ap-hL4dnQo2VwRUPdP1k8frYk) — one
### pre-registered kill line FIRED, then RETRACTED BY AUDIT (full record)
Exact results (n'=64, N=32, L=1, w_cov=6, MITM half-weight<=6 + direct
w<=4 enumeration; verdicts at T=1):
  q=193    W_cov=5978  hist{3:192, 4:2944, 5:33856, 6:301568}  w3_orbits=3
  q=7937   W_cov=334   hist{3:128, 4:512,  5:1984,  6:14336}   w3_orbits=2
  q=110849 W_cov=22    hist{5:256, 6:896}                      w3_orbits=0
  q=204353 W_cov=75    hist{3:64,  4:192,  5:384,   6:2752}    w3_orbits=1
- K3d fired at q=204353: "w5 orbits (6) < banked k (7)".
- AUDIT (band_census_and_clusters.json, cluster_204353 / cluster_110849):
  the banked cluster row records n_gens=10, z_rank=9 at 204353 and n_gens=4
  at 110849; the F-round table's k_indep (7 and 4) counts INDEPENDENT
  COMPONENTS across the WHOLE w<=5 window after multiplier-dilation
  clustering — NOT w5 orbits alone. My pre-registered floor misread that
  convention. The audited comparison: my total w<=5 orbit count at 204353 =
  1 + 3 + 6 = 10 == banked n_gens EXACTLY; at 110849 = 4 == banked n_gens
  EXACTLY; k_indep = 7 <= 10 consistent (clustering collapses 10 -> 7).
- VERDICT ON THE FIRED LINE: runner-side misregistration, retracted; NO
  catch against the banked census. Replaced (in eex_verify.py cell_C, with
  an in-code note) by the audited equalities. The retraction is recorded
  here in full per protocol; the first-run log is preserved above.
- What the first run DID establish (independent of the misread):
  - w3/w4 orbit counts at q=193: 3/46 == banked primitive counts EXACTLY
    (m2_c1prime_level_scaled_results.json); w5: 33856/64 = 529 == banked;
    at q=7937: 2/8/31 == banked EXACTLY. All w<=5 vanishers at these rows
    are primitive (total == primitive), and the banked W_cl arithmetic
    replays: 5763 = 24+184+1058+4497 at 193; 236 = 16+32+62+126 at 7937,
    with my w=6 totals (4712, 224) exceeding banked primitive (4497, 126)
    by exactly the imprimitive (multiplier-shadow) w=6 mass — the object
    item 3 exists to price.
  - All four banked exceptional rows: honest certificates instantiate all
    six items, verdict fail-closed REJECT at T=1 (their W_cov = 5978, 334,
    22, 75 all exceed 1) — the coverage-at-T=1 question honestly answered
    NO at exceptional rows by REJECT, never by false ACCEPT.
  - K3a floor held; orbit quantum exactly 2N=64 on every ledger rep (K3c).

### RUN 6 — CELL C corrected re-run (Modal; ap-YTnp5iwRlH6Uhhyiq8j4rU;
### exit 0) — ZERO kill lines
Audited K3d checks + Tmf scoring added:
  q=193    W=5978 MF=5953.29 (1.004x) T1:REJECT Tmf:ACCEPT  w3/w4/w5 orbits
           3/46/529 == banked primitive EXACTLY
  q=7937   W=334  MF=144.76  (2.31x)  T1:REJECT Tmf:REJECT  2/8/31 == banked
  q=110849 W=22   MF=10.37   (2.12x)  T1:REJECT Tmf:REJECT  w<=5 orbits 4 ==
           banked n_gens
  q=204353 W=75   MF=5.62    (13.3x)  T1:REJECT Tmf:REJECT  w<=5 orbits 10 ==
           banked n_gens; k_indep 7 <= 10 consistent
All counts orbit-quantized (divisible by 2N=64); quantum exact on every
ledger rep; verdict==truth at both thresholds at all four rows; honest
certificates instantiated all six items at every row. STRUCTURE FINDING
(F-2 below): q=193's exceptionality is entirely low-weight/graded (aggregate
1.004x mean-field but 3 w3-orbits and ACCEPT at Tmf), while the cluster row
q=204353 is aggregate-exceptional (13.3x). The pose's ledger-first design
(item 2 windows before aggregate thresholds) is exactly what distinguishes
these — an aggregate-only certificate would misclassify q=193.

### RUN 0 (anchor, run after the cells as confirmation) — the banked M3
### static contract audit
tools/ramguard tiny -- python3 critical/nodes/dli_prime_weighted_large_block_support/notes/verify_m3_endpoint_contract.py
=> status PASS, 11/11 checks (universal scope, soundness implication,
2^121 endpoint, coverage named, completeness + residual required,
engineering rejected, density-not-individual, source denies exhaustive
certificate, no endpoint node wired, dli stays TARGET).

---

## SECTION 3 — catches (#162+) and findings

### CATCH #162 (statement hygiene, dag.json dli node, wave-4 custody merge)
The wave-4 paragraph of dli_prime_weighted_large_block_support's statement
contains a TORN DUPLICATE of the M1 round record: after "binding new content
follows, full text in the node folder):" the text resumes MID-TOKEN with
"==gridDP PASS; full log banked at notes/m1_run_record_20260713.log): F-a
NOT FIRED..." — a verbatim copy of the earlier M1 ROUND SURVIVED block torn
at "shard-0 gate + xcheck MITM==gridDP PASS". Mechanically verified:
'F-a NOT FIRED at either depth' x2, "C2''s F-round count: 0 -> 1" x2,
'pending maintainer review' x2, '==gridDP PASS' x2 with 'MITM==gridDP PASS'
x1 (the second occurrence is the torn head). No conclusion flips; the M2/M3
content that follows the duplicate is intact. SURGERY: delete the duplicated
fragment from "==gridDP PASS; full log banked" through "...pending
maintainer review. " inside the wave-4 paragraph (leave the original M1
paragraph untouched). Maintainer edit; repo read-only for this runner.

### CATCH #163 (precision pin owed on the M3 pose, item 5 / soundness display)
M3 displays soundness as the unconditional implication
"VERIFY_ENDPOINT_EXC(R,pi_R)=ACCEPT ==> q^{-t+H} W_cen(R) <= 2^121" while
item 5 requires only "the C2'' coset/bulk/accident ownership ledger, with
the aggregate reserve charged once". Items 2-4 price PER-LEVEL ledger mass;
the bridge from per-level ledgers to the JOINT object W_cen is exactly the
C2''(+C1') content. If an implementation reads the six items as sufficient
and checks item 5 as CONSISTENCY-ONLY (the ledger is well-formed and
C2''-shaped), then ACCEPT implies the endpoint only conditional on C2'' —
contradicting the unconditional display. M3's own closing paragraph ("M4 may
still prove the exact arithmetic implication from accepted C1', C2'', and
endpoint certificates") already carries the conditional structure, so this
is a precision gap, not a substantive error. SURGERY (one sentence in M3):
pin item 5's verification semantics — the ownership ledger must either be
VERIFIED per-row (exact joint accounting, as this round's toy verifier
does by full enumeration) or consume C2'' as a wired proved predicate;
assumption-only item-5 content is a REJECT. Until C2'' is proved, M4's
assembly must list the C2''-instance as an exposed input ALONGSIDE coverage
(M3 currently names only coverage in its fail-closed clause).

### FINDING F-1 (cross-lane exceptional-prime transfer; positive evidence,
### not a catch)
The a3/dichotomy lane's exceptional set at (16,3) is banked as {7,17,97}
(a3_good_reduction_lemma; biconditional, brute-force both directions). Its
admissible members mod 16 are {17,97} — and this round finds they are
EXACTLY the two heaviest DLI-ledger rows of the entire n'=16 band
(L=1 top-3: 17 at 14.0625, 97 at 1.875, 113 at 1.375; at L=2 q=17 carries
the band's ONLY nonzero window mass). Null probability of hitting top-2 of
34 ~ 0.09%. Suggests the two lanes' exceptional structures share an
arithmetic source (small multiplicative-order coincidences of the pinned
omega); a cheap follow-up: run the same rank test at n'=32 against S(h)
divisor sets.

### FINDING F-2 (weight-graded exceptionality; supports the pose's design)
q=193 at n'=64: aggregate W_cov = 1.004x mean-field yet 3 weight-3 orbits
(the F_193 phenomenon is invisible to aggregate thresholds); q=204353:
13.3x mean-field aggregate. A certificate rule with aggregate-only checks
would misclassify q=193; the posed ledger-first item order (2 -> 4 -> 6)
distinguishes both correctly in this round's runs.

### FINDING F-3 (irredundancy of the six-item list)
In the abuse battery each item was, for at least one abuse, the SOLE
item-level blocker (item1<-A7, item2<-A1, item3<-A2, item4<-A3/A4/A8,
item5<-A5, item6<-A6). Deleting any single item from the pose admits at
least one certificate that is wrong-field, under-priced, or
rounding-corrupted. The six-item list is minimal in this battery's sense.

---

## SECTION 4 — ROUND VERDICT

ENDPOINT-EXC as posed: **SURVIVED round 1** (this round).
- K1 (soundness hole): NOT FIRED — 8/8 abuses blocked by explicit posed
  text in both threshold configs, including the flip-risk config where
  truth exceeds the threshold; no accepting certificate ever coexisted with
  ground truth above its threshold (524 certificate verifications total
  across cells A/B/C + battery — 508 honest, 16 adversarial: 0 soundness
  violations).
- K2 (vacuity/conflict): NOT FIRED — honest certificates instantiated all
  six items at 102 + 146 + 4 = 252 exact row-cells including the four
  banked exceptional rows and both mission-flagged primes 17/97; verdicts
  matched exact ground truth at every row at both thresholds; fail-closed
  REJECT demonstrated at engineered thresholds AND at the banked
  exceptional rows.
- K3a floor / K3b Markov / K3c quantum: NOT FIRED (0 violations anywhere).
- K3d census replay: one line fired on a runner-side misread of the banked
  k_indep convention, retracted by audit (RUN 5), corrected checks all
  PASS (RUN 6) — the banked censuses replay EXACTLY.
F-round state: C2'' 1, C1' 1, ENDPOINT-EXC 0 -> **1** (1/1/1). Per the
node-pinned F-round rule the dli amber attempt now needs only:
  M4 — the assembly verifier (exact-rational, fail-closed, with coverage
       AND the C2''-instance exposed as inputs per catch #163), and
  M5 — the 2^121 maintainer confirmation one-liner (catch #40).
Catches owed to the ledger: #162 (dag statement torn duplicate),
#163 (item-5 verification-semantics pin).
Attempt-limits stated honestly: toy scale n'<=64 exact; the production
coverage obligation remains OPEN (the pose itself says so — not scored);
the joint/tower dimension of W_cen was exercised structurally and pinned
textually (item 5), not mechanized (that is C2''s own lane, M1 survived).
