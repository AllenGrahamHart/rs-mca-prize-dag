# PREREG — r38_side_door (round 38)

Coordinator brief. Constraints: CONSTRAINTS.md in this dir (binding).
AUDIT-AND-DRAFT: any surgery stays coordinator-gated.

## Anchors (read these two FIRST, then register blind priors)

1. `notes/pilots_20260811/r37_share3_gap/REPORT.md` (round 37)
2. `notes/pilots_20260811/r36_m4_nonsplit/REPORT.md` (round 36)

## Mandate

THE SIDE DOOR — the cheapest potentially-decisive item on the
board. Round 37 derived the (SHARE3-4) prescribable-merge budget
(8 vs demand 11) and the coordinator CHECKED THE LOOPHOLE LEGAL:
one fibre whose slope cubic has a DOUBLE ROOT drops the slot
count 24 -> 23, so **10 merges suffice — which two rounds have
already achieved** — at the cost of its three points having
|A_x| = m-1 = 3, i.e. sum_x(m-d_x) = 3 = 1+O with O = 2, which
fits (SAT2) (O <= 3) and (SAT4) (sum <= 4) EXACTLY at the
identity. YOUR JOB: build the configuration and run the FULL
pipeline. If it survives, it is an m = 4 (BIV-CURVE) witness
candidate — the biggest single event available to the campaign.
If it dies, name the exact axiom that kills it (the per-side and
incidence bookkeeping at the three deficient points is the
unchecked part).

## Deliverables

**D1 — THE DEGENERATE-FIBRE ARITHMETIC, COMPLETE, BEFORE
SEARCHING.** With one fibre {x_1,x_2,x_3} carrying the slope
cubic (Z-alpha)^2(Z-beta): each x_i has A_x = {g-or-h, alpha,
beta} of size 3 = m-1 (the double root contributes ONE slope).
Derive the full ledger: the type-2 slot count (23), the merge
demand (10 for s = 13), the per-side caps at the deficient points
(X'_alpha picks up 3 incidences from one fibre — does the cap
2m-2 = 6 hold? does the PER-SIDE cap m-1 = 3 hold given the
(2,1)/(1,2) split?), the (OUT-m)/(DEG-m) corrected forms at
O = 2, and the (SAT4) identity placement (the deficient points
are INSIDE W — check the round-34 charge bookkeeping: inside
deficiency charges m-2 per unit, so sum eps~ = 3*(m-2)? derive
exactly). ANY axiom that fails here kills the door — check ALL
of them before building.

**D2 — THE BUILD.** Take 10-merge configurations (both prior
rounds have them: |slopes| = 14 draws = 10 merges; your own
regeneration is fine) and impose the degenerate fibre: in the
pencil picture the fibre's cubic has disc = 0 — one further
algebraic condition on the line in P^3; the round-37 Segre
budget arithmetic says what it costs (derive: is a double root
a cost-1 or cost-2 prescription?). Alternatively impose it first
and search for 10 merges around it. Two fields (q = 193, 257).
Target: a complete 13-slope, 27-point, O = 2 configuration
passing D1's full axiom ledger.

**D3 — THE PIPELINE ON ANY SURVIVOR.** W assembly (27 points:
8 fibres + the middle fibre — wait, with the degenerate fibre
among the 8: derive the exact W bookkeeping in D1); per-side
split on actual points; mu(x)-at-middles (the never-verified
check); build G explicitly ((SHARE3-4) form); outside
completion; the bivariate system via bank 2's biv_core.py (COPY
IN AND AUDIT ITS OUTPUT PATHS FIRST — it writes at import); the
full incidence table; layer A run on the result (the witness
would be the first m >= 2 object to face it with a completion).
Two fields. If no survivor: the named killing axiom, with the
measured margin.

**D4 — VERDICT.** The (BIV-CURVE) m-boundary of record; misses
first; cross-pilot flag (do NOT read siblings).

## Blind priors to register

P(D1's ledger closes — no axiom kills the door on paper),
P(a 13-slope O=2 configuration is built), P(it survives the full
pipeline => m=4 witness), P(the killing axiom, if any, is the
per-side cap), expected best outcome (a phrase).

## Pilot registrations

**R0 — WHAT I HAD READ WHEN I WROTE THIS.** Exactly the two named
anchors: `r37_share3_gap/REPORT.md` and `r36_m4_nonsplit/REPORT.md`.
No grep, no ls, no Read of any node/statement, no interpreter call.
Everything below is derived on paper. Any of it that the banked
statement contradicts is reported as a registration error, not
edited.

### R1 — THE DEGENERATE-FIBRE LEDGER (D1), DERIVED BLIND

**R1.1 Placement.** `m=4`: `N=64, rho=15, T=17, T_1=2, T_2=rho=15,
a=7m-1=27, delta=m-1=3`, `|S_g ^ S_h| = 3`, `|S_g D S_h| = 24`.
`W` = 8 outer fibres of `w` (24 points) + 1 middle fibre (3 points)
= 27. **The degenerate fibre must be one of the 8 OUTER fibres,
never the middle fibre**: the middle fibre's cubic must supply, per
r36's reading, two type-2 slopes plus `mu(x)` at each of 3 middles,
i.e. 3 DISTINCT roots with a distinct `mu` per middle; a double root
there leaves only 2 values for 3 middles. `P = 0.80`.

**R1.2 Slot identity.** Normal: `8 x 3 = 24` slot-incidences. One
outer fibre with slope cubic `(Z-alpha)^2(Z-beta)` has 2 DISTINCT
type-2 slopes, so `SLOTS = 23`. With `s = SLOTS - n_2`,
`n_1 = SLOTS - 2 n_2`, `X'_gamma = 3 d_gamma <= 2m-2 = 6` hence
`d_gamma <= 2`, and `s <= T_2 - 2 = 13` (two slopes reserved to the
middles), `13 slopes <=> n_2 >= 10`. **10 merges suffice, and both
prior rounds already reach 10.** `P = 0.90`.

**R1.3 (DEG-m) IS THE KILLER, AND IT IS AN IDENTITY IN THE SLOT
COUNT WITH THE MERGE COUNT CANCELLED.** In the form round 36 used
(`r36 REPORT.md:93`): `n_1 + 2(rho - s) <= 2m-2 = 6`. Substituting
`n_1 = SLOTS - 2n_2` and `s = SLOTS - n_2`, **`n_2` cancels**:

> `n_1 + 2(rho - s) = 2 rho - SLOTS = 30 - SLOTS`, so
> **(DEG-m) <=> `SLOTS >= 2 rho - 2m + 2 = 24`**, met with EQUALITY
> at `SLOTS = 24` and **violated by EXACTLY ONE (7 vs 6) at
> `SLOTS = 23`, for every `n_2`.**

So the door pays for its cheaper merge demand with a (DEG-m)
violation of exactly one unit, and no choice of merge count can
dodge it. `P(the cancellation algebra above is right) = 0.85`.
`P(the door dies at (DEG-m) in its uncorrected form) = 0.75`.
`P(an O-corrected (DEG-m) with RHS 2m-2+O or 2m-2+1 rescues it)
= 0.40`.

**R1.4 Per-side, and the multiplicity question that decides it.**
Merge graph bipartite between four `(2,1)`-triples and four
`(1,2)`-triples; a merged slope has per-side counts `2+1` and `1+2`
= `(3,3)` = the per-side cap `m-1 = 3` EXACTLY, total `6 = 2m-2`
EXACTLY. The double root changes this only if `X'` counts root
MULTIPLICITIES rather than POINTS. **`P(X' counts points, so
X'_alpha picks up 3 and not 6 from its own fibre) = 0.75.`** If it
counts multiplicity, `alpha` is at `X' = 6` from one fibre alone,
cannot merge, the degenerate fibre has merge-degree `<= 1`, and the
door dies harder. `P(the per-side cap is the killing axiom) = 0.20`.

**R1.5 The merge graph at `SLOTS = 23`, `n_2 = 10`.** `n_1 = 3`,
`s = 13 = 10 + 3`. Bipartite simple (pair multiplicity 1 by (OV) at
equality), 10 edges on `4+4`, vertex degree `<=` that fibre's slot
count, so the degenerate fibre has degree `<= 2`; per-side degree
sums are `10` and `10`, giving `(3,3,3,1)` or `(3,3,2,2)` on each
side. Unmerged slots: `3` (one on the degenerate fibre's side if it
sits at degree 2, two on the other). `P = 0.75`.

**R1.6 (OUT-m) is unaffected.** `13` outer slopes + `2` middle-only
slopes `= 15 = rho`, so no type-2 slope is unused; `X'+2X'' >= m-1`
reads `3d >= 3` and holds for every used slope. `P = 0.85`.

**R1.7 (SAT2)/(SAT4)/the `eps~` charge.** Each of the three
deficient points loses exactly one slope, so
`sum_x (m - d_x) = 3`; with the brief's identity `= 1 + O` this
forces `O = 2`, inside `(SAT2)`'s `O <= 3` and `(SAT4)`'s `sum <= 4`
with slack 1 in each. Round-34 inside charge, guessed:
`sum eps~ = (deficiency units) x (m-2) = 3 x 2 = 6`.
`P(the inside charge is exactly 3(m-2) = 6) = 0.35` — deliberately
low, I am reconstructing this from the brief's phrasing and have not
read the axiom.

### R2 — WHAT A DOUBLE ROOT COSTS (D2), DERIVED BLIND

**R2.1 A PRE-REGISTERED CORRECTION TO THE BRIEF.** D2 says *"in the
pencil picture the fibre's cubic has disc = 0 — one further
algebraic condition on the line in `P^3`"*. **That is the wrong
cubic.** The pencil cubic `P - t_* Q` in `P^3 = P(binary cubics)`
has for its roots the three POINTS `x_1,x_2,x_3` of the fibre;
`disc = 0` there collapses the fibre to `<= 2` points and destroys
`|W| = 27`. The degeneracy lives in the SLOPE cubic
`gamma |-> R(t_*,gamma) = w(t_*)^T Psi v(gamma)` — a condition on
`Psi in P^15`, **not** on the line in `P^3`, and therefore it costs
NOTHING in the round-37 Segre pencil budget and everything in the
`Psi` budget. `P = 0.88`.

**R2.2 The cost: two linear conditions = exactly one merge-edge's
worth.** Prescribing `alpha` as a double root over `t_*` is
`w(t_*)^T Psi v(alpha) = 0` and `w(t_*)^T Psi v'(alpha) = 0` with
`v'(gamma) = (3gamma^2, -2gamma, 1, 0)`: two independent rank-one
functionals spanning `w(t_*) (x) span{v(alpha), v'(alpha)}`. The
available-direction variety `{[w(t_*) (x) (a v(alpha) + b v'(alpha))]}`
has dimension `1 + 1 = 2` in `P^15` — **the same dimension as round
37's `Sigma_ij`** — so it obeys round 37's cost table verbatim:
cost 2 until the span reaches dim 14, cost 1 there.
**Prescription cost 2; bare-existence cost 1** (`disc_Z R(t_*,.) = 0`
is a single degree-4 NON-linear condition on `Psi`). `P = 0.80`.

**R2.3 THE INVARIANCE PREDICTION — the round's central registered
claim.** The side door is EXACTLY BUDGET-NEUTRAL, in both currencies:

> (i) *Instrument currency.* `k` edges + the tangency cost `2k+2`
> (or `2k+1` when `alpha` is itself the merged slope at `t_*`),
> against 15 dimensions, and the last item may cost 1 at dim 14 —
> **either way `k = 7` prescribable merges**, against a demand of
> **10**. **STRUCTURAL DEFICIT 3 — identical to round 37's 8 vs 11.**
> (ii) *Variety currency.* `15 - 10 (merges) - 1 (disc) = 4`, equal
> to round 37's `15 - 11 = 4`.

`P(the instrument deficit is exactly 3) = 0.75`;
`P(the variety dimension is 4) = 0.80`. **The demand drops by one
and the budget drops by one; the gap is invariant.**

**R2.4 Free supply is untouched.** Nothing in round 37's free-
coincidence rate `252/q` depends on the slot count, so the door
still needs **3 free merges** against a measured mean `0.096/0.079`
and an all-time maximum of `2` (`r37 REPORT.md:214`).
`P(a 13-slope O=2 configuration is BUILT by an incremental
instrument this round) = 0.08`.

**R2.5 THE SOLVE FORMULATION I WILL USE, registered before writing
any code.** Once the 13 slope values and the incidence design are
fixed, all 8 slope cubics are determined up to scale by their root
multisets: `f_i = c_i prod_{gamma in T_i}(Z - gamma)`, the degenerate
one `c_i (Z-alpha)^2 (Z-beta)`. A `Psi` exists iff `F = W Psi` is
solvable, `W` the `8x4` Vandermonde in the fibre values `t_i`, i.e.
iff **`K F = 0`** for `K` a `4x8` basis of the left kernel of `W` —
**16 linear equations in the 8 scales `c_1..c_8`**, and the
configuration is realizable iff that `16x8` matrix has a kernel
vector with **all coordinates nonzero**. Codim of corank `>= 1` is
`(16-7)(8-7) = 9` against 13 free slope values, so the variety has
dimension `13 - 9 = 4` — a THIRD independent route to 4.
`P(the three counts agree at 4) = 0.70`.

**R2.6 The A/B sequential instrument.** By round 37's interpolation
law (`r37 REPORT.md:62`), fixing the 12 `A`-side roots makes every
merge condition LINEAR in the four `A`-side scales
(`sum_{i' != i} lambda_{ji'} c_{i'} f~_{i'}(a) = 0`), so the solve
is "choose 12 roots making a `10x4` matrix drop to rank `<= 3`":
codim `(10-3)(4-3) = 7` against 12 roots, dim 5, minus 1 for the
tangency = **4** — a FOURTH agreeing count. This licenses a
sequential one-variable root scan over `F_q` with backtracking.
`P(the sequential instrument beats 8 prescribed merges) = 0.15`.

### R3 — THE FIVE BLIND PRIORS THE BRIEF DEMANDS

| quantity | prior |
|---|---|
| `P(D1's ledger closes — no axiom kills the door on paper)` | **0.25** |
| `P(a 13-slope O=2 configuration is built)` | **0.08** |
| `P(it survives the full pipeline => m=4 witness)` (joint) | **0.02** |
| `P(the killing axiom, if any, is the PER-SIDE CAP)` | **0.20** |
| `P(it is (DEG-m))` / `P(it is (SAT2)/(SAT4)/eps~)` / `P(nothing kills it)` | **0.55 / 0.15 / 0.25** |

**EXPECTED BEST OUTCOME (phrase):** *"the side door is legal inside
the `(SAT2)`/`(SAT4)` deficiency budget but dies on the `(DEG-m)`
slot identity by exactly one unit — and even if it lived it is
budget-neutral: demand 10 against a prescribable 7, deficit still
exactly 3."*

### R4 — MISS-2 GUARD (five clauses, registered before any search)

- **G1 (verifier, not counter).** No configuration is reported
  unless a SEPARATE verifier re-derives, on the actual point set:
  `|W| = 27` distinct points; 9 pairwise disjoint fibres; all 8
  outer slope cubics split over `F_q`; EXACTLY one with a double
  root; `d_gamma <= 2`; pair multiplicity `<= 1`; per-side counts
  `<= m-1 = 3`; the `(2,1)/(1,2)` 2-colouring with four of each;
  `|slopes| = 13`; and `Psi` recovered and re-evaluated.
- **G2 (r36's exact failure mode).** A slot/coincidence count is
  NOT a configuration. I will not report a merge count, a slot
  count or an excess `E > 0` as a witness.
- **G3 (no axiom laundering).** If the ledger fails an axiom I
  report the axiom and its MEASURED margin. Any `O`-corrected form
  must be QUOTED from the banked statement with `file:line`; I may
  not invent a relaxation that makes my configuration pass.
- **G4 (dimension counts are not existence).** `dim = 4` has zero
  power to produce a witness (`r37` zero-power 3), and four
  agreeing counts of 4 are still zero.
- **G5 (recovery or death).** If `Psi` cannot be recovered from a
  candidate and re-verified to have exactly the designed root
  pattern at BOTH fields, the candidate is DEAD, not "promising".

### R5 — ZERO-POWER DECLARATIONS (in advance)

1. Nothing this round decides `m = 4` positively unless a fully
   verified 27-point configuration WITH a completion appears. **A
   paper ledger that closes is not a witness.**
2. Any negative is a ceiling over a NAMED class — `(SHARE3-4)`,
   constant-norm pencils, two fields, a named budget — never an
   exclusion of `(BIV-CURVE)` at `m=4`.
3. The Segre/prescribable-budget count is a GENERIC-POSITION count
   inherited from round 37 (its zero-power 2), **not a theorem**;
   my tangency version (R2.2/R2.3) inherits that status exactly and
   bounds instruments, not the variety.
4. Two fields (`q = 193, 257`) is not `q`-uniformity; no claim at
   official scale `q ~ 2^167`.
5. If `biv_core.py` is not copied, audited and run, **nothing here
   is gated by bank 2's verifier**, and I will say so in MISSES.
6. Every axiom and device I use — `(OV)`, `(OUT-m)`, `(DEG-m)`,
   `(SAT2)`, `(SAT4)`, the demand law, Lüroth/the pullback lattice,
   the rational normal curve, `|slopes| = SLOTS - merges`, the
   `K_{4,4}` certificate, the interpolation law, the constant-norm
   census — is **BANKED** (rounds 34/36/37 and the crossing
   statement). I claim none of them. The only candidates for
   novelty are: the slot-cancellation identity (R1.3), the tangency
   cost (R2.2), the invariance prediction (R2.3), and the
   kernel-of-Vandermonde solve (R2.5) — each subject to CATCH-24A
   own-repo subtraction, hyphenated and infixed variants included,
   BEFORE any novelty claim.
7. Layer A, `(SAT3)`-conditionality, `m = 1`, and sporadic
   non-factoring sharing are untouched unless explicitly reported.
8. `mu(x)` at the middles has never been verified in this lane
   (`r36` MISS 10, `r37` MISS 11); if I do not verify it, it stays
   a miss and I do not use the middle bookkeeping as if verified.

### R6 — FALSIFIERS

- **F1.** If banked `(DEG-m)` is NOT of the form
  `n_1 + 2(rho-s) <= 2m-2`, **R1.3 is refuted** and I say so before
  reporting anything else about it.
- **F2.** If a 10-merge + tangency configuration is built needing
  fewer than 3 free coincidences, **R2.3(i) is refuted**.
- **F3.** If the measured cost of the tangency prescription is 1 at
  a span dimension `< 14`, **R2.2 is refuted**.
- **F4.** If the middle fibre can legally carry the degeneracy,
  **R1.1 is refuted**.
- **F5.** If `X'` is defined with root multiplicity in the banked
  statement, **R1.4's 0.75 branch is refuted** and the killing
  axiom is the per-side cap after all.

### R7 — EXPECTED SELF-ERRORS

- **E1.** I expect one of my four dimension counts to disagree with
  the other three.
- **E2.** I expect `(SAT4)`'s identity placement to be the item I
  get wrong: I am reconstructing `O` from the brief's phrasing, not
  from the statement.
- **E3.** I expect the per-side cap to HOLD and to be irrelevant —
  i.e. the brief's nominated suspect is the wrong suspect.
- **E4.** I expect at least one of the two prior rounds' 10-merge
  configurations to be unreproducible in my own code (both rounds
  reported exactly this defect: `r36` MISS 7, `r37` MISS 5).
