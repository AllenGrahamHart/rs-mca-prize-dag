# Proof

Choose a polynomial basis `F,G` for the rank-two row space supplied by the
uniform split-pencil reduction. Thus

```text
lambda_i(x)=(c_iF(x)+d_iG(x))/Lambda'_X(x),
deg F,deg G<=d.                                      (1)
```

The three-anchor owner says that all coefficient points lie on one
nonconstant Mobius hyperplane. Hence there are `A,B_0,C,D`, with
`AD-B_0C!=0`, and nonzero `s_i` such that

```text
(c_i,d_i)=s_i(B_0+D gamma_i,-A-C gamma_i).           (2)
```

Set

```text
P=B_0F-AG,       Q=DF-CG.                            (3)
```

The determinant in `(2)` shows that `(P,Q)` is another basis of the row
space. Substitution into `(1)` gives `(TG1)`.

The unweighted trade equation becomes

```text
(sum_i s_i)P+(sum_i s_i gamma_i)Q=0,
```

and the slope-weighted equation becomes

```text
(sum_i s_i gamma_i)P+(sum_i s_i gamma_i^2)Q=0.
```

Independence of `P,Q` proves the equivalence with `(TG2)`.

It remains to classify the moment kernel. For a polynomial `H` of degree
less than `t-3`, the leading-coefficient form of Lagrange interpolation gives

```text
sum_i H(gamma_i)gamma_i^j/L'_Gamma(gamma_i)=0,
0<=j<=2,                                             (4)
```

because `deg(H(T)T^j)<=t-2`. The map

```text
H |-> (H(gamma_i)/L'_Gamma(gamma_i))_i
```

is injective and has dimension `t-3`. The three-row Vandermonde matrix on
the distinct slopes has rank three, so its kernel also has dimension `t-3`.
Equation `(4)` therefore parameterizes that complete kernel uniquely. Since
every active row is nonzero, every `s_i` is nonzero, which is equivalent to
the root avoidance in `(TG3)`.

Finally take a canonical four-block owner `C`. The standard barycentric
identity on four distinct slopes says

```text
sum_(i in C) gamma_i^j/L'_C(gamma_i)=0,
0<=j<=2.                                             (5)
```

After the invertible basis change `(2)--(3)`, a scaling vector `kappa` is a
circuit precisely when `(kappa_i s_i)_(i in C)` satisfies `(5)`. The kernel
on four slopes is one-dimensional. Normalizing its `e` coordinate to one
gives exactly `(TG4)`. QED.
