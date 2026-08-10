# PREREG — maxscan_algorithm (round 28)

Coordinator brief, written before dispatch. The pilot appends its own
registrations BELOW the brief BEFORE any computation.

## Mandate

THE ONE UNDETERMINED NUMBER on RH-AC's supply side: the scaling of
the arbitrary-word maximum. Round 27's nonpoly_flank_census left it
honestly conflicted — the delta=1 mechanism's model collapses at
prize scale (2^-500), but the maximal-slack surplus GREW over the
two measured scales (+0.74 -> +0.94/1.25 bits) — and named the
deciding computation: the EXACT n=32, t=1 whole-word-space maxscan,
priced at C(32,15) ~ 5.7e8 subset-evaluations per word class,
"Modal-class, out of stdlib reach." ROUND 25'S LESSON IS YOUR
MANDATE: the z_n32_band pilot broke an "out of reach at 1G by any
kappa" wall with an ALGORITHM (BBM: contiguous residue buckets +
bisect — memory drop at no time cost). Try to break this wall the
same way BEFORE any compute is rented. Read first:
notes/pilots_20260809/nonpoly_flank_census/{REPORT.md,
FABLE_AUDIT.md, scratch/nf_maxscan.py}; the window-shift reduction
(the flank is the width-t window [delta+1, delta+t] — a LINEAR
structure that may be exploitable algorithmically); the
antipodal-pair-locator maximizer (its exact count profile at n=16:
16 members at agreement 9, 3 at 10).

## Deliverables

**D1 — THE ALGORITHM DESIGN (registered before implementation).**
Candidate routes to price (register your own list; these are
starters, not bounds): (a) the window-shift linear-algebra route —
the admissible set at (W, delta) is an affine subspace; counting
codewords at agreement >= a in an affine subspace of locator space
may reduce to rank/kernel computations per subset CLASS rather than
per subset; (b) the closed-form route — prove the
antipodal-pair-locator family's count exactly (its profile looks
structured) and prove it is the maximizer class, replacing
enumeration by a formula plus a bounded exceptional search; (c) the
meet-in-the-middle route — split the 32 evaluation points 16/16 and
join agreement counts (the BBM shape); (d) orbit quotients — the
scan at n=16 already deduplicates by a group; how far does the
symmetry cut n=32? Price each route in operations and RAM under
the 1G wall BEFORE building.

**D2 — THE VALIDATION LADDER.** Whatever you build must reproduce
the banked ground truth EXACTLY: the n=16 two-field maxima
(MAX_F_SUBSET = 46 at q=10177 AND q=10193, argmax at W1=0), the
n=8 exhaustive stratum data, and the delta=0 plateau at matched
cells. Run the ladder BEFORE the target scale.

**D3 — THE TARGET.** If the wall breaks: the exact n=32, t=1
whole-word-space maxscan at two independent fields (the round-27
two-field standard), and THE VERDICT: does the arbitrary-word
maximum grow toward the 4.83-bit razor need or collapse with the
delta=1 model? Register outcome thresholds in advance (what
measured max at n=32 counts as "grows", what as "collapses", what
as undetermined-still). If the wall does NOT break: validate the
best algorithm at the largest reachable n (register the honest
reachable point from your D1 pricing), and EMIT THE PRICED MODAL
REQUEST as a draft entry for notes/compute_requests (the exact
app design, sharding, fail-closed manifest plan, expected cost —
the Codex Modal-app pattern from the K3 campaign is the template),
written into your own dir for the coordinator to file.

**D4 — THE CLOSED-FORM BONUS (if budget remains).** The
antipodal-pair-locator count profile: prove it. A proved maximizer
family with a closed form would decide the scaling question at
EVERY n at once — strictly stronger than any single maxscan.

## Escape tests (before the main work)

- Replay nf_maxscan.py at n=8 (SCRATCH COPY) — exact match to the
  banked s2_maxscan_n8.json.
- Reproduce the n=16 argmax cell's count profile (46/19, {9:16,
  10:3}) from the banked machinery.

## Rules (binding)

- QUARANTINE: do not read notes/pilots_20260802/CAMPAIGN_LEDGER.md
  at or below line 4302; do not read the other round-28 pilot dirs
  (apolar_origin, ssparse_endpoints, mca_safe_rewire). Pass this
  clause to any subagent verbatim.
- COMPUTE LAW: every interpreter run via
  `tools/ramguard tiny|local -- python3 ...` from the repo root —
  including file patching and JSON peeking. RAMGUARD_TIMEOUT
  documented per use.
- BANKED SCRIPTS FROM SCRATCH COPIES ONLY.
- RAM DISCIPLINE: file-at-a-time reads; never open dag.json; no
  bulk loads; checkpoint everything; background batches with
  results files for >10-min runs. The 1G ceiling is the wall you
  are trying to beat BY DESIGN, not by relaxation.
- DRAFT-ONLY: writes only in
  notes/pilots_20260810/maxscan_algorithm/; no dag/nodes/tools
  writes; no git; NO MODAL (you design the request; the
  coordinator files and runs it); stdlib only.
- Register predictions with numeric windows BEFORE computing;
  misses first. Name every measured functional (CATCH-19C).
  Two-field confirmation for any structural claim (the round-27
  standard). Own-repo grep before claiming anything is missing
  (CATCH-24A).
- Your final message IS the report. End with a compliance
  paragraph.

## Pilot registrations (appended by the pilot before any computation)

Pilot: maxscan_algorithm (Opus), round 28, 2026-08-10. Everything below
was written BEFORE any interpreter was invoked. Inputs read first (file
reads only, no computation): round-27 `REPORT.md`, `FABLE_AUDIT.md`,
`scratch/nf_maxscan.py`, and the three banked maxscan JSONs
(`data/s2_maxscan_n8.json`, `s2_maxscan_n16.json`,
`s2_maxscan_n16_q2.json`).

### R0 — the object, restated exactly (so the price is honest)

Complement form (banked, `nf_maxscan.py`): t=1, δ=1, n even, k=n/2,
B ⊂ D=μ_n with |B| = k−1 = m. Writing e1(B), e2(B) for the elementary
symmetric functions of B, the admissibility condition is the LINE

  e2(B) − W1·e1(B) + W2 = 0   in the (W1,W2) plane.

So with α := −W1, β := W2:

  **F_SUBSET(n,q,α,β) := #{B ⊂ μ_n, |B| = n/2−1 : e2(B) + α·e1(B) + β = 0}**
  **MAXSCAN(n,q) := max over (α,β) ∈ F_q² of F_SUBSET**   [the target]
  **MAXSCAN_0(n,q) := max over β of F_SUBSET(n,q,0,β)**   [the α=0 slice]
  **TAIL_0(n,q,τ) := #{β : F_SUBSET(n,q,0,β) ≥ τ}**       [background meter]
  **STRAT_s(n,q,α,β) := the |S|=s part of F_SUBSET** (S defined in R3)
  **PLATEAU(n) := C(n/2−1, n/4)**  (3, 35, 6435 at n=8,16,32)
  **RATIO(n) := MAXSCAN(n)/PLATEAU(n)**, **SURPLUS(n) := log2 RATIO(n)**

Banked ground truth I must reproduce: MAXSCAN(8,10009)=6 at (W1,W2)=(0,1);
MAXSCAN(16,10177)=46 at (0,6891); MAXSCAN(16,10193)=46 at (0,4729).
N := C(32,15) = 565,722,720.

Signal-separation constraint (this is what prices q, and the banked runs
never had to state it): the mean per word class is μ = N/q, and a heavy
line is only readable if μ ≪ the target. At n=16 the banked runs used
μ≈1.12 because the target was 46. At n=32 the comparator is 6435, so μ up
to ~20 is harmless — **q ≈ 3·10⁷ suffices, q ≈ N is not needed.** This is
the first half of the break.

### D1 — routes priced BEFORE building (ops, RAM, verdict)

| route | time (n=32) | RAM | verdict |
|---|---|---|---|
| **R0** banked `nf_maxscan` as-is: loop α∈F_q, hash N values | q·N ≥ 5.7·10¹³ (q≥10⁵ forced by signal separation) | two length-N int arrays ≈ 9 GB (45 GB as lists) | dead on BOTH axes |
| **R1** 2-D histogram G[e1][e2], then scan lines | N + q³; balanced at q≈N^{1/3}=827 but then mean line weight N/q = 6.8·10⁵ swamps a 6435 signal; separation forces q≳10⁵ ⇒ q³ ≥ 10¹⁵ | q² counters | dead (the balance point and the signal window are disjoint) |
| **R2** meet-in-the-middle, 16 antipodal pairs split 8/8 (4⁸ × 4⁸) | join is per-(p1L,p1R) class because the coupling 2·p1L·p1R is bilinear ⇒ total join work is exactly N; no asymptotic gain | 65536 half-states | fixes RAM only; subsumed by R3 |
| **R3 (CHOSEN)** stratified antipodal enumeration + dense small-q counter | N inner increments per α; **N/2 at α=0** by the σ→−σ symmetry ⇒ ≈2.8·10⁸ steps | one `array('H')` of length q = 60 MB at q=3·10⁷, plus O(2^s) scratch | **RAM wall broken (9 GB → 60 MB); per-α time 2–10 min** |
| **R4** α-restriction by symmetry + char-0 identification | (#α scanned) × N | as R3 | the residual wall: q/(n·φ(n)) ≈ 5.9·10⁴ orbits × N = 3.3·10¹³ — **NOT broken** |
| **R5** orbit quotient alone | rotation (α,β)→(ζα,ζ²β) and Galois give ≤ n·φ(n) = 512 at n=32 | — | factor 512 only; insufficient alone |

**R3, the identity it runs on.** Pair up antipodes: μ_n = ⊔_{j<M} {ζ^j,−ζ^j},
M = n/2, ω := ζ². A subset B is (S,σ,T): S = pairs meeting B once (sign
σ_j = ±1), T = pairs contained in B, |S| + 2|T| = m. Then with
P := Σ_{j∈S} σ_j ζ^j, ω_X := Σ_{j∈X} ω^j:

  **e1(B) = P,  e2(B) = (P² − ω_S − 2ω_T)/2.**

(Direct check: cross terms between two doubled pairs and between a doubled
pair and anything else vanish, since ζ^j + (−ζ^j) = 0.) Enumeration order:
s (odd) → S → precompute the ω_T list once per S → σ → inner loop over the
ω_T list. At α=0, e2 depends on σ only through P², so σ and −σ give the
same fiber: enumerate 2^{s−1} sign patterns and weight 2.

**Honest statement of what R3 does and does not break.** It breaks the RAM
wall outright and makes ONE direction α exact at n=32 for the first time.
It does not break the α-count. So the reachable exact object is the α=0
slice plus a registered finite α-list — not the full q² word space. I
register that asymmetry now: **a lower bound suffices to prove GROWS; only
an upper bound proves COLLAPSES.** If the α=0 slice at n=32 exceeds the
plateau the verdict is proved; if it does not, the collapse verdict is
conditional on the argmax-at-α=0 law and the Modal request is emitted.

**Why α=0 is the right slice (2 scales, 2 fields, already banked).**
α=0 is the unique fixed point of the rotation action (α,β)↦(ζα,ζ²β), and
the banked per-W1 histograms show every other level occurring in exact
multiples of n (n=16: 46 at 1 α; 39 and 36 at 16 each; 26 at 64; …), i.e.
free rotation orbits off α=0. The banked argmax is W1=0 at n=8 AND n=16,
in both n=16 fields.

### D2 — the validation ladder (run in this order, before the target)

- **L0** replay `nf_maxscan.py` (scratch copy, unmodified) at n=8, q=10009.
- **L1** same at n=16, q=10177 and q=10193.
- **L2** my R3 enumerator must reproduce MAXSCAN_0 **and its argmax field
  element** at n=8 and n=16 in both fields (an exact F_q element match, not
  just the count), and must reproduce a sample of the banked per-W1
  histogram at α≠0 via its general-α path.
- **L3** the n=32 target.

### Predictions (numeric windows, misses reported first)

- **P1** (L0, tol 0): 6 / W1=0 / W2=1 / histogram {1:9504, 2:472, 5:8, 6:25}.
- **P2** (L1, tol 0): 46 / 0 / 6891 at q=10177; 46 / 0 / 4729 at q=10193.
- **P3** (L2, tol 0): my enumerator returns exactly those counts AND those
  argmax field elements at n=8 and n=16.
- **P4 — the closed form for the antipodal-pair-locator (|S|=1) family.**
  I claim, derived before computing, that the s=1 stratum's maximum
  single-fiber count is, for n = 2M with M a power of two and h := M/2 − 1:

    **STRAT_1^max(n) = 2(M−h)·C(M/2−1, (h−1)/2) = (M+2)·C(M/2−1, M/4−1).**

  Derivation: for s=1, e2 = −ω_T, so the fiber count is
  Σ_{j0∈[M]} 2·#{T ⊄∋ j0, |T|=h, ω_T = τ} = 2(M·A − h·A) = 2A(M−h) where A
  is the unrestricted prescribed-sum multiplicity, whose max over τ is
  C(M/2−1,(h−1)/2) by the banked P4 prescribed-sum theorem (h is odd here,
  so the support size s′ must be odd and s′=1 is optimal).
  Values: **n=8 → 6, n=16 → 30, n=32 → 630, n=64 → 218790.**
  Note this CORRECTS the banked round-27 model n·C(n/4−1,n/8−1) (= 48 at
  n=16), which omits the S∩T=∅ exclusion and overcounts by 2M/(M+2).
  Tolerance 0 at all three n.
- **P5 — the target, MAXSCAN_0(32).** Point estimate **1500**; registered
  window **[630, 4000]**. Trichotomy on R32 := MAXSCAN_0(32,q)/6435:
  * **GROWS** if R32 ≥ 1.314 (i.e. ≥ 8456 — the surplus is not shrinking
    relative to RATIO(16) = 46/35 = 1.314);
  * **SURVIVES-BUT-SHRINKS** if 1 ≤ R32 < 1.314 (6435 … 8455);
  * **COLLAPSES** if R32 < 1 (< 6435) — the δ=1 flank maximum has fallen
    below the slack-0 plateau by n=32 and the δ=1 mechanism cannot
    contribute to the 4.83-bit razor need.
  I predict COLLAPSES.
- **P6** (background meter): at q ≈ 3·10⁷ (μ ≈ 18.9) the largest non-structural
  fiber count at n=32, α=0 lands in **[35, 70]**; TAIL_0(32,q,100) is a
  small structured set, not a Poisson tail.
- **P7** (heavy-α family, n=16): the α with slice-max ≥ 20 number ≤ 800
  (≤ 50 rotation orbits), and ≥ 60% of them are reductions of cyclotomic
  integers of height ≤ 2 with ≤ 3 terms in the power basis (allowing a
  denominator of 2).
- **P8** (two-field): |MAXSCAN_0(32,q1) − MAXSCAN_0(32,q2)| ≤ 60 for the two
  registered fields, and the top fiber's structural description agrees.
- **P9** (honest reachable point if R4 stands): the largest n at which the
  FULL (α,β) scan is stdlib-reachable is **n = 16** (q·N = 1.2·10⁸); at
  n = 32 only finite α-lists are reachable. Registered in advance so the
  fallback is not retro-fitted.

### Late registration — P10, n=64 (appended 08:49, while the n=64 job runs and BEFORE it returns any value)

The parity theorem proved mid-run (only S inside one parity class of pairs
contributes at antipodal targets ⇒ stratum ceiling s ≤ n/4) reduces the
antipodal-target count to (3^{n/4} − 1)/2 nodes, which puts **n=64** inside
stdlib reach for the first time. Registered before the answer:
- **P10a** ANTIPODAL(64) ∈ [10⁶, 5·10⁷]; RATIO(64) = ANTIPODAL(64)/300540195
  < 0.1 (i.e. the collapse continues and deepens).
- **P10b** STRAT_1(64) = 218790 exactly (the P4 closed form at M=32).
- **P10c** the per-stratum profile has at least one nonzero stratum beyond
  s=3 (i.e. s=5 or higher switches on), since s=5,7 were exactly 0 at n=32
  only for arithmetic reasons, not by the ceiling.

### Fallback (registered now)

If P5 lands COLLAPSES on the α=0 slice, that is a conditional verdict, and
I will emit `MODAL_REQUEST.md` in this directory pricing the full n=32
(α,β) scan (app design, sharding over α-orbit representatives, fail-closed
manifest, expected cost) rather than claiming the unconditional result.

