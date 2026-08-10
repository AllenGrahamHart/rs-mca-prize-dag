# PREREG — staircase_extension (round 27)

Coordinator brief, written before dispatch. The pilot appends its own
registrations BELOW the brief BEFORE any computation.

## Mandate

The wave-10 composition on rate_half_band_closure proved: for every
admissible 2^128 < q < 2^167, a_RH(q) = n - floor(q/2^128) + 1,
UNCONDITIONAL (statement.md section "QUADRATIC EXACT RANGE ...",
line ~160). Its anatomy: the quadratic staircase equality
(mca_quadratic_prize_rows) covers B = floor(q/2^128) <= B_Q =
389,500,552,609 ~ 2^166.503; the (RQ4) equivalence reduces
B_Q < B <= 2^39+1 to the single far-CA bound; the Hankel
unconditional layer B_ca^far(n-r) <= r+1 covers every r <= 2^39-2;
the coordinate-tangent family supplies the adjacent unsafe witness.
EXACT RESIDUAL: budgets {2^39, 2^39+1} (strata recorded per w10-H1).
Beyond 2^167: brackets only, a_RH in [k+2^34, 3n/4] (q >= 2^169) or
[k+2^34, n]. The razor slice needs budgets ~2^128. Your job: close
the two-budget residual, diagnose the boundary, and price the
razor-scale analogue honestly.

## Deliverables

**D1 — THE TWO-BUDGET RESIDUAL {2^39, 2^39+1}.** The smallest named
open piece on this node. Read the w10-H1 strata (budget 2^39:
strict A=3, s=0, e in [2^37, floor((2^39-1)/3)]; budget 2^39+1:
A=3 e >= 2^37+1 plus A=1 rows) and the far-CA layer's proof to see
exactly why r = 2^39-1 and 2^39 escape it. Attempt the close: either
extend the Hankel layer's argument by the two steps, or find a
dedicated argument for the two strata, or exhibit why they are
genuinely harder (a structural obstruction at the boundary is a
bankable finding). Register your route and expected outcome first.

**D2 — THE BOUNDARY DIAGNOSIS.** For each of the three layers
(staircase equality; (RQ4) equivalence; far-CA Hankel), answer: is
its stopping point an artifact of the proof budget (a finite
computation that was run to a chosen depth) or structural (the
argument itself degrades)? The answer determines whether "extend to
razor" is a computation, a new theorem, or impossible by this route.
Own-repo read first: mca_quadratic_prize_rows and the Hankel suite
nodes are PROVED — their proofs state their own domains.

**D3 — THE RAZOR-SCALE PROBE.** The formula a_RH = n - B + 1 is
exact on 2^128 < q < 2^167. Test the MECHANISM beyond: at scaled
band-analogue rows (accessible q, scaled n where the full a_RH is
exactly computable), does the staircase-shaped formula continue
through and past the scaled analogue of the 2^167 boundary?
Register the scaling map and predictions first. A deviation
LOCATES where new mathematics starts; continuation is evidence the
bracket [k+2^34, 3n/4] is slack.

**D4 — THE BRACKET.** Beyond 2^167 the bracket floor k+2^34 comes
from the optimized v5 re-instantiation (c=2^33, d=1). Attempt any
improvement of either end using the wave-10 machinery + the K5
witness-kernel routes named in WP5 (averaged conversion at giant M;
B2b balance). Price what a full razor determination would need if
D2 says "new theorem."

## Escape tests (before the main work)

- Replay the wave-10 arithmetic anchors: B_Q = 389,500,552,609;
  the a_RH formula at 3 sample q below 2^167; the bracket constants.
- Verify one Hankel-suite node's verifier (SCRATCH COPY) passes
  before leaning on its layer.

## Rules (binding)

- QUARANTINE: do not read notes/pilots_20260802/CAMPAIGN_LEDGER.md
  at or below line 4062; do not read the other round-27 pilot dirs
  (pincer_formalization, nonpoly_flank_census, cancellation_recon).
  Pass this clause to any subagent verbatim.
- COMPUTE LAW: every interpreter run via
  `tools/ramguard tiny|local -- python3 ...` from the repo root —
  including file patching and JSON peeking. RAMGUARD_TIMEOUT
  documented per use.
- BANKED SCRIPTS FROM SCRATCH COPIES ONLY (the round-26 lesson).
- RAM DISCIPLINE: file-at-a-time reads; never open dag.json; no
  bulk loads; checkpoint long runs; background batches with
  results files for >10-min runs.
- DRAFT-ONLY: writes only in
  notes/pilots_20260809/staircase_extension/; no dag/nodes/tools
  writes; no git; no Modal; stdlib only.
- Register predictions with numeric windows BEFORE computing;
  misses first. Name every measured functional (CATCH-19C).
  Own-repo grep before claiming anything is missing (CATCH-24A) —
  this brief's own citations are a starting map, not a boundary.
- Your final message IS the report. End with a compliance paragraph.

## Pilot registrations (appended by the pilot before any computation)

### R0 — what I read first (no computation yet)

`critical/nodes/rate_half_band_closure/statement.md`;
`background/nodes/mca_quadratic_prize_rows/{statement,proof}.md`;
`background/nodes/rate_half_quadratic_exact_range/{statement,proof}.md`;
`background/nodes/rate_half_ca_hankel_minimal_index_budget/{statement,proof,claim_contract}.md`;
`background/nodes/rate_half_ca_hankel_exceptional_root_charge/statement.md`;
`background/nodes/rate_half_ca_hankel_{strict_a3,half_distance_a3,half_distance_a1_core}_slope_slack_ledger/statement.md`;
`background/nodes/rate_half_ca_hankel_{split_pencil_equivalence,strict_m1_corefree_five_slope_route_fence}/statement.md`;
`background/nodes/rate_half_{far_ca_rider_reduction,postquadratic_mds_extension_fence}/statement.md`.

Anatomy as I now hold it (to be checked, not assumed):
`A = R+1-2rho`, `delta = rho-Ae`, `(MI1) (A+s)e<=d=rho-s`,
`(ERC2) T <= floor(((N-s)e+rho-Ae)/(rho-s))`. At `N=16m`, `R=8m`:
strict budget `B=2^39` is `r=rho=4m-1`, `A=3`; half-distance budget
`B=2^39+1` is `r=4m` with `A=3` (`rho=4m-1`) or `A=1` (`rho=4m`).
`e>=m` forces `s=0` in the `A=3` profile; the residual is exactly the
window `m<=e<=floor(rho/3)` where `(ERC4) T<=4e+1` misses `rho+1` by
`4(e-m)+1`.

### R1 — D1 route and expected outcome (registered before computing)

Route, in the order I will attempt it:

1. **Counting-layer two-step extension.** Re-derive `(ERC2)` and ask
   whether the deficit at `A=3` can be closed by charging (i) the
   boundary/infinite slope, (ii) the unsaturated-row deficit `C`, or
   (iii) the `O`-slack. Registered expectation: **FAILS** (p ~ 0.9) —
   at `e=m` the required gain is exactly ONE slope below a cap that the
   `m=1` route fence realizes with equality.
2. **Truth probe by scale/field descent.** Recast the strict `A=3`
   residual as: an affine line (`e=1`) / degree-`e` rational normal
   curve in monic-locator coefficient space carrying `T>=rho+2` split
   locators over `D`, equivalently a line in syndrome space meeting the
   weight-`<=r` syndrome set in `T` points. Census this exactly at the
   accessible scales and, crucially, **across fields at fixed scale**.
3. **Dimension-count pricing.** Compare `dim(Q-space) - #conditions`
   `= [(e+1)(rho+1)-1] - T(rho-1)` against the number of admissible
   combinatorial configurations, to predict whether witnesses exist at
   official `q > 2^128`.

Registered expected outcome of D1: **the two-budget residual will NOT
be closed by me**, and I expect to bank instead (a) a proved-in-repo
structural reason (the `m=1` fence) that no incidence/Hankel-only
argument closes it uniformly in the scale, and (b) evidence about
whether the residual is a truth gap or only a proof gap.

### R2 — D3 scaling map (registered before computing)

Official row: `n=2k=2^41`, `R=n-k=2^40`, `B=floor(q/2^128)`,
`a_RH = n-B+1`. Two scaling axes:

- **Scale axis.** A band-analogue row is any rate-1/2 RS row
  `N=2k`, `R=k`, `D` = the order-`N` multiplicative subgroup of `F_q`
  (`N | q-1`). Under this map: `r_Q(R) = floor(k(3-sqrt 7))`; the
  proved far-CA reach is `r <= R/2-2`; **the scaled analogue of the
  `2^167` boundary is `B = R/2+1`, i.e. `r = R/2`**, and the scaled
  analogue of the two-budget residual is `r in {R/2-1, R/2}`.
  Official = `R=2^40` (`m=2^37`); accessible = `R=8,10,...,40`.
- **Field axis.** Fix the scale (`R=8`, `N=16`, `rho=r=3`, `A=3`,
  `e=1`) and vary `q = 1 mod 16`. Official `q > 2^128`; accessible
  `q <= 10^3`.

Predictions, with windows (all registered before computing):

- **P1 (escape).** `r_Q = 3k-floor(sqrt(7k^2))-1 = 389,500,552,608`,
  `B_Q = 389,500,552,609`, `F_(n,k)(B_Q-1) >= 0 > F_(n,k)(B_Q)`, and
  `(B_Q+1)2^128 = 1325401699591443156987887040901155312315433327` +
  `00160`. Exact match required; any mismatch is reported first.
- **P2 (escape).** All four printed prize primes pass a Proth
  certificate, `n | p-1`, `p < 2^256`, and the printed
  `B = floor(p/2^128)` is exact. Exact match required.
- **P3 (escape).** A SCRATCH COPY of
  `rate_half_ca_hankel_minimal_index_budget/verify.py` exits 0.
- **P4 (replication).** Over `F_17`, `D=F_17^*`, `rho=3`: the number of
  affine coefficient lines carrying `>= 5` split monic cubics is
  exactly **16**, the maximum on any core-free line is exactly **5**,
  and each such line omits exactly one domain point. Exact (16, 5).
- **P5 (liveness table).** Define the strict-`A=3` budget at scale `R`
  (even, `N=2R`, `rho=R/2-1`) LIVE iff
  `1+floor(rho/3)(4R-6)/(R-2) >= rho+2`. Predicted DEAD set for
  `R in [8,40]`: exactly `{10, 12, 18}`. Window: I will report the
  computed set; a difference is a self-correction.
- **P6 (flagship, field axis).** Number of `T>=5` witness lines at
  `N=16, rho=3, e=1` as a function of `q = 1 mod 16`: `q=17` gives 16;
  for `97 <= q <= 1000` I predict the TOTAL over all such fields is
  **0**, window `[0,3]`. (Heuristic: excess `dim-cond = -3`, so the
  count should decay like `16(17/q)^3`; expected total ~0.18.)
- **P7 (mechanism).** Consequently I predict the staircase-shaped
  formula `B_ca^far(N-r) = r+1` HOLDS at the residual radius
  `r = R/2-1` for every `q >= 97` at scale `R=8` — i.e. the official
  residual is a PROOF gap, not a TRUTH gap. Refuted if any `q >= 97`
  in the sweep carries a witness.
- **P8 (half-distance).** At `N=16, r=4` the `A=3` branch is EMPTY
  (`m+1=2 > floor(rho/3)=1`) and only `A=1`, `rho=4`, `e in [2,4]`
  survives; I predict no `T >= 6` witness at `q=17` and will report
  honestly if my search is not exhaustive.
- **P9 (D2 calls, registered as predictions).** staircase layer:
  STRUCTURAL; `(RQ4)` layer: STRUCTURAL (it is exactly the
  half-distance barrier `r <= (n-k)/2`); far-CA Hankel layer: METHOD
  wall with a proved no-go for the incidence family, not a finite
  computation run to a chosen depth.
- **P10 (D4 pricing).** The razor slice needs `B ~ 2^128 >> n = 2^41`,
  a regime in which `a = n-B+1` is not even well-posed; I predict
  "extend to razor" is a NEW THEOREM, not a computation, and that
  closing `{2^39, 2^39+1}` moves the determined `q`-axis by a relative
  `2^-38` only.

### R3 — compliance notes

All interpreter runs via `tools/ramguard tiny|local -- python3 ...`
from the repo root, `RAMGUARD_TIMEOUT` documented per use; banked
scripts run from scratch copies only; writes confined to
`notes/pilots_20260809/staircase_extension/`; quarantine respected
(no `CAMPAIGN_LEDGER.md` at/below line 4062, no other round-27 pilot
dirs); no subagents.
