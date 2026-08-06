# FABLE_AUDIT — f2_adm (round 17, pilot 3 of 4 to report)

**Auditor:** Fable, 2026-08-06. **Verdict: BANKED, MAINTAINER-LEVEL —
the F2 mechanism reconstructs on admissible rows (falsifier does not
fire; the 16-rung descent is replaced by LEMMA ADM-2's exact
direct-sum decomposition into prime-field GRS codes, making dim L
EXACT), but the reconstruction is worse news than vacuity would have
been: THEOREM A discharges no moving rung on any admissible row,
LEMMA 3 is exactly saturated (margin 1.000), and CATCH-1 exhibits
admissible rows where (O1) IS FALSE by 2^{Theta(n)} — every
non-generating row (ord_n(p) < e). The F2 lane's obligation of
record becomes CONDITIONAL on a generation hypothesis the rules do
not supply.**

Replay: verify.py 373/373 exit 0, digest F2_ADM_ALL_PASS (coordinator
re-run under ramguard local; pilot additionally verified a clean-state
replay byte-identical). Anchors verified by the coordinator:
official_row_primes_pinning/proof.md:28 ("for every choice of F, L,
and k" — the rules quantifier that forbids assuming generation);
f2_sl1b/PROOFS.md:161 (the bracket whose constant CATCH-2 corrects).
COORDINATOR INDEPENDENT CHECK of the CATCH-1 exhibit row: p =
3*2^41+1 verified prime (MR-30), q = p^6 with log2 q = 255.509775 <
256, 2^41 | q-1, p ≡ 1 mod 2^41 hence ord_n(p) = 1 < 6 —
non-generating and admissible, by my own arithmetic. CROSS-PILOT
CONVERGENCE: this is the SAME row es_g_lanes exhibited above global
balance (its log2 q matches to 6 decimals) — two blind pilots
converged on the same adversary class (extension/non-generating
rows) via different lanes.

ADOPTED:
- LEMMAS ADM-1/2/3 and the depth-budget trade-off (D rungs force
  t <= n/(2^D(41-D))); the 3-factor admissible ladder with the
  25% fixed sector; dim L EXACT (= C·min(S,R)) — f2_sl1b's bracket
  collapses to a point and its INTERACTION-1 is fully closed.
- The 23-row theorem survival table; (O3) unchanged in depth
  (order-filtration, not Frobenius); (M3) VACUOUS on admissible rows
  (needs R/m > 0.61, admissible max 0.0488); the antipodal law's
  coset gap (CATCH-6) as a NEW NAMED OBLIGATION — no F2 file
  mentions the rules-level coset domain.
- **THEOREM ADM-B and CATCH-1**: on k = e rows LEMMA 3 saturates
  exactly (certifies nothing beyond the unconditional floor); on
  k < e rows (O1) fails by 2^{Theta(n)}, for every t in the
  non-vacuous regime (t-naming-independent — the ratio is c·k/e with
  c <= 1). THE F2 HEADLINE OF RECORD (per the pilot's residual-7
  recommendation, adopted verbatim): "(O1) discharged on order
  layers <= 2t (<= 4.9% of the domain, none of them moving); at
  every moving rung it equals SL-1b' with LEMMA 3 exactly saturated;
  and it is FALSE unless the smooth domain generates the field."
  There is NO RUNG BAND on admissible rows — the round-16
  "1-10/1-9" band is a statement about the inadmissible tower only.
- SL-1b' SHARPENED to the explicit terminal: ternary mass of a
  [2^38, 2^38-R, R+1]_p GRS code on the half-system of mu_{2^39},
  R = 4.295e9, p ~ 2^64, Z(L) = Z_1^C with C <= 4 — prime-field,
  MDS, single-class.
- **THE SEAM IDENTITY (D5)**: (O1)'s necessary condition and the
  PP5.0 average-vs-sum seam are THE SAME INEQUALITY
  (log2|K1|_eff >= n/2), with equality exactly on surviving k = e
  rows. The pending user decision is hereby SHARPENED: the sum
  reading spends bits (O1) has already spent; the average reading
  makes (O1) an exactly-zero-slack claim.

CATCHES ACCEPTED: CATCH-1 (maintainer — raise the generation
hypothesis to Przemek with the exhibit; conservative posture: the F2
lane is CONDITIONAL on generation until answered); CATCH-2 (f2_sl1b
constant k = [F_q:F_p] -> ord_n(p); addendum written this bank —
the banked reading OVERSTATES dim L off-tower); CATCH-3 (the tower
inconsistent with its own t — 7e10 is 1.29e5x too large by the
tower's own arithmetic; joins the 7e10 dossier); CATCH-4 (the empty
(e_p,e) = (40,6) class); CATCH-5 (self-caught reducible-modulus
defect — the lcm-evading shortcut recorded for reuse); CATCH-6 (the
coset-domain gap, new obligation).

HONEST RESIDUALS accepted as stated (Z_1 untouched and toys are no
evidence at the official row; ADM-2 proved only for D <= 2 — exactly
the admissible regime, so no gap in scope; n = 2^40 untabulated;
ADM-B says nothing about non-LEMMA-3 routes to K1). Process defect
(~9 bare python3 for text edits/AST checks, no claim numbers
produced) — accepted with disclosure; the pattern is recurring
across pilots: text-editing convenience. Standing note added to the
brief template: use Edit/heredoc-under-ramguard for file patching.

Cross-pilot reconciliation: (i) with t_naming — this pilot's
registrations used the CATCH-E-correct max-index reading throughout
(R = ceil(t/2)); its ADM-B is t-collision-independent as claimed;
D5's numeric pricings inherit the t-interval and are so labelled.
(ii) with es_g_lanes — the non-generating adversary row is now
doubly load-bearing (above balance AND (O1)-false); the two
findings are one phenomenon: extension degree divides the
characteristic bits everywhere.

## ADDENDUM (2026-08-06, coordinator, from round-18 o1_generating_adversary)

1. **CATCH-6 HALF-CLOSED**: THEOREM C1 proves (O1) exactly
   coset-invariant (bijection phi_g, factor of 1); the coset gap is
   confined to the parity/descent machinery. CATCH-1 is coset-robust.
2. **D3's "margin 1.000" is reading-A-only** (CATCH-B): under parity
   reading B generating rows carry margin 2.000 and classes (1,2),
   (2,4) flip REFUTED -> SATURATED. The (1,6) CATCH-1 witness is
   unaffected under both readings.
3. **The saturation's meaning sharpened** (THEOREM Z2): at k = e
   LEMMA 3's requirement IS the balance t·L >= n — (O1) survives
   under the (C) calibration and is FALSE by 2^{Theta(n)} under the
   (T*) slice calibration; the internally-forced cell (reading A +
   slice) is the FALSE one. See o1_generating_adversary/.
