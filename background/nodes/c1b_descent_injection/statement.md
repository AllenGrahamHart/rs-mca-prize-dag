# c1b_descent_injection

- **status:** PROVED
- **closure:** proof
- **refs (legacy):** ['experimental/notes/roadmaps/a_pilot_wh_torsion_data.md']

## Statement

VERIFIED SEED (sympy-exact): under the squaring pushforward A |-> A_2 (A_2(X^2) = (-1)^h A(X)A(-X)), a trade B = A + c maps to a BAND PAIR: B_2 - A_2 = ±(c(A(X)+A(-X)) + c^2) — Y-degree exactly floor(h/2). So level-n trades descend to level-n/2 band pairs (budget h/2, saturating in ~log h levels) — but ONLY log2(1024/64) = 4 LEVELS are needed to reach the exhaustively-censusable domain n = 64 (pilot-verified feasible). THE CERTIFICATE ALGORITHM: (i) enumerate band pairs at the bottom (n = 64, budget delta_4) — census machinery extended; (ii) for each bottom candidate, check lift-compatibility up the 4 levels (each root has 2 square-root preimages; the lift must itself satisfy the trade/band condition at each level — a per-candidate bounded check); (iii) level-n trades inject into (bottom pairs) x (compatible lift data) — THE INJECTION LEMMA is the one new statement (my pushforward identity is its seed; the antipodal-paired roots branch to the toral/paid side per X24's mechanism and must be tracked — C1c). CALIBRATION GROUND TRUTH: the pilot's exact n = 32 eliminant and the n = 16/32/64 censuses. CORRECTION (roadmap-lane, delta-recursion analysis): the band budget saturates — delta_{k+1} = floor((h + delta_k)/2) hits the vacuous h-1 after ~log2(h) levels, retaining only h/2^k coefficients of information. The '4 levels to n = 64' claim was WRONG. True design: k* = min(log2 h - 1, levels available); the descent is informative and bottom-censusable for h <= ~8-10 (e.g. h = 4: one level, bottom n = 512 with a 2-coefficient condition, MITM-countable; h = 8: two levels, bottom n = 256, borderline). LARGE h (>= ~16) IS NOT COVERED by this route — nor by C1a's direct MITM. If the window audit returns H_max > ~10, a third piece is required: the large-h emptiness lemma (heuristic margin: hundreds of bits; the obstruction count h-1 grows with h). The injection-lemma brief is HELD until the audit lands — its H_max decides the brief's shape. PROVED (Fable agent, D1-D8 chain, 19/19 replayed): exact band budget delta_k = h - ceil(h/2^k); exhaustive case split (the diagonal branch = Q = -P, paid); exact lift characterization with THE TERMINAL-LIFT COLLAPSE — <= 2 lifts per bottom pair (h even), <= 4 (h odd), replacing the naive 2^{2h}, tight in the toys; the injection has a linear-time inverse; soundness theorem with exact k*(h) and bottom parameters; collision exclusion whenever 2^j | h. Validated end-to-end: 32->16 and 64->32 (h=4) recover the pilot's exact toral counts (28/120, non-toral empty); 16->8 (h=3, F17) recovers all 352 trades including 16 paid diagonals. HONEST CORRECTION (mine, again): the bottom census at n = 1024 stops at h ~ 6 (2^38 work), not ~8-10 — C1b certifies h = 5, 6. Gaps G-C2/C3/C4 named in the note.

## Attack surface

prove the injection lemma (pushforward + fiber data determines the lift); implement the bottom band census; validate the full pipeline at 128 -> 64 and 256 -> 64 against direct censuses before trusting 1024 -> 64

## Falsifier

the pipeline at 128->64 missing a known trade (the census has ground truth) or the bottom band count exploding beyond per-candidate-checkable size
