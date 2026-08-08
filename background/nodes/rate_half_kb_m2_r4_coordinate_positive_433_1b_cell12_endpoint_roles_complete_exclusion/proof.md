# Proof

Write the common kernel as polynomials `A(x),B(x)` and the linear square-root
polynomial `beta(x)`.  At the missing source label `x=-t^2`, put

```text
m = B(x)/A(x),        S = x beta(x)^2/A(x)^2.
```

The parent leading-open theorem makes `A(x)` a unit on the generic chart.  If
the missing record is `BF` or `sigma_c CF`, elimination of `f` gives the
necessary source equation

```text
(u^2+m)^2 - S u^2 = 0,       u=b or c.             (EP-1)
```

For each of four source-sign lanes, saturating the eight common-locus
equations by all source guards and adjoining `(EP-1)` gives a nonunit
zero-dimensional ideal.  Exact lex elimination gives one `r` eliminant: its
degree is 29 for `u=b` and 21 for `u=c`.  Factoring these eliminants over the
deployed field and replaying the proved triangular common-locus tower is
complete for deployed points.  It leaves four generic `b` points and six
generic `c` points per source-sign lane, hence 16 and 24 points respectively.
No replayed point lies on an unhandled route or tower boundary.

Fix one surviving point and one target lane.  Equation `(EP-1)` fixes `f` as

```text
f=m/b                 for BF,
f=sigma_c m/c         for sigma_c CF.
```

The only target variables left are `d,e`.  For each of the 15 perfect
matchings of the six residual records, substitute the six products into the
three exact pair-resultant equations supplied by the common kernel and
saturate by the full target guard.  The Cartesian total is

```text
(16+24) source points * 4 target lanes * 15 matchings = 2400.
```

The primary Singular computation obtains the unit ideal in every system.  An
independently written SymPy lex computation, initially without target-guard
saturation, also obtains the unit ideal in all 2400 systems.  Thus there is
not even an unguarded algebraic-closure residual solution.

The parent rational-boundary theorem already excludes all outside roles at
the eight deployed leading-boundary points.  Generic and boundary pieces are
therefore both empty for the two endpoint roles. QED.
