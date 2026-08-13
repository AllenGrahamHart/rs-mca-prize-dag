# Proof

## Quotient-space dimension

Extend scalars to the algebraic closure.  After clearing denominators and
taking the primitive representative, Gauss's lemma makes `P` a common
polynomial divisor of every member of `I_264`.  Put

```text
w=wdeg_(1,5,5)(P).
```

Weighted degree is additive under multiplication.  Division by the fixed
nonzero polynomial `P` therefore embeds the at-least-`938`-dimensional
kernel into the space `V_(264-w)) of polynomials of weighted degree at
most `264-w`.

For `D>=0`, the exact monomial count is

```text
M(D)=sum_(s=0)^floor(D/5) (s+1)(D-5s+1).
```

Thus `M(264-w)>=938`.  Direct evaluation at the adjacent integers gives

```text
M(46)=935 < 938 <= 990=M(47).
```

Monotonicity of `M` forces `264-w>=47`, hence `w<=217`.  Every
monomial of total `(Y,Z)`-degree `d` has weight at least `5d`, so

```text
d=deg_(Y,Z)(P) <= floor(217/5)=43.                 (WD1)
```

No irreducibility assumption was used.

## Higher-degree mass

The linear-factor router treats `d=1`.  In the complementary branch,
`2<=d<=43`.  The common-factor mass theorem gives

```text
t_d>=7583-(52-d)^2.
```

This is increasing in `d`, so its higher-degree minimum is

```text
t_2=7583-50^2=5083.                               (WD2)
```

Every captured pair has an inside core of at least `807`, and distinct
cores meet in at most five points.  The mass theorem's incidence bound at
`t=5083` is

```text
ceil(5083*807^2/(807+5*(5083-1)))=126266.          (WD3)
```

There are therefore at most `130237-126266=3971` exceptional inside
coordinates in the higher-degree branch.
