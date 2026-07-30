# Proof

## 1. Special source component

For `a=b=-1`, the one-parameter quartic is

```text
Q(S,P)=9(S^2P^2-2P^3-3P^2+1).                     (1)
```

The source-cover classifier permits `d=-1,ell=1` and gives source genus
zero. On the coefficient normalization, put

```text
P=(x^2+1)/2,       S=x(x^2+3)/(x^2+1).             (2)
```

Substitution proves `(1)`. The monic quadratic with root sum and product
`(2)`, after clearing denominators, is exactly `H` in `(KBM3G-1)`. Its
discriminant in `t` is

```text
-4(x^2-1)^2(x^2+2).                                (3)
```

After removing the square factor, `(3)` has two branch points, so the
normalization is rational. Since `P` determines `x^2` and `S` distinguishes
the two signs generically, the coefficient map is birational.

## 2. Dihedral pullback

The map `h` is `m^(-1)(t^2)` for `m(y)=(y-2)/(y+1)`, and `psi` is a
quadratic map with deck involution `x -> -x`. Direct substitution gives
`(KBM3G-2)`. Therefore `H(t,x)=0` is one irreducible source component and
`H(t,-x)=0` is its distinct deck conjugate above the non-diagonal cubic
correspondence.

The elementary identity

```text
D_3(y)-D_3(z)=(y-z)(y^2+yz+z^2-3)                 (4)
```

shows that `D_3(h(t))=D_3(h(psi(x)))` on either component. It follows that
`F(h(t))=F(h(psi(x)))` for every `F=G composed D_3`.

## 3. Poles and complete source

Let `p,q` be distinct values outside `{2,-2}` and choose a degree-ten
rational function `G` with poles of order five exactly at `p,q`; for
example, a generic numerator over `((v-p)(v-q))^5`. Then `F=G composed D_3`
has degree 30 and six distinct poles, all of order five.

The degree-six function `phi=D_3 composed h` is

```text
phi(t)=(t^2+2)(2t^4-10t^2-1)/(t^2-1)^3,
phi'(t)=54t(2t^2+1)/(t^2-1)^4.                    (5)
```

Its only finite branch values are `2,-2`; infinity is another point over
`2`. The branch values of `psi` map under `phi` to the same pair. Thus the
chosen `p,q` give twelve distinct source labels and 24 distinct roots of
the complete source pullback.

Let `R(v)=(v-p)(v-q)`. The twelve source labels are the zeros of the
numerator of `R(phi(t))`; the degree-24 complete source form `B(x)` is the
numerator of `R(phi(psi(x)))`. If `alpha` is any source label, then on
`H(alpha,x)=0`, equations `(4)--(5)` give

```text
R(phi(psi(x)))=R(phi(alpha))=0.
```

Hence the quartic `H(alpha,x)` divides `B(x)`. Summing over all twelve
labels gives total degree 48 on both sides. At a root of `B`, the quadratic
`H(t,x)` has at most two label roots, so local multiplicity is at most twice
that of `B`. Equality of total degrees forces

```text
sum_alpha div(H(alpha,x))=2 div(B).                 (6)
```

This is the exact complete-source saturation identity. Its regular `D_3`
incidence is the already-proved pair of `K_(2,2,2)` star graphs. Thus every
abstract geometric gate named in the statement is simultaneously realized.
Only the fixed active numerator/pencil and owner chronology remain. QED.
