# TARGET 2 — THE SUPPORT-FORCING DICHOTOMY. Prove or falsify.

## Setup (self-contained)

Let F = F_p (p an odd prime), H <= F^x a cyclic subgroup of
2-power order n, and M | n with M > 1. Let RS[F, D, k] be the
Reed-Solomon code of degree-< k polynomials evaluated on D = H,
with k < n. For a subset T of D let L_T(X) = prod_{a in T}(X - a).

A received word U: D -> F is arbitrary. For sigma >= 1 let
ImgFib_U(k + sigma) = {codewords f in RS[F,D,k] agreeing with U
on at least k + sigma points of D}. Call f STAIRCASE if the
agreement set {x : f(x) = U(x)} is, up to a tail of size < M, a
union of full fibers of the power map x -> x^M on D (equivalently
its locator has the form L_B(X) G(X^M) with |B| < M). Call f
STABILIZER-PRIMITIVE if its agreement set has trivial stabilizer
under the translation action of the order-M subgroup of H.

## The conjecture (the "top defect band" dichotomy)

There is an absolute constant C such that for every (p, n, M, k,
sigma) as above with M > sigma + 1, every U, and every codeword
f in ImgFib_U(k + sigma) whose agreement set has size in the top
defect band [k + sigma, k + sigma + M - 1]:

    f is STAIRCASE, or f is STABILIZER-PRIMITIVE —

and moreover the number of non-staircase, non-stabilizer-primitive
members of the band is zero (the dichotomy is exact, not
approximate).

## PROVE OR FALSIFY.

Available proved structure (all machine-verified in-repo, in the
E22 packet family and background nodes; use freely):
- Agreement on a petal T_i is equivalent to L_{T_i} | H_i where
  H_i = U L_{Z\C} - a_i L_{C\Z} (cofactor equations; exact).
- The locator of a tail-plus-full-fibers support is L_B(X) G(X^M),
  and for M > t its top t subleading coefficients depend only on
  (B, |H|).
- Staircase codewords are exactly enumerable across scales with no
  hidden multiplicity (a seven-lemma canonicalization ledger,
  verified), and their count C(n/M - 1, k/M) is a proved LOWER
  bound for the full fiber (so any bound ignoring them is false —
  the dichotomy is the only viable shape).
- Empirically (two-regime data, in-repo): staircase counts are
  p-independent; everything else decays with p — consistent with
  the dichotomy and with the primitive branch being "accidents"
  of density O(1/p) per shape.

A falsification means: an explicit (p, n, M, k, sigma, U) with a
band codeword that is neither staircase nor stabilizer-primitive
— or a family showing the band contains super-polynomially many
such hybrids. Either resolution is decisive for the prize node
petal_growth (see notes/kernel_basis/WP6_PETAL_VERDICT.md).

---

## APPENDIX (2026-07-10, internal audit): the BINDING form is the
## all-scales closure, not the fixed-M form above

An adversarial audit of our own consumption chain found a
composition gap in the statement as posed above: fixing one scale
M > sigma + 1 and using trivial-order-M-stabilizer leaves the
scales M <= sigma + 1 (in particular M = 2 at sigma = 1 on 2-power
rows) charged to NEITHER branch, so the per-M dichotomy does not
compose to the aperiodicity charge (c(S) = 1) that the downstream
primitive bound consumes.

The form our proof chain actually needs (now the binding statement,
node petal_g2_support_forcing in the critical DAG) is the CLOSURE
over all dyadic scales:

  at official rows, every top-band full-petal contributor's
  agreement set is STAIRCASE at SOME dyadic scale M >= 2 (tail
  |B| < M plus full M-fibers) OR is APERIODIC (periodicity scale
  c(S) = 1) — exactly, with no third class.

This is deliberately STRONGER than the fixed-M form above. A proof
of the fixed-M form is still valuable partial progress; a
falsification of either form at the stated band is decisive. The
falsifier shape is unchanged: an explicit (p, n, M, k, sigma, U)
with a top-band codeword neither staircase-at-any-scale nor
aperiodic, or a super-polynomial hybrid family.

---

## RESOLUTION APPENDIX (2026-07-10, internal falsification run): the
## fixed-M form is FALSIFIED; the closure form is TRUE but VACUOUS;
## the real problem is re-posed below

**The fixed-M form above is falsified as stated.** Minimal verified
witness: (p, n, M, k, sigma) = (17, 8, 4, 3, 1), D = <9> in F_17^*,
sunflower word U with core {1, 16}, petals {9,8}, {13,4}, {15,2},
scalars (1, 5, 8); codeword f(X) = 4X^2 + 11 agrees with U on
S = {9, 13, 8, 4} (exponents {1,2,5,6}), |S| = 4 = k+sigma, in band;
S contains no full 4-fiber (not staircase at M = 4) and is fixed by
the order-2 shift (not order-M-stabilizer-primitive). 4,550 in-band
instances, 3,661 distinct top-band full-petal witnesses, p-independent.
Self-contained re-verifiers exit 0 (witness at n = 32 with generic
shuffled layout also banked). The "either resolution is decisive"
clause has been exercised: thank you — this materially sharpened our
roadmap.

**The all-scales closure form (the previous appendix) is TRUE but
carries no information at 2-power rows**: any set with periodicity
c >= 2 is a union of full c-fibers, hence staircase at scale c with
empty tail (a one-line corollary of the stabilizer partition theorem
already in the source paper). Machine-confirmed exhaustively over all
2^16 subsets. Do not attack it; it cannot be falsified.

**THE REAL OPEN PROBLEM (new binding target).** At official rows,
every top-band full-petal contributor's agreement set is
STAIRCASE AT SOME DYADIC SCALE M > t (t = the contributor's full-petal
count; strict reading: at least one full M-fiber) OR APERIODIC
(c(S) = 1). The witnesses above show the excluded middle class
(periodic only at scales <= t) is NONEMPTY in engineered charts at
small rows and p-independent — so this statement has real content.
PROVE it (showing small-scale-periodic contributors cannot occur in
the official top band), or FALSIFY it at scale (a super-polynomial
family of scales-<=-t-periodic top-band contributors at official-like
rows would break the pricing route decisively). Alternatively: prove
the small-scale class is polynomially bounded and exactly priced by
the quotient-coset column (the paid-family shape our data suggests).
