# Audit

The proof uses the complete official exponent range `13<=s<=44`, not a
sample of rows. All calculations use Python integers and `isqrt`; there is
no floating-point comparison.

The primary replay solves both Johnson inequalities by exact square-root
intervals. The independent replay instead uses monotonic binary search for
the ordinary Johnson threshold and checks the nearest integers to the vertex
of the convex joint-background quadratic. Both implementations verify the
same empty prefixes and all printed boundary witnesses.

The hostile boundary controls are the first omitted scales `M=13,29,57`.
Each has a `(PF6)` parameter survivor at `n=8192`, so changing any asserted
prefix endpoint upward by one makes both verifiers fail closed.
