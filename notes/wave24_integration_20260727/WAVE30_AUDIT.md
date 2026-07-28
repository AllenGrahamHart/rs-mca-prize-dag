# Wave-30 audit — the node worked: Codex corrected me twice and changed direction

**Date:** 2026-07-28. **Planner:** Fable. **Range:** `8f211958..52666c2d`
(13 commits, 09:12–12:33). **Verdict: CLEAN — integrated in full.**

```text
math orbit  241 = 179/38/24   ->   241 = 179/38/24   (unchanged)
nodes 1343 -> 1365 (+22)      edges 3421 -> 3536 (+115)
```

22 new nodes, **39/39 verifier runs PASS**, no status changes on existing
nodes. Two of the new nodes are minted `TARGET` (both background, so the census
holds). This is the wave where the scope question I posed at `0acf7e8f` came
back answered — and where two of my own claims were corrected.

## Codex audited my node and caught a real over-claim

`e1_collision_square_mass_reparametrization` came back with Codex's own
`statement.md`, `proof.md`, `verify.py`, `audit.md`, `result.md` and a
`source_pin.json` pinning my commits `0acf7e8f` and `c90a724b` by SHA. Its
audit reads:

> The precursor's claim that `s` is unbounded at fixed quotient order is false:
> only `h` antipodal positions exist. This packet replaces it by the exact
> class-support bounds `H<=2T` and `S<=4T`.

**That is correct and I accept it.** My node said "unbounded `s`". At fixed
`N` there are only `h` antipodal positions, so `s` is finite — `S<=260` for
`N=256,ell=65` and `S<=132` for `N=256,ell=33`. What I could defend is the
weaker sentence I also wrote — *no norm bound can bound `s` above* — but I
stated the strong form as well, and it is wrong. Codex's replacement drops it.

**Codex also supplied the input I said was missing.** My `frontier.md` asked
for an upper bound on the `l_1` height and recorded "we looked for `ell'` and
did not find it pinned for this lane". It is pinned — via `acl_count` and the
clean-anchor rows. That is the bound that makes the square-mass range finite.

**The core finding survived.** Codex's `result.md`: "All three additional
`N=256,S=16` splits `(2,8)`, `(1,12)`, and `(0,16)` are realized by
official-size class pairs and survive the current norm test." And its audit:
the class-size parameter "bounds the global range but does not eliminate any of
the extra `S=16` splits."

## The second correction is the one that matters

I framed the conversion lemma as *prove `P = 0` by exhaustion*. Codex's
frontier:

> The universal consumer asks for the aggregate collision allowance
> `P<=K-B*-1`; it does not require every profile to be collision-free.

That is right and my framing was over-strict. `P` is a **budget**, not a
vanishing requirement. Exhausting profiles to emptiness is sufficient but far
from necessary, and insisting on it made the remaining work look larger than it
is. This is a better reading of the target than the one I gave.

## Consequence: the descent is paused, and a two-line argument beats it

`e1_prize_field_floor_even_norm_exclusion` (PROVED). On prize-envelope rows the
field floor is `p>2^255`, not the coarse `2^250`. At `S=16`, `N=256`:

```text
|Norm(alpha)| <= S^(h/2) = 16^64 = 2^256   exactly
p > 2^255  =>  2p > 2^256 >= |Norm|  =>  |Norm| < 2p
p | Norm, Norm != 0  =>  |Norm| = p
```

and every same-size class-difference norm is **even** while `p` is odd —
contradiction. Same at `N=512, S<=4` (`4^128 = 2^256`). So the prize-row floors
sharpen to `S>=18` and `S>=6`.

I checked this in exact integers. `16^64` and `4^128` are `2^256` on the nose,
so the argument turns on the strictness of `p>2^255`; Codex's audit flags
exactly that ("equality `R=2^256` is harmless because `p>2^255`"). The parity
leg it derives from equal class size rather than from a profile assumption,
which is cleaner than the route through `b` even that I checked it by.

**Scope, stated carefully:** this kills `S=16` on **prize-envelope** rows only.
RowC keeps the `2^250` floor and is explicitly unchanged, so the 74-node
`(3,4)` descent remains load-bearing there. It is a partial supersession, not a
retraction — and Codex says so itself.

Codex has accordingly **paused the per-endpoint descent** and started `S=18`
(`e1_prize_n256_s18_variance_cofactor_windows`), after closing `V=34` down to
`V=26` at `S=16`.

## The new direction

Two PROVED compilers and two new `TARGET`s reformulate the problem as a
counting/colouring question aimed straight at the aggregate budget:

- `e1_low_square_mass_plotkin_coloring_compiler` — join same-value class pairs
  with `S<=2ell`; `c`-colourability bounds every fibre by `c(ell+1)` via the
  Euclidean Plotkin identity. Binding prize rate-1/8 cap: `chi<=3`.
- `e1_low_square_mass_weighted_kernel_dictionary` — an oriented kernel vector of
  profile `(a,b)` represents exactly `M_ell(a,b)` ordered class pairs, giving
  `E_low` exactly.
- `e1_official_low_square_mass_collision_coloring` [TARGET] and
  `e1_official_low_square_mass_pair_budget` [TARGET] — the two open asks.

This attacks `P<=K-B*-1` directly rather than profile-by-profile. It is the
right shape given the reframing above.

## Merge notes

Codex has not pulled our HEAD, so the base was the pin. Its `dag.json` is a
strict superset of ours — it carries both my node and my `s>=3 -> s>=2`
correction, which its audit explicitly credits — so I took it wholesale. Two
files conflicted because I had edited them: `result.md` (my pointer paragraph)
was rebased on Codex's and the pointer re-appended, updated to record that the
question is now answered. My version of the node folder was removed in favour
of Codex's.

## Assessment

The node did exactly what it was for. It was posed as a question, it got
audited by the worker, two of my claims were corrected — one factual, one
strategic and more important — the missing input was supplied, the core finding
was confirmed, and the campaign changed direction as a result. That is the
loop working.

Worth being plain about the ledger anyway: eight waves, still **zero red
closures**, board unchanged at `241 = 179/38/24`. What changed this wave is not
the count but the plan — a per-profile exhaustion that could not have reached
the target has been replaced by an aggregate-budget attack that can, and a
two-line field-floor argument removed the layer the previous 74 nodes were
grinding, on the rows that matter most.
