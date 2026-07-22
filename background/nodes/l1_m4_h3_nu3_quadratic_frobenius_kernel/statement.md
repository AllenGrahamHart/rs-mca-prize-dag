# L1 m=4, h=3, nu=3 quadratic Frobenius kernel

- **status:** PROVED
- **dependencies:** `l1_m4_h3_cartier_resonance_reduction`,
  `l1_m4_h3_euler_quotient_factorization`
- **consumer:** `l1_mixed_petal_amplification`

Assume the surviving clean case `nu=3`. Then `H=c` is a nonzero constant,
`U`, `D`, and `B_0` are squarefree with the proved coprimalities, and

```text
U^3D+B_0=X^(4p-5),
deg U=p-3,  deg D=p+4,  deg B_0=2p-5.                  (QFK1)
```

Let `J` be the unique canonical antiderivative satisfying

```text
J'=cX^4U^2,
J(0)=0,
[X^(jp)]J=0 for every j.                               (QFK2)
```

The Cartier constraint `[X^(p-5)]U^2=0` makes this antiderivative exist.
There is a unique quadratic

```text
Q=q_2X^2+q_1X,       q_2!=0,       q_2^p=a,            (QFK3)
```

such that

```text
X^5U^3D=(X^4-Q)^p+J,
X^5B_0=Q^p-J.                                          (QFK4)
```

Moreover `ord_0(J)=5` and comparison at degree five recovers

```text
c=5U(0)D(0).                                           (QFK5)
```

Thus the entire Frobenius-kernel ambiguity of the clean `nu=3` case is a
two-parameter quadratic, rather than a degree-`p` polynomial. This does not
prove that the case is empty, classify its quadratic/interpolation
solutions, treat `nu=0,1,2`, classify nonembedded `h=2`, or close L1.
