# Proof

Use the same positive fixed-moving source reconstruction and finite incidence
chart as the direct-square theorem. The parent reconstruction and q-slice
nodes supply the nonzero source determinant and the forced factor
`(W-w)^2` at each root of `q=(T-c)(T-d)`.

Write the residual quadratic at a q-root `r` as
`A_r W^2+B_r W+C_r`. The swapped assignment is equivalent to

```text
C_c-d^(-2)A_c=0,       B_c+2d^(-1)A_c=0,
C_d-(1/2)^2A_d=0,      B_d+A_d=0.                 (1)
```

Each constant-to-leading equation in `(1)` is the nonzero finite-incidence
factor `H^2` times two lines in `b`. For each of their four pairings, the
`b`-resultant consists of one bidegree `(2,2)` or `(3,2)` curve and excluded
factors among

```text
c-1, d-1, d+1, cd-1, 5cd-4c-4d+5.                (2)
```

On the generic part of a selected left line, solve its full coefficient
equation for `b(c,d)` and substitute in the two middle equations. Eliminating
`c` against the residual curve gives

```text
line pair    resultant degrees    gcd degree    squarefree support
(0,0)             (16,34)             16        d=2,1,-1,1/2
(0,1)             (18,42)             16        d=2,1,-1,1/2
(1,0)             (24,34)             12        d=1,-1,1/2
(1,1)             (28,42)             14        d=2,1,-1,1/2.
```

Hence no generic pairing is admissible. Resultants are used only in their
necessary direction, so a leading specialization of the curve or a middle
polynomial is not discarded.

For a left line `L_1(c,d)b+L_0(c,d)`, cover the exceptional locus by imposing
`L_1=L_0=0` before solving for `b`. For the second line,

```text
Res_c(L_1,L_0) ~
(d-2)^3(d-1)^7(d+1)^5(2d-1)^3,
```

which is entirely forbidden. For the first line the same resultant is

```text
(d-2)^3(d-1)^5(d+1)^5(2d-1)^3(17d^2-38d+17).
```

On the last factor, a lex basis is exactly `(KBNSW-3)`. Reducing
`5cd-4c-4d+5` by that basis gives zero, so the entire extra component has
`z=1` and is inadmissible.

The independent audit eliminates the same exceptional loci in `d`. Its
first extra factor is `7c^2-22c+7` and again reduces the `z=1` factor to zero.
For the second line, the only extra `c` values are `-1/2` and `-2`; their
fibers force `d=2` and `d=1/2`, respectively.

Finally, both implementations clear rational coefficient denominators and
repeat their gcd support checks modulo `p=2130706433`. Thus the exclusion
holds over the algebraic closure of `F_p`, in particular over `F_(p^6)`.
QED.
