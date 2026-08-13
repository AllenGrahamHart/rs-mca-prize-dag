# Proof

Let

```text
K_2=dim ker(Phi)=3r-(e+1).                         (1)
```

The cubic-splitting theorem gives

```text
c_2=K_2-2c_1,
c_3=r-1-K_2+c_1,                                  (2)
```

so `c_3>=0` implies

```text
c_1>=K_2-(r-1)=2r-e.                              (3)
```

Fix one of the two small classes `M_gamma`, of size `n+2`. The
locator-interpolation theorem constructs a subspace of `ker Phi` whose
projection to the `gamma` coordinate has rank at least `r-1`. Hence the
full coordinate projection

```text
pi_gamma:ker Phi -> V                              (4)
```

also has rank at least `r-1`, and

```text
dim ker pi_gamma<=K_2-(r-1)=2r-e.                 (5)
```

Every `h` in the inverse prolongation `J` gives the Koszul syzygy between
the other two quadratic generators with zero `gamma` coordinate. This is
an injection

```text
J -> ker pi_gamma.                                 (6)
```

Since `dim J=c_1`, equations `(3),(5),(6)` force

```text
c_1=2r-e.                                         (7)
```

Substitution in `(2)` proves `(LQD2)`. The bundle splitting `(LQD3)` is
immediate. Twisting its evaluation sequence by `O(1)` gives

```text
H^1(E(1))=0,                                       (8)
```

so the multiplication map `S_1 tensor V -> S_(e-1)` is surjective, proving
`(LQD4)`. The boundary substitution gives `(LQD5)`.

It remains to identify the small-class defect. Equations `(5)--(7)` show
that `dim ker pi_gamma=c_1`, so

```text
rank pi_gamma=K_2-c_1=r-1.                         (9)
```

The classwise interpolation map `T_gamma` has rank at least `r-1` and its
image lies in `im pi_gamma`; therefore

```text
rank T_gamma=r-1.                                  (10)
```

Use the matrix factorization from the interpolation theorem:

```text
T_gamma=E_B^T D E_n,
D_x=eta_x^(-1)/L_U0'(x)^2.                         (11)
```

Here `E_B` evaluates `W_X` and has rank `r`, while `E_n` is the full
degree-`n` evaluation matrix on `n+2` points. Since `(11)` has rank `r-1`,
its left kernel is one-dimensional. A nonzero left-kernel vector determines
one nonzero `B_gamma in W_X` satisfying

```text
sum_(x in M_gamma)D_xB_gamma(x)h(x)=0
                         for every h in S_n.       (12)
```

The dual of the `[n+2,n+1]` Reed--Solomon evaluation code is spanned by

```text
(1/L_Mgamma'(x))_(x in M_gamma).                   (13)
```

Thus `(12)` is equivalent to

```text
D_xB_gamma(x)=kappa_gamma/L_Mgamma'(x)             (14)
```

for one nonzero `kappa_gamma`. Solving `(14)` and using `(11),(LQD9)` gives
both formulas in `(LQD8)`. Every displayed factor is nonzero on
`M_gamma`, proving the final assertion. QED.
