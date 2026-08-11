# Proof

Choose an affine projective coordinate `z` with `alpha=0` and `beta` finite.
Write the rectangular Hankel pencil and its primitive kernel as

```text
M(z)=M_0+zM_1,
q(z)=sum_(i=0)^e z^i q_i.                           (1)
```

The unique right minimal block has index `e`, so the `q_i` are independent
and span the same coefficient space `W_Q` as any homogeneous expansion in
`(CRK1)`.

The coefficient equations of `M(z)q(z)=0` are

```text
M_0q_0=0,
M_0q_i+M_1q_(i-1)=0       for 1<=i<=e,
M_1q_e=0.                                             (2)
```

At `alpha`, let `Q_min` be the degree-`rho-c_alpha` minimal recurrence.
The left kernel consists of the coefficient vectors of

```text
Q_min A,       deg A<=c_alpha-1.                    (3)
```

Left multiplication of the middle equations in `(2)` by `(3)`, together
with the terminal equation, gives for every `0<=i<=e`

```text
(Q_min A)^T M_1 q_i=0.                              (4)
```

As in the two-slope source theorem, subtract the affine codeword line through
the centers at `alpha,beta`. The derivative syndrome source is supported on
`S_alpha union S_beta`; multiplication by `Q_min` kills `S_alpha`. Hence
`(4)` becomes

```text
sum_(x in X_(alpha,beta)) eta_x A(x)Q_i(x)=0,

eta_x=lambda_x e_beta(x)Q_min(x)/(beta-alpha)!=0.   (5)
```

Let `m=|X_(alpha,beta)|` and let `V` be the `c_alpha` by `m` evaluation
matrix of polynomials of degree at most `c_alpha-1` on these distinct
points. It has rank `c_alpha`. Equation `(5)` says

```text
V diag(eta_x) Ev_(alpha,beta)=0.                    (6)
```

Thus the column space of `diag(eta_x)Ev` lies in a space of dimension
`m-c_alpha`. The diagonal matrix is invertible, so

```text
rank Ev<=m-c_alpha.                                  (7)
```

Using `|S_alpha|=rho-c_alpha`,

```text
m=|S_alpha union S_beta|-|S_alpha|
 =j_(alpha,beta)+c_alpha.                           (8)
```

Equations `(7),(8)` prove `(CRK4)`.

If `(CRK5)` holds, `(CRK4)` gives rank at most one. Every row in `(CRK3)`
is nonzero: an identically zero form `Q(-;x)` would make `X-x` a fixed
factor of the primitive core-free kernel, contradicting core-freeness.
Therefore the rank is exactly one and all row forms are proportional. A
change of affine parameter basis acts invertibly on `W_Q`, so the conclusion
is projectively invariant. QED.
