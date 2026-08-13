# Proof

For a fixed clone coordinate `x`, both `F_x` and `F_*` have bidegree at most
`(1,1)`. Since the latter is irreducible and divides the former, and `F_x`
is nonzero, they differ by a scalar `lambda_x`. Comparing the four
coefficients gives

```text
A_0-Q_0r_0 = lambda_x a,    B_0-Q_0r_1 = lambda_x b,
A_1-Q_1r_0 = lambda_x c,    B_1-Q_1r_1 = lambda_x d              (1)
```

at `x`.

The determinant condition `Delta=ad-bc != 0` is equivalent to
irreducibility of the bidegree-`(1,1)` form. It also makes `F_*=0` the graph
of a projective Mobius isomorphism. Substituting

```text
(c+d gamma)tau=-(a+b gamma)
```

in the owner triple gives exactly `Qhat,Nhat`. Substituting (1), or simply
using that every `F_x` vanishes identically on the common component, proves
`(LC1)`. The displayed degree bounds follow directly from the formulas.

Now suppose `span(q_0,q_1)` has dimension one. Homogeneously in the slope
coordinates, there are a nonzero linear form `ell` and a nonzero polynomial
`Q_*` such that

```text
Qhat=ell Q_*.
```

At the unique projective zero `gamma_0` of `ell`, `(LC1)` gives

```text
Nhat(gamma_0,x)=0                  for every x in C.    (2)
```

The left side is a polynomial in `X` of degree at most `m`. If `c>=m+1`,
root counting forces it to be the zero polynomial. A homogeneous quadratic
in the slope variables which vanishes at the zero of `ell` is divisible by
`ell`; hence

```text
Nhat=ell(A_*+gamma B_*).
```

Cancelling the common slope factor leaves a denominator independent of the
slope and a numerator affine in the slope. At every rational point of the
original owner pencil, the denominator is a nonzero scalar multiple of
`Q_*`; therefore `Q_*` is root-free on the domain whenever the source atom
is root-free. An exact size-`m` support and the degree profile

```text
deg Q_*<=m-k,       deg A_*,deg B_*<=m
```

then recover the usual coherent scalar-locator certificate: the polynomial
`A_*+gamma B_*-Q_*h_gamma` has degree at most `m`, vanishes at the `m`
support points, and is therefore an affine-in-`gamma` scalar multiple of
the monic support locator. If that affine scalar is identically zero, two
slopes force `A_*` and `B_*` to be divisible by `Q_*`, giving the globally
affine codeword-line degeneration. Otherwise this is one rational atom.
Thus every rational point is assigned to the same owner or the stronger
affine branch. At `gamma_0` the pulled-back denominator is the zero
polynomial, so that one projective parameter is a pure-locator/degenerate
point rather than a rational owner.

If `c=m`, equation (2) and the same degree bound say precisely

```text
Nhat(gamma_0,X)=mu Lambda_C(X)
```

for a unique scalar `mu`, including `mu=0`. The zero case repeats the
cancellation proof. The nonzero case is `(LC2)` and cannot be cancelled by
`ell`. These cases are exhaustive. QED.
