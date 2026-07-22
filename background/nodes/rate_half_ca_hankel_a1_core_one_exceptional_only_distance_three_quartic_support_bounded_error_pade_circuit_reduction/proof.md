# Proof

The two row root sets are subsets of the roots of the squarefree polynomial
`P_Z`. Their monic gcd `g_u` is squarefree, so `(QPCIR1)` is the complement
of their union and is a squarefree divisor of `P_Z`.

At an internal slope `xi_i`, multiply the two pair-Lagrange specializations.
Factoring the product of all exceptional locators into their involution norms
gives one nonzero scalar function `chi(u)`, independent of `i`, such that

```text
[P_Z/(Q_xQ_tau(x))](xi_i)
 =chi(u)mu_iN_i(u).                                 (1)
```

For a good pair `N_i(U)=(U-u_i)^2`; the at-most-`t` tail norms are arbitrary
nonzero quadratics. Their three coefficient interpolants are exactly
`M_0,M_1,M_2` in the statement.

Multiplication by `g_u(xi_i)` shows that `K_u` and the second term in
`(QPCIR2)` agree at every root of `I`. Their difference is divisible by
`I`. Its degree is at most `e+d_u`, so the quotient `A_u` has degree at most
`d_u<=t`. This proves `(QPCIR2)`.

Let `S` be a set of `s=2(t+1)` roots of `K_u`. Evaluation of `(QPCIR2)` at
`gamma in S` and division by the nonzero `I(gamma)` gives

```text
A_u(gamma)+chi(u)g_u(gamma)q_gamma(u)=0.            (2)
```

Pad the coefficient vectors of `A_u` and `chi(u)g_u` through degree `t`.
They form a nonzero right-kernel vector for the matrix in `(QPCIR4)`, so its
determinant vanishes at `u`. Every determinant term uses all `t+1` columns
containing `q_gamma(U)`, and each such entry is quadratic in `U`. Hence
`deg Delta_S<=2(t+1)`. A determinant which is not the zero polynomial has at
most that many field roots.

Each complement contains `e+d_u>=e` roots, so every orbit coordinate
contributes at least `binom(e,s)` incidences `(u,S)`. An identically zero
determinant contributes at most all `N` coordinates; every other determinant
contributes at most `2(t+1)`. Summing over all `binom(3e,s)` subsets proves
`(QPCIR5)`.

It remains to justify the outside-orbit count. The complement of the
`6e+3` active outside rows consists of the `2e` exceptional roots and five
boundary/omitted rows. Of the exceptional pairs, `e-t` are full nonfixed
involution-orbits. After removing them, only `2t+5` points can create
crossing orbits. The antipodal involution has no fixed subgroup point, so
there are at least `3e-t-1` full outside orbits. The constant-product
involution has at most two fixed points, giving at least `3e-t-2`. Removing
the at-most-one identical-row orbit proves `(QPCIR6)`.

Finally solve `(QPCIR5)` for `D_t`:

```text
D_t >=
 [N binom(e,s)-2(t+1)binom(3e,s)]/[N-2(t+1)].       (3)
```

Exact integer substitution of `(QPCIR6)` proves the strict rational bounds
in `(QPCIR7)`. QED.
