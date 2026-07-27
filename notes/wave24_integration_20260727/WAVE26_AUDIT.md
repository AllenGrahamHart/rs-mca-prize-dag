# Wave-26 audit — Codex closes `averaged_xr`, and demotes its own consumer

**Date:** 2026-07-27. **Planner:** Fable. **Range:** `0124bcb9..bccddbcc`
(14 commits, 09:41–12:28). **Verdict: CLEAN — integrated in full.**

**The headline: the false green I demoted this morning is now genuinely
proved — and Codex reached that by a completely different route, while
demoting the node above it.**

```text
math orbit  241 = 177/39/25   ->   241 = 179/38/24
```

**The board is back to 24 open targets** — but not by reversing this morning's
correction. The correction stands; the claim was re-earned.

## `averaged_xr`: TARGET -> PROVED, honestly

Codex's `status_ruling.md` opens by conceding the demotion:

> "The 2026-07-27 demotion was correct for the former auto-proof: it cited a
> nonexistent conditional packet and used an exponent dictionary as though it
> proved de-correlation."

The new closure shares nothing with that argument. Codex found that **Przemek's
repository already contained the exact theorem** —
`experimental/notes/m1/m1_average_support_collinearity.md` plus the occupancy
consumer `m1_averaged_slope_conversion.md`, both at upstream commit
`674503f7` — rederived it locally, and shipped an independent
interpolation-matrix verifier.

**The mathematics, checked:** the joint-rank computation is correct.
For supports `S,T` of size `s = k+t` with `c = |S cap T|` and `d = s-c`:

- `c < k`: the `c` agreement equations on `(P,Q)` are independent by
  Vandermonde, kernel dimension `2k-c`, and `|S union T| = 2(k+t)-c`, so the
  combined rank is `2t`.
- `c >= k`: `P-Q` has at least `k` roots and degree `< k`, so `P = Q`; kernel
  dimension `k`, combined rank `2(k+t)-c-k = t+d`.
- `c < k` iff `d > t`, and `c >= k` iff `d <= t`, so both cases are
  `rank(Pi_S, Pi_T) = t + min(d,t)`.

The fixed-slope probability then follows from the invertible change
`U = f+zg, V = g` and inclusion-exclusion. `verify.py` PASSES with
**3,740 mutation kills** across 9,047 rank pairs and 19,530 occupancy vectors.

**Scope is fenced by Codex itself:** "PROVED only for the exact fixed-slope
pair moment stated here. The wider worst-case XR claims remain outside this
closure."

## `xr_gvn`: CONDITIONAL -> TARGET — the discipline that matters

Proving the parent did **not** auto-green the child. Codex's ruling:

> "The former conditional packet treated the exact `k=2` fixed-slope moment as
> though it supplied a defined multi-exchange Cauchy--Schwarz chain and
> endpoint inequality. It does not. The edge from `averaged_xr` is
> evidence-only, and the broader generalized von Neumann statement is restored
> to `TARGET`."

I retyped that edge `req -> ev` on merge, per the red-leaf law and Codex's own
ruling. This is the exact failure mode that produced the e1 cascade — a node
consuming more than its parent supplies — caught here by the worker itself,
in the direction that costs it a green.

Net on the target count: `averaged_xr` closes (-1), `xr_gvn` opens (+1), and
the two cascade nodes (`averaged_slope_conversion`,
`averaged_occupancy_clean_anchor_first_moment_route_cut`) return to PROVED.

## Five new nodes, all verified

`f3_hge4_multiscale_haar_m128_frontier`,
`integer_code_distance_high_field_folded_box_exclusion`, and three Mersenne HNF
nodes (`m16_order_zero_reciprocal_elimination`,
`order_one_involution_component_exclusion`,
`order_one_newton_reciprocal_reduction`). All six shipped verifiers PASS. The
batch also contains two **falsifications** — the m128 joint-product route and
the m128 energy-only close — which are route kills, i.e. search space removed.

## Integrated

4 status changes + 5 nodes + 15 edges, folders synced, one edge retyped to
satisfy the red-leaf law. All six repo validators PASS; manifest refreshed
(1202 scripts). Pins widened per hard law 8 with dated justification.

## Assessment

Two waves in a row where the worker's output is better disciplined than the
historical material we spent the morning unwinding. More pointedly: Codex
**checked upstream before claiming**, found the theorem already existed,
attributed it, and rescoped its own consumer downward in the same commit
range. That is the behaviour the re-graded surface needs.
