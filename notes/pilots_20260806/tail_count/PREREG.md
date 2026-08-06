# PRE-REGISTRATION — THE TAIL-COUNT CRITERION attacked (round 20, GENERATIVE)

Round 20, 2026-08-06. Coordinator-authored brief; the pilot appends
its own registrations BEFORE any computation. The F2 mass terminal's
open form (post-route-(b)): the TAIL-COUNT criterion. No named route
exists; two leads do. Attack them.

## 0. The state (quote verbatim before working)

- background/nodes/f2_z1_mass_knife_edge (post-corrections) — the
  terminal: Z_1 <= 2^{o(m)} at k = e iff the tail count
  |{u in F_p^R : P(u) >= 2^{cS}}| <= 2^{(1-c)S + 46 + o(S)} for
  every c in [0,1], where P(u) = prod_{s<S}(1 + cos(2 pi
  f_u(zeta^s)/p)) — the exact 1+cos form (round-19 tern_route_b,
  machine-verified; the object is a sum of NON-NEGATIVE terms, no
  cancellation exists).
- notes/pilots_20260806/tern_route_b/{REPORT.md, PROOFS.md} —
  PROPOSITION 10 (LEAD 1): log2 P(u) EXACTLY as a doubling-map /
  log-sine functional (Dedekind-sum-shaped, strictly finer than
  V_1; no bound known); LEMMA 2 (complete subgroup sums); LEMMA 5
  (AM-GM); THEOREM 7 (the 2^{0.8908 S} baseline to beat);
  COROLLARY 8's family trap (any argument ending in a low-l1
  relation count re-enters the dead family — your route must not).
- notes/pilots_20260806/tern_small_scale_laws/{REPORT.md, PROOFS.md}
  — (LEAD 2) the p = 7, w = 4 484x OVER-representation: 9 orbits
  where 0.019 expected — an unidentified mechanism that CREATES
  ternary codewords. Understanding creation is the flip side of
  bounding tails: the tail count is large exactly where creation
  mechanisms operate.

## 1. Pre-registered deliverables

- **(T1) LEAD 1 — bound the doubling functional.** Prop 10 writes
  log2 P(u) through the value multiset {n_c(u)} and the doubling
  map c -> 2c with log-sine weights. Attack lines in order:
  (a) the doubling map's orbit structure on F_p^* (2 has order
  ord_p(2) — the functional telescopes over doubling orbits; does
  orbit-averaging bound the log-sine sum? Dedekind-sum literature
  shapes apply?); (b) equidistribution of {f_u(zeta^s)} for typical
  u via the value-multiset second moment (which is NOT a low-l1
  relation count if routed through n_c directly — verify you evade
  Corollary 8's trap and SAY HOW); (c) the large-P(u) structure:
  P(u) >= 2^{cS} forces the multiset to concentrate near c = 0 —
  what does concentration force on u? A structure theorem for
  large-P u ("the tail is structured") would convert the tail
  count into a parametrized family count.
- **(T2) LEAD 2 — the creation mechanism.** Identify the p = 7,
  w = 4 mechanism exactly (the cell is tiny: enumerate the 288
  codewords, find the algebraic pattern — subfield? norm form?
  quadratic residue structure?). Then: does the mechanism have an
  analogue at the F2 object's parameters (split primes, all-odd
  windows)? If provably NOT (like TWT), that is a tail-count
  constraint banked; if YES, it is a creation lower bound the
  terminal must respect — either way the terminal sharpens.
- **(T3) THE CRITERION AT TOY SCALE.** Measure the actual tail
  profile |{u : P(u) >= 2^{cS}}| exactly at the round-19 toy rows
  (G1-G6 shapes) — the empirical tail law vs the criterion's
  requirement. Does the measured tail obey (1-c)S-type decay with
  a bounded additive constant? Pre-register the grid; 2-power
  lengths; NO shift-0 cells (the integer layer).
- **(T4) THE VERDICT.** One of: a proved tail bound for some c-range
  (partial progress, state exactly which c); a structure theorem
  for the tail (route-shaped); a proved obstruction (the criterion
  needs input the object does not supply — name it); or honest
  null with the measured tail law banked.

## 2. Pre-registered falsifiers / honesty clauses

- Corollary 8's family trap is a MANDATORY self-check at every
  step: any bound consuming a distance theorem + a counting step
  must be flagged and its threshold computed — landing at p <= O(1)
  again means the route re-entered the dead family.
- AK-UNIT: no congruence conclusions about counts.
- Measured tail laws are evidence, never proof; label throughout.

## 3. Rules of engagement

- DRAFT ONLY: write only inside notes/pilots_20260806/tail_count/.
  Never edit dag.json, node shards, tools/, or push. Do NOT read
  notes/pilots_20260806/f2_repose/ (sibling this round). Do NOT
  read CAMPAIGN_LEDGER entries appended after the "ROUND 20
  LAUNCHED" marker.
- COMPUTE LAW: never bare python3, INCLUDING file patching and JSON
  peeking — tools/ramguard tiny|local -- python3 ..., literal --,
  from repo root /home/u2470931/smooth-read-solomin/prize.
- Verbatim quotes with file:line for every statement relied on.
- Do NOT write REPORT.md — your final message IS the report; the
  coordinator persists it verbatim.

---

# PILOT PRE-REGISTRATIONS (Opus, round 20) — appended 2026-08-06 BEFORE any computation

Environment checked only (python 3.12.3, numpy 2.3.4 under `tools/ramguard
local`; the `tiny` profile cannot hold numpy). No mathematics run yet.

## A. Notation I fix (matching `tern_route_b/PROOFS.md:47-61`)

`S`, `R`, `p`, `zeta` (order `2S`), `Y = {zeta^s : s<S}`, `H = Y u (-Y)`,
`Lambda = {1,3,...,2R-1}`, `f_u(X) = sum_{r<R} u_r X^{2r+1}`,
`c_s(u) := f_u(zeta^s) in F_p`, `n_c(u) := #{s : c_s(u) = c}`,
`P(u) := prod_{s<S}(1 + cos(2 pi c_s(u)/p))`, `U_c := {u : P(u) >= 2^{cS}}`,
`L := log2 p`, `Delta := R log2 p - S` (the row's saturation constant;
`46.02` at the official row).

NEW objects I introduce (and will define formally in PROOFS.md):
- `d(c) := -2 log2 |cos(pi c/p)| >= 0`  (the LOCAL COST of the value `c`;
  `d(0) = 0`).
- `cost(u) := sum_{s<S} d(c_s(u))`.
- `C* := { (f_u(zeta^s))_{s<S} : u in F_p^R } <= F_p^S`  (the value code).
- `E(c) := log2|U_c| - [(1-c)S + Delta]`  (the CRITERION EXCESS; the
  criterion is `E(c) <= o(S)` for every `c`).

## B. Pre-registered predictions (falsifiable, with the falsifier named)

**P1 (T1a — the doubling lead collapses).** I predict Prop 10's
doubling/log-sine functional TELESCOPES to an elementary form: summing by
parts over `c |-> 2c` gives `log2 P(u) = S - cost(u)` exactly, i.e. the
Dedekind-sum shape carries NO arithmetic content beyond the elementary
identity `log2(1+cos t) = 1 + 2 log2|cos(t/2)|`. FALSIFIER: the two
expressions disagree at any toy `(row, u)` — machine-checked exactly.
If P1 holds, LEAD 1 attack line (a) is a MIRAGE and I say so.

**P2 (T1b — the exact value-distribution facts, and the trap evasion).**
I predict, and will prove: (i) for every `s`, `c_s(u)` is EXACTLY uniform
on `F_p` as `u` ranges over `F_p^R`; (ii) any `R` distinct coordinates
`(c_{s_1},...,c_{s_R})` are EXACTLY uniform on `F_p^R` (i.e. the value
vector is `R`-wise independent), because `C*` is MDS; (iii) hence
`E_u[log2 P(u)] = -S(1 - 2/p)` EXACTLY and, for `R >= 2`,
`Var_u[log2 P] = S Var(d)` EXACTLY; (iv) `E_u[sum_c n_c(u)^2] = S + S(S-1)/p`
EXACTLY. TRAP SELF-CHECK (mandatory): these consume ONLY the
non-vanishing of the linear functionals `u |-> f_u(x) - f_u(y)`
(a Vandermonde/degree fact), NOT a low-`l1` relation count and NOT
THEOREM Z-2; I will state this explicitly. FALSIFIER: any toy row where
a measured marginal or the measured `E_u[log2 P]` disagrees with the
exact prediction.

**P3 (T1b — the moment supply's c-range).** I predict the Z-2/Chebyshev
supply of THEOREM 7, run PER LAYER `c` instead of in aggregate, certifies
`|U_c| <= 2^{(1-c)S+Delta}` for an EMPTY set of `c` at `L = 64`, and that
its threshold in `p` is the SAME `p <= 8.30` of COROLLARY 8 (attained at
`c = 1`). I will compute the exact per-`c` condition and its threshold by
bisection. If the threshold lands at `p <= O(1)`: MANDATORY FLAG — the
route re-entered the dead family.

**P4 (T1c — the structure theorem).** I predict the exact structure
statement: `U_c = {u : cost(u) <= (1-c)S}` is a SMALL-VALUES set for the
MDS code `C*` — i.e. the tail count is exactly a box/lattice-point count
for the Construction-A lattice over `C*` — and that (i) `|U_1| = 1`
EXACTLY (only `u=0` attains `P = 2^S`), (ii) the c-range provable by
interpolation (`R` small coordinates determine `u`) has width
`O(p^{-2})`, and (iii) the interpolation route is itself a
distance+counting member whose threshold I will compute (prediction:
WORSE than `8.30`). FALSIFIER for (i): a toy row with two distinct `u`
attaining `max_u P(u) = 2^S`.

**P5 (the critical layer).** I predict the criterion is SATURATED, not
slack: because each coordinate is exactly uniform, the flat/independent
model has `E[P] = 1` exactly, so its tail obeys `Pr[P >= 2^{cS}] = 2^{-cS}`
with EQUALITY at one layer `c* = m_1(p) := (1/p) sum_c (1+cos(2 pi c/p))
log2(1+cos(2 pi c/p))`, predicted `m_1 -> 0.4428...` as `p -> infinity`.
Consequence I will state: the binding layer of the terminal is
`c ~ 0.443`, NOT `c = 1` and NOT `c = 0`. FALSIFIER: measured `argmax_c
E(c)` on the toy grid drifting away from `m_1(p)` as `p` grows.

**P6 (T2 — the creation mechanism).** For the `p=7, w=4, n=32` cell
(`N=16`, `T = <7>`-closure of `{1,3}` mod 32, 288 codewords of weights
`{7,14}`) I pre-register the hypothesis list, to be decided by exhaustive
enumeration:
  H1 GENERATOR-COEFFICIENT: the negacyclic generator polynomial
     `h = prod_{s in T} (X - omega^s)` (degree 8 over `F_7`) has SMALL
     (ternary/sparse) coefficients, and the 288 are exactly the ternary
     multiples `h*q`; the 9 orbits are 9 essentially-different `q`.
  H2 SUBFIELD: the 288 lie in an `F_7`-subcode fixed by a subfield /
     Frobenius structure (`ord_32(7) = 4`).
  H3 DESIGN/DIFFERENCE-SET: the weight-7 supports form a difference set
     or a union of cosets of a subgroup of `Z/16`.
  H4 MULTIPLIER: the 288 are one orbit under a group strictly larger than
     the negacyclic rotation group (multipliers `X -> X^u`, `u` in the
     stabiliser of `T` mod 32).
I predict H1 is the mechanism (prior ~0.5), H4 additionally true as a
symmetry (~0.5), H2/H3 derivative. FALSIFIER: `h` has a coefficient
outside `{0,+-1,+-2}`, or the 288 are not all multiples of the predicted
`h` (which would be a contradiction in terms — that part is definitional
and serves as a CONTROL, not a finding).

**P7 (T2 — transport to the F2 object).** I predict the mechanism does
NOT transport: the official object's generator `prod_{r<R}(X - zeta^{2r+1})`
has constant term `+- zeta^{R^2}`, which is `+-1` iff `S | R^2`; at the
official row `v_2(R) = 2` while `S = 2^38`, so `S` does NOT divide `R^2`
and the generator is NOT ternary. I will verify the `v_2` arithmetic
exactly and state the transport verdict either way (both outcomes sharpen
the terminal, per the brief).

**P8 (T3 — the measured tail law).** I predict the measured excess `E(c)`
is (i) maximised near `c = m_1(p)`, (ii) bounded by a small constant on
the toy grid, and (iii) NOT growing linearly in `S` between the `S=8` and
`S=16` families. Any of (i)-(iii) failing is reported as a miss of my own
null. Measured tail laws are EVIDENCE, never proof (PREREG.md:74).

## C. Pre-registered T3 grid (fixed now; no post-hoc rows)

Rows are `(p, S, R)` with `S = 2^{v_2(p-1)-1}` FORCED by `p` (the
half-system convention, `tern_route_b/PROOFS.md:48-49`), `Lambda =
{1,3,...,2R-1}` so the exponent `0` NEVER occurs — the CATCH-19B
shift-0 integer layer is structurally absent, and I will ASSERT
`0 not in Lambda` in code. All lengths `2S` are 2-powers (CATCH-Z6
automatic).

- FAMILY A (saturated, `R = round(S/log2 p)`), exhaustive over all `p^R`
  tuples: the six round-19 rows G1..G6 `(17,8,2), (113,8,1), (241,8,1),
  (97,16,2), (353,16,2), (673,16,2)`, plus A7 `(65537,16,1)` (log2 p =
  16.0, saturated `R=1`), A8 `(193,32,4)` ONLY IF `193^4` tuples fit the
  compute law (else reported UNREACHED, never estimated).
- FAMILY B (off-saturation, `R` reduced to make the census exhaustive;
  LABELLED off-saturation everywhere): `(193,32,2)`, `(193,32,3)` if it
  fits, `(577,32,2)`, `(641,64,2)` if it fits, `(257,128,1)`,
  `(769,64,2)` if it fits.
- Controls (a failure VOIDS the pilot): each row must reproduce
  `Z_1 = p^{-R} sum_u P(u)` against an INDEPENDENT exact ternary-kernel
  census (meet-in-the-middle over `3^S`, exact rationals) where `S <= 16`;
  at G1 and G4 it must reproduce the banked `Z_1 = 1.25` and `9.387207`
  (`tern_route_b/PROOFS.md:124-127`). Rows with `S >= 32` have no exact
  cross-check and are labelled EVIDENCE-ONLY.
- Reported per row: `Z_1`, `E_u[log2 P]` vs the exact `-S(1-2/p)`,
  `max_u log2 P / S`, the full profile `E(c)` on `c in {0, 0.05, ...,
  1.0}`, `argmax_c E(c)`, and `m_1(p)`.

## D. Honesty clauses I bind myself to

- Corollary 8 family-trap self-check at EVERY bound: I will state, for
  each, whether it consumes a distance theorem + a count, and compute its
  threshold in `p`. A threshold at `p <= O(1)` is reported as DEAD FAMILY,
  never as progress.
- AK-UNIT: no congruence conclusions about counts.
- The standing calibration clause (`f2_z1_mass_knife_edge/statement.md:64-69`):
  no toy is evidence about `Z_1` at the official row; toys verify
  IDENTITIES and measure CONSTANTS only.
- If a prediction of mine misses, it is reported as a miss with the
  mechanism, not absorbed.
