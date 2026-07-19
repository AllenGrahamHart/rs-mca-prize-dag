# Proof

Contracting the fixed linear domain factor lowers the divided-power form
degree from `8m-1` to

```text
8m-2=2(4m-1)=2d.
```

The degree-`d` catalecticant is therefore the middle catalecticant, hence is
square and symmetric. In divided-power coordinates it is literally Hankel.
The residual router gives generic rank `d`, one right minimal index `e`, one
left minimal index `e`, and regular size `Delta=1`. Its primitive right
minimal vector is `q` in `(MAF3)`; symmetry gives the same rational left
kernel.

Since `M` has generic corank one, `det M` vanishes identically but at least
one `d x d` minor is nonzero. Thus `adj M` is nonzero and

```text
M adj(M)=adj(M) M=0.                                   (1)
```

Every column of `adj M` lies in the one-dimensional rational kernel spanned
by `q`. The vector `q` is primitive over the UFD `F[U,V]`, so Gauss's lemma
makes each polynomial column a polynomial multiple of `q`. Hence

```text
adj M=q w^T                                             (2)
```

for a polynomial vector `w`. The adjugate is symmetric. Equation `(2)` and
primitivity imply that `w=lambda q` for one polynomial `lambda`, proving the
factorization exactly after absorbing the scalar ambiguity into `lambda`.

Each adjugate entry is homogeneous of degree `d`, while every nonzero product
`q_i q_j` has degree `2e=d-1`. Therefore `lambda` is a nonzero homogeneous
linear form. Since the gcd of the entries of `q` is one, the gcd of all
products `q_iq_j` is also one; the common divisor of the nonzero adjugate
entries is exactly `lambda`.

The Kronecker form has one `L_e`, one transpose block `L_e^T`, and one
size-one regular block. The two singular blocks have constant total rank
`2e=d-1` at every projective parameter. The regular block is a nonzero linear
form, so it raises the rank to `d` away from its unique root and contributes
nothing there. Comparison with the common cofactor divisor identifies that
regular form with `lambda` up to scalar and proves the rank assertions.

The contracted exceptional-root ledger charges every residual omission to a
residual rank loss. There is no rank loss away from `lambda=0`, and the loss
at that root is exactly one. Thus all omission is concentrated there and
`(MAF5)` follows. Finally the core-one sharp-cap capacity identity from the
router is

```text
C=eta-Delta+O=e-1+O,
```

which proves `(MAF6)` and completes the proof. QED.
