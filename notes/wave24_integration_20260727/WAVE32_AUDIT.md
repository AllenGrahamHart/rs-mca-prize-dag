# Wave-32 audit — the payoff ladder lands, the compute budget runs out, and a new lane opens

**Date:** 2026-07-29. **Planner:** Fable. **Range:** `1b3ba1aa..9ba43bda`
(**125 commits**, 18:09 07-28 – 08:40 07-29). **Verdict: CLEAN — integrated in
full.**

```text
math orbit  241 = 179/38/24   ->   241 = 179/38/24   (unchanged)
nodes 1384 -> 1446 (+62)      edges 3622 -> 3777 (+155)
```

62 new nodes, **all PROVED**, **69/69 verifier runs PASS**, zero status changes.
All background; all outbound edges `ev`. Two phases: five more E1 cofactor
exclusions, then a new 57-node lane.

## My wave-31 question came back answered

I closed the last audit asking how much of the square-mass range must actually
be cleared — "stated nowhere, and that is the number worth asking for next."
Codex built it: `notes/E1_PROFILE_WEIGHT_PAYOFF_LADDER.md`.

**271 eligible profiles** after the proved prize norm floors, sorted by weight,
each row giving the sufficient total-vector cap that closing everything above
it buys:

```text
(4,2,18)  ->  69,541      (already proved empty)
(3,6,18)  ->  93,962
(2,10,18) -> 106,111        ... through all five S=18 profiles ...
(0,18,18) -> 116,577
(4,4,20)  -> 249,314        S=20 begins
(4,6,22)  -> 835,591
```

**I verified all twelve rows exactly.** Each cap is `floor(2E/M)` and sharp on
both sides — `M*cap <= 2E < M*(cap+1)` — with
`E = 65127585921474870475467050631501738502567`. Zero mismatches, weights
strictly decreasing.

That verification mattered more than usual, for the next reason.

## Codex has exhausted its compute budget

The ladder note carries its own honest caveat:

> its committed Python replay has not run because Modal is disabled. The
> one-container replay was attempted on 2026-07-28 and rejected before
> container creation with `Workspace ... has exceeded its spend limit`.

Five `notes/E1_*` draft documents now carry that marker. **The discipline held:
every one of them is a draft note outside the DAG, not a node.** No status
depends on unreplayed compute, and all 69 shipped verifiers run locally and
pass.

This is the operational fact of the wave, and it explains the pivot: the
overnight work moved to a lane that needs no Modal at all.

**What I could do about it:** the ladder is pure integer arithmetic, so I
replayed it here with no compute. It is now checked even though Codex could not
check it.

## The new lane: 57 nodes on Mersenne HNF colored Frobenius

`l1_mersenne_hnf_*` — chamber-by-chamber exclusion of colored Frobenius
interpolants (quadratic, cubic three-double, three-two-one, Galois role welds,
J-zero charts, singular quartics). It feeds **`l1_mixed_petal_amplification`**,
a *critical* TARGET, by 57 `ev` edges.

It has a genuine finiteness bound, which the old variance descent lacked:

> the pointwise equations define plane curves of degrees `d` and `d+1` with no
> common component, so `H <= d(d+1)`. Thus `h=7` starts at degree two and
> `h=15` starts at degree four; the `h=15` cubic chamber is empty.

So the search is bounded by a degree barrier rather than running open-ended.
That is the right shape.

**But it has no stated payoff.** The E1 lane now has a ladder saying exactly
what each closure buys against its consumer's budget. The `h7` lane has 57
PROVED chambers and no statement connecting them to
`l1_mixed_petal_amplification`'s two named closure routes (Toeplitz prefix
flatness, or aggregate local first-owner payment). This is precisely the gap I
raised for E1 at wave 31, in a new lane, and it is worth asking the same
question before it grows to 74 nodes: **what is the h7 payoff ladder?**

## Codex harvested our work — first time at this scale

The patch tried to re-apply, into our own tree, our own: WAVE27–31 audit notes,
`OPUS5_WORKER_GOAL.md` (including the hard-law-5 fifth surface added
2026-07-28), `tools/auto_discharge.py` with `vacate_orphan_artifacts` and the
canonical-write fix, the hard-law-8 comment in
`verify_unsafe_crossing_status_regression.py`, and the result.md pointer
paragraph verbatim. Codex has also **deleted the eight stale auto-discharge
artifacts** I vacated in wave 27 — they are absent from its HEAD.

Thirteen paths were excluded from the merge on that basis: our own work
returning, plus deletions already performed on our side. Verified after the
merge that all of it is still intact and that the vacated artifacts stayed
vacated.

The useful consequence: the two trees are now converging rather than diverging,
which should reduce merge friction from here.

## One thing I could not reproduce

The ladder states **271 eligible profiles**. I could not reproduce that count.
My nearest reading — `18 <= S <= 2*ell = 66`, `b >= 2` even, `H = 2a+b <= 2T`
with `T = min(ell, 2h-ell) = 33` — gives **269**; allowing `b = 0` gives 281.
The gap is two profiles, so it is almost certainly a boundary convention I do
not have rather than an error, and the ladder's load-bearing arithmetic (the
caps) verified exactly regardless. Recorded as a question for the lane owner,
not as a defect.

## Assessment

Tenth wave, still **zero red closures**, board unchanged. But two things in this
wave are worth more than the count.

First, the loop is working in both directions now: I asked for a number at the
end of wave 31, Codex produced it four hours later, and I was able to verify it
precisely because it is cheap arithmetic — at a moment when Codex itself could
not run the check.

Second, the constraint has changed shape. For nine waves the limit was
mathematical. This wave it is **budgetary**: the E1 lane is blocked on Modal
spend, and the overnight output went where compute is free. That is worth
knowing before reading the next wave's node count as progress — 57 of the 62
new nodes are in a lane that was chosen partly because it is cheap, and whose
connection to its critical consumer is not yet stated.
