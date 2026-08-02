# Fable audit of the FM0-FM2 pilot — 2026-08-02

**Verdict: ACCEPTED — the most consequential pilot result of the program
so far.** Opus-5 subagent, directed per the Brief-4 adversarial-audit work
packages. 4125/4125 exact checks pass; ten parameter points; complete
witness enumeration (up to 4.86M witnesses/case) by meet-in-the-middle.

## Audit trail

- **L1 (slope-disjointness of witness sets) verified by hand:** a shared
  support S at slopes z != w gives (z-w)V = p_z - p_w on S, forcing
  deg V < K against deg V = A-m >= K. Sound — and it means NO selector
  can compress by support collapse; compression = higher cores /
  repeated differences only.
- **L2 (max core = A-m) verified by hand:** on a core of size > A-m,
  v agrees with (p_z-p_w)/(z-w) (degree < K) on more than deg(V) points.
  At RowC 1/4 with m=4: A-m = 257 = K+1 > K.
- **The FM0 finding checked against the tree: the first-match order
  `prec` is genuinely UNDEFINED** — the bridge, canonicalization
  contract, and audits all say "a fixed order" without fixing one.
  PP4.0 was adopted in our Brief-4 audit and never written. And FM2
  proves the choice is OUTCOME-DECIDING: support-keyed lex/colex orders
  collapse |Gamma_lo| 97 -> 0-4; polynomial-keyed and random orders give
  NO compression (91-97/97, near-Sidon) — K1 is LIVE under those orders.
  P-B's truth may depend on which order the node means.
- **The headline mechanism is real and density-driven:** intended
  witnesses sit at the MEDIAN of W_z (never first); lex selection
  concentrates every selected support on a common low-index
  prefix/window (deg p = K-1 at 97/97 — the selector picks MAXIMALLY
  generic codewords with STRUCTURED supports); compression strengthens
  with witness density (breaks below ~10^2 witnesses/slope; at official
  scale log2|W_z| ~ 668 even at the smallest super-budget q —
  extrapolation, noted as such).
- **The honest limits are correctly stated:** budget untestable at pilot
  scale (the audit's own vacuity bound re-derived); the collapse is
  quantifier-driven (greedy pairwise-low-core subfamilies remain 34-60%
  of slopes and near-Sidon — P-B's "meets EVERY other" quantifier does
  the final ejection); collapsed slopes land in Gamma_hi (P-A1) — the
  mechanism RE-ROUTES mass, it does not pay 16n^3, so any exchange
  theorem must pair with a P-A1 accounting statement.

## The FLAG (surfaced for adjudication — no status change)

The bridge (`xr_tangent_support_mismatch_bridge`, PROVED) asserts the
strip rung leaves pairwise cores <= K, and its dichotomy defines
Gamma_hi by core EXACTLY K. By L2, cores can reach A-m = K+(h-m) > K
when h > m — including at RowC 1/4 (h=5, the split-fibre m=4 gives 257 =
K+1). My analysis of the seam: a (K+1)-core pair at distinct slopes
creates a joint codeword pair explaining (u,v) on exactly K+1 > k points
but NOT on an A-support. The bridge's nongeneric trigger is the
A-support version; the strip rung's trigger may be the >k-points
version. If the strip routes on >k points, the rung claim stands and the
bridge's generic-branch HYPOTHESIS is understated (should be "no joint
pair on >k points"); if the strip routes on A-supports, the dichotomy is
non-exhaustive and Gamma_hi must widen to {some core >= K}. Either
repair is statement-level surgery on a PROVED critical node. RECORDED as
a dated node-local flag; adjudication = planner decision with maintainer
visibility. The pilot's 17/97 (P3), 24 (P6), 46/46 (P5) slopes with
cores >= K+1 and never exactly K make the gap concrete.

## Adopted consequences

1. **PP4.0 (the selector manifest) is now THE gating decision of the
   P-B lane** — no longer a formality: the pilot proves the lane's truth
   may hinge on it. It must be written as a SUPPORT-KEYED order (the
   only tested class that compresses), and the choice surfaced to the
   maintainer since it effectively selects which theorem P-B is.
2. **The exchange theorem gets its first sharp falsifiable form** (the
   pilot's recommendation, adopted as the FM3 target): lex-first-match
   forces every selected support to contain the prefix {x_0..x_{K-1}}
   once |W_z| is large enough; hence all cores >= K and Gamma_lo is
   EMPTY. The prefix data (common blocks of 3/5/6/11 coordinates,
   growing with density) supports it.
3. The bridge flag blocks FM3's final wording until adjudicated.

> **[SUPERSEDED IN PART 2026-08-02 — selector-orders/K1 pilot
> (`notes/pilots_20260802/pb_selector_orders/`), coordinator-replayed.]**
> Item 2's FM3 wording is FALSE as drafted and is WITHDRAWN: at every
> dense scale the global common block under lex is 3-11 coordinates,
> always strictly below K, while Gamma_lo collapses anyway — and three
> support-keyed orders with common block 0 (colex, value-colex,
> reverse-lex) collapse identically. The operating mechanism is
> global-block + pairwise birthday over ~q^2/2 slope pairs, not a
> K-prefix; the exchange target must be re-worded from that mechanism.
> Item 1 is STRENGTHENED: the A1 fork is one-sided (5/5 support-keyed
> GREEN vs 3/3 polynomial/codeword-keyed RED, procedural reading RED at
> the densest point), so PP4.0 should freeze the support-keyed CLASS
> with lex as canonical representative and explicitly exclude the RED
> readings. Item 3: the bridge flag was adjudicated the same day
> (genuine gap, R2 forced — see
> `notes/pilots_20260802/xr_bridge_semantics/`); FM3 remains blocked
> only on the joint R2+P-A1 edit landing.
