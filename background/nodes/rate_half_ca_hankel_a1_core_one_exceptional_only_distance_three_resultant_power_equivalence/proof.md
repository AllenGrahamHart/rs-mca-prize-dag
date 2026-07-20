# Proof

Because `C` is monic and split with simple roots,

```text
H(z)=product_(C(x)=0)Q(z;x),
L=product_(C(x)=0)q_e(x).                             (1)
```

For a root `x` of `C`, the specialization `Q_x(z)=Q(z;x)` has exact degree
`e` precisely when `q_e(x)!=0`. Once this holds, it is squarefree precisely
when `Delta(x)!=0`. Since `C` is squarefree, these conditions for every
active row are equivalent to `(RPE3)`.

## Necessity

Assume the exact external design. Every active row belongs to exactly `e`
external blocks, at distinct external slopes. Since `deg Q_x<=e`, these are
all its roots, its degree is exactly `e`, and it is squarefree. This proves
`(RPE3)`.

Let `P_Z` be the monic locator of the `3e` external slopes. Multiplying the
row factorizations makes every external slope occur once for each of the
`r` rows in its block. Equation `(1)` therefore gives

```text
H=L P_Z^r,
```

which is `(RPE4)`. The slopes are distinct and base-field valued, so `P_Z`
is squarefree and split.

## Sufficiency

Conversely assume `(RPE3)--(RPE4)`. For every active row `x`, `Q_x` has
degree `e` and is squarefree. Unique factorization in `F[z]`, together with
`(1)` and `(RPE4)`, now shows that

```text
Q_x(z)=q_e(x) product_(gamma in Z_x)(z-gamma)         (2)
```

for one `e`-element subset `Z_x` of the roots of `P_Z`. In particular no
extension-field slope or repeated row root is hidden in `(RPE4)`.

Fix a root `gamma` of `P_Z`. Its multiplicity in `H` is exactly `r`. Every
factor in `(2)` is squarefree, so exactly `r` distinct active rows satisfy
`Q(gamma;x)=0`. The polynomial `Q(gamma;X)` has `X`-degree at most `r`. It
cannot vanish identically, since that would make all `6e+3>r` active rows
contribute the root `gamma` to `H`. Hence it has degree exactly `r`, and its
roots are exactly those `r` distinct active rows. This constructs the
squarefree external locator in `(RPE5)`.

No reconstructed slope is exceptional or internal. Indeed the pair-Lagrange
specializations give

```text
Q(0;X)=A(X),
Q(xi_i;X)=lambda_i B(X)A(X)/D_i(X),                  (3)
```

and both expressions are nonzero at every root of `C`. Thus neither zero nor
any `xi_i` is a root of `H` or `P_Z`. At a triple point `t`, the same normal
form gives

```text
Q(gamma;t)=Phi(gamma)A(t).
```

Dividing by the nonzero leading coefficient of `Q(gamma;X)` proves the
required constant ratio `G_gamma(t)/A(t)` on all three triple points. Hence
every reconstructed block is exactly a minimum-distance escape, and the row
and column degrees from `(2)` and the multiplicity argument give the complete
external split design. This proves sufficiency and uniqueness.

Finally the prime-field dependency gives `p>2^167`. Direct substitution of
the official `e=2^38-1`, `r=2^39-1` gives `(RPE6)`, so `p>deg H` and
`p` does not divide `r`. If `(RPE4)` holds, then

```text
gcd(H,H')=P_Z^(r-1)
```

up to a unit, because `P_Z` is squarefree. Conversely the monic squarefree
radical in `(RPE7)` is the only possible split factor in `(RPE4)`. This proves
the reconstruction statement and completes the equivalence. QED.
