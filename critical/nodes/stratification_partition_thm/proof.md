# proof: stratification_partition_thm

- **status:** PROVED
- **closure:** proof
- **verifier:** `verify.py` (this directory) — exhaustive toy-model machine-check
- **source of predicates:** `wp_detail/wp2_3_stratification_case_tree.md` §2
  (legacy repo `rs-mca-l1/experimental/notes/roadmaps/wp_detail/`); fuzz spec
  reproduced from that note's §4.

## The claim

The T0–T7 first-match stratification (the campaign's dedup convention, the
"first-match tree" consumed by the paid-ledger assembly) is a **partition** —
total and pairwise disjoint — of the pair space. Precisely: for a fixed exact
agreement `A`, let

```text
Pi_A = { ordered pairs (u,v) of syndrome vectors at exact agreement A }
```

(with `t = A - k`, `j = n - A`); the whole pair space is the disjoint union
`Pi = ⊔_A Pi_A`. The tree defines a classification map
`cls : Pi_A -> { T0, T1, T2, T3, T4, T5, T6, T7, L }` (the eight gates plus the
terminal residual leaf `L`), and the theorem is that `cls` is **well-defined
and everywhere-defined**, i.e. every pair lands in **exactly one** cell.

This node is the last leaf under the final three provables of the prize DAG;
`strat_tree/conditional.md` consumes it as its single predicate ("every pair
enters exactly one T0–T7 cell"), and `safe_assembly_uniformity/conditional.md`
clause (ii) is *exactly* this partition ("the stratified sum with first-match
dedup composes").

## 1. The eight case predicates, transcribed exactly

Quoted verbatim from `wp2_3_stratification_case_tree.md` §2 ("per exact
agreement A; pair (u,v); t = A-k, j = n-A"), first-match order:

```text
T0 containment gate      predicate: exists locator l with H(u)l = H(v)l = 0
                         (the degenerate-pencil stratum, s4 = def:residue's
                         noncontainment)  -> EXCLUDED from LD_sw. [exact]
T1 degenerate pairs      v = 0 / u = 0 / v = lambda u  -> zero/proportional
                         leaves; priced by the #171 zero-u/zero-v/
                         proportional lemmas [pending replay].
T2 tangent overlap       exists Z0, codeword c, agreement(u + Z0 v, c) =
                         A0 > A  -> TANGENT-PAID; fiber = common-divisor
                         plane, count C(A0, A0 - A) [verified toy,
                         s3b_iii_3]; price B_tan [PROVED-cited #147 range].
T3 quotient periodicity  the pencil folds rate-preservingly through
                         x -> x^M, M | gcd(n,k), M > 1 (syndromes descend)
                         -> QUOTIENT-PAID at scale M; recursion to the
                         quotient row [PROVED-cited Q_M = Q_1 + rem:aper
                         convention, s3b_ii/s4]; zone-(b) cells stay
                         intervals [s2].
T4 direction rank        r = generic rank of the pencil; r <= r0 (currently
                         r0 = 12 for the synthetic families) -> low-rank
                         ladder leaves [#170, pending replay]; else full.
T5 regime split          t >= j+1 -> REGULAR bucket: canonical gcd/lcm
                         ledger, fronts alpha/beta [predictions P1a/b/c,
                         P-beta, s3a]; else deficiency-d chart program
                         [wp2_6: Cramer/divisibility at d = 1, pencil
                         charts at d >= 2].
T6 cross-bucket dedup    kernel locators of degree < j -> charged to the
                         higher-agreement bucket [wp2_6 side chart; exact].
T7 split-locator gate    surviving eliminant roots filtered by
                         L | X^n - 1 and the noncontainment gate
                         [#171 gate, pending replay; s3b_iii_3 window
                         convention m = 1..t].
LEAF residual(named)     whatever survives: labelled quotient / tangent /
                         extension / candidate_new_obstruction / unknown
                         per towards-prize.md §4.6 — the catch-all that
                         makes the tree TOTAL.
```

Extension rows insert `T3'` (subfield confinement / pole type) between T3 and
T4 (`s6`); generating rows skip it. See §5 — this refinement does not affect
the partition property.

Write `P0, ..., P7` for the eight **match-predicates** on `Pi_A` — the
condition under which first-match testing assigns the pair to that gate:

```text
P0(u,v)  :=  ∃ locator l : H(u)_l = H(v)_l = 0                    (containment)
P1(u,v)  :=  v = 0  ∨  u = 0  ∨  (∃ λ : v = λ u)                  (degenerate)
P2(u,v)  :=  ∃ Z0, codeword c : agreement(u + Z0 v, c) = A0 > A   (tangent)
P3(u,v)  :=  ∃ M > 1, M | gcd(n,k) : the pencil folds through x↦x^M
                                     (syndromes descend)          (quotient)
P4(u,v)  :=  r(u,v) ≤ r0        [r = generic pencil rank; r0 = 12] (low-rank)
P5(u,v)  :=  the regime ledger closes the pair — the REGULAR ledger
             (when t ≥ j+1) or the deficiency-d chart (when t < j+1)
             prices it in full, leaving no sub-degree kernel locator
             and no surviving split eliminant root                (regime)
P6(u,v)  :=  ∃ kernel locator of degree < j                       (cross-bucket)
P7(u,v)  :=  ∃ surviving eliminant root ρ with L(ρ) | X^n − 1
             passing the noncontainment gate                      (split-gate)
```

The one interpretive choice is `P5`: T5 is written as a *split* (regular vs
deficiency), and T6/T7 are listed *after* it, so under first-match a pair can
only reach T6/T7 if T5 did **not** already close it. `P5` above is the reading
that makes the listed order `T5 < T6 < T7` consistent: T5 matches iff the
regime ledger fully prices the pair, and the pairs the source routes to T6
(a sub-degree kernel locator remains) or T7 (a split eliminant root survives)
are exactly the pairs the regime ledger did not close. §4 records that the
partition conclusion is **independent** of this choice: it holds for *any*
predicates whatsoever in the T5 slot; the choice moves mass between cells but
cannot break totality or disjointness.

## 2. The partition skeleton: a general lemma

The tree is evaluated **first-match-wins** in the order above (§1 of the
source: "that order IS the dedup convention"), and it terminates in an
explicit catch-all leaf `L`. Everything reduces to one purely logical fact.

**Lemma (first-match with catch-all is a partition).**
Let `Pi` be any universe and `P0, ..., Pm` any predicates on it. Define the
**guard predicates**

```text
G0    :=  P0
Gi    :=  (¬P0 ∧ ¬P1 ∧ ... ∧ ¬P_{i-1}) ∧ Pi        (1 ≤ i ≤ m)
GL    :=  ¬P0 ∧ ¬P1 ∧ ... ∧ ¬Pm                     (the catch-all leaf)
```

and the cells `S_i = { x : G_i(x) }`, `S_L = { x : G_L(x) }`. Then
`{ S_0, ..., S_m, S_L }` is a partition of `Pi` into (possibly empty) blocks;
equivalently, exactly one of `G_0, ..., G_m, G_L` is true at every `x`.

**Proof — disjointness.** Take indices `i < j` where `j ∈ {0,...,m,L}`. Every
guard with index `> i` — including `G_j` and `G_L` — contains `¬P_i` as a
conjunct, by construction. And `G_i` contains `P_i` as a conjunct (for
`i = 0`, `G_0 = P_0`). Hence
`G_i ∧ G_j  ⊢  P_i ∧ ¬P_i  =  ⊥`, so `S_i ∩ S_j = ∅`. As `i < j` was
arbitrary, the cells are pairwise disjoint: **at most one** guard is true at
any `x`.

**Proof — totality.** Fix `x ∈ Pi` and let `K = { i ∈ {0,...,m} : P_i(x) }`.

- If `K = ∅`: then `¬P_i(x)` for all `i`, so `G_L(x)` holds; `x ∈ S_L`.
- If `K ≠ ∅`: let `i* = min K`. For every `i < i*` we have `i ∉ K`, i.e.
  `¬P_i(x)`; and `P_{i*}(x)` holds. Thus the conjunction defining `G_{i*}`
  is satisfied: `x ∈ S_{i*}`.

Either way **at least one** guard is true at `x`. With disjointness, exactly
one is. ∎

The lemma needs *nothing* about the `P_i` — not that they are "simple", not
that they are disjoint, not that their disjunction is a tautology, not that
the cells are nonempty. Totality is bought entirely by the presence of the
catch-all `G_L`; disjointness is bought entirely by the guarding conjunctions
`¬P_0 ∧ ... ∧ ¬P_{i-1}`, which are *automatic* in a first-match evaluator (a
pair reaches gate `i` only after gates `0..i-1` all missed).

## 3. Instantiation: the T0–T7 tree is a partition

Apply the Lemma with `m = 7` and `P0, ..., P7` the eight match-predicates of
§1, and `S_L` the residual leaf `L`. The guard predicates are, written out so
a referee can read each stratum's exclusivity directly:

```text
G_{T0} = P0
G_{T1} = ¬P0 ∧ P1
G_{T2} = ¬P0 ∧ ¬P1 ∧ P2
G_{T3} = ¬P0 ∧ ¬P1 ∧ ¬P2 ∧ P3
G_{T4} = ¬P0 ∧ ¬P1 ∧ ¬P2 ∧ ¬P3 ∧ P4
G_{T5} = ¬P0 ∧ ¬P1 ∧ ¬P2 ∧ ¬P3 ∧ ¬P4 ∧ P5
G_{T6} = ¬P0 ∧ ¬P1 ∧ ¬P2 ∧ ¬P3 ∧ ¬P4 ∧ ¬P5 ∧ P6
G_{T7} = ¬P0 ∧ ¬P1 ∧ ¬P2 ∧ ¬P3 ∧ ¬P4 ∧ ¬P5 ∧ ¬P6 ∧ P7
G_{L}  = ¬P0 ∧ ¬P1 ∧ ¬P2 ∧ ¬P3 ∧ ¬P4 ∧ ¬P5 ∧ ¬P6 ∧ ¬P7
```

- **Disjointness (structural, by inspection).** For any two rows `Ti` (or `L`)
  with `i < j`: row `j`'s guard contains `¬Pi`; row `i`'s guard contains `Pi`.
  No pair can satisfy both. This is a *literal, per-stratum* pairwise
  exclusivity, not an asymptotic or generic statement — it is a propositional
  contradiction `Pi ∧ ¬Pi`. So the nine cells are pairwise disjoint: the tree
  never double-claims a pair. This is precisely the property the M4 dedup
  table and the WP-0.4 checker must enforce (source §1: "the tree definition
  and the dedup logic are one artifact, not two").

- **Totality (the real content).** `G_L` is the negation of the disjunction
  of the eight match-predicates, and it is a *defined cell of the tree* — the
  source's own `LEAF residual(named)`, "the catch-all that makes the tree
  TOTAL." Therefore the disjunction
  `G_{T0} ∨ ... ∨ G_{T7} ∨ G_L` is a tautology over `Pi_A`: every pair either
  hits a least-index gate or, hitting none, falls into `L`. There is **no**
  pair type for which no cell fires. The only way totality could have failed
  is if the tree had *no* catch-all and `P0 ∨ ... ∨ P7` were not a tautology
  — and indeed it is **not** a tautology (see §4). The tree is total *because*
  the residual leaf is defined, not because the eight gates exhaust the space.

By the Lemma, `cls` is well-defined and everywhere-defined: every pair enters
exactly one of `{T0,...,T7,L}`. **This is the partition theorem.** ∎

## 4. Honesty gate — the residual leaf is genuinely inhabited

The partition theorem is `∃!` per pair; it does **not** claim `S_L = ∅`. It
must not be confused with the far stronger — and *open* — claim "every pair is
paid" (that `L` is empty), which is essentially the prize itself. The source
is explicit that `L` carries real mass:

- **Toy scale (source §5, F1).** "A RANDOM toy pair reaches the residual leaf
  unpaid — at toy scale FM says this is possible (small q!)." So over a small
  field, `S_L ≠ ∅` by counting. The tree exposes that mass; it does not
  eliminate it.
- **By design (source §5, F2 / GAP-1).** "T3's fold-detection predicate misses
  non-equivariant periodic pairs (GAP-1) — they land in the residual leaf BY
  DESIGN — the tree makes GAP-1's mass visible and measurable rather than
  hidden." So `S_L` is *intended* to be a nonempty named cell (labelled
  `candidate_new_obstruction / unknown`, source §2 LEAF and towards-prize
  §4.6).

Consequently the eight gates **T0–T7 alone are not total**: `P0 ∨ ... ∨ P7`
is not a tautology, and the "8-cell stratification without the residual" is
*not* a partition of `Pi_A`. What is a partition is the **9-cell** family
`{T0,...,T7, L}`. This is the honest statement, and it is exactly what the DAG
title ("PARTITION of all pairs") and the consumers require: the residual `L`
is a *bona fide* block of the partition, the ledger's "named-not-paid" column,
not a proof that everything is paid.

Robustness of the conclusion to the T5 reading (§1): because the Lemma quantifies
over *arbitrary* `P0..P7`, replacing `P5` by any other predicate (e.g. the
naive `P5 ≡ ⊤`, which would empty T6/T7/L, or `P5 ≡ ⊥`, which would route
everything past T5) leaves `{T0,...,T7,L}` a partition. The interpretive choice
determines which cells are inhabited, never whether the family partitions.

## 5. Splits and the T3' insertion do not threaten the partition

Three nodes are not single terminating gates; none breaks the Lemma:

- **T4 (`r ≤ r0` low-rank vs "else full").** This is a *split* of the pairs
  reaching T4: `P4` is the low-rank match; the "else full" branch is simply
  `¬P4`, which continues to T5. A split refines a cell into disjoint
  sub-cells (`P4` and `¬P4 ∧ (rest)`) and cannot create overlap or a gap.
- **T5 (regular vs deficiency).** Likewise a split; whichever sub-bucket a
  pair falls in, `P5` (regime-closes) is the single match-predicate feeding
  the Lemma, and the regular/deficiency tag is an orthogonal sub-coordinate on
  `S_{T5}`. Splitting `S_{T5}` by `t ≥ j+1` keeps it a disjoint union.
- **T3' (extension rows only).** Inserting a gate between T3 and T4 just
  lengthens the guard list to `m = 8`; the Lemma holds for every `m`. On
  generating rows T3' is absent (`P_{T3'} ≡ ⊥`), collapsing its cell to empty
  — still a partition. So the tree is a partition on *both* row types, with or
  without T3'.

In general: subdividing any block of a partition by a predicate yields a finer
partition; the Lemma's conclusion is closed under such refinement. The tree's
splits are exactly such subdivisions.

## 6. Machine check (`verify.py`) and fuzz reproduction

`verify.py` builds a **complete finite toy model** of the pair space at the
level the predicates can resolve it: a record of the combinatorial features the
eight predicates read (containment flag, degeneracy flag, tangent flag, fold
scale `M ∈ {1,2,3}`, pencil rank `r ∈ {2,12,13,20}` straddling `r0 = 12`,
regime-closes flag with the `t≥j+1` regular/deficiency tag, cross-bucket flag,
split-gate flag). It **exhaustively enumerates the full Cartesian product**
(1536 feature points — the entire model, not a sample) and, for each point,
evaluates all nine guard conjunctions `G_{T0..T7}, G_L` independently and
asserts **exactly one is true**. That is a direct, complete machine-check of
both partition axioms over the toy model: "no fall-through" (≥ 1) and "no
double-claim" (≤ 1), reproducing the source §4(ii) acceptance criterion
exhaustively rather than by 500 random draws.

It additionally:
- plants the source §4(i) constructor pairs (contained; `v=0`; proportional;
  tangent `A0>A`; folded `M=2`; low-rank synthetic; a regime-closing generic;
  a cross-bucket residual; a surviving split-root; an all-miss pair) and checks
  each lands in its intended stratum;
- exhibits explicit points in `S_L` (all eight predicates false), confirming
  the §4 honesty gate that the residual leaf is a genuine, inhabited block;
- re-runs the exactly-one check under 200 randomized re-definitions of the
  slot predicates (including `P5`), demonstrating the partition property is
  invariant to the interpretive choice of §1 — i.e. it is structural.

Note: the source's named script `experimental/scripts/`
`verify_m3_stratification_tree.py` is *not yet materialized* in the legacy
repo (§4 is a spec with pinned seeds); `verify.py` here is a self-contained
stand-in that machine-checks the partition axioms the spec's step (ii)
demands. `verify.py` prints `PASS` with the count of feature points checked.

## 7. Conclusion

The T0–T7 first-match tree, terminating in its named residual leaf `L`, is a
partition — pairwise disjoint (propositional, per-stratum) and total (by the
catch-all `L`) — of the pair space `Pi`. Every pair enters exactly one cell,
so counting or charging by first match neither misses nor double-counts any
object. The residual leaf is a *nonempty* named block (GAP-1 / small-field
mass), which the theorem accounts for honestly and does not claim away. This
discharges the predicate consumed by `strat_tree/conditional.md` and by
`safe_assembly_uniformity` clause (ii). **PROVED.**
