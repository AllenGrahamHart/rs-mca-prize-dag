# Proof

The Forney-residue theorem gives a dimension-`e` self-dual subspace for the
diagonal evaluation form with weights

```text
mu_a=C(a)/A'(a).                                     (1)
```

Choose an information set `I` of size `e`; weighted self-duality makes its
complement `J` an information set as well. Normalize a generator as
`[I_e|B]`. Self-orthogonality gives

```text
D_I+B D_J B^T=0.                                    (2)
```

Taking determinants and writing `mu_I,mu_J` for the products of the weights
on the two halves gives

```text
det(B)^2 mu_J=(-1)^e mu_I,
product_a mu_a=(-1)^e(mu_I/det(B))^2.               (3)
```

Thus `(-1)^e product_a mu_a` is a square.

For monic squarefree `A` of degree `2e`,

```text
product_(A(a)=0) A'(a)=(-1)^e Disc(A).              (4)
```

Use `(1)` and `(4)` in `(3)`:

```text
(-1)^e product_a mu_a
 =Norm(C)/Disc(A).                                   (5)
```

This proves `(HNS2)`. Finally, evaluation in the squarefree algebra is
multiplicative, so

```text
Norm(C)=Res(A,q_1)Res(A,Phi)/Res(A,B_T).             (6)
```

Substitution gives `(HNS1)`. QED.
