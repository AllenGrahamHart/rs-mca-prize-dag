# Proof

The exact guard-saturated cell-14 lex basis has size eight.  Reducing the
eight common-kernel coefficients by this basis and eliminating the two
linear coordinates gives a compact plane equation with shape

```text
deg_(b,t) P=(4,8),  terms(P)=17,  lc_b(P)=t^4.     (1)
```

All normalized `A2,A0,B1` coefficients have `b`-degree at most three, and
the exact coefficient comparison gives `B1(-W)=-B1(W)`.  Hence the proved
paired-product interface supplies the two complete necessary equations
printed in `(KBC14-1)`.

Pseudo-reduction of those equations by `P` takes three and nine steps.
Their raw `w1` resultant has 179,183 terms and degrees `(16,18,672)` in
`(w0,b,t)`.  Fifteen further reductions give the 41,556-term polynomial
`R` of degrees `(16,3,752)`.  No selected factor is used: every signed pair
on the compact chart satisfies this full resultant.

Construct `D0^5`, the two factors `rd^2w0-rn^2` and `rd^2w0+rn^2`, and
the product in `(KBC14-2)`, reducing after each multiplication.  Each of
the nine reductions takes three steps, so the resulting `C` represents
the plane-leading coefficient to the 27th power times `G`.  Cross
multiplication of the leading `w0` coefficients gives the exact identity

```text
c16 R-r16 C congruent 0 (mod P).                  (2)
```

The exact norm of `r16` has degree 2752 and 1929 terms.  FLINT factors it
into eight linear factors, four irreducible cubics, one irreducible quintic,
and one irreducible sextic.  Its base-field roots are exactly

```text
0, 1, i, 33199819, 67070255, 1742551715, -i, -1. (3)
```

Specializing `gcd(P,r16)` at each root gives all deployed `b` lifts.  At
`0,1,+/-i,-1` the only lifts are `b=0,+1,-1`; at `33199819` and `67070255`
the only lift is `b=-1`.  These are explicit common localization guards.
At `t=1742551715` the two lifts are

```text
b=848523624, 1980548607.                          (4)
```

Factoring `R(w0)` at these lifts gives eight displayed base-field roots.
Every one satisfies at least one of

```text
N0=0, D0=0, w0=-1, w0=r^2, w0=-r^2.             (5)
```

The remaining factors are irreducible quadratics, so `(3)--(5)` are a
complete leading-exception atlas.

It remains to justify every division used to obtain the compact plane.
Exact factorization of the six scales shows that they depend only on `t`.
Their linear-root union is `0,+/-1,+/-i`; the only nonlinear factors are
two irreducible cubics.  These five roots are already label-collision
guards.  Independently, adjoining each specialization to the original
localized common ideal gives a reduced basis `[1]`.  Thus the compact chart
and its finite scale complement cover every admissible common point.

On the main chart away from `(3)`, a signed pair gives `R=0`; `(2)` then
gives `C=0`, hence `G=0`.  The product and denominator records make
`N0D0!=0`, while source-label distinctness excludes `w0=-1,+r^2,-r^2`.
This is impossible.  The scale ledger covers the complement, and exact
root-sign symmetry transports the representative to all four cell-14 sign
rows. QED.
