# Proof

The two affine forms in `(SAC1)` are nonconstant.  Indeed `a=-2` or `a=1`
would contradict `a^2=-2` in the official characteristic.  Their coefficient
determinant is

```text
(a+2)(2-a)-[-(a+1)](a-1)=3,                          (1)
```

which is nonzero.  Thus they are nonproportional.

We first recall the one-fiber part of the in-house Stepanov construction in
the field-general form needed here.  Let `K` be any field of characteristic
`p`, let `H<=K^*` have order `n`, and let `L_1,L_2` be nonconstant,
nonproportional affine forms.  An affine change of variable and separate
nonzero rescalings turn

```text
L_1(x),L_2(x) in H
```

into

```text
x^n=alpha,       (x-1)^n=beta                         (2)
```

for fixed nonzero `alpha,beta in K`.  Use the auxiliary polynomial

```text
Psi(X)=Phi(X,X^n,(X-1)^n),
Phi=sum lambda_(i,j,k)X^iY^jZ^k,
0<=i<A,       0<=j,k<B.                              (3)
```

Exactly as in the proved dependency, multiplicity `D` at every solution of
`(2)` imposes at most `D(A+D)` homogeneous conditions on `AB^2`
coefficients.  Hence a nonzero `Phi` exists when

```text
D(A+D)<AB^2.                                         (4)
```

The dependency's sparse nonvanishing lemma is characteristic-only: its
derivative induction works over every extension of the prime field.  Under

```text
AB<=n,       A+nB<p,                                 (5)
```

it proves `Psi!=0`.  Since `deg Psi<A+2nB`, root multiplicity then gives

```text
#{x:L_1(x),L_2(x) in H}<(A+2nB)/D.                  (6)
```

Apply `(6)` over `K=F_q`, `H=mu_N`, and the two forms in `(SAC1)`.  The
printed integers in `(SAC3)` are

```text
A_0=D_0=floor((27N^2/64)^(1/3)),
B_0=floor((125N/64)^(1/3))+1.                        (7)
```

Direct integer cubing gives `(SAC4)`.  It also gives

```text
(A_0+2NB_0)/D_0
 =355106851+51038404/79896510.                       (8)
```

It remains to check `(5)` in every official field.  The maximal-field
dependency gives `e in {1,2}` and `q>=3*2^128`.  If `e=1`, then
`p=q`.  If `e=2`, then

```text
p>=ceil(sqrt(3*2^128))=31950697969885030204.          (9)
```

The right side of `(9)` exceeds `A_0+NB_0` as printed in `(SAC3)`, so `(5)`
holds in both cases.  Equation `(6)` and the exact quotient `(8)` now imply
the integer cap `(SAC2)`.  The remaining affine-compiler gates define a
subset of `mathcal Y_a`, so they cannot increase it. QED.
