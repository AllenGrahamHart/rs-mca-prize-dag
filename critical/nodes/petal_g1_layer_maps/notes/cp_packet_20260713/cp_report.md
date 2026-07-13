# cp_report — CLAUSE (P) mission report (2026-07-13, fresh-context proof worker)

## STATUS: PROVED (as posed)

CLAUSE (P) of `petal_g1_layer_maps` — the aperiodic top-band atlas supply
at the FLOOR BAND `d >= ell(t_ch - 2)`, official rows, weighted census
`<= (121/128) n^6` — is a THEOREM, with no open hypothesis consumed and
with a WORD-INDEPENDENT atlas (so received-word uniformity, the
frontier.md "extraction" obstruction, is dissolved at this band). Proof:
cp_proof.md; statement + pins: cp_statement.md; verifier: cp_verify.py
(ramguard tiny, 59 PASS 0 FAIL); ledger: cp_findings.md (catches
#168-#171).

## The theorem in one breath

Floor band + full-petal + `|S| >= k+1` forces the support to agree on at
most `J = k+3-2t_ch` core points and to contain at least `t_ch - 1` full
petals (Lemma B, two lines). So the class census — any word, any field,
any scale, any layout with disjoint 2-point petals — is at most
`N_max = 2^{b0}(t_ch+1) S_J(k-1)`, and:

- **rates <= 1/4 (official n = 2^42..2^44):** `J < 0` — the floor band is
  EMPTY for ALL contributors (not just the #145 hazard family): clause
  (P) holds with the empty atlas. (In-vivo complete-census confirmation
  at (16,4,97): 51 contributor classes exist, zero in the floor band.)
- **rate 1/2 (official n = 2^41):** `J = 3` at EVERY row size. The
  explicit atlas `A^prim = {(D0,R) : D0 <= Z, |D0| >= 2(t_ch-2), R <= B}`
  (full petal set per chart, legal K4 band, |R0| < ell, both retained
  flavors) covers every floor-band full-petal contributor — aperiodic and
  periodic — with weighted census exactly `N_max = 2(t_ch+1)S_3(k-1)
  ~ n^4/96`: at n = 2^41 that is 2^157.42 against budget 2^245.92
  (margin 2^88.5); verified for all rate-1/2 rows s = 3..44.
- **per-chart K4 line re-proved word-free:** within a chart, a class is
  its touched petal set (<= t_ch + 1 options) — so the packet does not
  even consume the layer-map/dictionary transport; K4's m+1 bound holds
  for these charts by support counting.

Both banked hazards are separated from the floor band by the same
inequality `j <= 3`: the #145 odd-lift mass enters only at `z <= z0`
(= the banked 993 + 31 = 1024 caps at (128,64), which embed in N_max =
2,754,048), and the #138 exponential periodic mass sits at large `j`,
never floor-band.

## Deliverable 2 — the complement/aperiodic-locus analysis (reusable)

cp_proof.md section 4. Parity dichotomy at even-k fiber-aligned chart
words: with `h := f0 + x_nf f1`, full-fiber agreements are zeros of `h`;
`h == 0 <=> f` is a lift `(X - x_nf) g(X^2)`. Answer to the mission's
torus/rank question: the aperiodic LIFT locus carries NO consistency
equations (rank 0 — interpolation with the free split-point agreement;
that is WHY it is q-free and supply-complete, #145), while the aperiodic
NON-LIFT locus is the rank->=1 branch (`h = c L_{Y_full}`, 2 parameters
vs >= 3 half-agreement conditions) with first-moment ~ poly/q. Measured
in vivo: non-lift floor accidentals 30/18/10 at q = 97/193/257 (decaying
~1/q), lifts 53/48/53 (binomial, q-free). Upper and lower bounds on the
wide-band aperiodic mass now match at binomial scale: there is NO
wide-band budget rescue at any field size; the floor band is the unique
poly window (quantified P1 stakes).

## Catches minted (#168-#171, full text in cp_findings.md)

- **#168** Layout anchoring is load-bearing: the layout-existential floor
  band is pre-falsified by core re-basing (every |S| = k+1 lift enters a
  tailored layout's floor band; in-vivo witness z = 7, d = 0 -> d* = 14;
  the C(63,32) > 2^41.92 kill transports). Clause (P) is proved
  layout-anchored — the banked operational semantics.
- **#169** The rigidity + emptiness law (strengthens #145/#153's family
  law to ALL contributors; boundary bookkeeping note vs bsra's printed
  2k >= n-1).
- **#170** The lift family does NOT exhaust the aperiodic floor band:
  full censuses 83/67/63 at (32,16, q = 97/193/257) vs lift-only banked
  pins 53/48; a #153-cap-sized atlas would undercover (83 > 64); the
  rigidity census prices both branches.
- **#171** Below-top exposure honesty flag: under the floor posing, the
  wide-minus-floor aperiodic lift mass (~2^59.67 at (128,64)) moves to
  petal_growth's below-top obligation, which currently has no aggregate
  budget line for it; attach to the owed P1 maintainer request.

## Verification record

cp_verify.py stages P1-P7 (each standalone under ramguard tiny; full
suite 12.9 s, 59 PASS 0 FAIL): complete brute cross-validation of the
candidate (rigidity) method at (16,8,97) and on non-coset layouts;
banked-pin reproductions 8/53/48 + emptiness 0; two fresh cells incl. the
never-banked (32,16,257,geom3); dual-method lift census agreement
(official-row candidates vs quotient-side enumeration); four mutation
controls, all REQUIRED-TO-TRIP trip (band-sharpness, stratum-dropping,
word corruption, tailored-layout re-basing); exact bigint grid arithmetic
s = 3..44 + the four official maximal rows + #153 embedding + parity law
+ interpolation self-test.

## Suggested surgery (for the banking session; NOT performed here —
## read-only mission)

1. Fold cp_statement/cp_proof into `petal_g1_layer_maps` (clause (P) ->
   PROVED pending the house fresh-context audit replay), adding the #168
   layout-anchoring pin to the statement text.
2. Keep tripwire (P)-3 (P1 wide-resolution) and add #171's below-top
   note to petal_growth's obligations ledger + the P1 maintainer request.
3. Update the #153 line: the two-family cap is the LIFT-family account;
   the full-band account is the rigidity census (#170).
4. Consumers: K4 package unchanged (the per-chart line is independently
   re-proved at these charts); petal_growth's primitive branch can cite
   the census bound directly (chart-free) or through the atlas.

## Files (this scratchpad, cp_-prefixed, self-contained)

- cp_report.md      (this file)
- cp_statement.md   (theorem statement, pins, consumed-hypotheses table,
                     falsifiers)
- cp_proof.md       (Lemmas A-C, atlas theorem, complement analysis,
                     #168 construction, non-claims)
- cp_verify.py      (staged verifier; usage at top of file)
- cp_findings.md    (catches #168-#171, verification + consistency
                     record, optional strengthenings)
