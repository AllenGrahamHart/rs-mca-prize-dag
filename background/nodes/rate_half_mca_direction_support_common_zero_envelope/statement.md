# Direction-support common-zero envelope

- **status:** PROVED
- **closure:** exact one-dimensional affine-basis envelope
- **scope:** all shortened dimensions after a minimum-lift direction gauge

## Statement

Retain the direction-support affine-basis setting with transformed
explanation rank at most `r` and minimum-lift support `1<=e<=R`.  Then

```text
|Z| <= floor(max_(x=R+r..R+K)
  ((x)_(fall r+1)-(x-e)_(fall r+1))
  /((x-R+d)d_(rise r))).                              (CZ1)
```

Consequently, replacing the upper endpoint by `2R` gives one bound uniform
over every shortened dimension `r<=K<=R`.  Exact exhaustive integer
evaluation of this uniform envelope gives

```text
KoalaBear:   r=12 -> e<=31806; r=13 -> e<=870;
             r=14 -> e<=26;    r=15 -> no e>=1.
Mersenne-31: r=5  -> e<=124471; r=6 -> e<=2973;
             r=7  -> e<=83;     r=8 -> e<=2;
             r=9  -> no e>=1.
```

Every adjacent maximum in the certificate is attained uniquely first at
`x=2R=2097152`.  In particular, the Mersenne rank-five payment crosses the
puncturing boundary `e=d=67448` and removes part of the middle-support
region.

## Nonclaims

This does not prove that `x=2R` is the maximizer outside the certified
official cells, force rank or support, provide first-match ownership, or
close a deployed or prize row.

## Falsifier

A legal family exceeding `(CZ1)`, a legal zero-normal split whose fixed-`z`
maximum occurs at `c>0`, or an official scan cell exceeding a printed
maximum.
