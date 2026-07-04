# The band IS the floor's shadow (Modal run, exact verdict)

Computation: max over all 2-power scales c of the quotient-remainder floor's
reach d_max(c)*c at rate 1/2 (n = 2^41, k = 2^40, box 2^256, trigger 2^216).
Verifier: verify_floor_depth_modal.py (Modal app rs-mca-floor-depth; lgamma
log2-binomials, margins reported per scale).

RESULT: max depth = 2^33 = 8,589,934,592 EXACTLY, achieved on the plateau
c = 2^22 .. 2^33 (margins ~35 bits at d_max; the next fiber fails by ~-220
bits — the box charge quantizes depth in units of c and the entropy budget
tops out at n/256).

sigma* - 2^33 = 2,978,146: the banked 2,978,147-radius band is exactly the
residual between the floor family's maximal reach and the crossing (off-by-
one = endpoint convention; interval [2^33 + 1, sigma*] inclusive).

CONSEQUENCE (route 1 of the attack surface CLOSED): "extended quotient
scales" cannot cover the band — the scale-free floor family's reach is
capped at n/256 by arithmetic, and the band is definitionally its shadow.
Remaining routes: averaged conversion at giant M; B2b-style balance
analysis; or the safe side pushed down through sigma*.

QUEUED REFINEMENT (do NOT cite until run): depth scales as ~ n/log2(q), so
the band should CLOSE for admissible fields with log2 q below ~255.91 —
if exact, the rate-1/2 open band exists only for q in the top ~0.09 bits
of the admissible range, and the determination is complete below it.
