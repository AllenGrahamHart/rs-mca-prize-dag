# Proof

The exact local-norm and field-floor classification gives the seven possible
cofactors

```text
{2,514,1538,4,1028,16,256}.
```

The variance/cofactor theorem excludes `1538`. Its proved exhaustive children
exclude `1028`, `514`, and `256`. The analytic/exhaustive split for `m=16`
reduces to 540,332 residual vectors and its dual exact resultant ledger
excludes all of them. The corresponding `m=4` and `m=2` splits reduce to
21,376 and 511,272 vectors; independent FLINT/PARI ledgers put every quotient
outside the exact prize interval. This exhausts the seven-element cofactor
list, proving profile `(4,2,0)` empty on prize-envelope rows.

For the binding row, put `h=128`, `ell=33`, and

```text
E_max=65127585921474870475467050631501738502567.
```

The weighted-kernel dictionary assigns profile `(a,b)` the exact multiplicity

```text
M_33(a,b)=sum_(j=0)^b sum_(r=0)^(128-a-b)
 binom(b,j) binom(128-a-b,r) 2^r,
```

retaining exactly the terms for which

```text
a+j+r<=33,       a+b-j+r<=33,
a+j+r=33 mod 2,  a+b-j+r=33 mod 2.
```

Enumerate the integer profiles with `a,b>=0`, `a+b<=128`,
`0<4a+b<=66`, and positive multiplicity, retaining either `b>0,S>=18` or
`b=0,a>=15`. There are 271. Deleting the now-empty `(4,2,18)` profile leaves
270, and exact binomial evaluation gives the unique maximum

```text
M_33(3,6)=1386246316188473270092082114587711840.
```

Since

```text
E_low=(1/2) sum_d M_33(a(d),b(d)),
```

the uniform condition `M_33(3,6)|D_p(33)|/2<=E_max` suffices. Exact integer
division gives

```text
floor(2E_max/M_33(3,6))=93962,
```

and the next integer 93,963 violates this uniform inequality. This proves the
claimed sharpened sufficient cap without asserting any vector count.
