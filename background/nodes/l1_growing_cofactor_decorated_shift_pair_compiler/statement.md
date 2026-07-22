# L1 growing-cofactor decorated shift-pair compiler

- **status:** PROVED
- **role:** compile the collective growing-cofactor shell into an exact second moment
- **consumer:** `l1_mixed_petal_amplification`

## Exact pair record

Normalize `U` modulo degree-below-`k` codewords, let `h=deg U`, and fix an
exact shell size `a<=h`. Put

```text
w=a-k,       e=h-a.
```

For two distinct shell codewords `P_1,P_2`, let their exact agreement sets be
`S_1,S_2` and write the domain partition locators as

```text
G=L_(S_1 intersect S_2),
A=L_(S_1\S_2),       B=L_(S_2\S_1),
N=L_(H\(S_1 union S_2)).                              (DS1)
```

Put `g=deg G` and `d=deg A=deg B=a-g`. The exact shell factorizations are

```text
U-P_1=GAQ_1,       U-P_2=GBQ_2,                       (DS2)
```

where both cofactors have degree `e` and leading coefficient `lc(U)`. Then

```text
Omega=GABN,
g<=k-1,       d>=w+1,
R:=AQ_1-BQ_2 != 0,       deg R<=d-w-1,                (DS3)
gcd(Q_1,BN)=gcd(Q_2,AN)=1.                            (DS4)
```

Moreover

```text
P_2-P_1=GR.                                            (DS5)
```

Conversely, a record satisfying `(DS1)--(DS4)` and
`deg(U-GAQ_1)<k` reconstructs the ordered pair by `(DS2)`; the second
low-degree condition follows from `(DS5)`, and `(DS4)` gives exactness. Thus
if `Z_a(U)` is the number of exact-shell members, the number of ordered valid
records is exactly

```text
Z_a(U)(Z_a(U)-1).                                      (DS6)
```

## Scalar-cofactor identification

At `e=0`, `Q_1=Q_2=lc(U)` and `(DS3)` becomes

```text
deg(A-B)<=d-w-1.                                      (DS7)
```

This is exactly the locator-Q shift-pair / exact second-moment record: two
degree-`a` support locators share `G`, and their disjoint degree-`d` tails have
the same first `w` coefficients.

## Primitive decoration uniqueness

Call a decorated record cofactor-primitive when

```text
gcd(Q_1,Q_2)=1.                                       (DS8)
```

Fix the ordered split pair `(A,B)`, the degrees `(d,e,w)`, and the common
nonzero leading coefficient of `Q_1,Q_2`. If `e<=w`, there is at most one
cofactor-primitive pair `(Q_1,Q_2)` satisfying `(DS3)`.

Indeed, for two such pairs with residuals `R,R'`, cross multiplication gives

```text
A(Q_1Q'_2-Q'_1Q_2)=RQ'_2-R'Q_2.                      (DS9)
```

The right side has degree at most `d-w-1+e<d`, so it vanishes. Coprimality,
equal degrees, and the fixed leading coefficients force the two pairs to be
equal.

If `D=gcd(Q_1,Q_2)` is nonconstant, then `D|R`, and `(DS4)` gives

```text
gcd(D,ABN)=1.                                         (DS10)
```

Thus every domain root of `D` lies in the common agreement core `G`; all
other factors are off-domain common cofactors. This is an explicit
common-factor/tangency branch, not primitive multiplicity.

## Consequence

For `e<=w`, the primitive growing-cofactor second moment has no hidden
`q^(2e)` decoration multiplier once `(A,B)` is fixed. Its remaining cost is
the split support-pair census. The nonprimitive common-cofactor branch and the
high-cofactor range `e>w` remain unpaid.

This compiler proves no second-moment bound.
