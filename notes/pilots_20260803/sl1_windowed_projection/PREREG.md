# SL-1 WINDOWED PROJECTION — PRE-REGISTRATION (Opus 5, 2026-08-03)

Written BEFORE any code was run in this pilot directory. Sources read
first: `notes/pilots_20260803/listsize_program/REPORT.md` (SL-1's
statement, SHADOW LEMMA, `census.py profile()`),
`notes/pilots_20260802/xr_band_occupancy/REPORT.md` (THEOREM 1/2),
`notes/pilots_20260803/lb_escape1_overagreement/REPORT.md` (the
DICHOTOMY), `background/nodes/xr_band_key_lemma_pencil_mass/statement.md`
(THEOREM I/I', KEY LEMMA), `notes/BAND_LANE_DEFINITIONS.md`,
`notes/pilots_20260802/xr_graded_band_ledger/bandlib.py`.

## 0. Notation pinned (band-lane definitions of record)

`C = RS_k` on `n` distinct points of `F_q`; received pair `(u,v)`;
pencil `w_z = u + zv` (`z in F_q`), `w_inf = v` — `q+1` members indexed
by `P^1(F_q)`. `A = k + h`. A **joint-explanation pair** (band pair)
`P = (f,g)` in `C x C` has core `Z_P = {i : f(x_i) = u_i, g(x_i) = v_i}`,
`|Z_P| = k + d`, **depth** `d`. **Band proper** = `d in [ceil(h/2), h-2]`
(definitions item 2); `d = h-1` is the **cascade tier** (item 3).
Projection `pi_z(P) = f + zg`, `pi_inf(P) = g`.

Per-pair quantities defined here:

```
a_P(z)    := agr(pi_z(P), w_z)                     (z in P^1(F_q))
mult_P(z) := a_P(z) - (k+d)                        ("extra" points at z)
LIVE_P    := {z : a_P(z) = A}         (live slopes, definitions item 7)
OA_P      := {z : a_P(z) >= A-1}      (OVER-AGREEMENT members)
cap_d     := floor((n-k-d)/(h-d))     (= bandlib's `cap`, BANKED)
beta_d    := floor((n-k-d)/(h-d-1))                (h-d-1 >= 1 on band proper)
W_d(z)    := #{c in C : k+d <= agr(c, w_z) <= A-2}   (WINDOWED count)
b_d(z)    := #{depth-d band pairs P : z in OA_P}
```

SL-1 as assigned: *does `pi_z(P)` have agreement `<= A-2` with `w_z` —
at some member / at every member?*  I.e. is `OA_P` empty (every member),
or is `OA_P != P^1` (some member)?

## 1. Predictions (P1-P9)

- **P1 (projection-multiplicity identity).** For EVERY joint-explanation
  pair at any depth `d >= 0`: `sum_{z in P^1(F_q)} mult_P(z) = n-k-d`
  EXACTLY. Mechanism claimed: each non-core coordinate `i` has
  `(e_i, e'_i) != (0,0)` with `e_i = u_i - f(x_i)`, `e'_i = v_i - g(x_i)`,
  hence lies on exactly ONE member of `P^1`. Expect 0 violations.
- **P2 (gate).** `a_P(z) <= A` for every `z`, on tangent-gate fixtures.
  Expect 0 violations.
- **P3 (SL-1 "at SOME member": TRUE).** For every band-proper `P`,
  `#{z : mult_P(z) = 0} >= (q+1) - (n-k-d) > 0`, so `min_z a_P(z) = k+d`
  exactly and the window's upper end is met at a positive fraction
  `1 - O(n/q)` of members. Expect: 100% of band-proper pairs.
- **P4 (SL-1 "at EVERY member": FALSE).** Expect `OA_P != {}` for every
  band-proper pair on the banked planted fixtures — in fact
  `max_z a_P(z) = A` there.
- **P5 (DEFINITIONAL refutation).** `|LIVE_P|` equals bandlib's
  per-pair live-slope count `len(pr["slopes"])`, so every pair counted by
  `N_d = #{depth-d pairs with L_P >= 2}` (definitions item 8) has `>= 2`
  members at agreement EXACTLY `A`. Expect exact agreement with bandlib's
  ledger on every fixture. If true, SL-1-as-posed is false for every
  object the occupancy count counts — not merely on a fixture.
- **P6 (bad-set bounds).** `|LIVE_P| <= cap_d` (reproducing the banked
  line cap) and `|OA_P| <= beta_d`. Expect 0 violations.
- **P7 (member-privacy).** On below-cascade fixtures, for every
  over-agreeing `(P,z)` the set `S = agr(pi_z(P), w_z)` (`|S| >= A-1`)
  has `(A(S), B(S)) != (0,0)` in the KEY LEMMA's top-coefficient algebra
  — i.e. `S` is NOT a joint-explanation set and exactly ONE member of
  `P^1` has a codeword interpolant on it. Expect 0 violations.
- **P8 (WINDOWED REDUCTION — the payoff).** For EVERY `z in P^1(F_q)`,
  `N_d^raw <= W_d(z) + b_d(z)`, where `N_d^raw` = ALL depth-`d`
  joint-explanation pairs (dominates the selected `N_d`; safe
  direction). Aggregated over the pencil:
  `(q+1) N_d^raw <= sum_z W_d(z) + beta_d N_d^raw`, hence
  `N_d^raw <= avg_z W_d(z) / (1 - beta_d/(q+1))`. Expect 0 violations.
- **P9 (sharpness of `beta_d`).** At `d = h-2` (`h-d-1 = 1`) the bound
  `|OA_P| <= beta_d = n-k-d` is attained whenever the non-core slopes are
  distinct — i.e. GENERICALLY. So the `1 - beta_d/(q+1)` loss is sharp in
  form, not an artifact of the estimate.

## 2. Falsifiers (F1-F8), F1 as assigned

- **F1 [THE ASSIGNED FALSIFIER].** A full-gate admissible fixture with a
  band-proper pair projecting at `A-1` or `A` at EVERY member
  (`OA_P = P^1(F_q)`). **PREDICT: NEVER FIRES** — it contradicts P1+P3
  whenever `q+1 > n-k-d`, which holds because `q >= n`. If it fires the
  multiplicity identity is wrong and this pilot's verdict inverts.
- **F2.** A band-proper pair with `OA_P != {}` on a full-gate admissible
  fixture. **PREDICT: FIRES** on the banked planted fixtures. This is the
  refutation of SL-1-as-posed.
- **F3.** Over-agreement at an INTERIOR band-proper depth
  `ceil(h/2) <= d < h-2` (so the failure is not an artifact of the
  `d = h-2` boundary where `A-1` is one point above the core).
  **PREDICT: FIRES** on a purpose-built `h >= 6` row. If it does NOT
  fire, SL-1 is salvageable on the band interior and the verdict
  upgrades.
- **F4.** An over-agreement set `S` (`|S| >= A-1`) that IS a
  joint-explanation set on a below-cascade fixture. **PREDICT: NEVER**
  (would contradict below-cascade via the KEY LEMMA).
- **F5.** `|OA_P| > beta_d` or `|LIVE_P| > cap_d`. **PREDICT: NEVER.**
- **F6.** The per-member windowed inequality of P8 fails at some `z`.
  **PREDICT: NEVER.** This is the falsifier that matters for the payoff:
  if it fires, the windowed upgrade of THEOREM 2 is dead.
- **F7.** `sum_z mult_P(z) != n-k-d` for some pair. **PREDICT: NEVER.**
- **F8.** A fixture with `beta_d * N_d^raw < q+1` but no member `z` with
  `b_d(z) = 0` (no clean member). **PREDICT: NEVER** (union bound).

## 3. What each outcome means

| outcome | verdict |
|---|---|
| F1 fires | SL-1 HOLDS nowhere; identity wrong; pilot inverts |
| F2 fires, F6 does not | SL-1-as-posed FAILS but the WINDOWED payoff survives — PARTIAL with the reduction rescued |
| F2 and F6 both fire | SL-1 fails AND the windowed upgrade is dead; the codeword-pair route stays closed |
| F2 does not fire | SL-1 HOLDS; THEOREM 2 upgrades windowed outright |
| F3 does not fire | SL-1 holds on the band interior; a `d = h-2` carve-out may suffice |

## 4. Compute discipline

Every run under `tools/ramguard {tiny,local} -- python3 ...` from the
repo root. No network, no Modal. `bandlib.py` and `census.py` imported
READ-ONLY; nothing outside this pilot directory is written.

## 5. ADDENDUM (2026-08-03, POST-HOC — registered AFTER sl1.py ran)

HONESTY NOTE. Sections 0-4 above were written before any code ran. The
items below were NOT pre-registered: they were formulated after the
first run resolved F1/F2/F3 and after that run was killed mid-flight.
They are recorded here separately so the pre/post boundary is explicit.
None of them changes a section-1 prediction; they explain WHY the
section-1 outcomes were forced, and they answer route (3).

- **T-CELL** (bijection F_q^2\{0} -> P^1(F_q) x F_q^*). The proof engine
  behind P1. Predicted: exact, all q.
- **T-MULT** (exact multinomial law for (mult_P(z))_z). Predicted: the
  law is EXACTLY multinomial(r; uniform on q+1 cells), r = n-k-d, and
  it makes F1 *impossible* (not merely unobserved) whenever r < q+1.
- **T-PSI** (the assigned unification). Predicted: Psi^z_y(u,v) =
  (w_z)_y - (pi_z P)(x_y) identically, i.e. SL-1's over-agreement
  functional IS the L-B functional of `lb_escape1_overagreement`
  PREREG R1 pulled back along the pencil map. Predicted 0 mismatches.
- **M1/M2** (2-adic depth). REPLICATION of the banked node
  `xr_mc_depth_quantization` BP(1)/BP(3); predicted to agree exactly
  with its check C. Any disagreement would be a flag on this pilot.
- **M4** (SPECTRAL EXCLUSION). NEW. Predicted: the MC-reachable
  agreement spectrum {k+w : w a 2-power <= h-1} misses the window
  [k+d, A-2] for every band-proper d, at all six rows.
- **F9** (new falsifier): a 2-power w in [ceil(h/2), h-2] at any row of
  record, i.e. a coset family landing INSIDE the window. PREDICT: NEVER
  at the six rows (h odd); PREDICT: FIRES at h even (control), which is
  why the protection is parity, not impossibility.
