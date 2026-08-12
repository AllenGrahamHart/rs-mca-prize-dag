# Audit

1. Exact root multiplicity two is used to isolate a quadratic Hensel
   factor; the complementary factor is not silently included.
2. `F_0=b+c_0R(z,0)` rather than literally `b`; since `ord c_0=6` and
   `ord F_0=2`, the remainder coefficient `b` still has exact order two.
3. The trace estimate is checked separately for two unramified branches
   and one tame ramified branch; odd residue characteristic is explicit.
4. Original-source separation is not used. A unit `a(0)` is retained as the
   regular-corank-one profile `[4]`.
5. The determinant has a unique order-four leading term `b^2` in all three
   valuation ranges.
6. Explicit two-branch and tame-ramified fixtures realize all residual Smith
   profiles, so none is promoted to an exclusion.
