# Proof - L1 Mersenne next-to-maximal exceptional reduction

Put `u=n-hp=p+m`. The maximal-complement supplier depresses the monic
squarefree outer value polynomial and gives

```text
G(R)D=X^n-alpha,
G(Y)=Y^h+J(Y),       deg J<=h-2,
R=X^nu U.                                               (1)
```

Its Frobenius-degenerate abc arm is impossible because `h<m` and `u>p`.

## 1. Low-degree Euler eliminant

Define

```text
H=hXU'D+XUD'-(n-hnu)UD,
V=nu U+XU',
T(Y)=hG(Y)-YG'(Y).                                     (2)
```

Put `L=n-hnu`, `A=U^hD`, and
`B=(J(R)D+alpha)/X^(hnu)`, so `A+B=X^L` and

```text
XA'-LA=U^(h-1)H.                                      (3)
```

If `H=0`, every exponent of `A` is congruent to `L mod p`. But `A(0)!=0`,
so `L=0 mod p` and both `A` and `B` lie in `F[X^p]`, contradicting the
non-Frobenius branch. Thus `H!=0`. Moreover,

```text
deg B<=(h-2)p+u-hnu.
```

Comparing `XA'-LA=-(XB'-LB)` and subtracting
`deg U^(h-1)=(h-1)(p-nu)` gives

```text
H!=0,       deg H<=m-nu.                               (4)
```

Choose `s in {0,...,p-1}` with `s+n-hnu=0` in the field. Then

```text
(X^s U^hD)'=X^(s-1)U^(h-1)H.                          (5)
```

If equality held in (4), the leading term on the right of (5) would have
degree congruent to `-1 mod p`, impossible for a formal derivative. Hence

```text
deg H<=m-1-nu=h-nu.                                   (6)
```

A direct use of the differentiated domain identity gives

```text
D T(R)V=H G(R)-m alpha U.                              (7)
```

## 2. Every nonexceptional tangent branch is empty

Suppose `T` has a nonzero root `y`. Since `G` is squarefree, a common root
of `G` and `T` can only be zero; hence `G(y)!=0`. Put

```text
phi(Y)=m alpha Y/G(Y),       kappa=phi(y),
P_y=X^nu H-kappa.
```

Multiplying (7) by `X^nu/G(R)` yields

```text
P_y=phi(R)-phi(y)+X^nu D T(R)V/G(R).                  (8)
```

At `T(y)=0`, one has `yG'(y)=hG(y)`, and therefore

```text
phi'(y)=m alpha(1-h)/G(y)!=0.                         (9)
```

Every distinct root of `R-y` is a root of `P_y` by (8). At a root of
multiplicity `2<=e<p`, the correction in (8) has order at least `2e-1`,
whereas the first term has exact order `e`; hence `ord(P_y)=e`. If `P_y`
were nonzero, (6) would give at most `h` distinct roots, each repeated
multiplicity at most `h` (and each simple multiplicity one). Since
`e=p` would instead make `R-y` a `p`th power and the first term in (8) have
order `p>deg P_y`, which is also impossible. Since `deg(R-y)=p`, this would
force

```text
p<=h^2,                                               (10)
```

false on every row in `(NMR2)`. Consequently `P_y=0`. Since `kappa!=0`,
this forces `nu=0` and `H=kappa` constant. Repeating the argument for every
nonzero root of `T` gives `(NMR3)--(NMR4)`.

## 3. The exceptional local passport

Write `H=q`. Equation (7) is now

```text
D T(R) X R'=qG(R)-m alpha R.                         (11)
```

For a nonzero root `y` of `T`, put `A(Y)=qG(Y)-m alpha Y`. Equation
`(NMR4)` gives `A(y)=0`, while

```text
A'(y)=qG'(y)-m alpha=(h-1)m alpha!=0.                (12)
```

Thus `y` is a simple root of `A`. Let its multiplicity in `T` be `t`, and
let `x` be a root of `R-y` of multiplicity `e`. The case `e=p` would make
`R'=0`, so (11) would give the impossible polynomial identity `A(R)=0`.
Thus `e<p`. If `x!=0`, comparing local orders in (11) gives

```text
ord_x(D)+te+e-1=e.
```

Therefore `t=e=1` and `D(x)!=0`. If `x=0`, the extra factor `X` makes the
left order still larger and equality is impossible. This proves `(NMR5)`.

## 4. The no-nonzero-tangent branch

If `T` has no nonzero root, then each multiplier `h-j` below the depressed
leader is nonzero, so `T` is a monomial. Squarefreeness leaves only

```text
G(Y)=Y^h+c,       G(Y)=Y^h+cY.                       (13)
```

For the first form, divide

```text
U^hD+(cD+alpha)/X^(hnu)=X^(n-hnu)
```

into its coprime abc triple. Mason--Stothers gives

```text
n<=p-nu+2u,
(m-3)p<=m-nu,
```

which is impossible on `(NMR2)`.

For `G=Y^h+cY`, zero is a complete split value, so `nu=0`. Equation (7)
cancels `R` and becomes

```text
(m-2)cDXR'=H(R^(h-1)+c)-m alpha.                     (14)
```

Evaluation on the `p` roots of `R=0`, followed by evaluation at zero,
forces

```text
H=mh alpha/c,       c/R(0)^(m-2)=-(m-1)/(m-2).       (15)
```

Put `C=(m-1)/(m-2)`. Normalizing the `m-2` nonzero roots of `G` by
`z=beta/R(0)` and comparing root products with the zero fiber gives

```text
w=1-z in mu_(m(p+1)),       z^(m-2)=C.               (16)
```

Because `m-2` divides `p-1`, put `xi=C^((p-1)/(m-2))`. Then

```text
z^p=xi z,
epsilon=w^(p+1) in mu_m,
xi w^2+(1-xi)w-epsilon=0.                            (17)
```

The exact packet computes the gcd of the quadratic in (17) with
`W^(p+1)-epsilon` over `F_(p^2)` for every `epsilon in mu_m`. On each row,
only `epsilon=1` survives and its gcd has degree one. At most one `w` is
available, contradicting the `m-2` distinct values required in (16).
