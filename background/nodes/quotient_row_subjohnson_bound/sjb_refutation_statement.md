# REFUTATION: quotient_row_subjohnson_bound is FALSE as minted

- **status:** REFUTED (constructive counterexample family + exact integer instances;
  machine-verified: sjb_falsify_exact.py, sjb_semantics_tiny.py, sjb_n64_fiber_demo.py — ALL PASS)
- **target:** dag.json node `quotient_row_subjohnson_bound` (TARGET, key), verbatim scope
- **worker:** fresh-context proof worker, 2026-07-13; repos read-only; catch ledger from #124

## The refuted claim (verbatim scope)

For every dyadic quotient row (n' = 2^{s'} >= 64, k' = rho n', rho in
{1/2,1/4,1/8,1/16}) from an official row at scale M >= 2 (n = M n' = 2^s,
13 <= s <= 41), every prime q ≡ 1 (mod M n') with q >= (M n')^2, every received
word U', and every cell a in [max(k'+1,7), min(n'-7, isqrt((k'-1)n'))] (P1-OWN:
the single cell a = k'+1, present iff k' >= 8): the number of deg < k' codewords
whose exact agreement support with U' has size exactly a and is APERIODIC in
Z_{n'} is <= min((63/128) n'^6, (q-3n')/2).

## The refutation theorem

**Theorem (t = 1 truncated-locator floor).** Fix any n', k' < n', prime q, and an
n'-point evaluation domain D ⊆ F_q^*. For tau in F_q let W_tau = X^{k'}(X - tau),
received word = its evaluation on D. Then the exact-agreement-(k'+1) list of
W_tau is in support-exact bijection with {S ⊆ D : |S| = k'+1, e1(S) = tau}
(e1 = element sum), hence

    sum_tau L(W_tau, k'+1) = C(n', k'+1)   and   max_tau L(W_tau, k'+1) >= ceil(C(n',k'+1)/q).

If moreover D = H^M is the order-n' (dyadic) subgroup and k' is even, every such
support has ODD size k'+1 and is therefore automatically APERIODIC in Z_{n'}.

**Corollary (refutation).** The minted claim fails at every (s, rho, M, q) with
ceil(C(n',k'+1)/q) > min((63/128)n'^6, (q-3n')/2). Exact verified instances (P1-OWN
cell a = k'+1, all scope conditions checked):

| rate | s  | n'   | q                 | pigeonhole floor | minted cap | factor |
|------|----|------|-------------------|------------------|------------|--------|
| 1/2  | 13 | 64   | 67239937 (min adm.)| 2.64e10 (2^34)  | 3.36e7     | ~786x  |
| 1/2  | 14 | 64   | 268582913          | 6.6e9           | 1.34e8     | ~49x   |
| 1/2  | 15 | 64   | 1073872897         | 1.65e9          | 5.37e8     | ~3x    |
| 1/2  | 13 | 128  | 67239937           | 2^98            | 3.36e7     | 2^73   |
| 1/2  | 13 | 4096 | 67239937           | 2^4063          | 3.36e7     | 2^4038 |
| 1/4  | 13 | 128  | 67239937           | 2^75            | 3.36e7     | 2^50   |
| 1/8  | 13 | 128  | 67239937           | 2^43            | 3.36e7     | 2^18   |
| 1/16 | 13 | 256  | 67239937           | 2^60            | 3.36e7     | 2^35   |

All four rates are refuted at the P1-OWN cell; n' = 64 (the FIRST open quotient
size) is refuted at s in {13,14,15}. Violation q-windows (claim is ∀q >= n^2):
at (1/2, 13, 64) every admissible prime in [2^26, 1885253433]; at (1/2, 13, 128)
the n'^6 branch alone fails for every q in [2^26, ~2^83].

**Prize-wide corollary.** At EVERY field q < 2^256 (the prize envelope) the
word-uniform (63/128)n'^6 form is false for all dyadic n' >= 512 (rho = 1/2, 1/4)
resp. n' >= 1024 (rho = 1/8, 1/16), with persistence under doubling proved by
Vandermonde C(2n',2k'+1) >= C(n',k')C(n',k'+1). No word-uniform sub-Johnson
polynomial bound at a = k'+1 can serve scales with n' above these thresholds, at
any prize field, by any method.

**In-vivo exhibit (QRL-MODAL-1's own grid cell).** At (n = 256, M = 4, n' = 64,
k' = 32, q = 65537 >= n^2): the complete exact e1-fiber census (int64 DP, total
== C(64,33) exact, cross-validated against brute force at n'=16) gives
min_tau L = 27,111,731,756,096 and max_tau L = 27,116,735,434,620 — EVERY word of
the 65537-word family exceeds the minted n'^6 cap by ~802x, the (q-3n')/2 branch
by ~8.3e8x, and QRL-MODAL-1's pre-registered expectation (max <= 2n' = 128) by
~2.1e11x. An explicit (word, codeword, support) triple is verified end to end.

## Also refuted en passant

- "Conjectural true size O(n'^2)": false in the fiber-rich regime (the floor is
  exponential); tenable only where C(n',k'+1) <~ q n'^2.
- Catch #115's strength pin L <= min((63/128)n'^6, (q-3n')/2) is UNSATISFIABLE BY
  THE TRUTH at minimal official fields for every s=13 open scale (and analogues at
  all rates): no true lemma of any strength can feed the banked ESP transport there.
- "The APERIODICITY restriction is load-bearing": VOID at the consumed cell — the
  P1-OWN cell a = k'+1 is odd and every odd-size subset of Z_{2^{s'}} is aperiodic.

## What survives (not refuted here)

- QRL packet windows T1 (n' <= 32), T2 (Johnson cells), T3 (M >= k): all TRUE;
  the falsification begins exactly at the first open size n' = 64 and lives
  exactly in the open sub-Johnson band. The Johnson radius is the truth boundary.
- The claim restricted to the FIBER-STARVED regime (pairs/fields with
  ceil(C(n',k'+1)/q) <= cap; e.g. n' = 64 at s >= 16): open, not refuted;
  see successor-B in sjb_refutation_proof.md.
- The census gate itself (chart-constrained contributors), the chart-level K4
  theorem, the descent + ESP implications (they are true implications; the failed
  thing is that their word-uniform input target is false).

## Verifiers (all ramguard tiny, <60 s, <256 MiB total)

- sjb_falsify_exact.py — exact-integer instance table, scope checks per instance,
  violation q-windows with exhibited admissible primes, prize-field thresholds,
  doubling persistence, the honest not-refuted boundary (s >= 16 at n' = 64).
- sjb_semantics_tiny.py — EXHAUSTIVE validation at (n'=8, k'=4, q=17): bijection
  vs all 17^4 codewords for all 17 tau; aperiodicity-for-free; pigeonhole;
  averaging identity; mass identity sum_c C(A_c,k') = C(n',k') (mutation control
  on the object definitions).
- sjb_n64_fiber_demo.py — exact complete fiber census at the QRL-MODAL-1 grid
  cell + explicit witness verified in vivo + DP cross-validation at (16, 257).
