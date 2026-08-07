#!/usr/bin/env python3
"""GS-FLOOR OBSTRUCTION (named functional GSFLOOR(h) ).

The cheapest imaginable emptiness certificate for "no lattice vector of
Euclidean norm <= R" is the Gram-Schmidt floor
        lambda_1(Lambda) >= min_i ||b*_i||,
which is a 64-number certificate needing no enumeration at all.  Because
        prod_i ||b*_i|| = det(Lambda) = p,
we always have  min_i ||b*_i|| <= p^{1/h}  (geometric mean), for EVERY
basis.  So the GS floor can certify  lambda_1 > R = 2 sqrt(h)  only if

        p^{1/h} > 2 sqrt(h)   <=>   p > (2 sqrt h)^h = (4h)^{h/2}.

But (4h)^{h/2} is EXACTLY the AM-GM ceiling MAXNORMCEIL(h) above which
the round-22 norm criterion already certifies the row for free
(|Norm(w)| <= (4h)^{h/2} for every w in the box, by AM-GM on the h
archimedean absolute values, each <= 2 sqrt(h)).

CONSEQUENCE: the two cheapest certificate families have the SAME
threshold.  There is no window in which the GS floor works and the norm
bound does not.  On the whole admissible range the prize spec allows
(|F| < 2^256, background/nodes/official_row_primes_pinning/proof.md:27-30)
no N'=128 row admits either -- a COMPLETE enumeration is the only member
of this family that can decide those rows.  This is why the deliverable
had to be an enumeration transcript and not a bound.
"""
import math

print("== GSFLOOR(h) vs MAXNORMCEIL(h) ==")
print("%-6s %-8s %-16s %-16s %-8s" %
      ("h", "N'", "GSFLOOR = (2 sqrt h)^h", "MAXNORMCEIL=(4h)^{h/2}", "equal?"))
for h in (4, 8, 16, 32, 64, 128, 256):
    a = h * math.log2(2 * math.sqrt(h))
    b = (h / 2.0) * math.log2(4 * h)
    print("%-6d %-8d 2^%-14.4f 2^%-14.4f %-8s"
          % (h, 2 * h, a, b, abs(a - b) < 1e-9))

print("""
So GSFLOOR(64) = MAXNORMCEIL(64) = 2^256 exactly.

  - the prize field cap is |F| < 2^256
    (official_row_primes_pinning/proof.md:27-30: `|F| < 2^256`),
  - the PROVED high-field branch needs p > 253^32 = 2^255.4558
    (integer_code_distance_high_field_folded_box_exclusion),
  - so the free region is the 0.5442-bit sliver
    [2^255.4558, 2^256) intersect the admissible range, and NOTHING in
    the GS/norm family reaches below it.

Every N'=128 row with p < 2^255.4558 -- which includes the pinned E1
250-bit exhibit (2^249.000) and all four deployed Proth prize rows
(2^166.503 .. 2^170.503) -- requires a complete enumeration or a genuinely
new theorem.  A basis-quality improvement can make the enumeration
CHEAPER but can never replace it with a GS floor.
""")

print("-- and the same statement per row --")
for (nm, lp, h) in [("E1-128 pinned", 249.000, 64),
                    ("PROTH 1/2", 166.503, 64), ("PROTH 1/16", 170.503, 64),
                    ("corridor", 255.900, 64),
                    ("RowC (I_C floor)", 250.0, 64)]:
    best = lp / h                      # log2 of the best possible min||b*_i||
    print("   %-18s log2 p=%-8.3f  best possible min||b*_i|| = p^(1/64) = "
          "%.4f   vs R = 16  -> GS floor %s"
          % (nm, lp, 2 ** best, "WORKS" if 2 ** best > 16 else
             "CANNOT WORK FOR ANY BASIS"))
