# Proof

The center-overlap theorem with `(HNS2)` gives

```text
G(t,x_*)=c g_*S_B^2                                (1)
```

for a scalar `c`, initially allowed to be zero. Suppose `c=0`. Since `G`
vanishes identically on the row `x_*`,

```text
X-x_* divides G(t,X).                              (2)
```

Choose a projective root `sigma` of the squarefree quadratic `S_B`. By
`(HNS1)` and coprimality,

```text
ord_sigma Q(t,x_*)=3.                              (3)
```

Condition `(HNS2)` says `sigma` is not a center slope. There are two cases.

## Unsupported correction slope

If `sigma` is not an off-line supported slope, multiplicativity of the
`X`-resultant and `(2),(3)` give

```text
ord_sigma Res_X(Q,G)>=3.                           (4)
```

But the exact resultant factorization is

```text
Res_X(Q,G)
 =c_R E_4 product_(delta off line)
                 ell_delta^(n-a_delta).            (5)
```

At an unsupported, noncenter root of `S_B`, `(HNS1),(5)` give exact order
two, contradicting `(4)`.

## Supported correction slope

Suppose instead that `sigma` is off-line supported. The all-excess fiber
factorization gives

```text
gcd_X(Q(sigma,X),G(sigma,X))=A_sigma(X)R_sigma(X), (6)
```

where `A_sigma` is the actual-support factor inside the classified union and
`R_sigma` is the padded-heavy factor. Since `(2),(3)` make `x_*` a common
root, `(6)` leaves two possibilities.

If `x_*` is a root of `A_sigma`, the exact first-jet theorem says the two
curves meet transversely there, with local intersection multiplicity one.
On the other hand `(2)` makes `X-x_*` a component of `G`, and `(3)` gives

```text
I_((sigma,x_*))(Q,G)
 >=I_((sigma,x_*))(Q,X-x_*)=3,                     (7)
```

a contradiction.

If `x_*` is a root of `R_sigma`, then `sigma` is one of the supported slopes
whose padded-heavy factor contains the new root `x_*`. By the definition of
the squarefree supported form `g_*`, this says `g_*(sigma)=0`, contradicting
`gcd(g_*,S_B)=1`.

Both cases are impossible, so `c!=0` in `(1)`. This proves `(HNS3)`, and
the barycentric identity `R_lambda=G(t,x_*)` proves `(HNS4)`. QED.
