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
