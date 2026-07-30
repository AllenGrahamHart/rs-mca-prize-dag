# Wave-33 audit — Codex goes Galois, and three agents converge on one residue

**Date:** 2026-07-30. **Planner:** Fable. **Range:** `9ba43bda..f69c6fdc`
(126 commits, 18:0x 07-29 – 07:52 07-30). **Verdict: CLEAN — integrated in
full. One canonical-form defect found in Codex's tree and repaired here.**

```text
math orbit  241 = 179/38/24   ->   241 = 179/38/24   (unchanged)
nodes 1446 -> 1531 (+85)      edges 3776 -> 4060 (+284)
```

85 new PROVED nodes, **133/133 verifier runs PASS**, zero status changes, all
background, all `ev`. The largest block (34 edges) feeds
`rate_half_band_closure` — the red gating the rate-1/2 instance of BOTH grand
challenges.

## The campaign changed mathematical character

For ten waves the work was censuses and exact arithmetic. This wave is
**Galois theory and function-field geometry**: decomposition profiles of the
KoalaBear degree-60 endpoint map excluded by monodromy socles, adjacency
genus, dihedral factor analysis, and Riemann–Hurwitz ledgers. Overnight the
live inner-degree set went

```text
{2,3,4,5,6,10,12,30}  ->  {2,3,4,6,10,12}
```

(degree 5 by fifth-power injectivity, degree 30 routed through 6, the complete
m12 branch closed by a socle/centralizer argument), with the residual quartic
branch reduced to 26 transverse `(m,r,delta)` types and only `(2,24),(4,12)`
surviving at `m=12`.

**Independent checks I ran:** the S6 pair-action class table underlying the m4
passport reduction — all ten rows (pair cycle types, branch indices, parities)
recomputed from scratch, **0 mismatches**; the RH budget `2*15-2=28` with pole
index 12; and `gcd(5, p^6-1) = 1` for `p = 2130706433` (`p = 3 mod 5`), which
carries the fifth-power injectivity step. The group-theoretic load-bearing
data is right where I probed it.

## Three agents, one residue

The campaign attacks the `Q=6,u=2` equality-wall residue that the July wave
(#1114–#1117, other authors) left at 405 conic-universe survivors. Upstream
right now: **Scott Hughes's codex** holds #1122–#1131 on the same residue,
**our Codex** holds #1132, interleaved. Our Codex *replayed* Scott's open
#1130/#1131 locally as PROVED compilers before citing them — replay, not
trust, which is the right discipline for open PRs.

This is the first genuinely multi-agent convergence on a single named object:
our worker, Scott's worker, and the integrated ledger all pointing at cap-68 /
u2. The K3 lane is now the fastest-moving surface in the whole program.

## Fences: exemplary

The attack.md addition ends: *"None of the structural cuts moves the owner
ledger, proves `u=2` empty, establishes cap `68`, or closes the KoalaBear
row."* And the next-theorem requirement is stated concretely (exclude or
assign a first-match owner to each of the six rows; impose the quartic/
source-star incidence on the 26 transverse types). This lane has a stated
frontier — the complaint I raised about the h7 lane in wave 32 does not apply
here.

## Found and repaired: Codex's dag.json is off-canonical

Codex's HEAD `dag.json` breaks canonical form at byte ~1,977,449 — a
mis-indented path list (3 spaces where depth demands 4). Something other than
the canonical writer touched the file. Content is unaffected (byte-identical
node/edge data after parse); I renormalized on our side per the canonical
law. **Codex should re-run its canonical writer**; this will otherwise recur
in every diff.

## Merge notes

Five conflicted files were all byte-identical copies of our own July-harvest
work returning — Codex picked up the harvest, the crosswalk re-pin, and the
node notes verbatim. Excluded and verified identical. The trees are
effectively synchronized now; only in-flight work differs.

## Assessment

Eleventh wave, zero red closures, board unchanged — but this one moves real
strategic mass. The monodromy toolkit is qualitatively stronger than censuses
(it closes infinite families per argument, not levels), the K3 residue now has
three agents and a shrinking live set with stated terminal conditions, and the
evidence is pointed at the one red that gates both grand challenges at rate
1/2. If the six remaining inner degrees terminate the way m12 did, the
equality wall — the wall his July ledger calls one of the two genuine walls —
is what falls.
