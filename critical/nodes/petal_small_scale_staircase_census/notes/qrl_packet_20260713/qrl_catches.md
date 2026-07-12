# Catches (ledger continues from #108)

## Catch #109 — ESP transport of the minted residual FAILS at the minimal official field for every scale with n' > ~n^(1/3)

The banked reduction (census dag statement) routes the residual through
`exact_support_interleaving_projection`, whose bound requires
`D = (q-r)^2 - L_P q > 0`, i.e. essentially `q > L_P + 2r`. Feeding it the
minted bound `L_P = (63/64)(n/M)^6` at the minimal official field `q = n^2`
requires `(n/M)^6 < ~n^2`, i.e. `n' < n^(1/3)` (`M > n^(2/3)`).

Exact exhibit (S7): s = 13, M = 128, n' = 64, own-band a = 33:
`D = (2^26 - 31)^2 - (63*64^6/64)*2^26 = -4,535,124,828,922,838,079 < 0`.
Per-s largest n' whose minted bound still feeds ESP at q = n^2:
s=13: 32, s=17: 32, s=21: 128, s=25: 256, s=29: 512, s=33: 2048, s=37: 4096,
s=41: 8192. At s = 13 NO open scale (n' >= 64) transports.

Consequence: even a full proof of the minted claim would NOT close the census
gate through the banked chain at q = n^2 for scales with n' above the per-s
threshold — the residual as minted is weaker than what the chain consumes.
The fix is one of: (a) mint the missing lemma at strength
`L_P <= min((63/64) n'^6, q - 2n')` (or prove the much smaller true size,
conjecturally O(n'^2), which transports everywhere: D > 0 needs only
`q >= 4n'^2` — see T2's arithmetic); (b) find an ESP-free transport (T1's
class-level injection is one, but it is only sub-exponential-free up to
n' = 32); or (c) pin a larger official field floor for the gate. NOTE: within
this packet's PROVED windows the issue is moot (T1/T3 transport ESP-free;
T2's Johnson input n'^2 satisfies D > 0 with factor <= 2 at q >= 4n'^2); the
catch bites exactly on the open window.

## Catch #110 — the deep-regime window is arithmetically real but unconsumable, and (for s <= 32) strictly inside the unconditional support window

Verified (S3): at q = n^2 the deep-regime condition `q > 2^((1+eps)n')`
covers n' < 2s/(1+eps): n' <= 16 (s <= 16), n' <= 32 (17 <= s <= 32),
n' <= 64 (s >= 33; exactly 36 (s,rho) x scale pairs beyond n' = 32). Two
independent blockers: (i) `f2_deep_regime_exactness` concludes for ALMOST
EVERY prime in a dyadic window (sporadic primes dividing fixed cyclotomic
norms are not excluded for a FIXED row) — a row-uniform claim cannot consume
it; (ii) its conclusion (F2 extras vanish) is not a list bound — no banked
bridge converts exactness of the moment dichotomy into an aperiodic
exact-agreement list bound. Meanwhile T1 covers n' <= 32 unconditionally, for
every prime. Net value of the deep regime for this residual: zero except as
heuristic support at (n' = 64, s >= 33). The task-sketch's proposed coverage
plan ("deep regime covers the top, Johnson the rest") fails on both ends:
the top is covered by counting supports, and Johnson does not reach the
sub-Johnson band that IS the residual.

## Catch #111 — the minted claim does not parse at the scales M in (k, t] (rho = 1/8: M = 2k; rho = 1/16: M in {2k, 4k}); closed here at class level

`k/M` is non-integral there and the descent hypothesis `M | gcd(n,k)`
excludes them, yet those dyadic scales lie in the census range `2 <= M <= t`
(87 official (row, M) pairs; S3) and the intrinsic-scale ledger's hypothesis
("the scale-M class injects into a primitive quotient-row family...") had no
supplier. CLOSED in this packet: T1's class-level support injection (needs
only M | n; gives <= C(n', A/M) with n' in {4,8}) and T3's one-fiber lemma
(class <= n/M for every M >= k, three-line proof) price them. Banked-data
exhibit: the (16,6) census records' (4,8) cells are M ∤ k cells (M = 4, k =
6); verified <= C(4,2) = 6 (S4). Recommend: append the M > k pricing to the
census node statement so the ledger's scale partition has an explicit
supplier at every scale.

## Positive reconciliations (not catches; banked in Lemma 0)

- No interpolation-degenerate cell exists: M | A and M | k force the
  descended agreement a >= k'+1 at every consumed cell (the task-sketch's
  flagged crux dissolves).
- The edge band A = k+sigma is EMPTY for all scales M >= 2 at official rows;
  the own-band is the single cell a = k'+1.
- "Multiplicity 1 everywhere" in the banked census is a theorem (A > k =>
  support determines codeword), so class count = codeword count at every
  cell; the dag's codeword-vs-class distinction is an equality here.
