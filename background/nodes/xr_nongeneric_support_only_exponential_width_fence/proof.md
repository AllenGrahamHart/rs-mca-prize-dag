# Proof

At each clean-rate root, direct arithmetic gives

```text
2A<=N,       H/A<=1/16.                              (1)
```

Choose `2A` coordinates and partition them into labelled pairs
`{x_i^0,x_i^1}`, `1<=i<=A`. For a binary word `c in {0,1}^A`, put

```text
Y_c={x_i^(c_i):1<=i<=A}.
```

Then `|Y_c|=A` and

```text
|Y_c intersect Y_d|=A-dist(c,d).                    (2)
```

Greedily choose binary words, deleting after every choice all words at
Hamming distance at most `H-1`. This produces a code `mathcal C` of minimum
distance at least `H` and size

```text
|mathcal C|>=2^A/V,       V=sum_(i=0)^(H-1) binom(A,i).   (3)
```

The standard binary entropy bound and `(1)` give

```text
V<=2^(A H_2((H-1)/A))<2^(3A/8).                    (4)
```

For completeness,

```text
H_2(1/16)=1/4+(15/16)log_2(16/15)<3/8.
```

Indeed `(16/15)^15<e<3<4`, so `log_2(16/15)<2/15`.
Monotonicity of binary entropy on `[0,1/2]` proves `(4)`. Hence

```text
|mathcal C|>2^(5A/8).                               (5)
```

By `(2)`, the supports indexed by `mathcal C` satisfy

```text
|Y_c intersect Y_d|<=A-H=K-1
```

for distinct words. Finally, at the six roots the smallest exponent comparison
is the RowC rate-`1/16` row:

```text
5A/8=335/8>34=log_2(16n^3).
```

The other five comparisons are larger, as recorded in the audit table.
This proves `(XEF1)--(XEF3)`. QED.
