# Claim contract

## Input

`e1_prize_n256_s18_variance_cofactor_windows`, including the exact residual
`V in {10,18}` for cofactor `1028` and the singleton-separation interpretation
of `v_2(m)=2`.

## Output

Cofactor `1028` is impossible for a prize-envelope `N=256`, profile `(4,2,0)`
collision.

## Guards

1. The 320292000 count is a normalized-vector search space, not a class-pair
   or weighted-edge count.
2. Normalization is used only for emptiness; no orbit-size claim is made.
3. The finite-field test exhausts all 128 primitive roots modulo 257.
4. Divisibility by 257 is necessary because `257|1028`; it is not asserted to
   be sufficient for a prize collision.
5. The other five cofactor classes and every RowC class remain open.

## Falsifier

A normalized profile `(4,2,0)` vector with `V in {10,18}` and
`F(3^u)=0 mod 257` for an odd `u`, or a coverage mismatch in either census.
