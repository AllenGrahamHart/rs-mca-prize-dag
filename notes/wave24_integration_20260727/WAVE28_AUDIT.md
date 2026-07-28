# Wave-28 audit — the route boundary held, and Codex went around it

**Date:** 2026-07-27. **Planner:** Fable. **Range:** `e2a5fab2..52d61e6f`
(6 commits, 16:55–19:14). **Verdict: CLEAN — integrated in full.**

```text
math orbit  241 = 179/38/24   ->   241 = 179/38/24   (unchanged)
nodes 1291 -> 1302 (+11)      edges 3149 -> 3205 (+56)
```

Eleven new PROVED nodes, **zero status changes, zero red closures** — the
sixth consecutive wave with that shape. All eleven are in `background/`; both
critical consumers (`unsafe_crossing_family_instantiation`,
`e1_official_prime_exception_control`) remain `TARGET`. All 22 verifier runs
PASS.

The descent continued: **`V=64` closed, `V=62` closed**, and `V=60` is most of
the way there (parity reduction + three-profile quotient exclusion + two-odd
exclusion + the `(4,2,2)` exclusion).

## The route boundary passed an out-of-sample test

Yesterday's audit derived, and PR #1110 shipped, the claim that the
cubic-Hermite exclusion threshold is affine in `V`. That formula was **fitted
to three points** (`V = 68, 66, 64`). Wave 28 produced two more, computed by
Codex independently and afterwards:

```text
V=68 -> 1947   [fitted]        V=66 -> 1732   [fitted]
V=64 -> 1517   [fitted]
V=62 -> 1302   [OUT-OF-SAMPLE, exact match]
V=60 -> 1087   [OUT-OF-SAMPLE, exact match]
```

Both new thresholds are exactly what the affine law predicts. The structural
argument (all three moments affine in `(V, M_3)` against a fixed basis) is
therefore confirmed by data it was not fitted to. Five levels remain where the
majorant has a positive threshold — `V = 58, 56, 54, 52, 50` — and `V <= 48` is
dead, as PR #1110 states.

## But the prediction about *what happens next* was wrong

I wrote that if the descent continued below `V ~ 50` it would "have to be on
emptiness grounds rather than norm-majorant grounds." Codex found a different
escape, and started using it **before** reaching the boundary:

**Exact norm evaluation.** Rather than bound `M_3` and infer the norm, compute
the resultant norm outright and compare it to `2^250` directly. Two independent
engines — FLINT and PARI — with the majorant retained only to *triage* the bulk:

- `e32_profile_47_exact_norm_exclusion` (`V=64`): all 2,937,494,528
  representative vectors enumerated, 60,148 full-conductor survivors, exact
  247-bit maximum norm, `15*N_max < 2^250`.
- `e30_two_odd_profile_exclusion` (`V=60`): the `M_3=1087` cutoff clears the
  3,572 full-conductor `(1,5,1)` vectors; the 28,114 `(2,7)` vectors that it
  cannot clear are killed by exact resultant censuses instead.
- `e30_profile_422_exclusion` (`V=60`): the majorant leaves exactly **three**
  assignments above `M_3=1087`; two actual-vector engines reduce those to six
  vectors, four of proper conductor, and FLINT/PARI put both remaining
  primitive norms below threshold.

That last one is the pattern in miniature, and it is a good pattern: use the
cheap majorant everywhere it works, pay exact arithmetic only on the residue.
It is not bound by the route cut, because it never uses the majorant's
inequality.

**PR #1110 is still correct** — it claims the majorant expires, not that the
band is unreachable, and it explicitly says the cut is tool-relative. But its
"escape hatch" paragraph names only emptiness arguments. The demonstrated
escape is exact-norm evaluation. That is worth adding.

## The new thing to watch: exact-norm headroom is thin

The exact route has its own frontier, and the margins are already small:

```text
V=64  profile (4,7)          15 * N_max < 2^250          ~3.9 bits headroom
V=60  profiles (2,7),(1,5,1)  7 * N_max < 2^250 < 8*N_max ~2.8 bits headroom
V=60  profile (4,2,2)        447 * N_max < 2^250          ~8.8 bits headroom
```

A factor of **7** below `2^250` is razor-thin. These are exact maxima, not
bounds, so there is no slack to recover by sharpening. If some level produces
`N_max > 2^250`, that level does not close — and unlike a majorant failure,
that outcome is not a tooling artifact: it would be a genuine surviving
candidate.

I am explicitly **not** extrapolating a second horizon from three points across
different profiles; the norms are profile-dependent and the trend is not clean.
The honest statement is: the binding constraint has moved from the majorant's
threshold to the exact norm's headroom, and the headroom is now single-digit
multiplicative.

## Verification

- 22 verifier runs (11 nodes x `verify` + `verify_audit`): all PASS.
- Every new node in `background/`; partition law holds (`verify_prize_dag`).
- Both critical consumers still `TARGET`; no auto-discharge fired.
- All six validators PASS; canonical round-trip OK.
- My wave-27 tooling fixes (`vacate_orphan_artifacts`, canonical write,
  restored hard-law-8 comment) were untouched by this wave — checked before
  applying, since Codex has not merged our wave-27 commit.

## Assessment

The best wave yet on the discipline axis: exact two-engine arithmetic, the
majorant used only where it is cheap and sound, and honest reporting of the
margins including the near-misses (`7*N_max < 2^250 < 8*N_max` is stated with
both sides).

The strategic reading from wave 27 is unchanged and now better evidenced. Six
waves, zero red closures. The descent is 4 levels further along and has
consumed another ~5 billion census vectors plus exact resultant work, and the
band still has `0 < V <= 60` to clear before `(4,2,0)` and the swap bands are
touched at all. What wave 28 adds is that the *cost per level is rising* — the
cheap tool is being replaced by exact arithmetic on residues, with headroom now
measured in single-digit factors.
