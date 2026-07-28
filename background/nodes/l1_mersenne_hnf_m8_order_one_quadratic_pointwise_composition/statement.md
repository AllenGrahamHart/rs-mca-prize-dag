# L1 Mersenne HNF m=8 order-one quadratic pointwise composition

- **status:** PROVED
- **dependency:** `l1_mersenne_hnf_order_one_frobenius_gate`
- **consumer:** `l1_mixed_petal_amplification`
- **scope:** every quadratic-color packet on the four official
  `(m,h)=(8,7)` rows

Write

```text
E(W)=A W^2+B W+C,       A!=0,
P(W)=(W+1/d)L(W),       d=c-1,       r=rho*c.        (QPC1)
```

Then the pointwise Frobenius equations imply the exact polynomial identity

```text
A^p E(W)^3+B^p W E(W)^2+C^p W^2 E(W)-W^2
  =A^p A^3 L(W).                                    (QPC2)
```

Comparing its top and bottom coefficients gives

```text
C/A=(1-r)/d^2.                                      (QPC3)
```

If `g(y)` is the hypergeometric polynomial before the affine shift, every
quadratic-color survivor consequently satisfies the pure HNF equation

```text
g(1)=(1-r)^3.                                       (QPC4)
```

This identity preserves the root/color assignment and applies to the
collision-free, one-repeat, and two-repeat quadratic chambers. It does not
prove (QPC4) incompatible with the `h=7` conic, establish the cyclotomic
converse, construct an inner lift, treat higher color degree, or promote L1.
