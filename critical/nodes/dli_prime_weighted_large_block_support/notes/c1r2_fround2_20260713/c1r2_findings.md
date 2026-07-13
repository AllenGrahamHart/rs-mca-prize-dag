# C1' F-ROUND 2 — findings (catches c1r2-C1 .. c1r2-C7)

## c1r2-C1 — K' normalization resolved; mandate parenthetical is inconsistent
The round-2 mandate wrote "K' >= 1 (i.e. E-1 approaching or exceeding
4r(1+W_cl))". Under M2's actual K' (`verify_m2_c1prime_result.py` L96:
`excess/(r*(1+ledger))`; kill L95: `excess > 4*r*(1+ledger)`), `K'>=1` means
`E-1 >= r(1+W_cl)` = only 1/4 of the 4-allowance bound; `E-1 = 4r(1+W_cl)` is
`K'=4`. Resolved verbatim from M2: **K' = (E-1)/(r(1+W_cl)); literal kill K'>4;
recorded max 0.2469 is "below 4 by factor >16", consistent ONLY with threshold
4.** I used the 4-allowance unweakened and armed K'>=1 as a stricter secondary
watch. The mandate's identification of K'>=1 with the bound is arithmetically
wrong; it did not affect the verdict (the literal K'>4 line fired outright).

## c1r2-C2 — **C1' (r2 pose) is REFUTED** (the headline)
The r2 restatement ("for every generated prime-field full-half-section row
(q,2N,L) with q=1 mod 2N, 2^N>=q^L, N>=16L: E-1 <= 4r(1+W_cl)") is FALSE.
Counterexamples at L=1, N=32 (all in-hypothesis, all q=1 mod 64, all prime):
- q=63361: **K'=6.199084** (E-1 = 2029645184561543/288230376151711744, W_cl=76)
- q=65921: **K'=4.481241** (W_cl=72)
- q=204353: **K'=4.284843** (W_cl=50)
Independently verified with the banked kernels (signed_all_census + M2
primitive_orbit_count), sympy primality, DP mass invariant, and a brute-force
weight-3 orbit witness. **M2's survival was a scope artifact: it scanned only
q<=12289; the first amber is at q~32833 and the first literal kill at q=63361.**

## c1r2-C3 — the load-bearing method: exact upper bound + closed-form E
Two exact facts made the whole prime range rigorously decidable cheaply:
(a) `E = q^L * A_total / 4^N`, A_total = total odd-null signed-state count = the
    signed_all_census marginal summed over the singleton axis (grid (q,)^L DP;
    verified == recorded M2 E-1 for all 12 rows AND == banked signed_all_census).
(b) `K' <= (E-1)/r` for every row (W_cl>=0). So `(E-1)/r` — computable without
    ANY orbit enumeration — is an exact per-row K' ceiling; rows with (E-1)/r<4
    can never literal-kill, <1 can never amber. W_cl (the expensive enumeration)
    is needed only on the finite set with (E-1)/r>=1. This turns an "infinite"
    search into an exact finite one over the scanned range.

## c1r2-C4 — the accident envelope grows with q; the pose's correlation breaks
The residual (E-1)/r reaches 477 (q=63361), 327 (65921), 218 (204353) by
q~2e5 (vs 58.5 at the M2 near-worst q=7937). The pose's implicit bet is that a
big residual is always accompanied by a big low-weight ledger W_cl. It BREAKS on
single-weight-3-orbit rows (w3=1) with sparse higher-weight structure: the lone
weight-3 orbit's multiplier-shadow + additive-cluster mass pumps E across ALL
weights, but the window ledger [L+1..L+5] only prices the few in-window
primitives (W_cl=50..76 at the kills). Ratio residual/(1+ledger) crosses 4.

## c1r2-C5 — the kill is robust to the window cutoff, not an L+5 artifact
Extending the window to the rejected absolute `w<=7` demotes the kills only to
high amber (K' = 3.35 / 2.47 / 2.97), q=63361 still within 16% of 4, and the
growing envelope means w<=7 also fails at larger q. So no small fixed window
w_max rescues the "4-allowance": the mechanism is a genuine failure of a
low-weight orbit ledger to control the residual, not a truncation detail.

## c1r2-C6 — the re-pose did not escape its own motivating row
q=204353 is the "natural cluster row (k=7)" cited IN the node statement as the
row that refuted the frozen uniform form (K=23.2/10.9/3.77) and motivated the
C1' ledger re-pose. It refutes the ledger re-pose too (K'=4.285). The ledger
conditioning delayed but did not remove the failure.

## c1r2-C7 — level-independence (L=2 corroboration; deeper search DEFERRED)
L=2 shows the same growth: max K'=0.661 at q=3137 (vs M2 L=2 max 0.034 at q=577),
with (E-1)/r=1.32 already > 1. A literal L=2 kill is expected at larger q by the
same mechanism but was not reached — the (q,q) grid DP hits the 270s Modal
ceiling above q~4000 (DEFERRED per compute law). The refutation stands on L=1;
L=2 is corroborating, not required.

## Integrity notes
- No convention was weakened to force the kill: RAW ledger (matches M2 exactly at
  q=7937), w_max=L+5, 4-allowance, exact-rational verdict path, in-hypothesis
  rows only. The kill fires under the pose of record verbatim.
- Guardrail `dli_wcl_raw_ledger_interface_guardrail` says low levels (ell in
  {1,2,4,8}) reduce the WCL-ZONE bound to "primitive-window emptiness". The kill
  rows are exactly the NON-empty low-level rows; using the raw ledger (as the
  guardrail requires) they still violate the 4-bound. No contradiction with the
  guardrail — but it shows raw-ledger non-emptiness is not sufficient for the
  4-bound at ell=1.
