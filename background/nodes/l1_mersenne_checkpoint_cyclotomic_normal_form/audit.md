# Audit - Mersenne-checkpoint cyclotomic normal form

1. The frequency decomposition uses `N=p+1`, not `p`, and all congruences in
   the first coordinate are modulo `m`.
2. The endpoint residues `b=1,N-1` have only one initial source, but the two
   general residue classes coincide modulo `g_b=2`; no exception is hidden.
3. The `b=0` chamber contributes `m-1` complementary frequencies and is not
   governed by the `g_b` formula.
4. The verifier compares the formula with direct orbit closure on multiple
   small powers of two and checks the nine official tuples from the atlas.
5. The Vandermonde bound uses only the full consecutive block at `q=0`; it
   does not claim that the entire closure is a BCH interval.
6. The analogue census is separated as evidence and cannot promote this
   theorem or L1.
