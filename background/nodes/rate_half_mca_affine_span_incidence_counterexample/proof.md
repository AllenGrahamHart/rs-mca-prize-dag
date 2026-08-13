# Proof

The two verifiers reconstruct the following deterministic record in
`GF(1009)`.

For each `1<=i<=30`, the word `r_0+i r_1` vanishes on all 20 points of
`C_0`.  On the `i`-th point of `E` it has value

```text
-i^2+i*i=0,
```

while on every other point the construction explicitly avoids zero.  Its
zero codeword explanation therefore has maximal support exactly
`C_0 union {19+i}`, of size 21.

At slope zero, `r_0` agrees with the constant-one codeword exactly on `T`,
again a maximal support of size 21.  The explanations are consequently the
two constants zero and one, whose affine span is the complete
one-dimensional code.

On a zero-explanation support, the 20 core coordinates force any simultaneous
constant pair `(p_0,p_1)` to equal `(0,0)`, while the remaining coordinate
has nonzero `r_1`.  On `T`, the base word is constant one but the 21 direction
values are distinct, so no constant `p_1` explains the direction.  Every
support is pair-noncontained.

The direction values consist of zero with multiplicity 20 and 80 distinct
nonzero values.  Since codewords in `RS[F,D,1]` are constants,

```text
max_(c in C) agr(r_1,c)=20<21=m.
```

Finally, for `s=1` both terms of the asserted affine-span compiler are

```text
floor(100*99/(21*20))=23.
```

The family size is 31.  Thus the direction-separated upstream theorem and
the stronger support-wise replacement are false.

For the support refinements, `R=n-K=99`, `d=m-K=20`, and the minimum lift is
the zero constant because it gives 20 agreements, the maximum possible for
any constant.  Hence `e=80`.  Direct substitution gives

```text
floor((100*99-20*19)/(21*20))=22,
```

which is both the common-zero expression and the affine-basis expression at
this one-dimensional row.  Again `31>22`.

The proof failure is visible before arithmetic.  Pair noncontainment proves
that the normals incident with one selected parameter point span dimension
two.  It does not prevent 20 of the 21 incident normals from lying on one
line.  The rejected proof charged each point for `m*w=420` ordered bases;
these witnesses have only `2*20=40` ordered bases.
