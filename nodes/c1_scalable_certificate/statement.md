# c1_scalable_certificate

- **status:** TARGET
- **closure:** proof
- **refs (legacy):** ['experimental/notes/roadmaps/a_pilot_wh_torsion_data.md']

## Statement

The (A) closure's (C1) input cannot be computed by direct elimination (pilot-measured: dead at n = 32). NEEDED: a certificate for 'no non-toral mod-p solutions of the anchored system rem(X^n - 1, S^2 - S(1)^2) = 0' computable at n = 1024, h in the window, for the six official primes. ROUTES: (i) 2-ADIC RECURSIVE DESCENT (most promising): X^n - 1 = (X^{n/2} - 1)(X^{n/2} + 1) — the divisor S^2 - lambda distributes across the dyadic tower in finitely many degree patterns; per pattern the conditions decompose into subproblems at n/2 — D(n,h) as a product of much smaller resultants over descent patterns (the same tower structure that powers every 2-power argument in this campaign); (ii) mod-p elimination for the six specific primes (kills coefficient growth but symbolic degree growth in the 41 squarings remains — feasibility unclear); (iii) the absorbency retreat: even without certificates, bound the multiplicity at possibly-bad primes structurally (A3's G3 gap — currently no tool). Route (i) is the one with a campaign pedigree.

## Attack surface

work out the descent pattern combinatorics at h = 4, n = 32 vs the pilot's computed data (the calibration case exists); if the recursion closes, the n = 1024 certificate is log2(n) = 10 descent levels of bounded work

## Falsifier

the descent producing cross-terms that do not decompose (check at n = 32 against the pilot's exact eliminant)

## Ledger

DECOMPOSED (roadmap-lane, seed identity sympy-verified): C1a — direct MITM certificates at h = 4/5, n = 1024 (FEASIBLE NOW, ~2^35 hash entries; covers the most exposed window sizes); C1b — the descent-injection certificate (trades descend to band pairs via the exact pushforward identity, budget h/2 per level; only 4 levels needed to reach the censusable n = 64; the injection lemma is the one new statement, calibratable against the pilot's exact n = 32 ground truth); C1c — the antipodal branch tracked as paid per level (X24's mechanism); C1d — the interface with the h-window audit (running). ALSO NOTED: at official primes the first-moment gap is 700+ bits per h (unlike the giant regime's razor edge) — if C1b resists, a large-sieve/averaging argument over patterns is the theory fallback. | COVERAGE MAP after the delta-saturation correction: C1a (direct MITM) covers h = 4, maybe 5; C1b (descent) covers h <= ~8-10; h >= ~16 needs the large-h emptiness lemma (route ii) as a third piece IF the window audit's H_max reaches that high. The audit is the decisive pending input. | WINDOW VERDICT: H_max = A. Coverage now: C1a h=4(-5), C1b h<=~10, NEITHER for h in (10, A] — the widened gap is noded (midlarge_h_certification) and goes into the Fable brief.
