# Proof

Let `L(X)=L_U0(X)` and let

```text
Qbar(t,X)=sum_(i=0)^e t^iQ_i(X),       deg_X Qbar<=d. (1)
```

For every polynomial `h in S_n=F[X]_(<=n)`, the standard dual-RS parity
identity gives

```text
sum_(x in U_0) Qbar(t,x)h(x)/L'(x)=0.              (2)
```

Indeed

```text
n=R-d-2,                                           (3)
```

so every coefficient numerator in `(2)` has degree at most `R-2`.

On the source class `M_gamma`, the three-class row identity is

```text
Qbar(t,x)=eta_x^(-1)q_gamma(t)H_x(t),
H_x(t)=G(t,x)/L'(x).                               (4)
```

Define

```text
T_gamma(h)=sum_(x in M_gamma)
 eta_x^(-1)H_x(t)h(x)/L'(x)       in V.            (5)
```

Substitution in `(2)` gives

```text
q_alpha T_alpha(h)+q_beta T_beta(h)
 +q_theta T_theta(h)=0.                            (6)
```

Thus `T=(T_alpha,T_beta,T_theta)` maps `S_n` into `ker Phi`, proving
`(ISR2)`.

It remains to lower-bound one projection. Choose a minimal presentation

```text
G(t,X)=sum_(j=1)^r A_j(t)B_j(X),                   (7)
```

with both coefficient families independent and `deg B_j<=n`. Fix one of
the two classes `M_gamma` of size `n+2`. In the bases from `(7)` and a
monomial basis of `S_n`, the matrix of `T_gamma` is

```text
E_B^T D E_n,                                       (8)
```

where `E_B` evaluates the span of the `B_j` on `M_gamma`, `E_n` evaluates
all of `S_n` there, and

```text
D=diag(eta_x^(-1)/L'(x)^2).                        (9)
```

Every diagonal entry is nonzero. Evaluation on `n+2` distinct points is
injective through degree `n`, so

```text
rank E_B=r,       rank E_n=n+1.                   (10)
```

Sylvester's rank inequality applied to `(8)` yields

```text
rank T_gamma>=r+(n+1)-(n+2)=r-1.                  (11)
```

Therefore `rank T>=r-1`. The three-class generation theorem gives
`dim ker Phi=3r-(e+1)`, so `(ISR3)` follows. Rearranging gives `2r>=e`.
Since the official `e` is odd, this is `(ISR4)--(ISR5)`. Substituting
`r_1=(e+1)/2` into the kernel formula proves `(ISR6)`. QED.
