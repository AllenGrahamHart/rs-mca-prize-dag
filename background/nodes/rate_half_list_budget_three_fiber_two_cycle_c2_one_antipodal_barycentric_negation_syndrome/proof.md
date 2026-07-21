# Proof

For four distinct scalars, Lagrange interpolation gives

```text
sum_i w_i^m/Phi'(w_i)=0,       0<=m<=2,
sum_i w_i^3/Phi'(w_i)=1.                         (1)
```

This proves `(BNS2)`, including nonvanishing of each weight.

The Fourier ladder with `s=2` and the first three identities in `(1)` gives
the zero range in `(BNS3)`.  To compute the endpoint, put `D=C/B`.  The
formal logarithm used in the ladder is

```text
log G_i
 =log B+sum_(m>=1)(-1)^(m+1)w_i^m z^(mH)D^m/m.      (2)
```

At degree `3H`, the weighted sums of the `log B`, `m=1`, and `m=2` terms
vanish by `(1)`.  Since `D(0)=1`, the `m=3` term and `(1)` give

```text
-1/(3H) sum_i lambda_i p_(i,3H)=1/3,
sum_i lambda_i p_(i,3H)=-H.                         (3)
```

The negation identity from the Fourier-ladder proof is

```text
sum_a u(a)a^j=(1-(-1)^j)sum_i lambda_i p_(i,j).      (4)
```

Here `H=2^37+1` is odd, so `3H` is odd.  Equations `(3)--(4)` give the
endpoint `-2H`.  The official characteristic exceeds `N`, so that scalar is
nonzero.  This proves all of `(BNS3)`.

If the support had at most `3H` points, its first that many zero moments
would form a nonsingular square Vandermonde system and force `u=0`, contrary
to the endpoint.  Hence `(BNS4)` follows.

Suppose equality holds and write `t=3H+1`.  For any monic polynomial `Psi`
of degree `t` with distinct roots, partial fractions at infinity give

```text
sum_(Psi(a)=0) a^j/Psi'(a)=0,       0<=j<t-1,
sum_(Psi(a)=0) a^(t-1)/Psi'(a)=1.                  (5)
```

The support is stable under negation because `u(-a)=-u(a)`.  It has even
size, so its monic root polynomial `Psi` is even.  The moment vector in
`(BNS3)` and the vector `-2H/Psi'(a)` have the same `t` moments by `(5)`.
The square Vandermonde matrix on the support is nonsingular, so the two
vectors agree pointwise.  This proves `(BNS6)`.  Conversely `(5)` applied to
`(BNS6)` gives exactly the displayed zero moments and endpoint. QED.
