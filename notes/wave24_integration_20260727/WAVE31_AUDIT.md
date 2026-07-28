# Wave-31 audit — the pivot pays: one full S=18 profile closed by cofactor class

**Date:** 2026-07-28. **Planner:** Fable. **Range:** `52666c2d..1b3ba1aa`
(15 commits, 12:50–17:42). **Verdict: CLEAN — integrated in full.**

```text
math orbit  241 = 179/38/24   ->   241 = 179/38/24   (unchanged)
nodes 1365 -> 1384 (+19)      edges 3535 -> 3623 (+88)
```

19 new PROVED nodes, **19/19 verifier runs PASS**, no status changes. All in
the `S=18` layer. This is the first wave executed entirely under the new
aggregate-budget strategy, and the method changed with it.

## The method: cofactor classes, not variance endpoints

At `S=16` the field-floor argument forced `|Norm| = p` outright. At `S=18` that
collapses — `18^64 = 2^266.87` against `p > 2^255` — so the quotient
`m = |Norm|/p` is a small even integer rather than `1`. The new attack
enumerates the admissible `m` and kills each.

**I checked the enumeration independently.** From the norm bound alone,
`m < 18^64/2^255 = 3756`. An odd prime `q` dividing `Norm` contributes
`q^ord_256(q)`, so it can only appear if `q^ord_256(q) <= 3756`; sweeping all
odd primes below the cap leaves exactly `257`, `769`, `3329`, each `= 1 mod
256` with order `1`. With `Norm` even and `p` odd, `m = 2^v * odd`, giving

```text
admissible m (bound-only superset, 16 values):
  2 4 8 16 32 64 128 256 512 514 1024 1028 1538 2048 2056 3076
```

Every cofactor Codex names — `2, 4, 16, 256, 512, 514, 1024, 1028, 1538` — lies
in that set, and its per-profile lists are **strictly narrower** (7 classes on
`(4,2)`, 12 on `(3,6)`, with 2-adic valuation confined to
`{1,2,3,4,5,6,8,9,10}`, so `2^7` and `2^11` are cut by a sharper valuation
argument than my crude bound). Nothing is missing relative to the bound, and
Codex is ahead of it. That is the right direction for an exhaustiveness check
to come out.

## Why this is on-path, unlike the descent it replaced

`e1_prize_n256_s18_profile_exclusion`: the leading profile `(4,2,S=18)` is
**closed outright** — all seven cofactor classes excluded. And the consequence
is quantified against the open TARGET:

> Removing its zero contribution from the binding weighted ledger makes
> `(3,6,S=18)` the maximum-weight remaining profile and raises the sufficient
> oriented-vector cap from `69541` to `93962`.

That is the difference from the old descent in one sentence. Closing a profile
no longer just shrinks a residual — it **loosens the budget** in
`e1_official_low_square_mass_pair_budget`, moving a live TARGET's sufficient
condition. The aggregate-budget reframing from wave 30 is now doing visible
work.

`(3,6,S=18)` is the current front: twelve exact cofactors, with per-cofactor
variance windows from `V<=350` (cofactor 2) down to `V<=12` (cofactor 1538).
Those windows are tight, which is why the profile is being cleared cofactor by
cofactor rather than level by level.

## Verification

- 19/19 node verifiers PASS.
- Independent cofactor-superset check above.
- Exclusion method spot-checked: for each candidate `m`, the packets compute
  `Norm/m` and require it to fall **strictly outside** the prize prime
  interval, so it cannot be `p`. Dual streams (FLINT and PARI) agree through a
  64-bucket multiset fingerprint — the same two-engine discipline as the
  earlier censuses.
- All six repo validators PASS; canonical round-trip OK; board unchanged.

## Merge notes

Codex still has not pulled our HEAD, so the base is the pin. One conflict, as
last wave: `result.md`, where I hold a planner pointer. Rebased on Codex's
version and the pointer re-appended, refreshed to record that the two
consequences it flagged are now executed rather than proposed. Nothing else
collided; my tooling fixes and the `s>=2` correction are untouched and were
re-checked after the merge.

## Assessment

Ninth wave, still **zero red closures**, board unchanged at `241 = 179/38/24`.
But the shape of the work is now different in a way the census does not show.
Wave 29 spent thirteen levels and billions of vectors moving a residual inside
one profile that could not, by itself, reach the target. Wave 31 closed one
profile and *moved a number in the open TARGET's sufficient condition* —
`69541 -> 93962`. That is the first wave in this lane whose output is
denominated in the units the target actually asks for.

The honest caveat: `(3,6)` is the maximum-weight profile, so it is the
expensive one, and `(2,10)`, `(1,14)`, `(0,18)` sit behind it at `S=18` alone —
with `S=20` and upward behind that, bounded by `S<=132` on the binding row. The
budget framing means those need not all reach emptiness, only fit under the
allowance; how much of the range must actually be cleared is not yet stated
anywhere, and that is the number worth asking for next.
