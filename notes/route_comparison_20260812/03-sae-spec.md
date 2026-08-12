# Direct S/A/E route: precise specification of the missing theorem(s)

All file:line cites are to the pr1163 branch of /home/u2470931/smooth-read-solomin/rs-mca unless marked OURS. GF = experimental/grande_finale.tex; N1160 = experimental/notes/thresholds/kb_mca_supportwise_near_rational_two_anchor_repair_v1.md; N1163 = experimental/notes/thresholds/kb_mca_v4_common_core_shortening_staircase_route_cut_v1.md.

## 1. The missing chronology-correct whole-line selector (common-core forest compiler)

SOURCE-STATED (N1163 §5, blockquote; §7). The bridge required before any staircase payment moves the ledger:

> For every actual first-match non-affine common-core 32-record, construct a **total** chronology-correct selector that either (i) assigns its identical slope to a **named earlier owner**, or (ii) places it in **one disjoint fixed-core family** to which the staircase payment applies, or (iii)/(iv) emits one of two explicit residual labels. Projection fibers and add-back multiplicities must be derived in **distinct-slope units**.

**Input object** (N1163 §2): a deployed-row record with 32 distinct bad slopes γ_i, explanations h_i, maximal agreement supports Ŝ_i = {x : h_i(x)=r_0(x)+γ_i r_1(x)}, each slope carrying an actual size-m support-wise noncontained witness inside Ŝ_i; common core C = ∩Ŝ_i, c=|C|, with c<k forced in the non-affine case (GF 6112–6135, thm:slope-degree).

**The four terminal outcomes** (N1163 §3, §7):

- **T1 — earlier owner**: a named owner earlier in the v4 first-match chronology. SOURCE-STATED order of removed branches: tangent, common-support, quotient, extension, degree-drop, common-GCD (GF:4767; common-GCD branch defined GF:4724–4735).
- **T2 — paid fixed-core family** (s=k−c): paid iff globally affine (thm:global-block, GF:5759–5781, |Z|≤n−m+1); or s≤2 via B_cell(s)=min{C(R+s,d+s), C(R+s,s+1)} (fails first at s=3); or direction-separated (eq:direction-list-separated, GF:1402–1408: max_c agr(r_1,c)<m) with 3≤s≤13 via J_s=⌊∏_{i=0}^{s}(R+i)/(d+i)⌋, with the exact boundary J_13=47876303026096432<B_*<J_14=743896698428332665.
- **T3 — `DIRECTION_LIST_SHORTENED_s`**, 3≤s≤13, when separation fails.
- **T4 — `COMMON_CORE_SHORTENED_s_GE_14`**, s≥14.

T3/T4 are "residuals, not owners" (N1163 §3).

**Hard constraints** (N1163 §5, §7): totality and exactly-once termination; **disjointness of fixed-core families across varying local cores** — summing B_cell(s) or J_s over core choices is invalid because it "changes the maximum-type v4 endgame into an enormous additive support census"; no zero-cost core deletion (the converse embedding, N1163 §2, lifts any shortened (D′,s,d+s) record back to an original common-core record with identical slopes); hostile controls are the #1160 67472-slope globally-affine line and the inverse-lifted GF(17) atom (N1163 §6–7); preferred falsifier = "the smallest actual selector collision" (§7). Exact walls the selector must respect: the degree-18 interface of thm:partial-relative survives only for c≤4130 (32(m−c)>17(n−c) ⟺ 61952>15c), dying at c=4131; Jo's shortening transfer is blocked at c=4131 by a 3765-bit multiplier C(n,4131)/C(m,4131)>B_* (N1163 §3–4).

**Bypass variant** (SOURCE-STATED, N1163 §5 last paragraph): "An alternative same-owner maximum-type theorem could bypass the fixed-core forest entirely" — i.e., a whole-line theorem routing balanced cores straight into the S/A/E outcomes of prob:mca-spread-routing (GF:7592–7605): (a) rational-owner/quotient/extension/field-drop/near-sunflower atom; (b) bounded union of complete projective correction rays (thm:ray); (c) proper quotient correction space (thm:proper/thm:clone-tolerant); (d) explicitly named residual with a literal row-sharp slope bound — all "with the same received-line owner retained". The selector is not claimed unique; only that **this staircase route needs it**.

## 2. thm:partial-relative — exact preconditions

SOURCE-STATED (GF:6626–6651). Fix either deployed adjacent MCA row and 32 distinct bad slopes. **After (a) maximalizing supports, (b) removing their common-support branch, and (c) selecting exact m-subsupports**, any non-global-affine explanation outside the pure-locator, denominator-root, and scalar-locator rational-profile cells must satisfy 18≤deg_Z E≤31 and χ(S)≥3m−k+3 (=2299571 on KoalaBear). Coherence addendum: if every residual 32-subset is affine-or-rational, either one coherent global structure or a 31-overlap enters the near-sunflower branch.

**The common-factor branch routing requirement**: precondition (b) is load-bearing and unrouted. N1160 §5 (SOURCE-STATED): "thm:partial-relative applies only after its common-factor branch is separately routed; **that unresolved routing remains inside spread frontier (S)**." rem:common-factor (GF:6040–6048) proves the qualifier cannot be omitted: the GF(17) atom's common factor H=(X−1)(X−15) divides every locator and all h_i, so "rational denominator profiles can be hidden inside common-support reductions." N1163 §3 adds that after cancellation at c≥4131 the boxed degree-18 floor itself fails, so the theorem's constants "cannot be reused uniformly." MY-INFERENCE: the selector of §1 **is** the missing routing of precondition (b) — it discharges the common-factor branch that thm:partial-relative assumes removed; the full residual gate is the primitive-spread-core definition at GF:6764.

## 3. "Regenerate the active v4 S/A/E first-match chronology with the 2w charge"

SOURCE-STATED (N1160 §3, §5): the 2w=134944 bound "is a standalone upper bound for the full near-rational bad-slope stratum, hence also for any first-match subset of it. Integrating the charge into a summed ledger still requires the declared owner order. In the active maximum-type order-32 route, **the reserve and the (S)/(A)/(E) interfaces must be updated** rather than pretending this stratum costs one slope"; "its reserve and interfaces have not yet been regenerated" (§5). This route "must incorporate the exact near-rational charge and **same-support semantics**" (§5) — i.e., N1160 §3 repairs 3 and 5: one noncommon witness per bad slope with the w≥1 exact-support hypothesis, and no inference of global column-farness from support-wise badness.

**Which reserve** (MY-INFERENCE, anchored): the 31-slope exceptional reserve — GF:7031 "at most 31 exceptional slopes are reserved for the local-to-global first-match transition", entering eq:owner-target as B_owner(g) ≤ B_*−31−(n−g) (GF:7032–7036), and consumed exactly in thm:conditional-final: "adding the reserved 31 gives **exactly at most** B_*" (GF:7107). Because that arithmetic is exact, a stratum re-priced from +1 to +134944 cannot be absorbed silently; the reserve constant and the owner-target must be re-derived.

**Which interfaces**: (S) = prob:mca-spread-routing (GF:7585–7605) — where the unrouted common-factor branch sits; (A) = the large-owner input eq:owner-target (GF:7032–7036) inside thm:conditional-final (GF:7089–7110); (E) = def:exception-routing (GF:7082–7088) / prob:mca-exception-routing (GF:7607–7609). Concretely required (MY-INFERENCE from the above): declare the 2w-charged near-rational cell's position in the first-match owner order (GF:4767), re-prove thm:conditional-final's case arithmetic with the corrected charge and same-witness semantics, and re-issue eq:owner-target's row targets — none of which is done in any pr1163 source.

## 4. Worker cycle 19's "concrete source witness"

OURS: /home/u2470931/smooth-read-solomin/prize/notes/work_cycles/roadmap_r3/19-active-bc-semantic-gap-20260810.md.

**What exists** (SOURCE-STATED, lines 26–49): the "active balanced-core source-witness compiler [PROVED]". The formerly bare Boolean predicate `BAD_SLOPE_NOT_EARLIER_AND_HAS_ACTIVE_V4_BALANCED_CORE_CERTIFICATE` is now **instantiated** by the active shifted-lattice certificate relation with K=k+1=1048577, ω=981104, w=67471, d_1≥w+1. The schema retains the received line, slope, support locator, explaining data, canonical reduced basis, earlier-owner trace, and balanced profile; finite lexicographic minimization selects exactly one certificate per Z_BC slope, so the selected projection has **unit fibers**.

**What it proves** (lines 16–21, 49–52): it closes a logical-independence gap only — the prior contract admitted all 256 Boolean assignments in a two-slope audit, 31 with nonempty Z_BC and empty endpoint set, so the partition could not imply the K3 bridge. The compiler "prints no slope bound and makes no endpoint claim"; deriving the Q=6,s=6,u=2 endpoint hypotheses stays open (K3-route-specific).

**Why it matters for the direct route** (SOURCE-STATED, lines 54–58): upstream's final interface is exhaustive same-owner routing into (S)/(A)/(E); "the concrete source witness now exists, so the next route decision is to compare that direct route with K3 endpoint realization and pursue the shorter bankable theorem." MY-INFERENCE: it supplies exactly the "actual explanation states" that N1163 §7 orders the forest compiler built on — the two routes now share one witness substrate, and the direct route's entire remaining burden is the selector of §1 plus the regeneration of §3.