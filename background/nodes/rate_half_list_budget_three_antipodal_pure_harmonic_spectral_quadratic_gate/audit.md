# Audit

The factors in `(HSQ2)` represent a partition of the four deleted roots, not
an arbitrary factorization over an extension. The official deleted quartic
is split and squarefree, so there are exactly three unordered splittings.

The displayed formula is asymmetric in the two written factors, but its
value is their intrinsic eight-sign pairing norm. Exchanging the factors or
the roots within either factor leaves it unchanged. The verifier checks all
such reorderings independently.

Squaring the harmonic equation in `(3)` does not introduce solutions: `(3)`
is used as the product of the two complementary sign equations, and the two
subsequent quadratic norms multiply all eight sign classes. Vanishing of the
final field product therefore still means that an original sign equation
vanishes.

This node couples exact tests; it does not prove scarcity. The next useful
theorem must retain the succinct passport representation while showing that
the fourth-power spectral tests and `(HSQ3)` cannot hold together.

The deterministic toy pilot exhausts all `70` supports at `d=8` over four
admissible fields and all `1820` supports at `d=16` over three admissible
fields. No support passes the combined gate. Harmonic supports are nevertheless
abundant in several rows, confirming that the fourth-power coupling supplies
the observed rejection. At `d=16`, the degree-three polynomial `B` is fixed
by the first three quotient coefficients because `Z^4` begins in degree four;
this shortcut does not extend unchanged once `r>=4`. The counts are evidence,
not part of the proof, and replay from
`experiments/prize_resolution/rate_half_pure_harmonic_fermat_combined_gate_pilot.py`.
