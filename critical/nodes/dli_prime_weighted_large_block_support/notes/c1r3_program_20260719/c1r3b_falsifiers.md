# C1'-r3 F-ROUND 2 — pre-registered falsifiers (c1r3b)

- **predicate:** C1'-r3 EXACTLY as frozen in
  `critical/nodes/dli_prime_weighted_large_block_support/notes/c1r3_program_20260719/c1r3_pose.md`.
  NOTHING about the pose moves this round: gate H3 (official v_2(q-1) >= 41,
  analogue proxy v_2(q-1) >= 20 via Proth primes q = c*2^k+1, odd c, k >= 20),
  window [L+1, L+7], RAW primitive signed-shift orbit ledger W_ext with mass
  2N*2^-w per orbit, allowance 4, exact-rational verdict path, #137 discipline.
- **round-1 record of record:** same directory, `c1r3_falsifiers.md` (round-1
  pre-registration; its "Exact quantities", structural bounds (i)/(ii), and
  NOT-KILLS carry over verbatim), `c1r3_results.md` (banked exact fractions),
  `c1r3_report.md` (whose "Round-2 design sketch" THIS document instantiates).
- **written BEFORE any round-2 computation.** No DP, no enumeration, no Modal
  shard, no family enumeration has been run in this session. The only inputs
  are the banked round-1/round-2(r2) packet files read above. Date 2026-07-19.
- **mandate being executed:** the pre-registered ROUND 2 (parent-session
  mandate + the dag node `dli_dyadic_k_core` C1'-r3 PROGRAM block: "ROUND 2
  (pre-registered in c1r3_report.md): amber re-armed ABOVE the iid asymptote
  (K' >= 2) + iid-excess trend; segmented DP to 2^32 incl. the deferred row;
  L=2 at N=64").

## Exact quantities (carried verbatim, window unchanged)

```text
K'_r3 := (E-1) / ( r * (1 + W_ext) ),  W_ext over weights L+1..L+7, mass 2N*2^-w
env   := (E-1)/r        (the bare envelope; iid baseline env -> 1)
Structural bounds (exact, carried from round 1):
  (i)  K'_r3 <= env                          (W_ext >= 0)
  (ii) K'_r3 <= (E-1)/(r*(1+W_partial))      for any partial sub-ledger.
A SURVIVAL verdict may cite env or a partial ledger (upper bounds on K'_r3);
a KILL verdict at a row requires the FULL [L+1, L+7] ledger for that row.
```

## KILL LINES (frozen; verdict governed by these and nothing else)

- **KILL-LITERAL (refutes C1'-r3):** any exact in-hypothesis row (H1+H2+H3
  analogue gate) with K'_r3 > 4 on the full extended ledger. => KILLED.
  Unchanged from round 1.
- **KILL-AMBER-2 (blocks minting; does not logically refute):** any exact
  in-hypothesis row with K'_r3 >= 2 — twice the iid baseline, genuine excess
  above the established fluctuation band. => verdict MIXED. Certification
  logic: env < 2 certifies NOT tripped at that row (bound (i), no ledger
  needed); env >= 2 REQUIRES the full-ledger K'_r3 to read the line. Rationale
  (round-1 finding c1r3-C5, pre-registered here BEFORE any new scan): the
  gated bulk saturates at env -> 1; the old K' >= 1 watch line sits ON the
  asymptote and measures iid noise; the re-armed line sits 2x above the
  asymptote and 2x under the allowance.
- **KILL-IIDX (iid-excess trend):** over the COMPLETE-CENSUS octaves (round-1
  octaves 22,23,24,26,27 plus every octave this round completes below its
  pre-registered census cap), let for octave j
  eps_j = (max over census rows in octave j of exact env) - 1,
  UB_j  = max over census rows in octave j of (exact K'_r3 if the row's full
          ledger was computed, else env)   [UB_j >= true worst K'_r3 — the
          fit is on upper bounds, i.e. kill-biased, honest].
  The line FIRES if BOTH: (a) eps_j > 0 and strictly increasing across the
  last >= 3 consecutive populated complete-census octaves, AND (b) the
  log2-linear least-squares fit of log2(UB_j) vs log2(q_argmax) over those
  same octaves crosses log2(4) = 2 at log2(q) < 41 (the OFFICIAL gate scale
  — the hypothesis range of the ambient form). => KILLED-TREND.
  Probe rows (Tier C below) corroborate but do not enter the fit; a probe row
  individually violating is KILL-LITERAL/AMBER-2 as above in any case.
- **Legacy amber band K'_r3 in [1, 2): NOT a kill** — the established iid
  fluctuation band (round-1 c1r3-C5; the two round-1 ambers 1.0082/1.0245 sit
  here). Counted and reported exactly, scores nothing.

## VERDICT SEMANTICS (frozen)

- **KILLED**: KILL-LITERAL or KILL-IIDX fired.
- **MIXED**: no refuting line fired but KILL-AMBER-2 fired.
- **SURVIVED**: no kill line fired within scope (legacy [1,2) rows allowed
  and reported). SURVIVED + all controls PASS + the deferred row 918552577
  exactly evaluated + >= 2 new complete-census octaves => **MINTING IS GO**
  (the report will carry the full minting + amber-cascade prescription; the
  banking session, not this worker, executes it).
- **Integrity failures => DEFER** (not kill, not survive at the affected
  item): enumerator mismatch, DP mass-invariant failure, CRT modulus
  insufficiency, strategy-C divisibility failure, Modal timeout on a
  REQUIRED shard after the prescribed shrink attempt, control failure.
  A DEFER at a verdict-relevant row (env >= 2, or 918552577) caps the round
  verdict at INCOMPLETE-on-that-line; it cannot produce SURVIVED on that line.

## THE ROUND-2 ROW PROGRAM

**Family (intensional, re-enumerated in-round):** L=1, N=32, n'=64; q prime,
q = c*2^k+1, odd c, k >= 20, 2^28 <= q < 2^32 (the segment; H2 gives q <= 2^32).
Round-1 accscan counted 401 gated primes < 2^32 with 33 below 2^28 => expected
segment count 368; the in-round enumeration must reproduce 401/33/368 exactly
(consistency + nonemptiness assert). Octaves: 28 = [2^28,2^29), 29, 30, 31.

**Exactness kernels (all pre-registered here, validated in controls before
any verdict is read):**
- **T-A (uint64 exact DP)**, 1 shard/row: factored sub-steps
  (1+x^s)(1+x^-s) as out-of-place slice-adds on two preallocated uint64
  arrays. Exactness: intermediate cells <= 4^step <= 2^64 with the final
  A_total < 2^64 strictly (some walk lands off 0 since every shift z^i is a
  unit mod q); uint64 arithmetic is in any case exact mod 2^64 and
  A_total < 2^64, so the read-back is exact unconditionally. Integrity:
  wrap-sum(dp) == 0 mod 2^64 (total mass 4^32 = 2^64).
- **T-B (CRT trio)**, 3 shards/row: uint32-wrap (A mod 2^32) + two uint32
  mod-p shards (p1, p2 primes <= 2^30, mod once per step; intermediate
  < 4p <= 2^32). Reconstruction modulus 2^32*p1*p2 > 2^92 > 2^64 >= A —
  exact. Same wrap-sum / mod-p mass invariants (mass mod p = 2^64 mod p).
- **T-C (uint16 quint)**, 5 shards/row: uint16-wrap (A mod 2^16) + four
  uint16 mod-p shards (primes <= 2^14 - 1, mod once per step; intermediate
  < 4p < 2^16). Modulus 2^16*p1..p4 > 2^71 > 2^64 — exact.
- **Ledger kernel:** round-1 `primitive_orbit_count_fast` (numpy subset-sum
  primitivity) + verbatim orbit_key, weights 2..8 at L=1/N=32 — unchanged
  conventions; int64 dot products safe (8 terms * q < 2^35).
- E-1 = (q*A - 2^64)/2^64 exact Fraction; env = (q*A - 2^64)/(q*2^32).

**Tier ladder (memory caps fixed now; TIME caps filled by the benchmark
shard BEFORE any segment verdict row is run — engineering, not verdict):**
- Tier A: q <= min(0.98e9, Q_time_A) — T-A single shard. Q_time_A =
  (measured effective uint64 DP rate) * 235 s. DP+ledger combined in one
  shard where predicted DP time <= 180 s and env work allows; else ledger
  split out on demand.
- Tier B: q <= min(1.95e9, Q_time_B) — T-B trio. Q_time_B set by the
  benchmarked uint32 mod-p shard rate * 235 s.
- Tier C: q <= min(4.05e9, Q_time_C) — T-C quint; **probes only** (below).
- Above the feasible envelope: DEFERRED (compute law), listed row-by-row.

**Census vs probes (pre-registered coverage rule):**
- CENSUS (complete, verdict-grade, enters KILL-IIDX): every family row with
  q <= Q_census := min(1.95e9, Q_time_B). Priority order if wall-clock or
  budget forces truncation: complete octave 28, then 29, then ascending
  through 30; an incomplete octave is reported as partial and does NOT enter
  the trend fit as a complete octave.
- PROBES (Tier C, > Q_census): the deferred-row analysis cannot reach octave
  31 as census within the budget law (~190 rows * 5 shards); instead the
  following pre-named adversarial subsets are probed exactly: (a) the 5
  deepest-v_2 rows in (Q_census, 2^32), (b) the 4 largest feasible q under
  Tier C's caps, (c) 2 mid-octave-31 rows nearest 3e9. Probes get exact env
  (and full ledger if env >= 1). Labeled PROBE everywhere; corroboration
  only for the trend; full kill standard applies to each probe row itself.
- **q = 918552577 (the deferred w6 accident row, v_2 = 22): MANDATORY.**
  Tier A expected (16q = 14.7 GB); fallback T-B trio on memory failure.
  ALWAYS gets the full ledger shard (w2..8) regardless of env — the round
  must report its exact K'_r3 AND its w6 orbit mass in W_ext, plus an
  independent uint32 mod-p cross-shard asserting A mod p agreement.
- Ledger policy elsewhere: full ledger shard at every census/probe row with
  env >= 1 (exact K'_r3 there); env < 1 rows are certified survivors by
  bound (i) with K'_r3 <= env reported.

## POSITIVE CONTROLS (must all pass BEFORE any verdict is read)

- **C-REP (round-1 reproduction, >= 2 rows incl. the worst):** with the NEW
  T-A kernel: q=246415361 and q=81788929 must reproduce E-1 exactly equal to
  the banked round-1 values, derived from the banked exact K' fractions and
  W_ext = 0: E-1 = K' * q / 2^32 with K' = 1058880560632659/1033540934303744
  (246415361) and 2766759940242725/2744381056483328 (81788929); and their
  full ledgers must re-enumerate to W_ext = 0 (w2..8 all zero).
- **C-GROUND:** q=7937 (M2 anchor): E-1 == banked
  15584479363607/144115188075855872 via T-A.
- **C-XVAL (new-kernel trio):** at q=246415361, T-B (uint32-wrap + 2 mod-p)
  and T-C (uint16-wrap + 4 mod-p) reconstructions must equal the T-A exact
  A_total. Any mismatch = integrity failure => the affected tier is DEAD
  until fixed; no verdict from it.
- **MUT-1 (required to trip):** q=63361 (r2 killer) through the NEW T-A
  kernel with the gate DROPPED and the r2 window [2,6]: E-1 must equal the
  banked 2029645184561543/288230376151711744 and the literal detector must
  FIRE (K' = 6.199084... > 4) on the round-2 code path.
- **MUT-2 (required to trip):** allowance mutated to 10^-6: every evaluated
  in-gate row with E-1 > 0 must fire; assert E-1 > 0 everywhere (sum of
  squares minus the lambda=0 term; zero = integrity failure).
- **L2-XVAL:** strategy-C (projective directions, m=2: A = (sum_d N_d -
  4^N)/q with exact divisibility assert) must equal the direct (q,q)-grid
  L=2 A_total at q in {193, 257} and at q=12289 (N=32). The direct grid's
  own mass invariant: wrap-sum == 4^N mod 2^64. Divisibility failure or
  mismatch = integrity failure => the L=2 instrument is DEAD this round.

## THE L=2 PROGRAM (mandate item 3; instrument, pre-registered)

- **In-gate reachability wall (documented, not assumed):** the minimal gated
  prime is 7340033 (v_2 = 20). Exact L=2 E requires the (q,q) joint DP
  (>= 8*q^2 bytes: 4.3e14 B — impossible) or strategy-C projective sharding
  (q+1 one-dimensional DPs: ~q^2*N ~ 3.4e15 elem-ops ~ thousands of 280 s
  workers — out of the budget law). If the in-round arithmetic confirms
  this, gated L=2 rows are DEFERRED as a class; the wall goes in the
  results (this satisfies "at least the gated rows reachable at that
  aspect" — the reachable set is empty — and the instrument below is the
  deeper-level check).
- **Near-gate v_2-ladder (instrument, NOT verdict rows — all v_2 < 20, out
  of hypothesis; kill lines do NOT apply to them):**
  - N=32 (n'=64, H2: q <= 65536): all primes q = 1 mod 64, q <= 65536,
    v_2(q-1) >= 8; expected ladder {257 (v2 8), 12289 (12), 40961 (13)} plus
    any same-shape primes the enumeration adds (e.g. 13313 (10), 15361 (10)
    if prime). Direct grid for q <= 30000; strategy-C direction-sharded for
    larger (40961: ~8 direction-chunk shards).
  - N=64 (n'=128, H2: q <= 2^32, feasibility caps q): primes q = 1 mod 128
    with v_2 >= 9, q <= 20000 (grid q^2 with CRT over three int64 primes
    < 2^60, A < 4^64; 3 prime-shards/row): expected {7681 (9), 12289 (12),
    15361 (10) if prime, 18433 (11) if prime}.
  - Measured per row: exact E-1, r = q^2/2^N, env. Full L=2 ledger (window
    w in [3,9], level-2 primitive orbits) only if env >= 1 at that row
    (else env is the K'_r3 upper bound, survival-only, bound (ii)).
  - **Adverse-finding tripwire (pre-registered):** if the ladder's env is
    increasing in v_2 at fixed aspect AND its log2-linear extrapolation in
    v_2 crosses the allowance 4 at v_2 <= 20, that is a prominent ADVERSE
    FINDING against level-uniformity of r3 (recorded in findings + report;
    NOT a formal kill — the rows are out of hypothesis).

## NOT-KILLS (carried + new)

All round-1 NOT-KILLS carry over verbatim (ungated rows; large W_ext in-gate;
bulk K'_r3 -> 0; partial-ledger ratios > 4 [trigger full-ledger follow-up
where enumerable, else DEFER]; weight-5/6 accidents EXISTING at gated rows;
float excursions; ungated envelope growth). New: (a) K'_r3 in [1,2) at any
number of rows (fluctuation band — reported, scores nothing); (b) L=2 ladder
rows violating any line (out of hypothesis; adverse-finding channel only);
(c) DEFERRED rows beyond the engineering envelope (honest scope, listed);
(d) probe-set non-worst-ness (probes are not census; absence of a kill among
probes proves nothing about their octave — stated in the report).

## NONEMPTINESS / #137 ASSERTS

(1) segment family nonempty; counts printed and == (401 total, 33 below 2^28,
368 in segment) from the round-1 census; (2) >= 2 octaves COMPLETELY censused
this round (else the round is DEFERRED as underpowered, not scored);
(3) >= 1 row with v_2 >= 24 evaluated (deep-split adversarial content;
segment expected to contain such rows — if none exists in-family below the
envelope, record and probe the deepest reachable); (4) 918552577 evaluated
exactly with full ledger + cross-shard (else INCOMPLETE flag as above);
(5) all controls C-REP/C-GROUND/C-XVAL/MUT-1/MUT-2/L2-XVAL evaluated and
PASS before verdicts; (6) L=2 ladder nonempty at both aspects with >= 2
distinct v_2 values per aspect; (7) every Modal shard prints its mass
invariant and every strategy-C assembly asserts exact divisibility.

## SCOPE (honest, up front)

Exact K'_r3/env verdicts: L=1, N=32, in-gate census to Q_census (expected ~
octaves 28-30) + pre-named Tier-C probes + 918552577. Round-1's 33-row census
below 2^28 stands. NOT reachable this round: octave-31 census (budget law),
rows above the Tier-C envelope (memory/time law), gated L=2 (wall above),
official aspect N=256L (as always). SURVIVED means: no kill line tripped
within this scope; it does NOT prove C1'-r3, WCL-ZONE-ext, B-WEAK, or the
DLI node. Minting-GO is a recommendation to the maintainer under the
pre-registered bar, not DAG surgery by this worker.

## Budget & orchestration law (engineering)

Single benchmark shard first (doubles as C-REP worst-row control). All Modal
runs via tools/ramguard modal -- ~/.venvs/modal/bin/modal run
tools/modal_run_script.py (280 s worker; shrink+DEFER on failure). Waves of
<= 10 concurrent single-row shards (local client cgroup limits). Target
total <= ~450 shards, cents-to-low-$ total. Every shard's stdout captured to
the scratchpad log directory; app ids recorded where surfaced.
