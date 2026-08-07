# Rate-half FPC5 LS6 canonical-owner packing

- **status:** PROVED
- **consumer:** `l1_fpc5_ratehalf_m4_t3_split_slice_payment`
- **upstream interface:** primitive shift-pair / split-pencil ownership

Use the determinant chart with

```text
j=2ell-a,       h=ell-2a,
H=D_0Q_H-D_HQ_0,       deg H<=h,
gcd(D_0,Q_0)=gcd(D_H,Q_H)=1.                         (CO1)
```

Assume `D_0` and `D_H` are distinct squarefree locators split on the fixed
core `C`. Define the monic canonical owner and normalized coordinates

```text
G=gcd(D_0,H),       g=deg G,
D_0=GA,             D_H=GB,       H=GK.              (CO2)
```

Then

```text
G=gcd(D_0,D_H),       0<=g<=h,                       (CO3)
gcd(G,A)=gcd(G,B)=gcd(A,B)=1,
deg A=deg B=j-g,       deg K<=h-g,
K=AQ_H-BQ_0,           gcd(K,AB)=1.                  (CO4)
```

Conversely, in the determinant chart the candidate primitive guard is
exactly

```text
gcd(K,B)=1       and       gcd(G,Q_H)=1,              (CO5)
```

because `gcd(K,A)=1` is automatic. The second condition is the shared-root
derivative guard from the determinant chart. Thus `(CO2)` is a canonical,
owner-safe decomposition rather than an arbitrary common-root rechart.

Fix one owner `G`, and let `F_G` be all non-base guarded candidates with this
owner. Put

```text
v=|C|-j,       w=j-g,       t=h-g+1.                  (CO6)
```

Every normalized candidate locator `B` is a `w`-subset of
`C\Z(D_0)`. Two distinct such locators meet in at most `h-g=t-1` roots.
Consequently

```text
|F_G| <= floor( binom(v,t) / binom(w,t) ).            (CO7)
```

For the official core size `|C|=4ell+b-2`, with `b<ell`, write
`g=h-c`. Then `(CO7)` becomes

```text
|F_G|
 <= floor( binom(2ell+a+b-2,c+1)
           / binom(ell+a+c,c+1) )
 < 3^(c+1).                                           (CO8)
```

Hence every fixed top-overlap owner chamber with bounded co-deficiency `c`
has a uniform constant payment.

## Scope

The theorem pays one fixed canonical owner. It does not bound how many
different divisors `G|D_0` occur, coalesce their charges, prove prefix
flatness, or classify quotient/dihedral owners. Summing `(CO7)` over all
possible `G` can still be exponential. The live aggregate theorem is now an
owner-coalescence or chronology-valid owner-transport statement, not a
fixed-owner split packing.
