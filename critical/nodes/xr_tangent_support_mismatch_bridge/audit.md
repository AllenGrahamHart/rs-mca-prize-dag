# Audit

This is an obligation-preserving contraction, not a proof of an XR count.

The original generic P-A/P-B route allotted `8n^3+8n^3`. The former mismatch
bridge separately requested one combined `16n^3` bound for globally
nongeneric pairs. Requiring each nongeneric high/low stratum to fit `8n^3`
would be stronger and is explicitly rejected. Instead P-A is made a
two-clause target: original generic high-core P-A1, plus the original combined
nongeneric mismatch statement as P-A2. P-B retains its original generic
scope.

The `F_17`, `n=8`, `K=2`, `A=3` regression fixture routes to P-A2. All eight
mismatch slopes remain live; none is discarded merely because the pair is
jointly zero on another support.

The verifier exhausts the generic high/low partition on small set families,
replays the eight-support regression fixture, and checks the case-specific
DAG assembly.
