# Audit

Run `verify.py` and `verify_audit.py`. The independent audit checks the AST
adapter and separate SymPy/Galois-tools root-reconstructor boundaries,
validates every polynomial hash and shape, checks complete candidate-root
coverage and each leading-boundary transport, then rebuilds the source
kernel and directly replays all equations at the eight `(z,q)` lifts and 32
final lanes.
