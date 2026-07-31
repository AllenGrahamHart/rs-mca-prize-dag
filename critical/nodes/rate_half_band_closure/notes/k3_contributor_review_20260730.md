# K3 contributor review, 2026-07-30 — all open PRs, all authors

Reviewed: Scott Hughes's codex #1122, #1126–#1131, #1133; our Codex's #1121,
#1123–#1125, #1132. Upstream main unmoved at 93fba1be. Facts banked here are
node-local per the standing rule. Nothing below changes this node's status.

## Independent replay of the conic exclusion (#1128)

We re-ran Scott's verifier ourselves from the PR head:
`verify_kb_mca_v4_q6_u2_complete_source_conic_exclusion_v1.py
--check --tamper-selftest` → PASS, **30/30 tamper self-tests**,
`ledger_movement=0`, residual `2+2+2` frontier at **324 cases / 10 orbits**.
The saturation identity `sum div H(alpha_i,-) = 2 div B` that our wave-33
integration cites is therefore independently replayed on our side, not just
inherited from Codex's replay.

## Our degree-5 deletion is the CORRECTED argument — provenance now explicit

Upstream `dead_ends/kb_mca_v4_degree5_prime_field_pgl2_misidentification.md`
(in #1133) documents a REJECTED first draft of the fifth-power argument: it
placed the active roots in the prime-field carrier `D ⊆ F_p` and sought an
order-5 element of `PGL_2(F_p)`. The roots are parameter-line values in
`K = F_(p^6)`; the correct deletion uses `gcd(5,|K^x|)=1` after K-rational
normalizations. **Our integrated attack text is the corrected version**
(checked line-by-line against the dead end's "correct replacement").

## FENCE — the `m | 2^21` trap

From the same dead end: *"the same error also invalidates any unconditional
use of `m | |D| = 2^21` for the geometric endpoint map."* Divisibility of an
inner degree by `|D|` is a necessary condition ONLY after a separate
same-record theorem identifies the parameter-line decomposition with an
m-fold map on the carrier. #1133 states the gate conditionally (only
`m in {2,4}` would pass IF the bridge existed; the bridge is not proved).
**Checked 2026-07-30: our tree currently contains no unconditional use.**
Do not introduce one.

## #1133 — the degree-60 source-fiber adapter (content-reviewed only)

Eight exact inner-degree pole-profile rows; `m=5` empty over `K`; `m=30`
refines to inner degree 6 by exact fifth-power extraction. Its Python
verifier binds to git objects not reachable from the fetched PR ref, so we
could NOT replay it in our checkout — recorded as content-reviewed, not
replayed, matching the ledger's own provenance discipline.

## #1122 — cap-68 secant route refuted

An exact 69-record carrier family realizes constant support 981105, ranks,
exchanges, all 3280 projective ternary secants at distance >= 1052958, and
every printed circuit bound — while NOT implying cap 68. So the pairwise
ternary-secant / support-rank / circuit route to cap 68 is a proved route
cut. Any future cap-68 attempt from this node must use more than those
weakened consequences.

## Lane state

Q=6,u=2 after this review: conic-image branch EMPTY (#1128, replayed);
reciprocal P6 deleted (#1126/#1127, with one false positive caught and
documented in `dead_ends/`); residual = the `2+2+2` frontier (324/10) plus
the decomposition rows `{2,3,4,6,10,12}` under the wave-33 narrowing, with
the 26→24 transverse types at m=12. Three agents interleaved: Scott
(#1122–#1131, #1133), our Codex (#1132), this review.

## Addendum 2026-07-31 — the 112 coordination gap, surfaced and commented

Scott's #1140 compiles all 36 aligned-positive q-slice systems freshly
(`ALL_CELLS_UNCLASSIFIED`, zero citations of our lane); #1141 deletes
F02/F03 from that atlas. Our #1132 export had already excluded the
aligned-positive ramified slices (6 unit ideals) with printed residual
`remaining_unramified=6, deep_cases=17`. Neither stack consumes the other —
the first genuine coordination failure between the forks.

Maintainer approved a cross-reference comment; posted on #1140
(issuecomment-5146556389): states our coverage and residual with replay
line, explicitly does NOT assert cell-for-cell identity (the partitions
differ: his 12x3 vs our ramified/unramified/projective), proposes a mapping
row in either direction, and frames overlap as free cross-verification.
Watch: whether the atlas note gains the mapping, and whether F02/F03 land in
our printed residual (which would make #1141 a continuation, not a
re-derivation).
