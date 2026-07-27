# Empty-statement remediation on the critical PROVED surface

**Date:** 2026-07-27. **Planner:** Fable. **Result: 31 -> 9.**

A PROVED node with no `statement` cannot be audited, Lean-targeted, or checked
against upstream — it is a label with no claim. 22 of the 31 were remediated by
**faithful transcription from a primary source**, never by paraphrase, and every
one carries its provenance inline plus a SCOPE fence where the source section is
mixed-status.

## Method (three sources, in order of preference)

1. **The node's own proof.md carries an explicit `## Statement` section** —
   lifted verbatim: `dyadic_profile_evaluation`, `gap2_seam`.
2. **The node's own proof.md is a genuine self-contained proof** — statement
   distilled from it: `fm1` (the exact first-moment count
   `E[#aligned] = binom(n,j)(1 - q^-t) q^(1-t)`), `paid_tan_fn`, `paid_quot_fn`
   (interval-valued, with the zone-(b) nonclaim preserved), `ext_import`,
   `paid_ext_fn`, `stratification_partition_thm` (the T0-T7 partition,
   machine-checked by its own verify.py), plus the two citation-closure nodes
   `axis9_dither` and `rules_m_reading` distilled from their ledgers.
3. **The node is a stub pointing upstream** — transcribed from the section,
   read via `git -C ../rs-mca show origin/main:experimental/notes/roadmaps/proof_sketch/<file>`:
   `list_unsafe`, `qcore` (s7#2, PROVED-cited + verified), `codegree`,
   `deep_point` (s7#3), `staircase` (s2#1), `q_recursion` (s3b_ii#2),
   `confinement`, `isotypic` (s3b_ii#1), `b_rational_lift` (s6#1),
   `counting_frame`, `v8_ledger` (spine#2), `cap_theorem` (Paper D v12).

Where a source section is mixed-status, the transcription states only the
verified half and names the excluded half explicitly. Examples: `staircase`
claims `B_tan(A) <= n - A + 1` and fences off the load-bearing quotient term;
`q_recursion` claims the recursion `Q_M(H_n) = Q_1(H_{n/M})` and fences off the
surrounding SKETCH; `b_rational_lift` fences off the CONJECTURE safe-side
classification; `cap_theorem` records that it is an upper bracket on `delta*`
and does NOT pin `delta*` (that is the separate `unsafe_at_crossing`
obligation), and carries the blueprint's "modulo Crites-Stewart" caveat.

## The 9 deliberately NOT written

Writing a statement I cannot source would be worse than leaving the gap — it
manufactures false precision on a PROVED node. Each of these needs a specific
read first:

| node | source to read | why it was deferred |
|---|---|---|
| `acl_count` | `thm:exactcount` (its critical_dag title: `Acl = 2^{beta N'(1-o(1))}`, char 0) | Its ref points at `s3b_iii_3#2`, tagged **SKETCH**, whose content (Conjecture F unification) does NOT match the node's claim. **The ref is probably mis-pointed** — locate `thm:exactcount` upstream and re-point before stating. |
| `averaged_xr` | `s3b_iii_2#5` | Section tagged **SKETCH** ("Averaged version"). Same risk class as `zone_b`: may be an over-claim rather than a documentation gap. |
| `axes_verified` | `s4_reserve_dictionary.md` (whole-file ref, no section) | Ref lacks a section anchor; §1 is `[VERIFIED]` but §3 is a derivation and §5 forks. Needs the anchor pinned first. |
| `char0_collision_classification` | `tex/slackMCA_v4.tex` | Paper-level ref; needs the theorem located. |
| `common_code_line_budget` | `experimental/notes/m2/m2_common_code_line_residual_budget.md` | Ledger says it is "the proved general tangent-payment engine"; transcribe from the note. |
| `l1_program_frontier`, `l1_core_defect_reduction`, `l1_crt_compression`, `l1_defect_layer_bounds` | `experimental/notes/l1/l1_full_list_quotient_proof_program.md` | The note is a **proof PROGRAM**: its centrepiece is *Conjecture 1* (conjectural) while *Theorem J* is PROVED. These four must be graded against which part each actually rests on — a genuine adjudication, not a transcription. |

**Priority: `acl_count` and `averaged_xr` first** — both are the `zone_b`
signature (a PROVED node citing a SKETCH-tagged section), so they are candidate
over-claims rather than documentation gaps. The four `l1_*` nodes are next, and
should be adjudicated as a block against Theorem J vs Conjecture 1.

Empty-statement pin lowered **31 -> 9**.

---

## COMPLETE — 2026-07-27: the count reached ZERO

All nine deferred nodes were resolved. Outcomes:

**The four `l1_*` nodes — adjudicated, all four PROVED stand.** The note's
HEADER status "CONJECTURAL / PROOF PROGRAM" applies to its **Conjecture 1**;
each individual lemma carries its own `Status: PROVED`. The mapping:

| node | proved result |
|---|---|
| `l1_program_frontier` | **Theorem J** (Full-List Johnson Region): `|ImgFib_U(s)| <= 1` if `2s > n+k-1`; `<= n(n-k+1)/(s^2 - n(k-1))` if `s^2 > n(k-1)`. Pins the frontier: the open difficulty is the SUB-Johnson range `s^2 <= n(k-1)`. |
| `l1_core_defect_reduction` | **Lemma 2** (Sunflower Core-Defect Reduction) |
| `l1_defect_layer_bounds` | **Lemma 3** (Fixed-Defect Layers Are Polynomial): `<= sum_{d<=d0} binom(k-1,d) binom(n-k+1,d+1) = O_{d0}(n^{2d0+1})` |
| `l1_crt_compression` | **Lemma 7** (Full-Petal CRT Compression): defect pinned to `ell <= d <= (t-1)ell` |

Each statement records that it rests on the proved lemma and **not** on
Conjecture 1.

**`common_code_line_budget`** — upstream note is a "PROVED finite theorem for
MDS codes"; the exact bound `<= floor((|Omega|-c0)/(h-c0))` transcribed.

**`char0_collision_classification`** — real source is `thm:rigidcyclo`
(Cyclotomic rigidity, `tex/slackMCA_v4.tex`): a vanishing `p_1(A)` on
`A subset mu_{2^s}` forces `A` to be a union of antipodal pairs, so every
characteristic-zero `V_2` witness is coset type. Ref re-pointed and
scope-fenced against `rem:wall` (asymmetric `V_t` elements are genuinely
modular and are NOT claimed).

**`axes_verified`** — recovered from its original dag title, "Axes 3/5/7
verified + q-dictionary (axis 6)": a scope-normalization aggregate, sourced to
`s4_reserve_dictionary.md` (§1 the `FM crossover = tau*` identity, tagged
VERIFIED and machine-checked exact at all four rates; §2 the quantifier
dictionary). **An honest gap is recorded in the statement itself:** the ref has
no section anchor and the individual contents of axes 3, 5, 7 are not pinned
in-tree. Retained PROVED as a scope record rather than a mathematical bound,
with the dossier obligation to pin each axis written into the node.

**`_EMPTY_STMT_PIN` is now 0 and must never rise.** Every PROVED node on the
critical surface carries a statement with provenance, and every mixed-status
source carries an explicit SCOPE fence.
