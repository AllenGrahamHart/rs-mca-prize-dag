# PRE-REGISTRATION — THE CROSSING GAP: the prime-row emptiness question (round 20, GENERATIVE + one adversarial check)

Round 20, 2026-08-06. Coordinator-authored brief; the pilot appends
its own registrations BEFORE any computation. The crossing low-w
core at PRIME rows (tau = 2, subcritical — EMPTINESS is the target
per the phase transition): the official primes sit provably in the
gap between the two closed ends (SP-COVER from below, CS from
above, 2^4.69 wide in w). Close or narrow the gap; and re-verify
the cliff the whole bracket stands on.

## 0. The state (quote verbatim before working)

- background/nodes/es_ternary_suppression_instruments — THEOREM CS
  (+ CS-M's window-free upgrade via LEMMA BR,
  notes/pilots_20260806/tern_master_statement/), SP-COVER/COS/
  SP-UNIFORM, SP-TERNARY, CATCH E-3 (the gap; re-labelled a
  shared-row property by the round-19 adversary bank).
- background/nodes/tern_master_threshold — tau = 2 at these rows;
  the per-tau target (emptiness); COROLLARY PT-2 (the 0.336-bit
  cliff); the untested cell (constant-weight Z-FLOOR at I2 — "the
  one place a genuinely new instrument might live").
- notes/pilots_20260806/efloor_sparsity/ — the even-condition lead
  (residual 5: "even-window conditions are used in none of the
  proofs, yet the census shows they matter... An even-condition
  SP-COVER would lower every threshold — the most obvious next
  step").

## 1. Pre-registered deliverables

- **(C1) THE EVEN-CONDITION EXTENSION.** Round 18's named next
  step: extend SP-COVER to use the EVEN window conditions. By
  LEMMA OE the even conditions live on sigma (the next stratum) —
  so an even-condition SP-COVER is a RECURSIVE statement: coverage
  at stratum a plus coverage of the reduced instance. Formalize the
  recursion, prove the extended coverage criterion, recompute
  w_cov(p) — the census says p = 7 empties at w = 7 while
  odd-alone never suffices: your extension must reproduce that
  cell. Then: how much of the 2^4.69 gap closes?
- **(C2) THE UNTESTED CELL — constant-weight Z-FLOOR at I2.** The
  round-19 adversary's residual 6. Z-FLOOR-M's scope note says the
  difference-multiplicity weighting is NOT the constant-weight
  functional — derive the constant-weight analogue: a floor for
  #{S of weight exactly r' : window conditions} via the collision
  identity restricted to the weight shell. If it exists, it is a
  NEW instrument at exactly the crossing instance; if the
  restriction breaks the identity, prove why (that too is new).
- **(C3) THE PT-2 CLIFF RE-VERIFICATION (adversarial check).** The
  bracket's lower endpoint w = 2^34 rests on RHL-LB (the proved
  floor a_L >= k + 2^34) and clears the supercriticality threshold
  by 0.336 bits. Re-derive RHL-LB's constant from its source with
  fresh eyes (the exactness of "2^34" — is it exact, floored, or
  conventional?); recompute the clearance under both the new-part
  and nested readings and both Lambda parities; state whether ANY
  banked reading places the endpoint below the threshold. If one
  does, that is a MAJOR catch (prime rows supercritical =>
  emptiness is false at the endpoint) — reproduction script + stop.
- **(C4) THE GAP VERDICT.** After (C1)-(C3): the exact remaining
  (p, w) gap for the prime-row emptiness question, and the honest
  list of what could close it (with the dead routes named — the
  SPD union bound is proved vacuous; do not resurrect it).

## 2. Pre-registered falsifiers / honesty clauses

- (C1)'s extension must reproduce the p = 7, w = 7 census cell or
  report the mismatch as a defect in the extension.
- (C3) is adversarial: the desired answer does not exist; report
  the clearance as computed, whichever way it falls.
- 2-power lengths; no shift-0 cells; name the functional
  (weighted/unweighted) in every measured claim (CATCH-19C rule).

## 3. Rules of engagement

- DRAFT ONLY: write only inside notes/pilots_20260806/crossing_gap/.
  Never edit dag.json, node shards, tools/, or push. Do NOT read
  notes/pilots_20260806/gamma_shell/ (sibling this round). Do NOT
  read CAMPAIGN_LEDGER entries appended after the "ROUND 20
  LAUNCHED" marker.
- COMPUTE LAW: never bare python3, INCLUDING file patching and JSON
  peeking — tools/ramguard tiny|local -- python3 ..., literal --,
  from repo root /home/u2470931/smooth-read-solomin/prize.
- Verbatim quotes with file:line for every statement relied on.
- Do NOT write REPORT.md — your final message IS the report; the
  coordinator persists it verbatim.

---

# PILOT REGISTRATIONS (appended 2026-08-06, BEFORE any computation)

Opus pilot, round 20. Every prediction below is registered before a
single line of code is run. Falsifiers are stated with the prediction.
CATCH-19C rule adopted throughout: every measured claim names the
functional (TERNARY-odd / TERNARY-deep / TERNARY-orbit-corrected /
GLOBAL (ES-G) / PER-WEIGHT) and the reading (new-part vs nested;
Lambda parity).

## G0. Scope of what I will and will not touch

I will NOT resurrect the SPD union bound (proved vacuous,
`efloor_sparsity/PROOFS.md:367`). I will NOT claim CC-sparsity. All
prize-row statements are deductions from theorems proved for all `n`,
never extrapolations from small-`n` censuses.

## G1 (C1). The even-condition recursion is the 2-adic Haar tower

REGISTERED CLAIM. Writing `m^{(a)}_j := #{i in S : i = j mod 2^{m-a}}`
and `eps^{(a)}_j := m^{(a)}_j - m^{(a)}_{j + 2^{m-a-1}}`, the FULL
window condition set `{f_S(xi^s) = 0 : 1 <= s <= w-1}` decomposes
EXACTLY by `a = v_2(s)`: writing `s = 2^a t` with `t` odd,
`f_S(xi^s) = eps^{(a)}(theta_a^t)` with `theta_a = xi^{2^a}` of order
`n_a = 2^{m-a}`. `S <-> (eps^{(0)},...,eps^{(m-1)}, r')` is a
bijection. LEMMA OE is the single step `a -> a+1`.

REGISTERED PREDICTION G1.1: `strat(S) >= b` iff
`eps^{(0)} = ... = eps^{(b-1)} = 0`.

REGISTERED PREDICTION G1.2 (the decisive one, and I expect it to be
NEGATIVE for the mandate's hope): SP-COVER applied at level `a`
requires `w_a := floor((w-1)/2^a)+1 >= w_cov(p, n_a)`; since `w_cov`
is `n`-uniform (LEMMA COS) this is `w >= 2^a (w_cov(p) - 1) + 1`,
STRICTLY INCREASING in `a`. Hence coverage at any level `a >= 1`
NEVER fires before level `a = 0`, and **the even conditions cannot
lower the SP-COVER threshold at all**. FALSIFIER: any `(p, n, w)`
with `m - a >= v_2(p^2-1)` where level-`a` coverage holds and
level-`0` coverage fails.

REGISTERED PREDICTION G1.3: the level-`a` conclusion needs the
integrality gate `p > 2^a` (entries of `eps^{(a)}` lie in
`[-2^a, 2^a]`). At `a = 0` this is LEMMA AB(2).

REGISTERED PREDICTION G1.4 (the positive half): when level-0 coverage
DOES hold, coverage holds simultaneously at every level
`a <= A_cov := floor(log2((w-1)/(w_cov(p)-1)))`, so the conclusion
UPGRADES from `strat(S) >= 1` to `strat(S) >= A_cov + 1`, which
forces `2^{A_cov+1} | r'` — a divisibility exclusion absent from
SP-COVER.

REGISTERED PREDICTION G1.5 (the census gate): the `p = 7`, `n = 32`,
`w = 7` cell (a=0 class EMPTY while `w_cov(7) = 12`) is explained NOT
by coverage at any level but by the COUPLED criterion: `eps^{(0)}`
ternary in the odd code `C_odd` AND `m^{(1)}` in the even code
`C_even` with `supp(eps^{(0)}) = {j : m^{(1)}_j = 1}`. I predict the
coupled criterion certifies emptiness at that cell and that the
odd-only (SP-TERNARY) criterion does not. FALSIFIER: the coupled
count at `(32,7,7)` is nonzero, or the odd-only count is zero.

REGISTERED PREDICTION G1.6 (the gap): I predict **0.00% of the
2^4.6869 gap closes** by the even-condition route, because the gap is
governed by `w_cov(q)` and G1.2 says `w_cov` does not move. Reported
as computed either way.

## G2 (C2). The constant-weight Z-FLOOR at I2

REGISTERED CLAIM (the candidate instrument). At the I2 deep stratum
(`theta` of order `2L`, `Q := p^{delta_a}`,
`X_{r'} := {S' <= Z/2L : |S'| = r', sum_{i in S'} theta^i = 0}`), for
`r'` EVEN:

```text
|X_{r'}|  >=  N(r'/2, r'/2)  >=  C(L, r'/2)^2 / Q.        (CW-FLOOR)
```

where `N(W,W) = #{(a,b) in Y_W^2 : psi(a) = psi(b)}`, `Y_W` the
weight-`W` subsets of `[0,L)`, `psi(a) = sum_{j in a} theta^j`.

REGISTERED PREDICTION G2.1: the proof needs the coincidence that the
constant-weight collision multiplicity `C(L-U, W-U/2)` at `W = r'/2`
is IDENTICALLY LEMMA TC's fibre size `C(L-U, (r'-U)/2)`.

REGISTERED PREDICTION G2.2 (the break): the cross-shell terms
`N(W,W')`, `W + W' = r'`, `W != W'` admit NO lower bound (Cauchy-
Schwarz bounds them ABOVE, not below), so Vandermonde's
`sum_{W} C(L,W)C(L,r'-W) = C(2L,r')` cannot be recovered; the floor
loses exactly `log2 C(2L,r') - 2 log2 C(L,r'/2)` bits. I predict that
loss is `3.33` bits at the prize stratum (`L=128`, `r'=126`), and
that for `r'` ODD the route is UNAVAILABLE (every equal-weight
collision has balanced, hence even-support, `eps`).

REGISTERED PREDICTION G2.3 (verdict at the crossing instance):
CW-FLOOR fires iff `delta_a * log2 p < log2 C(L,(L-2)/2) = 124.149`
at `v = 34`, i.e. it is STRICTLY INSIDE THEOREM DSA's regime
(`< 126`) by `1.851` bits, and therefore **VACUOUS at every `e = 1`
prime row** (which need `log2 p >= 128`). FALSIFIER: a computed
threshold outside `[124, 125]`.

REGISTERED PREDICTION G2.4 (the positive content): at TOWER rows
CW-FLOOR converts round-18's HEURISTIC excess estimate into a PROVED
count. At the banked witness row (`p = 3*2^41+1`, `e = 6`,
`delta_a = 1`) I predict a proved `|X_126| >= 2^{205.7}` against the
structural `C(128,63) = 2^{124.149}` and the heuristic `2^{209.0}`.

## G3 (C3). Adversarial re-verification of the PT-2 cliff

REGISTERED PREDICTION G3.1 (exactness of `2^34`): `sigma_cyc = dc + s`
with `d = 1`, `c = 2^33`, `s = c-1` is the EXACT integer `2^34 - 1`;
no floor, no rounding. `a_L >= k + 2^34` is the integer successor and
is EXACT. But the CHOICE `(c,d,s) = (2^33,1,2^33-1)` is
CONVENTIONAL: it is extremal only among maximal-prefix instances of
the printed cyclic construction certified uniformly at `q = 2^256`.
DIRECTION CHECK: RHL-LB is a LOWER bound on `a_L`, so any improvement
moves `w` UP, away from the threshold.

REGISTERED PREDICTION G3.2 (the adversarial one). I predict the
`0.336`-bit clearance is computed at `log2 p = 256` ONLY, and that
the threshold is `p`-dependent:
`w_tern(p) = 2^41 * log2(3) / log2(p)` (TERNARY functional, odd-part
reading). I predict that the LIVE admissible `e = 1` prime range is
`log2 p in [129.585, 256)` (because `B* in {1,2}` is already closed
exactly by (RHL-B12), so the open crossing needs `B* >= 3`), and that
`w = 2^34` sits BELOW the threshold for `log2 p < 202.875` — i.e.
**for a majority of the live prime range the endpoint is
supercritical, not clear by 0.336 bits.** If this holds it is a
SCOPE DEFECT in the minted watch line; I will check honestly whether
it is already banked upstream (subtraction, hard law 5) before
calling it new. FALSIFIER: a banked constraint pinning the live
`e = 1` prime range to `log2 p > 202.875`.

REGISTERED PREDICTION G3.3 (parity invariance): the odd-part
(`g = w/2`, `h = n/2`) and full-window (`g = w-1`, `h = n`) readings
of the TERNARY functional give the SAME threshold `log2 p = 202.875`
at `w = 2^34`; the deep-stratum (I2) reading agrees. The
orbit-corrected reading gives `194.875`; the retired PER-WEIGHT
functional `251.628`; the GLOBAL (ES-G) functional `256`.

REGISTERED PREDICTION G3.4: under the GLOBAL (ES-G) reading the
endpoint is below threshold for EVERY admissible row (`log2 q < 256`).

## G4 (C4). Gap verdict

REGISTERED PREDICTION G4.1: after G1-G3 the remaining open `(p,w)`
region for prime-row emptiness is
`{ w in (2^34, 2^37.3131] } x { log2 p in [129.585, 256) }` minus the
CS-covered part, and the even-condition route removes NONE of it.
I will state the exact residual as computed.

## G5. Honesty / fail-closed protocol

Every script stage exits nonzero on any failed check; a permanent
`failclosed` stage injects a false check and MUST exit 1. All runs go
through `tools/ramguard tiny|local -- python3` with a literal `--`.
No file is written outside `notes/pilots_20260806/crossing_gap/`.
`gamma_shell/` is never read; CAMPAIGN_LEDGER after the ROUND 20
marker is never read.
