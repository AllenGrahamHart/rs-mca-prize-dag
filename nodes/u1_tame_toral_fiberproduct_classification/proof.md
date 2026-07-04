# proof: u1_tame_toral_fiberproduct_classification

- **status:** PROVED
- **closure:** proof

## Source

Vendored from the working record; primary artifact(s):
- `experimental/notes/roadmaps/u1_proof_skeleton_ritt_route.md`

## Ledger

LITERATURE SEARCH RESOLVED THE ROUTE (roadmap-lane, web-verified to exist; exact statements to be pulled from the PDFs before use): (1) Zannier, 'Ritt's Second Theorem in arbitrary characteristic', Crelle 445 (1993) 175-203 — Ritt II in char p under tameness; (2) Kulkarni-Muller-Sury, 'Quadratic factors of f(X) - g(Y)' — Bilu's classification EXTENDED TO ARBITRARY CHARACTERISTIC (the bidegree-(1,1) toral case directly); (3) Turnwald's Dickson/Schur treatment for the Dickson normal forms; (4) Fried-Guralnick-Saxl + Klyachko for the exceptional direction (degree coprime to p: compositions of monomials/Dicksons exhaust). THE ASSEMBLY: toral factor x^a y^b = c => monomial substitution => Laurent functional equation => Zannier char-p Ritt II + Turnwald => monomial/Dickson. THE COMPLICATION FOUND: Zieve's 'Decompositions of Laurent polynomials' (the natural one-shot import) is CHARACTERISTIC 0 (built on Bilu-Tichy) — cannot be imported directly; the route goes through Zannier + substitution instead. THE TWO SEAMS THAT ARE OURS: (a) lifting general bidegree (a,b) toral factors to the quadratic/KMS case via the substitution (elementary-looking, needs writing); (b) the bounded-tails robustness wrapper. Status upgraded TARGET -> PROVABLE: an assembly task with named sources, not an open import. | T IS NOW ASSEMBLED MODULO ONE LEMMA: toral branch PROVED (t_laurent_ritt_toral_stabilizer — cyclic/dihedral pullback exactly); many-fibers branch = the verified subgroup-point bound with the corrected max{n^{2/3}, n^2/p} threshold (satisfied at the candidates by ~200 bits) forces a toral component, then the theorem applies; REMAINING: the bounded-tails wrapper (fibers-minus-B-points incidence loss — lemma-sized, named in X-8). Status TARGET -> CONDITIONAL on the tails wrapper. GRAMMAR NOTE: v1's charged forms should read outer-LAURENT in the cyclic branch per the X-9 correction.
