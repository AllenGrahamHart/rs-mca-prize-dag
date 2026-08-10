# Proof

For distinct points `W` of size `a`, the barycentric identity says

```text
sum_(x in W) f(x)/sigma'_W(x)=0       when deg f<=a-2. (1)
```

If `q_j(X)` has degree at most `rho`, apply `(1)` to `X^i q_j(X)` for
`0<=i<a-rho-1`. This gives

```text
sum_(x in W) x^i q_j(x)/sigma'_W(x)=0.                (2)
```

Substituting

```text
q_j(x)=sum_(t=0)^Delta_x r_(x,t)[Y^j](A_x(Y)Y^t)
```

turns `(2)` exactly into `E_W r=0`.

Conversely, the evaluation code on `W` of polynomials of degree at most
`rho` has dimension `min(a,rho+1)`. When `a>rho+1`, the rows in `(2)` are
the `a-rho-1` independent checks of its dual generalized Reed-Solomon code.
Their common kernel is therefore exactly that evaluation code. When
`a<=rho+1`, ordinary interpolation already extends every value vector with
degree at most `a-1<=rho`, and `E_W` correctly has no rows. This proves the
equivalence `(LEK3)` coefficient by coefficient.

An actual locator curve has

```text
Q_Y(X)=sum_(j=0)^m q_j(X)Y^j,       deg_X q_j<=rho.
```

The deficiency-aware factorization gives `(LEK1)` on `W`, so its nonzero
coordinate-block vector `r` satisfies `E_W r=0`. It already satisfies
`M_W r=0` by `(DCK5)`, hence lies in the kernel of `C_W`. Full column rank
therefore excludes an actual failure. QED.
