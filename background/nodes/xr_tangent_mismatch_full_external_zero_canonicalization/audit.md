# Audit

The earlier reduction allowed any `W=S\T`; this strengthening uses all zeros
of `q_z` outside `T`. Since the full zero count can only increase, the
guaranteed internal agreement `A-|S\T|` is at least `A-|Z_z|`, while degree
and dimension fall by the same amount.

`verify.py` exhausts all nonzero degree-below-three polynomials, four-point
witnesses, and discrepancy sets on a six-point `F_7` domain. It includes
cases where the full zero set strictly contains the witness-selected subset.
