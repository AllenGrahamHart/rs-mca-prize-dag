# Audit

Run `verify.py` and `verify_audit.py`. The external root packet validates
each profile by the Frobenius identity `gcd(P,x^p-x)` and factors only the
squarefree root part. The local audit checks candidate unions and leading
boundaries, rebuilds the source kernel, and directly replays all first-pair
quadratics, missing relations, recovered variables, and colored-pair values.
