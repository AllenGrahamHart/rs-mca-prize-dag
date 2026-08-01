# Wave-37 audit — the (4,2) negative row collapses: two-loop residual, both one-loop skeletons, and half the zero-loop atlas

**Date:** 2026-08-01. **Planner:** Fable. **Range:** `8b5ab50b..37be856d`
(53 Codex commits, 07-31 19:48 – 08-01 09:57, plus its merge of our master).
**Verdict: CLEAN — integrated in full.**

```text
math orbit  241 = 179/38/24   ->   241 = 179/38/24   (unchanged)
nodes 1610 -> 1663 (+53)      edges 4348 -> 4532 (+184)
```

53 new nodes, **all PROVED**, all background, **116/116 verifier runs PASS**
(112 from the overnight snapshot + 4 from the second zero-loop orbit committed
mid-audit), zero status changes. Edge discipline exact: 53 `ev` edges into
`rate_half_band_closure` (one per node), 96 `req` edges confined to background.
Codex committed twice *while I was auditing* — the wave is pinned at
`37be856d`, the second zero-loop orbit close.

## What fell this wave

The entire remaining negative-parity ledger of the m2 `(4,2)` row except
seven zero-loop cells:

1. **X2/N1/L1 constrained cells (30) — CLOSED.** The missing outside
   forced-mate/invariance compiler wave 36 asked for was built: exact
   candidate-row minors force `p` in each ledger (`b=-c^3` in all three rows),
   and a nonsingular bilinear involution `Gamma yz-Alpha(y+z)-Beta=0` defines
   exactly 30 cells in three rank-eight base algebras. The same 75 universal
   matching templates as the M2/M3 theorem evaluate to **450/450 unit
   obstructions**, independently replayed by a second projection order and
   full-rank `8x8` multiplication matrices. With the M2/M3 parent, **the
   complete `(4,3,3)` two-loop skeleton is empty**.

2. **One-loop `(4,4,2)` — CLOSED** (38 nodes). The 15 common matching cells
   fall into six orbits under the target sign/exchange four-group,
   `[0]|[1,2]|[3,6]|[4,5,7,8]|[9,10,12,13]|[11,14]`, each deleted by a named
   terminal parent; the `[9,10,12,13]` sextic sector alone took the
   S0/S1/S2 guarded-product chain (eighty product cells). Composed in
   `..._one_loop_442_complete_exclusion`.

3. **One-loop `(4,3,3)` — CLOSED** (9 nodes). Same six-orbit partition; five
   orbits die at the common stage, `[3,6]`'s sixteen packets die at the
   complete paired-product gate (11760 = 3360+6720+1680 unit ideals, census
   reproduced under the reverse variable order). Composed in
   `..._one_loop_433_complete_exclusion`.

4. **Zero-loop `(4,3,3)` — 8/15 cells.** The q-weld compiler is PROVED
   (rank-3 rows `[1,s,s^2,v_s]`, two `4x4` determinants necessary and
   sufficient), and the first two four-cell orbits `[0,4,7,11]` and
   `[1,3,8,10]` are deleted. Remaining: `[2,5,6,9]`, `[12]`, `[13]`, `[14]` —
   the working tree already shows uncommitted work on the next orbit.

## Independent checks I ran

- **Both weld lemmas replayed symbolically.** The denominator-free one-loop
  weld `(KBN1W-4)` is exactly the `3x3` minor of `[1,s,q_s/d_s]` cleared by
  `d_i d_j d_k` — sympy confirms the identity. The anchor-sufficiency legs
  reduce to `2x2`/`3x3` Vandermonde determinants, which factor as products of
  label differences, nonzero for distinct labels in `K`.
- **Crossed-pair resultant `(KB41X-3)` replayed:** `Res_r(P/b,Q/c)` reduces
  mod `i^2=-1` to `-2(b-1)(b+1)` exactly. The premise that `i` exists in the
  deployed field holds: KoalaBear `p = 2130706433 = 1 mod 4`.
- **Partition arithmetic:** both 15-cell orbit partitions are disjoint covers
  (1+2+2+4+4+2 and 4+4+4+1+1+1), with orbit sizes consistent with a Klein
  four-group action.
- Repo validators at the pin: 5/6 PASS (census, conditional propagation,
  auto-discharge paths, harness coverage, crosswalk). The sixth — see below.

## Two operational findings

**The canonical-writer tax is gone.** `dag.json` at the pin is byte-exact
canonical (`indent=1, ensure_ascii, trailing newline`). First wave since the
tax began with **no renormalization commit needed**. Watch item (c) closed.

**Codex fixed ramguard, and the fix is load-bearing.** It added a
`prlimit --as` fallback (same byte limits per profile) for hosts where the
systemd user bus is absent. Our own prize checkout's old ramguard **fails on
this machine today** ("Failed to connect to bus") — the fallback is not a
convenience, it is what kept the COMPUTE LAW enforceable overnight. The whole
wave ran at **zero Modal cost**: every certificate is exact algebra sharded
under the 60-second tiny profile.

**A latent validator break in BOTH trees** (found while running the six):
`verify_official_row_primes_pinning.py` still points at
`critical/nodes/official_row_primes_pinning/`, but the node moved to
`background/nodes/` in the 07-26 critical-surface reorganization. It fails
identically in our tree and Codex's — a pre-existing path break, not a Codex
regression. Fixed post-merge as a forced correction (one line,
`critical` -> `background`).

## Upstream watch items

- **#1140 coordination comment:** no responses yet (posted 07-31 19:10).
- **#1132 (living PR):** last push remains 07-31 10:21 (`543db66f`,
  saturated-112 q-slices). **None of the `kb_m2_r4` campaign — not just the
  overnight material, the entire multi-week (4,2) coordinate-row program —
  has ever been exported upstream.** `#1132`'s file list contains zero
  `kb_m2_r4` paths. This is no longer an export-granularity question; see
  the collision finding below.

## COLLISION FINDING — Scott's codex is in the order-two row

Post-integration review of the open PR queue (prompted by the maintainer's
duplication concern) found Scott Hughes's #1139/#1141 carrying
`kb_mca_v4_m2_r4_order2_source_facet_interpolation_v1` — his codex is
working **the same `(m,r,delta)=(2,4,2)` order-two type** from the source
side. Three facts, established against the PR heads:

1. **A second convergent duplication is confirmed.** His packet's
   diagonal-orientation leg — split quartics from the two quadratic fibers
   over a `psi` fiber, exact diagonal transport under `tau`, descent from a
   bidegree-`(4,4)` endpoint component iff an interpolation kernel condition
   holds (his concrete `35 x 12` matrix) — is the same construction as our
   `rate_half_kb_m2_r4_diagonal_fiber_resultant_interpolation_compiler`,
   down to the shared Corollary 9.27 support facets. **Both were built on
   2026-07-30, independently** (his upstream commit 09:47; our three
   diagonal nodes committed the same day). After the 112 atlas, this is the
   second same-week re-derivation caused by the unexported lane.
2. **His coordinate-orientation leg is complementary and useful:** an exact
   source-facet census `(10,10,4)` plus an aligned defect-zero fixture
   proving *counting alone cannot delete the coordinate orientation*. We
   never proved that impossibility; our worker simply chose the algebraic
   route. His theorem justifies our route — and points his agent's next
   step directly at algebraic deletion, i.e. at re-deriving our closed
   negative-parity skeleton campaign.
3. **Cross-consumption works where material is exported.** His note takes
   the full-V4 deletion as given — consuming our #1132 export
   (`rate_half_kb_m2_r2_dihedral_full_v4_exclusion`). The one lane we
   exported is the one lane he did not duplicate.

Our unduplicated diagonal surplus: `diagonal_source_subfield_dichotomy` and
`diagonal_facet_mixing_obstruction` (both 07-30, both unexported).
- **h7 payoff ladder** (standing): untracked `l1_mersenne_hnf_colored_frobenius_gate`
  in Codex's working tree — the h7 lane is stirring again, still without a
  stated payoff. Unchanged ask.

## The m2 ledger after this wave

`(4,2)` order-two row, negative coordinate parity: two-loop **done**,
one-loop **done**, zero-loop 8/15. Then: positive parity, the other
coordinate orientation (fenced in every statement), the `(2,4)` full-V4
realizability question (`n in {3,6}`), and the untouched `(8,1)` row.

## Assessment

Fifteenth wave, still zero red closures, and the census will not move until
the whole K3 endpoint-map campaign discharges into `rate_half_band_closure`.
But this is the fastest structural collapse the lane has had: wave 36 closed
two skeleton families in a night; this wave closed **the two-loop residual,
both one-loop skeletons, and half the zero-loop atlas** — everything it
touched reached a terminal composition node with an explicit falsifier. The
q-weld compilers are doing what the Vieta compiler did for the two-loop
phase: collapsing each new skeleton to two scalar conditions before any
cell-by-cell work starts, which is why one-loop 442 took 38 nodes but
one-loop 433 took only 9. If the pattern holds, zero-loop finishes in days,
and the real question becomes the positive-parity sector's size.
