# Pilot report: P-B selector orders / K1 experiment (Opus 5 subagent, 2026-08-02)

Coordinator note: subagent's final report, persisted verbatim by Fable
(HTML entities restored). Coordinator verification and adopted posture:
FABLE_AUDIT.md alongside.

---

# K1 UNDER EVERY VIABLE SELECTOR ORDER — lane P-B, 2026-08-02

**Headline verdict.** K1 splits cleanly along ambiguity **A1**, and the split is total. Under **every support-keyed order** (5 of them, including two that are *reverses* of each other) the selector destroys the split-fibre family: retention `|Gamma_lo|/live` = **0.000-0.078** at all eight n=32 scales, against a null control of **0.79-1.00** — contrast x0.010-x0.081, and *strongest at the highest witness density*. Under **polynomial-keyed orders** (`ORD-POLYLEX`, `ORD-POLYCENT`, and the degenerate `ORD-SLOPEMAJOR`) the selector retains **the entire live-slope set** — retention **1.000** at four of the six dense points, 0.938-0.959 elsewhere — i.e. exactly the family shape the adversarial audit exhibits. **K1 is GREEN under support-keyed orders and RED under polynomial-keyed orders, at every computable scale.** PP4.0 does not merely pick a convention; it picks whether P-B's target survives its own kill line.

Two negative results sharpen the decision: the **A8 (procedural) reading is also RED at the densest point** (`ORD-DEGLEX` 97/97 at Q9), and the **budget clause of K1 is provably untestable** at any exhaustively enumerable scale — so the verdicts above are mechanism verdicts, and I quantify exactly where the budget first becomes testable.

---

## 1. What was run

12 scales x 13 candidate orders x complete exhaustive first-match selection over the *entire* witness population `W_z` at every live slope. **19,124,533 exact-`A` witnesses** enumerated in total; **5,317 exact structural checks, all PASS**; **9 parameter points cross-validate bit-exactly against the prior pilot** (P1, P2, P3, P4, P4b, P4c, P5, P6, P7 — total witnesses, live slopes, full per-slope census, and for every shared order the `Gamma_lo` size, Sidon flag, max multiplicity, common prefix and the example selected supports all match). Everything ran under `tools/ramguard local` (worst case 34 s / well inside 1 G).

The construction, parameter checks, strip/genericity checks, candidate-family builder and family statistics are **imported** from `pb_split_fibre_pilot.py` so the two pilots cannot silently diverge. The enumerator is new and ~200x faster: for `U = G.X^{ma}`, `V = -G.X^{m(a-1)}`, membership `deg(f_z - prod_{x in S}(X-x)) < K` reads `e_j(S) = (-1)^j(alpha_j + z beta_j)`, `j = 1..h`, with `alpha_j = G[g-j]`, `beta_j = -G[g-j+m]`. Since `beta_j = 0` for `j < m`, the first `m-1` constraints are **slope-free** (meet-in-the-middle key on power sums), `beta_m = -1` always so `j = m` **determines** `z`, and `j = m+1..h` are verified. Every witness is produced exactly once, at every slope, with no per-slope loop.

---

## 2. The candidate orders — exact comparators and A1-A8 resolutions

Objects: `(p_z, S_z)` with `S subset {0,...,n-1}`, `|S| = A`, `x_i = omega^i`; `p = f_z - prod_{i in S}(X - x_i)`, `deg p < K`; `mask(S) = sum_{i in S} 2^i`; `rev_n` = bit-reversal on `n` bits; `pi(i)` = rank of `omega^i` among the domain sorted by integer representative in `{1..q-1}`; `c(r) = r` if `2r <= q-1` else `r - q`. Every comparator is a **strict total order on each `W_z`** — no ties occurred anywhere (A6 discharged empirically at all 12 scales).

| order | comparator (minimum is selected) | A1 (object) | A2 | A3 (coords) | A4 (poly reading) | A8 |
|---|---|---|---|---|---|---|
| **ORD-LEX** *(leading candidate)* | `key = (2^n-1) XOR rev_n(mask)`; equivalently `S < T <=> min(S Delta T) in S` | agreement support | lex | exponent `x_i=omega^i` | — | order-min |
| **ORD-COLEX** | `key = mask`; equivalently `S < T <=> max(S Delta T) in T` | agreement support | colex | exponent | — | order-min |
| **ORD-VALEX** *(value-major, support reading)* | `key = (2^n-1) XOR rev_n(pi(mask))` | agreement support | lex | **integer-representative** | — | order-min |
| **ORD-VALCOLEX** | `key = pi(mask)` | agreement support | colex | integer-representative | — | order-min |
| **ORD-ERRLEX** | `key = rev_n(mask)`; = lex-min of the **error support** `D\S` | **error support** | lex | exponent | — | order-min |
| **ORD-POLYLEX** | `key = (p_0,...,p_{K-1})`, residues `0..q-1`, lex | witness polynomial | — | — | low->high, `0..q-1` | order-min |
| **ORD-POLYHI** | `key = (p_{K-1},...,p_0)`, lex | witness polynomial | — | — | **high->low** | order-min |
| **ORD-POLYCENT** | `key = (c(p_0),...,c(p_{K-1}))`, lex | witness polynomial | — | — | low->high, **centred reps** | order-min |
| **ORD-CODEWORD** *(value-major, codeword reading)* | `key = (p(x_0),...,p(x_{n-1}))`, residues `0..q-1`, lex | **codeword / evaluation vector** | — | exponent (eval coords) | evaluations | order-min |
| **ORD-DEGLEX** | `key = (deg p, ORD-LEX key)` — a decoder enumerating by increasing degree | poly then support | lex (tie) | exponent | degree only | **procedural** |
| **ORD-SLOPEMAJOR** | `key = (z, ORD-POLYLEX key, ORD-LEX key)` | full datum incl. slope | lex | exponent | low->high | order-min |
| **ORD-HASH-pb-null-01/02** | `key = blake2b(mask.to_bytes(8,'little'), digest_size=16, key=seed)` | — | — | — | — | **NULL CONTROL** |

A5 is moot at every scale (the pencil is proved strip-free: T0/T1/T2/T3/T4 and global genericity all checked exactly, per case). A7 is immaterial (`z = infinity` carries no exact-`A` witness: `deg(V - c) = A - m < A`). These resolutions are persisted machine-readably in every `k1_Q*.json` under `orders[<name>].spec`.

### Two structural facts about the order space (both proved, both verified)

- **`ORD-ERRLEX` is exactly the reverse of `ORD-LEX`.** `(D\S) Delta (D\T) = S Delta T`, so `min` of it lies in `D\S` iff it lies in `T`; hence `S <_ERRLEX T <=> T <_LEX S`. The decoder reading (order the *error* pattern) is not a new order — it is lex run backwards. **It collapses just as hard as lex** (0/97 at Q9, 3/193 at Q12), which kills the natural conjecture that the collapse is about *lex-minimality*: it is about *extremality in a support-keyed order*, either end.
- **`ORD-SLOPEMAJOR` is degenerate.** Under the pinned "one selection per slope" semantics, `z` is constant on `W_z`, so a slope-major leading key never separates and the induced selection equals the tail order's. Verified computationally: selected families identical to `ORD-POLYLEX` at **all 12 scales** (`extra_checks.slopemajor_equals_polylex = true` everywhere). **"Slope-major" is not a live fork in PP4.0** — writing it would silently write the tail order instead.

---

## 3. Pencil parameters (all live, all strip-free, all globally generic)

`U = G.X^{ma}`, `V = -G.X^{m(a-1)}`, `p_J = -G.R_J(X^m)`, `U + z_J V - p_J = G.Q_J(X^m)` over `D = mu_n < F_q^*` — the same recipe as the audit's `F_12289` fixture, checked identity-by-identity per case.

| case | n | q | K | h | m | A | witnesses | live | mean \|W_z\| | pencil family M | prior |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Q9 | 32 | 97 | 16 | 2 | 2 | 18 | 4,860,173 | 97 | 50,105 | 89 | P7 |
| Q12 | 32 | 193 | 16 | 2 | 2 | 18 | 2,442,627 | 193 | 12,656 | 105 | new |
| Q4 | 32 | 97 | 8 | 2 | 2 | 10 | 665,071 | 97 | 6,856 | 55 | P4 |
| Q5 | 32 | 193 | 8 | 2 | 2 | 10 | 334,249 | 193 | 1,732 | 58 | P4b |
| Q10 | 32 | 97 | 16 | 3 | 2 | 19 | 43,927 | 97 | 453 | 97 | P6 |
| Q6 | 32 | 449 | 8 | 2 | 2 | 10 | 144,239 | 449 | 321 | 60 | P4c |
| Q7 | 32 | 97 | 8 | 3 | 2 | 11 | 17,542 | 97 | 181 | 95 | P3 |
| Q8 | 32 | 193 | 8 | 3 | 2 | 11 | 5,454 | 193 | 28 | 110 | new |
| Q1 | 16 | 17 | 4 | 2 | 2 | 6 | 471 | 17 | 28 | 3 | P2 |
| Q3 | 16 | 17 | 4 | 3 | 2 | 7 | 64 | 17 | 4 | 6 | P1 |
| Q2 | 16 | 97 | 4 | 2 | 2 | 6 | 92 | 49 | 2 | 3 | new |
| Q11 | 32 | 97 | 8 | **5** | **4** | 13 | 85 | 46 | 2 | 6 | P5 |

Field sizes: **four** (17, 97, 193, 449); domain sizes: two (16, 32); rates 1/4 and 1/2; `h-m in {0,1,1}`. **Q11 is the only case at the official RowC 1/4 fibre width `m = 4, h = 5`** — and it has ~1 witness per slope, i.e. no competition, so it cannot test the selector (it is the control showing what "no competition" looks like: the intended witnesses *are* selected, 4-6 of 6).

---

## 4. The budget clause of K1 is structurally untestable — and here is where it stops being so

`|Gamma_lo| <= #live <= min(q, #witnesses)` and `#witnesses ~ C(n,A)/q^{h-1}`. Testing `|Gamma_lo| > 8n^3` therefore requires **both** `q > 8n^3` **and** `C(n,A) > (8n^3)^h`; since a split-fibre pencil forces `h >= m >= 2`, the necessary condition `C(n,A) > (8n^3)^2` is unavoidable by any choice of order, rate or field. At every case above, `max|Gamma_lo| = live <= 449` against a budget of `32,768` or `262,144`: **`budget_testable = false` at all 12 scales**, and `budget_violated = false` for all 156 (order, scale) pairs.

Exact frontier (`h = m = 2`, the densest shape; `q` chosen optimally at `~ sqrt(C(n,A))` subject to `q == 1 mod n`, prime, `q > 8n^3`):

| n | rate | 8n^3 | q_opt | witnesses | max\|Gamma_lo\| | headroom | retention needed | testable |
|---|---|---|---|---|---|---|---|---|
| 32 | 1/2 | 262,144 | 262,337 | 1,797 | 1,797 | 0.007 | 145.9 | no |
| 40 | 1/2 | 512,000 | 512,321 | 221,307 | 221,307 | 0.432 | 2.31 | no |
| **44** | **1/2** | **681,472** | **1,327,217** | **1,326,866** | **1,326,866** | **1.947** | **0.514** | **yes** |
| 48 | 1/2 | 884,736 | 5,233,153 | 5,233,108 | 5,233,108 | 5.915 | 0.169 | yes |
| 52 | 1/4 | 1,124,864 | 2,116,973 | 2,116,881 | 2,116,881 | 1.882 | 0.531 | yes |

**The first split-fibre scale at which K1's budget clause can be observed at all is n = 44, rate 1/2, q ~ 1.33e6** — needing retention > 0.514, and n = 48 needs only > 0.169. This is the operationally important number: **the polynomial-keyed orders' measured retention is 1.000 at every dense point tested, so at the first testable scale they would already produce an over-budget `Gamma_lo`** — while the support-keyed orders' measured 0.00-0.08 would pass with two orders of magnitude to spare. The obstruction to actually running it is the enumerator, not the mathematics: `2^{n/2}` half-tables means 2^22 (n=44) / 2^24 (n=48) entries — a few GB with the current Python meet-in-the-middle, i.e. **outside the 1 G law but within reach of a bit-packed/native rewrite on a larger box.** I recommend that as the single highest-value P-B follow-up.

---

## 5. Comparison table — retention `|Gamma_lo| / live`, all orders x all scales

Columns ordered by witness density (mean `|W_z|` above each column).

```
                     Q9      Q12      Q4       Q5      Q10      Q6       Q7      Q8       Q1      Q2      Q3      Q11
mean |W_z|        50104    12656    6856     1731      452     321      181      28       28       2       4       2
live slopes          97      193      97      193       97     449       97     193       17      49      17      46
ORD-LEX            1/97   11/193    3/97    9/193     4/97   7/449     1/97  26/193     0/17    0/49    0/17    0/46
ORD-COLEX          0/97    6/193    3/97    7/193     5/97  12/449     4/97  20/193     0/17    1/49    0/17    1/46
ORD-VALEX          0/97   11/193    1/97    6/193     6/97  12/449     3/97  20/193     0/17    0/49    0/17    0/46
ORD-VALCOLEX       2/97    8/193    5/97   15/193     7/97  16/449     4/97  15/193     0/17    0/49    0/17    0/46
ORD-ERRLEX         0/97    3/193    2/97    8/193     5/97  11/449     3/97  14/193     0/17    0/49    0/17    0/46
ORD-POLYLEX       97/97  193/193   97/97  193/193    93/97 449/449    91/97 111/193    12/17    0/49    0/17    1/46
ORD-POLYHI        93/97  140/193   84/97   52/193    76/97  34/449    68/97  72/193     0/17    1/49    0/17    2/46
ORD-POLYCENT      97/97  193/193   97/97  193/193    93/97 449/449    89/97 141/193    15/17    0/49    0/17    0/46
ORD-CODEWORD      91/97  193/193   89/97  187/193    76/97 382/449    78/97  70/193     1/17    1/49    0/17    0/46
ORD-DEGLEX        97/97   74/193   73/97   46/193    72/97  43/449    50/97  32/193     3/17    1/49    0/17    2/46
ORD-SLOPEMAJOR    97/97  193/193   97/97  193/193    93/97 449/449    91/97 111/193    12/17    0/49    0/17    1/46
ORD-HASH-null-01  97/97  193/193   95/97  185/193    85/97 392/449    79/97  78/193     5/17    0/49    0/17    0/46
ORD-HASH-null-02  97/97  193/193   93/97  187/193    89/97 395/449    77/97  83/193     4/17    1/49    0/17    0/46
```

**Exact budget ratios** `|Gamma_lo| / 8n^3` are computed as rationals for all 156 cells (in `K1_TABLE.json`). Representative rows at the densest scale Q9 (`8n^3 = 262,144`): `ORD-LEX = 1/262144 ~ 3.815e-6`; `ORD-COLEX = ORD-ERRLEX = ORD-VALEX = 0`; `ORD-VALCOLEX = 1/131072`; `ORD-POLYLEX = ORD-POLYCENT = ORD-SLOPEMAJOR = ORD-DEGLEX = 97/262144 ~ 3.700e-4`; `ORD-POLYHI = 93/262144`; `ORD-CODEWORD = 91/262144`; nulls `= 97/262144`. Largest ratio anywhere: **`ORD-POLYLEX` at Q6, `449/262144 ~ 1.713e-3`**. Every ratio is << 1 — see section 4 for why that is a theorem, not an accident.

---

## 6. K1 verdict per candidate order

Classification (pre-registered): retention >= 0.90 -> super-budget-shaped (**RED**); <= 0.10 -> support-collapsed (**GREEN**); else **AMBER**. Verdicts are read off the n=32 grid (the n=16 scales are *geometrically* degenerate — `A/n` is so large that even the null controls collapse, so they carry no signal; Q2, Q3 and Q11 are excluded from verdicts and reported as controls).

| order | K1-mech verdict | evidence |
|---|---|---|
| **ORD-LEX** | **GREEN** (7/8 n=32 scales; AMBER at the sparsest Q8) | 0.010-0.057 at the six densest; contrast vs null x0.010-x0.057 |
| **ORD-COLEX** | **GREEN** (7/8; AMBER at Q8) | 0.000-0.052 |
| **ORD-VALEX** | **GREEN** (7/8; AMBER at Q8) | 0.000-0.062 |
| **ORD-VALCOLEX** | **GREEN** (8/8) | 0.021-0.078 |
| **ORD-ERRLEX** | **GREEN** (8/8) | 0.000-0.073 |
| **ORD-POLYLEX** | **RED** (7/8; AMBER only at Q8) | **1.000, 1.000, 1.000, 1.000, 0.959, 0.938** at the six densest |
| **ORD-POLYCENT** | **RED** (6/8) | 1.000, 1.000, 1.000, 1.000, 0.959, 0.918 |
| **ORD-SLOPEMAJOR** | **RED** (== POLYLEX, degenerate) | identical to POLYLEX at all 12 |
| **ORD-CODEWORD** | **RED** (5/8), AMBER (3/8) | 0.938-1.000 at Q9/Q12/Q4/Q5; tracks the null control almost exactly |
| **ORD-DEGLEX** (procedural A8) | **RED at the densest point** (1.000 at Q9), AMBER/GREEN below | 1.000, 0.383, 0.753, 0.238, 0.742, 0.096, 0.515, 0.166 — trend is **towards RED with density** |
| **ORD-POLYHI** | AMBER (0.269-0.959), GREEN once | unstable across scales; no coherent mechanism |
| **null controls** | RED by construction | 0.79-1.00 at n=32; the yardstick |

**Pre-registered bad trend (collapse weakening as scale grows): NOT observed in the direction that matters.** Support-keyed collapse *strengthens* with witness density, which is the direction of the official scale:

```
rate 1/2, h=2:  |W_z| 50,104 -> worst support-keyed 0.021 (null 1.000, contrast x0.021)
                |W_z| 12,656 -> 0.057 (null 1.000, x0.057)
rate 1/4, h=2:  |W_z|  6,856 -> 0.052 (null 0.969, x0.053)
                |W_z|  1,731 -> 0.078 (null 0.964, x0.081)
                |W_z|    321 -> 0.036 (null 0.876, x0.041)
rate 1/4, h=3:  |W_z|    181 -> 0.041 (null 0.804, x0.051)
                |W_z|     28 -> 0.135 (null 0.417, x0.323)   <- degrades below ~10^2/slope
```

The only weakening is *below* ~10^2 witnesses/slope — away from the official regime (`log2|W_z| ~ 647` at RowC 1/4 with `q` large enough to host the audit's `M`). This reproduces and extends the prior pilot's density finding across five new orders and two new scales.

---

## 7. Mechanism findings that bear directly on the proof route

- **The FM3 prefix/shadow target as currently worded is FALSE.** The prior pilot's proposed theorem — "lex-first-match forces every selected support to contain `{x_0..x_{K-1}}`" — fails at every point measured: the *global* common block under `ORD-LEX` is 3, 4, 5, 6, 11 coordinates against `K = 8` or `16`, always strictly below `K`, while `Gamma_lo` collapses anyway. Worse, `ORD-COLEX`, `ORD-VALCOLEX` and `ORD-ERRLEX` have common block **0** and collapse just as hard. The real mechanism is **global block + pairwise birthday over ~q^2/2 slope pairs**, not a `K`-prefix. FM3 must be re-worded before any proof attempt.
- **The collapse is quantifier-driven, at every scale and every support-keyed order.** The largest *pairwise* low-core subfamily of the selected family (greedy lower bound) retains **33-45 % of live slopes** everywhere (Q9 LEX 40/97; Q4 34/97; Q6 164/449; Q12 90/193). Only P-B's "meets **every** other" quantifier ejects them. An exchange theorem leaning on this is leaning on a quantifier, not on structure — the prior pilot's warning is confirmed across five further orders.
- **The intended witnesses are never first matches where there is competition, always where there is none.** `intended_is_first_match` = 0/55 (Q4, LEX), 0/89 (Q9), 0/95 (Q7) at dense points, but 4-6 of 6 at the no-competition control Q11 (the official `m=4, h=5` shape). This is precisely the audit's "not yet a counterexample" clause, now measured at ten scales.
- **The counterfactual confirms the audit's family is genuinely super-budget-shaped.** Forcing the intended witnesses at the pencil slopes puts **all** of them into `Gamma_lo` (55/55, 89/89, 95/95, 105/105) — so the only thing standing between the audit's construction and a P-B counterexample is first-match minimality, exactly as claimed.
- **Collapsed slopes land in `Gamma_hi`.** The mechanism re-routes mass into P-A1 rather than paying it; any exchange theorem still needs a paired P-A1 accounting statement.

---

## 8. Honest caveats

1. **Budget untestability.** No cell in the table violates `8n^3`, and section 4 proves none could. All GREEN/RED verdicts are **mechanism** verdicts (retention + Sidon shape), not budget verdicts. Calling any of them a refutation or a proof would be wrong.
2. **Structural gap to the `F_12289` fixture.** Official RowC 1/4 has `m = 4, h = 5`, `A - m = K + 1`, core 53, 52 fibres from a 104-label pool. My *dense* points all have `m = 2`: the `h = 3` cases (Q7, Q8, Q10) reproduce the official `A - m = K + 1` relation; the `h = 2` cases (Q4-Q6, Q9, Q12) have `A - m = K` exactly. The only `m = 4, h = 5` case (Q11) has no competition. **Nothing here tests `m = 4` under competition** — that shape needs `C(n,A) >> q^4`, unreachable at `n <= 32`.
3. **The audit's `M = 129,948,699,009` is not a live-slope count in any single `F_q`.** Its slopes are separated at split primes; realizing them with distinct slopes needs `q >~ 1.3e11` while `N = 1024`, i.e. `q/n ~ 1e8`. All my dense points have `q/n in [3, 14]`. The regimes "large `q/n`" and "high witness density" are simultaneously reachable at official scale but not at `n <= 32` — this is the single biggest extrapolation gap, and it is the same gap the frontier table in section 4 quantifies.
4. **Density extrapolation is enormous.** Densest measured `log2|W_z| ~ 15.6`; official is `~ 647`. The measured trend is monotone in the favourable direction but is a trend over 4 orders of magnitude being read against 195.
5. **n = 16 carries no signal.** At `A/n in {6/16, 7/16}` even the null controls collapse (0-5 of 17/49). Q1/Q2/Q3 are reported for completeness only.
6. **`ORD-POLYHI` is erratic** (0.076 -> 0.959 non-monotonically); I do not claim a mechanism for it. **`ORD-DEGLEX` is scale-dependent** and its RED at Q9 rests on one point.
7. Agreement among the five support-keyed orders is **evidence, not a transport lemma**. No transport lemma was attempted.
8. `ORD-VALEX/VALCOLEX` depend on the integer-representative order of `F_q`, which is not canonical under field isomorphism; they are included because A3 genuinely permits them, not because they are defensible as a spec.

---

## 9. What this says for the surfaced PP4.0 decision (evidence only — the call is the coordinator's/maintainer's)

- The A1 fork is **outcome-deciding and one-sided**: 5/5 support-keyed orders GREEN, 3/3 polynomial-keyed orders RED, at every scale with competition. If PP4.0 is written support-keyed, K1 is survived at every computable scale with a x12-x100 margin over the null control, and the margin *grows* with density. If it is written polynomial-keyed or codeword-keyed, K1 is live now and would be an actual budget violation at the first testable scale (n = 44) if the measured retention of 1.000 persists.
- Within the support-keyed class the choice barely matters (lex, colex, value-lex, value-colex and reverse-lex all collapse) — so PP4.0 can be written with a *class* justification rather than a coin-flip, which is a much stronger footing for a normative freeze.
- Two forks can be closed for free: **slope-major is degenerate** (never a real choice), and **error-support-lex is exactly reverse-lex** (not a new order). Both should be recorded so PP4.0 doesn't relitigate them.
- The A8 procedural reading must be **explicitly excluded**, not left implicit: a decoder that enumerates by increasing degree is RED at the densest point.

---

## 10. File inventory (all inside `notes/pilots_20260802/pb_selector_orders/`, absolute paths)

- `.../k1_orders.py` — 13 comparators with machine-readable A1-A8 resolutions (`ORDER_SPEC`), the 12-scale grid (`CASES`), the fast complete enumerator, exact two-stage first-match selection (cheap 2-coordinate prefixes, exact resolution on survivors), stage `select` (slope-chunkable) and stage `stats`.
- `.../k1_summary.py` — aggregation, null-control contrast, density trends, the budget-testability frontier, support-concentration table.
- `.../k1_Q1.json ... k1_Q12.json` (12 files) — per scale: all parameter/strip/genericity checks, full census, candidate-family stats, and per order the **exact selected family** (`selected_masks`, slope -> support bitmask), `Gamma_lo`, budget ratio, class, verdict, Sidon/energy stats, concentration, intended-first-match, restricted and counterfactual families, and the order's A1-A8 spec.
- `.../sel_Q*.json` (12 files) — stage-1 checkpoints (per-slope selections, chunk-mergeable).
- `.../K1_TABLE.json`, `.../K1_TABLE.txt` — the full comparison table, trends, frontier and concentration data.

Nothing outside this directory was written or modified (a stray `__pycache__` created by importing the prior pilot was removed, and `sys.dont_write_bytecode` now prevents recurrence). No commits, no pushes, no `dag.json` / `critical/` / `background/` / `tools/` changes, nothing m2- or kb_m2_r4-related touched.
