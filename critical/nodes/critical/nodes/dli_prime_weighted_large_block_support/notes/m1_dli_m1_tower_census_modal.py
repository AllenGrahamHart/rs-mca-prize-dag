#!/usr/bin/env python3
"""M1 (C2'' adversarial round 1): SHARDED n=64 TOWER CENSUS  --  app rs-mca-dli-m1

The decisive falsification experiment for CONJECTURE C2''
(critical/nodes/dli_prime_weighted_large_block_support/notes/C2PP_POSED_20260710.md).
DO NOT LAUNCH without maintainer review.  House Modal law: every function call
< 280 s, modest RAM (<= 16 GB), wide .map() fan-out.

MEASUREMENT (per row (n=64, t, q), q prime, q = 1 mod 64)
=========================================================
The f2b nested-tower junction measurement (banked exactly at n=32, 8 rows:
notes/f2b_nested_correlation.json + f2b_replay_perclass_20260710.py) lifted to
n = 64: h = n/2 = 32 fibers i in 0..31 (pairs {i, i+32} of mu_64 exponents),
level-1 state per fiber in {N, B, single}; e = floor(t/2) even moments
p_{2s}(m_1) = sum_i m_1(i) zeta^{2si}; o = ceil(t/2) odd (skew) moments
sum_{i in G} eps_i zeta^{(2s+1)i}.  Per class k = #singletons (k = 0..32):

  cn[k]   = # even-null states with k singletons          (conditional count)
  cs[k]   = sum of skewcount(G) over those states          (conditional mass)
  an[k]   = C(32,k) 2^(32-k)                               (all states, exact)
  asum[k] = sum of skewcount(G) over ALL states            (unconditional mass)

and the C2'' three-part decomposition exactly as in c2pp_calibration_20260710:
COSET column = k = 0 (routed, clause i); ACCIDENT classes = k >= 1 with
class-conditional mean > theta = 2 x unconditional class mean (window-priced,
clause iii); BULK = the rest (clause ii object).  Junction ratio continuity
objects (raw ratio, stripped mean/mass ratios) reported per row.

THE EXPONENTIAL BOTTLENECK AT n=64 AND ITS EXACT RESOLUTION
===========================================================
The n=32 machinery tabulates skewcount over 2^16 singleton masks and joins
3^8-per-half even configs; at n=64 the mask table is 2^32 entries (>= 32 GB)
and the even-null join has ~3^32/q^e matched pairs (~1e13) -- both impossible.
FUSION: a level-1 state PLUS its skew pattern is one choice per fiber from
{N, B, +, -} with moment key in F_q^t (N -> 0; B -> (2w, 0); +/- -> (w, +-v)).
cs[k] = # of fused states with key = 0 and k signed fibers.  Then:

  STRATEGY B (grid DP == the 16+16 MITM join collapsed onto its key grid):
    the sort-merge join of the banked f2_watch_w3_transition_modal.py pattern,
    with halves aggregated by (key, k); since q^t << 4^16 the aggregated half
    IS a dense grid, and building both halves + joining is dominated by one
    incremental DP over (q^t x 33) cells, 4 shifted adds per fiber, 32 fibers.
    int64 exact, per-fiber max-cell guard << 2^63.
  STRATEGY C (projective sharding, for rows where the q^t grid is too big):
    exact hyperplane identity over a projected key block u in F_q^m:
      sum_{d in P^{m-1}(F_q)} [u.d = 0] = (q^{m-1}-1)/(q-1) + q^{m-1} [u = 0]
    so cs[k] = (sum_d N_d[k] - c1 * N_ref[k]) / q^{m-1}  (EXACT integer
    division -- asserted, a strong end-to-end exactness guard).  Each N_d is a
    small scalar-key DP; directions d are .map()-sharded in chunks < 280 s.
    In all configured rows the projected block is 2-dim (m = 2, c1 = 1,
    divisor q, q+1 directions).
  STRATEGY A (literal MITM sort-merge, xcheck): halves of 16 fibers built by
    prefix-sharded doubling + bincount aggregation onto (key, k) grids, then
    the negated-key join with k-convolution.  Run at (t=2, q=193) as an
    independent-machinery cross-check against Strategy B ON MODAL (equality
    asserted); the same code path is validated locally at n = 16/32 against
    brute force and the banked 8-row record.

  The junction state-class axis (k) rides INSIDE every DP as its last
  dimension (33 slices), so no class-bucket sharding is needed; the shard
  grid is (row) x (direction chunks).

MARGINALS (cheap, exact, one small worker or in-row):
  cn[k]:  3-option DP {N, B, S} on the e even components (grid q^e x 33);
  asum[k]: 3-option signed DP {+, -, unsigned*weight-2} on the o odd
           components (grid q^o x 33) -- N/B collapse exactly (equal odd
           contribution 0), weight 2^{#unsigned};
  an[k], n_all = 3^32: closed form.

RUN PLAN (shard grid; per-shard estimates from the local validation record
m1_validation_record.json, measured rate then derated 2x for Modal)
==================================================================
  SHARD 0 (go/no-go gate ON MODAL, runs first, blocks everything on FAIL):
    one worker: (a) replays the banked 8-row n=32 f2b record with THESE
    kernels and asserts exact agreement with the pre-registered expected
    values baked below (BANKED_F2B / BANKED_F2B_RATIOS, transcribed from
    f2b_nested_correlation.json + f2b_replay_perclass_20260710.json --
    the transcription itself is asserted against the .jsons by the local
    validator); (b) the DEFERRED-TO-MODAL n=64 identity check: strategy B
    (grid DP, 1.23e6 cells -- over the local 1e6-state law) == strategy C
    (projective sharding) at (t=2, q=193), all 33 classes exact.
    [Local RAM law addendum 2026-07-12: local validation < 300 MB RSS,
     < 1e6 states; everything local fits EXCEPT this B-grid, hence shard 0.]
  PHASE p1 (t = 2: F-c census + F-a depth-1 scales):
    full-grid rows (one census_row_full worker each; grid (q,q,33) int64;
    np.roll peak ~4 grids, so cap q <= 2753 -> <= ~8.1 GB/worker):
      q in [193, 257, 449, 577, 641, 769, 1153, 1217]   (F-a low scales)
      q in [1409, 1601, 2113, 2689, 2753]                (census head)
      est <= ~65 s derated at q = 2753.
    direction-sharded rows (census_row_dirs chunks + row_marginals):
      q in [3137 .. 10369] (27 census rows) + 12289 (F-a top scale);
      per direction: 128 passes over (q x 33); chunks sized ~120 s;
      ~2-4 chunks/row typical, ~65 chunk workers + 28 marginal workers.
  PHASE p2 (t = 3: F-a depth-2 scales):
    q = 193: one full-grid worker (grid 193^3 x 33 = 1.9 GB, est <= 120 s);
    q in [257, 449, 577]: direction-sharded, g = 1 (grid (q, q, 33) per
      direction, q+1 directions, chunks ~120 s: ~2/4/7 chunks resp.).
  PHASE p3 (OPTIONAL stretch, t = 4 depth-3 anchor):
    q = 193, g = 2 (grid (193,193,193,33) = 1.9 GB per direction, 194
      directions, ~1 direction per ~40-80 s, chunks of 3, ~65 workers).
    Off by default; enable with --phase p3.
  XCHECK: strategy A at (t=2, q=193): 8 workers (2 halves x 4 prefix
    ranges of 64/256 prefixes, ~30-110 s each; a single worker would
    extrapolate to ~420 s > 280 s law, hence the prefix-range sharding);
    5 MB half-grids joined in the entrypoint vs the p1 grid row.
  Estimated totals (local measured rate 4.3-6.9e8 elem-ops/s run-to-run;
    planner uses the 2x-derated floor RATE_DERATED = 2.5e8):
    shard0 ~ 2 min; p1 ~ 3-5 CPU-hr measured / ~6-10 derated (dominated by
    the 28 direction-sharded t=2 rows, ~800-1900 core-s measured each at
    the top q); p2 ~ 1 / ~2; xcheck ~ 0.15; p3 (optional) ~ 5 / ~10.
  All shards < 280 s, < 16 GB.  ~10-20 CPU-hr worst case incl. p3 --
  single-digit dollars at Modal CPU pricing.

ROW LIST is frozen below (FA_T2_SMALL, FC_CENSUS, FA_T2_TOP, T3_SCALES,
T4_STRETCH).  F-c fixed shape = (n=64, t=2), 32 census rows with q >= 1241
so the weight-3 window is rare (lambda_3 = C(32,3) 2^3 / (64 q) <= 0.5).

PRE-REGISTERED READS (baked; quoted verbatim from C2PP_POSED_20260710.md)
=========================================================================
See PREREG_VERBATIM below (printed before any data).  Operational proxies
FIXED HERE, BEFORE THE RUN:

  F-a (super-polylog stripped bulk trend): per depth t, group positive bulk
  ratios by octave floor(log2 q); scale value = GM within octave; slope
  object s_j = GM_j / (j + 0.5)  (~ bulk / log2 q).  FIRES at a depth iff
  >= 3 octaves are populated AND s is strictly increasing across the top 3
  populated octaves AND s_top >= 2 * s_min.  F-a KILL iff it fires at >= 2
  depths.  (The coset column and accident classes are stripped/priced FIRST
  -- clauses (i)+(iii) -- exactly as in the calibration.)

  F-c (Poisson window law, >= 30 rows at fixed shape): census cells =
  (census row r, class k) with k in {3,4,5} and lambda_{r,k} =
  C(32,k) 2^k / (64 q_r) <= 1/2 (the rare-window regime; over the frozen
  census list this is exactly k = 3 -- the ternary weight-3 window, the same
  proved object as the band census mu = ORBITS_w/q, band_census_and_
  clusters.py, and the q-independent ledger product C(N,w) 2^(w-N-L-1)).
    PRIMARY (exceedance frequencies): X = # cells whose class is flagged
    ACCIDENT by the theta = 2 decomposition; model P_cell = 1 - exp(-lambda);
    exact Poisson-binomial two-sided tail; KILL iff p < 1e-3.
    SECONDARY (orbit-dressing quanta): T = sum over cells of the exact
    unconditional weight-k vanisher orbit count V_{r,k} = asum[k] / 2^(32-k)
    / 64 (integrality checked; sub-orbit anomalies flagged, not scored);
    vs Poisson(sum lambda); exact two-sided tail; KILL iff p < 1e-3.
    Census NOT ARMED (no read) if < 30 rows assembled.

  NON-FALSIFIERS (explicitly NOT scored, printed with the results): raw
  unstripped conditional ratios (the coset column is exact accounting);
  single orbit-quantized spikes consistent with the exact window mean;
  failures of per-level / per-junction-uniform / factorized proxies.

CONTINUITY ANCHORS (n=32 banked): raw GM 2.139; coset-stripped bulk GM 0.967
(anti-correlated); accident masses 128/128/64/128, exact multiples of 32.
"""
import json
import math
from collections import defaultdict

try:
    import modal
    app = modal.App("rs-mca-dli-m1")
    image = modal.Image.debian_slim().pip_install("numpy")
except ImportError:                      # local validation mode (no modal)
    modal = None

    class _App:                          # no-op decorators; kernels stay pure
        def function(self, **kw):
            return lambda f: f

        def local_entrypoint(self, **kw):
            return lambda f: f
    app = _App()
    image = None

# ------------------------------------------------------------------ row grid
N64 = 64
THETA = 2.0
FA_T2_SMALL = [193, 257, 449, 577, 641, 769, 1153, 1217]
FC_CENSUS = [1409, 1601, 2113, 2689, 2753, 3137, 3329, 3457,
             4289, 4481, 4673, 4801, 4993, 5441, 5569, 5953,
             6337, 6529, 6977, 7297, 7489, 7681, 7873, 7937,
             8513, 8641, 9281, 9473, 9601, 9857, 10177, 10369]
FA_T2_TOP = [12289]
T3_SCALES = [193, 257, 449, 577]
T4_STRETCH = [193]

FULL_GRID_MAX_CELLS = 2.6e8      # int64; ~2.1 GB/grid, np.roll peak ~4 grids
RATE_DERATED = 2.5e8             # elem-ops/s; local measured, derated 2x
TARGET_SHARD_S = 120.0           # aim well under the 280 s law

# pre-registered SHARD-0 expected values, transcribed from the banked
# f2b_nested_correlation.json: (t, q) -> (null_states, E_cond, E_uncond)
BANKED_F2B = {
    (2, 97): (443841, 1.0268181623599442, 1.0286044319148024),
    (2, 193): (223041, 0.5223792934931246, 0.5171675677689829),
    (2, 8353): (10881, 0.05293631100082713, 0.012451587195224463),
    (2, 32801): (7713, 0.033190716971347074, 0.003951799255511239),
    (3, 97): (443841, 0.014852165527745296, 0.01429144858675763),
    (3, 193): (223041, 0.004591084150447676, 0.0039458522287911316),
    (4, 97): (4369, 0.040283817807278556, 0.01429144858675763),
    (4, 193): (1137, 0.014072119613016711, 0.0039458522287911316),
}
# and from f2b_replay_perclass_20260710.json:
# (t, q) -> (ratio, stripped_mean_ratio, stripped_mass_ratio)
BANKED_F2B_RATIOS = {
    (2, 97): (0.9982634047652964, 0.9982643827159152, 0.9981285990617759),
    (2, 193): (1.010077441140837, 1.0096559781116154, 1.0091643748453256),
    (2, 8353): (4.2513705418317835, 2.751522241871854, 2.690883197134267),
    (2, 32801): (8.398887399216648, 0.0, 0.0),
    (3, 97): (1.0392344371239752, 1.0334167782499855, 1.0332762131764144),
    (3, 193): (1.1635215624519777, 1.066158533199014, 1.0656394187395681),
    (4, 97): (2.8187358029336016, 2.8741696984709986, 2.868010384467522),
    (4, 193): (3.566306794344376, 0.0, 0.0),
}

PREREG_VERBATIM = """\
## PRE-REGISTERED FALSIFIER (fixed at pose time, before any new data)
[C2PP_POSED_20260710.md, quoted verbatim]

C2'' is refuted by any of:
- (F-a) sustained super-polylog growth of the COSET-STRIPPED,
  ACCIDENT-PRICED junction ratios: after clauses (i)+(iii) with exact
  accounting, a residual bulk trend exceeding C*log q per junction for
  every C, sustained across >= 3 increasing q-scales at >= 2 depths of the
  packet's nested toy towers;
- (F-b) a replayable tower whose total clause-(ii)+(iii) charge,
  transported by the packet arithmetic, exceeds the full 21-bit reserve;
- (F-c) an accident census (>= 30 rows at fixed shape) whose exceedance
  frequencies reject the clause-(iii) Poisson window law at p < 10^-3.

NOT falsifiers: raw unstripped conditional ratios (F2b's 4.25x/8.40x -- the
coset column is exact accounting); single orbit-quantized spikes consistent
with the exact window mean (the 6.6x/9.4x classes); failures of per-level,
per-junction-uniform, or factorized proxies.

[M1 scope note: F-a and F-c are scored by this experiment; F-b needs the
packet transport arithmetic and is NOT scored here (aggregate bit-charge is
printed as an unscored diagnostic).]"""


# ------------------------------------------------------------- field helpers
def least_primitive_root(q):
    x, d, fac = q - 1, 2, []
    while d * d <= x:
        while x % d == 0:
            fac.append(d)
            x //= d
        d += 1
    if x > 1:
        fac.append(x)
    fac = sorted(set(fac))
    return next(c for c in range(2, q)
                if all(pow(c, (q - 1) // r, q) != 1 for r in fac))


def get_zeta(q, n):
    """Deterministic primitive n-th root, IDENTICAL convention to the archived
    verify_level2_tower.get_zeta (least primitive root ^ ((q-1)/n))."""
    assert (q - 1) % n == 0, f"mu_{n} does not exist in F_{q}"
    z = pow(least_primitive_root(q), (q - 1) // n, q)
    assert pow(z, n, q) == 1 and pow(z, n // 2, q) != 1
    return z


def fiber_contribs(q, n, t):
    """Per fiber i in 0..h-1 the F_q^t key contributions of the four fused
    options; component order pinned: evens s=1..e first, then odds s=0..o-1.
       returns list of (cN, cB, cP, cM), each a length-t tuple."""
    h, e, o = n // 2, t // 2, (t + 1) // 2
    zeta = get_zeta(q, n)
    out = []
    for i in range(h):
        w = [pow(zeta, (2 * s * i) % n, q) for s in range(1, e + 1)]
        v = [pow(zeta, ((2 * s + 1) * i) % n, q) for s in range(o)]
        cN = tuple([0] * t)
        cB = tuple([2 * x % q for x in w] + [0] * o)
        cP = tuple(w + v)
        cM = tuple(w + [(q - x) % q for x in v])
        out.append((cN, cB, cP, cM))
    return out


# ------------------------------------------------- Strategy B: grid DP census
def joint_grid_census(q, n, t):
    """cs[k] exact: # fused states {N,B,+,-}^h with key = 0 in F_q^t and k
    signed fibers.  Grid DP (q,)*t + (h+1,), int64, guarded."""
    import numpy as np
    h = n // 2
    fib = fiber_contribs(q, n, t)
    axes = tuple(range(t))
    dp = np.zeros((q,) * t + (h + 1,), dtype=np.int64)
    dp[(0,) * t + (0,)] = 1
    for (cN, cB, cP, cM) in fib:
        new = dp + np.roll(dp, cB, axis=axes)          # N (identity) + B
        tp = np.roll(dp, cP, axis=axes)
        new[..., 1:] += tp[..., :-1]                   # + (k -> k+1)
        del tp
        tm = np.roll(dp, cM, axis=axes)
        new[..., 1:] += tm[..., :-1]                   # - (k -> k+1)
        del tm
        dp = new
        assert int(dp.max()) < (1 << 61), "int64 headroom guard tripped"
    return [int(x) for x in dp[(0,) * t]]


# ------------------------------------- Strategy C: projective direction shards
def proj_directions(q, m):
    """Canonical representatives of P^{m-1}(F_q): first nonzero coord = 1."""
    import itertools
    dirs = []
    for lead in range(m):
        for tail in itertools.product(range(q), repeat=m - 1 - lead):
            dirs.append((0,) * lead + (1,) + tail)
    assert len(dirs) == (q ** m - 1) // (q - 1)
    return dirs


def joint_proj_chunk(q, n, t, g, dirs):
    """sum over the given directions d of N_d[k] = # fused states with the
    first g key components = 0 AND (projected block).d = 0, k signed fibers.
    Grid (q,)*g + (q, h+1) per direction.  Returns python-int list len h+1."""
    import numpy as np
    h = n // 2
    m = t - g
    fib = fiber_contribs(q, n, t)
    gaxes = tuple(range(g + 1))
    total = [0] * (h + 1)
    for d in dirs:
        assert len(d) == m
        dp = np.zeros((q,) * g + (q, h + 1), dtype=np.int64)
        dp[(0,) * (g + 1) + (0,)] = 1
        for (cN, cB, cP, cM) in fib:
            sB = tuple(cB[:g]) + (sum(a * b for a, b in zip(d, cB[g:])) % q,)
            sP = tuple(cP[:g]) + (sum(a * b for a, b in zip(d, cP[g:])) % q,)
            sM = tuple(cM[:g]) + (sum(a * b for a, b in zip(d, cM[g:])) % q,)
            new = dp + np.roll(dp, sB, axis=gaxes)
            tp = np.roll(dp, sP, axis=gaxes)
            new[..., 1:] += tp[..., :-1]
            del tp
            tm = np.roll(dp, sM, axis=gaxes)
            new[..., 1:] += tm[..., :-1]
            del tm
            dp = new
            assert int(dp.max()) < (1 << 61), "int64 headroom guard tripped"
        row = dp[(0,) * (g + 1)]
        for k in range(h + 1):
            total[k] += int(row[k])
    return total


def ref_census(q, n, t, g):
    """N_ref[k]: # fused states with the first g key components = 0 (no
    constraint on the projected block).  g = 0 -> closed form."""
    import numpy as np
    h = n // 2
    if g == 0:
        return [math.comb(h, k) * (2 ** h) for k in range(h + 1)]
    fib = fiber_contribs(q, n, t)
    gaxes = tuple(range(g))
    dp = np.zeros((q,) * g + (h + 1,), dtype=np.int64)
    dp[(0,) * g + (0,)] = 1
    for (cN, cB, cP, cM) in fib:
        new = dp + np.roll(dp, cB[:g], axis=gaxes)
        tp = np.roll(dp, cP[:g], axis=gaxes)
        new[..., 1:] += tp[..., :-1]
        tm = np.roll(dp, cM[:g], axis=gaxes)
        new[..., 1:] += tm[..., :-1]
        dp = new
        assert int(dp.max()) < (1 << 61)
    return [int(x) for x in dp[(0,) * g]]


def assemble_from_projection(q, n, t, g, sum_over_dirs, n_ref):
    """cs[k] = (sum_d N_d[k] - c1 N_ref[k]) / q^(m-1); EXACT divisibility
    asserted (end-to-end integrity guard for the sharded path)."""
    h = n // 2
    m = t - g
    c1 = (q ** (m - 1) - 1) // (q - 1)
    div = q ** (m - 1)
    cs = []
    for k in range(h + 1):
        num = sum_over_dirs[k] - c1 * n_ref[k]
        assert num % div == 0, (
            f"PROJECTION IDENTITY BROKEN at k={k} (q={q},t={t},g={g}): "
            f"{num} not divisible by {div} -- a shard is missing or corrupt")
        cs.append(num // div)
        assert cs[k] >= 0
    return cs


# ------------------------------------------------------------- marginal DPs
def even_null_census(q, n, t):
    """cn[k]: # {N,B,S}^h level-1 states, even components all 0, k singletons.
    Grid (q,)*e + (h+1,)."""
    import numpy as np
    h, e = n // 2, t // 2
    fib = fiber_contribs(q, n, t)
    axes = tuple(range(e))
    dp = np.zeros((q,) * e + (h + 1,), dtype=np.int64)
    dp[(0,) * e + (0,)] = 1
    for (cN, cB, cP, cM) in fib:
        new = dp + np.roll(dp, cB[:e], axis=axes)      # N + B
        ts = np.roll(dp, cP[:e], axis=axes)            # single (even part = w)
        new[..., 1:] += ts[..., :-1]
        dp = new
        assert int(dp.max()) < (1 << 61)
    return [int(x) for x in dp[(0,) * e]]


def signed_all_census(q, n, t):
    """asum[k] = sum of skewcount over ALL level-1 states, class k
    == # weight-k odd-null signed patterns * 2^(h-k).  N/B collapse exactly
    (equal odd contribution 0) into one weight-2 unsigned option.
    Grid (q,)*o + (h+1,)."""
    import numpy as np
    h, e, o = n // 2, t // 2, (t + 1) // 2
    fib = fiber_contribs(q, n, t)
    axes = tuple(range(o))
    dp = np.zeros((q,) * o + (h + 1,), dtype=np.int64)
    dp[(0,) * o + (0,)] = 1
    for (cN, cB, cP, cM) in fib:
        new = 2 * dp                                   # {N,B}: weight 2
        tp = np.roll(dp, cP[e:], axis=axes)
        new[..., 1:] += tp[..., :-1]
        tm = np.roll(dp, cM[e:], axis=axes)
        new[..., 1:] += tm[..., :-1]
        dp = new
        assert int(dp.max()) < (1 << 61)
    return [int(x) for x in dp[(0,) * o]]


# ----------------------------- Strategy A: literal MITM sort-merge (xcheck)
def mitm_joint_census_dict(q, n, t):
    """cs[k] via literal half-split sort-merge with dict aggregation
    (any q; 4^(h/2) per half -- n <= 32 only).  Validation ground truth."""
    h = n // 2
    fib = fiber_contribs(q, n, t)

    def half(fibers):
        agg = defaultdict(int)
        agg[((0,) * t, 0)] = 1
        for i in fibers:
            cN, cB, cP, cM = fib[i]
            nxt = defaultdict(int)
            for (key, k), c in agg.items():
                for con, dk in ((cN, 0), (cB, 0), (cP, 1), (cM, 1)):
                    nk = tuple((a + b) % q for a, b in zip(key, con))
                    nxt[(nk, k + dk)] += c
            agg = nxt
        return agg

    L = half(range(0, h // 2))
    R = half(range(h // 2, h))
    Rbykey = defaultdict(dict)
    for (key, k), c in R.items():
        Rbykey[key][k] = Rbykey[key].get(k, 0) + c
    cs = [0] * (h + 1)
    for (key, kL), cL in L.items():
        nk = tuple((q - a) % q for a in key)
        for kR, cR in Rbykey.get(nk, {}).items():
            cs[kL + kR] += cL * cR
    return cs


def mitm_half_grid(q, n, t, fibers, prefix_fibers=4, prefix_lo=0,
                   prefix_hi=None):
    """One MITM half: (q^t, h/2+1) int64 grid of (key, k)-aggregated counts
    over the 4-option states of the given fibers, built by prefix-sharded
    doubling + bincount.  prefix_[lo,hi) selects a range of the 4^prefix
    prefix choices (the Modal xcheck shard axis); full range by default."""
    import itertools
    import numpy as np
    hf = len(fibers)
    kmax = hf + 1
    fib = fiber_contribs(q, n, t)
    qt = q ** t
    pf = list(fibers)[:prefix_fibers]
    sf = list(fibers)[prefix_fibers:]
    if prefix_hi is None:
        prefix_hi = 4 ** len(pf)
    comps = [np.zeros(1, dtype=np.int64) for _ in range(t)]
    kk = np.zeros(1, dtype=np.int64)
    for i in sf:                                       # suffix by doubling
        cN, cB, cP, cM = fib[i]
        comps = [np.concatenate([c, (c + cB[j]) % q,
                                 (c + cP[j]) % q, (c + cM[j]) % q])
                 for j, c in enumerate(comps)]
        kk = np.concatenate([kk, kk, kk + 1, kk + 1])
    grid = np.zeros(qt * kmax, dtype=np.int64)
    opts = [(0, 0), (1, 0), (2, 1), (3, 1)]            # N,B,+,- ; dk
    for ci, choice in enumerate(itertools.product(opts, repeat=len(pf))):
        if not (prefix_lo <= ci < prefix_hi):
            continue
        pc = [0] * t
        pk = 0
        for (oi, dk), i in zip(choice, pf):
            con = fib[i][oi]
            pc = [(a + b) % q for a, b in zip(pc, con)]
            pk += dk
        flat = np.zeros(len(kk), dtype=np.int64)
        mul = 1
        for j in range(t):
            flat += ((comps[j] + pc[j]) % q) * mul
            mul *= q
        idx = flat * kmax + (kk + pk)
        grid += np.bincount(idx, minlength=qt * kmax)
    return grid.reshape(qt, kmax)


def mitm_join(q, t, GL, GR, h):
    """Negated-key sort-merge join of two half grids + k-convolution."""
    import numpy as np
    qt = q ** t
    kmax = GL.shape[1]
    neg = np.zeros(qt, dtype=np.int64)
    rest = np.arange(qt, dtype=np.int64)
    mul = 1
    for j in range(t):
        cj = rest % q
        rest = rest // q
        neg += ((q - cj) % q) * mul
        mul *= q
    GRn = GR[neg]
    assert int(GL.max()) < (1 << 31) and int(GRn.max()) < (1 << 31)
    E = np.einsum('fi,fj->ij', GL, GRn)                # join + k-convolution
    cs = [0] * (h + 1)
    for i in range(kmax):
        for j in range(kmax):
            cs[i + j] += int(E[i, j])
    return cs


def mitm_joint_census_array(q, n, t, prefix_fibers=4):
    """cs[k] via literal half-split sort-merge, numpy path.  The Modal xcheck
    runs the SAME mitm_half_grid/mitm_join code path, prefix-range-sharded
    across workers (each half grid is q^t*(h/2+1) int64: q=193, t=2: 5 MB)."""
    h = n // 2
    GL = mitm_half_grid(q, n, t, range(0, h // 2), prefix_fibers)
    GR = mitm_half_grid(q, n, t, range(h // 2, h), prefix_fibers)
    return mitm_join(q, t, GL, GR, h)


# --------------------------------------------------- decomposition + pricing
def lam_window(h, k, q, o):
    """Clause-(iii) window intensity: mean-field weight-k signed vanisher
    ORBITS per row = C(h,k) 2^k / (2h q^o) -- the band-census mu = ORBITS/q
    instance of the q-independent ledger product C(N,w) 2^(w-N-L-1)."""
    return math.comb(h, k) * (2 ** k) / (2 * h * (q ** o))


def decompose_row(q, n, t, cn, cs, asum, theta=THETA):
    """The C2'' three-part decomposition; mirrors c2pp_calibration_20260710.py
    and f2b_replay_perclass_20260710.py semantics EXACTLY."""
    h, o = n // 2, (t + 1) // 2
    an = [math.comb(h, k) * (2 ** (h - k)) for k in range(h + 1)]
    n_all = 3 ** h
    assert sum(an) == n_all
    n_null, s_null, s_all = sum(cn), sum(cs), sum(asum)
    Ec = s_null / n_null if n_null else float('nan')
    Eu = s_all / n_all
    ratio = Ec / Eu if Eu > 0 else float('nan')
    # coset-stripped (k >= 1), both f2b conventions
    sn1, nn1 = s_null - cs[0], n_null - cn[0]
    sa1, na1 = s_all - asum[0], n_all - an[0]
    Ec1 = sn1 / nn1 if nn1 else float('nan')
    Eu1 = sa1 / na1 if na1 else float('nan')
    r1 = Ec1 / Eu1 if (Eu1 and Eu1 > 0) else float('nan')
    r2 = (sn1 / n_null) / (sa1 / n_all) if sa1 else float('nan')
    # accident classes (calibration semantics)
    accid = []
    for k in range(1, h + 1):
        Eck = cs[k] / cn[k] if cn[k] else 0.0
        Euk = asum[k] / an[k] if an[k] else 0.0
        if Euk > 0 and Eck / Euk > theta and cs[k] > 0:
            accid.append((k, Eck / Euk, cs[k]))
        elif Euk == 0 and cs[k] > 0:
            accid.append((k, float('inf'), cs[k]))
    acc_ks = {k for k, _, _ in accid}
    bn = sum(cn[k] for k in range(1, h + 1) if k not in acc_ks)
    bs = sum(cs[k] for k in range(1, h + 1) if k not in acc_ks)
    un = sum(an[k] for k in range(1, h + 1) if k not in acc_ks)
    us = sum(asum[k] for k in range(1, h + 1) if k not in acc_ks)
    Ecb = bs / bn if bn else float('nan')
    Eub = us / un if un else float('nan')
    bulk = (Ecb / Eub if (Eub and Eub > 0)
            else (0.0 if Ecb == 0 else float('nan')))
    # window objects: unconditional weight-k vanisher orbits V_k + lambda_k
    Vk, V_flags = {}, []
    for k in range(1, h + 1):
        pat, rem = divmod(asum[k], 2 ** (h - k))
        assert rem == 0, f"asum[{k}] not divisible by 2^(h-k) -- machinery bug"
        vq, vr = divmod(pat, 2 * h)
        Vk[k] = vq if vr == 0 else pat / (2 * h)
        if vr:
            V_flags.append(k)          # sub-orbit anomaly: flagged, not scored
    acc_list = [{"k": k, "class_ratio": (r if r != float('inf') else 'inf'),
                 "mass": mm, "quanta": mm / (2 * h),
                 "quantized": (mm % (2 * h) == 0),
                 "lam": lam_window(h, k, q, o)} for k, r, mm in accid]
    return {"q": q, "n": n, "t": t, "n_null": n_null, "s_null": s_null,
            "E_cond": Ec, "E_uncond": Eu, "ratio": ratio,
            "stripped_mean_ratio": r1, "stripped_mass_ratio": r2,
            "bulk_ratio": bulk, "coset": {"cn0": cn[0], "cs0": cs[0],
                                          "an0": an[0], "asum0": asum[0]},
            "accidents": acc_list, "V_orbits": {k: Vk[k] for k in Vk if Vk[k]},
            "suborbit_flags": V_flags,
            "table": {k: [cn[k], cs[k], an[k], asum[k]]
                      for k in range(h + 1) if cn[k] or cs[k] or asum[k]}}


# -------------------------------------------------------- exact tail tests
def poisson_binom_pmf(ps):
    pmf = [1.0]
    for p in ps:
        new = [0.0] * (len(pmf) + 1)
        for j, x in enumerate(pmf):
            new[j] += x * (1 - p)
            new[j + 1] += x * p
        pmf = new
    return pmf


def two_sided_from_pmf(pmf, x):
    lo = sum(pmf[:x + 1])
    hi = sum(pmf[x:])
    return min(1.0, 2 * min(lo, hi))


def poisson_two_sided(lam, x):
    term, k = math.exp(-lam), 0
    lo = 0.0
    kmax = max(x, int(lam + 12 * math.sqrt(lam + 1) + 20))
    while k <= kmax:
        if k <= x:
            lo += term
        k += 1
        term *= lam / k
    hi = 1.0 - lo + (math.exp(-lam) * lam ** x / math.factorial(x)
                     if x < 170 else 0.0)
    return min(1.0, 2 * min(lo, max(hi, 0.0)))


# ----------------------------------------------------------- the two reads
def read_Fa(rows_by_depth):
    """Operational F-a proxy (pre-registered above).  Returns (fired, log)."""
    lines = ["", "=" * 72, "F-a READ -- coset-stripped, accident-priced bulk "
             "trend vs C log q", "=" * 72]
    fired_depths = 0
    for t in sorted(rows_by_depth):
        rows = sorted(rows_by_depth[t], key=lambda r: r["q"])
        lines.append(f"\ndepth t={t}: q, bulk_ratio, bulk/log2(q):")
        for r in rows:
            b = r["bulk_ratio"]
            bb = b if b == b else float('nan')
            sm = r["stripped_mass_ratio"]
            lines.append(f"  q={r['q']:>6}  bulk={bb:8.4f}"
                         f"  s={bb / math.log2(r['q']):8.5f}"
                         f"  (raw={r['ratio']:.3f}"
                         f" strip={sm if sm == sm else 0.0:.3f})")
        oct_gm = {}
        for r in rows:
            b = r["bulk_ratio"]
            if b == b and b > 0:
                oct_gm.setdefault(int(math.log2(r["q"])), []).append(b)
        octs = sorted(oct_gm)
        s = {j: math.exp(sum(math.log(x) for x in oct_gm[j]) / len(oct_gm[j]))
             / (j + 0.5) for j in octs}
        lines.append("  octave slope objects s_j: " +
                     "  ".join(f"j={j}:{s[j]:.5f}" for j in octs))
        fire = False
        if len(octs) >= 3:
            top3 = octs[-3:]
            inc = all(s[a] < s[b] for a, b in zip(top3, top3[1:]))
            grow = s[top3[-1]] >= 2 * min(s.values())
            fire = inc and grow
        lines.append(f"  depth t={t} F-a proxy: "
                     f"{'FIRES' if fire else 'does not fire'} "
                     f"({len(octs)} octaves populated)")
        fired_depths += fire
    kill = fired_depths >= 2
    lines.append(f"\nF-a KILL LINE: fires at {fired_depths} depth(s); "
                 f"requirement >= 2  ==> " +
                 ("*** F-a FIRED -- C2 double-prime REFUTED ***" if kill else
                  "F-a NOT fired (C2 double-prime survives this read)"))
    return kill, "\n".join(lines)


def read_Fc(census_rows):
    """Operational F-c (pre-registered above).  Returns (fired, log)."""
    h = 32
    lines = ["", "=" * 72, "F-c READ -- accident census vs the Poisson window "
             "law (fixed shape n=64, t=2)", "=" * 72]
    if len(census_rows) < 30:
        lines.append(f"only {len(census_rows)} census rows assembled ( < 30 )"
                     " ==> F-c NOT ARMED; extend the census upward.")
        return False, "\n".join(lines)
    cells = []
    for r in sorted(census_rows, key=lambda x: x["q"]):
        o = (r["t"] + 1) // 2
        for k in (3, 4, 5):
            lam = lam_window(h, k, r["q"], o)
            if lam <= 0.5:
                acc = any(a["k"] == k for a in r["accidents"])
                V = r["V_orbits"].get(k, 0)
                cells.append({"q": r["q"], "k": k, "lam": lam,
                              "exceed": acc, "V": V})
    lines.append(f"census: {len(census_rows)} rows, {len(cells)} rare-window "
                 f"cells (k with lambda <= 1/2)")
    for c in cells:
        lines.append(f"  q={c['q']:>6} k={c['k']}: lambda={c['lam']:.4f}  "
                     f"V_orbits={c['V']}  "
                     f"accident={'YES' if c['exceed'] else 'no'}")
    X = sum(1 for c in cells if c["exceed"])
    ps = [1 - math.exp(-c["lam"]) for c in cells]
    pX = two_sided_from_pmf(poisson_binom_pmf(ps), X)
    lamT = sum(c["lam"] for c in cells)
    Tf = sum(c["V"] for c in cells)
    T = int(round(Tf))
    frac = abs(Tf - T) > 1e-9
    pT = poisson_two_sided(lamT, T)
    lines.append(f"\nPRIMARY (exceedance frequency): X={X} accidents vs "
                 f"E={sum(ps):.3f}  exact Poisson-binomial two-sided p={pX:.3e}")
    lines.append(f"SECONDARY (orbit-dressing quanta): T={Tf} orbits vs "
                 f"Poisson(sum lambda={lamT:.3f})  exact two-sided p={pT:.3e}"
                 + ("  [FRACTIONAL QUANTA FLAGGED -- inspect sub-orbits]"
                    if frac else ""))
    kill = (pX < 1e-3) or (pT < 1e-3)
    lines.append("F-c KILL LINE: p < 1e-3 on either test  ==> " +
                 ("*** F-c FIRED -- C2 double-prime REFUTED ***" if kill else
                  "F-c NOT fired (window law survives at 30+ rows)"))
    return kill, "\n".join(lines)


# ------------------------------------------------------------ Modal wrappers
def _shard0(spec):
    """GO/NO-GO GATE: banked 8-row n=32 record must be reproduced EXACTLY by
    these kernels, and strategy B == strategy C at n=64 (t=2, q=193)."""
    report, ok = [], True
    for (t, q), (nn, Ec, Eu) in sorted(BANKED_F2B.items()):
        cs = mitm_joint_census_dict(q, 32, t)
        cn = even_null_census(q, 32, t)
        asum = signed_all_census(q, 32, t)
        d = decompose_row(q, 32, t, cn, cs, asum)
        r0, r1, r2 = BANKED_F2B_RATIOS[(t, q)]
        row_ok = (d["n_null"] == nn
                  and abs(d["E_cond"] - Ec) < 1e-12
                  and abs(d["E_uncond"] - Eu) < 1e-12
                  and abs(d["ratio"] - r0) < 1e-12
                  and abs((d["stripped_mean_ratio"]
                           if d["stripped_mean_ratio"] ==
                           d["stripped_mean_ratio"] else -1) - r1) < 1e-12
                  and abs((d["stripped_mass_ratio"]
                           if d["stripped_mass_ratio"] ==
                           d["stripped_mass_ratio"] else -1) - r2) < 1e-12)
        ok &= row_ok
        report.append({"row": [t, q], "ok": row_ok,
                       "got": [d["n_null"], d["E_cond"], d["E_uncond"],
                               d["ratio"]]})
    csB = joint_grid_census(193, N64, 2)
    dirs = proj_directions(193, 2)
    csC = assemble_from_projection(
        193, N64, 2, 0, joint_proj_chunk(193, N64, 2, 0, dirs),
        ref_census(193, N64, 2, 0))
    n64_ok = (csB == csC)
    return {"ok": bool(ok and n64_ok), "banked_replay": report,
            "n64_B_eq_C": n64_ok}


def _full_row(spec):
    q, t = spec["q"], spec["t"]
    cs = joint_grid_census(q, N64, t)
    cn = even_null_census(q, N64, t)
    asum = signed_all_census(q, N64, t)
    return {"spec": spec, "cs": cs, "cn": cn, "asum": asum}


def _dirs_chunk(spec):
    q, t, g = spec["q"], spec["t"], spec["g"]
    dirs = [tuple(d) for d in spec["dirs"]]
    s = joint_proj_chunk(q, N64, t, g, dirs)
    return {"spec": {k: spec[k] for k in ("q", "t", "g", "chunk_id")},
            "ndirs": len(dirs), "sum_dirs": s}


def _marginals(spec):
    q, t, g = spec["q"], spec["t"], spec["g"]
    cn = even_null_census(q, N64, t)
    asum = signed_all_census(q, N64, t)
    n_ref = ref_census(q, N64, t, g)
    return {"spec": spec, "cn": cn, "asum": asum, "n_ref": n_ref}


def _xcheck_half(spec):
    """One prefix-range shard of one MITM half grid (returned as raw bytes;
    q=193, t=2: 5 MB)."""
    q, t = spec["q"], spec["t"]
    h = N64 // 2
    fibers = range(0, h // 2) if spec["half"] == 0 else range(h // 2, h)
    g = mitm_half_grid(q, N64, t, fibers, prefix_fibers=4,
                       prefix_lo=spec["lo"], prefix_hi=spec["hi"])
    return {"spec": spec, "shape": list(g.shape), "grid": g.tobytes()}


if modal is not None:
    shard0_gate = app.function(image=image, cpu=2, memory=4096,
                               timeout=280)(_shard0)
    census_row_full = app.function(image=image, cpu=4, memory=16384,
                                   timeout=280)(_full_row)
    census_row_dirs = app.function(image=image, cpu=4, memory=8192,
                                   timeout=280)(_dirs_chunk)
    row_marginals = app.function(image=image, cpu=2, memory=4096,
                                 timeout=280)(_marginals)
    xcheck_mitm64 = app.function(image=image, cpu=4, memory=8192,
                                 timeout=280)(_xcheck_half)


# ------------------------------------------------------------- shard planner
def plan_shards():
    """The frozen shard grid.  Returns (full_specs, dir_row_specs, xchecks).
    dir_row_specs: per row a dict with the direction chunks."""
    full, dirrows = [], []
    for q in FA_T2_SMALL + FC_CENSUS + FA_T2_TOP:
        t, g = 2, 0
        cells = q * q * 33
        if cells <= FULL_GRID_MAX_CELLS:
            full.append({"q": q, "t": t, "phase": "p1"})
        else:
            dirrows.append(_plan_dir_row(q, t, g, "p1"))
    for q in T3_SCALES:
        t, g = 3, 1
        if q ** 3 * 33 <= FULL_GRID_MAX_CELLS:
            full.append({"q": q, "t": t, "phase": "p2"})
        else:
            dirrows.append(_plan_dir_row(q, t, g, "p2"))
    for q in T4_STRETCH:
        dirrows.append(_plan_dir_row(q, 4, 2, "p3"))
    # xcheck: 2 halves x 4 prefix-range shards of 64 (of 4^4=256) prefixes
    xchecks = [{"q": 193, "t": 2, "phase": "xcheck", "half": hf,
                "lo": lo, "hi": lo + 64}
               for hf in (0, 1) for lo in range(0, 256, 64)]
    return full, dirrows, xchecks


def _plan_dir_row(q, t, g, phase):
    h = N64 // 2
    dirs = proj_directions(q, t - g)
    cells = (q ** (g + 1)) * (h + 1)
    ops_per_dir = 5 * h * cells                    # 4 passes + guard
    per_chunk = max(1, int(TARGET_SHARD_S * RATE_DERATED / ops_per_dir))
    chunks = [{"q": q, "t": t, "g": g, "phase": phase, "chunk_id": i,
               "dirs": [list(d) for d in dirs[i:i + per_chunk]]}
              for i in range(0, len(dirs), per_chunk)]
    return {"q": q, "t": t, "g": g, "phase": phase, "ndirs": len(dirs),
            "chunks": chunks,
            "est_s_per_chunk": ops_per_dir * min(per_chunk, len(dirs))
            / RATE_DERATED}


@app.local_entrypoint()
def main(phase: str = "shard0,p1,p2,xcheck",
         out: str = "m1_dli_m1_results.json", dry: bool = False):
    print(PREREG_VERBATIM)
    print(f"\ntheta = {THETA} (pose-time convention); coset column = k = 0; "
          f"n = {N64}, h = 32; orbit quantum = 64.")
    phases = set(phase.split(","))
    full, dirrows, xchecks = plan_shards()
    full = [s for s in full if s["phase"] in phases]
    dirrows = [r for r in dirrows if r["phase"] in phases]
    xchecks = [s for s in xchecks if s["phase"] in phases]
    nchunks = sum(len(r["chunks"]) for r in dirrows)
    print(f"\nSHARD PLAN: shard0={'shard0' in phases}, {len(full)} full-grid "
          f"rows, {len(dirrows)} direction-sharded rows ({nchunks} chunks + "
          f"{len(dirrows)} marginal workers), {len(xchecks)} xcheck workers")
    for r in dirrows:
        print(f"  dirs row q={r['q']} t={r['t']} g={r['g']}: {r['ndirs']} "
              f"directions in {len(r['chunks'])} chunks "
              f"(~{r['est_s_per_chunk']:.0f}s est/chunk)")
    if dry:
        print("\nDRY RUN -- nothing launched.")
        return

    if "shard0" in phases:                       # gate: blocks all on FAIL
        g0 = shard0_gate.remote({})
        print(f"\nSHARD 0 (banked 8-row replay + n64 B==C): "
              f"{'PASS' if g0['ok'] else 'FAIL'}")
        if not g0["ok"]:
            print(json.dumps(g0, indent=1, default=str))
            raise SystemExit("SHARD 0 FAILED -- run aborted, nothing scored")

    rows = []
    # full-grid rows
    for res in census_row_full.map(full, return_exceptions=True):
        if not isinstance(res, dict):
            raise SystemExit(f"full-row worker error: {res}")
        sp = res["spec"]
        rows.append((sp, decompose_row(sp["q"], N64, sp["t"],
                                       res["cn"], res["cs"], res["asum"])))
    # direction-sharded rows
    all_chunks = [c for r in dirrows for c in r["chunks"]]
    marg_specs = [{"q": r["q"], "t": r["t"], "g": r["g"]} for r in dirrows]
    chunk_res = list(census_row_dirs.map(all_chunks, return_exceptions=True))
    marg_res = list(row_marginals.map(marg_specs, return_exceptions=True))
    bad = [c for c in chunk_res + marg_res if not isinstance(c, dict)]
    if bad:
        raise SystemExit(f"worker error(s): {bad[:3]}")
    for r in dirrows:
        key = (r["q"], r["t"], r["g"])
        parts = [c for c in chunk_res
                 if (c["spec"]["q"], c["spec"]["t"], c["spec"]["g"]) == key]
        ndirs = sum(p["ndirs"] for p in parts)
        assert ndirs == r["ndirs"], \
            f"row {key}: {ndirs}/{r['ndirs']} directions returned"
        sum_dirs = [sum(p["sum_dirs"][k] for p in parts)
                    for k in range(N64 // 2 + 1)]
        marg = next(mm for mm in marg_res
                    if (mm["spec"]["q"], mm["spec"]["t"],
                        mm["spec"]["g"]) == key)
        cs = assemble_from_projection(r["q"], N64, r["t"], r["g"],
                                      sum_dirs, marg["n_ref"])
        rows.append(({"q": r["q"], "t": r["t"], "phase": r["phase"]},
                     decompose_row(r["q"], N64, r["t"],
                                   marg["cn"], cs, marg["asum"])))
    # xcheck: strategy A (prefix-range-sharded MITM halves) vs strategy B
    if xchecks:
        import numpy as np
        xres = list(xcheck_mitm64.map(xchecks, return_exceptions=True))
        if any(not isinstance(r, dict) for r in xres):
            raise SystemExit(f"xcheck worker error: {xres}")
        q, t = xchecks[0]["q"], xchecks[0]["t"]
        halves = {}
        for hf in (0, 1):
            parts = [r for r in xres if r["spec"]["half"] == hf]
            assert sum(r["spec"]["hi"] - r["spec"]["lo"]
                       for r in parts) == 256, "xcheck prefix range gap"
            halves[hf] = sum(np.frombuffer(r["grid"], dtype=np.int64)
                             .reshape(r["shape"]) for r in parts)
        csA = mitm_join(q, t, halves[0], halves[1], N64 // 2)
        ref = next((d for sp, d in rows
                    if sp["q"] == q and sp["t"] == t), None)
        if ref is None:
            raise SystemExit(f"xcheck needs the (t={t}, q={q}) p1 row -- "
                             "run xcheck together with p1")
        got = {k: v[1] for k, v in ref["table"].items() if v[1]}
        exp = {k: v for k, v in enumerate(csA) if v}
        assert got == exp, f"XCHECK MISMATCH at q={q},t={t}: {got} != {exp}"
        print(f"\nXCHECK PASS: literal 16+16 MITM == grid DP at "
              f"(t={t}, q={q}), all classes exact")

    # ------------------------------------------------------------- reporting
    print("\n" + "=" * 72 + "\nPER-ROW RECORD (n=64)\n" + "=" * 72)
    for sp, d in sorted(rows, key=lambda x: (x[0]["t"], x[0]["q"])):
        acc = ", ".join(f"k={a['k']}:{a['class_ratio']}x mass={a['mass']}"
                        f" ({a['quanta']:g} orb64, lam={a['lam']:.3g})"
                        for a in d["accidents"]) or "-"
        sm = d["stripped_mass_ratio"]
        bk = d["bulk_ratio"]
        print(f"t={d['t']} q={d['q']:>6}: raw={d['ratio']:7.3f} "
              f"strip_mass={sm if sm == sm else float('nan'):7.3f} "
              f"BULK={bk if bk == bk else float('nan'):7.3f} | acc: {acc}")
    # unscored diagnostic toward F-b bookkeeping
    charges = [math.log2(d["bulk_ratio"]) for _, d in rows
               if d["bulk_ratio"] == d["bulk_ratio"] and d["bulk_ratio"] > 0]
    if charges:
        print(f"\n[unscored F-b diagnostic] per-junction bulk log2-charges: "
              f"max={max(charges):.3f} bits, GM allowance 21/33="
              f"{21 / 33:.3f} bits/junction (aggregate form primary)")

    by_depth = defaultdict(list)
    for sp, d in rows:
        by_depth[d["t"]].append(d)
    fa_kill, fa_log = read_Fa(by_depth)
    print(fa_log)
    census_qs = set(FC_CENSUS)
    census_rows = [d for sp, d in rows if d["t"] == 2 and d["q"] in census_qs]
    fc_kill, fc_log = read_Fc(census_rows)
    print(fc_log)

    print("\nNON-FALSIFIERS (not scored, per the pose): raw unstripped "
          "ratios above; single orbit-quantized spikes consistent with the "
          "window mean; per-level/uniform/factorized proxies.")
    verdict = ("C2'' REFUTED by " +
               "+".join(x for x, k in (("F-a", fa_kill), ("F-c", fc_kill))
                        if k)
               if (fa_kill or fc_kill) else
               "C2'' SURVIVES its first adversarial round (M1) -- eligible "
               "for promotion per the F-round rule after maintainer review")
    print(f"\n{'=' * 72}\nM1 VERDICT: {verdict}\n{'=' * 72}")

    blob = {"prereg": PREREG_VERBATIM, "theta": THETA,
            "rows": [d for _, d in sorted(rows, key=lambda x: (x[0]["t"],
                                                               x[0]["q"]))],
            "Fa_fired": fa_kill, "Fc_fired": fc_kill, "verdict": verdict}
    with open(out, "w") as fh:
        json.dump(blob, fh, indent=1, default=str)
    print(f"results written to {out}")
