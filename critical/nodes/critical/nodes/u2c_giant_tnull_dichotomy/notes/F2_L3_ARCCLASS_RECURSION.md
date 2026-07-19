# F2 campaign L3: the ARC-CLASS RECURSION LEMMA
# (+ CATCH: the design note's "structured arcs exactly computable"
#  claim corrected — per-arc values are infeasible at official scale;
#  the class MASSES are what the assembly needs, and they recurse)

Status: PROVED (one-line orthogonality, proof inline) +
machine-verified exactly (f2_l3_arcclass_recursion_modal.py, digest
F2_L3_ARCCLASS_RECURSION_PASS).

## Catch (banked per protocol)

F2_L3_DESIGN.md claimed the structured arcs (linear l2=0, quotient
l1=0) "enter the assembly as exact terms — no estimates needed". At
calibration scale true; at OFFICIAL scale computing a single e_b at
mid-band b costs ~n*b = 2^80+ operations — infeasible. The claim is
corrected here: the assembly never needs per-arc values, because the
class masses collapse by orthogonality.

## Lemma (arc-class recursion)

For the t = 2 moment map Phi = (p1, p2) on weight-b subsets of mu_n:

  (1/q^2) sum_{l1 in F_q} E_b((l1, 0))  = (1/q)   #{S : p1(S) = 0}
  (1/q^2) sum_{l2 in F_q} E_b((0, l2))  = (1/q)   #{S : p2(S) = 0}
  (1/q^2) sum_{all lambda} E_b(lambda)  =          #{S : p1 = p2 = 0}.

Proof. sum_{l} psi(l * v) = q * 1_{v = 0}; exchange the (finite) sums
over S and lambda. QED

Hence the exact inversion regrouping (all terms EXACT, no estimates):

  N_b^{(2)}(0) = C(n,b)/q^2                       [lambda = 0]
    + [ N_b^{(p1)}(0)/q - C(n,b)/q^2 ]            [linear class]
    + [ N_b^{(p2)}(0)/q - C(n,b)/q^2 ]            [quotient class]
    + (1/q^2) sum_{l1 != 0, l2 != 0} E_b(lambda)  [generic class]

where N^{(p_j)}(0) = #{S : p_j(S) = 0} are the ORDER-1 censuses. The
t = 2 structured mass IS the t = 1 problem: the hierarchy recurses,
t -> its order-<t sub-censuses, with only the GENERIC class left as
an estimate target at each level. (General t: each proper subset J of
{1..t} contributes its own sub-census by the same one-line argument —
inclusion-exclusion over condition subsets.)

## What this changes for the assembly (L5 shape, updated)

extras bound at level t = exact recursion to level-1 censuses
  + generic-class mass  (chord-orbit lemma + Weil-Newton at extreme
    bands; mid-band = the M1 flatness obligation)
Level-1 censuses: p2's is a doubled level-1 p1-census on mu_{n/2}
(double cover, exact); p1's is the single-linear-condition census —
its own mid-band needs the same M1 mechanism at t = 1, the EASIEST
instance. So M1's target instance is now t = 1: prove the flatness /
0-fiber pricing for #{S : sum(S) = 0} first, then lift through the
recursion. Mildest-instance ordering, again.

## Replay

    ~/.venvs/modal/bin/modal run critical/nodes/u2c_giant_tnull_dichotomy/notes/f2_l3_arcclass_recursion_modal.py

Digest: F2_L3_ARCCLASS_RECURSION_PASS. Gates: all three identities
exact (integer DP censuses vs float arc sums, < 1e-6) at 6 cells; the
regrouped four-term decomposition reproduces N(0) exactly.
