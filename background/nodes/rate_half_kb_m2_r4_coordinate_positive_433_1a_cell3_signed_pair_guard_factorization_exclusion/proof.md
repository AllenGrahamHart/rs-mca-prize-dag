# Proof

The paired-product interface supplies the necessary equations

```text
N1D0+N0D1=0,
k^2w0(1-w0)^2D1^2-k^2w1(1-w1)^2D0^2-4N0D0D1^2=0. (1)
```

Here `Dj=A2(wj)`, `Nj=A0(wj)`, and the compact kernel theorem gives
`B1(W)=k(1-W)`.  Plane pseudo-reduction takes three and nine steps on the
two rows of `(1)`.  Their exact `w1` resultant has 151,031 terms and degrees
`(16,18,471)` in `(w0,b,t)`.  Fifteen further plane reductions give the
35,876-term polynomial `R` of degrees `(16,3,531)`.  Every actual main-chart
signed pair therefore satisfies `R=0`; only powers of the nonzero plane
leading coefficient were introduced.

Construct `D0^5` one multiplication at a time, reduce `rd^2w0-rn^2` and its
square, then multiply by `N0`, `w0+1`, and `w0-t^2`, reducing after every
operation that raises `b`-degree.  All eight reductions take three steps.
Thus the resulting `C` represents the plane-leading coefficient to the
24th power times

```text
G=N0D0^5(w0+1)(w0-t^2)(rd^2w0-rn^2)^2.          (2)
```

The scalar of proportionality between `R` and `C` is a function on the
plane, not an ambient polynomial scalar.  Cross multiplication of their
leading `w0` coefficients and three more plane reductions gives the exact
zero identity

```text
c16R-r16C congruent 0 (mod P).                    (3)
```

The exact norm of `r16` has degree 2104 and 2101 terms.  FLINT factors it
into ten linear factors, three irreducible quadratics, and three irreducible
cubics.  Its base-field root set is exactly

```text
0, 1, i, 33199819, 67070255, 253393149, 486122301,
1288361599, -i, -1.                               (4)
```

The exceptional-scale dependency has already replayed and excluded
`0,+/-1,+/-i,1288361599` from the original common and signed equations.
For each of the other four roots, specialize `P` and `r16`, factor their gcd
in `b`, and retain only linear factors.  At `33199819` and `67070255`, the
only deployed lift is `b=-1`; the common localization explicitly inverts
`b+1`.  At `253393149` and `486122301`, there are two deployed `b` lifts
each.  Exact factorization of the specialized `R(w0)` gives only linear
roots, and every root is recorded with at least one of

```text
N0=0, D0=0, w0=-1, w0=t^2, w0=r^2.               (5)
```

Thus no admissible leading exception survives.

At every other main-chart point, `r16!=0`.  If a signed pair existed, then
`R=0`; equation `(3)` would imply `C=0`, and the nonzero plane-leading scale
in `(2)` would imply `G=0`.  The outside product record and rational-map
guards give `N0D0!=0`; distinct source deck pairs exclude `w0=-1`, `t^2`,
and `r^2`.  This contradicts `(2)`.

The exceptional-scale theorem handles the complement of the compact chart.
The common root-sign quotient transports equations and guards from cell 3
to all four sign rows and duplicate-role cell 6.  All eight rows of `[3,6]`
are therefore excluded. QED.
