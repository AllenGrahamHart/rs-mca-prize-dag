(Coordinator-persisted verbatim from the pilot's final message, 2026-08-06.)

Clean run: exit 0, **137/137 PASS**, nothing outside the pilot directory touched, no REPORT.md written. Here is the report.

---

# ROUTE (b) — PILOT REPORT (round 19, GENERATIVE)

**Files (all under `/home/u2470931/smooth-read-solomin/prize/notes/pilots_20260806/tern_route_b/`):** `PREREG.md` (coordinator brief + my appended pre-registrations P1–P8, grid, falsifiers — written before any computation), `PROOFS.md` (derivations), `verify_route_b.py`, `VERIFY_LOG.txt` (137/137 PASS, exit 0).

## VERDICT (R5) — **DEAD AS POSED / TRANSFORMED RESIDUAL**

Route (b)'s sizing is **refuted**, and both implementations I could construct are dead by measured margins. What survives is not the route but a changed object: three new reductions and one new unconditional theorem.

- **The "factor-2 headroom" does not exist.** The correct Weil comparison at the official row is `deg(f_u)·√p = 2^65.000` against `|H| = 2^39` — **vacuous by exactly 26.000 bits**, not a factor 2 of slack.
- **The only executable substitute lands on THEOREM Z-NOGO's own threshold.** Replacing Weil by moments of `V_1` evaluated through THEOREM Z-2 gives an unconditional `Z_1 ≤ 2^{0.8908·S}`, and reaches `2^{o(S)}` only if `log2 p ≤ 3.0529`, i.e. **`p ≤ 8.30`** — against the admissible floor `log2 p ≥ 39`. Gap: **60.95 bits in `log2 p`**; equivalently the exponent budget delivers `3.197e10` of the `2.749e11` bits required, short by a factor **8.60** (`2.429e11` bits).
- **Honest limit of the kill.** This is weaker than Z-NOGO. Z-NOGO proves *no* bound in its family can close. I prove the route's *sizing* is wrong and that the two supplies I could find (uniform Weil; Z-2 moments) both fail by stated margins. I do **not** prove no character-sum argument can work. Board consequence, stated plainly: with (a) dead quantified, (c) localising only, distance+counting killed by Z-NOGO, and (b)'s sizing now refuted, **the F2 knife edge has no route with a named instrument behind it.**

## R1 — THE EXACT CHARACTER-SUM FORM: **PASSED (the gate holds)**

`Z_1 = p^{−R} Σ_{u∈F_p^R} Π_{s&lt;S} (1 + cos(2π f_u(ζ^s)/p))`, with `f_u(X) = Σ_{r&lt;R} u_r X^{2r+1}` odd of degree `≤ 2R−1`. Machine-verified **exactly** (integer arithmetic in `Z[x]/(x^p−1)`, zero floating point) at G1–G4, and numerically at all six rows to relative `&lt; 5e-14`. `Z_1` itself computed exactly by two independent methods (meet-in-the-middle; brute force over `3^S`), agreeing.

**CATCH-B1 (against our own bank).** `notes/pilots_20260806/z1_ternary_mass/PROOFS.md:394` states verbatim:

```
394	`Z_1 = p^{-R} sum_{u in F_p^R} prod_{s&lt;S} (1 + 2cos(2π f_u(omega^s)/p))`
```

The local factor `1 + 2cos` is the **unweighted** one — that formula computes `|T ∩ ker A|`, not the weighted mass. Machine-separated at all six rows: at G4 it returns `4833.000000 = |T ∩ ker A|` while `Z_1 = 9.387207`. The line is explicitly disclaimed as non-theorem at `PROOFS.md:545-546`, so nothing downstream breaks, but the two differ by `(3/2)^S = 2^{0.585·S} = 2^{37.23}` bits in the trivial-character term.

**CATCH-B2 (against the brief).** `PREREG.md:30` says "multiplicative-character tuples". The syndrome group is additive `F_p^R`; the tuples are **additive** characters. The brief's own local-factor hint at `PREREG.md:34-35` is the right shape and evaluates to `1+cos` — the hint is right, the label is wrong.

## R2 — THE CANCELLATION LEDGER: **theorem-grade, and it kills the headroom**

**PROPOSITION 3 — route (b) is not a cancellation route.** Every local factor `1+cos θ ≥ 0`, so `Z_1 = p^{−R} Σ_u P(u)` is a sum of `p^R` **non-negative** terms. No cancellation between character tuples is available *in principle*. What the route needs is equidistribution of the value multiset `f_u(H)` plus a **count** of exceptional `u`. Two floors fall out free: THEOREM Z-FLOOR in one line (`Z_1 ≥ p^{−R}P(0)`, no Cauchy–Schwarz needed), and a new Galois-norm line floor (`Π_{t≠0} P(tu) = 2^{−S(p−1)}Nm(N(u))² ≥ 2^{−S(p−1)}`, since `σ_t(N(u)) = N(tu)`).

**PROPOSITION 4 — the main term is not the main term.** The trivial-character term is `2^{S−R log2 p}` = `2^{−46.025}` (banked reading) / `2^{+17.975}` (exact balance) — reproducing the banked knife edge to 0.005 bits, which validates the decomposition. But `Z_1 ≥ 1` unconditionally. So **the error term exceeds the main term by ≥ 46.02 bits, unconditionally, with no hypothesis.** R2's literal target ("what bound per tuple keeps the total error below the main term") is **unsatisfiable as posed**; the correct target is `error ≤ 2^{o(S)}`.

**THE LEDGER (exact).** `Z_1 ≤ 2^{o(S)}` **iff** `|{u : P(u) ≥ 2^{cS}}| ≤ 2^{(1−c)S + 46.02 + o(S)}` for every `c ∈ [0,1]`. It is a **tail-count** requirement, not a per-tuple bound.

**LEMMA 2 answers the brief's structural question outright.** `PREREG.md:44-47` asks whether the relevant sum is over the full subgroup or genuinely over the half. Because every exponent in `Λ` is **odd**, `f_u` is odd and `H = Y ⊔ (−Y)`, so `2 Re W_j(u) = V_j(u) := Σ_{x∈μ_{2^{e_p}}} e_p(j f_u(x))` **exactly**. It is a **complete sum over the full subgroup**; no partial-sum loss bites. Verified as an exact `F_p` multiset identity on all six rows.

**LEMMA 5 (AM-GM).** `P(u) ≤ (1 + V_1(u)/|H|)^S`, verified at every `u` on all six rows (worst ratio 1.000000). This needs **only `j = 1`** and loses no `log J`, strictly beating the Fourier/majorant route (which needs all `V_j`, `j ≤ J`, plus a Beurling–Selberg majorant for the log singularity). Needed input: `max_{u≠0}|V_1(u)| = o(|H|)`.

**CATCH-B3 (against the node's sizing).** `background/nodes/f2_z1_mass_knife_edge/statement.md:56-59` and `z1_ternary_mass/PROOFS.md:398-400` size the route as `√p·log p = 2^38` vs subgroup `2^39` — "a factor 2 of headroom". That comparison **drops the degree factor**. Restored: `deg·√p = 2^65` vs `|H| = 2^39`. Non-vacuity needs `deg ≤ |H|/√p = 128.00`, but `deg = 2R−1 = 2^33.000` — useful only for `u` supported on the first **64** of `R = 4,294,967,340` coordinates. The sizing is wrong in both factors: the `log p` (a Polya–Vinogradov interval factor) does not belong either, by Lemma 2 — wrong once favourably, once fatally.

**THEOREM 7 (new, unconditional).** `Z_1 ≤ 2^{0.8908·S} = 2^{2.449e11}` against trivial `2^S` — a saving of `3.002e10` bits. Proof: Lemma 5 + Chebyshev on the `2k`-th moment `Σ_u |V_1(u)|^{2k} = p^R N_k`, with `N_k ≤ (2k−1)!!·|H|^k` for `k ≤ R` by THEOREM Z-2 (odd exponents let every solution be reduced to an integer relation of `ℓ1` weight `≤ 2k ≤ 2R`, forced to zero). Machine-verified: `N_2 = 720 ≤ 768` (G1), `2976 ≤ 3072` (G4). **The cap `k ≤ R` is sharp** — at G2 (`R=1`) the bound already fails at `k=2`: `N_2 = 1104 &gt; 768`. Z-2's hypothesis is exactly load-bearing.

**COROLLARY 8.** Theorem 7 closes iff `log2(e·log2 p) ≥ log2 p`, i.e. `p ≤ 8.30` — **THEOREM Z-NOGO's threshold** (`statement.md:40-44`: "discharges only if p &lt;= 8"). Not a coincidence: the moment evaluation consumes a *distance* theorem plus a *count*, so it is a member of the family Z-NOGO killed. **Honesty on the constant:** the `e` comes from Stirling; cruder constants give "closes for no `p` at all". `8.30` is the most generous provable value; the *shape* (`log2 p ≤ O(log log p)` vs `log2 p ≥ 39`) is constant-free.

## R3 — STRUCTURED-SET PRECEDENT: **the headroom is illusory, but not for the briefed reason**

**CATCH-B4 (against the brief's premise).** `PREREG.md:20-23` asserts the round-15 loss happens "because sqrt-cancellation is exactly what fails on structured sets". That because-clause is **not in the round-15 record**. `notes/pilots_20260804/mun_anticoncentration/REPORT.md:87` states the cause as the **L2→L∞ conversion** (`max_b N(b) ≤ √(Σ N(b)²)`), and its own F4 table shows the second moment within 1.4% of flat at all but the smallest fixture — square-root cancellation *held* there. (The "1–2 orders" figure is also loose: replayed `L2/true-max` ratios are `2.92, 2.03, 4.12, 6.64, 9.10, 9.85` — 0.31–0.99 decimal orders — and they track `√p`. Cite the `√p` factor, not the orders.)

Applied on its true mechanism, route (b) is **new in two respects and identical in the fatal one**:

| round-15 failure mode | hits route (b)? |
|---|---|
| L2→L∞ conversion loses `√p` (`mun REPORT:87`; `F2_L3_DESIGN.md:29-37`) | **NO** — Lemma 5 makes it a *first*-moment statement; no mean-to-max step exists. Genuinely new. |
| partial-sum/interval loss over a subgroup (`f2_opening/REPORT.md:45`) | **NO** — Lemma 2 makes it a *complete* subgroup sum. Genuinely new, favourable. |
| **Weil vacuous by DEGREE** (`mun REPORT:71`, misses 13.5–107 bits; `f2_opening/REPORT.md:45`) | **YES, identically** — `2^65` vs `2^39`, **26 bits**. Same mechanism, same verdict. |

Route (b) escapes the two losses the brief feared and dies of the third, which the brief did not name.

## R4 — TOY VALIDATION (2-power grids only, CATCH-Z6 automatic since `S = 2^{e_p−1}`)

```
  row  p      S    R      max|V_1|        |H|    sqrt|H| Weil deg*sqp   max/|H|  maxlgP/S
  G1   17     8    2         8.030         16      4.000     12.369    0.5018    0.1638
  G2   113    8    1         7.395         16      4.000     10.630    0.4622   -0.1778
  G3   241    8    1         6.915         16      4.000     15.524    0.4322    0.2212
  G4   97     16   2        17.706         32      5.657     29.547    0.5533    0.5721
  G5   353    16   2        18.698         32      5.657     56.365    0.5843    0.4764
  G6   673    16   2        20.254         32      5.657     77.827    0.6329    0.6453
```

1. **Parseval is exactly right in the bulk:** measured RMS `|V_1|` = `3.894, 3.723, 3.873, 5.648, 5.656, 5.657` vs `√|H|` = `4.000, 4.000, 4.000, 5.657, 5.657, 5.657`. The *typical* tuple shows full square-root cancellation to three digits. Route (b)'s problem is entirely in the tail.
2. **The maximum is a constant fraction of `|H|`, rising with `p`** (0.43 → 0.63) — the measurement that makes the uniform route look capped.
3. **The vacuity criterion `deg ≤ |H|/√p` is confirmed on both sides** (G1–G4 useful, G5–G6 vacuous); the official row sits 26 bits inside the vacuous side.
4. **Calibration clause honoured:** all six toys have `Z_1 ∈ [1.098, 9.387]` — the terminal is *true* at toy scale, and per `statement.md:64-69` that is **not evidence** at the official row. Toys were used only to verify identities and measure constants; nothing in Theorem 7 / Corollary 8 depends on a toy. **AK-UNIT respected** — every statement bounds an archimedean magnitude; no congruence conclusion about any count.

## R5(iii) — THE 2-POWER GAUSS-SUM CHASE (chased hard; briefed version is misdirected)

**PROPOSITION 9.** The characters that enter are those **trivial on `H = μ_{2^{e_p}}`**, i.e. of order dividing `d = (p−1)/2^{e_p}`. Since `v_2(p−1) = e_p` **exactly**, `d` is **odd** — so quadratic and quartic symbols are precisely the characters that never appear. Their classical exact evaluations govern sums over the index-2/index-4 subgroups (squares, fourth powers), the *opposite* object. **No classical closed evaluation applies on that ground.**

**PROPOSITION 10 (the one genuine 2-power exactness found, machine-verified).**
`log2 P(u) = −S + 2n_0(u) + 2 Σ_{c≠0} (n_{c/2}(u) − n_c(u))·log2|2 sin(πc/p)|`,
with `n_c(u) = #{s&lt;S : f_u(ζ^s) = c}` and `c/2 = c·2^{−1}` in `F_p`. Exact, not a bound; normalisation-free (`Σ_{c≠0}(n_{c/2}−n_c) = 0`). The entire `p`-dependence runs through the **doubling map `c ↦ 2c`** and the log-sine weights — a Dedekind-sum-shaped object, strictly finer than `V_1`. **Recorded as a lead, not a route:** I have no bound for it, and any argument ending in a low-`ℓ1` relation count re-enters the family of Corollary 8.

## HONEST RESIDUALS

1. **The tail-count question is not closed.** I killed the two supplies I could construct (uniform Weil; Z-2 moments). A third — e.g. via Proposition 10's doubling identity, or a moment bound not routed through Z-2 — is not excluded. Corollary 8 is a statement about *my* implementations, not a Z-NOGO-strength no-go.
2. **No lower bound on `max_u |V_1(u)|` at the official row is claimed.** The degree-count construction in `PROOFS.md` §3.4 is explicitly flagged HEURISTIC (the residual `|H| − 2(R−1)` unit vectors are not provably `O(√|H|)`); nothing load-bearing rests on it.
3. **Theorem 7's constant `0.8908` is not claimed optimal**, and `8.30` is the most generous provable threshold constant, not a canonical one.
4. **Theorem 7 inherits Z-1/Z-2's scope** — shift-0 windows only (`statement.md:32-33`), which the official `Λ = {odd l ≤ t}` satisfies.
5. **Four catches are against our own bank or brief** (B1: `z1_ternary_mass/PROOFS.md:394`; B2: `PREREG.md:30`; B3: the node's route-(b) sizing at `statement.md:56-59`; B4: the round-15 gloss at `PREREG.md:20-23`). B3 is the one that changes a node statement's content and should reach the maintainer stack.

result: Route (b) is DEAD as posed — the node's "factor-2 headroom" is refuted (Weil is vacuous by exactly 26.000 bits once the degree factor is restored), and the only executable substitute lands on THEOREM Z-NOGO's own `p ≤ 8` threshold (gap 60.95 bits in log2 p); banked on the way out are the exact `1+cos` character form (machine-verified exactly, 137/137), two new favourable reductions (oddness ⇒ complete subgroup sums; AM-GM ⇒ first-moment in `V_1` only), the new unconditional bound `Z_1 ≤ 2^{0.8908·S}`, and four catches including one against the node statement itself.
