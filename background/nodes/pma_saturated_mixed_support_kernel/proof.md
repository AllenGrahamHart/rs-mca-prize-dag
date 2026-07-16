# Proof - pma saturated mixed-support kernel

## 1. Exact interpolation kernel

Let `V_d` be the `(d+1)`-dimensional space of polynomials of degree at most
`d`. Evaluation on the `s` distinct points of `X`, multiplication by the
fixed label function `alpha`, interpolation in degree `<s`, and projection
to coefficients in degrees `d+1,...,s-1` are all linear. Their composition
is `T_(X,d)`.

Suppose `deg F,deg W<=d` and

```text
W(x)=alpha(x)F(x)       for every x in X.
```

Because `d<s`, both `W` and `I_X(alpha F)` have degree `<s` and agree at all
`s` points. They are equal. In particular the top coefficients vanish, so
`F in ker T_(X,d)`. Conversely, if `F` is in the kernel, then
`W=I_X(alpha F)` has degree at most `d` and satisfies the displayed
relations by construction. The target has one coordinate for every degree
from `d+1` through `s-1`, hence dimension

```text
s-d-1=ell+lambda-1.
```

Split monicity, root location, exact nonvanishing, and absence of extra
agreements are additional guards on this exact linear parametrization.

## 2. Largest-class rank bound

Choose a largest label class `Y=X_*`, with label `c_*` and size `a_*`.
For `F in ker T_(X,d)`, write `W_F=I_X(alpha F)`. The polynomial
`W_F-c_*F` vanishes on `Y`, so

```text
Phi(F)=(W_F-c_*F)/L_Y
```

is a polynomial of degree at most `d-a_*`. This defines a linear map

```text
Phi:ker T_(X,d) -> V_(d-a_*).
```

The target has dimension `d-a_*+1`. If `F` lies in `ker Phi`, then
`W_F=c_*F`. At each point of `X\Y`, its label differs from `c_*`, and the
interpolation relation gives

```text
(alpha(x)-c_*)F(x)=0.
```

Thus `F` vanishes on all `s-a_*` points of `X\Y`. The PMA bounds
`a_*<=ell` and `s=d+ell+lambda` imply `s-a_*>=d`.

- If `s-a_*>d`, then `F=0`, so `Phi` is injective.
- If `s-a_*=d`, then `F` is a scalar multiple of `L_(X\Y)`, so
  `dim ker Phi<=1`.

It follows that

```text
dim ker T_(X,d) <= d-a_*+1                  if s-a_*>d,
dim ker T_(X,d) <= d-a_*+2                  if s-a_*=d.
```

Subtracting from `dim V_d=d+1` proves respectively

```text
rank T_(X,d)>=a_*,
rank T_(X,d)>=a_*-1.
```

In the second case, `a_*=ell+lambda`. Since `a_*<=ell`, this forces
`lambda=0` and `a_*=ell`. The background class has size `<ell`, so in PMA
the exceptional largest class is a full petal.

## 3. Exact-defect saturation

For an actual PMA codeword, the core-defect normal form is

```text
P=Q+L_(C\D)W,       F=L_D.
```

At every `x in D`, the factor `L_(C\D)(x)` is nonzero. If `W(x)=0`, then
`P(x)=Q(x)`, contradicting that `D` is the exact missed-core set. Hence `W`
is nonzero at every root of the squarefree split polynomial `F`, and

```text
gcd(F,W)=1.
```

For a touched label `c_j`, put `B_j=W-c_jF`. Then
`gcd(F,B_j)=gcd(F,W)=1`. If `i!=j`, every common divisor of `B_i` and
`B_j` divides

```text
B_i-B_j=(c_j-c_i)F.
```

The labels are distinct and `B_i` is coprime to `F`, so
`gcd(B_i,B_j)=1`. In the nonplanted residual these fiber polynomials are
nonzero.

Finally, suppose a larger displayed defect is obtained from disjoint split
core factors by

```text
F=L_E F_0,       W=L_E W_0,       D=D_0 disjoint_union E.
```

Then

```text
L_(C\D)W
 =L_(C\(D_0 disjoint_union E))L_EW_0
 =L_(C\D_0)W_0.
```

It is the same codeword represented with the smaller defect `D_0`; moreover
`W` vanishes on `E`, so `D` was not exact. Exact-defect enumeration therefore
removes every principal common-factor component. The surviving counting
object is a normalized reduced split-denominator pencil, not all vectors in
the ambient interpolation kernel.

## 4. Dual Reed-Solomon and Hankel form

Let

```text
L_X(Z)=prod_(x in X)(Z-x)
```

and, for values `y=(y_x)_(x in X)`, define

```text
M_j(y)=sum_(x in X) x^j y_x/L_X'(x).
```

The coefficient of `Z^(s-1)` in the degree-`<s` interpolant of the values
`x^j y_x` is exactly `M_j(y)`, by the Lagrange interpolation formula. We use
the following dual Reed-Solomon criterion:

```text
deg I_X(y)<=r
iff
M_j(y)=0 for 0<=j<=s-r-2.
```

For the forward direction, `Z^j I_X(y)` has degree at most `s-2` throughout
the displayed range, so its top Lagrange coefficient vanishes. Conversely,
write `I_X(y)=sum b_t Z^t`. The equation `M_0=0` gives `b_(s-1)=0`.
Inductively, once `b_(s-1),...,b_(s-j)` vanish, `Z^j I_X(y)` has degree at
most `s-1` and its top coefficient is `b_(s-1-j)`. Thus the stated moments
successively kill every coefficient above degree `r`.

Put `w=s-d-1` and

```text
mu_m=sum_(x in X) alpha(x)x^m/L_X'(x).
```

If `F=sum_(t=0)^d f_t Z^t`, the dual criterion gives

```text
F in ker T_(X,d)
iff
sum_(t=0)^d mu_(j+t)f_t=0,       0<=j<w.
```

Hence `T_(X,d)` has the same kernel and rank as the Hankel matrix

```text
H_(j,t)=mu_(j+t),       0<=j<w, 0<=t<=d.
```

There is also a useful exact interpretation of row-rank defect. If the rows
of `H` are dependent, choose nonzero `q_0,...,q_(w-1)` in its left kernel and
put `Q(Z)=sum q_j Z^j`. The left-kernel equations say that the first `d+1`
moments of the values `alpha Q` vanish. Applying the dual criterion with
`r=w-1` produces a polynomial `A` of degree at most `w-1` such that

```text
A(x)=alpha(x)Q(x)       for every x in X.
```

The converse follows by reversing the same argument. Thus a row defect is
equivalent to a second low-degree rational representation of the labels.

## 5. Maximal rank for an exact saturated pair

Assume now that the kernel contains the actual exact pair `(F,W)`, where
`deg F=d` and `gcd(F,W)=1` by Section 3.

First suppose `d<w`. For any `G in ker T_(X,d)`, let
`B=I_X(alpha G)`, so `deg B<=d`. The polynomial

```text
WG-BF
```

vanishes on all `s=d+w+1` points of `X` and has degree at most `2d`.
Because `w>d`, one has `s>=2d+2`, so the polynomial is zero. Coprimality of
`F` and `W` then implies `F` divides `G`. Since `deg G<=d=deg F`, the kernel
is exactly the line spanned by `F`, and `rank T_(X,d)=d`.

Now suppose `d>=w`. If the row rank were less than `w`, Section 4 would give
nonzero `Q` and a polynomial `A`, both of degree at most `w-1`, satisfying
`A=alpha Q` on `X`. Then

```text
WQ-AF
```

vanishes on `X` and has degree at most `d+w-1=s-2`, so it is identically
zero. Thus `F` divides `WQ`. Since `gcd(F,W)=1`, it follows that `F` divides
`Q`, impossible because `deg F=d>=w>deg Q`. Therefore the `w` rows are
independent. In both cases,

```text
rank T_(X,d)=min(d,w).
```

The exact-defect coprimality is load-bearing. Without it, multiplying a
lower-degree rational representation by a common split factor creates a
larger kernel and the maximal-rank conclusion can fail.

## 6. Canonical core-root pinning

Let `K=ker T_(X,d)` and

```text
m=dim K=d+1-min(d,w).
```

Fix the ordered source core `C`. For any monic degree-`d` split locator
`F=L_D in K`, with `D subset C`, consider

```text
K_D={G in K:G(x)=0 for every x in D}.
```

A degree-at-most-`d` polynomial vanishing on the `d` distinct points of `D`
is a scalar multiple of `L_D`. Hence `K_D=span(F)`. The evaluation
functionals at the points of `D` therefore have rank `m-1` on `K`. Choose,
in the fixed core order, the lexicographically first subset
`R(F) subset D` of size `m-1` whose evaluations already cut `K` down to
`span(F)`.

This assignment is injective on monic locators. If `R(F_1)=R(F_2)`, the
common vanishing subspace is both `span(F_1)` and `span(F_2)`. The locators
are therefore scalar multiples, and monicity makes them equal. Consequently

```text
# {L_D in K:D subset C, |D|=d}
 <= binom(|C|,m-1)
 =  binom(k-1,max(0,d-w)).
```

This solves the locator count for one exact labelled support in terms of a
canonical binomial charge. It does not sum the support patterns, and the
charge can still be exponential when `d-w` is large. Those are profile and
first-match aggregation obligations of the consumer.
