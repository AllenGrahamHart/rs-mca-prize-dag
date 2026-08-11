# PREREG — r34_pstar (round 34)

Coordinator brief. Constraints: CONSTRAINTS.md in this dir (binding).
AUDIT-AND-DRAFT: any surgery stays coordinator-gated.

## Anchors (read these two FIRST, then register blind priors)

1. `notes/pilots_20260811/rh_moving_kernel/REPORT.md` (round 33)
2. `background/nodes/rate_half_ca_hankel_split_pencil_equivalence/statement.md`

## Mandate

THE CHEAPEST DECISIVE FAR-CA QUESTION (round 33's R-PSTAR). The
far-CA deep stratum's structure now turns on one invariant: p*, the
minimal common apolar degree of the pencil space V = <Phi_0,Phi_1>.
Generically p* = floor((2R-1)/3)+1 ~ 2R/3. The FG stratum (where a
fixed generator exists, and where the scaled-Vandermonde normal
form + key equation live) requires p* <= 2rho; the honest
fixed-generator mechanism needs p* + p_gen <= R i.e. p* <= R/2
(misses generically by 7/6). THE QUESTION: does ANY column-far
pencil at razor-shaped parameters have p* <= R/2 (equivalently:
is FG nonempty among column-far pencils in the wide regime)? IF NO:
FG is empty at the razor, the whole fixed-generator branch closes
NEGATIVELY, and R-KER becomes the SOLE far-CA residual — a major
structural simplification. IF YES: the FG key equation gets its
first live instances and R-FG becomes a real budget question.

## Deliverables

**D1 — THE p*-vs-COLUMN-FARNESS STRUCTURE.** Low p* means V lies in
the inverse system of a degree-p* form: V ⊂ Ann(P*)^perp — i.e.
both syndromes are linear combinations of powers of P*'s roots
(generalized: the apolarity/Waring structure). Column-farness says
K_0 = Ann(V)_r contains no D-split element. Derive the exact
tension: for p* <= R/2, K_0 = P* · F[x]_{r-p*} (round 33's FG2:
column-far <=> P* not D-split-squarefree). So FG-membership at
p* <= R/2 just needs P* squarefree-non-D-split AND the syndromes
genuinely in the inverse system — CONSTRUCT directly (round 33's
FG pencils were constructed this way at small scale — quote and
extend). The REAL question is whether such pencils exist AT THE
RAZOR SHAPE (r/R = 1 - 2^-6, rho = R - r): check the dimension
arithmetic exactly — dim of the low-p* pencil locus vs the
column-far conditions.

**D2 — THE CENSUS.** At wide-regime cells (round 33's e1 cells +
razor-shaped ratios as feasible): the p* spectrum of column-far
pencils (exhaustive where cheap, constructed families otherwise).
Does p* <= R/2 occur? With what codimension?

**D3 — THE RAZOR VERDICT, exact arithmetic.** The locus
{p* <= R/2} has codimension ~(something)(p*-dependent) in pencil
space; column-farness is one condition per D-split candidate.
Derive whether the intersection is empty/nonempty at razor
parameters BY DIMENSION COUNT (with the naive-count caveat quoted —
round 33 bank 3's MISS 5 precedent), and if constructible, exhibit.

**D4 — VERDICT.** FG empty (R-KER sole residual) / FG nonempty
(R-FG live with witnesses) / undecided-with-named-gap. Misses
first; LB1-consistency check (LB1 pencils have dim K_0 = 0 — where
do they sit in the p* spectrum? predict then measure).

## Blind priors to register

P(FG nonempty at razor shape), P(p* <= R/2 occurs at any wide
census cell), expected codimension of the low-p* locus, P(the
dimension count is decisive either way).

## Pilot registrations

Registered after reading ONLY the two named anchors
(`rh_moving_kernel/REPORT.md`, `..._split_pencil_equivalence/statement.md`)
and CONSTRAINTS.md, and BEFORE any grep, any `ls`, any other file read,
and any interpreter invocation. Nothing below is edited afterwards.

**Honesty note on "blind".** I did an in-head parameter count and sketched
a candidate construction *after* reading the anchors and *before* writing
this block. I therefore register TWO numbers where they differ: `gut` =
belief on reading the brief, `post-count` = belief after the in-head
arithmetic. Only `post-count` is my operative prior; `gut` is recorded so
the round can be scored honestly and so a later refutation lands on the
right number.

### R0 — headline priors

- **R0-a. P(FG nonempty at razor shape).** gut **0.55**; post-count
  **0.93**. Mechanism I expect to work: pick `P*` of degree
  `p ∈ (rho, 2rho]` that is NOT `D`-split-squarefree; take `V` a 2-dim
  subspace of the `p`-dimensional truncated inverse system `IS(P*)`;
  then `K_0 = P*·F[x]_{<=r-p}` and column-farness is FREE by round 33's
  own FG2 equivalence.
- **R0-b. P(`p* <= R/2` occurs at some wide census cell).** By
  CONSTRUCTION **0.95**. By RANDOM SAMPLING at a wide cell **0.10**
  (codimension too large at reachable `q`). These are different
  questions and I score them separately.
- **R0-c. Expected codimension of the low-`p*` locus.** I commit to the
  EXACT formula
  `dim{p* <= p} = 3p-4` inside `Gr(2,R)` of dimension `2R-4`, hence
  **`codim{p* <= p} = 2R - 3p`**
  (`p` projective parameters for `P*`, plus `dim Gr(2,p) = 2(p-2)`).
  Sanity anchors it must reproduce: `codim = 0` at `p = ceil(2R/3)`
  (round 33's generic `p*`), and `codim = R/2` at `p = R/2`.
  **Falsifier:** at cells where the predicted codim is 1 or 2, measured
  `-log_q(frequency of p* <= p)` must lie within **±0.5** of `2R-3p`.
- **R0-d. P(the dimension count is decisive either way).** **0.35.** I
  expect the verdict to come from an explicit CONSTRUCTION, with the
  count only corroborating. A naive count is exactly the thing round 33
  flags (its zero-power #4), and it can fail three ways: no `F_q`-points
  on a positive-dimensional locus, non-transverse intersection with
  column-farness, and a reducible/over-counted parameterisation. A
  witness is immune to all three, so I pre-commit to answering by
  witness and using the count only for "how thin".
- **R0-e. P(the brief's "equivalently" is WRONG).** **0.85.** The brief
  equates "`p* <= R/2`" with "FG nonempty". I predict these are
  different conditions: FG (i.e. `K_0 = P*·F[x]`, i.e. `h_r = p*`)
  needs **`p* <= 2rho`**, which at the razor is `p* <= R/32` — a factor
  **16** stronger than `p* <= R/2`. So FG ⟹ `p* <= R/2` but not
  conversely, and there should be a whole intermediate stratum
  `2rho < p* <= R/2` with a FIXED generator but a NON-principal `K_0`,
  invisible at every round-33 cell because those all have
  `2rho >= ceil(R/2)`.
- **R0-f. LB1 consistency (predict-then-measure).** `dim K_0 = 0` ⟺
  `Ann(V)_r = 0` ⟺ **`p* > r`**, a tautology, so LB1 pencils sit at the
  TOP of the `p*` spectrum, opposite FG. Sharper prediction: at LB1's
  cell `(7,2,4,q=11)` (`R=5, r=3`) the measured `p*` is **exactly
  `r+1 = 4`** for **>= 90%** of `dim K_0 = 0` pencils, and `4` is also
  `ceil(2R/3) = 4`, so LB1 is *generic*, not special. Falsified if
  `p* > r+1` occurs in more than 10% of them.
- **R0-g. Generic `p*`.** `p* = ceil(2R/3) = floor((2R-1)/3)+1` is the
  modal value at **every** wide census cell, in **>= 90%** of uniform
  random pencils, at two independent fields.
- **R0-h. Nondegeneracy of the constructed FG family.** I predict the
  construction is NOT trivially bad-slope-free: at small scale at least
  one constructed column-far FG pencil has bad-slope count `T > 0`
  (window: `T > 0` for `>= 1` of the constructed pencils; I also expect
  the round-33 saturation `T = q` to recur at reachable cells and I
  declare zero power for it at the razor).

### R0-i — exact razor integers I commit to in advance

`R = 2^40`, `rho = 2^34`, `r = R-rho`, `n = 2R = 2^41`.

| quantity | committed value |
|---|---|
| `2rho` (top of the FG bracket) | `34,359,738,368` |
| `R/2` (lemma bracket) | `549,755,813,888` |
| generic `p* = ceil(2R/3)` | `733,007,751,851` |
| `dim K_0` on FG at `p = 2rho` | `1,047,972,020,225` |
| `codim{p* <= R/2} = 2R-3p` | `549,755,813,888` |
| `codim{p* <= 2rho} = 61·2^35` | `2,095,944,040,448` |
| `m_Q = p-rho` at `p = 2rho` | `17,179,869,184` |

Any of these off by even 1 is a registered MISS.

### MISS-2 GUARD (mean-vs-max), pre-registered

Round 33's MISS 2 was a numeric-window miss; the structural analogue I am
exposed to this round is **mean-vs-max**, so I guard it explicitly:

1. The census (D2) measures a **distribution** of `p*` over sampled
   pencils. The mandate (D3/D4) asks an **existence / minimum** question:
   is `min p*` over the column-far locus `<= R/2`? A sampled census has
   **ZERO power** to answer that, in either direction, and I pre-commit
   to never inferring "no column-far pencil has `p* <= R/2`" from any
   observed frequency, however many samples.
2. Symmetrically I will not report a modal or mean `p*` in a sentence
   that a reader could take as bounding `min p*`. Every `p*` number is
   labelled `modal` / `mean` / `min-over-sample` / `constructed`.
3. `T` (bad slopes) is reported as a **max over the sample**, never a
   mean, when used against a candidate bound; and as a distribution when
   descriptive. Round 33's `T = q` is a saturation artefact with zero
   razor power and I inherit that declaration.
4. The codimension in R0-c is an expectation over the ambient
   Grassmannian; it bounds **density**, never **emptiness**. A
   codimension of `2^39` is fully compatible with a locus of
   `q^{3p-4} ≈ 2^{4·10^12}` points. I pre-commit to stating this
   whenever a codimension number appears near an existence claim.

### Zero-power declarations (pre-registered)

1. **No razor-scale computation exists or will be attempted.** Every
   razor claim is closed-form construction plus exact integer
   arithmetic. Machine evidence lives only at small cells.
2. **Every round-33 cell has `2rho >= ceil(R/2)`** — I predict this and,
   if true, those cells have **zero power** to separate FG from the
   `p* <= R/2` lemma condition. I will build cells with `4rho < R`
   (i.e. `r > 3R/4`) specifically to separate them.
3. **The naive dimension count is naive** (round 33 zero-power #4
   precedent). Wherever a count is decisive I state it as a count, and
   I do not let it carry an existence verdict on its own.
4. **No claim about `char F`, about `q` at razor scale beyond `q >= n`,
   or about non-squarefree `P*` inside round 33's FG3/FG4** — those
   assume `P*` squarefree and I will keep a squarefree witness separate
   from any non-squarefree one.
5. **Two-field confirmation** (`q = 11, 13` at least) required before
   any structural claim is stated as measured.

### Compute plan

Stdlib-only Python, every invocation
`tools/ramguard tiny -- python3 ...` (256M/60s) or
`tools/ramguard local -- python3 ...` (1G/5min), from the repo root,
with a literal `--` and `RAMGUARD_TIMEOUT` documented per use. No bare
`python3` for any purpose, including patching and probes; all file edits
go through Edit/Write. Results checkpointed to `e*_results.txt` in this
directory after every emit. `dag.json` never opened. Planned runs:
`e1` (`p*` spectrum census + codim calibration), `e2` (explicit FG
witness families + bad-slope counts, incl. cells with `4rho < R`),
`e3` (exact razor arithmetic), `e4` (LB1 `p*` measurement).
