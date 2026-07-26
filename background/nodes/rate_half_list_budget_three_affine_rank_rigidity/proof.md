# Proof

Let `A` be the affine span of the four codewords and let `s` be its direction
dimension. Pairwise distinctness gives `s>=1`.

At the parameters

```text
n=4d,       K=2d,       m=3d-1,       w=d-1,
```

the affine-span pencil compiler gives

```text
|L_A(u,m)|<=floor((n-K+1)/(w+1))
            =floor((2d+1)/d)=2.                     (1)
```

Thus `s!=1`. Suppose for contradiction that `s=2`.

Let `C'` be the two-dimensional direction code of `A`, let `G` be its common
zero set, and put `z=|G|`. Locator division gives

```text
z<=K-2=2d-2.                                        (2)
```

Let `g` count the coordinates of `G` where the common affine value agrees
with `u`. At a coordinate outside `G`, agreement with `u` cuts `A` in an
affine codeword pencil. By `(1)`, at most two of the four listed codewords
can agree there. Counting all codeword-coordinate agreements therefore gives

```text
12d-4 <= 4g+2(4d-z).                                (3)
```

Rearranging and using `g<=z` and `(2)` yields

```text
2d-2 <= 2g-z <= z <= 2d-2.                          (4)
```

Every inequality is equality. Hence `z=g=2d-2`, every codeword has exactly
`3d-1` agreements, and every coordinate outside `G` has exactly two agreeing
codewords.

Let `Q` be the locator of `G`. Every polynomial in `C'` is divisible by `Q`.
Since `deg Q=2d-2`, division embeds `C'` into the two-dimensional space of
polynomials of degree below two. Dimensions are equal, so

```text
C'=Q F[X]_<2.                                       (5)
```

Write the four codeword polynomials as

```text
c_i=c_*+Q ell_i,                                    (6)
```

where the `ell_i` are four distinct affine-linear polynomials. At each
`x in D\G`, exactly two codewords, say `i,j`, agree with `u`, so
`ell_i(x)=ell_j(x)`. A fixed nonzero affine-linear difference
`ell_i-ell_j` has at most one root. Thus the `2d+2` coordinates outside `G`
inject into the six unordered pairs `{i,j}`. This gives

```text
2d+2<=6,
```

contrary to `d>=3`. Therefore `s=3`, proving `(ARR2)`. QED.
