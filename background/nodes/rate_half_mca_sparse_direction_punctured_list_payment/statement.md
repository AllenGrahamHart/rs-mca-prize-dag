# Sparse-direction punctured-list MCA payment

- **status:** PROVED
- **closure:** field-general reduction and exact deployed boundary
- **scope:** one shortened support-wise MCA-bad family

## Statement

Let `C=RS[F,D,s]` have length `N=R+s`, let `m=d+s`, and let
`r_gamma=r_0+gamma r_1`.  Suppose the direction has a codeword
approximation

```text
r_1=b+q,       b in C,       E=supp(q),       |E|=e,
```

with `1<=e<d`.  If every counted slope has an exact size-`m`
pair-noncontained agreement witness, then

```text
|Z| <= e*floor(C(R-e+s,s)/C(d-e+s,s)).               (SP1)
```

At the first dimension not paid for every direction, `(SP1)` pays

```text
KoalaBear s=14:   e<=5, equivalently j=R-e>=1048571;
Mersenne s=6:     e<=1, equivalently j>=1048575.
```

The exact last-paid and first-unpaid values are pinned in the contract.

## Nonclaims

This does not pay `e>=d`, the middle direction-defect interval, later
dimensions at the displayed boundary, an external first-match atlas, or a
full deployed or prize row.

## Falsifier

A legal family exceeding `(SP1)`, more than `e` slopes assigned to one
punctured codeword, or an incorrect official boundary.
