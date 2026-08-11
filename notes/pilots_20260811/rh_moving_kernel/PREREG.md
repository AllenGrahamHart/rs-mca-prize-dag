# PREREG — rh_moving_kernel (round 33)

Coordinator brief. Constraints: CONSTRAINTS.md in this dir (binding).
AUDIT-AND-DRAFT: any surgery stays coordinator-gated.

## Anchors (read these two FIRST, then register blind priors)

1. `notes/pilots_20260810/rh_farca_upper/REPORT.md` (round 32)
2. `background/nodes/rate_half_ca_hankel_fixed_kernel_branch/statement.md`

## Mandate

R-MOVING / R-DEEP: the far-CA deep stratum is the safe half's whole
exposure (UB-NEAR discharged the rest). Round 32 located the crack:
in the wide regime the generic kernel of the syndrome Hankel pencil
is a TWO-GENERATED apolar truncation (generators of degrees p and
R+1-p, both entering since p >= R+1-r); the kernel splits as
(r+1-p) shifts of P and (r+p-R) shifts of Q'; the two multiplicities
sum to 2r+1-R ~ 2^40 while their weighted Kronecker sum is
<= rho <= 2^34 — SO AT LEAST ONE GENERATOR IS FORCED FIXED (defined
over F, slope-independent), and column-farness forbids THAT
generator from being D-split-squarefree — exactly the (HK2)
mechanism's hypothesis, half-satisfied for free. YOUR JOB: bound the
slopes contributed by the OTHER (moving) generator — the wide-regime
replacement for (MI1)/(MI2).

## Deliverables

**D1 — THE FORCED-FIXED LEMMA, proved.** Make round 32's
multiplicity arithmetic a theorem: state exactly which generator
(low or high degree) is forced fixed, under which inequality on
(r, R, rho), with the Kronecker identity quoted (sum eps + sum eta
+ delta = rho). Verify at the round-32 cells (the d6 pencils are
banked in rh_farca_upper/).

**D2 — THE MOVING-GENERATOR BUDGET.** For a bad slope gamma, the
kernel member in D_r(D) (the split locator) decomposes over the two
generators. The fixed generator contributes a FIXED factor
(column-far => not D-split-squarefree). Derive what the moving
generator must supply and bound the slope count: candidate shapes —
a divisor count on the fixed factor's complement (the (MI2) shape
with the fixed generator playing Q_Z), or an (HK2)-style minor
argument on the moving block alone. ANY finite bound on the deep
stratum is the first ever.

**D3 — SMALL-SCALE STRUCTURE.** At the wide-regime cells (copy
rh_farca_upper/d6_kernel_structure.py + d3_wide.py): measure the
two-generator split per bad slope (degrees p, R+1-p; which is
fixed; what the moving factor does at each bad slope). Test D2's
candidate bound against measured T. Pre-register expectations.

**D4 — VERDICT + R-KER cross-check.** Does the bound reach
B_ca^far(k+2^34) < 2^128? If partial, the exact stratum covered.
Cross-check against LB1 (its pencils MUST satisfy your bound —
T = r+1 there; if your bound is < r+1 anywhere LB1 lives, your
bound is WRONG — use LB1 as the built-in falsifier). Misses first.

## Blind priors to register

P(forced-fixed lemma proves cleanly), P(any finite deep-stratum
bound this round), P(the bound beats 2^128 at the razor), which
generator you expect forced (low/high degree).

## Pilot registrations

Registered by rh_moving_kernel (round 33) after reading ONLY the two
named anchors (`rh_farca_upper/REPORT.md`, `fixed_kernel_branch/statement.md`)
and BEFORE any grep, any `ls`, any other file, and any interpreter run.

### R0 — the four required priors

- **R0-a. P(forced-fixed lemma proves cleanly) = 0.85.** The argument I
  expect is pure counting on Kronecker right minimal indices: the
  degree-`r` piece of a binary complete-intersection apolar ideal
  `(P_gamma, Q'_gamma)` with `deg P = p <= deg Q' = R+1-p` has basis
  `(r+1-p)` shifts of `P` plus `(r+p-R)` shifts of `Q'`; a generator
  that is NOT defined over `F` forces every one of its shifts to have
  right minimal index `>= 1`; `sum eps + sum eta + delta = rho` caps the
  number of index-`>=1` columns at `rho`. Residual 0.15 risk sits in one
  step, not the arithmetic: that "generator moves" ⟹ "all its shifts
  have `eps_i >= 1`" in the Kronecker normal form (basis-choice /
  column-space vs. spanning-set gap).
- **R0-b. P(any finite deep-stratum bound this round) = 0.45.** I mean:
  an unconditional finite upper bound on `#{CA-bad slopes of error
  weight in (R/2-2, r]}` for a column-far pair at the razor, better
  than round 32's `C(n,a) = 2^{2.2e12}`. I expect to reach a
  *dichotomy* with high probability and a *bound on the second horn*
  with much lower probability.
- **R0-c. P(the bound beats 2^128 at the razor) = 0.22.**
- **R0-d. Which generator is forced fixed: THE LOW-DEGREE ONE (`P`,
  degree `p <= (R+1)/2`).** Reason: its shift multiplicity is
  `m_P = r+1-p` and the high generator's is `m_Q = r+p-R`, with
  `m_P - m_Q = R+1-2p >= 0`; the larger block is the one that cannot
  afford a positive index.

### R1 — the structural predictions I will test (windows fixed now)

- **PR-1 (multiplicity identity).** `m_P + m_Q = 2r+1-R = r+1-rho`
  exactly, at every measured wide-regime pencil (this is `dim ker`, so
  it is also a self-check on my kernel code). P = 0.90.
- **PR-2 (forced-fixed inequality).** The lemma's hypothesis is
  `rho < (r+1)/2`, equivalently `r+1-rho > rho`; at the razor
  `rho <= R-r = 2^34` and `r+1-rho ~ 2^40`, so it holds with ~6 bits of
  slack per unit and I predict the exact razor slack ratio
  `(r+1-rho)/rho >= 63.0` (window `[62.9, 64.1]`). P = 0.75.
- **PR-3 (the BOTH-FIXED corollary — the one I most want).** I predict
  the lemma is not merely "one of the two", but that BOTH generators are
  forced fixed unless `p` is small; specifically both blocks have
  multiplicity `> rho` whenever `R+rho-r < p < r+1-rho`, and since
  `p <= (R+1)/2 < r+1-rho` holds at the razor, the ONLY escape from
  `(HK1)` is `p <= R+rho-r <= 2rho = 2(R-r) = 2^35`. **So I pre-register
  the dichotomy: at the razor, either `(HK1)` holds and `T <= rho <=
  2^34` by the banked `(HK2)`, or `deg P <= 2^35`.** P(this dichotomy
  survives) = 0.60. If it survives it is the round's main object.
- **PR-4 (moving multiplicity cap).** In the escape horn, the moving
  block is the HIGH generator with multiplicity `m_Q = p - rho <= rho`,
  so the moving part of the kernel has dimension `<= rho <= 2^34` and
  `sum eps_i <= rho` over `<= rho` columns. P = 0.55.
- **PR-5 (`p <= (R+1)/2` at the razor forbids the high horn).** The
  inequality `(R+1)/2 < r+1-rho` at the razor reduces to `3R < 4r+1`;
  I predict it holds with `r/R = 1 - 2^-6 = 0.984375` against the
  needed `0.75`. P = 0.85.

### R2 — D3 measurement expectations (pre-registered)

- **PR-6.** At the round-32 wide cells `(7,2,a=4,r=3,R=5)` and
  `(8,3,a=5,r=3,R=5)` the generic `rho = R-r = 2`, so `r+1-rho = 2`
  and `rho = 2`: **the forced-fixed hypothesis `r+1-rho > rho` FAILS at
  every reachable cell**. I register this as a ZERO-POWER declaration
  *in advance*: the d6 cells can verify the multiplicity arithmetic and
  the two-generator split, but they CANNOT exhibit the forced-fixed
  conclusion, because the razor's `~6 bits` of slack does not exist at
  `n = 7`. P(this is confirmed) = 0.80. I will look for any cell with
  `r+1-rho > rho`, i.e. `2r+1 > R + rho`, i.e. (generically) `3r+1 > 2R`
  — needs `r > 2R/3` with `R-r >= 2`, so the smallest candidates are
  `R = 6, r = 4` (`rho = 2`, `r+1-rho = 3 > 2`) — I predict such cells
  exist at `n` around `10`-`13` and I will build one.
- **PR-7 (degrees measured).** At the d6 pencil `(q=11, r=3, R=5,
  rho=2)` I predict the apolar generator degrees are `p = 3` and
  `R+1-p = 3` at the generic slope (i.e. `p = (R+1)/2` exactly, the
  balanced case), giving `m_P = 1`, `m_Q = 1`, and kernel gcd degree
  `0` — which is exactly round 32's measured "gcd degree 0 at 10 of 11
  slopes". Window: `p in {2,3}`. P = 0.55.
- **PR-8 (LB1 falsifier).** LB1's pencils have `T = r+1` bad slopes and
  `dim K_0 = 0`. Any bound I derive MUST be `>= r+1` wherever LB1 lives.
  I pre-register that LB1 lives ONLY where the forced-fixed hypothesis
  fails (`r+1-rho <= rho`), since `dim K_0 = 0` and my lemma forces
  `dim K_0 >= max(m_P, m_Q) >= (r+1-rho)/2`. **If I find an LB1 pencil
  with `r+1-rho > rho` and `dim K_0 = 0`, my lemma is REFUTED.** This is
  the built-in falsifier and I will run it. P(lemma survives) = 0.70.

### R3 — zero-power declarations made in advance

1. No cell reachable by exhaustive search has `rho_cell < 1`; nothing I
   measure is in the razor's own statistical regime (inherited from
   round 32, restated).
2. Per PR-6, the round-32 d6 cells are structurally incapable of
   exhibiting the forced-fixed conclusion; they can only check the
   split/multiplicity arithmetic.
3. Any bound whose proof needs `deg P <= 2rho` is conditional on the
   escape horn and is NOT an unconditional bound on `B_ca^far`.
4. Sampled negatives about `(HK1)` density do not transport to the
   razor (round 32's `0/1700` is a small-`n` fact).

### R4 — compute plan

Stdlib only, `tools/ramguard` from the repo root with a literal `--`
and an explicit `RAMGUARD_TIMEOUT` per call. Copy
`notes/pilots_20260810/rh_farca_upper/d6_kernel_structure.py` and
`d3_wide.py` into my dir before running. Checkpointed results files
after every emit; `dag.json` never opened.

