# Audit

1. Each source completion maximum is an integer in `0..q`.
2. Defects `0..9-c` and fallback `M_c<=q-(10-c)` are disjoint and exhaustive.
3. The replacement leaf count is `11-c`.
4. Every child retains every parent cap.
5. Terminal leaves use both their source ceiling and all valid carrier caps.
6. Fallback leaves use only their valid source deletion ceiling.
7. The statement makes no row-payment claim.
