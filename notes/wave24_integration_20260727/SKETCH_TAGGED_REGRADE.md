# The two SKETCH-tagged nodes, adjudicated

**Date:** 2026-07-27. **Planner:** Fable. Both were flagged in
`STATEMENT_REMEDIATION.md` as carrying the `zone_b` signature — a PROVED node
citing a SKETCH-tagged section. **They resolved in opposite directions.**

---

## `acl_count` — PROVED stands; the reference was mis-pointed

Its ref pointed at `proof_sketch/s3b_iii_3_fibers_and_noanchor.md#2`
(`[textually grounded SKETCH]`, on the Conjecture F unification), which does not
state the node's claim. The **real source is `thm:exactcount`** (Exact slope
count) in `archived/slackMCA_v3.tex` upstream — a genuine theorem with a closed
form:

```text
A(N',l') = sum_{u>=0, t=l'-2u>=0, u<=n_1-t} binom(n_1,t) 2^t     (n_1 = N'/2)
B(p) = A(N',l')  for every prime in the stable range
     = (3^{n/(2 sigma)} - 1)/2  at rho = 1/2
```

**Scope fence (load-bearing, now written into the statement):** exactness holds
only ABOVE the quotient norm threshold `p > (2 l')^{N'/2}`. At `log2 q = 256`,
`rho = 1/2` that is `N' <= 80` — precisely **zone (a)** of
`s2_paid_ledger.md#3`, the PROVED-exact zone. The range `80 < N' < ~512` is
zone (b), explicitly CONJECTURAL there and carried by the separate node
`zone_b` (already CONDITIONAL). The consumers are consistent with this:
`paid_quot_fn` states an interval-valued column and explicitly disclaims a
point-valued zone-(b) conclusion.

**Verdict: PROVED, scope-fenced, ref re-pointed.** Not an over-claim — a
citation defect.

---

## `averaged_xr` — FALSE GREEN, demoted to TARGET

Three independent reasons, any one sufficient:

1. **There is no `conditional.md`.** The folder holds only `notes/`,
   `proof.md`, `sketch.md`, `statement.md`. Yet `proof.md` reads *"The
   conditional implication (see conditional.md) is proved and every predicate is
   now green."* There is no implication to invoke.
2. **The sole req-predicate presupposes the claim.**
   `xr_ledger_exponent_reconciliation` reads: *"Reconcile **averaged_xr's
   stated** shell exponent `q^{-min(s,t)}` with the proved ledger's
   `c(s,t) = min(s,t-1)` ..."* — a consistency check **about** this node, which
   cannot prove it. (It is now correctly re-typed as an `ev` edge, satisfying
   the red-leaf law.)
3. **Both self-reports say otherwise.** The node's own `sketch.md` records
   status **PROVABLE**, and the upstream source
   (`s3b_iii_2_displacement_spectral.md#5`, `[SKETCH]`) says only that the
   averaged form *"LOOKS PROVABLE with current tools"*, explicitly leaving
   worst-case de-correlation as the wall.

**Attack recorded:** the Hooley-Katz / Scott exponential-sum lane named in that
section. **Falsifier:** a shell where the reconciled exponent `c(s,t)` breaks
the variance control the conversion needs.

### Cascade (all propagation, each recorded in-statement)

| node | change | reason |
|---|---|---|
| `averaged_xr` | PROVED -> **TARGET** | false green (above) |
| `averaged_slope_conversion` | PROVED -> **CONDITIONAL** | its proof explicitly relies on `averaged_xr` to "supply the slope-resolved second moment"; `fm1` remains PROVED |
| `xr_gvn` | PROVED -> **CONDITIONAL** | req on `averaged_xr` |
| `averaged_occupancy_clean_anchor_first_moment_route_cut` | PROVED -> **CONDITIONAL** | req on `averaged_slope_conversion` |
| `xr_inverse` | PROVABLE -> **CONDITIONAL** | req on `xr_gvn` |
| `xr_ledger_exponent_reconciliation` | folder moved to `background/` | left the critical path when `averaged_xr` became a red leaf |

This **independently corroborates Opus's session-7j finding** on
`averaged_slope_conversion` — reached there via scope drift (post-paid support
families consumed at row level), reached here via a false predicate. Two
different routes, same node.

Everything downstream (`unsafe_at_crossing`, `mca_unsafe`, `mca_grand`) was
already CONDITIONAL from wave-24, so the cascade stops cleanly.

---

## Re-pricing

```text
math orbit  242 = 180/38/24   ->   241 = 177/39/25
submission  257 = 192/40/25   ->   256 = 189/41/26
```

**The board is 25 open targets.** All pins widened per hard law 8 with dated
justification, including Codex's `verify_unsafe_crossing_status_regression`
assert on the occupancy route cut (widened to accept CONDITIONAL, not deleted).
