# Proof

The complete-fiber Vieta compiler proves that a negative packet has an
injective product map

```text
F(W)=B_0(W)/B_2(W) in PGL_2.
```

Let `nu(W)=-W` be the source-label involution and put

```text
iota=F nu F^(-1).
```

This is a nontrivial projective involution on product values.  In odd
characteristic it has a trace-zero matrix

```text
[ a  b]
[ c -a]
```

with nonzero determinant `-a^2-bc`.  Since `F(kappa_i)=y_i` and
`F(-kappa_i)=z_i`, one has

```text
z_i=(a y_i+b)/(c y_i-a).
```

Clearing the denominator gives `(KBNP-2)`.  Hence `(c,a,b)` is a nonzero
kernel vector for the six rows in `(KBNP-1)`, proving the rank gate.  The
parent injectivity theorem makes all twelve product values distinct, so none
of the six displayed orbits is fixed.

Suppose two rows come from `(u,-u)` and `(v,-v)`.  Their equations in
`(KBNP-2)` are

```text
-c u^2-b=0,       -c v^2-b=0.
```

Subtracting and using `u^2!=v^2` gives `c=0`, then `b=0`.  Nonsingularity
gives `a!=0`, and every remaining equation becomes `y_i+z_i=0`.  This proves
`(KBNP-3)`.

For the exact defect-zero fixture, use signed pair representatives
`A,B,C,D,E,F`.  Its paired products are

```text
(DE,DF), (-DF,EF), (-EF,AB),
(AC,-AC), (BC,-BC), (AD,BE).                      (3)
```

Distinct signed pairs give `A^2!=B^2`, and all labels are nonzero.  The
fourth and fifth pairs invoke `(KBNP-3)`, while the first has sum
`D(E+F)!=0` because `E!=-F`.  This contradiction deletes the fixture in
negative parity over every odd field.

For the independent finite regression, use signed pair representatives
`1,4,5,6,7,9,13` in `F_29`.  Exact enumeration of their 5,040 ordered choices
finds rank three in every matrix `(KBNP-1)`.  At the printed assignment, the
first three rows are

```text
(22,8,-1), (20,10,-1), (5,2,-1)
```

and their determinant is `12` modulo 29. QED.
