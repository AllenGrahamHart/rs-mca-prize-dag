# Proof

Fix one row of `(SL2)` and write `R` for its polynomial ring in the base
variables. Because `G` is monic, Euclidean division by `G` is defined and
unique over every commutative `R`-algebra.

Suppose `V_t` has degree less than `w`. Its square has degree at most
`2w-2`, so there are unique polynomials `Q_t,V_(t+1)` with

```text
V_t^2=GQ_t+V_(t+1),
deg Q_t<=w-2,       deg V_(t+1)<w.                       (1)
```

These are exactly the degree bounds encoded in `(SL3)`. Coefficientwise,
the top equation in degree `2w-2` first determines the top coefficient of
`Q_t`, because the leading coefficient of `G` is one. Descending through
the degrees uniquely determines every remaining coefficient of `Q_t`; the
bottom `w` equations then uniquely determine `V_(t+1)`. Thus the recurrence
ideal is triangular over `R`, including after arbitrary base change.

Starting from `V_0=Y`, induction in the quotient ring `R[Y]/(G)` gives

```text
V_t congruent to Y^(2^t) mod G.                          (2)
```

At `t=m`, the terminal equations say exactly that the unique remainder of
`Y^(2^m)` is one. Since `N=2^m`, this is equivalent to
`G | Y^N-1`. Conversely, that divisibility forces the same terminal
remainder. The triangular uniqueness above gives mutually inverse maps on
coordinate rings, proving the scheme isomorphism and not merely a bijection
on field-valued points.

There are `mw` coefficients among the `V_t`, `m(w-1)` among the `Q_t`, and
`b` base variables. Each recurrence is an equality of polynomials of degree
at most `2w-2`, hence contributes `2w-1` coefficient equations; the terminal
condition contributes `w`. This proves the formulas and the four evaluations
in `(SL7)`.

The coefficients `g_j` have base-variable degree at most two in all four
forms in `(SL2)`. A coefficient of `V_t^2` has degree two in auxiliary
variables, a coefficient of `V_(t+1)` has degree one, and a coefficient of
`GQ_t` has degree at most three. Hence every `E_a` has total degree at most
three.

For `(SL8)--(SL10)`, the choice of `s` gives `2^s<w`. No division is needed
in the first `s` squarings, so induction gives

```text
V_t=Y^(2^t),       Q_(t-1)=0,       1<=t<=s.            (9)
```

These are constants, not variables or equations. There remain `k=m-s`
recurrences. The intermediate remainders `V_(s+1),...,V_(m-1)` contribute
`(k-1)w` variables, and the `k` quotients contribute `k(w-1)`; the final
remainder is the fixed polynomial one. This gives

```text
b+(k-1)w+k(w-1)=b+k(2w-1)-w
```

variables and `k(2w-1)` equations. Substitution of uniquely determined
variables in a triangular presentation preserves the coordinate ring, so
the pruned system is scheme-isomorphic to both `(SL4)` and `(SL6)`. The four
rows in `(SL10)` are direct substitutions. Its equations are a subset of the
same recurrence equations with constants substituted, so the cubic degree
bound is unchanged.

The three divisor-descent theorems prove that none of the four base schemes
has a point over `Qbar`. The isomorphism therefore leaves each lifted scheme
without a `Qbar`-point. Hilbert's Nullstellensatz makes its ideal the unit
ideal over `Q`; clearing denominators in a rational identity for one gives
`(SL11)` with a nonzero integer `Delta`. Reduction of that identity shows
that every supporting finite characteristic divides `Delta`. No value or
factorization of `Delta` is obtained here. QED.
