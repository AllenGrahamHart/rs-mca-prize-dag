# Upstream PR proposals — crosswalk of master's AUDITED results vs przchojecki/rs-mca towards-prize v13.2

Snapshot 2026-07-20. READ-ONLY reconnaissance. Base pin for any submission:
`origin/main@9908454995f3f195cfe748f35a1135211609d066` (upstream HEAD, towards-prize v13.2, 2026-07-19).
Our public mirror for SHA pins: `github.com/AllenGrahamHart/rs-mca-prize-dag@b8a169acb020f4a8cf990a552daf12b29127337b`
(in sync with master `prize` HEAD `b8a169ac`).

## 0. Headline finding (the honest crosswalk verdict)

The a-priori best bet — **our rate-half crossing determinations vs his §0.4 adjacent-finite-targets
safe side** — is a **PARAMETRIZATION MISMATCH / DIFFERENT-LANE**, not a match. Proving otherwise
would repeat the #750 over-claim. The mismatch is quadruple and numerically confirmed (exact integer,
`tools/ramguard`):

| axis | his §0.4 four targets | our exact determinations | verdict |
|---|---|---|---|
| row size `n` | `2^21` (2,097,152) | `2^41` (`rate_half_quadratic_exact_range`) | MISMATCH |
| field `q` | KoalaBear `p^6 ≈ 2^185.86`; Mersenne `p'^4 ≈ 2^123.36` | valid only `2^128 < q < 2^166.502` | MISMATCH (both outside) |
| target `ε*` | KoalaBear `2^-128`; **Mersenne `2^-100`** (extra-official) | `2^-128` | MISMATCH (Mersenne) |
| radius/`δ` regime | `δ ≈ 0.4678` (near-capacity, above Johnson) | `δ ≤ 1/4` (up to half-distance) | MISMATCH |

This is exactly the boundary our own WP5 verdict already recorded
(`critical/nodes/rate_half_band_closure` statement: "quantifier mismatch: K3's rows are n=2^21
extension fields vs the n=2^41 prime razor rows, transport NOTE-LEVEL"). **Our exact crossing does
not supply his §0.4 safe side.** That is the finding, and it is worth stating precisely to him.

What we CAN honestly offer on §0.4 is an **independent exact-integer audit** of the four crossing
locations and margins (we reproduce them from a separate codebase), plus a precise map of the
regime boundary (where an exact two-sided determination IS available: our `n=2^41`, `q<2^167` family).

Numeric confirmations run this session (`ramguard tiny`/`local`, exact integers):
- KoalaBear `q = p^6` (`p = 2^31−2^24+1`) → `B_* = floor(q/2^128) = 274,980,728,111,395,087`
  — matches independently the imported paving node's printed `B_*`.
- Mersenne `q = p'^4` (`p' = 2^31−1`) → `B_* = floor(q/2^100) = 16,777,215 = 2^24−1`
  — matches independently peer PR **#993** (DannyExperiments) printed budget.
- KoalaBear MCA radius `n − a0 = 2097152 − 1116047 = 981,105` = his §0.1 numerator exactly;
  `δ = 981105/2097152 = 0.46782732…` = his §0.1 `0.4678273…`.
- Full four-pair flip (exact `C(n,m)` vs `p^{m−K−pencil}·floor(q·ε*)`) reproduces every location
  and every margin: KB MCA `+8.978/−22.197` (22.2), KB list `+9.164/−22.011` (22.0),
  M31 MCA `+27.927/−3.259` (3.3), M31 list `+28.113/−3.073` (3.1). All PAIR OK.

---

## 1. Ranked candidate PRs

Ranking key = (relevance to his live priorities) × (audit readiness) × (faithfulness / low over-claim)
× (non-overlap with open PRs).

### RANK 1 — Independent exact-integer audit of the §0.4 four-pair crossings + constants (CROSSWALK/AUDIT)

- **(a) Priority item addressed:** §0.4 (THE live priority) + §3/§10 "audit the exact prize object,
  denominator, or endpoint convention" and success-criterion "formalized or independently replayed
  arithmetic gates."
- **(b) Master result + provenance:** `notes/correspondence/REGIME_MAP.md` + replay
  `notes/correspondence/four_pairs_exact.py`; node-local datum
  `critical/nodes/rate_half_band_closure/notes/upstream_determination_datum.md`. Banked wave-7
  (2026-07-07); re-verified this session by exact integer arithmetic (four PAIR OK). New this
  session: cross-source confirmation of both field budgets `B_*` (KoalaBear vs our imported paving
  node; Mersenne vs peer PR #993).
- **(c) Crosswalk verdict: MATCH (as a replay/confirmation).** We reproduce his four locations
  `1116047/1116046/1116023/1116022` and margins `22.197/22.011/3.259/3.073` exactly, and pin his
  exact exponent convention: list `unsafe(m) ⟺ C(n,m) > p^{m−K}·floor(q·ε*)`, MCA
  `⟺ C(n,m) > p^{m−K−1}·floor(q·ε*)` (the `−1` = pencil degree of freedom / identity-witness at
  `K = k+1`). It is a confirmation, not a closure.
- **(d) Honest scope / non-claims:** confirms only the first-moment crossing LOCATION arithmetic,
  the margins, the exponent constants, and the unsafe-side realization at `n=2^21`. Does NOT confirm
  the safe side (his conjecture at `a0+1`). Closes nothing; moves no score. Does not import or
  re-derive his witnesses.
- **(e) Type:** CROSSWALK / AUDIT contribution.
- **(f) Overlap:** NONE. Nobody replays the margins. Danny #993 (Mersenne scalar-descent) is a
  base/extension mechanism, not a margin/constant audit; scottdhughes #989–995 are the KoalaBear
  rank-nine ledger (safe-side construction), not an arithmetic replay.
- **Impact:** MEDIUM. Only thing we can put directly on his live priority §0.4 with zero over-claim
  and zero overlap; a genuine cross-implementation audit gate of the arithmetic underpinning his
  entire 0.4 execution target (and the Mersenne margin is only 3.07 bits, so an exact-integer, not
  floating, confirmation is load-bearing per his own "poly(n) loss is not a certificate" point).

### RANK 2 — Exact self-contained two-sided MCA threshold for the `n=2^41` rate-1/2 family, `2^128<q<2^167` (RESULT)

- **(a) Priority item addressed:** §10 "threshold-pinned rows, not just lower bounds"; strengthens
  §0.2's self-contained safe edge (from `(1−ρ)/3 = 1/6`) to an EXACT adjacent crossing up to
  `δ → 1/4` WITHOUT the BCIKS half-distance import — but is EXPLICITLY complementary to, not a
  solution of, §0.4.
- **(b) Master result + provenance:** `background/nodes/rate_half_quadratic_exact_range/statement.md`
  — PROVED, **wave-10 audited** (`WAVE10_AUDIT_FINDINGS.md`; commits `e86b0b88`+`568178b8`; all 7
  verifiers PASS, 25/25 independent checks PASS). Supporting layers:
  `rate_half_far_ca_anchor_pencil_normal_form` (`8997e257`), `rate_half_far_ca_rider_reduction`
  (`ce16a7fc`). Formula: `a_RH(q) = n − floor(q/2^128) + 1`, both halves (safe = quadratic-staircase
  equality; unsafe = universal MDS coordinate-tangent lower family).
- **(c) Crosswalk verdict: DIFFERENT-LANE from §0.4** (see §0 table). But a genuine threshold-pinned
  family in the below-half-distance regime his §3.1 calls the "controlled proving ground"
  (`δ ≲ (1−ρ)/2 = 1/4`, the regular-overdetermined regime). Applies to real prize-admissible rows:
  prime `F_q`, `q ≡ 1 mod 2^41`, `2^128<q<2^166.5`, `D` = order-`2^41` subgroup, `k=2^40` (`≤2^40`),
  `ρ=1/2`, `|F|<2^256`.
- **(d) Honest scope / non-claims:** NOT the near-capacity band; NOT his four §0.4 targets (different
  `n`, field, `δ`, and Mersenne `ε*`); NOT `q ≥ 2^167` (there only a bracket
  `a_RH ∈ [k+2^34, 3n/4]`, and `3n/4` for `q≥2^169` uses the BCIKS import — that piece is NOT
  self-contained); residual exact-budget cases `{2^39, 2^39+1}` remain.
- **(e) Type:** RESULT (two-sided threshold determination).
- **(f) Overlap:** NONE. No open PR touches rate-half `n=2^41` / far-CA / quadratic-staircase.
- **Impact:** MEDIUM–HIGH standalone (exact, self-contained, whole family); MEDIUM relative to his
  current laser-focus on the near-capacity `B_ap` Hankel band. Best packaged as "a determined
  threshold family that maps the exact boundary between determined (`q<2^167`) and conjectural
  (`≥2^167`, and his §0.4)"—i.e. context that sharpens where his hard problem actually begins.

### RANK 3 — §0.5 falsifiability objects: explicit machine-checkable prefix-fiber + split-pencil census (RESULT + LEAD)

- **(a) Priority item addressed:** §0.5 — his two named falsifiability objects: "super-polynomial
  primitive prefix fiber" and "super-polynomial primitive split-pencil family."
- **(b) Master results + provenance:**
  - `critical/nodes/rate_half_cyclic_rotated_prefix_floor` — PROVED, **wave-9 audited**; Modal
    verifier + backward audit `ap-YVuPe20N3lQuwNgedf0h5c`, manifest 178/178 in
    `ap-CRn9AwYF0xIGWOsvrDntDM`. An EXPLICIT super-polynomial cyclic-rotation prefix-fiber family
    (`≥ ceil(C(N−1,m)/(N q^{d−1}))` codewords), `s`-independent, list-unsafe across the whole
    residual band with a 75.08-bit margin even at `q=2^256`.
  - `background/nodes/rate_half_list_budget_three_quadratic_scroll_full_rank` — PROVED. Split-pencil
    normal form; the rank-deficient quadratic-scroll branch is proved EMPTY
    (`det C = b01^2(L12 L03 − L02 L13) ≠ 0`).
  - `critical/nodes/rate_half_list_adjacent_crossing` (TARGET) — budget-3 reduction of any
    4-codeword witness to EXACTLY 13 chambers (split-pencil normal form + Plücker gate),
    machine-enumerated and re-enumerated at audit (**wave-11/12**). **0/13 chambers closed.**
- **(c) Crosswalk verdict: PARTIAL / calibration.** Our prefix-fiber construction is an explicit
  instance of his named object, but on the UNSAFE side — it realizes (does not contradict) the
  envelope, so it CALIBRATES the falsifiability boundary rather than exhibiting a counterexample.
  Our split-pencil census proves one branch empty (evidence AGAINST a counterexample there) but does
  not settle the 13 open chambers.
- **(d) Honest scope / non-claims:** the prefix floor is a confirming construction, NOT a
  counterexample to his envelope; the split-pencil census is a reduction with the rank-deficient
  branch empty, NOT a proof that no super-poly primitive split-pencil family exists (13 chambers
  open); no threshold moved by the classification (the proved B*=3 bracket `[k+2^34, 3n/4]` stands).
- **(e) Type:** RESULT (prefix floor + empty branch) + REDUCTION/LEAD (13 chambers).
- **(f) Overlap:** NONE on rate-half prefix/split-pencil. Danny's counterexamples (#990) are a
  different O5c object; scottdhughes "rich-pencil" (#898/#899) is a KoalaBear/M1 compiler object,
  not our split-pencil.
- **Impact:** MEDIUM. Directly engages his §0.5 named, machine-checkable objects; honest about being
  boundary calibration, not resolution.

### RANK 4 (mention only) — nothing else clears the bar

- C36 `6^{n/4}` norm cutoff (wave-8): our dli/large-field lane; not on his current list.
- WCL slots (2,5)/(2,6) CLOSED: our dli lane; no §-item consumes it.
- DSP8 reduction / budget-3 split-pencil census as a "result": AMBER — leads only (folded into
  RANK 3 honestly, not sold as closure).

---

## 2. "Tempting but DON'T" (over-claim risk / mismatch / contributor already there)

1. **DON'T** submit our `a_RH` crossing as "the §0.4 safe side" or "the adjacent-agreement upper
   ledger." Quadruple parametrization mismatch (§0 table); it is the #750 trap re-baited.
2. **DON'T** submit anything on the **KoalaBear §0.4 safe side** — scottdhughes owns it live
   (#989, #991, #992, #994, #995: M1 rank-nine slack ledger). This is the hot M1 lane the brief
   warns off, and it is also Codex's branch.
3. **DON'T** submit anything on the **Mersenne-31 §0.4 safe side** — DannyExperiments #993 is live
   there (scalar-descent base/extension equivalence at agreement 1,116,023).
4. **DON'T** re-propose imgfib full-petal (already #750; mixed-petal gap open, catch #212). A
   narrower follow-up is not currently ready above lead-grade.
5. **DON'T** propose `paving_rf3_double_prime_koalabear_safe_rows` — that node is IMPORTED from
   upstream (`source: przchojecki/rs-mca@999b8f3a`); it is THEIR result, and it is only a one-sided
   safe bound at `A=1,485,170` (radius 611,982), far above his §0.4 target radius 981,104 — it does
   not pin the threshold anyway.
6. **DON'T** present budget-3 (13 chambers) or DSP8 as a closure — 0/13 chambers closed; reductions
   only.
7. **DON'T** silently use the delta≤1/4 self-contained framing to imply we beat his §0.2 `1/6` for
   HIS KoalaBear/Mersenne rows — the improvement is for OUR `n=2^41`, `q<2^167` family; say so.

---

## 3. Recommended action

Submit **RANK 1** as the single best opportunity (draft: `upr_draft_1.md`): honest, on his live
priority, zero over-claim, zero overlap, real audit value. Hold **RANK 2** (`upr_draft_2.md`) as a
strong standalone RESULT to offer if he wants determined-threshold context / a sharper regime
boundary. Hold **RANK 3** (`upr_draft_3.md`) as a §0.5-facing lead. All three fence off the prize and
his four §0.4 targets explicitly.
