# MANIFEST — r37_mint_drafts (D2)

Ten drafted node packages. **AUDIT-AND-DRAFT: every status below is a
PROPOSAL.** Nothing is wired; no file outside this directory was touched.

Anchor 1 is `critical/nodes/rate_half_band_crossing_location/statement.md`,
abbreviated **A1** in the line references below.

---

## 1. `statement_u` — Statement U and the far-CA exact value

- **Source:** A1:4420-4505 (Round-36 R-HRLOW addendum, coordinator-audited,
  round 36 bank 3). U and (U-VAL) at A1:4482-4488; (R36-D) at A1:4475-4481;
  the U-sym threshold at A1:4468-4470; the rho=3 gap at A1:4472-4474; the
  queued binomial correspondence at A1:4426-4429 and A1:4492-4495; the shape
  fence at A1:4496-4500. Constants independently banked at
  `notes/pilots_20260811/r36_hrlow/f4_results.txt:29-45`.
- **Status assigned: TARGET**, with PROVED components separated in a ledger.
  U itself is `T_sym = T_rand = 0` and `T_rand` is unpriced, so the weaker
  status is the only honest one. The razor arithmetic, the (FIB) cap and the
  U-sym kill are individually PROVED and marked as such.
- **verify.py: PASS** (`tiny`). Razor integers to the digit,
  `log2(r+1) = 39.977280`, the two cap forms proved identical for all
  `f >= 1`, the U-sym surplus `2^33-1`, and the `C(128,63)`/`C(127,64)` ratio
  `128/65 = 0.9776` bits.
- **Could NOT verify / left flagged:** U itself (T_rand unpriced — ZERO
  POWER); the rho=3 symmetric-T variant (unmeasured in the source); anything
  at razor scale by measurement.
- **Suggested wiring:** evidence edge to `rate_half_band_crossing_location`.
  Cross-pointers to packages 5, 9 and 4.

## 2. `l2_par_parametrization` — the (PAR) rational parametrization

- **Source:** A1:4347-4418 (Round-36 (SAT3)-on-(L2), round 36 bank 2);
  (PAR)/(RES) at A1:4357-4366; hand-checks at A1:4349-4355. Model at
  `notes/pilots_20260811/r35_l2_gate/d1_structure.py:6-9`. Certified `T = 2`
  witness at `notes/pilots_20260811/r36_sat3_on_l2/d2_results.txt:18-33`.
- **Status assigned: PROVED** for the parametrization, the determinantal
  form and the two syzygies (all coordinator hand-checked). **(RES) is
  carried as PROVED forward / MEASURED backward** — see DISCREPANCY D2.
- **verify.py: PASS** (`local`). Determinantal identity and both syzygies on
  120 random draws over two fields; the two-conditions-imply-the-third claim
  and its exception verified EXHAUSTIVELY over `F_13^4` (144 exception
  tuples, all of the form `f=g=0`, matching `(q-1)^2`); the banked `q=97`,
  `T=2` witness rebuilt from `(f,g,h,k,L)` and fully re-certified;
  `dim = 18`.
- **Could NOT verify:** the converse of (RES); birationality itself; any
  `m >= 3` statement; (SAT2)/(SAT4)/(SAT5) (inapplicable at `T = 2`).
- **Suggested wiring:** evidence edge to the crossing node; note that it
  supersedes package 3's (D-F) inversion as the construction instrument.

## 3. `l2_nonempty_theorem` — R-L2 nonempty at m = 2

- **Source:** A1:3526-3604 (Round-35 R-L2, round 35 bank 1);
  coordinator-independent verification at A1:3528-3534; the re-priced stake
  at A1:3560-3572. Witness at
  `notes/pilots_20260811/r35_l2_gate/d2_results.txt:9-31`; deficit row at
  `.../d1_results.txt:34-44`.
- **Status assigned: PROVED** — existence is witness-checkable and the
  witness re-certifies from scratch.
- **verify.py: PASS** (`local`). Degrees `(7,7,7)`, `s = 0`, separation rank
  `3`, `M(Z)Q_Z = 0` entrywise, `nullity(36x32) = 1` spanned by `(y_0,y_1)`,
  generic rank `7`, single drop at `z = 10` to `6`, no drop at infinity, no
  kernel vector of degree `<= 1` (so `e = 2` exactly), `T = 0`, max roots `4`,
  max shared `1`, `a* = 13`; (D-B) on `60/60` fresh curves plus the witness;
  planted common root gives nullity `2` on `24/24`; the counting corrections.
- **Could NOT verify:** the other eleven witnesses; the (D-F) `24x24`
  inversion (round-35's `B`-parametrization is a different object from
  package 2's and was not reconstructed); `m >= 3`.
- **CONVENTION FLAG:** `a* = 13` reproduces only under the projective
  reading — see DISCREPANCY D1.
- **Suggested wiring:** evidence edge to the crossing node; cross-pointer to
  the PROVED `rate_half_ca_hankel_endpoint_residual_pole_interpolation_
  exclusion` (which is what actually excludes official-row profiles).

## 4. `hr_dictionary_common_support` — the h_r dictionary

- **Source:** A1:4420-4505; (DICT)/(CS) at A1:4431-4438; LB1 at
  A1:4439-4443; the p* law and its five named failures at A1:4443-4448; the
  rho+2 band at A1:4449-4456. Model at
  `notes/pilots_20260811/r36_hrlow/f1_family.py:5-16`; banked rows at
  `.../f1_results.txt:8-25` and `:95-171`, the five failures at
  `:103,120,137,154,171`.
- **Status assigned: PROVED** for (DICT), (CS) and LB1; **POSED** for the
  `p*(d)` law. **Recommend the coordinator SPLIT this into two nodes** — the
  verify.py already separates the blocks cleanly.
- **verify.py: PASS** (`local`, first run). Dictionary on `32/32` rows
  (2 shapes x 2 fields x 8 families); common-support reconstruction exact on
  `24` rows; LB1's forced `T_1 = r+1` on `8` rows with every structural slope
  checked by exhibiting its annihilating locator; the `p*` law `30/32` with
  **exactly** the two named H2 symmetric-T quadratic failures (`6` vs
  predicted `7`); and `p*` confirmed not to separate `h_r = 3` from `4`.
- **Could NOT verify:** the `h_r = 2rho` (non-polynomial ratio) leg; the
  exhaustive `T` censuses at `q = 65537 / 999983`; `rho >= 3`; char 2.

## 5. `negation_closure_excess_fence` — the T = 95 mechanism

- **Source:** A1:4457-4474; shape fence A1:4496-4500; mechanism text at
  `notes/pilots_20260811/r36_hrlow/f4_close.py:5-21`; banked scan at
  `.../f4_results.txt:6-24`, control `:26-27`, razor forms `:29-45`.
- **Status assigned: PROVED** — the mechanism is exact, the counts
  exhaustive, the kill is condition counting.
- **verify.py: PASS** (`local`). Six cell-field scans; odd rows verified to
  collapse on all `1158` covering even locators; at `rho = 2` the bad set is
  **exactly** the covering set (84 at H1, 330 at H3); at `rho = 3`, `0` bad
  from `165` covering; the general law reproduces all six banked cells; the
  razor surplus `2^33-1`.
- **THREE CORRECTIONS MADE** — see DISCREPANCY D3, D4, D5.
- **Could NOT verify:** the full `T = 95..98` census (this reproduces the
  carrier, not the whole `C(n,r)` sweep); the rho>=3 symmetric-T variant.

## 6. `la_eq_and_geometry_counterexamples` — (LA-EQ) and the two rungs

- **Source:** A1:4270-4345 (round 36 bank 1); hand-checks A1:4272-4278;
  (LA-EQ) A1:4280-4288; H1/H1+H2 A1:4289-4300; the infinite family
  A1:4301-4308; (LA-PADE) A1:4309-4321; the terminus A1:4322-4331; the
  retirement of the bare target A1:3945-3954.
- **Status assigned: PROVED** for the (LA-EQ) reading and both constructive
  refutations; **POSED** for (LA-PADE)/(LA-DEG), which is not re-verified.
- **verify.py: PASS** (`local`, first run). H1 nullity-1 on `47/47` (q=97)
  and `37/37` (q=193) admissible builds; an H1+H2 exhibit at `q=97` with the
  **exact banked profile** `[7,7,2,2,2,2,2,1,1]`, `T = 9`, max
  pair-intersection `1`, `26x24`, nullity `1`; the generalized fence at a
  **fresh m = 3** over `mu_48`: `60x48`, rank `42`, nullity `6 = 2m`.
- **DUPLICATION WARNING:** the `Z^m - X^{2m}` family is already banked in
  `background/nodes/rate_half_layer_a_saturation_count_route_fence/
  statement.md:73-89`. **Cite, do not re-claim.**
- **WIRING GAP:** neither fence node currently cites (RIC3), though the
  addendum records all three as faces of one mechanism.

## 7. `share3_luroth_template` — (SHARE3-m)

- **Source:** A1:4507-4574 (round 36 bank 4); hand-checks A1:4509-4518;
  (LUR) A1:4520-4529; the m=4 gap A1:4530-4545; the guard A1:4546-4551;
  (DEG-m) A1:4552-4557; flat supply A1:4558-4565; scope and the compliance
  censure A1:4566-4574; predecessor demand law A1:3731-3751.
- **Status assigned: POSED** (the headline object does not exist and the
  (OUT-m)/(DEG-m) inheritances are POSED), with the constant-norm mechanism
  and the demand arithmetic proved inside. **Coordinator may prefer a split.**
- **verify.py: PASS** (`local`). Lüroth/waste arithmetic `m=3..12`; both
  demand rows with supply meeting demand only at `m = 3`; `D_max = 4m-8`;
  and an exhaustive constant-norm scan at `q = 193`: `41664` split cubics in
  `64` equidistributed norm classes, **max 31 collinear**, `9152` lines at
  `>= 8`.
- **THREE TEXT DEFECTS FOUND** — see DISCREPANCY D6, D7, D8.
- **MISS-2 note:** the `31`/`9152` count RAW lines; the source's `12/9/9`
  are structurally-verified complete fibres from SAMPLED bases. Different
  quantities; the former does not supersede the latter.
- **Provenance:** round-36 bank 4's one bare-python3 breach is recorded, not
  adjudicated.

## 8. `outm_identity_degm` — (OUT-m) and (DEG-m)

- **Source:** A1:3329-3350 (round 34 bank 3, with the two coordinator
  corrections); refinement A1:3752-3771 (round 35 bank 3, hand-checks
  A1:3686-3690); symbol collision A1:3767-3771; completion record
  A1:4552-4557.
- **Status assigned: POSED** (the source's own status, inherited).
  **No proof.md** — writing one would overstate the item.
- **verify.py: PASS** (`tiny`, first run). The double count exact on `200`
  synthetic configurations at `m = 3,4,5,6,8`; the aggregate `(m-1)(1+O)`
  attained only by outside deficiency; the `m=3` witness's `sum = 2`
  refuting the original rider; the corollary's `O <= m-3` qualifier, vacuous
  at `m=2`; the (DEG-m) floor forcing middle support for a degree-1 slope at
  every `m >= 4` and not at `m = 3`; the middle budget `(m-1)(m-2)`.
- **Could NOT verify:** the geometry (the placement argument is not
  re-derived); any DFS ceiling; (SAT3)-conditionality.
- **BLOCKING before wiring:** the `deg_H` symbol collision with the PROVED
  `a1_core_one_active_partition_incidence_reconstruction`.

## 9. `type2_ledger_scope_fence` — vacuity by sign

- **Source:** A1:3613-3625 (round 35 bank 2; razor integers replayed exact
  per A1:3608-3611); the 24-locator cap at A1:3672-3677.
- **Status assigned: PROVED** (exact arithmetic).
- **verify.py: PASS** (`tiny`). The razor floor `-1065151889407` to the
  digit; `2r <= R <=> a >= 3n/4` verified for every even `n <= 398` and at
  razor; the threshold `62r/63 = 98.412698%`; a worked small cell; the whole
  half-open bracket vacuous with the sign flipping to exactly `+1` at the
  excluded top `a = 3n/4 = k + 2^39`.
- **Edge character:** a route restriction, like the layer-A count fence — it
  does NOT discharge a requirement.

## 10. `sat3_ledger_corrections` — the realizability ledger record

- **Source:** A1:3428-3439 (round 34 bank 4); A1:4380-4396 (round 36 bank
  2); A1:3846-3860 (round 35 bank 4); the (L2) row A1:3403-3407 and
  `notes/pilots_20260811/r35_l2_gate/d1_results.txt:34-44`; DEF-ID posed and
  closed at A1:3497-3505 and A1:3588-3595.
- **Status assigned: HEURISTIC / RECORD.** **No proof.md** — there is
  nothing to prove and the ledger's conclusion is explicitly not licensed.
- **verify.py: PASS** (`tiny`, first run). The `(L2)` row `-1,+4,+17,+38`
  negative only at `m=1` and identical to the (BIV-G) and reduced deficits;
  DEF-ID exact for `m = 1..59` and coincidental; the `m=2` cell's two
  independent corrections and their `+8..+10` stacking; the preserved
  controls; `C(16m,4m-1)` for `m = 1..4`; the `16 = 16` calibration with its
  `9.75`-bit overestimate.
- **BLOCKING MISSING CONSTANT** — see DISCREPANCY D9. The verifier
  deliberately refuses to recompute the gate's bits.
- **SIGN-CONVENTION FLAG** — see DISCREPANCY D10.

---

## Cross-package structural observation

`2r > R` at razor is ONE inequality carrying THREE separate facts: the
type-2 ledger's vacuity by sign (package 9), the razor row sitting at
`r > R/2` so that the proved shape bound does not cover the crossing offset
(package 5), and therefore the necessity of an independent pigeonhole cap in
Statement U (package 1). Recommend the coordinator wire these three as a
cluster rather than as three unrelated fences.
