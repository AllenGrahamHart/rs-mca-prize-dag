# Proof

The macroscopic pair floor gives

```text
|S_alpha union S_beta|>=rho+p-1.                    (1)
```

If the union is at least `rho+p`, the line cap with `j>=p` gives

```text
p h<=rho+p-1=3p-1,                                  (2)
```

so `h<=2`. The endpoint line already contains `alpha,beta`, proving the
strict branch.

Now suppose equality holds in `(1)`. Thus `j=p-1`. Substitute this value and
`h=2` into the global incidence inequality `(8)` of the macroscopic-floor
theorem. The right side minus the left side is

```text
-(e+3)/2<0,                                          (2a)
```

so `h=2` is impossible. The line cap gives `h<=3`; hence the endpoint line
has exactly the three slopes in `(ETR3)`. The same cap says

```text
3(p-1)+sum_(gamma in A)r_gamma<=3p-2,               (3)
```

which proves the deficit bound.

Every point of `U_0` is a nonzero linear residual coordinate on the endpoint
line and is therefore absent at at most one of its three slopes. The three
missing sets are disjoint. Their sizes are `p-1+r_gamma`; consequently they
cover all of `U_0` when the line deficit is one and all but one point when it
is zero.

For `delta notin A`, minimum distance gives

```text
|U union S_delta|>=2rho+1.                           (4)
```

Since `|U|=rho+p-1`, `|S_delta|=rho-r_delta`, and the fixed core belongs to
their intersection, `(4)` is equivalent to

```text
|S_delta intersect U_0|<=p-3-r_delta.               (5)
```

Define the nonnegative slack

```text
a_delta=(p-3-r_delta)-|S_delta intersect U_0|.       (6)
```

Expanding the union cardinality shows that `(6)` equals `(ETR4)`.

There are `T-3=rho+1=3e` off-line slopes. Their total capacity in `(5)` is

```text
(p-3)(T-3)-sum_(delta notin A)r_delta.               (7)
```

Their actual incidence on `U_0` is the global incidence `e|U_0|` minus the
exact incidence of the three line slopes. Using

```text
|U_0|=3p-2,
sum_(all supported delta)r_delta=e-6,                (8)
```

and the exact line missing count, subtracting the actual total from `(7)`
gives

```text
sum_(delta notin A)a_delta=e.                        (9)
```

This proves `(ETR5)`. Since the `a_delta` are nonnegative integers, at most
`e` of the `3e` off-line slopes have positive slack. At least `2e` have
`a_delta=0`, equivalently triple union exactly `2rho+1`.

Fix one such `delta` and choose an affine chart containing
`alpha,beta,delta`; this is always possible on the official field. The
coefficients in `(ETR6)` annihilate both constants and the affine slope
coordinate, so the same combination of the received words is zero.
Therefore

```text
w_delta
 =-[(beta-delta)(f_alpha-c_alpha)
    +(delta-alpha)(f_beta-c_beta)
    +(alpha-beta)(f_delta-c_delta)],                 (10)
```

and its support is contained in `U union S_delta`. The center at `delta` is
off the endpoint codeword line, so `w_delta` is nonzero. The RS minimum
distance and `|U union S_delta|=2rho+1` force equality of the support and
weight in `(ETR7)`.

A nonzero degree-`<k` RS polynomial of weight `N-(k-1)=2rho+1` has exactly
`k-1` domain zeros. It is therefore a nonzero scalar multiple of their monic
locator, proving the last assertion. QED.
