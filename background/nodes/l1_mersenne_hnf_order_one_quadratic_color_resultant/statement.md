# L1 Mersenne HNF order-one quadratic color resultant

- **status:** PROVED
- **dependency:** `l1_mersenne_hnf_order_one_frobenius_gate`
- **consumer:** `l1_mixed_petal_amplification`
- **scope:** the four official `(m,h)=(8,7)` rows and the official
  `(m,h)=(16,15)` row

Suppose the colored Frobenius interpolant on the `H=h-1` reduced roots is

```text
E(W)=A W^2+B W+C,       A!=0.                        (QCRS1)
```

For a color variable `X`, define

```text
U=A A^p X^3+C^p X^2-(C C^p+1)X+C,
V=A B^p X^2-B C^p X+B,
T=(B A^p+B^p)X^3-C B^p X^2,
R_E(X)=U^2-VT.                                       (QCRS2)
```

Every distinct color used by a reduced root is a root of `R_E`. The
polynomial has exact degree six and leading coefficient `(A A^p)^2`.
Consequently:

1. no quadratic colored interpolant exists on the `m=16,h=15` row, because
   fourteen roots require at least seven distinct quadratic fibers;
2. on an `m=8,h=7` row,

```text
R_E(X)=(A A^p)^2 product_(L(x)=0)(X-E(x)),           (QCRS3)
```

   with colors counted with their root multiplicities.

In particular, in the collision-free chamber with missing colors
`eta,theta`,

```text
R_E(X)=(A A^p)^2 (X^8-1)/((X-eta)(X-theta));         (QCRS4)
```

and in the one-repeat chamber with repeated color `epsilon` and missing
colors `eta_1,eta_2,eta_3`,

```text
R_E(X)=(A A^p)^2 (X-epsilon)(X^8-1)
         /product_(j=1)^3(X-eta_j).                 (QCRS5)
```

These are exact necessary identities. They do not prove either `h=7`
chamber empty, recover the root/color assignment from the multiset, establish
the cyclotomic converse, construct an inner lift, or promote L1.
