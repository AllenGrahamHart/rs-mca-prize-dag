# Proof

The three-center ledger gives

```text
sum_(delta in Gamma)a_delta=e,
sum_(delta in Gamma)r_delta=e-7.                    (1)
```

Among `3e` nonnegative integer excesses, at most `e` are positive. Hence at
least `2e` slopes have `a_delta=0`. At most `e-7` of those can have positive
padding degree, by the second equality in `(1)`. Thus at least `e+7` slopes
have `a_delta=r_delta=0`.

For such a slope, the all-excess fiber theorem gives

```text
G(delta,X)=zeta_delta A_delta(X)H_delta(X),
deg H_delta<=a_delta=0.                             (2)
```

Thus `H_delta` is a nonzero scalar, `q_delta=0`, and `A_delta` has degree
`n`. Its roots are the distinct classified actual-support rows. This proves
`(PSC2)`.

We next check absolute irreducibility. Shape A says that `G` is irreducible
over `F(X)` and has constant content, hence is irreducible over `F[t,X]`.
If it split geometrically into `s>=2` Frobenius-conjugate components, their
equal bidegrees would be `(m/s,n/s)`. Every one of the `Rm` rational
classified-grid points would lie on every conjugate. Two distinct
components, however, have projective intersection number

```text
2mn/s^2<=mn/2<Rm.                                   (3)
```

This contradicts Bezout. Therefore `G` is absolutely irreducible.

The two polynomials `G(t,X)` and `G(t,Y)` are coprime over `F(X,Y)`, so
their resultant is nonzero. On the generic separable row, each of the `m`
parameter roots gives one diagonal factor; hence `(X-Y)^m` divides the
resultant. The raw resultant has degree at most `mn` in each coordinate,
proving `(PSC3)--(PSC4)`.

Every pure split fiber supplies `n(n-1)` ordered off-diagonal pairs in
`U_0^2`. For fixed distinct rows `(x,y)`, the exact-degree polynomials
`G(t,x)` and `G(t,y)` have at most `m` common roots. Therefore the number of
distinct pair points is at least

```text
ceil((e+7)n(n-1)/m)=P_A.                            (4)
```

For a connected separable degree-`n` cover, the geometric off-diagonal
fiber-product components correspond to point-stabilizer orbits on the
other `n-1` sheets. There are at most `n-1`. Pigeonholing `(4)` gives a
component with at least

```text
ceil(P_A/(n-1))>=ceil((e+7)n/m).                    (5)
```

Finally

```text
(e+7)n/(e-2)=n+9n/(e-2),
13<9n/(e-2)<14                                      (6)
```

for `e>11`. Thus the last ceiling is `n+14`. Direct substitution of the
official `e=(2^39+1)/3` gives the integers in `(PSC5)--(PSC6)`. QED.
