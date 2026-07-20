# Proof

Work first over the polynomial ring in the `d` nonleading coefficients of
`T` and in `c`. The divisor `F=YT^2-c` is monic of degree `h`.

If `V_t` has degree less than `h`, monic Euclidean division uniquely gives

```text
V_t^2=FQ_t+V_(t+1),
deg Q_t<=h-2,       deg V_(t+1)<h.                    (1)
```

Coefficient comparison from degree `2h-2` downward first determines every
coefficient of `Q_t`, because the leading coefficient of `F` is one, and
then determines `V_(t+1)`. This triangular determination is valid after
arbitrary base change. Starting from `V_0=Y`, induction gives

```text
V_t congruent to Y^(2^t) mod F.                       (2)
```

Since `N=2^m`, the terminal equation `V_m=1` is equivalent to
`F | Y^N-1`. The unique recurrence variables give mutually inverse maps on
coordinate rings, proving the scheme isomorphism.

There are `b=d+1` base variables. In the pruned presentation, the
`k-1` intermediate remainders contribute `(k-1)h` variables and the `k`
quotients contribute `k(h-1)`. Thus

```text
b+(k-1)h+k(h-1)=b+k(2h-1)-h.                         (3)
```

Each of the `k` polynomial identities has degree at most `2h-2` and hence
gives `2h-1` coefficient equations. The coefficients of `F` have base
degree at most two. Therefore `V_t^2` has variable degree two, `V_(t+1)`
degree one, and `FQ_t` degree at most three. This proves `(SLC4)`.

The choice `s_0=floor(log_2(h-1))` gives `2^s_0<h`. No reduction occurs in
the first `s_0` squarings, so those remainders are the fixed monomials
`Y^(2^t)` and their quotients are zero. Removing uniquely determined
variables preserves the coordinate ring. Substitution of
`(m,h)=(12,5),(12,7),(12,9)` proves `(SLC5)`.

It remains to prove characteristic-zero emptiness. Suppose over an
algebraically closed characteristic-zero field that

```text
F(Y)=YT(Y)^2-c divides Y^N-1.                         (4)
```

The binomial is squarefree, so `F` has `h` distinct roots `Y_0 subset mu_N`.
Its nonzero constant gives `c!=0`; because `h` is odd, comparison with the
root product gives `c=prod_(y in Y_0)y`, hence `c in mu_N`. Choose
`a in mu_(2N)` with `a^2=c`. Then

```text
F(X^2)=(XT(X^2)-a)(XT(X^2)+a).                       (5)
```

Moreover `F(X^2)` divides `X^(2N)-1`. The latter is squarefree, so both
coprime factors in `(5)` split into distinct roots in `mu_(2N)`. Let `P` be
the `h` roots of the first factor. Its `X^(h-1)` coefficient is zero, so

```text
sum_(x in P)x=0.                                     (6)
```

This is impossible for an odd number of `2N`th roots of unity. For
completeness, work over the complex numbers, choose a primitive `2N`th root
`zeta`, and let
`R(Z)=sum_(x=zeta^e in P) Z^e`, with `deg R<2N`. Equation `(6)` makes
`Z^N+1`, the minimal polynomial of `zeta` over `Q`, divide `R`. Writing
`R=(Z^N+1)Q` with `deg Q<N` pairs every nonzero
coefficient at exponents `e` and `e+N`; because the coefficients of `R` are
zero or one, its weight is even, a contradiction.

Thus the divisor scheme has no point over `Qbar`. The scheme isomorphism
gives the same conclusion for the pruned recurrence ideal. Hilbert's
Nullstellensatz makes that ideal the unit ideal over `Q`; clearing
denominators in an identity for one proves `(SLC6)` with
`Delta_(N,h)!=0`. Reduction modulo a finite characteristic proves that every
solution characteristic divides the certified integer. QED.
