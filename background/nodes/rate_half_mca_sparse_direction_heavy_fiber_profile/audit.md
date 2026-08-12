# Audit

The primary checker evaluates `(HF1)` with exact binomial integers, scans
every support size in each certified prefix through its adjacent failure,
checks prefix monotonicity, pins both supplier statements and proofs, and
rejects four mutations.

The independent checker recomputes every printed adjacent boundary using
gcd-cancelled products.  It also brute-forces small cumulative-cap
allocation problems to check the telescoping linear-program formula
independently, and rejects three contract controls.

Both checks are bounded integer arithmetic under RAMguard.  No Modal
compute is used.
