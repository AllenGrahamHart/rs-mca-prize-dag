# Audit

Run `verify.py` and `verify_audit.py`. The external root packet validates
each profile by the Frobenius identity `gcd(P,x^p-x)` and factors only the
squarefree root part. The local audit checks candidate unions and guard
partitions, rebuilds the source kernel, and directly replays all first-pair
quadratics, missing relations, target boundaries, and colored-pair values.
