# AUDIT CHECKLIST — MINT REMAINDER package (F2 lane + P-B lane)

What the coordinator should hand-verify before wiring, per package, plus
**every** place where I added an inference, reconstructed a derivation,
or found the source ambiguous or wrong. **Flags are raised, not
guessed.**

Replay command for all four (from the repo root):

```text
tools/ramguard tiny -- python3 <node>/verify.py
```

Measured runtimes: **0.03 / 0.71 / 0.67 / 1.84 s** (packages 1-4 in the
order below). All pure-python integers (plus exact `Z[zeta_p]` vectors),
deterministic, no third-party imports, no reads outside their own
directory — all pins inlined, provenance paths in comments only — so they
keep passing after the move. Check totals **11 / 9 / 9 / 8 = 37 PASS,
0 FAIL** at draft time. **Every assertion is an exact integer (or exact
`Z[zeta_p]`) comparison**; the only floats in the wave are the printed
bit-margin figures in package 3's check E, which are a DIAGNOSTIC — that
check's own assertions are the exact integer inequalities
`8n^3 > ceiling * 2^23` (all six rows) and `8n^3 < ceiling * 2^24`
(RowC 1/16, pinning 23 bits as the honest headline).

Brief asked for FIVE nodes; **four are drafted, one is REFUSED** (F0.a, and WIRING section 3).

---

## 0. Cross-cutting flags (read first)

- ***(F0.a — the REFUSAL, and where its content went.)*** `pb_l1_lemma`
  is **not drafted**: it is already banked verbatim (WIRING section 3). Its
  P-B-specific corollary is minted INLINE as Lemma 0 of
  `pb_design_ceiling`, mirroring the band wave's F0.b decision (fibre
  identity inline in the cost theorem). **Coordinator's call:** accept
  the refusal + inline placement, or commission a P-B-gauge alias node.
  I recommend the refusal.
- ***(F0.b — two proofs are RECONSTRUCTED, not transplanted.)*** In this
  wave, two proofs were written by me because **the record contains no
  derivation to transplant**: package 2's Theorems 2/3 (the value
  `D = ((p-1)/2)^2` and its scope) and package 4's Claims 1-4 (the whole
  block dichotomy). Both are flagged in their own `proof.md` headers.
  These are the two places that most need a line-audit: **F2.b-F2.d** and
  **F4.a-F4.e**.
- ***(F0.c — the F2 nodes would be ORPHANS.)*** No `dag.json` node exists
  for the F2 slice theorem, PP5.0, (H-flat), or the K1 mass obligations;
  the statement of record is a draft document
  (`notes/pro_briefs_20260801/responses/F2_SLICE_THEOREM_DRAFT.md`). The
  existing F2 reds (`f2_growing_order_myerson` TARGET,
  `f2_conditional_close` CONDITIONAL, `u2c_giant_tnull_dichotomy`
  CONDITIONAL) are about Myerson-at-growing-order / extras, **not** window
  flatness, so I proposed **no `ev` edge** rather than invent one.
  **Decide: wire as standalone PROVED background nodes now, or hold both
  until the slice-theorem obligation is itself a node.**
- ***(F0.d — three corrections to the record, none silent.)*** Each is
  machine-witnessed inside the relevant `verify.py`:
  1. **F3.d** — the design ceiling is NOT an unconditional cap on
     realised families (a spread, zero-collision, realised family of size
     20 exceeds it). This has a consequence **for the already-banked
     `xr_two_slope_cost_theorem`**.
  2. **F3.a** — the P-B lane's "spread `<=>` pairwise-transverse" is
     one-directional as written; the exact equivalence is with `<= K`.
  3. **F2.c** — the parity-defect corollary's stated scope ("the
     FULL-group window has `D = ((p-1)/2)^2` exactly") is too broad by
     exactly `2(p-1)` frequencies.
- ***(F0.e — nothing was strengthened where the brief said not to.)***
  The antipodal descent lemma is drafted **exactly** in the strongest
  already-verified form (`tower.py:22-43`), clause for clause. What I
  added is only: written-out proofs of clauses (i) and (ii) (the source
  says "[LTE]" and states (ii) without argument), and the two-line
  derivation of `flat = 0` from `omega^p = -1`. No clause was widened.
- ***(F0.f — compute-law self-report, VIOLATION, flagged not hidden.)***
  Every verifier run, every probe and every source-triage computation ran
  under `tools/ramguard`. **One exception:** a single bare `python3`
  heredoc was used to text-substitute four literal tuples inside my own
  draft `pb_block_dichotomy/verify.py` (fixing shapes where `m` did not
  divide `n`). It performed no arithmetic of record and touched no file
  outside my pilot directory, but the law is absolute and the lapse is
  recorded here. The band wave recorded a comparable lapse; a standing
  reminder in future pilot briefs would help.

## 1. `f2_antipodal_descent_lemma`

Hand-verify:

1. **Clause (i)'s factorisation** `p^{2^j}-1 = (p-1)(p+1)prod_{i=1}^{j-1}(p^{2^i}+1)`
   and the two valuation facts: `v_2(p+1) = 1` **because `e >= 2` forces
   `p == 1 mod 4`**, and `v_2(p^{2^i}+1) = 1` because an odd square is
   `1 mod 8`. The `e >= 2` hypothesis is doing real work here — at
   `e = 1` the lemma is false.
2. **Clause (ii)'s gcd step**: `gcd(n_j, q_{j-1}-1) = 2^{e+j-1}` uses that
   `n_j` is a pure 2-power (no odd part). This is exactly the caveat
   "fails if `n` has an odd part" (`REPORT.md:70`) — check the statement
   carries it.
3. **Corollary B's `sigma` identification** — the load-bearing step, and
   the one place I phrased the model differently from the source. The
   source says "`s^- = -s^+` hence `Delta = 2 sigma^+`"; I inserted the
   intermediate lemma **`sigma(s)` is the CENTRED representative of
   `s mod p`, hence an ODD function of `s`**, which is what actually makes
   `sigma^- = -sigma^+`. Three lines; please check them (`proof.md`,
   Claim 5, facts (N1)/(N2)). The degenerate coordinate `s^+ = 0` is
   handled separately.
4. **Corollary C** (`R_p = 1`, `flat = 0` exactly) — two lines, uses
   `omega^p = -1` and `p` odd so that `k = p` is an ODD mode. Confirm
   nobody can read `flat = 0` as approximate.
5. **Flag (F1.a — what is NOT claimed.)** The degeneracy law
   (`n_ord/gcd(n_ord,p-1) == 2 <=> all Delta even`, 194 censused rows) is
   labelled MEASURED and only the `=>` direction for rung subgroups is
   proved; and the `-log2 rho_b <= log2 p + o(1)` corollary — which
   `REPORT.md:45` attaches to T1 — is **excluded** from this node (the
   ladder is exact at toy scale with a measured saturation; the `o(1)` is
   not proved). **Confirm you want T1 minted without that corollary.**
6. **Flag (F1.b — the KoalaBear primality screen.)** Check A0 proves
   primality by trial division to `5e4` and asserts `50000^2 > p`; that
   is a complete proof, not a screen, but the label should be read once.

## 2. `f2_parity_defect_certificate`

Hand-verify:

1. **Theorem 1 is the pilot's** (`deployed.py:37-56`), transplanted in
   substance. The only content is `omega^{k(x+p)} = -omega^{kx}` for odd
   `k` plus the class collapse. Check the statement makes clear that
   `(DEF)` is an **upper bound**, not an identity.
2. ***(F2.b — RECONSTRUCTED, needs a real line-audit.)*** The value
   `D = ((p-1)/2)^2` has **no derivation anywhere in the record** — the
   pilot states it and checks it at `p in {11,13,19,23,31,41}`,
   `c in {(1,1),(2,3)}` (`verify.py:300-321`). My proof is a four-step
   chain: (a) `c_d = A(d)` needs `a_c != 0`; (b)
   `A(t) = (-1)^t (p-2t)` for `0 <= t <= M` by the overflow count
   (exactly `t` of the `p` centred parameters overflow); (c) the support
   is a **half-system**, which needs `b_c != 0`; (d)
   `sum_{t=1}^{M}(p-2t) = M^2`. **Please check (b) and (c) by hand** —
   they are the two non-obvious steps. Sanity anchors in the file:
   `A(0) = p` and `sum_t A(t) = 1`.
3. ***(F2.c — SCOPE CORRECTION to the record.)*** `REPORT.md:37` says
   "the FULL-group window has `D = ((p-1)/2)^2` exactly" with no
   condition on `c`. **That is false for exactly `2(p-1)` frequencies**:
   the line `b_c = 0` (`c in F_p^*`, `Delta == 0`) and the line
   `a_c = 0` (`c in w F_p^*`, all `Delta` even) both give `D = m`. The
   pilot's two tested frequencies both satisfy `a_c b_c != 0`, so its
   check never saw them. Verified exhaustively here over every frequency
   at `p = 11,13,19,23,31,41` (3,552 frequencies). **Confirm the
   corrected scope is what goes on record**, and note these two lines are
   precisely the "two parity-pure linear subspaces" of `REPORT.md:11`.
4. **The multiplicity law** (`sorted non-zero Delta-counts = [1..p-1]`)
   is part of the pilot's A8 assertion. Here it is labelled **MEASURED**
   and is used in **no** proof. It held at 100% of the `a_c b_c != 0`
   frequencies tested. Confirm the label.
5. ***(F2.d — the flip statement, sharpened.)*** `REPORT.md:71` records
   that `max_{k != p}|R_k|` is convention-dependent. For `D` I prove the
   precise version: invariant under the **global** reversal
   (`Delta -> -Delta` preserves parity and permutes `d -> -d`), **not**
   under partial flips — the verifier exhibits 16-23 of 30 random partial
   flips changing `D`. Check the statement forbids quoting `D` label-free.
6. **Corollary 4** — confirm the "tight but empty" reading is the one you
   want on record: at deployed windows `D = m` makes `(FLAT)` vacuous,
   and the true `flat = 0` means nothing was lost.

## 3. `pb_design_ceiling`

Hand-verify:

1. ***(F3.a — CORRECTION: Lemma 0 is one-directional in the record.)***
   `pb_h4_hunt/REPORT.md:29` states "spread `<=>` pairwise-transverse
   condition spaces (dual distance `K+1`)". By banked L1,
   `C_S ^ C_T = 0` iff `|S^T| <= K` — so **spread implies transverse, and
   the converse fails exactly at core `= K`**. The verifier exhibits 99
   such pairs. The gap matters for this lane: core-`K` pairs are
   `Gamma_hi`, not `Gamma_lo`. Nothing downstream in the node uses the
   false direction (Claim 1 needs independence, which is stronger).
   **Confirm the correction, and check whether any other P-B record
   quotes the equivalence.**
2. ***(F3.b — margin arithmetic differs from the pilot's, on purpose.)***
   The pilot's "`2^23.1` to `2^117.4` below `8n^3`" is computed from the
   **free-slope** ceiling `383/447/959`. I derive forcedness from the
   **proved prescribed-slope** ceiling `307/358/639 / 383/447/959`, giving
   margins `24.74/24.52/23.68` (RowC) and `117.42/117.20/116.09` (prize)
   — slightly BETTER, and not resting on the unproved form. The headline
   `<= ~960 designable` and `>= 1 - 2^-23 forced` hold under both (both
   maxima are 959). **Check you want the proved-form numbers on record**;
   `OFFICIAL.json`'s `ceiling_below_budget_bits` will then differ from
   the node by design, not by error.
3. ***(F3.c — the free-slope form is NOT PROVED, and I say so.)***
   `expC.py:19-21, 352-364` introduces `M <= (2r-1)/(h-1)` as "the
   determinantal count" / "the true ceiling **SHOULD** be". The pilot
   REPORT headlines it as "DESIGN CEILING". I demote it to a recorded
   non-claim (Theorem 2). Also note the banked proved table has the
   per-DATUM `floor((2r-1)/(2h-2)) = 191/223/479`, and
   `2 x 191 = 382 != 383`, so the per-support number is **not** a
   corollary of the banked entry. **Confirm the demotion** — this is the
   single largest difference between the node and the pilot's headline.
4. ***(F3.d — a consequence for the ALREADY-BANKED node. Please
   read.)*** `background/nodes/xr_two_slope_cost_theorem/statement.md:74-79`
   states the corollary as: "*a realisable family carried by `V` rays has
   `rank <= V h`, so `V <= (2(n-k)-1)/h`*". As a chain that is a
   non-sequitur unless `rank = Vh`, and the `mu_20`-orbit exhibit
   replayed here is a **concrete realised, spread family with `V = 20`
   rays and `V > (2r-1)/h = 10`**. The banked node's own NOT-claimed
   section already says the bound is "conditional on ray independence —
   exactly the support-4 gap" (`statement.md:119-122`), so this is a
   **wording** issue in the corollary sentence, not a false green. I did
   **not** edit that node (outside my remit). **Recommended: a node-local
   addendum on `xr_two_slope_cost_theorem` making the independence
   hypothesis explicit in the corollary itself, citing the `mu_20`-orbit
   as the witness** (per the standing node-local-notes rule). Coordinator
   decision.
5. **Claim 2's "maximal independent sub-family" step**: the forcedness
   statement turns on reading "forced" as "condition block lies in the
   span of the others". Check that this is the reading the lane wants
   when it says a counterexample is "`1 - 2^-23` forced" — the pilot's
   phrasing is "at most ~960 of its members can be **independently
   designed**", which matches.
6. **Theorem 3's invariance sentence.** The proof asserts the witness set
   is closed under the index shift as a **machine fact** (the verifier
   checks it) rather than deriving it from the substitution
   `x -> omega x`; the honest reason is that the substitution scales `u`
   and `v` by different powers, so the clean statement needs care.
   **Either accept the machine fact, or ask for the two-line
   substitution argument to be written out.**

## 4. `pb_block_dichotomy`

Hand-verify (**this is the package with the weakest source support**):

1. ***(F4.a — THE HEADLINE FLAG: no written proof exists in the
   record.)*** `pb_h4_hunt/REPORT.md:15` asserts "*Block dichotomy*
   (**proved + verified**)"; `expE.py:4-14` states it and defers the
   proof "to the report", where none appears. A grep over `background/`,
   `critical/`, `dag.json` and the whole pilot tree finds no derivation.
   `FABLE_AUDIT.md:19-23` records that the coordinator hand-verified "the
   coset power-sum vanishing behind the dichotomy" — i.e. Claim 3's
   computation, not Claims 1/2/4. **Everything in this node's `proof.md`
   is written by me.** If the coordinator is not satisfied by a
   line-audit, the honest fallback is to mint Claims 1-3 only (they are
   elementary) and drop Claim 4 to a recorded non-claim.
2. ***(F4.b — COORDINATE DISCREPANCY in the source, load-bearing.)***
   `expE.py:7-8` states the collinearity conclusion for **power-sum**
   vectors `beta_j = (p_1(B_j),...,p_h(B_j))`; `expE.py:49-50` computes
   `core.moment_vector`, which is the **elementary-symmetric** vector
   (`core.py:144-150`). Newton's identities are polynomial, not affine,
   so the two conditions are inequivalent — the verifier exhibits the
   `p`-collinear triple `(0,0,0),(1,0,0),(2,0,0)` whose `e`-images have
   affine rank 2. I state Claim 4 in `e`-coordinates (what the code
   tests, and what the proof gives). **For COSET blocks both readings
   coincide** (direction `e_m` either way), so Claims 2-3 and
   (SF-SELFCOLLISION) are unaffected. **Confirm the `e`-reading is
   correct for the lane's intended use.**
3. ***(F4.c — HYPOTHESIS CORRECTION.)*** `expE.py:5` writes
   `b >= a+1`. At `b = a+1` only two blocks vary and collinearity is
   vacuous. My proof needs `b >= a+2` for `a >= 2` (and nothing for
   `a = 1`). Check the corrected hypothesis, and check whether any
   downstream use assumed the weaker one.
4. **Claim 4's chaining step** (the only genuinely new inference in this
   package): fix `a-1` blocks and vary the last, giving
   `R_{S_J} = C_{J_0} R_{B_j}` with `C_{J_0}` a **unit** of
   `F_q[Y]/(Y^{h+1})`; multiplication by a unit is linear and bijective,
   so it maps lines to lines in both directions; then two `(a-1)`-sets
   differing in one element give lines sharing `b-a >= 2` points, hence
   equal. **Four lines — please hand-verify.** The verifier checks the
   ring identity, unit-ness, inverse and linearity separately (check E).
5. **Claim 3's `m > h` branch, as re-phrased.** I sharpened the source's
   "`beta_j = 0` (one slope, strip)" to the exact statement: all `E(S_J)`
   coincide at one point `P`, so if `beta != 0` then `P = alpha + z beta`
   for **exactly one** `z` and every member is a witness at that same
   slope; if `beta = 0` there is no slope parameter. **Either way the
   family exhibits one slope.** This is stronger and cleaner than "`beta`
   may be taken 0"; check the phrasing.
6. ***(F4.d — the residue is OPEN and I replay it as such.)*** The
   non-coset residue (blocks of size `m >= h+1` with collinear moment
   vectors) is measured **FEASIBLE** at 4 of the pilot's 5 shapes. My
   independent replay at `n=20, q=101, h=2, m=3` reproduces `EXPE.json`
   **exactly**: 1140 blocks, richest line 28, 4 of them disjoint, family
   `C(4,2) = 6`, feasible. It is closed at official scale only by a
   first-moment count that `REPORT.md:61` explicitly says "is **not a
   theorem**". The node labels this MEASURED-OPEN and claims nothing.
   **Confirm the label survives into any consumer.**
7. ***(F4.e — the SELECTOR CATCH must travel with the node.)***
   `Gamma_lo = 0` for split-fibre is a **joint** identity-plus-
   support-keyed-selector statement (`REPORT.md:43`,
   `FABLE_AUDIT.md:26-36`): a uniform selector leaves `~q e^{-nu}`
   survivors, `~2^187 >> 8n^3` at official RowC 1/4 (`nu = 3.0`), while
   support-lex first-match measured 0 at 18/18. This node proves the
   **identity half only**, and says so. Since the P-B TARGET's addendum
   cites (SF-SELFCOLLISION) as closing kill line K1 "structurally,
   selector-free", **check the addendum's wording against this node** —
   the audit already adopted the amendment, but the two texts should
   agree.

## 5. Things I did NOT do

- No `dag.json`, `background/`, `critical/`, `tools/` or m2-related file
  was touched; the verifier manifest was not regenerated (it must be,
  after the move). Everything lives under
  `notes/pilots_20260803/mint2_prep/`.
- I did not run any pilot's own scripts. Every number cited was
  re-derived in a fresh implementation inside each `verify.py` and
  cross-checked against the pilots' persisted JSONs
  (`EXPC_*.json`, `EXPE.json`, `OFFICIAL.json`), never against prose
  alone. Two independent replications came out **byte-identical** to the
  record: the `mu_20`-orbit numbers (40 witnesses, rank 31/60, 20
  slopes) and the residue line census (28 on the line, 4 disjoint).
- I did not attempt: the non-split-fibre concentration half of (H4); the
  RowC 1/4 q-scope decision; the word-model exhaustive search; the
  generic-frequency flatness bound (T3); or anything toward the K1 mass
  obligations (O1)-(O3) — which are **OPEN constructive obligations**,
  not theorems, and whose only measured constant is explicitly "banked as
  a labelled first-moment heuristic".
- I did not mint `pb_l1_lemma` (F0.a) and did not edit
  `xr_two_slope_cost_theorem` despite finding a wording issue in its
  corollary (F3.d) — that is surfaced for the coordinator, not applied.
