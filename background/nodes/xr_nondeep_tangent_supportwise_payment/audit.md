# Audit

`verify.py` exhausts all `C(8,3)=56` exact agreement supports for every one
of the 17 finite slopes. Polynomial interpolation and joint extension are
computed directly over `F_17`; no lattice or heuristic classifier is used.

The verifier also checks the smooth domain, the failed deep hypothesis, the
common six-coordinate pair explanation, the exact eight-slope list, the
distinct low-core witnesses, trivial cyclic stabilizers, and failure of the
`x -> x^2` pullback test.
