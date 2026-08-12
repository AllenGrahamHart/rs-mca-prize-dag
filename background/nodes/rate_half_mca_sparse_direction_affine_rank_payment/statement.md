# Sparse-direction affine-rank MCA payment

- **status:** PROVED
- **closure:** rank-refined punctured-list compiler
- **scope:** any shortened support-wise MCA family after a codeword gauge

## Statement

Let the shortened row be `(R+K,K,d+K)`.  Choose `b in C`, put

```text
q=r_1-b,       e=|supp(q)|,       1<=e<d,
```

and suppose the transformed selected explanations
`a_gamma=c_gamma-gamma b` have affine rank at most `r`.  Then

```text
|Z| <= e*floor(C(R-e+r,r)/C(d-e+r,r)).               (SR1)
```

The bound is independent of the ambient shortened dimension `K`.  Exact
rank/support walls for both deployed rows are pinned in the contract.  The
first residual ranks give

```text
KoalaBear transformed rank 14: e<=5 paid;
Mersenne transformed rank 6:   e<=1 paid.
```

One rank lower gives the wider payments `e<=87` and `e<=18`; one rank higher
does not pay even `e=1` by this compiler.

## Nonclaims

This does not force the transformed rank, pay support sizes beyond the table,
handle `e>=d`, or close a deployed or prize row.

## Falsifier

A family exceeding `(SR1)` while satisfying every rank/support hypothesis,
or any incorrect adjacent official wall.
