# Direction-support affine-basis MCA payment

- **status:** PROVED
- **closure:** support-sensitive affine-incidence compiler
- **scope:** a minimum-lift gauged direction and a bounded-rank transformed
  explanation family in any shortened rate-half row

## Statement

Let the shortened row be `(R+K,K,d+K)`, choose a minimum-lift codeword
`b`, and put

```text
q=r_1-b,       e=|supp(q)|,       1<=e<=R.
```

Suppose the transformed selected explanations `c_gamma-gamma b` lie in an
affine codeword flat of dimension at most `r`, where `1<=r<=K`.  Define

```text
P(R,r,e)=1-(R+r-e)_(fall r+1)/(R+r)_(fall r+1),

M(K,r)=max(
  (R+K)_(fall r+1)/((d+K)d_(rise r)),
  (R+r)_(fall r+1)/d_(rise r+1)).
```

Then

```text
|Z| <= floor(P(R,r,e) M(K,r)).                       (AB1)
```

The support factor is strictly increasing in `e`.  For every shortened
dimension `r<=K<=R`, exact uniform payments are

```text
KoalaBear:   r=11 -> every e<=R; r=12 -> e<=15903;
             r=13 -> e<=435;     r=14 -> e<=13;
             r=15 -> no e>=1.
Mersenne-31: r=4  -> every e<=R; r=5  -> e<=62235;
             r=6  -> e<=1486;    r=7  -> e<=41;
             r=8  -> e<=1;       r=9  -> no e>=1.
```

Unlike the punctured-list payments, `(AB1)` remains valid for `e>=d`.

## Nonclaims

This does not force a small direction support or explanation rank, pay the
remaining middle-support/high-rank cells, prove first-match ownership, or
close a deployed or prize row.

## Falsifier

A legal family exceeding `(AB1)`, a full incident-normal basis supported
outside `supp(q)`, or an incorrect printed adjacent wall.
