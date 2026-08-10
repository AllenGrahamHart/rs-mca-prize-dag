# PREREG — ssparse_endpoints (round 28)

Coordinator brief, written before dispatch. The pilot appends its own
registrations BELOW the brief BEFORE any computation.

## Mandate

RH-AC (rate_half_band_crossing_location, the pose of record) names
two candidate endpoints with NO discriminating evidence held:
(RH-AC-lo) a_RH = k + 2^34 (the quotient floor is tight) vs
(RH-AC-hi) a_RH = 3n/4 (the half-distance pincer HD1 is tight). The
open content is min{a : S_sparse(a) <= B*(q)} within the PROVED
bracket. YOUR JOB: produce the first discriminating evidence — by
executing the two registered falsifiers with their power stated, and
by the first-ever scaled measurements of where the S_sparse crossing
actually sits. Read first: the child's statement
(critical/nodes/rate_half_band_crossing_location/statement.md), the
(RH-SPLIT) lossless decomposition
(rate_half_mca_sparse_layer_reduction, PROVED — S_sparse's exact
definition lives there), HD1
(rate_half_half_distance_safe_bracket), and the round-27
cancellation_recon consumer-bar map.

## Deliverables

**D1 — FALSIFIER F1 (fires against -lo, high power).** Push the
quotient-remainder floor's razor reach beyond 2^34 - 1. The
constant moved 2^33 -> 2^34 in one wave (the optimized v5
re-instantiation, c=2^33, d=1); round-27 cancellation_recon proved
the NEXT RUNG of the same family is 11.87 bits short with a tight
normalizer — so a further push needs a NEW mechanism, not the next
rung. Attack surfaces to price and try (register your order): a
non-2-power scale c; a mixed-depth (d >= 2) instantiation evading
the rung quantization; a hybrid of the rotated-prefix and
fixed-tail variants. A push to 2^34 + delta for ANY delta > 0
refutes (RH-AC-lo) and is the single highest-information result
available. An exhausted search with the mechanism space enumerated
is the complementary result: (RH-AC-lo) hardens.

**D2 — FALSIFIER F2 (fires against -lo from the safe side).**
Exhibit one received word y and one razor row with
N(y, k + 2^34; q) > floor(q/2^128). This is an S_sparse evaluation
at a single agreement — the object of
rate_half_sparse_pinning_rigidity's coupled system. Price it
honestly BEFORE attempting (the round-23 lesson: an unreachable
falsifier is not a falsifier); if unreachable at razor parameters,
execute the scaled analogue and state the transport caveat.

**D3 — THE FIRST CROSSING MEASUREMENTS.** At scaled band-analogue
rows where S_sparse is EXACTLY computable (register the scaling map
— the round-27 staircase_extension R2 map is a template: rate-1/2
RS rows N = 2k, D = the order-N subgroup, B = the scaled budget),
measure min{a : S_sparse(a) <= B} directly across a q-ladder and a
scale-ladder. THE QUESTION: does the measured crossing track the
scaled analogue of k + 2^34 (the -lo endpoint), of 3n/4 (the -hi
endpoint), or an intermediate law? Register predictions per
endpoint with numeric windows. Two-power grids; matched controls
(the random-word crossing at the same cells, computed but used ONLY
as the negative control — the F3 zero-power declaration binds: no
random-word quantity may enter the verdict).

**D4 — THE VERDICT.** State plainly which endpoint (if either)
survives, with the margin ladder. If the measurements land strictly
between the endpoints: the intermediate law, fitted and stated as
the new candidate, with the mechanism-change caveat (the round-27
rho extrapolation's caveat pattern).

## Escape tests (before the main work)

- Reproduce the (RH-SPLIT) decomposition at one banked cell (the
  split is PROVED lossless — your S_sparse must reproduce
  B_mca - B_ca^far exactly there).
- Replay the wave-10 a_RH formula at 3 sample q < 2^167 (the
  crossing your scaled measurements must reproduce in the
  determined region — the calibration).

## Rules (binding)

- QUARANTINE: do not read notes/pilots_20260802/CAMPAIGN_LEDGER.md
  at or below line 4302; do not read the other round-28 pilot dirs
  (apolar_origin, maxscan_algorithm, mca_safe_rewire). Pass this
  clause to any subagent verbatim.
- COMPUTE LAW: every interpreter run via
  `tools/ramguard tiny|local -- python3 ...` from the repo root —
  including file patching and JSON peeking. RAMGUARD_TIMEOUT
  documented per use.
- BANKED SCRIPTS FROM SCRATCH COPIES ONLY.
- RAM DISCIPLINE: file-at-a-time reads; never open dag.json; no
  bulk loads; checkpoint long runs; background batches with
  results files for >10-min runs.
- DRAFT-ONLY: writes only in
  notes/pilots_20260810/ssparse_endpoints/; no dag/nodes/tools
  writes; no git; no Modal; stdlib only.
- Register predictions with numeric windows BEFORE computing;
  misses first. Name every measured functional (CATCH-19C). The F3
  zero-power declaration binds throughout. Own-repo grep before
  claiming anything is missing (CATCH-24A).
- Your final message IS the report. End with a compliance
  paragraph.

## Pilot registrations (appended by the pilot before any computation)

Registered 2026-08-10 by pilot `ssparse_endpoints`, AFTER reading primary
text only (RH-AC statement, RH-SPLIT statement+proof, sparse pinning
rigidity, HD1, the rotated-prefix floor statement+proof, the fixed-tail
floor, the simple-pole MCA floor statement+proof, the far-CA rider
reduction, the two Hankel far-CA nodes) and BEFORE any interpreter run.

### R0. Named functionals (CATCH-19C)

All measurements below are of these and only these. `n_s` = scaled length,
`K = n_s/2`, `D_s` = order-`n_s` subgroup of `F_q^*` (`q` prime,
`q = 1 mod n_s`), `C = RS[F_q, D_s, K]`, `a = K + tau`, `r = n_s - a`.

- `F_SSPARSE(n_s,q,a)` = max over sparse pairs `(eps1,eps2)` with
  `|supp e1 u supp e2| <= r` of the number of MCA-bad FINITE slopes.
  (Exact `S_sparse`, the pose's object.)
- `F_SSPARSE_PROJ` = same, counting MCA-bad points of the projective
  pencil `P(U)`, `U = span(eps1,eps2)`. (GL2-invariant companion.)
- `F_TANG(n_s,q,a)` = the tangent-only part of `F_SSPARSE`.
- `F_LMAX(n_s,q,a)` = max over received words `U` of
  `#{c in C : agreement(U,c) >= a}` (exact max list size), computed in the
  equivalent coset form: max over cosets `V` of `F[X]_{<K}` inside
  `F[X]_{<n_s}` of `#{f in V : f has >= a roots in D_s}`.
- `F_FARLB(n_s,q,a)` = max over `U` and over poles `alpha in F\D_s` of
  `#{distinct P(alpha) : P in List(U,a)}`. This is the exact scaled
  payload of the PROVED simple-pole conversion; it is a certified LOWER
  bound on `B_ca^far(a)` (its pair is column-far by the same argument as
  the proof).
- `F_RWORD(n_s,q,a)` = the same crossing computed for uniformly random
  received words. **CONTROL ONLY — zero power by F3; never enters D4.**
- `F_CLASS(N,d,q)` = largest pigeonhole class of the map
  `A |-> (a_0(A),...,a_{d-1}(A))` over `m`-subsets `A` of `Q\{b_0}`,
  `m = N/2+d`, in the rotated-prefix construction.
- `F_MARGIN(N,d)` = `log2(2^128 C(N-1,N/2+d)) - log2(N q^d)` at
  `q = 2^256` (exact integers): the rung admissibility margin, and
  `F_REACH(N,d) = (d+1)*2^41/N - 1`.

### R1. Scaling map (SM), registered before use

Razor row invariants preserved: rate `1/2` (`K = n_s/2`); `D_s`
multiplicative of order `n_s`; and the budget EXPONENT
`B*/q = q^{-1/2}` (since `B* = floor(q/2^128)` and `log2 q ~ 256`).
Scaled budget therefore `B_s = floor(q/2^{L/2})` with `L = log2 q`, i.e.
`B_s = floor(sqrt(q))`. Scale ladder `n_s in {8,16}` (2-power grid);
q-ladder = primes `= 1 mod n_s` in increasing order.

Endpoint images under (SM):
- **(RH-AC-lo) image**: `tau_lo(n_s,q) = 2 n_s / log2 q` — the razor
  constant `2^34 = 2 n / log2 q` is exactly twice the first-moment line,
  a banked identity (CATCH-E). Equivalently `a_lo = K + tau_lo`.
- **(RH-AC-hi) image**: `tau_hi(n_s) = n_s/4`, `a_hi = 3 n_s/4` — the
  terminal wedge `r <= tau` of (PR4)/(PR5), which is q-independent.
- First-moment reference line `tau_FM = n_s / log2 q` (control-side
  scale only; it is a MEAN object and never enters D4).
- DISCRIMINATING RATIO: `rho_S = tau_measured / tau_FM`.
  **(RH-AC-lo) predicts `rho_S -> 2`, q-independent.
  (RH-AC-hi) predicts `rho_S = log2(q)/4`, growing in `log q`.**
  The endpoints separate only for `log2 q > 8`; every cell with
  `log2 q <= 8` is registered NOW as non-discriminating.

### R2. D1 attack-surface order (registered before attempting)

Order of attack, most-promising first, with prices:
1. **S-ROT-EXP** (mine, not in the brief): free the rotation exponent
   `v` in `R_A = rem_{Y^N-delta}(Y^v P_A)`. Price: the constrained
   coefficient count is the cyclic overlap of an interval of length
   `m+1` with `[N/2,N-1]`.
2. **S-DEPTH** (brief's (ii)): `d >= 2`.
3. **S-HYBRID** (brief's (iii)): rotated-prefix x fixed-tail.
4. **S-RIDER** (mine): `S = rem(Y^v P_A W)` with a free rider `W`.
5. **S-OVERFLOW** (mine): prefix degree `s >= c` (blocks overlap).
6. **S-SCALE** (brief's (i)): non-2-power `c`.

### R3. Predictions with numeric windows (all pre-computation)

**P0 (the pose's own reduction).** The RH-AC parenthetical "the binding
term is `S_sparse` alone — `B_ca^far` is free at razor rows" is FALSE on
the open part of the bracket `[k+2^34, 3n/4)`. Grounds to verify:
the PROVED simple-pole floor's own received pair is column-FAR
(`g_alpha` has no code explanation on `> k` positions, and `a > k`), so
its payload lands in `B_ca^far`, not in `S_sparse`; and the Hankel
far-CA layer's scope is `r < R/2 = 2^39`, i.e. `a > 3n/4`. Registered
window: `B_ca^far(k+2^34-1) >= 2^215` (predicted value `~2^216`), versus
`B* = 2^128`. Confidence 0.90.

**P1 (D1 rung lattice).** Over all `N = 2^i`, `2 <= N <= 2^20`,
`1 <= d <= N/2-1`, the admissible set `{F_MARGIN > 0}` has maximum reach
exactly `2^34 - 1`, attained at `(N,d) = (256,1)`, with
`F_MARGIN(256,1) in [114.0, 115.0]` bits; and
`F_MARGIN(128,1) in [-11.95, -11.80]` bits at reach `2^35-1`.
Confidence 0.90.

**P2 (S-SCALE empty).** `c | n/2 = 2^40` forces `c = 2^j`; the
non-2-power surface is EMPTY at the razor row, not merely unpromising.
Confidence 0.97.

**P3 (S-ROT-EXP closed).** The minimum over `v` of the constrained
coefficient count equals `d+1` and is attained by the printed
`v = N-d`. Confidence 0.85.

**P4 (S-DEPTH dead twice).** (a) At the admissibility boundary the reach
scales as `(d+1)/(2d-1)`, strictly decreasing, so `d=1` dominates every
`d >= 2`. (b) The `d=2` pigeonhole COLLAPSES: the second constrained
coefficient is `a_1/a_0 = -sum_{b in A} b^{-1}`, an ADDITIVE subset-sum
functional, which is essentially injective on the family. Registered
window: at scaled parameters, `F_CLASS(N,2,q) <= 4` while
`F_CLASS(N,1,q) = C(N-1,m)/N` to within `+-1`. Confidence 0.80.

**P5 (S-HYBRID / S-RIDER / S-OVERFLOW closed).** Fixed-tail's
denominator `q^d` is worse than rotated's `N q^{d-1}` by exactly `q/N`
(= 2^248 at N=256); a free rider `W` adds `deg W` unknowns and
`deg W` constraints, leaving the net count at `d+1`; prefix overflow
costs one full `log2 q = 256` bits per `+1` of reach against a
114.65-bit budget. No hybrid beats reach `2^34-1`. Confidence 0.80.

**P6 (F1 VERDICT).** F1 does NOT fire. Confidence 0.85.

**P7 (F2 reachability, priced BEFORE attempting).** At razor parameters
a witness needs `> 2^128` MCA-bad slopes from ONE sparse pair. Budget:
(i) tangent slopes `<= e <= r < 2^40`; (ii) non-tangent slopes are
solutions of `eps1|_E + gamma eps2|_E = h * P_Z|_E`, a system with
`tau - 1` excess conditions per `Z`, whose first-moment total is
`C(n-e,a-e) q^{1-tau} <= 2^{2^41 - 2^42} < 1` at `tau = 2^34`, and whose
adversarially-forcible count is at most `(2e-2)/(tau-1) < 2^8`.
Registered window: `S_sparse(k+2^34) in [2^40 - 2^34, 2^40 + 2^8]`,
i.e. `<= B* = 2^128` with `>= 87` bits to spare. **F2 is therefore
UNREACHABLE at razor parameters and predicted FALSE; the scaled
analogue is executed instead, with the transport caveat.**
Confidence 0.80.

**P8 (unconditional sparse tangent floor).** `S_sparse(a) >= min(r,q)`
for every `a` (tangent slopes are always MCA-bad via the `c=0`
witness). Confidence 0.90.

**P9 (D3, the pose's object).** The measured `F_SSPARSE` crossing does
NOT discriminate: `min{a : F_SSPARSE(a) <= B_s}` sits at or below the
BOTTOM of the scaled bracket in every cell with `B_s >= n_s`, i.e. the
sparse layer is free across the whole bracket. Confidence 0.65.

**P10 (D3, the discriminating object).** The list/far crossing
`sigma_L = max{sigma : F_FARLB(K+sigma) > B_s}` obeys
`rho_S = sigma_L / tau_FM in [1.0, 4.0]` at every measured cell —
i.e. strictly above the first-moment line and strictly below the
`log2(q)/4` law of `(RH-AC-hi)`. Confidence 0.60.

**P11 (D3, q-trend).** `rho_S` is non-increasing along the q-ladder to
within `+0.5`: `rho_S(q_max) <= rho_S(q_min) + 0.5`. (`-lo` predicts a
flat `rho_S`; `-hi` predicts `rho_S` growing by `log2(q_max/q_min)/4`,
which over the registered ladder is `>= +0.5`.) Confidence 0.55.

**P12 (matched control, ZERO POWER).** `F_RWORD` crossing sits strictly
below the `F_LMAX` crossing at every cell, gap `>= 1` unit of `a`.
Recorded as the negative control only; F3 binds and no `F_RWORD`
quantity may appear in D4. Confidence 0.85.

**P13 (escape ESC-1, registered MISS).** The brief's ESC-1 as written
("your `S_sparse` must reproduce `B_mca - B_ca^far` exactly") is NOT
(MS1): the proved identity is `B_mca = max(B_ca^far, S_sparse)`, a
maximum, so the difference identity is false in general (e.g. whenever
`B_ca^far > S_sparse`, as P0 predicts holds at every open `a`). I will
execute the corrected escape: verify the (RH-SPLIT) proof's actual
content — that translating a column-close pair by a code pair preserves
the MCA-bad slope set EXACTLY — at a banked-shaped cell. Confidence
0.90 that the difference form is wrong; 0.90 that the translation
invariance replays exactly.

**P14 (escape ESC-2).** `a_RH(q) = n - floor(q/2^128) + 1` at 3 sample
`q < 2^167` lies inside `[k+2^34, n]` and satisfies
`n - a_RH + 1 = floor(q/2^128)`. Confidence 0.95.

### R4. Compute plan (cells fixed in advance)

- `F_SSPARSE`, `F_SSPARSE_PROJ`, `F_TANG`: exhaustive at `n_s = 8`,
  `q in {17,41,73,89,97,113,193,241,257}`, all `a in [K+1, n_s-1]`;
  at `n_s = 16`, `q in {17,97,113,193,241,257}`, `a in [K+1, n_s-1]`,
  exhaustive where the config space allows and certified-lower-bound
  otherwise (declared per cell).
- `F_LMAX`, `F_FARLB`: exhaustive at `n_s = 8` over the same q-ladder;
  at `n_s = 16` over the reachable `a` only, declared per cell.
- `F_CLASS`: exact at small `(N,d)` with a real prime `q = 1 mod N`.
- Rung lattice: exact integers, `N` up to `2^20`.
- All runs under `tools/ramguard`; RAMGUARD_TIMEOUT documented per use.
- Deviations from this plan will be reported in D4 as declared
  deviations, misses first.

### R5. ADDENDUM registered mid-D1 (before its computation)

A seventh attack surface surfaced while pricing S-DEPTH, and is
registered here before being computed:

- **S-SUBGROUP** (mine): let `H <= Q` with `|H| = t`, `N' = N/t`, and take
  `A` = (`j` full `H`-cosets) union (`u` loose points), `m = jt+u = N/2+d`.
  Then `P_A(Y) = Ptilde(Y^t) E(Y)` with `deg E = u`, so for `d <= t` the
  constrained coefficients are `a_i = ptilde_0 * e_i` (`i < d`) — the
  `q^{d-1}` pigeonhole loss is REPLACED by the much smaller loss from the
  loose points. Admissibility becomes `C(N',j)/N' > 2^128`; reach stays
  `(d+1)n/N - 1`. This is the only way I can see to evade the rung
  quantization without leaving the printed proof skeleton.
  **Prediction P15: the S-SUBGROUP family's maximum admissible reach is
  again exactly `2^34 - 1`, attained only at `t = 1` (the printed rung),
  because keeping `N' >= 256` forces `N = 256t` and the reach ceiling
  becomes `n(1+1/t)/256 - 1`, which is maximised at `t = 1`. Registered
  window: max reach over the whole `(N,t,d,u)` scan lies in
  `[2^34-1, 2^34-1]` (i.e. exactly equal, no gain). Confidence 0.75.**
  If P15 is refuted the reach improves and **F1 FIRES**.

### R6. ADDENDUM registered before the D2/D3 measurements

Two further functionals, both q-INDEPENDENT in cost (so they reach the
`log2 q > 8` regime where the endpoint images actually separate — the
regime my R4 cell list could not reach):

- `F_DECAY(n_s,q,a) = log2 F_LMAX(a) - log2 F_LMAX(a+1)`, the per-unit
  decay of the EXACT max list profile. This is the decisive razor
  quantity: the proved construction supplies `2^242.65` codewords at
  `sigma = 2^34-1` and its own next rung supplies `2^116.13` at
  `sigma = 2^34+1` — a 126.5-bit cliff with the budget `2^128` strictly
  inside it. Whether the TRUE profile crosses `2^128` at `2^34` or far
  above is exactly a question about the decay rate.
  **Prediction P16: the measured `F_DECAY` of the exact max profile is
  within a factor 4 of `log2 q` (registered window
  `F_DECAY / log2 q in [0.25, 4.0]`) at every measured cell.**
  Consequence if held (stated now, before measuring): at the razor row
  the 114.65 bits of slack buy at most `114.65 * 4 / 256 = 1.79` units
  of `sigma` beyond `2^34-1`, i.e. `a_RH <= k + 2^34 + 1` — `(RH-AC-lo)`
  correct to within 2 units — whereas `(RH-AC-hi)` needs the profile to
  stay flat for `2^39-2^34 = 5.5e11` consecutive agreements, i.e.
  `F_DECAY <= 2.1e-10` bits, a factor `1.2e12` below `log2 q`.
  Confidence 0.65.
- `F_COLL(n_s,q,tau)` = max over supports `E` (`|E| = e = tau+1`) and
  over projective lines `l` in `P^(e-1)(F_q)` of
  `#{Z subset D\E, |Z| = a-e : [p_Z] in l}`, `p_Z = (prod_{x in Z}(j-x))_{j in E}`.
  This is EXACTLY the non-tangent part of `S_sparse` at the minimal
  support `e = tau+1`, and therefore the sharp scaled form of F2.
  **Prediction P17: `F_COLL` is small — registered window
  `F_COLL <= 4` for every `tau >= 2` cell measured** (i.e. the locator
  point set has no large collinear subset), so the sparse layer cannot
  supply a witness. Confidence 0.6.

Also registered: **P4b is already a MISS** — the measured largest
`(a_0,a_1)` class is 9 at `(N,d,q) = (20,2,10141)`, outside my
window `[1,4]`; the collapse itself (9 vs the 2524 needed) holds.
