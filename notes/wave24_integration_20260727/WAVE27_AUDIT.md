# Wave-27 audit — the E1 variance descent, and the horizon it is running into

**Date:** 2026-07-27. **Planner:** Fable. **Range:** `7f54beaa..e2a5fab2`
(34 Codex commits, 12:48–16:47). **Verdict: CLEAN — integrated in full.**
**Two tool defects found and fixed; one route-level finding recorded.**

```text
math orbit  241 = 179/38/24   ->   241 = 179/38/24   (unchanged)
nodes 1272 -> 1291 (+19)      edges 3049 -> 3150 (+101)
```

Nineteen new PROVED nodes, **zero status changes, zero red closures.** Every
new node is in `background/` and reaches the critical tree only by `ev`
edges. Both critical consumers — `unsafe_crossing_family_instantiation` and
`e1_official_prime_exception_control` — remain `TARGET`. Nothing was inflated.

## What the campaign proves

A descending exhaustion of the autocorrelation variance for the `N=256`,
folded-profile `(3,4,0)` band (`s16` = square mass `3*2^2 + 4*1^2 = 16`;
the band index `s=5` is a different parameter — I checked, there is no scope
mismatch with the `s=5` conductor theorem it consumes).

- **`V=68` closed.** Slack recurrence → 24 profiles → cubic threshold `M_3=1947`
  → 3 profiles → chord parity → the single profile `(6,7)` → four heavy-position
  templates → four census exclusions (`M_3 = 1188, 1560, 1722, 1770 < 1947`).
- **`V=66` closed.** 21 profiles → threshold `1732` + parity → 4 profiles →
  four exclusions (`1644`, `1356`, `≤1732/1670`, `1416`).
- **`V=64` opened.** 18 profiles → threshold `1517` + parity → 3 profiles;
  `(0,8)` already excluded. Two remain.

Residual for this profile: **positive even `V <= 64`**, and the result note
says so plainly, together with "`(4,2,0)` and the later swap bands remain
open, so the universal target remains unproved."

## Verification

- **38 verifier runs (19 nodes × `verify.py` + `verify_audit.py`): all PASS.**
- I recomputed the four-template partition independently:
  `C(128,3) = 341376 = 128 + 7936 + 7936 + 325376` — quarter (32 quadruples × 4),
  diameter (64 antipodal pairs × 124 non-quarter thirds), progression
  (128 × 62 steps), generic by subtraction. Exact match to the verifier.
- I recomputed every profile's energy: `sum_i i^2 n_i` equals the claimed `E`
  for all ten profiles across `V = 68, 66, 64`.
- The four-template case split is exhaustive on paper: diameter present
  (third point quarter / not) or absent (three lengths distinct / exactly two
  equal; all three equal is impossible since `Z/128Z` has no element of order 3).
- The one near-miss is handled honestly. The `(5,7)` census maximum is
  `M_3=1758`, **above** the `1732` threshold; the proof names the maximizer
  `(36,48,60,0,4,24,64)`, computes its conductor `4`, cites the proved
  proper-conductor exclusion, and reports the full-conductor maximum `1416`.
  The `req` edge to that theorem exists in the DAG.

## The finding: this route has an analytic horizon at `V ~ 50`

The cubic-Hermite certificate tests a fixed, **`V`-independent** Hermite basis
against moments `m1 = 16`, `m2 = 256 + V`, `m3 = 4096 + 48V + M_3`. Every
ingredient is affine in `(V, M_3)`, so the exclusion threshold is exactly
linear in `V`. I reconstructed the certificate from the shipped basis and
recovered all three thresholds **exactly**:

```text
V=68 -> 1947 (shipped 1947)     V=66 -> 1732 (shipped 1732)
V=64 -> 1517 (shipped 1517)     threshold(V) = 107.5*V - 5363
```

Extrapolating the same certificate:

```text
V=62:1302  V=60:1087  V=58: 872  V=56: 658
V=54: 443  V=52: 228  V=50:  13  V=48: -202  (nonpositive from here down)
```

**At `V <= 48` the threshold is negative and the certificate excludes nothing.**
That is a property of the tool, not of the mathematics — but the tool has
carried 8 of the 9 exclusions so far, and those census maxima run `1188`–`1770`
against thresholds `1732`–`1947` (margins of 5–39%). For the descent to reach
`V=52` the census maxima would have to fall below `228`. Nothing in the last
three levels suggests they fall that fast.

Two things sharpen this:

- **32 endpoints remain** for `(3,4,0)` alone (`V = 2,4,...,64`), before
  `(4,2,0)` and the swap bands are touched at all.
- **There is a certified full-conductor `(3,4,0)` vector at `V=36`** — the
  proper-conductor node cites it precisely to show low variance does not force
  proper conductor. At `V=36` the cubic threshold is `-1491`, so *neither* of
  the campaign's two disposal tools reaches it. This is not a counterexample to
  the target; it is a witness that the current toolkit stops short of it.

**The one encouraging counter-signal:** the newest node, the `(0,8)` exclusion
at `V=64`, excludes by retaining **zero** census vectors — a geometric
emptiness, independent of the threshold. Arguments of that shape are not bound
by the horizon. If the descent is to continue below `V~50`, it will have to be
on emptiness/parity grounds rather than norm-majorant grounds.

This is consistent with — and sharpens — Codex's own r3 roadmap meta-datum,
which this wave confirms for a fifth time: *"four consecutive waves, +195
nodes, +709 edges, ZERO red closures. Reduction is exhausted; every remaining
leaf is priced at full cost."*

## Codex caught a false-green residue in OUR tree

The incoming diff deletes `critical/nodes/mca_unsafe/proof.md`. That file read
"By modus ponens the statement is PROVED", citing `zone_b [PROVED]` and
`unsafe_at_crossing [PROVED]` — both demoted to `CONDITIONAL` in this morning's
audit, while `mca_unsafe` itself was already `CONDITIONAL`. The artifact
contradicted its own node. Correct deletion, and a good catch: it survived my
own sweep this morning.

Codex also shipped the systematic fix — `regress_to_fixpoint` in
`tools/auto_discharge.py`, which demotes a stale auto-discharge and removes its
artifact. **That closes the tooling hole, not just the datum.**

I swept for the same residue and found **9 stale auto-discharge artifacts**,
so I extended the fix in two places:

1. **`vacate_orphan_artifacts` (new).** `regress_to_fixpoint` only inspects
   nodes whose status is in `GREEN = {PROVED, PROVABLE}`, so it catches a node
   *as* it is demoted but never one that some other route already demoted.
   Eight `proof.md` and one `sketch.md` were in exactly that state — including
   one on a `TARGET` node, and `xr_inverse`'s sketch citing an `xr_gvn` that
   wave 26 demoted. The new pass uses the *same rule the validator enforces*,
   so writer and checker cannot drift apart. All 9 vacated;
   `verify_auto_discharge_paths.py` went from FAIL to PASS.
2. **Canonical-form defect (pre-existing, ours).** `auto_discharge.py` wrote
   `json.dump(..., indent=1)`, which omits the trailing newline — so *every*
   run left `dag.json` one byte off canonical form and dirtied the next commit's
   diff. It now writes `json.dumps(..., indent=1, ensure_ascii=True) + "\n"`
   through a round-trip assert and an atomic `os.replace`.

## Merge-law application

Codex dropped my dated hard-law-8 comment from
`verify_unsafe_crossing_status_regression.py` while keeping the widened
assertion. Per the WAVE-MERGE LAW (rebase on Codex, re-append our reason) I
restored it, noting that wave 26 re-earned `averaged_xr` by an independent
route but that the widening stands on its own terms.

Census pins came in already updated to `241 = 179/38/24` and submission
`256 = 191/40/25`; both verify against the merged DAG.

## Assessment

Third consecutive disciplined wave. The mathematics is correct, the
verification is genuinely independent (two engines per census, mutation
controls throughout), the fencing is explicit, and the worker again caught a
defect in the planner's tree rather than the other way round.

The concern is not correctness but **direction**. This wave spent 34 commits
and roughly 5.9 billion census vectors to move one band's variance frontier
from `V<=68` to `V<=64`, on a route whose own certificate provably expires
around `V=50`, with 32 endpoints to go and a known exhibit sitting past the
expiry. That is the "sweeping vs paying" wall the r3 roadmap names, met head-on.
**Recommend: pose the horizon to Codex explicitly** and ask for either an
emptiness-style argument that survives below `V~50`, or a decision to stop the
descent and spend the compute on one of the three unifying-lemma legs.
