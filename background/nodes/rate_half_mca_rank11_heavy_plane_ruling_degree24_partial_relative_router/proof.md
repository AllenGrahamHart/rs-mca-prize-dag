# Proof

The parent seed already performs exact cancellation. Write its residual
explanations as `h_i'`, its 32 distinct slopes as `gamma_i`, and the monic
locators of its exact size-`m'` supports as `Lambda_i'`. We retain

```text
n'=n-c,        K'=K-c,        m'=m-c,
d=m'-K'=m-K=67472.
```

At least 24 explanations lie on one affine codeword line and at least one
lies off it. The tuple is therefore not globally affine. Its slope-error
degree is in `24..31`.

## Support-collapsed extraction

Use coefficients of polynomials

```text
deg Q<=d,        deg A',deg B'<=m'
```

as homogeneous unknowns. At a coordinate occurring in at least two exact
supports impose the two equations

```text
A'(x)=Q(x)r_0'(x),        B'(x)=Q(x)r_1'(x).
```

At a coordinate occurring in exactly the support of record `i`, impose

```text
A'(x)+gamma_i B'(x)=Q(x)h_i'(x).
```

There are at most `chi'` equations and

```text
(d+1)+2(m'+1)=3m'-K'+3                              (1)
```

unknowns. If `chi'<3m'-K'+3`, a nonzero solution exists. For each `i`,

```text
P_i=A'+gamma_i B'-Qh_i'
```

has degree at most `m'` and vanishes on all `m'` roots of `Lambda_i'`.
Consequently

```text
Qh_i'+(c_0+c_1 gamma_i)Lambda_i'=A'+gamma_i B'.     (2)
```

The multiplier is affine in `gamma_i` by comparing leading coefficients.

If `Q=0`, nontriviality and two distinct slopes force
`(c_0,c_1)!=(0,0)`, which is a pure-locator certificate. Suppose `Q!=0`.
If `(c_0,c_1)=(0,0)`, identities (2) at two slopes show that `Q` divides
both `A'` and `B'`. Cancellation then puts every `h_i'` on one affine
codeword line. Its agreement with the anchor line at two of the 24 anchor
slopes identifies the two lines, contradicting the selected off-line
explanation. Thus the remaining low-complexity case is a nontrivial
scalar-locator rational certificate. We retain roots of `Q` as part of the
certificate and never divide pointwise by `Q`.

If the strict inequality fails, (1) gives the third branch directly.

## Exact lift

Let `R_0,R_1` be the received-column interpolants on `C` and `L_C` its
squarefree locator. The parent cancellation gives

```text
h_i=R_0+gamma_i R_1+L_C h_i',
Lambda_i=L_C Lambda_i'.
```

Multiplying (2) by `L_C` yields

```text
Qh_i+(c_0+c_1 gamma_i)Lambda_i=A+gamma_i B,
A=Q R_0+L_C A',        B=Q R_1+L_C B'.              (3)
```

Both lifted coefficient polynomials have degree at most `m`: since
`deg R_j<K`, one has `deg(QR_j)<d+K=m`, while
`deg(L_C A'),deg(L_C B')<=c+m'=m`. Thus (3) retains the denominator,
affine locator scalars, monic exact locators, first-owned slope labels, and
all original selected supports.

Every coordinate of `C` lies in all 32 original supports, hence contributes
exactly two to two-cover complexity. Therefore

```text
chi=chi'+2c.
```

The high-complexity threshold lifts without loss:

```text
3m'-K'+3+2c
=3(m-c)-(K-c)+3+2c
=3m-K+3
=2299571.
```

This proves the trichotomy and its exact original-row interfaces. QED.
