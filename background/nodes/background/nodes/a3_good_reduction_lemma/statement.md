# a3_good_reduction_lemma

- **status:** PROVED
- **closure:** proof
- **refs (legacy):** ['experimental/notes/roadmaps/x83_uniform_square_shift_obstruction_gate.md']

## Statement

For p outside a finite, h-only, row-independent exceptional set S(h) — primes dividing explicit nonzero integers (discriminants/resultants of W_h's non-toral components and torsion-coset membership data) — the mu_n(F_q)-points of W_h do not exceed the char-0 structure: no new trades appear mod p. This is the exceptional-prime phenomenon (F_193, the q-sweep non-monotonicity, X-6) in its proper algebro-geometric form. TWO EXITS: (i) bound S(h)'s defining integers below 2^128 (heights ~ exp(poly(h)): plausible at small h, unclear at h ~ 40); (ii) THE FALLBACK THAT ALWAYS WORKS: compute S(h)'s integers ONCE per h (row-independent, reusable), then per-row certification = GCD/divisibility tests — trivial arithmetic. x83's triangularity makes the eliminant chain computable. PROVED AT FIXED (n,h) (Fable agent, 14/14 replayed; biconditional validated at (16,3): exceptional set exactly {7,17,97} matching brute-force both directions). LEMMA 0 (structural): W_h is a GRAPH in coefficient space (O_j = P_j(c_h..c_{2h-1}) - c_j); anchored torsion intersection = rem(X^n - 1, S^2 - S(1)^2) = 0. D(n,h) pointwise-minimal + computable RUR-certificate integer (identity-checked; Rouillier provenance-only G1). Torsion rigidity elementary, both q = p^2 splits. CORRECTIONS: h-only n-uniformity PROVED FALSE (G4, quarantined); Laurent OFF the critical path (G2 — X24 suffices at fixed n, char-0 set EMPTY at window sizes). Gaps G1-G5 named; G5 = the pilot certificates (computation).

## Attack surface

formulate via the triangular eliminant chain (each obstruction eliminates one variable); the components' torsion data reduces to resultants against X^n - 1 evaluated on the h-only component ideals; small-h (4,5,6) computations first to calibrate integer sizes

## Falsifier

an official-row prime dividing one of S(h)'s integers at some window h (= a real trade at that row; then charge it, absorbency has n^3 room)

## Ledger

PILOT RESULTS (7/7 replayed, every claim by two independent methods): obstructions built two ways byte-identical; isobaric weights confirmed; fiber vanishing verified. CHAR-0 CENSUS EXACT: h=4 non-toral torsion EMPTY at n = 16/32/64 (toral count exactly C(n/4,2)); h=5, h=6 entirely empty — X24 confirmed, no banked theorem contradicted. FEASIBILITY VERDICT (decisive NEGATIVE): the brute eliminant route to D(n,h) dies at n=32 (first elimination >150s; coefficient bits double per n-doubling: 9/22/51 at 16/32/64 => ~800+ bits at 1024); the census route is exact only to n ~ 64-128. THE (C1) COMPUTATION AS POSED IS INFEASIBLE AT n = 1024 FOR ALL h.
