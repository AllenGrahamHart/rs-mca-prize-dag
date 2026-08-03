# Coordinator audit — maelcar PR audit pilot

**Auditor:** Fable, 2026-08-03. **Verdict: BANKED — zero collisions,
zero exposure; the HIGH flag on our SOL_TARGET_4 is the actionable
output and is ADOPTED as a task.**

The pilot replayed 11 of their artifacts + 4 independent checks;
nothing tracked was modified. Adopted findings: (1) all four maelcar
PRs are genuinely new to our record (no S_k/mu_11/ell-11 objects, no
pointwise K(d,e) <= 4, no sixteen-locator fixture anywhere in our
1770 nodes); (2) #1148 is DOMINATED IN APPLICABILITY by our proved
rate_half_list_chamber_affine_rank_bridge (locator-side geometry has
no map to codeword counts — 0/13 chambers) — cite as adjacent-
distinct, price nothing; (3) never cite their "S6 <= 20" beyond its
2/252 supports (their own residual is 21); (4) the T4 <-> T_sm BRIDGE
(proved exactly at (32,97): our banked 792 -> 288 smooth -> 9 orbits
= their T_sm) is adopted into the SOL_TARGET_4 trail; (5) HIGH FLAG:
their replayed n=128 counterexample row is admissible under our
SOL_TARGET_4 as stated (no q-vs-N hypothesis) and gives T4/N^3 = 2.87
with implied exponent ~N^5.6 at bounded index — SOL_TARGET_4 needs an
index hypothesis or should be expected to fall; decisive run = N=256,
q=769 (COMPUTE REQUEST, C++/large memory). Their flags (vacuous 288T
assertion; uncertified headline counterexample; 7 unexplained sieve
normals; unattainable envelope) recorded as trust-calibration for
future citation of maelcar material. Brief corrections accepted (kb_*
= KoalaBear; the ell-11 false friend).

## Dated addendum (2026-08-03, coordinator Modal run ap-sx9plNuGHtzGtGYisoYrh0)

Task #36 DECIDED — **SOL_TARGET_4 IS FALSIFIED AS STATED.** Exact
census (sol_target4_n256_result.json, sha256 27ed261e...):
- N=256, q=257 (index 1, fully admissible under the conjecture's own
  hypotheses): T_4 = 1,729,295,040, **T_4/N^3 = 103.07**;
- N=256, q=769 (index 3): T_4 = 63,361,728, T_4/N^3 = 3.78 (still
  rising from 2.87 at N=128).
No absolute constant C survives: the index-1 family's ratio scales as
~N^2/576 (first-moment pigeonhole into q^3 ~ N^3 keys — the mechanism
is elementary and predicts unbounded growth), and 103 > any C the
trail ever contemplated. The REPRICE IS FORCED: the conjecture needs
an index hypothesis (index = (q-1)/N), and even at fixed index 3 the
ratio has not yet plateaued — the repriced form should be stated as
T_4 <= C(index) N^3 with C(index) DECREASING, or with an explicit
index floor, and re-calibrated on the banked (32,97) anchor. Reprice
wording = surfaced decision; falsification = banked fact.
