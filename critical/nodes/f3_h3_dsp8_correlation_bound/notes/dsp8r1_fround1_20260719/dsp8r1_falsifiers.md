# DSP8 F-ROUND 1 — pre-registered falsifier instantiation

Date: 2026-07-19. Worker: fresh-context falsification worker (read-only in
the repo; all artifacts under scratchpad prefix `dsp8r1_`).

Predicate under attack: `f3_h3_dsp8_correlation_bound` (TARGET, minted
2026-07-19; req ROUTE OF RECORD of the C36 amber
`critical/nodes/f3_h3_mobius_excess_half/conditional.md`).

    At every official row in n^2 <= p <= 6^{n/4}:
        10*J_25^0 + 17*J_25^A <= 892*n^2.

Written BEFORE any computation, per the pre-registration discipline.

## 0. Pinned definitions (#137 normalization discipline — reused verbatim
from the provenance chain, no re-derivation)

Sources of record:

- `background/nodes/f3_h3_disjoint_distance_six_split_pencil_router/`
  (statement DSP1–DSP8, proof, verify.py — wave-14, PROVED router)
- `background/nodes/f3_h3_distance_six_support_overlap_payment/statement.md`
  (DSO4: the D_6,25 class sums; DSO7 = the (223/20)n^2 form)
- `background/nodes/f3_h3_antipodal_tail_distance_six_split/statement.md`
  (antipodal target classification, A6S8/A6S10 = the cutoff-25 lane)
- `notes/kernel_basis/WAVE14_AUDIT_FINDINGS.md` (J=8D factor audited;
  "unordered-disjoint-edge x ordered-quotient records" makes it exact)

Pins:

1. **Row** (official or analogue): n = 2^s, p prime, p ≡ 1 (mod n),
   n^2 <= p <= 6^{n/4}. H = the unique order-n subgroup of F_p^*.
   Official corridor: 13 <= s <= 41. Analogue rows: same shape at small s.
2. **A** = (1−H)\{0}; **P(t)** = #{(a,b) ∈ A^2 : ab = t};
   diag(t) = #{a ∈ A : a^2 = t}.
3. **S_t** = {r ∈ H : Q_(t,r)(X) = X^2 − (1+r−t)X + r splits as (X−x)(X−y),
   x,y ∈ H\{1}}; bijection r = xy ↔ {x,y} with t = (1−x)(1−y) (DSP2);
   identity P(t) = 2|S_t| − diag(t) (DSP3) asserted on every verdict-path
   fiber.
4. **Signed half-basis support** of a representation E = {x,y}: the vector
   +xy − x − y written in the half-basis: value with discrete log e ↦
   coordinate e mod n/2, sign +1 if e < n/2 else −1 (exactly the
   `signed_support` of the router verify.py). **Generic** member: support has
   exactly 3 distinct coordinates, each coefficient ±1. G_t = generic
   members of S_t.
5. **N_6^disj(t)** = #{ {r,s} ⊆ G_t : supports disjoint } (DSP4;
   disjoint ⟺ squared distance 6, asserted on verdict-path fibers).
6. **R(t)** = #{z ∈ H\{1} : 1 − t(1−z) ∈ H\{1}} (DSP5, ordered quotient
   records).
7. **Antipodal target**: the fiber of t contains its unique antipodal
   representation {x, −x} ⊆ H\{1}, i.e. ∃x ∈ H\{±1} with x^2 = 1−t.
   Equivalent membership form: (1−t) mod p ∈ H^2 \ {1} (H^2 = squares of
   H, order n/2; n is a 2-power so −1 ∈ H). Both forms computed and
   asserted equal on every verdict-path fiber. Antipodal-free = the rest.
8. **Retained targets**: t ≠ 1 (upstream X_18 selection; A6S1 "selected
   targets t≠1"), P(t) >= 25 (the E=6 tail cutoff of DSO4/A6S8).
9. **D_6,25^0** = Σ_{t retained, antipodal-free} N_6^disj(t)·R(t);
   **D_6,25^A** = Σ_{t retained, antipodal} N_6^disj(t)·R(t);
   **J_25^c = 8·D_6,25^c** (DSP7, factor-eight audited at wave-14).
10. **LHS** = 10·J_25^0 + 17·J_25^A = 80·D_6,25^0 + 136·D_6,25^A;
    **ratio** ρ = LHS / (892·n^2). All integer arithmetic exact; the only
    rational is ρ, reported as an exact fraction where it matters.

NOT negotiable (verdict discipline): the constant 892, the weights 10/17,
the normalization J = 8D, the cutoff 25, and the t ≠ 1 selection are all
pinned. No weakening to survive; no strengthening to kill.

## (a) The analogue row family (>= 3 scales)

Pigeonhole fence (named in advance): P(t) <= |A| = n−1, so every scale with
n <= 26 has J_25 ≡ 0 identically — scales below 32 are definitionally
vacuous and are NOT used.

- **Scale n = 32 — EXHAUSTIVE FULL CORRIDOR**: every prime
  p ≡ 1 (mod 32), 1024 <= p <= 6^8 = 1679616. Complete coverage of an
  entire analogue corridor (contains the wave-14 toy fixture row
  (32, 1153)).
- **Scale n = 64**: exhaustive window p ≡ 1 (mod 64),
  4096 <= p <= 10^7, PLUS high-p sample: first 5 primes ≡ 1 (mod 64)
  above 10^11 (corridor top 6^16 ≈ 2.82e12).
- **Scale n = 128**: exhaustive window 16384 <= p <= 10^7, PLUS first 5
  primes ≡ 1 (mod 128) above 10^11.
- **Scale n = 256**: exhaustive window 65536 <= p <= 10^7, PLUS first 5
  primes ≡ 1 (mod 256) above 10^11.
- **Scale n = 8192 — OFFICIAL rows (adversarial anchor)**: the first four
  official primes p ≡ 1 (mod 8192), p >= 8192^2 = 67108864, which include
  the provenance-identified **richest known row (8192, 67657729)** (wave-5
  boundary row: max P = 20, two rich targets P=20 R=1, X_18 = 4,
  S_ns^rich = 720). This is the adversarial choice required by the round:
  the row with the richest split-pencil structure identified anywhere in
  the banked data. n = 8192 is inside the official corridor, so any kill
  here is a direct kill, not an analogue kill.

Adversarial escalation rule (pre-registered): any scanned row with
max_{t≠1, R(t)>0} P(t) >= 19 is promoted to the FULL exact measurement +
independent pure-Python big-int replay. Context from banked sweeps (7,090
rows, 64<=n<=4096: max P+2R = 32; first twelve n=8192 rows: X_35 = 0)
predicts retained targets are rare; the scan is designed to find the ones
that exist, not to assume they don't.

## (b) Kill lines + trend rule

- **KILL-1 (exact row)**: some measured row (analogue or official) has
  LHS = 80·D_6,25^0 + 136·D_6,25^A > 892·n^2, confirmed by BOTH the
  primary implementation and an independent pure-Python exact big-int
  replay of that row. Witness banked with (n, p, generator, retained
  targets, per-target P, R, N_6^disj, class, D^0, D^A, LHS).
- **KILL-2 (trend at official aspect)**: let ρ_max(n) = max over measured
  rows at scale n of LHS/(892n^2). If ρ_max is strictly monotone
  increasing across >= 3 consecutive measured scales AND the log-linear
  extrapolation of log ρ_max against log n over those scales reaches
  ρ >= 1 at some official order n = 2^s, 13 <= s <= 41, that is a trend
  kill (predicate survives the letter but the round reports KILLED-BY-TREND
  with the fit banked).
- Anything else: SURVIVED, with scope stated honestly (see NOT-kills).

## (c) NOT-kills (named in advance)

1. **Vacuous survival**: J_25 = 0 at every measured row makes SURVIVED
   vacuous at those rows — it is honest scope, not confirmation. The
   report must say so explicitly, and the banked sweep context (max P+2R
   <= 32 at 64..4096) already makes widespread vacuity the expected
   outcome. Zero rows with retained targets ⇒ flat-zero trend ⇒ KILL-2
   cannot fire vacuously.
2. **Sub-cutoff pressure**: diagnostic moments at cutoffs q < 25 (we also
   record D_6,19 and D_6,0 per row) exceeding 892n^2 are NOT kills — the
   predicate is pinned at cutoff 25; lower cutoffs are paid by other
   proved nodes (DSO5 etc.). They are recorded as diagnostics only.
3. **t = 1 richness**: P(1) can be large (Stepanov P(1) < 4n^{2/3}); t=1
   is excluded by the pinned selection. A rich t=1 fiber is never a kill.
4. **Toy rows outside the corridor** (p < n^2: the router fixture rows
   (17,8), (97,16), (193,16)): positive-control material only, never kill
   evidence.
5. **Single-scale spikes**: one structured prime raising ρ_max at one
   scale without monotone continuation across >= 3 scales does not meet
   KILL-2.
6. **Numerical artifacts**: no kill from the numpy path alone; a kill
   witness must replay in exact pure-Python big-int arithmetic. Any numpy
   row uses asserted-overflow-safe int64 (p^2 < 2^63) and is still exact;
   the replay is belt-and-braces.
7. **Vacuity by pigeonhole at n <= 26**: excluded from the family; not
   evidence either way.
8. **High-p thinning**: high-p sample rows with empty rich loci mirror
   the proved large-field branch (Parseval: P(t)>=19 ⇒ p <= 6^{n/4});
   their vacuity is expected and is not extra evidence weight.

## (d) Positive controls + mutation controls

Positive controls (banked constants reproduced exactly):

- **PC-1 (router fixture totals)**: run the node replay of record
  `tools/ramguard tiny -- python3 background/nodes/
  f3_h3_disjoint_distance_six_split_pencil_router/verify.py`, bank its
  printed `targets/edges/raw_records` totals for rows (17,8), (97,16),
  (193,16); then reproduce the same three-row totals with the dsp8r1
  census in control mode (cutoff 0, no t-exclusion, both classes merged,
  raw = 8·edges·R). REQUIRED: exact match.
- **PC-2 (wave-5 boundary row constants)**: on official row
  (8192, 67657729): reproduce max_t P(t) = 20, exactly two targets with
  P >= 19, both with R = 1, X_18 = Σ_{t≠1}(P−18)_+·R = 4, X_35 = 0.
  REQUIRED: exact match (these are banked in frontier.md / wave-5).
- **PC-3 (DSP3 identity)**: P(t) = 2|S_t| − diag(t) asserted over all
  targets on the wave-14 audit toy row (32, 1153) and on every
  verdict-path fiber.

Mutation controls (REQUIRED TO TRIP — the round is invalid if either
fails to trip):

- **MC-1 (census mutation)**: rerun PC-1 comparison with the census edge
  count offset by +1 per row. REQUIRED: PC-1 comparison FAILS.
  (Chosen because it trips even if all disjoint-edge counts are zero.)
- **MC-2 (kill-detector mutation)**: rerun the kill-line evaluation on
  the three control rows with the RHS constant 892 replaced by −1.
  REQUIRED: every row (even with LHS = 0) reports a violation, i.e. the
  kill-detection code path demonstrably fires.

## Compute plan (COMPUTE LAW)

- Local under `tools/ramguard tiny` ONLY for: PC-1 replay, control-mode
  census on the three toy rows, MC-1/MC-2.
- ALL scans + the n=8192 rows on Modal via
  `tools/ramguard modal -- ~/.venvs/modal/bin/modal run
  tools/modal_run_script.py --script dsp8r1_census_modal.py --args "..."`,
  sharded by (scale, multiplier window), each shard sized well under the
  280s ceiling; Modal app ids recorded in dsp8r1_results.md. Modal failure
  ⇒ shrink + DEFER that shard, never rescue locally.
- Scan path: pure-Python exact integers (Counter-based) for n <= 256;
  numpy int64 (overflow-asserted, exact) only for n = 8192 rows;
  cross-checked against the pure path on toy rows in the control shard.

## Verdict rule

- KILLED: KILL-1 or KILL-2 fires (witness/fit banked, reproduction
  commands in dsp8r1_results.md).
- SURVIVED: no kill line fired in the stated scope; scope stated
  honestly, including vacuity accounting (how many measured rows had any
  retained target at all).
- MIXED: controls failed or shards deferred in a way that materially
  narrows scope; reported as such with the surviving scope.
