# Wave-34 audit — the m2 grind, and a retraction done exactly right

**Date:** 2026-07-30. **Planner:** Fable. **Range:** `f69c6fdc..181c77e4`
(73 commits, 08:xx–19:49). **Verdict: CLEAN — integrated in full.**

```text
math orbit  241 = 179/38/24   ->   241 = 179/38/24   (unchanged)
nodes 1531 -> 1559 (+28)      edges 4059 -> 4140 (+81)
```

28 new PROVED nodes, zero status changes, all background, 27 of 28 feeding
`rate_half_band_closure` by `ev`. **57/57 batch verifier runs PASS**, plus a
separate clean-worktree run for the one node whose working-tree copy had
uncommitted successor edits (below).

## The work: descending the m2 decomposition branch

The wave grinds the `m=2` inner-degree branch left by wave 33: diagonal rows
(202 deleted, 112 classified), the saturated-112 colored-divisor descent, and
a q-slice campaign that reduced the aligned positive slices to twelve exact
ideals and closed the first deployed near-slice chart. Method is exact
commutative algebra — resultants, grevlex bases, colored divisors — with
helpers bound by SHA-256 into the node verifiers.

## The retraction (`a9761aa7`) — audited closely, and it is exemplary

Mid-campaign, Codex retracted its own "near q-slice elimination". The bug is
a classic sympy trap: `Poly(...).coeff_monomial(b)` returns the coefficient
of the exact monomial `b*c^0*d^0`, NOT the full coefficient of `b` — so the
helper substituted spurious constants `b=3`/`b=-1` instead of the rational
function from the endpoint line. What makes it exemplary:

- the invalid eliminants and survivor bases are **named and retracted with
  hashes**, and their replay timings explicitly disclaimed as evidence;
- what SURVIVES is stated (`c=1`, `cd=1`, `5cd-4c-4d+5=0` remain valid);
- the chart was demoted to "must be classified from scratch before this
  chart can be promoted";
- the corrected helper (full coefficient by differentiating in `b`) is
  identified by SHA, and only then was the chart re-closed (`181c77e4`);
- **none of the invalid material ever became a DAG node** — 0 removals and 0
  status changes across the whole wave because the error was caught at the
  notes stage, before minting.

I verified the re-closed chart from the COMMITTED tree, not the working
tree: Codex's working copy carries uncommitted successor edits (a new helper
hash and an extra CLI argument — the next chart in progress), so the batch
run for that node was not probative of HEAD. A clean worktree at `181c77e4`
gives `..._DIRECT_PASS` and `..._AUDIT_PASS`, each with a mutation catch,
and the committed verify binds the committed helper hash and contains none
of the retracted constants.

## Merge notes

Only `dag.json` conflicted — ours is canonical after the wave-33
renormalization, Codex's is still not (the mis-indent persists in its tree).
Took Codex's HEAD dag and renormalized again. The nag stands: **Codex should
re-run its canonical writer**; until then every wave pays this one-step tax.

## Assessment

Twelfth wave, zero red closures, board unchanged — the m2 branch is a grind
and nobody should pretend otherwise. What this wave actually banks is trust
calibration: an agent that catches its own subtly-wrong computer algebra,
retracts loudly with hashes, preserves exactly what survives, and re-closes
only under a corrected, hash-bound helper is an agent whose 28 green nodes
mean something. The near-slice queue continues; the `2+2+2` frontier and the
remaining inner degrees `{3,4,6,10,12}` sit behind it.
