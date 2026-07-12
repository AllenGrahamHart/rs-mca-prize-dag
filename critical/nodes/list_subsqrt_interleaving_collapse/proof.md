# Proof of sub-square-root interleaving collapse

Fix `a` and abbreviate the worst ordinary list size by `L`. The case `m=1`
is immediate, so assume `m>=2`.

## Diagonal lower bound

Choose a received word `u` whose ordinary list has size `L`. Against the
interleaved received word `(u,...,u)`, the diagonal tuples `(c,...,c)` for
those `L` codewords have the same agreement support as `c` against `u`.
Hence `L_m>=L`.

## Projection collision bound

Fix an arbitrary interleaved received word `U=(u_1,...,u_m)`, and let `X` be
its common-support list at agreement `a`; put `N=|X|`. For every
`alpha=(alpha_2,...,alpha_m) in F^(m-1)`, define

```text
Phi_alpha(c_1,...,c_m) = c_1 + sum_(i=2)^m alpha_i c_i.
```

Linearity puts `Phi_alpha(x)` in `C`. If `x` agrees with `U` on a common set
of at least `a` coordinates, then `Phi_alpha(x)` agrees on that set with

```text
u_1 + sum_(i=2)^m alpha_i u_i.
```

Therefore `Phi_alpha(X)` has at most `L` elements. If its fiber sizes are
`n_y`, Cauchy-Schwarz gives at least

```text
sum_y binom(n_y,2) >= (N^2/L-N)/2                         (1)
```

unordered colliding pairs for every `alpha`.

Now fix distinct `x,x' in X` and write `d_i=c_i-c'_i`. The collision equation
is

```text
d_1 + sum_(i=2)^m alpha_i d_i = 0                         (2)
```

in `F^n`. If some `d_j` with `j>=2` is nonzero, then after fixing all other
coefficients, (2) has at most one value of `alpha_j`: scalar multiplication
by the nonzero vector `d_j` is injective. Thus the pair collides for at most
`q^(m-2)` choices of `alpha`. If every `d_j=0` for `j>=2`, then `d_1` is
nonzero and the pair never collides.

Summing (1) over all `q^(m-1)` projections and then counting by pairs gives

```text
q^(m-1)(N^2/L-N)/2 <= binom(N,2) q^(m-2).
```

For `N>0`, cancellation and rearrangement yield

```text
N <= L(q-1)/(q-L).
```

Taking the integer floor and then maximizing over `U` proves the upper bound.

Finally,

```text
L(q-1)/(q-L) - L = L(L-1)/(q-L) < 1
```

exactly when `L^2<q`. In that case the integral upper bound is at most `L`,
and the diagonal lower bound gives `L_m=L`.

## Prize specialization

At a safe base-list agreement let

```text
B* = floor(q/2^128),   L <= B*.
```

For an official field `q<2^256`,

```text
(B*)^2 <= q^2/2^256 < q.
```

Consequently every interleaving arity has exactly the same worst list size as
the base code at that agreement. At an unsafe base agreement, diagonal tuples
preserve every base witness, so every arity is unsafe there as well.
