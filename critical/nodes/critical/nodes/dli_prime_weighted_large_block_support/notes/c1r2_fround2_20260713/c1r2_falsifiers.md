# C1' F-ROUND 2 — pre-registered falsifiers (RAW ledger, schedule r2)

- **predicate:** node `dli_dyadic_k_core` (C1'), r2 restatement.
- **pose of record:** `critical/nodes/dli_prime_weighted_large_block_support/notes/C1PRIME_LEVEL_SCALED_POSE.md`
- **round-1 record:** `M2_C1PRIME_RESULT_AUDIT.md` (12 rows, L=1,2, RAW ledger; max K'=0.246909432 at L=1,q=7937).
- **corrections baked in:** (4a/#206) RAW primitive signed-shift ledger, NO first-owner dedup; (4c/#205) level parametrised by L with odd-index moments 1,3,...,2L-1; analogue rows use the M1/M2 convention N=32, n'=2N=64 (h fibers = N), and I state L/dim mapping per axis below.
- **written BEFORE any computation** (house law #1). Timestamp 2026-07-13.

## Exact quantities (verbatim from pose + `verify_m2_c1prime_result.py`)

Row = generated prime-field full-half-section `(q, n'=2N, L)` with `q = 1 mod n'`,
`2^N >= q^L`, `N >= 16L`. `omega = (least primitive root of q)^((q-1)/2N) mod q`
(a primitive 2N-th root of unity; requires `q = 1 mod 2N`). Fibers `i=0..N-1`,
odd-moment vector per fiber `v_i = (omega^{(2ell-1) i} mod q)_{ell=1..L}`.

```
T(lambda) = prod_{y=0}^{N-1} cos^2(pi a_y(lambda)/q)
E   = 1 + sum_{lambda != 0} T(lambda)              (full signed-vanisher spectrum)
r   = q^L / 2^N
w_max(L) = L+5
W_cl(q,N,L) = sum_{primitive orbit O, L+1 <= w(O) <= L+5} 2N * 2^{-w(O)}   (RAW ledger)
```

Signed-vanisher identity used to compute E (reproduces the M2 record exactly):
`E = (q^L/2^N) * (1 + sum_{w>=1} signed_count(w) * 2^{-w})`, and equivalently
(derived + independently verified here) **`E = q^L * A_total / 4^N`**, where
`A_total = # signed odd-null fused states` = the total DP mass at odd-key 0 over
the per-fiber option set {N,B (weight 2, no shift), +v_i, -v_i}. This gives an
exact-integer E with a grid-(q^L) DP (cheap for L=1,2).

`E`, `W_cl`, `r` are all exact rationals (Fraction/bigint) on the verdict path.

## K' DEFINITION AND THRESHOLD — resolved from M2 (verbatim)

`verify_m2_c1prime_result.py` line 96: `exact_k = excess / (r_value*(1+ledger))`
with `excess = E-1`. Kill test line 95/pose line 62: `E-1 > 4*r*(1+W_cl)`.

**Therefore K' := (E-1) / ( r * (1 + W_cl) ), and the LITERAL C1' KILL is K' > 4.**
Recorded max K' = 0.246909432 is "below 4 by a factor > 16" (M2 audit) — this is
consistent ONLY with threshold 4, NOT with a threshold-1 normalization.

> FINDING c1r2 (pre-registered): the round-2 mandate's phrase "K' >= 1 (i.e.
> E-1 approaching or exceeding 4r(1+W_cl))" is arithmetically INCONSISTENT with
> the M2 record: under M2's K', `K'>=1` means `E-1 >= r(1+W_cl)`, i.e. only
> ONE-QUARTER of the 4-allowance bound; `E-1 = 4r(1+W_cl)` is `K'=4`. I use the
> M2 normalization verbatim (threshold 4 = literal kill) and do NOT weaken the
> 4-allowance. I additionally arm the mandate's conservative K'>=1 watch line as
> a stricter secondary trip (below).

## STRUCTURAL BOUND (exact, used to make the search rigorous)

Because `W_cl >= 0`, for EVERY row `K' = (E-1)/(r(1+W_cl)) <= (E-1)/r`.
So `(E-1)/r` (cheap: needs only A_total, no orbit enumeration) is an EXACT upper
bound on K'. Consequences, all pre-registered:
- A row with `(E-1)/r < 4` can NEVER trip the literal kill.
- A row with `(E-1)/r < 1` can NEVER trip the amber watch.
- The census computes `(E-1)/r` exactly over the WHOLE scanned prime range, and
  computes exact `W_cl` (hence exact K') for every row whose `(E-1)/r >= 1`
  (the only rows that could matter). This bounds K' rigorously over the entire
  scan, not just at sampled points.
- q=7937 has `(E-1)/r ~ 58.5 > 4` but `W_cl=236` pulls K' to 0.2469; the game
  is whether some row has `(E-1)/r` large while its window ledger W_cl stays
  small (the correlation between the two is the pose's load-bearing structure).

## KILL LINES (pre-registered; verdict governed by these)

- **KILL-LITERAL (refutes C1'):** any EXACT analogue row satisfying the row
  hypotheses (`q=1 mod 2N`, `2^N>=q^L`, `N>=16L`) with `K' > 4`
  (equivalently `E-1 > 4 r (1+W_cl)`). => verdict KILLED; bank witness with full
  reproduction (q, N, L, A_total, E-1, r, primitive-orbit counts per weight,
  W_cl, K') and the exact-rational check.
- **KILL-AMBER (stricter watch; does NOT logically refute C1' but BLOCKS the
  named-conjecture amber flip):** any EXACT in-hypothesis row with `K' >= 1`.
  => verdict MIXED; the M2-advertised >16x safety margin is destroyed at that
  row even if the 4-bound literally holds. Bank witness.
- **KILL-SCALING:** across >= 3 increasing q-scales at a fixed level, the
  accident-envelope of K' (max K' per octave) is monotone increasing AND its
  log-linear extrapolation crosses 4 within the in-hypothesis q-range
  (`q <= 2^{N/L}`). Amber variant: extrapolation crosses 1. => KILLED (resp.
  MIXED).
- **KILL-ASPECT (instantiation exposure):** the K' upper bound `(E-1)/r`
  worst-case (over the scanned primes at a level) is monotone INCREASING as the
  aspect `N/L` increases toward the official regime, extrapolating above 4
  (literal) / 1 (amber). Probed by comparing levels L=1 vs L=2 at N=32
  (aspect 32 vs 16) and, if it fits Modal, N=64,L=1 (aspect 64).

## NON-KILLS (explicitly NOT falsifiers)

- A single accident row with large `(E-1)/r` but correspondingly large `W_cl`
  keeping `K' << 4` (this is exactly the designed q=7937 behavior).
- Bulk (non-accident) rows: `K' -> 0` as q grows (expected DLI cancellation).
- Large `W_cl` (it only enlarges the RHS / helps the bound).
- Any row violating the row hypotheses (`q != 1 mod 2N`, `2^N < q^L`, `N<16L`).
- Float-only excursions: the verdict path is exact rational; floats are display.
- Fractional/anomalous orbit quanta or incomplete signed-shift orbits => flagged
  as an integrity failure (DEFERRED), not scored as a kill.

## POSITIVE CONTROL (must reproduce)

Recompute BOTH sides at (L=1, q=7937) from scratch on the RAW ledger:
E via the A_total DP (cross-checked against the banked M1 `V_orbits` identity),
and W_cl via an independent port of the primitive-orbit enumerator
(cross-checked against M2 `primitive_orbits` = {3:2,4:8,5:31,6:126}, W_cl=236).
Target: `K' = 0.246909432...`, exact `E-1 = 15584479363607/144115188075855872`,
exact `W_cl = 236`. If raw and M2 disagree => FINDING (M2 should already be raw
per w7-C2). Also reproduce the other 11 M2 rows exactly.

## MUTATION CONTROL (required to trip)

Re-price q=7937 with the DELETED ledger `W_cl := 0` (the pose's "removing the
ledger makes the row fail"). Then `K' = (E-1)/r = 58.5... > 4` MUST fire
KILL-LITERAL. This simultaneously (a) proves the kill detector fires on a true
positive and (b) reproduces the pose's load-bearing claim. Second mutation:
lower the literal threshold to 0.2 and confirm q=7937 (real K'=0.2469) fires.

## NONEMPTINESS ASSERTS (house #137)

Assert: scanned prime count > 0; the 12 M2 rows are all inside the L=1/L=2
scans; q=7937 present and reproduced; at least one accident row (weight-3 orbit
present at L=1) found; the mutation control actually fires a kill.

## SCOPE (stated honestly up front)

Analogue rows at N=32 (n'=64): L=1 over primes `q = 1 mod 64` up to the widened
cap (well beyond M2's 12289), and L=2 over primes `q = 1 mod 64` up to a smaller
cap (grid q^2). Optional aspect stretch N=64 if it fits the Modal ceiling. The
OFFICIAL aspect (N ~ 2^32, dyadic tower) is always beyond direct reach; SURVIVED
means no kill line tripped WITHIN this analogue scope, reported with the honest
extrapolation toward official aspect.
