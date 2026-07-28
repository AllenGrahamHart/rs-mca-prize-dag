# Wave-29 audit — thirteen levels in one night, and the route boundary vendored

**Date:** 2026-07-28. **Planner:** Fable. **Range:** `52d61e6f..8f211958`
(16 commits, 19:37–02:12). **Verdict: CLEAN — integrated in full.**
**One stale critical narrative found and repaired.**

```text
math orbit  241 = 179/38/24   ->   241 = 179/38/24   (unchanged)
nodes 1302 -> 1343 (+41)      edges 3204 -> 3422 (+218)
```

Forty-one new PROVED nodes, **zero status changes, zero red closures** —
seventh consecutive wave. All background; both critical consumers remain
`TARGET`. **82/82 verifier runs PASS.**

The descent went from `V=60` to `V=36` in a single night. The live positive
even frontier for folded profile `(3,4,0)` is now **`0<V<=34`**.

## The route boundary was vendored, and the provenance is exemplary

Commit `85cadcc1` imports upstream PR #1110 as the background node
`e1_first_band_variance_route_boundary`. I audited the import:

- `source_pin.json` pins the upstream repository, **PR number 1110**, and the
  exact head commit `52775686c8f181c08d36de66d3ce0d3b556f8d74` — which is my
  latest push, including the sufficiency caveat.
- All three upstream files are vendored bytewise under `upstream/rs-mca/…`
  with recorded sha256. I recomputed all three: **intact**, and byte-identical
  to my branch at that commit.
- The node statement restates the theorem correctly and keeps the fences:
  "decides no variance level and proves no collision exclusion … rules out only
  continued use of this fixed cubic-Hermite majorant below `V=50`."
- Edges are `ev`-only into both consumers. `UPSTREAM_IMPORT_LEDGER.md` records
  it with an explicit non-claim line.

This is the cleanest cross-repo import in the tree.

## The affine law now holds at ten levels, seven out-of-sample

Wave 29 shipped four more thresholds. Against my rigorous reconstruction:

```text
V:        68   66   64   62   60   58   56   54   52   50
shipped: 1947 1732 1517 1302 1087  872  658  443  228   13
mine:    1947 1732 1517 1302 1087  872  658  443  228   13   (0 mismatches)
naive:   1947 1732 1517 1302 1087  872  657  442  227   12   (4 mismatches)
```

Only `68, 66, 64` were fitted. The other **seven are out-of-sample**, and all
match. The "naive" row is the exact-`107.5` line through the first three
integers — it is wrong at four levels, which is why PR #1110 reports the slope
as the bracket `(107,108)` and pins each threshold two-sided rather than
publishing a closed formula. That judgement is now vindicated by data.

## Codex solved the constraint I flagged in wave 28

Wave 28's audit said the binding constraint had moved from the majorant's
threshold to exact-norm headroom, which was down to a factor of 7. At `V=36`
that constraint actually bit — **six whole norms reach `2^250`** — and Codex
got past it by **odd-part extraction**:

> write `R = 2^mu R_odd`; a pair-feasible row prime `p > 2^250` is odd, so
> `p | R` implies `p | R_odd`; every `R_odd` is below `2^250`.

I checked the argument and it is sound: row primes are odd, so the 2-part is
irrelevant to divisibility by `p`. The whole-norm test was simply the wrong
test, and the odd-part test is the right one.

## My PR #1110 claim about the `V=36` exhibit survives — and sharpens

I told upstream that the certified full-conductor `(3,4,0)` witness at `V=36`
"is a witness that these two tools together stop short of the bottom of the
band." Wave 29 closed `V=36`. That does **not** refute the claim — it confirms
it, because the closure needed a *third* tool. The `V=36` reduction node says
so in as many words: **"No cubic-Hermite cutoff is used."** The conductor
theorem likewise handles only the 3,718 proper-conductor vectors; the 2,994
full-conductor ones needed exact norms.

Codex also evaluated the witness itself. I recomputed it independently:

```text
norm      = 2 * R_odd,   249 bits
R_odd     = 248 bits, PRIME, congruent to 1 mod 256
R_odd < 2^250 by a factor of about 5  (2.34 bits)
```

**Correction to my own first reading of this:** I initially checked
`R_odd = 1 mod 2^41` and found it false, and briefly took that as a second
independent exclusion. That is the wrong modulus — `2^41` is the rate-1/2
family's condition, not this lane's. For `N=256` the row congruence is
`mod 256`, which Codex checked and which the witness **satisfies**. So the
witness is excluded by size alone, with about two bits to spare. The bottom of
this band is genuinely tight.

## Repair: the critical narrative was nine levels stale

`critical/nodes/unsafe_crossing_family_instantiation/result.md` at
`8f211958` ends its per-level narrative at `V=52` with "it is not yet closed",
while the DAG at the *same commit* closes `V=52` and every level down to
`V=36`. That is an under-report, not an over-claim — the safe direction — but
it left the critical node contradicting the background chain feeding it.

I appended a dated frontier addendum recording the nine closures, the live
frontier `0<V<=34`, the method change (exact resultants below `V=50`, odd-part
extraction at `V=36`), and the margin note above. It restates plainly that the
node is **not** closed: `(4,2,0)` and the swap bands are untouched.

## Verification

82/82 verifier runs PASS. Independently of Codex's own checks I confirmed:

- every one of the **96 magnitude profiles** listed across the seventeen
  endpoint statements is a genuine integer profile at its energy
  (`sum_i i^2 n_i = E`) — 0 mismatches;
- the vendored upstream files are byte-identical to PR #1110 at the pinned
  commit;
- the `V=36` witness norm, valuation, odd part, bit lengths, primality and
  residue mod 256;
- all ten shipped cubic thresholds against the rigorous reconstruction.

Two artifacts in my own first pass, both corrected before they reached this
note: my profile parser matched the band label `(3,4,0)` as if it were a
magnitude profile, and my first scan read the working tree rather than `HEAD`
— Codex has uncommitted `V=34` work in flight, which is correctly excluded from
this integration.

## Assessment

Technically the strongest wave so far: two independent census engines per
level, FLINT and PARI as independent norm engines, a correct and non-obvious
number-theoretic fix when the naive test ran out of room, and a cross-repo
import with better provenance than most of our own nodes.

The strategic picture is unchanged and should not be overstated by the pace.
Seven waves, **zero red closures**. Thirteen levels fell in one night, but the
band is one of two in the first band alone, `0<V<=34` remains, and the
universal target has not moved. What has changed is that the cost per level is
now dominated by exact arithmetic on residues, and at `V=36` the decisive
margin was about two bits.
