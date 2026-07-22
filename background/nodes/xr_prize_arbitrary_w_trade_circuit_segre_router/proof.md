# Proof

Let a trade have active rows `lambda_i` and matrix rank `r`. Choose a basis
`f_1,...,f_r` of its row space and write

```text
lambda_i=sum_j c_(ij)f_j.
```

For row scalars `alpha_i`, the scaled rows are a trade exactly when

```text
sum_i alpha_i c_(ij)=0,
sum_i gamma_i alpha_i c_(ij)=0       for every j.     (1)
```

Let `M` be the `2r x ell` coefficient matrix in `(1)`. The `r` independent
coefficient columns indexed by `j` lie in the dual of the two-row slope check,
whose dimension is `ell-2`. Hence `r<=ell-2`.

If a support-minimal scaling trade had `ell>=2r+2`, then
`dim ker M>=ell-2r>=2`. Intersecting the kernel with any coordinate
hyperplane gives a nonzero scaling trade on a strict sub-support, a
contradiction. Therefore `ell<=2r+1`, proving `(AW1)`.

Any nonminimal scaling vector can be split by choosing a nonzero kernel
vector on a strict sub-support and cancelling one coordinate. Induction on
support size decomposes every trade into row-scaling circuits, each of rank
at most `r`.

Now take `r=2`. A rank-one circuit has arity exactly three by `(AW1)`, and
the rank-one owner theorem applies. A rank-two circuit has arity four or five.
With the basis `F,G`, equations `(1)` say that a scaling vector is in the
kernel of the Segre columns `(AW2)`, and each column satisfies

```text
z_1z_4-z_2z_3=0.                                      (2)
```

Circuit minimality makes the column kernel one-dimensional with an all-
nonzero generator. After rescaling rows, that generator is the all-one
vector. Thus four columns have rank three; five columns have rank four and
every four are independent.

For four blocks, their Segre points lie on one projective hyperplane

```text
A c+B d+C gamma c+D gamma d=0.                        (3)
```

It gives

```text
[c:d]=[B+D gamma:-(A+C gamma)].                       (4)
```

The map is nonconstant: a constant map would make the trade row space rank
one. The two linear forms have no common projective root, since otherwise
they are proportional and `(4)` is constant. Hence `(4)` is a Mobius graph,
and distinct slopes give distinct row classes. For five blocks, the rank and
independence statement is exactly the full five-point Segre circuit.

No property of the support code `W` entered this coefficient argument. The
uniform theorem's rank-one exclusion is replaced here by the explicit
three-block owner, proving the claimed arbitrary-`W` decomposition. QED.
