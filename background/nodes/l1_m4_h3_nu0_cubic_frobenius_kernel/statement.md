# L1 m=4, h=3, nu=0 cubic Frobenius kernel

- **status:** PROVED
- **dependencies:** `l1_m4_h3_cartier_resonance_reduction`,
  `l1_m4_h3_euler_quotient_factorization`
- **consumer:** `l1_mixed_petal_amplification`

Assume `nu=0`. Then

```text
R^3D+B_0=X^(4p+4),
deg R=p,       deg D=p+4,       deg B_0=2p+4,
H(0)!=0,       0<=h=deg H<=3.                         (CFK1)
```

Let `J` be the unique canonical antiderivative satisfying

```text
J'=X^(p-5)R^2H,
J(0)=0,
[X^(jp)]J=0 for every j.                              (CFK2)
```

The Cartier constraints

```text
[X^4](R^2H)=[X^(p+4)](R^2H)=0
```

make this antiderivative exist. There is a unique cubic

```text
Q=q_3X^3+q_2X^2+q_1X,
q_3!=0,       q_3^p=a,                                (CFK3)
```

such that

```text
X^(p-4)R^3D=(X^5-Q)^p+J,
X^(p-4)B_0=Q^p-J.                                     (CFK4)
```

Moreover

```text
ord_0(J)=p-4,
H(0)=-4R(0)D(0).                                      (CFK5)
```

Thus all four `nu=0` eliminant-degree cases share a three-scalar cubic
Frobenius kernel; the quartic and constant kernel coefficients are forced to
zero. This does not exclude or classify any `h`, determine the remaining
polynomials from `Q`, treat positive valuation or wider `m`, or close L1.
