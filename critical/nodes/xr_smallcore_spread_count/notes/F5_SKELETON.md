# F5 skeleton — formal statements and first proved pieces (P1, 2026-07-07)

## Conventions (pinned against verify_xr_smallcore_rungs_2a_2b.py)

Row: domain D ⊂ F_q^×, |D| = n; codewords = deg<k polynomials; pair
(u, v) ∈ F_q^n × F_q^n; pencil word at slope z: u + z·v. A SUPPORT is the
exact agreement set of a codeword with u + z·v at size A = k + σ (σ = the
excess; the floor's core threshold is k + t − 1). ALIGNMENT CONDITION for
(S, z): the values of u + z·v on S extend to a deg<k codeword, i.e. the σ
top interpolation coefficients vanish:

>  Π_S(u + z·v) = 0 ∈ F_q^σ,   Π_S linear in the word.

**Structure Fact 1 (linearity + slope split).** Π_S(u + z v) =
Π_S(u) + z·Π_S(v). Hence each (S, z) contributes σ linear functionals on
(u, v)-space of the RIGID FORM (a_S, z·a_S), where a_S = the top-coeff
interpolation functional row(s) of S, depending on S ONLY.

**Structure Fact 2 (full support, nonzero weights).** Each scalar
component of a_S is supported exactly on S with ALL coordinates nonzero
(Lagrange top-coefficient weights 1/Π_{l≠j}(x_j − x_l) ≠ 0).

## L1 (classification — assembly of proved rung identities)

Every z-aligned support of (u,v) is exactly one of:
(i) SAME-SLOPE (rung 2a: the exact-list object of u + zv) — stripped;
(ii) TANGENT-CHARGED (rung 2b: a distinct-slope pair with core r ≥ k+1
forces (u,v)|core to a codeword pair; depth d = r − k) — stripped;
(iii) LIVE: distinct slopes, all pairwise cores ≤ k + t − 2.
The post-strip remainder consists of class-(iii) families. [Assembly of
proved identities; formal write-up with the verifier's conventions.]

## L2 (alignment ledger — definitional)

A live family {(S_i, z_i)} imposes the condition set
{(a_{S_i}, z_i a_{S_i})}. If the conditions are INDEPENDENT, the family
size is ≤ 2n/σ (solution space nonempty demands #conditions ≤ 2n). So
the theorem reduces to bounding DEPENDENT (syzygetic) families — L3.

## L3a (per-coordinate collapse — PROVED, the first mined obstruction)

**Lemma.** Let Σ_i λ_i (a_{S_i}, z_i a_{S_i}) = 0 be a dependence
(λ ≠ 0). Then per coordinate x, with μ_i(x) := λ_i a_{S_i}(x) over the
participating supports containing x:
   Σ_i μ_i(x) = 0   and   Σ_i z_i μ_i(x) = 0.
If some x is contained in EXACTLY TWO participating supports with
DISTINCT slopes, then (z_i − z_j)μ_i(x) = 0 forces μ_i(x) = 0, and by
Structure Fact 2 (a_{S_i}(x) ≠ 0) λ_i = 0 — contradiction on that
support's participation.
**Corollary (covering rigidity).** In any live dependence, EVERY point of
EVERY participating support is covered by ≥ 3 participating supports (or
≥ 2 sharing a slope — excluded in a live family by class (i) stripping...
[boundary detail: same-slope pairs within a live family are re-classified
to (i); pin in the write-up]). Combined with pairwise cores ≤ k + t − 2,
a participating support of size A needs ≥ ⌈2A/(k+t−2)⌉ partners — live
syzygies require RICH COVERING DESIGNS, not generic families. ∎ (proof
as above; verifier to instantiate at toys)

## L3 (live-syzygy lemma — the remaining core, now sharpened)

**Candidate statement.** A live family admitting a dependence whose
covering design satisfies the L3a rigidity must, on its solution locus,
force Π_{S_i}(v) = 0 for some participant (invalid alignment) or a
class-(i)/(ii) structure. Equivalently: rich-covering live syzygies are
arithmetically unrealizable with all alignments valid.
**Status:** open; held adversarially (Pro window-5: all found dependencies
collapsed to Π_S(v) = 0). P2 attacks EXACTLY the L3a-rigid configurations
(triple-covering designs with pairwise-small cores) — the only place a
counterexample can now live.

## L4 (composition — arithmetic once L3 lands)

Independent families ≤ 2n/σ (L2); dependent families need L3a-rigid
designs, which L3 kills (or bounds); totals ≤ 2n/σ + O(design bound)
≪ 16n³ at every official candidate (slack ~2^100). Toy calibration:
measured engineered maximum 0.55n; measured natural families = q
(slope-limited).

## P1/P2 run 1 (2026-07-07) — HONEST STATUS

- **L3a PROVED on paper** (the proof does NOT depend on the checker):
  dependence Σ λ_i (a_{S_i}, z_i a_{S_i}) = 0 splits into u-block
  Σ λ_i a_{S_i} = 0 and v-block Σ λ_i z_i a_{S_i} = 0. Restrict to the
  LEADING top-coefficient functional a_S^lead(x) = 1/Π_{l≠x}(x−x_l),
  which is nonzero at every x ∈ S (Structure Fact 2, leading row only —
  the lower rows can vanish, but one nonzero functional per point
  suffices). At x: Σ_{i∋x} μ_i = 0 and Σ_{i∋x} z_i μ_i = 0 with
  μ_i = λ_i a_{S_i}^lead(x). A point in exactly one participant forces
  λ_i = 0; in exactly two distinct-slope participants forces
  (z_i−z_j)μ_i = 0 ⟹ μ_i = 0 ⟹ λ_i = 0. So every participant point is
  triple-covered or shares a slope. ∎
- **CHECKER BUG (not banked as verification):** the Modal L3a covering
  flag is over-conservative (flags min-multiplicity < 3 without the
  shared-slope exception), so its "L3a holds: False" is a FALSE flag —
  it does not refute the paper lemma. Also the greedy live-family
  extraction is degenerate on random words (live = 1354 at q = 47 from
  noise, not a structured family). Both need repair before the checker
  validates L3a.
- **P2 decisive signal (partial run):** rigid VALID live syzygies found
  = 0 across all COMPLETED trials (the object whose existence would
  refute L3). Several shards timed out; the run is INCONCLUSIVE, not a
  survival credit. Next: fix the checker (shared-slope exception + a
  real live-family definition scoped to STRUCTURED words), shard the
  larger rows, and run the engineered triple-cover construction that L3a
  says is the only remaining home for a counterexample.

STATUS: L3a is a PROVED obstruction (first mined lemma of the program);
the counterexample surface for L3 is now provably confined to
triple-covering designs with pairwise cores ≤ k+t−2 and all valid
alignments — that confinement is the program's first real progress.

## P2 v2 + realization decision (2026-07-07) — the loop closes on L3's true form

- CHECKER FIXED (one support per slope; shared-slope exception): the
  natural/adversarial-word runs are clean.
- ENGINEERED HUNT (f5_p2_v2_modal.py): ~387 rigid triple-cover designs x
  8 embeddings x 3 scales = ~3000 dependent-configuration tests. ONE hit
  passed the hunt's (incomplete) validity screen: q = 47, the MINIMAL
  3-regular design (8 points, 6 supports, cores <= 2, distinct slopes),
  condition rank 11/12 — a genuine linear-algebra syzygy.
- EXACT REALIZATION DECISION (f5_p2_realize_modal.py): the hit is an
  **ARTIFACT — exactness is FORCED to fail**: coincidence functionals
  cf_i(y) − (u_y + z_i v_y) for union points y outside S_i are
  IDENTICALLY ZERO on the solution space — every solution makes some
  codeword agree beyond its design support, inflating the true agreement
  sets and re-classifying the family OUT of the live class (into
  tangent/big-core territory). The syzygy exists linearly but cannot
  manifest as a spread-family object. L3 STANDS on this hit.

## L3 REFINED (the mined dichotomy — now the precise proof target)

**L3 (refined).** Any dependence among the alignment conditions of a live
family forces, IDENTICALLY on its solution locus, at least one of:
  (a) Π_S(v) = 0 for a participant (invalid alignment — Pro's observed
      collapse mode), or
  (b) an agreement-spillover coincidence (a participant's codeword
      forced to agree outside its support — re-classifying the family
      out of class (iii)).
Evidence: every dependence ever produced (Pro's greedy adversary + our
~3000 engineered rigid configs) died by (a) or (b); the q=47 minimal
design died by (b) via identically-vanishing coincidence functionals.

## L4 ROBUSTNESS (the theorem survives even a weakened L3)

Independent of L3's final form: by L3a + the design-cost combinatorics,
every independent syzygy consumes >= m_min participants (m_min = 6 at
A = 4; general m_min(A) from C(m,2)(A−2) >= 3P >= ... — a finite
combinatorial lemma). Hence rank >= sigma·N_f − N_f/m_min, so
N_f <= 2n/(sigma − 1/m_min) = THETA(n) even if valid syzygies existed.
The 16n^3 theorem is therefore TWO-WALLED: L3 (dichotomy) OR the design
cost — either suffices for L4.

## CORRECTION (same day, self-caught): the "two-walled" claim overstates wall 2

The design-cost route ("every syzygy costs >= m_min participants ⟹
rank >= sigma·N − N/m_min") is NOT a proof as sketched: matroid girth
does not bound nullity in general (R generic vectors in a (c−1)-dim
space have girth c and nullity R−c+1). The route survives only if the
SPECIAL structure of the functionals (full-support a_S on S, pairwise
cores <= k+t−2, the (a_S, z·a_S) slope form) fights nullity growth —
i.e. wall 2 needs L3a-type per-coordinate arguments applied to the whole
dependence SPACE, not just minimal circuits. Status: wall 2 = CANDIDATE
route with this named gap; wall 1 (the L3 dichotomy) remains the primary
proof target, now precisely stated with both collapse modes evidenced.
