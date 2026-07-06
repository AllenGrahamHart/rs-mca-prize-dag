# u1_tame_toral_fiberproduct_classification

- **status:** PROVED
- **closure:** proof
- **refs (legacy):** ['experimental/notes/roadmaps/u1_proof_skeleton_ritt_route.md']

## Statement

deg psi < p, D = gamma mu_n, p coprime to n: if psi's non-diagonal fiber product has a toral component x^a y^b = c, or psi has > poly(deg) n^{2/3} full D-fibers, then psi is v1-chargeable (monomial/power or Dickson/Chebyshev pullback, up to linear conjugacy, coset scaling, bounded tails). STRONGER than Ritt's Second Theorem (which IS verified: tame composition collisions of coprime degrees are monomial-or-Dickson, von zur Gathen normal forms); the needed form is a Laurent/toral statement — Zieve's Laurent-polynomial decompositions are the right orbit, unverified at this exact strength. CORRECTED WORDING (per X-7): Frobenius/additive wild composition is excluded by deg < p; tame exceptional families (monomial, Dickson) are the DICTIONARY, not absent phenomena. X-8 CORRECTIONS: (i) the exact-polynomial toral case is PROVED and gives MONOMIAL ONLY (t_poly_exact_toral) — Dickson requires the Laurent/rational case, so the load-bearing missing theorem is a POSITIVE-CHARACTERISTIC LAURENT-RITT statement (named; Zannier's polynomial Ritt II does not cover it); (ii) the many-fiber threshold MUST carry the n^2/p term: the trigger is K > C(d) max{n^{2/3}, n^2/p}, equivalently the hypotheses need p >= C(d) n^{4/3} — SATISFIED at the six candidates by ~200 bits (p ~ 2^250 vs n^{4/3} = 2^54.7) but low-q admissible rows are NOT covered (the same low-q danger zone as the boundary column); (iii) the bounded-tails wrapper is a named missing lemma (fiber-minus-B-points incidence loss). T = one proved subtheorem + conditional assembly on {Laurent-Ritt, corrected threshold, tails lemma}.

## Attack surface

literature verification first (Zieve, Laurent decompositions; Bilu-Tichy orbit); else prove directly: a toral component gives a multiplicative identity between root multisets of psi - y — push through the tame normal forms

## Falsifier

a tame-degree psi with toral fiber-product component that is NOT monomial/Dickson-conjugate (searchable at toy degrees)

## Ledger

LITERATURE SEARCH RESOLVED THE ROUTE (roadmap-lane, web-verified to exist; exact statements to be pulled from the PDFs before use): (1) Zannier, 'Ritt's Second Theorem in arbitrary characteristic', Crelle 445 (1993) 175-203 — Ritt II in char p under tameness; (2) Kulkarni-Muller-Sury, 'Quadratic factors of f(X) - g(Y)' — Bilu's classification EXTENDED TO ARBITRARY CHARACTERISTIC (the bidegree-(1,1) toral case directly); (3) Turnwald's Dickson/Schur treatment for the Dickson normal forms; (4) Fried-Guralnick-Saxl + Klyachko for the exceptional direction (degree coprime to p: compositions of monomials/Dicksons exhaust). THE ASSEMBLY: toral factor x^a y^b = c => monomial substitution => Laurent functional equation => Zannier char-p Ritt II + Turnwald => monomial/Dickson. THE COMPLICATION FOUND: Zieve's 'Decompositions of Laurent polynomials' (the natural one-shot import) is CHARACTERISTIC 0 (built on Bilu-Tichy) — cannot be imported directly; the route goes through Zannier + substitution instead. THE TWO SEAMS THAT ARE OURS: (a) lifting general bidegree (a,b) toral factors to the quadratic/KMS case via the substitution (elementary-looking, needs writing); (b) the bounded-tails robustness wrapper. Status upgraded TARGET -> PROVABLE: an assembly task with named sources, not an open import. | T IS NOW ASSEMBLED MODULO ONE LEMMA: toral branch PROVED (t_laurent_ritt_toral_stabilizer — cyclic/dihedral pullback exactly); many-fibers branch = the verified subgroup-point bound with the corrected max{n^{2/3}, n^2/p} threshold (satisfied at the candidates by ~200 bits) forces a toral component, then the theorem applies; REMAINING: the bounded-tails wrapper (fibers-minus-B-points incidence loss — lemma-sized, named in X-8). Status TARGET -> CONDITIONAL on the tails wrapper. GRAMMAR NOTE: v1's charged forms should read outer-LAURENT in the cyclic branch per the X-9 correction.
