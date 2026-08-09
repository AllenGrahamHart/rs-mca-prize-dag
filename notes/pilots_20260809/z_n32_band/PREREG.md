# PRE-REGISTRATION — Z-CEILING AT N = 32, sigma ~ 0: THE ALGORITHM (round 25)

2026-08-09. Coordinator brief; pilot appends registrations BEFORE
any computation. MANDATE: round 24 named N = 32 at sigma in [-2, 2]
"the single highest-value next computation" for Z-CEILING — the
record (C >= 1.7681) lives at sigma ~ 0 and small N, and the
"C decays in N" claim rests on an N-ladder with no sigma-matched
N = 32 point. The MITM state count 3^16 = 43M exceeded the 1G
wall. Design an algorithm that reaches it; run it as far as
reachable.

## Sources
- notes/pilots_20260808/z_ceiling_assault/ (REUSE: zcore.py, the
  families M2/M4, the functionals; THEOREM RC — rc.py — the
  finite-max + p > N^{N/2} kill; the record cell's 3-way
  verification pattern).
- background/nodes/f2_z1_mass_knife_edge round-24 update (the
  conjecture of record + the admissible pinning).

## Deliverables
- (D1) THE ALGORITHM, registered with its cost model BEFORE
  implementation. Candidate routes to price (pick or beat):
  (i) RC-aided weight truncation — TMASS needs only weights
  U <= U*(p) by RC's UMIN >= p^{2/N} kill + a proved tail bound
  from the weight enumerator's Z-1/Z-2 moments; enumerate only
  the low-weight shells (sum_{U <= W} C(32,U) 2^U terms — priced
  per W); (ii) orbit quotients (the mu_2N symmetry: TMASS is
  root-choice-invariant — quotient the cube by the shift/negation
  group before hashing); (iii) a two-level MITM with disk-backed
  checkpointed buckets under the 1G ceiling (the wall is RAM, not
  time — 12-hour modal profile local wall is available with
  RAMGUARD_TIMEOUT); (iv) the character-sum route (SMOOTH =
  sum_u prod cos^2 — p^kappa terms, feasible when p^kappa < ~2^32
  — EXACT rational or error-bounded float with the bound proved).
- (D2) THE RUN: max CRATIO over the N = 32 admissible sigma in
  [-2, 2] band (p ~ 2^30-2^34 at kappa = 1... register the exact
  admissible (kappa, p) cells; the M4/RSET family kappa = 1 needs
  p = 1 mod 64 near 2^32 — enumerate the reachable cells). Every
  computed cell 2-way verified (two independent algorithms, the
  round-24 pattern).
- (D3) THE N-LADDER VERDICT: with the N = 32 sigma-matched point,
  does max CRATIO decay from N = 16's 1.7681 (supporting an
  absolute C) or grow (re-opening the conjecture's death
  direction)? State the honest scope of whatever grid was reached.

## Rules
QUARANTINE: do not read notes/pilots_20260802/CAMPAIGN_LEDGER.md at
or past line 3731 (the "ROUND 25 LAUNCHED" marker); do not read the
other round-25 pilot dirs; PASS THIS CLAUSE VERBATIM to any subagent.
RAM DISCIPLINE (binding): file-at-a-time reads; never load dag.json
whole (grep it or read node.json shards); no bulk directory reads.
COMPUTE LAW: every python3 via tools/ramguard tiny|local -- python3
(literal --) from repo root, INCLUDING file patching and JSON
peeking; checkpoint long runs to YOUR OWN dir across the walls.
DRAFT ONLY in your own dir; never edit dag.json/nodes/tools; no git
writes; no Modal; stdlib only. Name every measured functional
(CATCH-19C); 2-power grids where yours to choose (CATCH-Z6); no
shift-0 cells (CATCH-19B). Verbatim quotes with file:line. No
REPORT.md — your final message IS the report.

# PILOT REGISTRATIONS

Appended 2026-08-09 by the Opus pilot BEFORE any computation. Nothing
below has been measured. Sources read so far: this brief;
notes/pilots_20260808/z_ceiling_assault/{zcore.py, rc.py, PREREG.md,
REPORT.md}; background/nodes/f2_z1_mass_knife_edge/statement.md
(lines 10-20, 90-100, 150-200); tools/ramguard.

## Z0. NAMED FUNCTIONALS (CATCH-19C)

Round-24 R0 is reused VERBATIM (TMASS, H, HEUR, CRATIO, EXCESS, SIGMA,
ZFRATIO, AU, UMIN, PFREE/PFMASS, SMOOTH, MAXCR); families M2 (I1
negacyclic GRS, S coords, kappa = R rows, Lambda = {1,3,...,2R-1},
w of exact order 2S) and M4 (I2 RSET, kappa = 1, Lambda = {1}, th of
exact order 2L) are reused verbatim from zcore.py:131-145.  New names:

- `TNUM(cell)` = 2^N * TMASS, an INTEGER.  All exactness claims below
  are about TNUM as an integer, never about a float.
- `NKER(cell)` = |ker cap {0,+-1}^N|, the eps = 0 vector included.
- `MSTATES(cell)` = min(3^{N/2}, p^kappa), the round-24 MITM wall
  (REPORT.md:98: "3^16 ~= 43M states -- out of reach at 1G by any kappa").
- `RBUCK` = number of buckets in the chosen algorithm; `DPEAK` = peak
  number of live dict entries.
- `BMAX(N,kappa,band,M)` = max CRATIO over M cells drawn from a band.
- `MMATCH(N,M)` = the distribution of max CRATIO over random M-subsets
  of an EXHAUSTIVELY swept in-band N-line (the size-matched null).
- `EVX(M0->M1)` = sqrt(ln M1 / ln M0), the extreme-value rescaling used
  to compare maxima taken over different numbers of cells.

## Z1. THE ALGORITHM (D1), with its cost model, registered before code

### Z1.0  Pricing the four brief routes (and rejecting three)

(i) RC-AIDED WEIGHT TRUNCATION -- REJECTED, with a forced correction of
the brief's framing.  THEOREM RC bounds weight from BELOW
(UMIN >= p^{2/N} = p^{1/16}); at p = 2^32 that kills only U <= 3.  The
mass sits at the OTHER end: E[AU[U]] = C(32,U) 2^U / p^kappa, so the
expected TMASS contribution of weight U is C(32,U)/p, maximised at
U = 16 and summing to (2^N - 1)/p = H.  Capturing 90% of TMASS-1 needs
sum_{U<=W} C(32,U) >= 0.9*2^32, i.e. W >= 18, at enumeration cost
sum_{U<=18} C(32,U) 2^U ~ 3.5e13 -- worse than the full MITM.  This is
round-24's own S4 miss restated (REPORT.md:84: "W90/N sits at 0.688").
NO tail bound can rescue it because the tail IS the mass.  Registered
as a rejection with a reason, not an unexplored option.

(ii) ORBIT QUOTIENTS -- REJECTED as a route, RETAINED as an invariant.
The negacyclic shift eps -> x*eps mod (x^N+1) generates a group of
order 2N = 64 acting on ker and preserving weight (shift^{32} = -1 is
negation), so TMASS = 1 + sum over nontrivial orbits |O| 2^{-wt}.  But
the cost is not in the OUTPUT (predicted ~4.3e5 kernel vectors, ~6.7e3
orbits); it is in the 3^16 intermediate half-sums, and the shift MIXES
the two halves, so it does not act on the intermediate object.  A
genuine factor 2 is available inside a half (eps -> -eps gives r -> -r
at equal weight); registered as an optional micro-optimisation only.

(iii) DISK-BACKED TWO-LEVEL MITM -- kept only as FALLBACK.  2 * 3^16
records at 8 B = 688 MB of disk traffic per cell.  Beaten by (v).

(iv) CHARACTER SUM -- REJECTED in this band except as a spot check.
With th^{32} = -1, the 32 columns and their negatives fill mu_64
exactly, so G(u) = prod_j cos^2(pi u th^j / p) is constant on
mu_64-cosets and SMOOTH = 64 * sum over the (p-1)/64 cosets.  That is
1.7e7 terms at p = 2^30 and 2.7e8 at p = 2^34, each 32 modmuls + 32
cos: >= 1e9 float ops in pure Python.  The brief's "feasible when
p^kappa < ~2^32" is true only at the extreme bottom edge of the band,
and even there route (v) is faster and EXACT.  Registered: I will run
it once, at the smallest admissible p reached, as an extra check only.

### Z1.1  THE CHOSEN ROUTE: BBM (Bucket-Bisect Meet-In-The-Middle)

The wall is RAM (43M live dict entries), not arithmetic.  BBM keeps the
O(3^{N/2}) TIME of the MITM while cutting its MEMORY by an arbitrary
factor RBUCK, WITHOUT re-enumeration and WITHOUT disk.

Construction.  Coordinates are split H1 = {0..15}, H2 = {16..31}; each
half is further split into two octets, giving lists P_h, Q_h of
3^8 = 6561 partial residues with masses 2^{8-wt}.  Every half-sum is
p_val (+) q_val.  Q_h is SORTED by residue (by the FIRST coordinate
when kappa >= 2).  Buckets are CONTIGUOUS residue intervals
B_b = [b*p/RBUCK, (b+1)*p/RBUCK) (intervals in the first coordinate
when kappa >= 2).  For a fixed p_val, the set of q_val with
(p_val + q_val) mod p in B_b is at most TWO CONTIGUOUS RANGES of the
sorted Q_h, located by bisect.  Hence each bucket pass touches only the
elements it needs, and the R bucket passes together cost ONE
enumeration, not R.

Join identity, REGISTERED (it is what makes the second half free of a
sign convention): the half-2 residue multiset is negation-symmetric
with masses, since eps -> -eps on H2 sends s -> -s at equal weight.
Therefore, with D_h[r] the mass-sum of half h at residue r,

        TNUM = sum_r D1[r] * D2[(-r) mod p] = sum_r D1[r] * D2[r].

Both forms are computed; EZ5 below asserts they agree exactly.
NKER is accumulated in a parallel pair of dicts with mass replaced by 1.

COST MODEL (registered, before implementation):
- TIME  = 2 * 3^16 = 86,093,442 inner-loop dict operations
          + 4 * RBUCK * 3^8 = 26,244*RBUCK bisect calls,
          + O(kappa) extra mod-ops per element when kappa >= 2.
          The bisect term at RBUCK = 256 is 6.7e6, i.e. < 8% of the
          dominant term, so total time is INDEPENDENT of RBUCK.
- MEMORY = 2 dicts of ~ 3^16 / RBUCK entries.  At RBUCK = 256 that is
          168,151 entries per dict, ~ 34 MB at ~100 B/entry, i.e.
          >= 25x under the 1G ceiling.  DPEAK is asserted in code.
- DISK   = one checkpoint line per bucket per cell.

### Z1.2  ALG-2, the independent verifier: UMITM (unbalanced MITM)

Split 18/14 (big side = coords {0..17}, small side = {18..31}), NO
bucketing, one plain dict of at most 3^14 = 4,782,969 entries; the
3^18 = 387,420,489 big-side sums are STREAMED with one lookup each.
Memory ~ 3^14 entries (registered risk: ~480 MB, the tight one; if peak
exceeds 800 MB I fall back to 13/19, or to BBM-ALT = BBM on the
even/odd coordinate split with a different RBUCK, and I will say which
was used).  Time ~ 3^18 lookups.

REGISTERED SCOPE OF THE 2-WAY VERIFICATION (what it does NOT buy).
ALG-1 and ALG-2 share (a) the column construction rows_M2/rows_M4 and
(b) Python integer arithmetic.  They differ in split point, in
bucketing vs none, in join direction, in the association order of the
partial sums, and in the source file.  They therefore CANNOT catch an
error in the column construction or in the admissibility pinning; those
are covered separately by EZ2 against round-24's machinery at N <= 16.

## Z2. THE EXACT ADMISSIBLE CELL GRID (D2), fixed now

Admissibility (from statement.md:12-15 and zcore.py:131-145): p prime,
p == 1 mod 2N so that an element of exact order 2N exists; 2N a 2-power
(CATCH-Z6: here 2N = 64, a 2-power, ASSERTED in code); 0 not in Lambda
(CATCH-19B, ASSERTED in code).  SIGMA = N - kappa*log2 p; the band is
SIGMA in [-2, 2].

TIER 1 (THE MANDATE).  M4 / I2 RSET, N = 32, kappa = 1, Lambda = {1},
th of exact order 64, p == 1 mod 64 prime.
  band  <=>  p in [2^30, 2^34] = [1.074e9, 1.718e10].
  Priority order FIXED NOW:
  (T1a) 9 SIGMA-anchors: for t in {2, 1.5, 1, .5, 0, -.5, -1, -1.5, -2},
        p = least prime == 1 mod 64 with p >= 2^{32-t}.
  (T1b) the SIGMA ~ 0 cluster: the 8 least primes == 1 mod 64 above
        2^32 and the 8 greatest below 2^32.
  (T1c) further cells on a t-grid of step 1/8 over [-2,2] (33 points),
        least prime == 1 mod 64 above 2^{32-t}, duplicates skipped,
        as far as the wall allows.
TIER 2.  M2 / I1, S = N = 32, R = kappa = 4, Lambda = {1,3,5,7}.
  band <=> p in [2^7.5, 2^8.5] = [181.0, 362.0]; p == 1 mod 64 prime
  ==> p in {193, 257} only.  EXHAUSTIVE, 2 cells.  p = 257 has
  SIGMA = 32 - 4 log2 257 = -0.0225: a DEAD-CENTRE sigma cell.
TIER 3.  M2 / I1, S = 32, R = 3, Lambda = {1,3,5}.
  band <=> p in [2^10, 2^{34/3}] = [1024, 2580].  EXHAUSTIVE; I predict
  the list is {1153, 1217, 1409, 1601, 2113} (5 cells).
TIER 4.  M2 / I1, S = 32, R = 2, Lambda = {1,3}.
  band <=> p in [2^15, 2^17] = [32768, 131072]; I predict ~ 130-145
  admissible primes.  I will sweep a REGISTERED sample -- the 12 least,
  the 12 greatest, and the 12 nearest SIGMA = 0 -- and will call it a
  sample, not a sweep.
LADDER CONTROL LINES (cheap, and cross-checked against round-24 code):
  N = 8  (kappa = 1, p == 1 mod 16, p in [2^6, 2^10])   EXHAUSTIVE;
  N = 16 (kappa = 1, p == 1 mod 32, p in [2^14, 2^18])  EXHAUSTIVE.
  These give the M-matched null MMATCH(8,M) and MMATCH(16,M).

## Z3. TWO-WAY VERIFICATION DESIGN (the round-24 pattern)

Every reported N = 32 cell must have ALG-1 and ALG-2 agree on TNUM
EXACTLY AS INTEGERS and on NKER exactly -- not to a tolerance.  A
disagreement is reported as a red flag, never silently resolved.
Escape tests, all of which must pass or the census is worthless:
- EZ1 (Z-FLOOR, statement.md:17-18): TMASS >= 2^N / p^kappa at EVERY
  computed cell.
- EZ2 (round-24 agreement): BBM and UMITM reproduce zcore.tmass_exact
  EXACTLY as Fractions on >= 20 cells at N in {8,16}, including the
  round-24 record cell (N = 16, kappa = 1, p = 161761,
  TMASS = 159/64, CRATIO = 1.7680688810).
- EZ3 (degenerate identity): with all columns == 0 mod p,
  TMASS = 2^N exactly.
- EZ4 (bucket independence): TNUM computed at RBUCK = 64 and 256 is
  BIT-IDENTICAL on >= 2 N = 32 cells.
- EZ5 (negation identity): sum_r D1[r]D2[r] = sum_r D1[r]D2[(-r) mod p]
  exactly, on >= 2 cells.
- EZ6 (grid asserts): CATCH-Z6 (2N a 2-power) and CATCH-19B (0 not in
  Lambda) asserted in code at every cell; RC(i) UMIN >= p^{2/N}
  wherever a weight enumerator is computed.
- EZ7 (mean law, diagnostic only): band mean of TMASS ~ 1 + H.

## Z4. PREDICTIONS (registered before any run)

Model of record (round-24 R4/P4a, fitted exponent -0.22532):
   MAXCR(N,M) - 1 = A sqrt(2) 2^{-sN} g(SIGMA) sqrt(2 ln M),
   g(SIGMA) = 2^{SIGMA/2}/(1+2^SIGMA), g(0) = 1/2, g(+-2) = 0.4,
   s = 0.20752 (model) or 0.22532 (round-24 fit).
Calibration on the round-24 record (N=16, band max 1.7681, band cell
count predicted ~1300): A ~ 3.9 at s = 0.22532.

- **P-Z1 (HEADLINE).** max CRATIO over the TIER-1 N = 32 sample
  (M ~ 20 cells) = **1.041**, registered window **[1.015, 1.12]**.
- **P-Z2.** No N = 32 in-band admissible cell exceeds **1.2**; none
  exceeds 1.7681; none exceeds 2.  A cell above 1.7681 is the DEATH
  direction and a MAJOR event: I would verify it with both algorithms
  plus a third and report it as the headline.
- **P-Z3 (the statistic that decides D3).** M-MATCHED ratio
  (MAXCR-1)_{N=32} / (MAXCR-1)_{N=16} at equal M lands in
  **[0.03, 0.30]** (model 0.100, fit 0.082).  A ratio >= 1 is DEATH.
- **P-Z4.** Band-extrapolated N = 32 max over all ~2.1e7 admissible
  primes: EVX(20 -> 2.1e7) = sqrt(16.86/3.00) = 2.37, giving
  **1 + 2.37*0.041 = 1.097**, window [1.03, 1.28] -- still far below
  the N = 16 exhaustive record 1.7681.  Registered as HEURISTIC.
- **P-Z5.** NKER at a SIGMA ~ 0 Tier-1 cell = 3^32/p ~= **431,000**
  +- 20%; UMIN in **[7, 10]** (RC alone gives only >= 4).
- **P-Z6.** Mean CRATIO over the Tier-1 sample = 1.000 +- 0.010.
- **P-Z7 (Tier 2, dead-centre).** CRATIO(M2, S=32, R=4, p=257,
  SIGMA = -0.0225) in **[1.00, 1.35]**, and < 1.7681.
- **P-Z8 (cost).** BBM: < 20 min wall and < 400 MB peak per Tier-1
  cell under tools/ramguard local.  UMITM: < 45 min, < 800 MB.
- **P-Z9.** The N = 16 exhaustive in-band max reproduces 1.7681 at
  p = 161761 (a replay of the round-24 record, not a new number).

## Z5. VERDICT RULES (registered before the fact)

- DECAY (supports an absolute C): M-matched ratio < 1 AND no N = 32
  in-band cell above 1.7681.
- GROWTH / DEATH DIRECTION: any N = 32 in-band cell above 1.7681, or an
  M-matched ratio >= 1.
- INCONCLUSIVE: fewer than 8 Tier-1 cells reached, or any 2-way
  disagreement.
- Either way: NO status flip, NO closure, no node edit.  Census
  evidence is evidence, never proof.  The f2 calibration clause binds
  every number here -- "No toy is evidence about Z_1 at the official
  row" (background/nodes/f2_z1_mass_knife_edge/statement.md) -- so all
  of this is about the FORM of Z-CEILING, never about Z_1 itself.

## Z6. COMPUTE DISCIPLINE

Every python3 invocation is `tools/ramguard local -- python3 ...` from
repo root, with RAMGUARD_TIMEOUT extending the 5-minute default wall.
The 1G RAM ceiling is NOT relaxed: the modal profile's 1536 MB is not
used, only the principle that the wall may be long.  Results are
appended per cell to CELLS.tsv in this directory; a cell already
present is skipped on resume; inside a cell, per-bucket partial sums
are checkpointed so a wall kill loses at most one bucket.  Draft only
in this directory; no node/tool/dag edits; no git; no Modal; stdlib
only.
