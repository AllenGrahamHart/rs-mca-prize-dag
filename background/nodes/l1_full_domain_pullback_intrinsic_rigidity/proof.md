# Proof - L1 full-domain pullback intrinsic rigidity

## 1. Composition identity

Let `B=P(H)` be the set of fiber labels. The complete-fiber hypothesis gives
`|B|=n/s`. For every `a in B`, the monic degree-`s` polynomial `P-a` has the
corresponding fiber as all its roots. Multiplying the fiber locators gives

```text
X^n-alpha^n=product_(a in B)(P(X)-a)=F(P(X)),          (1)
F(Z)=product_(a in B)(Z-a).                            (2)
```

Thus

```text
K(X^n) subset K(P) subset K(X).                        (3)
```

## 2. Cyclic intermediate field

Because `mu_n subset K^*`, the extension `K(X)/K(X^n)` is Galois cyclic of
degree `n`, with automorphisms

```text
X -> zeta X,       zeta in mu_n.                       (4)
```

The characteristic does not divide `n`, since `n` divides `|K^*|`. Hence it
also does not divide `s`. The rational map `P` is separable and

```text
[K(X):K(P)]=deg P=s.                                  (5)
```

By Galois correspondence, `K(P)` is the fixed field of the unique subgroup
of `(4)` having order `s`, namely `mu_s`. The field `K(X^s)` is fixed by this
subgroup and has index `s` in `K(X)`, so

```text
K(P)=K(X^s).                                           (6)
```

## 3. Polynomial normalization

Put `Y=X^s`. Equality `(6)` says that `P` and `Y` generate the same rational
function field. Since `P in K(Y)` and `[K(Y):K(P)]=1`, `P` is a degree-one
rational function of `Y`:

```text
P=(aY+b)/(cY+d),       ad-bc!=0.                       (7)
```

The polynomial `P` has a pole at infinity. If `c!=0`, the right side of `(7)`
is finite at infinity, so `c=0`. Therefore `P=a'Y+b'`. Monicity of `P` forces
`a'=1`, proving `(IR2)`.

For `x,y in H`, equality `P(x)=P(y)` is now `x^s=y^s`, equivalently
`x/y in mu_s`. Hence the fibers are precisely the `mu_s`-cosets. Every union
of them is stabilized by `mu_s`, proving the exact-periodic ownership
corollary and the L1 consequence.
