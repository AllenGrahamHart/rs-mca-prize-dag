# Proof

The first identity in `(CM2)` is immediate:

```text
lambda_(i,j)-lambda_(0,j)
 =(beta_i-beta_0)c_(u_j)
 =pi^2 c_(u_j)alpha_i.                            (1)
```

Identity `(CM3)` is the coupling/quotient syzygy proved in the coupling-batch
odd-saturation theorem. Both `pi` and every `c_(u_j)` have 2-power norm, so
they are units in `O[1/2]`.

Start with `I_joint`. Equation `(1)` with `j=0` puts every
`lambda_(i,0)` in its localization. Equation `(CM3)` and invertibility of
`c_(u_0)` put every `lambda_(0,j)` there. Thus the localized coupling cross is
contained in the localized joint ideal.

Conversely, `(1)` with `j=0` gives

```text
alpha_i=(pi^2 c_(u_0))^(-1)
        (lambda_(i,0)-lambda_(0,0)),               (2)
```

and `(CM3)` expresses every `theta_(0,j)` in the coupling cross. This proves
the first equality in `(CM5)`.

The cross generators are entries of the rectangle. For the reverse
inclusion, use `(1)` for arbitrary `i,j`, then substitute `(2)`. Every
`lambda_(i,j)` lies in the localized cross ideal, proving the second equality.
Equality of odd prime-ideal valuations and odd ideal-norm parts follows from
localization.

It remains to classify zero entries. In one fixed row,
`lambda_(i,j)=0` says

```text
beta_i=c_(v_j)/c_(u_j).                            (3)
```

The right side is a nonidentity quotient. The quotient consequence of
shifted-product Sidonicity permits at most one ordered representation of this
fixed value, so a row contains at most one zero. In one fixed column, `(3)`
fixes a shifted-product value. Multiplicative Sidonicity makes the distinct
unordered pairs `E_i` have distinct products `beta_i`, so a column also
contains at most one zero. The zeros are therefore a partial matching of size
at most `min(m,r)`, proving `(CM6)`.

For a finite target, every product `beta_i` and quotient ratio reduces to the
same `t`, so every `lambda_(i,j)` lies in the degree-one row-prime ideal. The
formula for `U(t)` and `P(t)>=19` give `m>=10`; the remaining assertions follow.
QED.
