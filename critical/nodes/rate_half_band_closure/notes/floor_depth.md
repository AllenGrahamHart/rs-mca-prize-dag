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

## The q-threshold (second Modal run — the refinement, now exact)

Parameterizing box charge (log2 q per fiber) and trigger (log2 q - 40):
the floor family's reach covers sigma* for ALL admissible fields with
log2 q <= 255.900 (depth 8,592,916,480 > sigma* at the threshold; falls
354 short just above). Verifier: verify_q_threshold_modal.py.

CONSEQUENCE: the rate-1/2 band is OPEN ONLY for q in (2^255.9, 2^256) —
the top 0.100 bits of the admissible range. Everywhere below, the clean
rate-1/2 determination corridor closes by the same scale-free floor as
the other rates. The battlefield node's honest statement shrinks to:
cover 2.98M radii for fields within a factor ~1.07 of the size cap.
The legitimacy of per-q parameterization rests on the sweep's proved
hypothesis audit (the floor is scale-free; q enters only via trigger+box).
