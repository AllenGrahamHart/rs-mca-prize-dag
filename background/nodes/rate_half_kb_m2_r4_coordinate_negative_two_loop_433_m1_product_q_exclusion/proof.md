# Proof

Form the five rows `[-p,-pk,1,k]` from `(KBM1-1)` and their five `4 x 4`
minors.  After division by the nonzero label `R`, the remaining squared
weld, comparing the `BC` and `AB+` rows with the `C` loop anchor, is

```text
(1-R)^2(c^2+b)^2+4c^2R(1+b)^2=0.                 (1)
```

We cover the product map by two cases.

## Boundary: `b+R=0`

Adjoin `b+R` to the five raw minors and `M^2+1`.  Its exact lexicographic
basis contains

```text
R(R-1)(R+1)(R^3-M),
R(R-1)(R+1)(c-MR^2).                              (2)
```

The factors `R,R-1,R+1` are nonzero by label distinctness, so `(2)` proves
`(KBM1-2)`.  Substituting it into `M^2+1` gives `R^6+1=0`.  Substitution in
`(1)`, followed by reduction modulo `R^6+1`, gives

```text
-2(R^5-R+2)=0.                                   (3)
```

But

```text
Res_R(R^6+1,R^5-R+2)=4.                          (4)
```

This is nonzero in odd characteristic, deleting the boundary.

## Interior: `b+R!=0`

Normalize the denominator constant to one.  The unique Mobius map through
`F(1)=b`, `F(-1)=-b`, and `F(R)=-1` has

```text
d=(-bR-1)/(b+R),     n_0=b(-bR-1)/(b+R),     n_1=b,
F(x)=(n_1 x+n_0)/(d x+1).                        (5)
```

Cross-multiplying `F(-R)=bc` gives `-b E1=0`, and
cross-multiplying `F(M)=-c^2` gives `-E2=0`.  Since `b!=0`, these are
exactly `E1=E2=0` in `(KBM1-3)`; `(1)` is `Q=0`.

A lexicographic Groebner basis in `(c,b,R,M)` proves the first membership
in `(KBM1-4)`.  This is an exact integral-polynomial identity; the verifier
reconstructs it from `E1,E2,Q`.  In `M1`,
`b!=-1`, `R!=+/-1`, and `R^2+1!=0`.  The last condition follows because
`M^2=-1`: otherwise `R=+/-M` over the geometric closure, colliding with one
of the existing antipodal labels.  Thus `(KBM1-4)` forces `T=0`.

Adjoin `T` to the same chart equations.  A fresh exact lexicographic basis
contains `b^2(b+1)^2`, proving `(KBM1-5)`.  Since `b` and `b+1` are both
nonzero, the interior has no actual-packet point.  Together with the
boundary deletion, this proves `(KBM1-6)`. QED.
