# Proof

Trial division proves `33409` prime. Since

```text
33408=2^7*3^2*29,
```

the checks

```text
7^(33408/p) != 1 mod 33409       for p in {2,3,29}
```

show that `7` is primitive. Hence

```text
zeta=7^(33408/32)=7473 mod 33409
```

has exact order 32; directly `zeta^16=-1` and `zeta^32=1`.

Split the 32 coordinates into two sets of 16. Enumerate the `2^16` subset
sums of the pairs

```text
(zeta^i,zeta^(2i)) in F_q^2
```

on each half and convolve opposite syndromes. This gives `Z_0=384`. On the
antipodal owner, odd moments vanish and the even moment becomes the one-
moment order-16 census on `zeta^2`; independent enumeration gives `C_1=256`.
Thus the primitive count is 128.

For completeness, let `h_even(s)` count subsets of
`{zeta^(2i):0<=i<16}` with sum `s`, and let `h_odd(s)` count subsets of
`{zeta^i:0<=i<16}` with sum `s`. The level-one and odd-band binary counts are

```text
Z_1=sum_s h_even(s)h_even(-s)=1696000,
B_0=sum_s h_odd(s)^2=174912.
```

Substitution into the ambient and Haar identities gives

```text
33409^2*128/2^32 = 1116161281/33554432 > 8,
128*2^32/(1696000*174912) = 33554432/18106125 < 8.
```

Both comparisons are exact integer comparisons. This refutes `(AQSQRT)` and
simultaneously proves that the same row does not refute the Haar square-root
candidate.

