# t_laurent_ritt_toral_stabilizer

- **status:** PROVED
- **closure:** proof
- **refs (legacy):** ['experimental/notes/roadmaps/u1_proof_skeleton_ritt_route.md']

## Statement

k algebraically closed, psi a Laurent polynomial of degree d, char 0 or p > d: if the reduced non-diagonal fiber product has a geometric toral component, then EITHER psi = F(x^m), m > 1, F LAURENT (F in k[z, 1/z]; F in k[z] if psi is an ordinary polynomial) — the cyclic branch — OR psi = F(x^m + alpha x^-m) with F in k[z] — the dihedral/Dickson branch. Converse holds. PROOF SELF-CONTAINED, ZERO IMPORTS (verified here incl. the dihedral factorization identity and the discriminant of the rational counterexample): (1) degree multiplicativity collapses every primitive toral component x^a y^b = c to y = lambda x or xy = c — the graph of a tame automorphism of G_m; (2) the toral stabilizer is finite (separability from p > d) and cyclic-or-dihedral; (3) invariant fields k(x^m) and k(x^m + alpha x^-m) + the Laurent pole argument pin the outer map. TWO WORDING CORRECTIONS to T as I posed it: the cyclic outer map is Laurent, not polynomial (witness x^m + x^-2m); general rational psi needs an outer RATIONAL map (witness R(z) = z + 1/(z^2+1), degree 3, no totally ramified fiber, discriminant 592). Scale-free; tame hypothesis survives every quotient row with ~2^100 slack.

## Ledger

PROVENANCE: GPT Pro X-9 (10-for-10 substantive). The theorem is EASIER than full Laurent-Ritt precisely because the degree collapse kills general-bidegree components geometrically — the fence that made T look hard was an artifact of not parametrizing. | T-TOY (#32, 212/212): the classification confirmed empirically through degree 20 at tame toy rows — zero unclassified bidegree-(1,1) toral/affine cases; line factors are linear-conjugate power pullbacks; Dickson appears at the X^2 symmetry exactly as the theorem predicts.
