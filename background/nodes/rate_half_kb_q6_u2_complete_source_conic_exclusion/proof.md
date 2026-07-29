# Proof

The source reduction pins twelve distinct labels `alpha_i`, pairwise
pole-disjoint coordinate quadratics `z_i`, and

```text
B=product_i z_i,
M(T,X)=sum_i kappa_i L_i(T) B(X)/z_i(X).
```

Every actual outgoing component satisfies `H|M`. Specializing at `alpha_i`
therefore gives

```text
q_i=H(alpha_i,X) divides B/z_i divides B.             (1)
```

Each `q_i` is a nonzero quartic. Fix a geometric root `x` of `B`. The form
`H(T,x)` is nonzero of degree at most two in `T`, so at most two source
labels contribute at `x`. Equation `(1)` gives

```text
sum_i ord_x(q_i)<=2 ord_x(B).                         (2)
```

Both sides have total degree `48`: the left side is twelve quartics and the
right side is twice a degree-24 divisor. Thus every inequality `(2)` is an
equality, proving `(KBC-1)`.

In the conic branch the coefficient map factors through a separable
degree-two quotient by `iota`. Every `div(q_i)` is therefore
`iota`-invariant, and `(KBC-1)` makes `div(B)` invariant. At a fixed point of
`iota`, every pulled-back row divisor has even order. Local saturation then
shows that an `iota`-fixed root of `B` cannot be simple.

It remains to consume the three exhaustive reduced profiles.

## Reciprocal

Normalize the deck involution and conic involution by

```text
b(x)=-x,       iota(x)=mu/x.
```

On the deck quotient `w=x^2`, the induced involution is
`J(w)=mu^2/w`, with fixed source values `+mu,-mu`. The proved common
five-set is `J`-invariant and contains exactly `-mu`. Complete-source
invariance makes its seven-element complement invariant, so that odd set
contains the other fixed value `+mu`. Its two deck lifts satisfy `x^2=mu`:
they are the fixed points of `iota`, are not deck branch points, and hence
are simple roots of `B`. This contradicts the fixed-root parity above.

## D4

Put `g=b iota`. Here `g` has order four, with its two fixed points already
in the simple common divisor; every other orbit has length four. If `r` is
the number of selected deck branch points, then `r in {0,1,2}`, the double
stratum has size `r`, and the simple stratum has size `24-2r`. Invariance
would require

```text
r=0 mod 4,       24-2r=2 mod 4.                      (3)
```

For `r=0,1,2`, respectively, the second condition, the first condition,
and both conditions fail as recorded by the exact table; no row satisfies
both `(3)`.

## D5

Now `g` has order five and the common ten-point orbit contains neither
fixed point. For `r=0`, the simple stratum has size `24=4 mod 5` and would
need four fixed points. For `r=1`, the singleton double stratum and the
`22=2 mod 5` simple stratum need three distinct fixed points. Both exceed
the two fixed points of a nonidentity projectivity. For `r=2`, the double
points must be the two fixed points of both `g` and the deck involution `b`.
Then `iota=bg` fixes the same pair. The two involutions `b` and `iota` are
equal, forcing `g=1`, contrary to order five.

The imported reduced-profile classification is exhaustive, while its
ramified-common branches were already excluded. Hence the complete conic
image is empty. QED.
