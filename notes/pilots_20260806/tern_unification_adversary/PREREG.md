# PRE-REGISTRATION — the TERNARY UNIFICATION, attacked (round 19, ADVERSARIAL)

Round 19, 2026-08-06. Coordinator-authored brief; the pilot appends its
own registrations BEFORE any computation. MANDATE: attack the round-18
unification candidate BEFORE it becomes load-bearing. The campaign has
already had one unification collapse — (ES), which died in round 17
because it was a SHAPE identification, not a shared regime (mutually
unsatisfiable field requirements; "discharges all four consumers"
never checked per lane). Your falsifiers ARE that collapse's failure
modes. If this unification is a pun, kill it now.

## 0. The candidate under attack

Round-18's convergence: four blind pilots found "ternary vectors in
p-ary codes from cyclotomic windows" as the primitive of their
problems. The claimed instances:

- **(I1) The F2 terminal** (background/nodes/f2_z1_mass_knife_edge):
  Z_1 = weighted ternary mass of the negacyclic prime-field GRS dual
  [S, S-R, R+1]_p on the half-system of mu_{2^{e_p}}, S = 2^40/e,
  R/S = 1/log2 p, p >= 2^39. Question: Z_1 <= 2^{o(m)} at k = e.
- **(I2) The crossing deep stratum**
  (background/nodes/crossing_dsa_refutation, LEMMA DS/TC): ternary
  relations eps in {0,±1}^L with sum eps_j theta^j = 0, theta of
  order 2L in F_{p^{delta_a}} — ONE condition. Existence refuted at
  small p (DSA); openness at large p (the prime rows, heuristic
  53-61 bit margin).
- **(I3) The sparsity engine**
  (background/nodes/es_ternary_suppression_instruments, LEMMA AB):
  ternary vectors A - B in p-ary cyclic codes at length n/2;
  CC-sparsity IS this question (CATCH E-2).
- **(I4) The band pricing** (LEMMA TC's 3^L functional — the same
  eps object as I2, used as a count).

## 1. Pre-registered attack lines (verdict each)

- **(A1) THE SHAPE-PUN TEST.** Write each instance as a fully
  parametrized formal statement (object, alphabet, weighting, number
  of conditions, evaluation-point structure, quantifier, target).
  The unification survives ONLY if there is a single parametrized
  statement T(params) whose specializations are the three banked
  obligations EXACTLY — not "analogous". Known disanalogies to
  press: (i) I1 is a WEIGHTED MASS (2^{-wt}), I2/I3 are EXISTENCE /
  counts — round 18's CATCH-Z1 proved mass and exact-zero come
  apart; (ii) I1 has R ~ 4.3e9 conditions, I2 has ONE; (iii) I2's
  eps arises as a DIFFERENCE of binary indicators (fibred, LEMMA
  TC), I1's ternary vectors are native; (iv) evaluation structures
  differ (half-system vs theta-powers vs cyclic). For each: absorb
  into params, or declare the pun.
- **(A2) THE REGIME-COMPATIBILITY AUDIT (the (ES) killer).** For
  each pair of instances: are the parameter regimes where their
  questions LIVE mutually satisfiable, or provably disjoint? I1
  lives at k = e generating rows, p ~ 2^39-2^64; I2's open part
  lives at e = 1 prime rows, p ~ 2^129+; I3 lives at the official q
  in the SP/CS gap. If no common row/regime exists, say so PLAINLY
  — that was (ES)'s exact failure. (NOTE: a unification of
  STATEMENT with disjoint regimes can still be legitimate — unlike
  (ES), no one is claiming a shared DISCHARGE — but then its value
  is transfer of METHODS, which is (A3)'s test. Be precise about
  which kind survives.)
- **(A3) THE TRANSFER MATRIX.** For each banked instrument —
  Z-FLOOR, THEOREM Z-1/D1, THEOREM CS, SP-COVER/SP-UNIFORM, DSA,
  LEMMA ROT — determine with EXACT hypothesis-matching which OTHER
  instances it applies to. A unification whose instruments do not
  transfer is decoration. Produce the matrix with a
  applies/fails-because verdict per cell; every "applies" needs the
  hypothesis match spelled out, every "fails" the exact mismatch.
- **(A4) THE STRUCTURAL-DISANALOGY HUNT.** Find a property that is
  TRUE of one instance and FALSE of another and LOAD-BEARING (e.g.
  the 2-power Z-basis property — CATCH-Z6 showed composite lengths
  carry parasitic relations; do all instances sit at 2-power
  lengths in their live regimes? the negacyclic symmetry; the
  fibred binary origin). One proved load-bearing disanalogy = the
  pun verdict for that pair.

## 2. Pre-registered falsifiers / honesty clauses

- The unification is REFUTED as a statement-unification if (A1)
  fails; as a regime-unification if (A2) finds disjointness; it may
  still SURVIVE as a method-unification if (A3)'s matrix is dense —
  report which of the three grades survives, with the evidence.
- Do not soften: "the instances are related" is not a finding. The
  deliverable is a graded verdict with proofs.
- Any exact claim about an instance must quote the minted node
  verbatim (file:line), not the round summaries.

## 3. Rules of engagement

- DRAFT ONLY: write only inside
  notes/pilots_20260806/tern_unification_adversary/. Never edit
  dag.json, node shards, tools/, or push. Do NOT read
  notes/pilots_20260806/tern_master_statement/ (sibling — it BUILDS
  what you attack; independence required).
- COMPUTE LAW: never bare python3, INCLUDING file patching and JSON
  peeking — tools/ramguard tiny|local -- python3 ..., literal --,
  from repo root /home/u2470931/smooth-read-solomin/prize. Toy grids:
  2-POWER LENGTHS ONLY (the CATCH-Z6 rule) unless deliberately
  probing the composite-length disanalogy.
- Verbatim quotes with file:line for every statement relied on.
- Do NOT write REPORT.md — your final message IS the report; the
  coordinator persists it verbatim.

---

# APPENDIX — PILOT REGISTRATIONS (Opus 5, round 19, appended before any
# mathematical computation)

## 4. Honesty note on ordering

Before this appendix was written I (a) read the brief, (b) read the three
minted nodes and their node.json shards, (c) read es_g_lanes/FABLE_AUDIT.md,
(d) ran ONE utility, `_extract_sweep.py` (under `tools/ramguard tiny`), which
is a pure JSON->text reformat of a read-only subagent's tool result into
`_sweep_raw.md`. It has no mathematical content and computes nothing about
any instance. No other code has been run. Everything registered below is
registered BEFORE the corresponding computation.

## 5. The master object I will test (registered, may be refuted)

**M(N, c, p).** Let `p` be an odd prime, `N` a power of 2, `theta` an element
of exact multiplicative order `2N` over `F_p`, and

```text
  C(N, c, p) = { eps in F_p[X]/(X^N + 1) : eps(theta^{2j-1}) = 0, j = 1..c }
  T_N        = {0, +1, -1}^N   (ternary vectors, identified with F_p-coeffs)
```

i.e. the **negacyclic** code of length `N` over `F_p` whose zeros are the
first `c` ODD powers of `theta`, starting at exponent 1 (shift-0), intersected
with the ternary cube. **REGISTERED CLAIM P1:** I1, I2, I3 are each EXACTLY
`C(N,c,p) cap T_N` for banked `(N, c, p)`, namely
`I1: (S, R, p)`, `I2: (L, delta_a, p)`, `I3: (h = n/2, ceil((w-1)/2), p)`.
**FALSIFIER P1:** any instance whose root of unity does not have order exactly
`2N`, or whose window is not a shift-0 run of consecutive odd exponents, or
whose ambient algebra is not `X^N + 1`.

## 6. The criticality coordinate (registered before computation)

Define, for an instance at parameters `(N, c, p)`,

```text
  tau     :=  c * log2(p) / N          (F_p-conditions per coordinate, in bits)
  B       :=  N - c*log2(p)  =  N(1 - tau)        (Z-FLOOR informativeness)
  Tcrit   :=  N*log2(3) - c*log2(p) = N(log2 3 - tau)   (first-moment count)
```

- **P2 (regimes on tau).** I1 has `tau = 1` up to the `R = ceil(t/2)` rounding;
  I2 at `v = 34` on an `e = 1` prime row has `tau = 2`; I3 at `w = 2^34` on the
  official row has `tau = 2`. FALSIFIER: any `tau` off by more than 1%.
- **P3 (reproduction of banked constants).** The framework reproduces, to
  <= 0.05 bits: I1's knife edge `-46.02` bits and its `+17.98` bits under the
  one-condition (exact-balance) reading; I2's `2^{-53.1}` and orbit-corrected
  `2^{-61.1}`; CATCH-Z1's `(3/2)^S = 2^{0.585*2^38}`. FALSIFIER: any mismatch
  > 0.05 bits. (This is the test that the coordinate is the RIGHT one and not
  numerology: it must re-derive numbers I did not fit it to.)
- **P4 (the A4 disanalogy).** `sign(Tcrit)` is POSITIVE at I1 and NEGATIVE at
  I2 and I3 on their live rows. FALSIFIER: equal signs.

## 7. Registered predictions, A1-A4

- **P5 (A2, against the brief's own premise).** The brief asserts I1 lives at
  `p ~ 2^39-2^64`. I predict that range is UNSOURCED and that the banked
  generating classes admit `e = 1` with `p` prime, `v_2(p-1) >= 41`,
  `p < 2^256` — the SAME rows as I2's open prime rows and I3's official rows.
  I therefore predict A2 finds the regimes MUTUALLY SATISFIABLE (unlike (ES)),
  and I will exhibit an explicit 256-bit prime admissible for all three.
  FALSIFIER: a banked statement excluding `e = 1`, or no such prime.
- **P6 (A3, the strongest cell).** THEOREM Z-FLOOR's existence corollary
  (`2^N > p^c` => a nonzero ternary codeword) and THEOREM DSA's pigeonhole are
  THE SAME ARGUMENT, weighted vs unweighted; DSA's hypothesis is exactly
  `tau < 1` up to the 2-bit support correction. FALSIFIER: a 2-power toy where
  one fires and the other does not, beyond that correction.
- **P7 (A3, ROT).** LEMMA ROT transfers VERBATIM to all three because all
  three are negacyclic; orbits have size dividing `2N`. FALSIFIER: a toy orbit
  of size not dividing `2N`, or a negacyclic shift leaving the code.
- **P8 (A3, Z-1/D1).** THEOREM Z-1's four hypotheses match all three exactly,
  yielding min ternary weight `>= 2c+1`. FALSIFIER: a 2-power toy ternary
  codeword of weight `<= 2c` on a shift-0 window.
- **P9 (A3, CS).** THEOREM CS fails on I1 as banked (its hypotheses are a 0/1
  indicator SET and a char-0 ideal norm); and even under its natural ternary
  extension its exclusion condition is PROVABLY VACUOUS at I1, because
  saturation makes `c log2 p = N` so the condition collapses to `U < 4`.
  FALSIFIER: an arithmetic error making CS non-vacuous at I1.
- **P10 (A3, SP-COVER).** At the shared row `v_2(p-1) >= 41` forces
  `v_2(p^2-1) >= 42`, so SP-COVER needs an odd window reaching `2^42` — which
  ALL THREE fail (I1's window top ~`2^33`, I3's `<= 2^39`, I2's `2^1`). E-3's
  blind spot is not an I3 defect but a property of the shared row.
  FALSIFIER: any instance meeting the coverage requirement.
- **P11 (A4, the 2-power question).** All three sit at 2-POWER `N` in their
  live regimes, so CATCH-Z6's parasitic relations cannot occur in any of them;
  I predict this is PROVABLE (not merely toy-observed) from
  `deg Phi_{2N} = N` at 2-power `2N`. FALSIFIER: a p-independent ternary
  relation at 2-power `2N`, or a live regime at composite length.
- **P12 (the instance count).** I4 is NOT an independent instance: LEMMA TC's
  `3^L` is the CARDINALITY of I2's ambient ternary cube. FALSIFIER: a banked
  I4 obligation distinct from I2's.

## 8. Registered headline prediction (so a contrary result is visible)

**P13.** I predict the graded verdict: OBJECT unification SURVIVES (exactly,
and more strongly than the brief claims); REGIME unification SURVIVES as
SATISFIABILITY but with NO shared discharge; METHOD unification SURVIVES with
proved transfers that are all provably insufficient at their targets; and
STATEMENT unification is KILLED as a theorem-unification, surviving only as a
schema/taxonomy. If any of these comes out the other way I will report it as a
self-refutation.

## 9. Registered methodological gate (new, offered for adoption)

The (ES) post-mortem installed a REGIME test. I register that the regime test
is NOT sufficient: a schema can pass A1 and A2 and still transfer nothing if
its instances straddle a counting PHASE TRANSITION. I will grade this
candidate against a third gate, **CRITICALITY-COMPATIBILITY**: do the
instances lie in a common `tau`-interval on which the instruments are
non-vacuous? Registered before computing the taus.
