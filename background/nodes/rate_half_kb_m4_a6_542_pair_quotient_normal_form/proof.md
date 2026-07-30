# Proof

## 1. Companion and pair curve

Let `phi=N/D` be the pinned BelyiDB map over `E=Q(nu)`, with
`nu^2-nu+4=0`. Exact factorization gives

```text
N=x^5(1902382848+67262400nu)(x-1/3-nu/6)/648626449,

D=(x^2+(2020-960nu)x/14569+(2020-960nu)/14569)
  (x^2+(68+189nu)x/422+(40-75nu)/211)^2,

N-D=(1253756399+67262400nu)
    (x-14/47-12nu/47)^4(x+4/23+9nu/46)^2/648626449.
```

Thus the letter fibers are `5.1`, `2.2.1.1`, and `4.2`.

Represent an unordered pair by `q(X)=X^2-yX+z`. Reduce `N` and `D`
modulo `q`, writing their remainders as `N0+N1X` and `D0+D1X`.
The proportionality determinant `N0D1-N1D0`, normalized at `y^5`, is the
irreducible quintic printed in the certificate.

## 2. Adjoint normalization

The pair quintic has four `E`-rational singular points. Cubic adjoints are
required to pass through those points, two regular fiber points, and the
two printed infinitely-near tangent directions. These eight independent
linear conditions have rank eight in the ten-dimensional cubic space. A
normalized basis is the certificate's `h0,h1`.

For the pencil `h0-u h1`, elimination of `z` has fixed-factor rows

```text
(1,0,1),(1,0,1),(1,0,2),(1,0,2),(1,0,4),(1,0,4)
```

and one moving factor `(1,5,1)` in `(y,u)`. Elimination of `y` has fixed
rows

```text
(1,0,1),(1,0,2),(1,0,2),(1,0,4),(1,0,5)
```

and one moving `(1,5,1)` factor in `(z,u)`. Solving these moving factors
gives the certificate's degree-five rational functions `y(u),z(u)`. Direct
common-denominator evaluation proves both the quintic equation and
`h0-u h1=0`. The single moving factor proves birationality away from the
finite base locus.

## 3. Quotient and branch fibers

On the pair curve the common remainder ratio is

```text
T=N0/D0=N1/D1.
```

Coefficient-level substitution of `y(u),z(u)` and polynomial gcd
cancellation gives `(KBM4-A1)`. Exact subtraction gives `(KBM4-A2)`. All
printed factors are squarefree and pairwise coprime in their fiber. Their
degree/exponent rows are

```text
T=0:        (1,5),(2,5),
T=1:        (1,1),(1,2),(1,4),(2,4),
T=infinity: (1,1),(2,1),(2,2),(4,2).
```

Hence the profiles are exactly `5^3`, `4^3.2.1`, and `2^6.1^3`. Their
branch indices are `12,10,6`, summing to `28=2*15-2`, so no further branch
value occurs. The companion has monodromy `A6`; its unordered-pair quotient
therefore has the retained two-subset monodromy and the stated passport.

## 4. KoalaBear descent

For `p=2130706433`, the two roots of `nu^2-nu+4` are

```text
463918232, 1666788202 mod p.
```

Under these embeddings, the monic quadratic zero factor has discriminants
`149224915` and `1898905147`, both nonzero. Its values at the root of the
linear zero factor are `1501399179` and `1964168949`, also nonzero. Thus the
zero fiber consists of three distinct points defined over at most
`F_(p^2)`. Since `2` divides `6`, all three lie in `F_(p^6)`. Replacing `T`
by `1/T` supplies the split three-point pole divisor.

No active-fiber or quartic source-star condition is asserted.
