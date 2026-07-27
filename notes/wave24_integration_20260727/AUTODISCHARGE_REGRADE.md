# Re-grade of the 20 auto-discharged critical PROVED nodes

**Date:** 2026-07-27. **Planner:** Fable. **Directive:** get the prize
directory stable and accurate.

**Result: no further demotions. Five nodes upgraded from unauditable to
auditable.** The auto-discharge machinery is sound; the e1 failure was a bad
*leaf*, not bad propagation.

## Method

1. **Structural check.** For each of the 20, take the req-parents from
   `dag.json` (authoritative — the prose in `conditional.md` mixes predicates
   with an "Evidence/calibration" list, which is easy to misread; my first pass
   did exactly that and produced a false alarm on `f_primitive_case`).
2. **Leaf trace.** Walk the req-closure of all 20 to its PROVED leaves — the
   actual proof obligations. The cone spans **61 nodes** resting on **26 leaves**.
3. **Failure-signature scan** of every leaf for the two known modes
   (typicality/density; named-exhibit-only) plus conjectural language.
4. **Source grading** of every leaf that rests on a `proof_sketch` section:
   read the section's own status tag upstream and decide whether it supports
   *that node's* claim.

## Findings

**Structure: 19/20 clean** — all req-parents PROVED. The one exception
(`averaged_xr`) had an empty statement, not a bad parent.

**Signature scan: 2/26 leaves flagged, both false positives.**
`acl_second_order` matched on falsifier text that literally reads "not a
conjecture risk"; `f_dual_distance_frame` on the ordinary phrase "all but one
point of a minimal support".

**Sketch-backed leaves: 11 of 26.** Five of those cite
`s3b_iii_3_fibers_and_noanchor.md#1`, tagged **`[verified toy + CONJECTURE]`** —
the same signature that condemned `zone_b`. **They survive, and the reason is
the distinction that matters:**

- That section has two halves: verified toy computations (F_13, mu_12, the
  planted-fiber law `fiber = C(A_0, A_0-A)`) and **Conjecture F** (fiber
  rigidity), explicitly tagged CONJECTURE.
- The five citing leaves — `f_gcd_reduction`, `f_dim1`, `f_termination_mds`,
  `f_concurrency_equiv`, `f_dual_distance_frame` — carry **self-contained
  proofs that import neither half**. `f_gcd_reduction` is a linear-algebra
  reduction (divide by the common divisor; division is linear and injective);
  `f_dim1` is a voting argument (each domain point casts at most one vote, so
  at most floor(n/j) members); `f_termination_mds` is MDS shortening + dual
  distance. They cite the section as *provenance*, not as an imported premise.

**Contrast with `zone_b`, and the general rule this establishes:**

> A citation into a mixed-status sketch section is only a defect when the
> node's own claim IS the conjectural part. `zone_b`'s claim was the
> conjectural zone (b) verbatim. These five merely share a section with a
> conjecture.

## The real defect found: five PROVED leaves with no written claim

Five leaves had a **stub `proof.md`** (whole content: a pointer to a sketch
section) **and an empty statement** — so nothing could be audited even in
principle. They are load-bearing: `periodic_strata` alone has 14 critical
consumers, `ext_pole_floor` 12.

Demoting them would have been wrong — an absence of documentation is not a
substantive defect, and (unlike `zone_b`) each cited section is tagged
**verified** or **elementary** for exactly the fact the node names. So each
statement was **transcribed faithfully from the upstream source and
scope-fenced**:

| node | source section | tag |
|---|---|---|
| `vtdv` | `s3b_iii_2_displacement_spectral.md#1` | elementary, verified |
| `ext_pole_floor` | `s6_extension_lift.md#2` | verified |
| `generating_escape` | `s6_extension_lift.md#3` | verified |
| `periodic_strata` | `s3b_ii_strip_periodic.md#4` | verified combinatorics + SKETCH |
| `noncontain_degeneracy` | `s4_reserve_dictionary.md#2` | textually grounded (quotes `thm:normalform`, PROVED-cited) |

Each transcription carries an explicit **SCOPE fence** naming what is *not*
claimed — in particular `periodic_strata` fences off the interpretive
"right stratification" reading and the same file's section 5, which is
CONJECTURE (operative R2); and `ext_pole_floor` fences off section 4's
safe-side classification, also CONJECTURE. `noncontain_degeneracy` is recorded
as closure-by-citation (an identification of quantifiers; it strengthens no
bound).

Empty-statement pin lowered **36 -> 31**.

## Standing rule added

Never read `conditional.md` prose for predicates — take req-parents from
`dag.json`. The "Evidence/calibration" list sits under the same heading style
and includes non-PROVED nodes by design (`f_primitive_case` lists `perfiber`
[WALL] and `f_pair_bound_envelope` [CONJECTURE] there, entirely correctly).
