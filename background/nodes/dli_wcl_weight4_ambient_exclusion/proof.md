# Proof certificate

Encode a negative reduced term `-X^e` by the full exponent `e+256` in
`Z/512`. A reduced weight-4 polynomial is then a four-set with no antipodal
pair, modulo translation by 256 (global sign).

For an ordered non-antipodal pair `(x,y)`, write
`y-x=2^v u mod 512`, where `0<=v<=7` and `u` is odd modulo `2^(9-v)`.
Choose an odd `a` with `au=1 mod 2^(9-v)` and translate by `-ax`. The pair
becomes `(0,2^v)`. Thus every affine orbit meets the normalized section used
by the compiler. The independent verifier reconstructs all 1,014,080 section
keys, generates every normalized transform of each listed representative,
and proves that the 24,979 disjoint normalized orbits exhaust the section.
The normalization argument then proves coverage of all 1,398,341,120 raw
supports without enumerating that raw universe.

Modal/FLINT computes one resultant per class and PARI factors it. The ledger
verifier independently checks the resultants. For each deterministic prime
`p=1 mod 512`, it evaluates `P` at all 256 odd powers of an exact order-512
root in `F_p`; their product is `Res(X^256+1,P) mod p`. Vectorized batches do
this for every class. The CRT modulus exceeds `2*4^256`, while the product of
the 256 complex conjugate magnitudes is at most `4^256`, proving exact integer
equality.

The factor products reconstruct those exact norms. The second verifier checks
all 154,086 recursive Pocklington nodes: complete factorizations of `r-1`,
recursive primality of every divisor, Fermat congruences, and the required gcd
conditions. Hence all 44,599 factor roots are prime. Direct inspection gives
zero factors below `2^256` with 41-bit splitting and maximum depth 29.

If an official-row weight-4 relation existed at an order-512 root in `F_q`,
then `q` would divide its certified cyclotomic norm. The official ambient
split requires `2^41|q-1`, contradicting the exhaustive factor ledger.
