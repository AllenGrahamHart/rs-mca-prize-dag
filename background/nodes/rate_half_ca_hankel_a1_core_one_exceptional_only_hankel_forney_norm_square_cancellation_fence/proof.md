# Proof

The Forney interpolation theorem gives, for every root `a` of `A`,

```text
Phi(a)=beta_a q_1(a)A'(a)B_T(a).                    (1)
```

Hence the residue unit `C=q_1Phi/B_T mod A` has values

```text
C(a)=beta_a q_1(a)^2A'(a).                          (2)
```

Taking norms in `(2)` and using

```text
product_(A(a)=0) A'(a)=(-1)^e Disc(A)               (3)
```

gives

```text
Norm(C)/Disc(A)
 =(-1)^e product_a beta_a (product_a q_1(a))^2
 =(-1)^e Norm_A(Beta) Res(A,q_1)^2.                 (4)
```

This is `(HNC1)`.

The exceptional coefficient code is a dimension-`e` self-dual subspace for
the diagonal form with weights `beta_a`. Choose any information set and
normalize a generator to `[I_e|B]`. Taking determinants in

```text
D_I+B D_JB^T=0
```

shows that `(-1)^e product_a beta_a` is a square. This is `(HNC2)`. The
factor `Res(A,q_1)^2` in `(HNC1)` is already a square, so `(HNS1)` and
`(HNC2)` have the same square class. QED.
