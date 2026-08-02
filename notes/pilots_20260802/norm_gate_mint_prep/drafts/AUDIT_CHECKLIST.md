# AUDIT CHECKLIST — DLI norm-gate mint package

What the coordinator should hand-verify before wiring, per package, plus every
place where I was uncertain of scope. **Flags are raised, not guessed.**

Replay command for all four (each finishes in under 3 s):

```text
tools/ramguard tiny -- python3 <node>/verify.py
```

`dli_norm_gate_forward_and_ofold/verify.py` imports `sympy` (for the third leg
of the norm triple check); it still fits the `tiny` profile (measured peak
~46 MB, 1.3 s). The other three are pure-python-integer only.

---

## 1. `dli_norm_gate_forward_and_ofold`

Hand-verify:

1. **`(LN3-2)`, the Hensel step.** `x^h + 1` reduces mod `q` to a product of
   `h` DISTINCT linear factors, so each root is simple and lifts uniquely to
   `Z_q`. This is the whole engine: `Norm = prod_j alpha(r_j)` in `Z_q` and
   each `j in Z(alpha)` contributes a factor divisible by `q`. Check that
   simplicity (not merely splitting) is what is used.
2. **`Norm(alpha) != 0` and the basis-range clause.** The `Z`-basis argument
   plus irreducibility of `x^h+1` over `Q`. Confirm this is exactly the banked
   C1 "reduced signed support / no opposite pairs" condition and that the DLI
   junction index range `0 <= i < h_{j+1} = phi(h_j)` really is the basis range
   (this is the clause a future seam edit could break — the standing check
   recorded in the pilot's FABLE_AUDIT).
3. **LN2's second proof.** `p_u = sigma_u^{-1}(p_1)` pairwise distinct requires
   simple transitivity, i.e. that there are exactly `phi(n)` primes above `q`
   and exactly `phi(n)` automorphisms. Check the count matches.
4. **The `o`-fold claim is about `m(alpha) >= o`, not about `H_U`.** Confirm
   there is no accidental converse anywhere in the statement.
5. **Verifier claim E** reproduces the banked `o > 1` solution counts (16 at
   `(16,17,U={1,3},w=6)`, 64 at `(32,97,U={1,3},w=5)`) from an independent
   code path — spot-check one of those against
   `notes/pilots_20260802/dli_norm_gate/results/splitting_n16_o.json` /
   `splitting_n32_o.json`.

**Uncertainty flags.**

- *(F1.a)* I state `Z[zeta_n]` is the full ring of integers as a classical
  fact, but arranged the proofs so that nothing depends on it (the elementary
  route is Hensel over `Z_q`). If house policy dislikes even the parenthetical,
  it can be deleted without touching any claim.
- *(F1.b)* The "ramification caveat" in LN0 is phrased as *both* hypotheses
  being load-bearing (`q` odd for unramifiedness, `n | q-1` for residue degree
  1). At `n` a power of two and `q` an odd prime the first is automatic; I kept
  it because the C2'' tower could in principle be re-posed at non-2-power `n`.
  Confirm that framing is wanted.

## 2. `dli_norm_gate_energy_ceiling`

Hand-verify:

1. **The Parseval step `(N-3)` is the ONLY place the coefficients enter.**
   Read the banked sandwich `proof.md` Claim 2 side by side and confirm `w`
   appears there solely as `||f||_2^2`. This is the whole content of the
   generalization; if `w` enters anywhere else, the node is wrong.
2. **Conjugate pairing needs `h >= 2` and `j != n-j`.** Check the `n = 4`
   boundary (`h = 2`) is inside scope and that `s >= 2` is stated.
3. **`(R-3)`, the `256:1` collapse.** `q^{L} <= (E^{128})^{L} <=> q <= E^{128}`
   uses strict monotonicity of `t -> t^L` on positive integers only — no logs.
   Confirm no float sneaks in.
4. **LN5 is one-sided.** Confirm the statement nowhere suggests
   `E >= E_min` is sufficient.
5. **Verifier check C** reproduces the banked maxnorm tables at `2N = 8, 16`
   exhaustively and at `2N = 32` for `w <= 3`; `w = 4,5,6` at `2N = 32` are
   *witnesses* (iota images) matching the banked values, not an independent
   exhaustive maximum. Confirm the statement says exactly that.

**Uncertainty flags.**

- *(F2.a)* **Edge kind for the sandwich attribution.** I propose
  `dli_c1_ternary_relation_norm_sandwich --ref--> dli_norm_gate_energy_ceiling`
  because the logical implication runs the other way (general `=>` ternary
  special case) while the proof is the banked one transplanted. If the house
  convention is `req` for transplanted proofs, switch it — but the direction
  question is real and I did not want to guess. See WIRING.md §B.
- *(F2.b)* I did NOT fold the WCL fence into this node even though it is two
  lines from LN2+LN4, because it needs the banked WCL slot definitions and I
  could not audit those inside my write scope. See item 5 below.

## 3. `dli_norm_gate_splitting_law`

Hand-verify:

1. **S1's double count.** The "by `a`" fibre is `sigma_a^{-1}(Sol_U)`; this
   needs BOTH `(S0)` (`sigma_a` bijects `W_w`) and `(S0')`
   (`Z(sigma_a alpha) = a^{-1} Z(alpha)`). Check the direction of `(S0')` — an
   inverse in the wrong place silently breaks the identity.
2. **`(S0)`'s injectivity argument.** `ai == aj (mod h)` with `a` odd implies
   `i = j` because `a` is invertible mod `h` as well as mod `n`. Confirm.
3. **S2's denominator.** `|D_U| = #{H_U != empty}`, which for `o = 1` — and
   ONLY for `o = 1` — coincides with `#{q | Norm}`. The C2'' L13 sentence
   ("`1/8` of norm-divisible sign patterns are solutions") is an `o = 1`
   statement; check the node does not silently extend that reading to `o > 1`.
4. **S3 Step 1 is where the stabilizer hypothesis lives.** `a_1 U = a_2 U`
   forces `a_2^{-1} a_1 in Stab(U)`. Without `Stab(U) = {1}` the step fails and
   S3 is false as stated. Check the two proved sufficient conditions
   (`U = {1}`; `max(U)^2 < n`).
5. **The `1/phi(n)` consequence is phrased as an implication, not a fact.**
   Confirm the statement's "at official scale" paragraph never asserts the
   ratio unconditionally.

**Uncertainty flags.**

- *(F3.a)* **The main open side condition: `Stab(U_j) = {1}` at official
  junctions `j <= 25`.** My proved sufficient condition `max(U)^2 < n` gives
  `T_j^2 < h_j`, i.e. `2^{66-2j} < 2^{41-j}`, i.e. `j >= 26`. For `j <= 25` I
  have only a VERIFIED PATTERN: for `U = {1,3,...,2L-1}` in `Z/2^m` the
  stabilizer is trivial for every `L` except `L = n/4` (`Stab = {1, n/2-1}`,
  the reflection `u -> n/2 - u`) and `L = n/2` (`Stab` = everything),
  exhaustive for `m <= 11`. Official blocks have `L_j = n_j/512`, outside both.
  This is stated as unproved in `statement.md` and `proof.md`. **It looks easy
  and I could not close it in the time available — flagged rather than
  claimed.** Nothing in package 4 depends on it.
- *(F3.b)* **Provenance number discrepancy.** The pilot's `REPORT.md` prose
  says "1930 rows / 53 deviating"; the persisted `results/analysis.json` says
  `total_rows = 1960`, `rows_deviating_from_1_over_phi = 63` (and the six
  `splitting_*.json` files do sum to 1960 rows). I cited the persisted
  artifact. Coordinator should decide whether the REPORT prose needs a
  correction of record.
- *(F3.c)* Of the 63 deviating rows, 9 are `n = 128` where no banked `maxnorm`
  exists, so S3 is *untested* there rather than confirmed. I corrected the
  headline wording accordingly; check I did not over- or under-state it.

## 4. `dli_official_support_forcing`

Hand-verify:

1. **The pins.** `n = 2^41`, `t = 2^33`, 34 blocks / 33 junctions,
   `ell_j = 2^{32-j}`, `N_j = 2^{40-j}` — all inlined as literals in
   `verify.py` and cross-checked against
   `notes/pilots_20260802/c2pp_nullity_structure/results/official_scale.json`.
   Confirm the literals match the JSON, since the node no longer reads it.
2. **`N_j = 256 L_j` at ALL 33 junctions**, hence `N_j/2 = 128 L_j`. The whole
   theorem is this one invariant; if any junction had a different ratio the
   `j`-independence collapses.
3. **`4^128 = 2^256` exactly and `3^128` has bit length 203.** These pin the
   `E_min` table. Both are exact integer facts in the verifier.
4. **Junction 0 has `E = |S_0|` exactly AND its domain omits `0`.** Both are
   needed: the first for the energy identity, the second for `rho_0 = 0`
   (Claim 4). At junctions with an even `c_i` the zero skew is admissible and
   `rho_j > 0` — check the scope sentence is present and correct.
5. **The honest-pricing paragraph.** A single constraint at junction 0 excludes
   only `E = 1`; all strength comes from the `o`-fold upgrade. Confirm this is
   not buried, since it names exactly what a seam failure would cost.

**Uncertainty flags.**

- *(F4.a)* **Claim 4 (`rho_0 = 0`, `Rem_0 = -q^{delta_0}`) depends on the C2''
  pilot's DEFINITION of `rho_j`**
  (`junctions.py`: `rho_j = (#admissible skews solving block j) q^{L_j} /
  |domain|`) and on the banked decomposition `rho_j = q^{delta_j} + Rem_j`.
  I did not audit those definitions against the C2'' node's own statement of
  record — I only read the pilot script. **If the DAG's `rho` differs
  (normalisation, whether `d = 0` is counted, stratum convention), Claim 4
  must be restated or dropped.** Claims 1-3 are independent of it.
- *(F4.b)* **Tower count discrepancy.** The pilot REPORT says "2,053 states
  predicted empty by the router, 0 solutions found"; the persisted
  `results/tower.json` per-row counts sum to **2,453**
  (393+204+140+333+382+0+1+400+600). I cited 2,453 and said so in `proof.md`.
  Coordinator to confirm and, if wanted, correct the REPORT.
- *(F4.c)* **The 34th-block reading.** The pilot flagged that a 34th-block
  reading gives `E_min = 16` at the exhibit. I could not determine from the
  banked artifacts which reading the DAG's official row semantics endorses, so
  I pinned the 33-junction / ratio-256 schedule (matching `official_scale.json`
  `junctions: 33` and `support_to_constraint_ratio: 256`) and recorded the
  alternative in the verifier as explicitly unused. **Coordinator should
  confirm the 33-junction reading is the row of record.**
- *(F4.d)* **Closure string.** I used `"proof plus exact integer ledger"`,
  which exists in the DAG's closure vocabulary. If the surface prefers plain
  `"proof"` (the arithmetic is all inside the proof), change it.
- *(F4.e)* The named exhibit's primality is BPSW-only in the banked C2''
  artifacts. The verifier runs a 12-base strong-probable-prime test and labels
  it a NON-certificate; the theorem quantifies over admissible `q` and does not
  depend on the exhibit. Confirm that framing is acceptable, or drop the
  exhibit to a pure illustration.

---

## 5. Candidate FIFTH node — not written, flagged

The **WCL norm fence** is fully proved by LN2 + LN4 and is arguably the single
most consequential item in the provenance pilot, but I did not write it up
because it needs the banked WCL slot family definitions (`order M = 512 ell`,
reduced signed weight-`w` relation vanishing at `u = 1,3,...,2 ell - 1`) that
live in nodes I could read but not audit inside my scope:

- **Unconditional:** the slot `(ell, w)` is empty for every `q > w^128`,
  **independently of `ell`** (because `phi(M)/2 = 256 ell` and `o = ell` give
  the same `256:1` ratio). This re-proves the banked
  `dli_wcl_weight3_ambient_exclusion` (11M polynomials) and
  `dli_wcl_ell2_weight3_ambient_exclusion` in two lines **for the top of the
  official range only** — the banked nodes cover ALL `q < 2^256`, so the fence
  does not subsume them.
- **The cap coincidence:** `4^128 = 2^256` exactly, which is why weight 4 cost
  a 1,398,341,120-polynomial enumeration while weight 3 did not.
- **Decisive negative (adopted as lane law in the pilot's FABLE_AUDIT):** no
  open WCL slot is reachable by a max-norm gate — all have `w >= 5`, and even
  the conditional fence needs `q > 23^64 = 2^289.5 > 2^256`. Effort should
  redirect to COUNT bounds (Minkowski second minimum).
- **Conditional (1,4) route:** under the C1 doubling law at `w = 4` to
  `N = 256` the fence becomes `14^64 = 2^243.7`, which covers the production
  window — a concrete new consumer for the C1 conjecture, whose proposed
  mechanism (imprimitivity) is REFUTED, so this must be flagged as an
  extrapolated pattern.

If the coordinator wants it minted, the statement/proof are a short delta on
`dli_norm_gate_energy_ceiling` + `dli_norm_gate_forward_and_ofold`, and the
verifier is an exact integer fence table (`w^128` vs `2^256`, `c_w^64` vs
`2^256`) — essentially `notes/pilots_20260802/dli_norm_gate/scripts/ladder.py`
`wcl_fence()` re-expressed as assertions.

---

## 6. Cross-cutting things I did NOT do

- No `dag.json`, `background/`, `critical/` or `tools/` file was touched; the
  verifier manifest was not regenerated (it must be, after the move).
- I did not re-run the provenance pilot's own scripts; I re-derived every
  number I cite from a fresh, independent implementation inside each
  `verify.py`, and cross-checked against the pilot's persisted JSON.
- I did not touch anything m2-related.
- The four verifiers do not read any file outside their own node directory,
  so they will keep passing after the move.
