# ATTACK — petal_excess_induction (medium; the induction STEP)
Bridge petal_fixed_excess (PROVED, c fixed) -> growing excess c, with poly(n)
constants uniform in c. This is an INDUCTION: the scan gives base cases c=2..8
(evidence, cannot close). Write the mixed-amplification induction STEP: assume
the bound at excess c, prove it at c+1 with the constant not blowing up.
route_exact_rank is REFUTED, so the step needs the residue-line / L1 coset-
chart bridge (Vadim's), not rank counting. If counts are flat in c (scan), the
step's shape is right; write it. If the residue-line count grows with c, that
growth IS the obstruction — report it precisely.
