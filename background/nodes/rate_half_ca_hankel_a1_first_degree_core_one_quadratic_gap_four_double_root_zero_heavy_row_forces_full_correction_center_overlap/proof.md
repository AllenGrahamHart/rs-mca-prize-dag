# Proof

Assume that the heavy row vanishes:

```text
G(t,x_*)=0.                                         (1)
```

Evaluation at `x_*` is the remainder on division by `X-x_*`, so `(1)` gives

```text
X-x_* divides G(t,X).                              (2)
```

Suppose, toward a contradiction, that `S_B` has a projective root `sigma`
over the algebraic closure which is not a root of `Lambda`. By `(HZF1)` and
`gcd(g_*,S_B)=1`,

```text
ord_sigma Q(t,x_*)=3.                              (3)
```

There are two cases.

## Unsupported correction slope

If `sigma` is not an off-line supported slope, multiplicativity of the
`X`-resultant and `(2),(3)` imply

```text
ord_sigma Res_X(Q,G)>=3.                           (4)
```

The exact resultant factorization is

```text
Res_X(Q,G)
 =c_R E_4 product_(delta off line)
                 ell_delta^(n-a_delta).            (5)
```

Because `sigma` is unsupported and is not a center, no factor in the
product contributes at `sigma`. Equations `(HZF1),(5)` therefore give exact
order two, contradicting `(4)`.

## Supported correction slope

Suppose that `sigma` is off-line supported. The all-excess fiber theorem
gives the complete specialized gcd

```text
gcd_X(Q(sigma,X),G(sigma,X))=A_sigma(X)R_sigma(X), (6)
```

where `A_sigma` is the actual-support factor and `R_sigma` is the
padded-heavy factor. Since `(2),(3)` make `x_*` a common root, `(6)` puts
`x_*` in one of these two factors.

If `x_*` is an actual-support root, first-jet transversality gives local
intersection multiplicity one. But `(2),(3)` give

```text
I_((sigma,x_*))(Q,G)
 >=I_((sigma,x_*))(Q,X-x_*)=3,                     (7)
```

a contradiction.

If `x_*` is a root of `R_sigma`, then `sigma` is a supported slope whose
padded-heavy factor contains `x_*`. By definition of the squarefree
supported form `g_*`, this gives `g_*(sigma)=0`, contradicting
`gcd(g_*,S_B)=1`.

Thus every root of `S_B` is a root of `Lambda`. Since `S_B` is squarefree,

```text
S_B divides Lambda.                                (8)
```

Also `S_B` divides `g_*S_B^2`, so `(8)` implies `S_B|J` and `j>=2`. This
proves `(HZF3)` and its contrapositive `(HZF4)`. The barycentric identity
`R_lambda=G(t,x_*)` gives the final assertion. QED.
