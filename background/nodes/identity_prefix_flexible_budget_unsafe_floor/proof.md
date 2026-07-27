# Proof

Apply the identity-prefix construction to the dimension-`k+1` code
`C+=RS[F,D,k+1]`. For every `m`-subset `M` of `D`, write its monic locator as

```text
Lambda_M(X)=X^m+sum_(j=1)^m (-1)^j e_j(M) X^(m-j).
```

The first `w=m-k-1` coefficients lie in `B^w`. Pigeonholing the
`binom(n,m)` locators over these prefixes gives one fiber of size at least

```text
ceil(binom(n,m)/|B|^w).
```

The first strict inequality makes this at least `B*+1=L0`. For the common
prefix `z`, let `U_z` be the degree-`m` polynomial carrying those leading
coefficients. Then `P_M=U_z-Lambda_M` has degree at most `k`, so its evaluation
is a codeword of `C+`, and it agrees with `U_z` on all `m` points of `M`.

These codewords are distinct. Equality of two evaluations would make a
polynomial of degree at most `k<n` vanish on all of `D`. The polynomial is
therefore zero; combining its trailing-coefficient equality with the common
prefix gives equal monic locators and hence equal subsets.

Take any `L0` resulting polynomials `P_i`. For a pair `i!=j`, the equation
`P_i(alpha)=P_j(alpha)` has at most `k` solutions because `P_i-P_j` is a
nonzero polynomial of degree at most `k`. Across all pairs, fewer than

```text
binom(L0,2) k < q-n
```

points of `F\D` are forbidden. Choose `alpha in F\D` at which all values
`P_i(alpha)` are distinct. The standard simple-pole line

```text
f_alpha = U_z/(X-alpha),
g_alpha = -1/(X-alpha)
```

has slope `P_i(alpha)` explained by the dimension-`k` codeword
`(P_i(X)-P_i(alpha))/(X-alpha)` on the `m` agreement points of `P_i` and
`U_z`. Thus one received line has at least `L0=B*+1` distinct MCA-bad slopes.

Finally `(B*+1)/q > 2^-t` by the definition `B*=floor(q/2^t)`. The variant
outside `B` repeats the pair-root count on `F\B`, whose size is `q-|B|`;
the usual two-point ratio argument shows the pole line is not projectively
`B`-rational.
