# Result

The torsion-only characteristic sieve is now split into its exact dyadic
cyclotomic pieces. The minus sign is one order-`2^38` norm, while the plus
sign is a 36-level norm tower through order `2^37`. Odd-prime valuations are
twice the valuations of the corresponding Jacobi/Chebyshev resultants.

The plus tower is equivalently a product of `36` trace resultants against
`T_1,T_2,...,T_(2^35)`. This halves the largest plus-branch torsion degree
and permits exact level-by-level short-circuiting.

Over the official field, the minus branch is likewise two degree-`2^35`
trace resultants whose quadratic norm is `R_-`. Thus neither sign requires a
torsion polynomial of degree greater than `M` in a modular implementation.

This replaces an infeasible integer-resultant output contract by a modular
norm-certificate interface. It does not exclude an official characteristic.
